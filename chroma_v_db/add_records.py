from .create_db_collection import create_db_collection
from pinecone_v_db.create_embedding import create_embedding


def add_records(items):
    collection = create_db_collection()
    for item in items:
        print(item)
        embedding = create_embedding(item["name"])

        collection.add(
            ids=[item["id"]],
            documents=[item["name"]],
            embeddings=[embedding],
            metadatas=[{"pcode": item["pcode"]}],
        )
