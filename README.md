# AI_Projects
The biggest issue with today’s AI—despite all the hype—is that it can confidently give you the wrong answer. Ask a large language model a straightforward question about your data, whether it’s a PDF, an internal company document, or even today’s news, and it may respond with something that sounds convincing but is completely incorrect—or fail altogether. This behavior, known as hallucination, is the primary obstacle preventing AI from being genuinely reliable and useful.

Fortunately, the solution is simpler than it seems. We don’t need a larger or more powerful model. Instead, we need to let the model work with reference material—essentially giving it an open-book exam. This idea forms the foundation of a technique called Retrieval-Augmented Generation (RAG).

**RAG System**
Forget costly APIs and closed, proprietary platforms. We’ll use the same open-source tools that engineers rely on to build scalable, production-ready systems. Here’s what we’ll work with:
transformers (Hugging Face) – to access a powerful, free large language model
sentence-transformers – for generating high-quality text embeddings with minimal setup
faiss-cpu – Facebook AI’s fast, open-source vector search library, used as our vector store
langchain – used only for its text-splitting utility, saving hours of manual parsing and regex work

**Document Analysis**
Document analysis refers to extracting, interpreting, and understanding the information contained within a document. Traditionally, this involved manual review or simple keyword-based techniques, but with the rise of Large Language Models (LLMs) like GPT and BERT, LLMs are now preferred for document analysis because they can comprehend context, generate summaries, answer questions, and identify key insights efficiently.
