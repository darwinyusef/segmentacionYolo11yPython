wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n-seg.pt

# Análisis de Movimiento en Video con Segmentación y Mapas de Calor

Este proyecto implementa una técnica para analizar el movimiento en secuencias de video, combinando sustracción de fondo y segmentación de instancias mediante el modelo YOLOv11. El objetivo es identificar y rastrear objetos en movimiento, específicamente personas, y visualizar su trayectoria a través de un mapa de calor acumulativo.

## Descripción del Código

1. **Inicialización**: Se carga el modelo YOLOv11 para segmentación (`yolo11n-seg`) y se inicializa el acumulador del mapa de calor `heatmap_refined`.

2. **Captura de Video**: Se procesa cada fotograma del video en un bucle continuo. Si no se puede leer un fotograma, el proceso se detiene.

3. **Sustracción de Fondo**: Se aplica un sustractor de fondo para obtener una máscara binaria que resalta las áreas en movimiento en el fotograma actual.

4. **Segmentación con YOLOv11**: Se utiliza el modelo YOLOv11 para realizar la segmentación de instancias en el fotograma, identificando objetos y generando máscaras para cada instancia detectada.

5. **Filtrado de Personas**: Se filtran las máscaras correspondientes a la clase "persona" (clase 0 en COCO) y se combinan en una única máscara de segmentación.

6. **Combinación de Máscaras**: Se realiza una intersección entre la máscara de movimiento y la máscara de segmentación de personas para obtener una máscara refinada que representa las áreas donde hay movimiento de personas.

7. **Actualización del Mapa de Calor**: La máscara refinada se acumula en el `heatmap_refined`, que visualiza las áreas con mayor actividad a lo largo del tiempo.

8. **Visualización**: Se muestran en ventanas separadas el fotograma original, la máscara de movimiento y la máscara refinada. El proceso continúa hasta que se presiona la tecla 'q'.

## Contexto Teórico

La combinación de sustracción de fondo y segmentación de instancias es una técnica poderosa en visión por computadora para detectar y rastrear objetos en movimiento. La sustracción de fondo permite identificar áreas de cambio en una escena estática, mientras que la segmentación de instancias, como la proporcionada por YOLOv11, permite identificar y delinear objetos específicos dentro de esas áreas. Al combinar ambas técnicas, es posible aislar y rastrear objetos de interés, como personas, en secuencias de video, facilitando aplicaciones en seguridad, análisis de comportamiento y más.


# Descargar 