from .get_db_table import get_db_table
from .pinecone_api_client import pinecone_client
from .create_embedding import generate_embedding


def insert_records(items):
    db, table = get_db_table()
    pc = pinecone_client()
    index = pc.Index(db)
    vectors = []
    for item in items:
        print(item)
        vector = generate_embedding(item["name"])
        record = {
            "id": item["id"],
            "values": vector,
            "metadata": {"product_name": item["name"]},
        }
        vectors.append(record)

    t = index.upsert(vectors=vectors, namespace=table)
    print("Upserted successfully!")
    return t
