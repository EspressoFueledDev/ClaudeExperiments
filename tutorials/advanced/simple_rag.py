"""
Tutorial: Building a Simple RAG System

RAG (Retrieval Augmented Generation) combines:
1. Information retrieval (vector search)
2. Text generation (Claude)

This gives Claude access to your specific knowledge base.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import chromadb
from chromadb.utils import embedding_functions
from utils.claude_helper import call_haiku


class SimpleRAG:
    """Simple RAG system combining ChromaDB + Claude"""

    def __init__(self, collection_name="rag_docs"):
        """Initialize RAG system"""
        print("Initializing RAG system...")

        # Set up ChromaDB
        self.client = chromadb.Client()

        # Use local embeddings
        self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )

        # Create collection
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedding_function
        )

        print(f"RAG system ready. Documents: {self.collection.count()}")

    def add_documents(self, documents):
        """
        Add documents to knowledge base

        Args:
            documents: List of dicts with 'id', 'text', 'metadata'
        """
        ids = [doc['id'] for doc in documents]
        texts = [doc['text'] for doc in documents]
        metadatas = [doc.get('metadata', {}) for doc in documents]

        self.collection.add(
            documents=texts,
            ids=ids,
            metadatas=metadatas
        )

        print(f"Added {len(documents)} documents")

    def retrieve(self, query, n_results=3):
        """
        Retrieve relevant documents

        Args:
            query: Search query
            n_results: Number of results to return

        Returns:
            List of relevant document texts
        """
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )

        # Extract just the text
        docs = results['documents'][0]
        distances = results['distances'][0]

        # Show what was retrieved
        print(f"\nRetrieved {len(docs)} documents:")
        for i, (doc, dist) in enumerate(zip(docs, distances), 1):
            print(f"{i}. (distance: {dist:.3f}) {doc[:60]}...")

        return docs

    def generate_answer(self, query, context_docs):
        """
        Generate answer using Claude with context

        Args:
            query: User question
            context_docs: Retrieved documents for context

        Returns:
            Claude's answer
        """
        # Build context from retrieved documents
        context = "\n\n".join([
            f"Document {i+1}:\n{doc}"
            for i, doc in enumerate(context_docs)
        ])

        # Create prompt with context
        prompt = f"""Answer the question based on the provided context documents.

Context:
{context}

Question: {query}

Instructions:
- Use information from the context documents
- If the answer isn't in the context, say so
- Be concise and accurate
- Cite which document(s) you used

Answer:"""

        print("\nGenerating answer with Claude...")
        answer = call_haiku(prompt, max_tokens=2048)

        return answer

    def query(self, question, n_results=3):
        """
        Complete RAG query: retrieve + generate

        Args:
            question: User question
            n_results: Number of documents to retrieve

        Returns:
            Generated answer
        """
        print("=" * 80)
        print(f"QUERY: {question}")
        print("=" * 80)

        # Step 1: Retrieve relevant documents
        docs = self.retrieve(question, n_results)

        # Step 2: Generate answer with context
        answer = self.generate_answer(question, docs)

        return answer


def demo_rag_system():
    """Demo the RAG system"""

    print("=" * 80)
    print("SIMPLE RAG SYSTEM")
    print("=" * 80)

    # Initialize RAG
    rag = SimpleRAG(collection_name="demo_rag")

    # Sample knowledge base (imagine this is from web scraping)
    documents = [
        {
            'id': 'python-basics',
            'text': 'Python is a high-level programming language created by Guido van Rossum in 1991. It emphasizes code readability with significant whitespace. Python supports multiple programming paradigms including procedural, object-oriented, and functional programming.',
            'metadata': {'topic': 'python', 'category': 'basics'}
        },
        {
            'id': 'python-ml',
            'text': 'Python is the dominant language for machine learning and AI. Popular libraries include TensorFlow, PyTorch, scikit-learn, and NumPy. Its simple syntax and extensive ecosystem make it ideal for data science and ML development.',
            'metadata': {'topic': 'python', 'category': 'ml'}
        },
        {
            'id': 'python-web',
            'text': 'Python web frameworks include Django, Flask, and FastAPI. Django is a full-featured framework following the "batteries included" philosophy. Flask is lightweight and flexible. FastAPI is modern and fast, with automatic API documentation.',
            'metadata': {'topic': 'python', 'category': 'web'}
        },
        {
            'id': 'javascript-basics',
            'text': 'JavaScript was created by Brendan Eich in 1995. It is the programming language of the web, running in all web browsers. Modern JavaScript (ES6+) includes features like arrow functions, promises, async/await, and modules.',
            'metadata': {'topic': 'javascript', 'category': 'basics'}
        },
        {
            'id': 'javascript-frameworks',
            'text': 'Popular JavaScript frameworks include React, Vue, and Angular. React, developed by Facebook, uses a component-based architecture and virtual DOM. Vue is progressive and easy to learn. Angular is a full framework from Google.',
            'metadata': {'topic': 'javascript', 'category': 'frameworks'}
        },
        {
            'id': 'rag-concept',
            'text': 'RAG (Retrieval Augmented Generation) combines information retrieval with language model generation. It allows LLMs to access external knowledge bases, reducing hallucinations and providing up-to-date information. RAG systems typically use vector databases for semantic search.',
            'metadata': {'topic': 'ai', 'category': 'rag'}
        }
    ]

    # Add documents to knowledge base
    print("\nAdding documents to knowledge base...")
    rag.add_documents(documents)

    # Test queries
    print("\n" + "=" * 80)
    print("TESTING RAG QUERIES")
    print("=" * 80)

    questions = [
        "Who created Python and when?",
        "What are the best Python libraries for machine learning?",
        "What is RAG and how does it work?",
        "What are popular JavaScript frameworks?"
    ]

    for question in questions:
        answer = rag.query(question, n_results=2)

        print("\n" + "-" * 80)
        print("ANSWER:")
        print("-" * 80)
        print(answer)
        print("\n")

    # Explain the architecture
    print("=" * 80)
    print("RAG ARCHITECTURE")
    print("=" * 80)
    print("""
HOW IT WORKS:

1. INDEXING (one-time)
   - Split documents into chunks
   - Generate embeddings for each chunk
   - Store in vector database

2. RETRIEVAL (per query)
   - Convert user question to embedding
   - Find similar document embeddings
   - Retrieve top-k most relevant documents

3. GENERATION (per query)
   - Inject retrieved documents into prompt
   - Send to Claude as context
   - Claude generates answer based on context

BENEFITS:
- Gives Claude access to your specific data
- Reduces hallucinations
- Answers based on real documents
- Can cite sources
- Up-to-date information

LIMITATIONS:
- Quality depends on retrieval accuracy
- Limited by context window size
- May miss information in poor chunking
- Embeddings may not capture all nuances

NEXT STEPS:
- Add more documents (web scraping)
- Improve chunking strategy
- Hybrid search (keyword + semantic)
- Re-ranking results
- Add citation tracking
    """)


if __name__ == "__main__":
    demo_rag_system()
