from dotenv import load_dotenv

import os


def table_headers():
    load_dotenv()

    pinecone_api_key = os.getenv("pinecone_api_key")
    index_host = os.getenv("host")

    if not index_host or "https" in index_host.lower():
        raise ValueError(f"Invalid INDEX_HOST: {index_host}")

    url = f"https://{index_host}/namespaces"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Api-Key": pinecone_api_key,
        "X-Pinecone-API-Version": "2025-10",
    }
    return url, headers
