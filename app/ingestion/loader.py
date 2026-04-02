from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents import Document
from app.ingestion.invoice_parser import parse_invoice
import os

def load_pdfs_from_folder(folder_path: str):

    documents = []

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            file_path = os.path.join(folder_path, file)

            # -------- Extract raw text --------
            loader = PyMuPDFLoader(file_path)
            docs = loader.load()
            full_text = "\n".join([doc.page_content for doc in docs])

            # -------- LLM Parsing --------
            parsed = parse_invoice(full_text)

            page_content = parsed.get("page_content", "")
            metadata = parsed.get("metadata", {})

            # -------- Final Document --------
            document = Document(
                page_content=page_content,
                metadata={
                    "source": file,
                    "file_path": file_path,
                    "invoice_no": metadata.get("invoice_no"),
                    "client_name": metadata.get("client_name"),
                    "seller_name": metadata.get("seller_name"),
                    "date": metadata.get("date"),
                    "total_amount": metadata.get("total_amount"),
                }
            )

            documents.append(document)

    return documents