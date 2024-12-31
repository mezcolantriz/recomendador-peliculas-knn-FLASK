import os
import gdown
import gzip
import shutil

# Define el directorio de descarga
DOWNLOAD_DIR = "compressed_models/models"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# URLs de los modelos en Google Drive
VECTOR_URL = "https://drive.google.com/uc?id=1UXfc4KNFfocNLwTz91la3wfirbUB4Wv6"
SIMILARITY_URL = "https://drive.google.com/uc?id=13ZuYLIVPRWvATLmBX3AeKsqnP89SvXEL"

# Rutas para guardar los modelos
VECTOR_PATH = os.path.join(DOWNLOAD_DIR, "vectorizer_compressed.pkl.gz")
SIMILARITY_PATH = os.path.join(DOWNLOAD_DIR, "similarity_compressed.pkl.gz")

def download_and_save_model(url, output_path):
    """
    Descarga un archivo desde una URL de Google Drive y lo guarda en la ruta especificada.
    """
    print(f"Descargando modelo desde: {url}")
    gdown.download(url, output_path, quiet=False)
    print(f"Modelo guardado en: {output_path}")

def decompress_gzip(file_path, output_path):
    """
    Descomprime un archivo .gz y lo guarda como .pkl.
    """
    print(f"Descomprimiendo {file_path}...")
    with gzip.open(file_path, 'rb') as f_in:
        with open(output_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"Modelo descomprimido en: {output_path}")

# Descargar y guardar los modelos comprimidos
download_and_save_model(VECTOR_URL, VECTOR_PATH)
download_and_save_model(SIMILARITY_URL, SIMILARITY_PATH)

# Descomprimir los modelos
decompress_gzip(VECTOR_PATH, VECTOR_PATH.replace(".gz", ""))
decompress_gzip(SIMILARITY_PATH, SIMILARITY_PATH.replace(".gz", ""))

print("Todos los modelos han sido descargados y descomprimidos correctamente.")
