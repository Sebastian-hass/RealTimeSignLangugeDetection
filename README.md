# Detector de Lengua de Señas en Tiempo Real ✋📷

Este proyecto implementa un sistema completo para la detección en tiempo real de lenguaje de señas usando la **TensorFlow Object Detection API**. Incluye todo el flujo: desde el etiquetado de imágenes, la generación de datos, el entrenamiento y la inferencia en vivo con webcam. El paso a paso detallado para ejecutar el proyecto se encuentra en el notebook `Tutorial.ipynb`.

---

## 📌 Características principales

- Entrenamiento con imágenes propias y etiquetas personalizadas
- Flujo completo reproducible: desde anotación hasta inferencia
- Detección en vivo vía webcam
- Basado en TensorFlow 2.10 y la API oficial de Object Detection
- Código y scripts organizados para facilitar la extensión y el aprendizaje

---

## 📁 Estructura del proyecto

La carpeta principal donde se encuentra toda la lógica y recursos es `Tensorflow/`:

- **Tensorflow/labelImg/**: Herramienta gráfica para etiquetar imágenes (LabelImg), con scripts y dependencias para crear los archivos de anotación necesarios.
- **Tensorflow/scripts/**: Scripts utilitarios, como `generate_tfrecord.py` para convertir anotaciones a formato TFRecord compatible con TensorFlow.
- **Tensorflow/models/**: Repositorio oficial de modelos de TensorFlow, incluyendo la API de Object Detection y modelos preentrenados.
- **Tensorflow/workspace/**: Espacio de trabajo donde se almacenan las anotaciones, imágenes, modelos entrenados y modelos preentrenados descargados.
    - `annotations/`: Archivos de etiquetas y TFRecords generados.
    - `images/`: Imágenes de entrenamiento y prueba.
    - `models/`: Modelos personalizados entrenados.
    - `pre-trained-models/`: Modelos base descargados del Model Zoo.

El archivo `Tutorial.ipynb` contiene el flujo completo, desde la preparación de datos hasta la inferencia en tiempo real, y es la mejor guía para reproducir el proyecto.

---

## 🛠️ Instalación

### 1. Crear entorno virtual con Anaconda

```bash
conda create -n tfod python=3.10
conda activate tfod
```
### 2. Instalar dependencias

pip install -r requirements.txt

### 3. Instalar la TensorFlow Object Detection API

Sigue la guía oficial aquí:
👉 https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html

## 🚀Entrenamiento y Resultados

El modelo fue entrenado por 20,000 pasos, logrando una pérdida (loss) final aproximada de 0.116, lo cual indica un buen rendimiento para un dataset personalizado.

## 🎥 Detección en tiempo real

Utilizando OpenCV, el modelo es capaz de detectar señas a través de la webcam con buena velocidad y precisión.

## 📌 Notas

Este proyecto fue desarrollado completamente desde cero, inspirado en proyectos de ejemplo del uso de la Object Detection API en otras aplicaciones como detección de mascarillas.

## 📜 Licencia
Todos los derechos reservados

## Previsualización
https://github.com/user-attachments/assets/46811364-3485-4778-b8a4-8ea871ad8c08
