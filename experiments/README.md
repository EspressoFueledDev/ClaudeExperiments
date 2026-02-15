# Experiments

Practical applications and sandbox for testing ideas.

## Web Scraper

**File:** `web_scraper.py`

Scrapes webpages and uses Claude to analyze content.

```bash
python experiments/web_scraper.py
```

**Features:**
- Scrapes any webpage
- Cleans and extracts text
- Claude analysis: summarize, extract facts, sentiment
- Configurable analysis types

**Modify for your needs:**
- Change URL in the main section
- Add custom analysis types
- Integrate with your own data sources

---

## ChromaDB Explorer

**File:** `chromadb_explorer.ipynb`

Interactive Jupyter notebook for exploring vector database.

```bash
jupyter notebook experiments/chromadb_explorer.ipynb
```

**What you can do:**
- View all collections and documents
- Semantic search with live results
- Filter by metadata
- Add new documents
- Visualize with pandas DataFrames

---

## Setup ChromaDB UI

**File:** `setup_chromadb_ui.py`

Creates a sample ChromaDB database with demo documents.

```bash
python experiments/setup_chromadb_ui.py
```

**Creates:**
- Database at `./chroma_data`
- 8 sample documents (AI, programming, databases)
- Ready for tutorials and testing

---

## Tips

- Use this folder for quick tests and prototypes
- Don't worry about code quality here
- When something works well, move it to `projects/`
- Experiments are meant to be messy and exploratory
