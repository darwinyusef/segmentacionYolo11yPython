# Trabajo Actividad 2 Evaluación de la segmentación

# PRESENTACIÓN
+ ### DARWIN YUSEF GONZALEZ TRIANA
+ ### C.C. 14297510
+ ### © Universidad Internacional de La Rioja (UNIR)
+ ### INVESTIGACIÓN EN IA

![Presentación](https://raw.githubusercontent.com/darwinyusef/20exHuggingFacePytorchTensorFlowSklearn/refs/heads/master/skitimage/intensity/presentacion.png)

# descripción de archivos
1. [Taller de Segmentación según lo relacionado en la GUIA](https://github.com/darwinyusef/segmentacionYolo11yPython/blob/master/segmentacionDarwinYusefGonzalez14297510.ipynb)
2. [Análisis de Movimiento en Video con Segmentación y Mapas de Calor con YOLO](https://github.com/darwinyusef/segmentacionYolo11yPython/blob/master/umbrdetectyolo.ipynb)
3. [Detección de personas usando Segmentación con YOLO11](https://github.com/darwinyusef/segmentacionYolo11yPython/blob/master/main.py)
   



## Objetivos

El objetivo de este trabajo es aprender a construir y evaluar el rendimiento de uno o más segmentadores. Esta actividad permitirá consolidar los conceptos sobre segmentación de imágenes aprendidos.

## Descripción

Este trabajo se entrega de forma individual. En él nos vamos a enfrentar a un verdadero problema de segmentación. La segmentación, como se ha visto, consiste en detectar regiones homogéneas y aislar/detectar objetos dentro de una imagen. Estas regiones habitualmente corresponden a los objetos que se están queriendo identificar.

Existen muchas maneras de enfocar este problema y puedes hacer uso de las técnicas de segmentación que consideres para resolverlo. Una vez elegidas estas técnicas, debes evaluar su rendimiento frente a imágenes de ground truth. En caso de que se utilicen partes de un software existente, deberá referenciarse la fuente. Debes mostrar en pantalla los resultados de los principales pasos.



# Crear un Entorno Virtual en Python e Instalar `freeze`

A continuación, se explica cómo crear un entorno virtual en Python e instalar el paquete `freeze` dentro de este entorno. El entorno virtual es útil para gestionar dependencias de proyectos de manera aislada y evitar conflictos entre bibliotecas.

## Paso 1: Crear un Entorno Virtual

1. Abre una terminal o consola de comandos.

2. Navega al directorio de tu proyecto o donde desees crear el entorno virtual.

3. Crea el entorno virtual ejecutando el siguiente comando:

    ```bash
    python -m venv nombre_del_entorno
    ```

    - **`nombre_del_entorno`** es el nombre que deseas darle a tu entorno virtual (puede ser cualquier nombre que elijas).

    Esto creará una carpeta llamada `nombre_del_entorno` en tu directorio, donde se almacenarán los archivos del entorno virtual.

## Paso 2: Activar el Entorno Virtual

- **En Windows:**

    ```bash
    nombre_del_entorno\Scripts\activate
    ```

- **En macOS y Linux:**

    ```bash
    source nombre_del_entorno/bin/activate
    ```

Una vez activado, verás el nombre del entorno virtual en el prompt de la terminal, lo que indica que el entorno virtual está activo.

## Paso 3: Instalar `freeze`

1. Con el entorno virtual activado, instala el paquete `freeze` usando `pip`:

    ```bash
    pip install freeze
    ```

    Esto instalará `freeze` en tu entorno virtual.

## Paso 4: Verificar la Instalación

Para asegurarte de que `freeze` se ha instalado correctamente, puedes ejecutar el siguiente comando para ver una lista de los paquetes instalados:

```bash
pip freeze
```


# Referencias 

Platzi. (Fredy Vega 2024). Redes neuronales. Platzi. Recuperado de https://platzi.com/cursos/redes-neuronales/

Platzi. (Fredy Vega 2024). PyTorch. Platzi. Recuperado de https://platzi.com/cursos/pytorch/

Platzi. (Fredy Vega 2024). Redes neuronales con TensorFlow. Platzi. Recuperado de https://platzi.com/cursos/redes-neuronales-tensorflow/

Platzi. (Fredy Vega 2024). Redes neuronales convolucionales. Platzi. Recuperado de https://platzi.com/cursos/redes-neuronales-convolucionales/

Platzi. (Fredy Vega 2024). Computer vision con TensorFlow. Platzi. Recuperado de https://platzi.com/cursos/computer-vision-tensorflow/

Platzi. (Fredy Vega 2024). TensorFlow para objetos. Platzi. Recuperado de https://platzi.com/cursos/tensorflow-objetos/

Ratan, R. (2024). *Modern Computer Vision GPT, PyTorch, Keras, OpenCV4 in 2024!*. Udemy. Recuperado de https://www.udemy.com/course/modern-computer-vision/
