"""
Setup ChromaDB with Sample Data for UI

This creates a persistent ChromaDB database with sample data
that you can view in the ChromaDB UI.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions


def setup_sample_database():
    """Create persistent ChromaDB with sample data"""

    print("=" * 80)
    print("SETTING UP CHROMADB WITH SAMPLE DATA")
    print("=" * 80)

    # Create persistent client
    db_path = "./chroma_data"
    print(f"\nCreating database at: {db_path}")

    client = chromadb.PersistentClient(path=db_path)

    # Setup embedding function
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

    # Create collection
    print("\nCreating collection: 'sample_docs'")
    collection = client.get_or_create_collection(
        name="sample_docs",
        embedding_function=embedding_fn,
        metadata={"description": "Sample documents for demo"}
    )

    # Add sample documents
    print("\nAdding sample documents...")
    documents = [
        {
            'id': 'python-1',
            'text': 'Python is a high-level programming language known for its simplicity and readability. It is widely used in data science, machine learning, and web development.',
            'metadata': {'topic': 'programming', 'language': 'python', 'difficulty': 'beginner'}
        },
        {
            'id': 'javascript-1',
            'text': 'JavaScript is the programming language of the web. It runs in browsers and on servers with Node.js. Modern JavaScript includes features like async/await and modules.',
            'metadata': {'topic': 'programming', 'language': 'javascript', 'difficulty': 'beginner'}
        },
        {
            'id': 'ml-1',
            'text': 'Machine learning is a subset of artificial intelligence that enables computers to learn from data. Popular frameworks include TensorFlow and PyTorch.',
            'metadata': {'topic': 'ai', 'subtopic': 'machine-learning', 'difficulty': 'intermediate'}
        },
        {
            'id': 'nn-1',
            'text': 'Neural networks are computing systems inspired by biological neural networks. They consist of layers of interconnected nodes that process information.',
            'metadata': {'topic': 'ai', 'subtopic': 'neural-networks', 'difficulty': 'advanced'}
        },
        {
            'id': 'rag-1',
            'text': 'RAG (Retrieval Augmented Generation) combines information retrieval with language model generation. It allows LLMs to access external knowledge bases.',
            'metadata': {'topic': 'ai', 'subtopic': 'rag', 'difficulty': 'advanced'}
        },
        {
            'id': 'vector-db-1',
            'text': 'Vector databases store embeddings and enable semantic search. Popular options include ChromaDB, Pinecone, and Weaviate.',
            'metadata': {'topic': 'databases', 'subtopic': 'vector-db', 'difficulty': 'intermediate'}
        },
        {
            'id': 'web-scraping-1',
            'text': 'Web scraping extracts data from websites using tools like BeautifulSoup and Scrapy. It is useful for building datasets and monitoring content.',
            'metadata': {'topic': 'data-collection', 'subtopic': 'scraping', 'difficulty': 'beginner'}
        },
        {
            'id': 'embeddings-1',
            'text': 'Embeddings are vector representations of text that capture semantic meaning. Similar texts have similar embeddings, enabling semantic search.',
            'metadata': {'topic': 'ai', 'subtopic': 'embeddings', 'difficulty': 'intermediate'}
        }
    ]

    collection.add(
        documents=[doc['text'] for doc in documents],
        ids=[doc['id'] for doc in documents],
        metadatas=[doc['metadata'] for doc in documents]
    )

    print(f"Added {len(documents)} documents")
    print(f"Total documents in collection: {collection.count()}")

    # Show sample query
    print("\n" + "=" * 80)
    print("TESTING SEARCH")
    print("=" * 80)

    query = "How do I build AI applications?"
    print(f"\nQuery: '{query}'")

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    print("\nTop 3 results:")
    for i, (doc, distance, metadata) in enumerate(zip(
        results['documents'][0],
        results['distances'][0],
        results['metadatas'][0]
    ), 1):
        print(f"\n{i}. Distance: {distance:.3f}")
        print(f"   Topic: {metadata.get('topic')} / {metadata.get('subtopic', 'N/A')}")
        print(f"   Text: {doc[:100]}...")

    print("\n" + "=" * 80)
    print("SETUP COMPLETE!")
    print("=" * 80)
    print(f"\nDatabase created at: {Path(db_path).absolute()}")
    print("\nTo view in UI, run:")
    print(f"  chroma run --path {db_path} --port 8000")
    print("\nThen open: http://localhost:8000")


if __name__ == "__main__":
    setup_sample_database()
