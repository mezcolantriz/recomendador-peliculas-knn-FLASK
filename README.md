# 🧠 ML - K-NEAREST NEIGHBORS 
# 🎥 Recomendador de Películas KNN para Flask

Este proyecto es un **sistema de recomendación de películas** desarrollado como parte del aprendizaje en **4Geeks Academy**, utilizando el algoritmo **K-Nearest Neighbors (KNN)** y la tecnología **Flask** para crear una interfaz web interactiva y fácil de usar.

El objetivo principal de este proyecto es recomendar películas a los usuarios basándose en similitudes y preferencias, utilizando datos estructurados y procesados con Python.

Para acceder al recurso web se puede hacer desde # https://knnparaflask.onrender.com

---

## 🚀 Características

- **Recomendaciones personalizadas**: Basadas en el algoritmo KNN para encontrar similitudes entre películas.
- **Interfaz web interactiva**: Construida con Flask, HTML y CSS, pensada para la usabilidad.
- **Extensible y personalizable**: Puedes agregar más datos o ajustar la lógica del modelo para mejorar las recomendaciones.
- **Diseño modular**: Separación clara entre frontend, backend y lógica del modelo.

---

## 📂 Estructura del Proyecto

El proyecto está organizado de la siguiente manera:


```plaintext
recomendador-peliculas-knn-FLASK/
│
├── static/               # Archivos estáticos como CSS, imágenes y JavaScript
├── templates/            # Archivos HTML para la interfaz web
├── app.py                # Script principal que ejecuta la aplicación Flask
├── knn.py                # Implementación del algoritmo K-Nearest Neighbors
├── data/                 # Directorio que contiene los datasets
├── requirements.txt      # Lista de dependencias necesarias
└── README.md             # Este archivo
---

## ⚙️ Instalación y Ejecución

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

### **1. Clona el repositorio**
```bash
git clone https://github.com/mezcolantriz/recomendador-peliculas-knn-FLASK
cd recomendador-peliculas-knn-FLASK
```` 


2. Crea un entorno virtual e instala las dependencias
```bash
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
pip install -r requirements.txt
````

3. Ejecuta la aplicación
```bash
python app.py
```` 
4. Abre tu navegador
Accede a la aplicación desde http://127.0.0.1:5000/.


-----  


## 🧠 ¿Cómo funciona el algoritmo KNN en este proyecto?  
  
- Datos de entrada: El sistema utiliza un dataset de películas con características como género, año de lanzamiento, popularidad, etc.  
- Cálculo de distancias: Utiliza la distancia euclidiana para medir similitudes entre películas.  
- Recomendación: Con base en las películas más cercanas (vecinas), se generan recomendaciones personalizadas para el usuario.  
  
📊 Dataset  
El dataset contiene información como:  
    
- Títulos de las películas  
- Géneros  
- Año de lanzamiento  
- Popularidad y puntuaciones
  
Puedes personalizar o ampliar el dataset para mejorar las recomendaciones y adaptarlo a tus necesidades.
  
✨ Contribuciones    
Este proyecto fue desarrollado como parte del aprendizaje en 4Geeks Academy. Si tienes ideas para mejorarlo, deseas reportar errores o simplemente colaborar, ¡no dudes en abrir un issue o enviar un pull request!  
  
🔗 Recursos y Referencias  
Flask: Documentación oficial  
K-Nearest Neighbors: Guía en scikit-learn    
    
📜 Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
