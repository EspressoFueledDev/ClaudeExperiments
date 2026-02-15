import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))


def chunk_by_character(text, chunk_size=500, overlap=50):
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunk = text[i:i + chunk_size]
        if chunk:
            chunks.append(chunk)
    return chunks


def chunk_by_sentence(text, max_sentences=5):
    import re

    # Simple sentence splitter
    sentences = re.split(r'(?<=[.!?])\s+', text)

    chunks = []
    current_chunk = []

    for sentence in sentences:
        current_chunk.append(sentence)

        if len(current_chunk) >= max_sentences:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    # Add remaining sentences
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks


def chunk_by_paragraph(text):
    # Split by double newline (paragraph separator)
    paragraphs = text.split('\n\n')
    chunks = [p.strip() for p in paragraphs if p.strip()]
    return chunks


def semantic_chunking(text, max_chunk_size=1000):
    # Split into paragraphs first
    paragraphs = text.split('\n\n')

    chunks = []
    current_chunk = []
    current_size = 0

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        para_size = len(para)

        # If adding this paragraph exceeds max size, start new chunk
        if current_size + para_size > max_chunk_size and current_chunk:
            chunks.append('\n\n'.join(current_chunk))
            current_chunk = []
            current_size = 0

        current_chunk.append(para)
        current_size += para_size

    # Add remaining content
    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))

    return chunks


def demo_chunking_strategies():
    """Demonstrate different chunking strategies"""

    sample_text = """
Artificial Intelligence (AI) is transforming the world. Machine learning algorithms can now perform tasks that once required human intelligence.

Large language models like GPT and Claude can understand and generate human-like text. They are trained on massive datasets containing billions of words.

These models use a technique called transformer architecture. Transformers use attention mechanisms to process text efficiently. This allows them to understand context and relationships between words.

AI applications are everywhere. They power search engines, recommendation systems, virtual assistants, and much more. The technology continues to advance rapidly.

However, AI also raises important questions. How do we ensure AI systems are safe and beneficial? What about privacy and bias? These challenges require careful consideration.

The future of AI is exciting. As models become more capable, they will unlock new possibilities. But we must develop them responsibly.
""".strip()

    print("=" * 80)
    print("TEXT CHUNKING STRATEGIES")
    print("=" * 80)

    print("\nORIGINAL TEXT LENGTH:", len(sample_text), "characters")
    print("\n" + "=" * 80)

    # Strategy 1: Character-based
    print("\n1. CHARACTER-BASED CHUNKING (500 chars, 50 overlap)")
    print("-" * 80)
    char_chunks = chunk_by_character(sample_text, chunk_size=500, overlap=50)
    print(f"Number of chunks: {len(char_chunks)}")
    for i, chunk in enumerate(char_chunks[:2], 1):
        print(f"\nChunk {i} ({len(chunk)} chars):")
        print(chunk[:150] + "...")

    # Strategy 2: Sentence-based
    print("\n" + "=" * 80)
    print("\n2. SENTENCE-BASED CHUNKING (5 sentences per chunk)")
    print("-" * 80)
    sentence_chunks = chunk_by_sentence(sample_text, max_sentences=3)
    print(f"Number of chunks: {len(sentence_chunks)}")
    for i, chunk in enumerate(sentence_chunks[:2], 1):
        print(f"\nChunk {i} ({len(chunk)} chars):")
        print(chunk)

    # Strategy 3: Paragraph-based
    print("\n" + "=" * 80)
    print("\n3. PARAGRAPH-BASED CHUNKING")
    print("-" * 80)
    para_chunks = chunk_by_paragraph(sample_text)
    print(f"Number of chunks: {len(para_chunks)}")
    for i, chunk in enumerate(para_chunks[:2], 1):
        print(f"\nChunk {i} ({len(chunk)} chars):")
        print(chunk)

    # Strategy 4: Semantic
    print("\n" + "=" * 80)
    print("\n4. SEMANTIC CHUNKING (max 300 chars)")
    print("-" * 80)
    semantic_chunks = semantic_chunking(sample_text, max_chunk_size=300)
    print(f"Number of chunks: {len(semantic_chunks)}")
    for i, chunk in enumerate(semantic_chunks[:2], 1):
        print(f"\nChunk {i} ({len(chunk)} chars):")
        print(chunk)

    # Recommendations
    print("\n" + "=" * 80)
    print("\nRECOMMENDATIONS")
    print("=" * 80)
    print("""
1. CHARACTER-BASED: Use for simple cases, consistent sizes needed
   - Pros: Simple, predictable
   - Cons: May break sentences/words

2. SENTENCE-BASED: Good general-purpose choice
   - Pros: Coherent chunks, preserves meaning
   - Cons: Variable sizes

3. PARAGRAPH-BASED: Best for well-structured documents
   - Pros: Preserves document structure
   - Cons: Very variable sizes, may be too large

4. SEMANTIC: Best for RAG applications
   - Pros: Keeps related content together
   - Cons: More complex, slower

For RAG: Start with SEMANTIC or SENTENCE-BASED
For code: Use function/class boundaries
For chat: Use message boundaries
    """)


if __name__ == "__main__":
    demo_chunking_strategies()

    print("\n" + "=" * 80)
    print("NEXT STEP: Learn about embeddings and vector databases")
    print("=" * 80)
