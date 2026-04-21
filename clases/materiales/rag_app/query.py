import os
import sys
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate

# Cargar variables de entorno (OPENAI_API_KEY)
load_dotenv()

CHROMA_PATH = "chroma_db"

def main():
    if not os.path.exists(CHROMA_PATH):
        print(f"Error: No se encontró la base de datos en '{CHROMA_PATH}'. Ejecuta ingest.py primero.")
        sys.exit(1)

    print("Cargando la base de datos vectorial...")
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": 5})

    print("Configurando el modelo de lenguaje (LLM)...")
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    # Prompt template for the RAG
    system_prompt = (
        "Eres un asistente útil que responde preguntas basándose estrictamente en el contexto proporcionado. "
        "Usa los siguientes fragmentos de contexto recuperado para responder a la pregunta. "
        "Si no sabes la respuesta basándote en el contexto, simplemente di que no lo sabes. "
        "Intenta mantener la respuesta concisa y clara.\n\n"
        "Contexto:\n{context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    print("El modelo de lenguaje y recuperador están listos.")

    print("\n--- RAG LOCAL INICIADO ---")
    print("Escribe 'salir' o 'exit' para terminar.\n")

    while True:
        query = input("Tu pregunta: ")
        if query.lower() in ["salir", "exit", "quit"]:
            break
            
        if not query.strip():
            continue

        print("\nPensando...")
        try:
            # 1. Recuperar los documentos relevantes
            docs = retriever.invoke(query)
            
            # 2. Combinar el texto de los documentos
            context_text = "\n\n".join([doc.page_content for doc in docs])
            
            # 3. Preparar los mensajes para el LLM y obtener la respuesta
            messages = prompt.format_messages(context=context_text, input=query)
            response = llm.invoke(messages)
            
            print(f"\nRespuesta: {response.content}\n")
            
            # Opcional: mostrar las fuentes
            print("Fuentes:")
            for i, doc in enumerate(docs):
                source = doc.metadata.get('source', 'Desconocido')
                page = doc.metadata.get('page', 'N/A')
                print(f"  [{i+1}] Archivo: {os.path.basename(source)}, Página: {page}")
            print("-" * 50)
            
        except Exception as e:
            print(f"\nError al consultar: {e}")

if __name__ == "__main__":
    main()
