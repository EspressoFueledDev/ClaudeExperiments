# AI Development Learning Project

Complete learning path for building RAG (Retrieval Augmented Generation) systems with Claude API.

## Quick Start

```bash
# Setup
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Create .env file
echo "ANTHROPIC_API_KEY=your_key_here" > .env

# Run first tutorial
python -m tutorials.basics.vague_vs_specific
```

## Running Tutorials

```bash
# Method 1: Using -m flag (recommended)
python -m tutorials.basics.vague_vs_specific
python -m tutorials.advanced.simple_rag

# Method 2: Direct path (if script has path fix)
python tutorials/basics/vague_vs_specific.py
```

## Experiments

### Web Scraper
```bash
python experiments/web_scraper.py
```
Scrapes webpages and analyzes content with Claude.

### ChromaDB Explorer (Jupyter)
```bash
jupyter notebook experiments/chromadb_explorer.ipynb
```
Interactive notebook for exploring vector database.

### Setup Sample Database
```bash
python experiments/setup_chromadb_ui.py
```
Creates ChromaDB with sample documents.

## Utils

Shared helper functions in `utils/claude_helper.py`:

```python
from utils.claude_helper import call_haiku, call_sonnet

# Quick single prompt
response = call_haiku("Your question")

# Multi-turn conversation
response = call_sonnet(messages, system_prompt="You are...")
```


## Tech Stack

- Python 3.13
- Claude API (Anthropic)
- ChromaDB (vector database)
- sentence-transformers (local embeddings)
- BeautifulSoup (web scraping)
- Jupyter (interactive development)

## Environment Variables

Create `.env` file:
```
ANTHROPIC_API_KEY=your_api_key_here
```