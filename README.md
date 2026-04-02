# invoice-search-and-retrieval-system
The Invoice Search & Retrieval System is a Retrieval-Augmented Generation (RAG)-based application designed to efficiently extract, search, and analyze information from invoice documents across multiple sellers and clients.

This system enables users to upload invoice PDFs and interact with them using natural language queries. It leverages advanced document parsing, semantic search, and large language models to provide accurate, context-aware responses from unstructured invoice data.

The application processes invoices by segmenting them into meaningful sections such as seller details, client information, itemized lists, and financial summaries. These segments are converted into vector embeddings and stored in a vector database, enabling fast and relevant information retrieval.

Users can perform tasks such as:

- Extracting invoice details (e.g., seller name, tax ID, total amount)
- Searching invoices by client, product, or date
- Retrieving item-level insights from multiple invoices
- Summarizing invoice contents
- Performing cross-invoice queries for better decision-making

The system supports metadata-based filtering (e.g., seller, client, invoice date) and combines semantic search with structured querying to improve accuracy and performance.

⚙️ Key Technologies
- Retrieval-Augmented Generation (RAG)
- Vector Database (Pinecone)
- Embedding Models (OpenAI)
- LLMs for natural language understanding
- PDF parsing and text extraction

🎯 Key Features
- Natural language querying over invoice data
- Semantic search across multiple documents
- Context-aware answer generation
- Multi-invoice comparison
- Structured data extraction from unstructured PDFs