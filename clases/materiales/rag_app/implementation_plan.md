# Plan de Implementación: RAG Local en Python

Este plan describe los pasos para construir un sistema RAG (Retrieval-Augmented Generation) completamente local utilizando los documentos (PDFs y presentaciones) que tienes en tu carpeta `materiales`.

## Proposed Architecture

- **Framework:** LangChain (para orquestar el RAG).
- **Vector Store:** ChromaDB (base de datos vectorial local para guardar los embeddings).
- **Embeddings:** `OpenAIEmbeddings` (usaremos la API de OpenAI para generar los vectores).
- **LLM (Modelo de Lenguaje):** `ChatOpenAI` (usaremos un modelo de OpenAI como `gpt-3.5-turbo` o `gpt-4o`).
- **Procesamiento de Documentos:** `PyPDF` para leer los PDFs que tienes en la carpeta.

## Proposed Steps

### Fase 1: Preparación del Entorno
- Crear la carpeta del proyecto (`rag_app`).
- Crear el entorno virtual `env` (`python -m venv env`).
- Instalar dependencias (`langchain`, `chromadb`, `pypdf`, `langchain-community`, `langchain-openai`, `python-dotenv`).

### Fase 2: Ingesta de Documentos
- Crear un script `ingest.py`.
- Este script leerá los archivos `.pdf` de la carpeta `materiales`, extraerá el texto, lo dividirá en fragmentos (chunks) y los guardará en ChromaDB usando los embeddings de OpenAI.

### Fase 3: Creación del RAG (Consulta)
- Crear un script `query.py`.
- Este script recibirá una pregunta tuya, buscará los fragmentos más relevantes en ChromaDB y usará el LLM de OpenAI para generar una respuesta basada en tus materiales de clase.

## Verification Plan

- Ejecutaremos el script de ingesta y verificaremos que la base de datos de ChromaDB se haya creado correctamente.
- Haremos una pregunta de prueba usando `query.py` relacionada con "No Code vs Codigo Asistido" o "Agentes LLMs" (basado en los nombres de tus PDFs) para verificar que el modelo responda correctamente leyendo tus documentos.
