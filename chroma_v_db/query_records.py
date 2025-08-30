from .create_db_collection import create_db_collection
from pinecone_v_db.create_embedding import create_embedding


def query_records(queries):
    collection = create_db_collection()
    matched, unmatched = [], []

    for query in queries:
        query_embedding = create_embedding(query)

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=1,
        )
        # print(results)

        ids = results["ids"][0]
        docs = results["documents"][0]
        metas = results["metadatas"][0][0]
        dists = results["distances"][0][0]
        print(dists, type(dists))
        # print(metas)

        record = {
            "query": query,
            "id": ids,
            "name": docs,
            "pcode": metas.get("pcode"),
            "distance": dists,
        }

        if dists <= 1:
            matched.append(record)
        else:
            unmatched.append(query)

    return matched, unmatched
