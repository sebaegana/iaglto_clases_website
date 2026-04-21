import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# Cargar variables de entorno (OPENAI_API_KEY)
load_dotenv()

# Ruta a la carpeta de materiales de clase
MATERIALES_PATH = r"C:\Users\sebae\Downloads\FEN - LLM e IA\iaglto_clases_website\clases\materiales"
# Directorio donde se guardará la base de datos de ChromaDB
CHROMA_PATH = "chroma_db"

def main():
    print("Iniciando el proceso de ingesta de documentos...")
    
    # 1. Cargar documentos
    print(f"Buscando PDFs en: {MATERIALES_PATH}")
    loader = PyPDFDirectoryLoader(MATERIALES_PATH)
    docs = loader.load()
    print(f"Se cargaron {len(docs)} páginas de documentos.")

    if not docs:
        print("No se encontraron documentos. Revisa la ruta.")
        return

    # 2. Dividir el texto en fragmentos (chunks)
    print("Dividiendo documentos en fragmentos...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_documents(docs)
    print(f"Se generaron {len(chunks)} fragmentos.")

    # 3. Crear los embeddings y guardar en ChromaDB
    print("Generando embeddings y guardando en ChromaDB...")
    # OpenAIEmbeddings usará automáticamente la clave OPENAI_API_KEY de tu archivo .env
    embeddings = OpenAIEmbeddings()
    
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )
    print(f"¡Base de datos vectorial guardada exitosamente en el directorio '{CHROMA_PATH}'!")

if __name__ == "__main__":
    main()
