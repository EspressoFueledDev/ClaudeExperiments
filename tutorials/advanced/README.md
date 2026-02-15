# Advanced AI Development Tutorials

Learn to build RAG (Retrieval Augmented Generation) systems from scratch.

## Prerequisites

Completed tutorials/01_basics (prompt engineering fundamentals)

## Learning Path

### 01_text_chunking.py
Learn how to split documents into chunks for vector storage.

**Covers:**
- Character-based chunking
- Sentence-based chunking
- Paragraph-based chunking
- Semantic chunking

**Run:** `python tutorials/02_advanced/01_text_chunking.py`

---

### 02_embeddings_intro.py
Understand how text is converted to numerical vectors.

**Covers:**
- What embeddings are
- How they capture meaning
- Similarity calculations
- Embedding providers

**Run:** `python tutorials/02_advanced/02_embeddings_intro.py`

---

### 03_vector_database.py
Set up and use ChromaDB for semantic search.

**Covers:**
- ChromaDB setup
- Storing documents with embeddings
- Semantic search
- Metadata filtering

**Run:** `python tutorials/02_advanced/03_vector_database.py`

**First time:** `pip install chromadb sentence-transformers`

---

### 04_simple_rag.py
Build a complete RAG system combining retrieval + generation.

**Covers:**
- RAG architecture
- Document retrieval
- Context injection
- Answer generation with Claude

**Run:** `python tutorials/02_advanced/04_simple_rag.py`

---

## Installation

```bash
# Install all dependencies
pip install -r requirements.txt

# Or install individually
pip install chromadb sentence-transformers
```

## Quick Start

```bash
# Run tutorials in order
python tutorials/02_advanced/01_text_chunking.py
python tutorials/02_advanced/02_embeddings_intro.py
python tutorials/02_advanced/03_vector_database.py
python tutorials/02_advanced/04_simple_rag.py
```

## What You'll Build

By the end, you'll have:
- Working RAG system
- Understanding of embeddings and vector search
- Practical knowledge of ChromaDB
- Ability to build custom knowledge bases

## Next Steps

After completing these tutorials:

1. **Build a real project:** Use web scraper to build knowledge base
2. **Improve retrieval:** Add hybrid search, re-ranking
3. **Scale up:** Handle larger document sets
4. **Production:** Build API with FastAPI, deploy with Docker

See `RAG_LEARNING_PATH.md` for full roadmap.

## Common Issues

**Import errors:** Run `pip install chromadb sentence-transformers`

**Slow first run:** sentence-transformers downloads model (~80MB) on first use

**Memory issues:** Reduce document count or chunk size

## Resources

- ChromaDB docs: https://docs.trychroma.com/
- Sentence Transformers: https://www.sbert.net/
- RAG patterns: https://github.com/anthropics/anthropic-cookbook
