
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import chromadb
from chromadb.utils import embedding_functions


def setup_vector_db():
    print("Setting up ChromaDB...")

    client = chromadb.Client()

    embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

    collection = client.get_or_create_collection(
        name="docs",
        embedding_function=embedding_function,
        metadata={"description": "Document collection for RAG demo"}
    )

    print(f"Collection created: {collection.name}")
    print(f"Items in collection: {collection.count()}")

    return client, collection


def add_documents(collection, documents):
    print(f"\nAdding {len(documents)} documents...")

    ids = [doc['id'] for doc in documents]
    texts = [doc['text'] for doc in documents]
    metadatas = [doc.get('metadata', {}) for doc in documents]

    collection.add(
        documents=texts,
        ids=ids,
        metadatas=metadatas
    )

    print(f"Added {len(documents)} documents")
    print(f"Total documents: {collection.count()}")


def query_documents(collection, query, n_results=3):
    print(f"\nQuerying: '{query}'")

    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    return results





def demo_vector_database():

    print("=" * 80)
    print("VECTOR DATABASE TUTORIAL (ChromaDB)")
    print("=" * 80)

    documents = [
        {
            'id': 'doc1',
            'text': 'Python is a high-level programming language known for its simplicity and readability. It is widely used in data science and machine learning.',
            'metadata': {'topic': 'programming', 'language': 'python'}
        },
        {
            'id': 'doc2',
            'text': 'Machine learning is a subset of artificial intelligence that enables computers to learn from data without explicit programming.',
            'metadata': {'topic': 'ai', 'subtopic': 'ml'}
        },
        {
            'id': 'doc3',
            'text': 'Dogs are loyal pets that require regular exercise, training, and attention. They come in many breeds with different characteristics.',
            'metadata': {'topic': 'pets', 'animal': 'dog'}
        },
        {
            'id': 'doc4',
            'text': 'Neural networks are computing systems inspired by biological neural networks. They consist of layers of interconnected nodes.',
            'metadata': {'topic': 'ai', 'subtopic': 'neural-networks'}
        },
        {
            'id': 'doc5',
            'text': 'Cats are independent pets that are known for their agility and hunting skills. They require less maintenance than dogs.',
            'metadata': {'topic': 'pets', 'animal': 'cat'}
        },
        {
            'id': 'doc6',
            'text': 'JavaScript is a programming language primarily used for web development. It runs in web browsers and on servers with Node.js.',
            'metadata': {'topic': 'programming', 'language': 'javascript'}
        }
    ]

    # Set up database
    client, collection = setup_vector_db()

    # Add documents
    add_documents(collection, documents)

    # Test queries
    print("\n" + "=" * 80)
    print("SEMANTIC SEARCH EXAMPLES")
    print("=" * 80)

    queries = [
        "What programming languages are good for AI?",
        "Tell me about pet animals",
        "How do neural networks work?"
    ]

    for query in queries:
        results = query_documents(collection, query, n_results=2)

        print(f"\nTop {len(results['documents'][0])} results:")
        print("-" * 80)

        for i, (doc, distance, metadata) in enumerate(zip(
            results['documents'][0],
            results['distances'][0],
            results['metadatas'][0]
        ), 1):
            print(f"\nResult {i} (distance: {distance:.3f}):")
            print(f"Metadata: {metadata}")
            print(f"Text: {doc[:100]}...")

    # Demonstrate filtering
    print("\n" + "=" * 80)
    print("FILTERED SEARCH (only 'ai' topic)")
    print("=" * 80)

    results = collection.query(
        query_texts=["artificial intelligence"],
        n_results=3,
        where={"topic": "ai"}  # Filter by metadata
    )

    for i, (doc, metadata) in enumerate(zip(results['documents'][0], results['metadatas'][0]), 1):
        print(f"\n{i}. {metadata}")
        print(f"   {doc[:80]}...")

    # Explain
    print("\n" + "=" * 80)
    print("KEY CONCEPTS")
    print("=" * 80)
    print("""
1. VECTOR DATABASE FEATURES
   - Stores documents with embeddings
   - Fast similarity search
   - Metadata filtering
   - Persistence to disk

2. HOW IT WORKS
   - Documents are converted to embeddings
   - Embeddings stored in optimized index
   - Queries converted to embeddings
   - Find nearest neighbors (similar vectors)

3. DISTANCE METRICS
   - Lower distance = more similar
   - Typically: <0.5 very relevant, 0.5-1.0 somewhat relevant, >1.0 not relevant

4. CHROMADB BENEFITS
   - Simple API
   - Local embeddings (no API keys needed)
   - Fast for <1M documents
   - Easy to get started

5. PRODUCTION ALTERNATIVES
   - Pinecone (managed, scalable)
   - Weaviate (open source, feature-rich)
   - Qdrant (fast, rust-based)
   - pgvector (PostgreSQL extension)
    """)

    print("\n" + "=" * 80)
    print("NEXT STEP: Build a simple RAG system")
    print("=" * 80)


if __name__ == "__main__":
    demo_vector_database()
