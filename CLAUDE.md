# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI development learning project focused on building RAG (Retrieval Augmented Generation) systems with Claude API. Structured as progressive tutorials from prompt engineering basics to production RAG systems.

## Setup and Common Commands

### Environment Setup
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Required .env file
ANTHROPIC_API_KEY=your_api_key_here
```

### Running Tutorials
```bash
# Run tutorials using -m flag (ensures imports work)
python -m tutorials.basics.vague_vs_specific
python -m tutorials.advanced.simple_rag

# Or with direct path (if script has path fix)
python tutorials/basics/vague_vs_specific.py
```

### Development
```bash
# Test Claude helper utilities
python utils/claude_helper.py

# Run web scraper experiment
python experiments/web_scraper.py
```

## Architecture

### Learning Path Structure
The project follows a progressive learning path:
1. **Basics** (tutorials/basics/) - Prompt engineering fundamentals
2. **Advanced** (tutorials/advanced/) - RAG system components
3. **Experiments** (experiments/) - Practical applications
4. **Projects** (projects/) - Production systems

### RAG System Architecture
RAG implementation follows this pipeline:
```
Web Scraping → Text Chunking → Embeddings → Vector DB → Retrieval + Generation
```

**Key Components:**
- **Text Chunking**: Split documents into semantic chunks (character, sentence, paragraph, semantic)
- **Embeddings**: Convert text to vectors using sentence-transformers (local, free)
- **Vector Database**: ChromaDB for semantic search and storage
- **RAG Engine**: Combines retrieval (ChromaDB) + generation (Claude API)

**Data Flow:**
1. Documents scraped and chunked
2. Chunks embedded and stored in ChromaDB
3. User query embedded and used to retrieve relevant chunks
4. Retrieved context injected into Claude prompt
5. Claude generates answer based on context

### Utilities Architecture
`utils/claude_helper.py` provides standardized API access:
- `call_haiku()`: Single-turn prompts with Haiku (fast, cheap)
- `call_sonnet()`: Multi-turn conversations with Sonnet (smart, capable)
- `get_client()`: Shared Anthropic client initialization

All tutorials use these helpers instead of direct API calls.

## Code Conventions

### Style Rules
- **No emojis** in code, comments, or output (enforced project-wide)
- Plain text output only, no special characters or decorations
- Descriptive names, no numeric prefixes (e.g., `text_chunking.py` not `01_text_chunking.py`)

### Import Pattern for Tutorial Scripts
All tutorial scripts must include this path fix:
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.claude_helper import call_haiku
```

This allows scripts to find `utils/` regardless of execution location.

### Tutorial Format
Tutorials follow consistent structure:
```python
# 1. Header with separators
print("=" * 80)
print("TUTORIAL NAME")
print("=" * 80)

# 2. Show comparison (BAD vs GOOD)
print("\nBAD - Example:")
print("-" * 80)
# ... bad example with output

print("\n" + "=" * 80)
print("\nGOOD - Example:")
print("-" * 80)
# ... good example with output

# 3. Key takeaways at end
print("\n" + "=" * 80)
print("KEY TAKEAWAY:")
print("Brief explanation of lesson learned")
```

### RAG System Conventions
When building RAG components:
- Always print what documents are retrieved before generation
- Show distances/similarity scores with results
- Display context being sent to Claude
- Use ChromaDB with sentence-transformers (no external API needed)
- Include metadata with documents for filtering

## Dependencies

Core stack:
- `anthropic` - Claude API client
- `chromadb` - Vector database
- `sentence-transformers` - Local embeddings (all-MiniLM-L6-v2)
- `requests` + `beautifulsoup4` - Web scraping
- `python-dotenv` - Environment variables

## Project Structure Rationale

```
tutorials/basics/      # Prompt engineering (7 techniques)
tutorials/advanced/    # RAG components (chunking, embeddings, vector DB, RAG)
experiments/          # Sandbox for quick tests
projects/             # Complete applications
utils/                # Shared Claude API helpers
docs/                 # Guidelines and notes
```

Tutorials are self-contained and runnable independently. Each demonstrates one concept with clear examples.

## Important Notes

- This is a learning project, prioritize clarity and education over optimization
- ChromaDB runs in-memory by default (use persist_directory for production)
- First run of sentence-transformers downloads ~80MB model
- RAG learning path documented in `tutorials/advanced/RAG_LEARNING_PATH.md`
- Detailed style rules in `docs/coding_guidelines/RULES.md`
