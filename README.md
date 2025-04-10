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
