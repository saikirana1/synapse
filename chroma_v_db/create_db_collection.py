import chromadb


def create_db_collection():
    chroma_client = chromadb.PersistentClient(path="data")
    collection = chroma_client.get_or_create_collection(name="ice_creams")
    print(collection.count())
    return collection
