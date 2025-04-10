# Sistema de Segmentación de Objetos en Tiempo Real con YOLOv11

El código implementa un sistema de segmentación de objetos en tiempo real utilizando el modelo YOLOv11 de Ultralytics. Este modelo es conocido por su capacidad para realizar detección y segmentación de objetos con alta precisión y velocidad, lo que lo hace adecuado para aplicaciones en tiempo real.

## Proceso General del Código

### 1. Configuración Inicial

- **Importación de Librerías**: Se importa el modelo YOLOv11 de Ultralytics y las librerías necesarias para el procesamiento de video (`cv2`), medición de tiempo (`time`) y manipulación de arrays (`numpy`).
  
- **Carga del Modelo YOLOv11**: Se carga el modelo YOLOv11 preentrenado de segmentación, como el archivo `yolo11n-seg.pt`, que está optimizado para tareas de segmentación de instancias.

- **Configuración de la Fuente de Video**: Se define la fuente de video, que puede ser una cámara en vivo o un archivo de video, y se establece la resolución deseada para la captura.

### 2. Captura y Procesamiento de Video

- **Captura de Fotogramas**: El código inicia un bucle que captura cada fotograma del video de la fuente configurada.

- **Medición de Latencia**: Para cada fotograma capturado, se mide el tiempo de inicio y se calcula la latencia de procesamiento, lo que permite conocer la eficiencia del sistema en tiempo real.

### 3. Detección y Segmentación

- **Aplicación del Modelo YOLOv11**: El modelo YOLOv11 se aplica sobre cada fotograma para detectar y segmentar objetos. En este caso, el modelo está configurado para detectar personas (índice 0 de la clase en COCO).

- **Obtención de Resultados**: Se obtienen las cajas delimitadoras (bounding boxes) y las máscaras de segmentación para cada objeto detectado en el fotograma.

### 4. Visualización de Resultados

- **Dibujo de Cajas Delimitadoras**: Para cada detección, se dibuja una caja delimitadora alrededor del objeto y se muestra una etiqueta con la clase y la confianza de la predicción.

- **Máscaras de Segmentación**: Las máscaras de segmentación de los objetos detectados se superponen al fotograma original utilizando colores aleatorios para diferenciar los objetos.

- **Latencia en el Fotograma**: Se muestra la latencia de procesamiento en milisegundos en el fotograma, proporcionando información sobre el rendimiento del sistema.

### 5. Interacción y Finalización

- **Visualización del Fotograma Procesado**: Se muestra el fotograma procesado en una ventana de visualización en tiempo real.

- **Cierre del Programa**: El bucle continúa hasta que se presiona la tecla 'q', momento en el cual se liberan los recursos y se cierran todas las ventanas abiertas.

## Contexto Teórico

La segmentación de instancias es una técnica avanzada en visión por computadora que no solo detecta la presencia y ubicación de objetos en una imagen, sino que también delimita con precisión sus contornos. A diferencia de la detección de objetos tradicional, que utiliza cajas delimitadoras, la segmentación de instancias proporciona una máscara a nivel de píxel para cada objeto, permitiendo una comprensión más detallada de la escena.

YOLOv11 es un modelo de última generación que combina velocidad y precisión en tareas de detección y segmentación, facilitando aplicaciones en tiempo real como vigilancia, análisis de tráfico y asistencia en conducción autónoma.

