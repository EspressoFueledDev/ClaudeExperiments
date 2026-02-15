# RAG (Retrieval Augmented Generation) Learning Path

Complete path from web scraping to production RAG system with Claude.

## Learning Roadmap

### Phase 1: Data Collection & Processing
- [x] 1. Web scraping basics (Done in experiments/)
- [ ] 2. Advanced scraping (multiple pages, pagination, rate limiting)
- [ ] 3. Parsing & cleaning data
- [ ] 4. Text chunking strategies

### Phase 2: Vector Databases
- [ ] 5. Understanding embeddings
- [ ] 6. Vector database setup (ChromaDB)
- [ ] 7. Storing and querying vectors
- [ ] 8. Similarity search basics

### Phase 3: Building RAG
- [ ] 9. Basic RAG architecture
- [ ] 10. Document ingestion pipeline
- [ ] 11. Retrieval strategies
- [ ] 12. Context injection into prompts

### Phase 4: Advanced RAG
- [ ] 13. Improving retrieval quality
- [ ] 14. Hybrid search (keyword + semantic)
- [ ] 15. Re-ranking results
- [ ] 16. Evaluation and optimization

### Phase 5: Production (Optional)
- [ ] 17. NextJS frontend
- [ ] 18. API design
- [ ] 19. Deployment
- [ ] 20. Monitoring and updates

## Tech Stack

### Core
- Python for backend/processing
- Claude API for LLM
- ChromaDB for vector storage (simple, lightweight)
- BeautifulSoup/Scrapy for web scraping

### Optional (Production)
- NextJS for frontend
- FastAPI for backend API
- PostgreSQL with pgvector (production vector DB)
- Docker for deployment

## Project Structure

```
ClaudeExperiments/
├── tutorials/02_advanced/
│   ├── 01_advanced_scraping.py
│   ├── 02_text_chunking.py
│   ├── 03_embeddings_intro.py
│   ├── 04_vector_db_setup.py
│   ├── 05_basic_rag.py
│   ├── 06_advanced_rag.py
│   └── RAG_LEARNING_PATH.md (this file)
│
├── projects/rag_system/
│   ├── scraper/
│   ├── vector_store/
│   ├── rag_engine/
│   └── api/
│
└── experiments/
    └── web_scraper.py (✓ Done)
```

## Quick Start

We'll build each component step by step:

1. Start with tutorials to learn concepts
2. Build a simple RAG system
3. Gradually add complexity
4. Eventually build a production-ready system

## Estimated Timeline

- Beginner: 2-3 weeks (learning + building)
- With coding experience: 1 week
- Just tutorials: 2-3 days

## First Steps

1. Complete web scraping tutorial (✓ Done)
2. Learn about text chunking
3. Set up ChromaDB
4. Build first simple RAG

Ready to start with tutorial #2?
