# from pinecone_v_db.create_db import create_or_get_db

# from pinecone_v_db.create_table import create_table
# import json
# from pinecone_v_db.insert_records import insert_records

from open_ai.image_to_text import extract_text
# from open_ai.filter_records import filter_records
# print(t)

# t = create_table()
# print(t)
# with open("data.json", "r") as f:
#     data = json.load(f)
# t = insert_records(data)
# print(t)
# r = []


# data = t.name

# r.append(data)

# print(data)
# print(r)

# da = filter_records(r)
# print(da)

# from chroma_v_db.add_records import add_records


# from chroma_v_db.create_db import create_db

# t = create_db()
# print(t)

# t = add_records(data)
# print(t)
from chroma_v_db.query_records import query_records

# queries = ["Vanilla Ice Cream Tub", "Strawberry Sundae"]
# matched, unmatched = query_records(queries)

# print("Matched:", matched)
# print("Unmatched:", unmatched)
# r = []
# t = extract_text("image-3.png")


# data = t.name

# r.append(data)

# print(data)
# print(r)

# da = filter_records(r)
# print(da)


# r = []
# t = extract_text("image-3.png")


# data = t.name

# r.append(data)

# print(data)
# print(r)

# da = filter_records(r)
# print(da)

# import json
# from chroma_v_db.add_records import add_records


# with open("products.json", "r") as f:
#     data = json.load(f)
#     t = add_records(data)
#     print(t)

# from chroma_v_db.create_db_collection import create_db_collection
from chroma_v_db.get_records import get_records

t = extract_text("image.png")
r = []


data = t.name

r.append(data)

print(r)
# print(r)

t = query_records(r)
print(t)
# t = get_records()
# print(t)
