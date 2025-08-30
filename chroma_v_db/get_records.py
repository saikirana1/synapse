from chromadb import Client
import chromadb


def get_records():
    chroma_client = chromadb.PersistentClient(path="data")
    collection = chroma_client.get_or_create_collection("ice_creams")

    records = collection.get()

    return records
