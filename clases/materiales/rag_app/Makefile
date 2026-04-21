.PHONY: install ingest query run clean

# Windows virtual environment paths
PYTHON = env/Scripts/python
PIP = env/Scripts/pip

install:
	$(PIP) install langchain chromadb pypdf langchain-community langchain-openai python-dotenv

ingest:
	$(PYTHON) ingest.py

query:
	$(PYTHON) query.py

run: ingest query

clean:
	rmdir /S /Q chroma_db 2>nul || exit 0
