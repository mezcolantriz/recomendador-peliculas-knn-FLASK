from flask import Flask, render_template, request, jsonify, url_for
import pandas as pd
import pickle
from dotenv import load_dotenv
import os
from googletrans import Translator
import requests  # Asegurarse de que requests está instalado
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Cargar las variables de entorno
load_dotenv()


# Cargar el dataset limpio
df = pd.read_csv("src/movies_cleaned.csv")

# Cargar los modelos previamente generados
with open("src/model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("src/model/similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

# Configurar traducción
translator = Translator()

def recommend(movie_title):
    try:
        # Traducción del título al inglés
        translated_title = translator.translate(movie_title, src="es", dest="en").text.lower()
    except Exception as e:
        print(f"Error en la traducción: {e}")
        translated_title = movie_title.lower()

    # Buscar el índice de la película traducida o en minúsculas
    movie_index = df[df['title'].str.lower() == translated_title].index

    if not movie_index.empty:
        # Obtener las películas más similares
        movie_list = similarity[movie_index[0]]
        movie_list = sorted(list(enumerate(movie_list)), reverse=True, key=lambda x: x[1])[1:6]
        recommendations = [(df.iloc[i[0]].title, get_poster(df.iloc[i[0]].title)) for i in movie_list]
    else:
        # Si no se encuentra, mensaje personalizado con el video
        recommendations = [("No encontrado", url_for("static", filename="no_image.jpg"))]

    return recommendations

def get_poster(title):
    """Obtiene el póster de una película dado su título usando la API de TMDB."""
    api_key = os.getenv("TMDB_API_KEY")
    base_url = f"https://api.themoviedb.org/3/search/movie"
    params = {"api_key": api_key, "query": title}
    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data["results"]:
                poster_path = data["results"][0].get("poster_path")
                if poster_path:
                    return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except Exception as e:
        print(f"Error al obtener el póster: {e}")

    # Si falla, devolver imagen predeterminada
    return url_for("static", filename="no_image.jpg")

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []  # Siempre inicializamos las recomendaciones como lista vacía
    movie_title = ""
    if request.method == "POST":
        movie_title = request.form.get("movie")
        recommendations = recommend(movie_title)
    return render_template("index.html", recommendations=recommendations, movie=movie_title)

@app.route("/autocomplete", methods=["GET"])
def autocomplete():
    query = request.args.get("q", "").lower()  # Convertimos a minúsculas
    suggestions = df[df["title"].str.lower().str.contains(query)].head(5)["title"].tolist()
    return {"suggestions": suggestions}

if __name__ == "__main__":
    app.run(debug=True)
