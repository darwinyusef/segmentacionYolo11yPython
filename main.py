# pip install ultralytics

import cv2
import time
import numpy as np
from ultralytics import YOLO


# Cargar el modelo YOLOv11 para segmentación (o de tener descargado 'yolo11n-seg.pt')
model = YOLO("yolo11n-seg")

# Definir la fuente de video (puede ser una ruta o un índice de cámara)
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Medir el tiempo de procesamiento para calcular la latencia
    start_time = time.time()
    
    # Realizar la detección y segmentación en el frame
    results = model(
        frame, 
        conf=0.7,
        classes=[0]
        )
    latency = (time.time() - start_time) * 1000  # Latencia en milisegundos

    # Acceder a las detecciones (bounding boxes)
    boxes_obj = results[0].boxes
    if boxes_obj is not None and len(boxes_obj) > 0:
        bboxes = boxes_obj.xyxy.cpu().numpy()   # [x1, y1, x2, y2]
        confs = boxes_obj.conf.cpu().numpy()      # Puntajes de confianza
        classes = boxes_obj.cls.cpu().numpy()     # Índices de clase
        
        for i, box in enumerate(bboxes):
            x1, y1, x2, y2 = map(int, box)
            # Obtener el nombre de la clase si existe
            class_name = model.names[int(classes[i])] if hasattr(model, 'names') else str(int(classes[i]))
            label = f'{class_name} {confs[i]:.2f}'
            # Dibujar bounding box y etiqueta en el frame
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Procesar las segmentaciones: asignar un color aleatorio a cada máscara detectada
    masks_obj = results[0].masks
    if masks_obj is not None and len(masks_obj) > 0:
        # Extraer las máscaras; se asume que masks_obj.data es un tensor
        masks = masks_obj.data.cpu().numpy() if hasattr(masks_obj.data, 'cpu') else masks_obj.data
        for mask in masks:
            # Convertir la máscara a binaria (umbral 0.5) y escalándola a 0-255
            mask_bin = (mask > 0.5).astype(np.uint8) * 255
            # Redimensionar la máscara para que tenga el mismo tamaño que el frame
            mask_bin = cv2.resize(mask_bin, (frame.shape[1], frame.shape[0]), interpolation=cv2.INTER_NEAREST)
            
            # Crear una máscara booleana de 3 canales
            binary_mask = cv2.threshold(mask_bin, 127, 255, cv2.THRESH_BINARY)[1]
            binary_mask_3c = cv2.merge([binary_mask, binary_mask, binary_mask])
            
            # Generar un color aleatorio (BGR)
            random_color = np.random.randint(0, 256, size=(3,), dtype=np.uint8)
            # Crear una imagen del mismo tamaño que el frame, rellenada con el color aleatorio
            colored_mask = np.full((frame.shape[0], frame.shape[1], 3), random_color, dtype=np.uint8)
            
            # Combinar la máscara con el frame: en las regiones donde la máscara es 255, se usa el color aleatorio
            output_frame = frame.copy()
            output_frame[binary_mask_3c == 255] = colored_mask[binary_mask_3c == 255]
            
            # Actualizar el frame con la máscara coloreada (manteniendo el fondo natural)
            frame = output_frame
        
        # Mostrar la cantidad de máscaras detectadas
        cv2.putText(frame, f'Masks: {len(masks)}', (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    # Mostrar la latencia en el frame
    cv2.putText(frame, f'Latency: {latency:.1f}ms', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # Mostrar el frame procesado en tiempo real
    cv2.imshow("YOLOv11-Seg - Segmentación en Tiempo Real", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()