from app.ingestion.loader import load_pdfs_from_folder

docs = load_pdfs_from_folder("data")

print(len(docs))
print(docs[0])
