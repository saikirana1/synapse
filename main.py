# from pinecone_v_db.create_db import create_or_get_db

# from pinecone_v_db.create_table import create_table
# import json
# from pinecone_v_db.insert_records import insert_records

from open_ai.image_to_text import extract_text
from open_ai.filter_records import filter_records
# print(t)

# t = create_table()
# print(t)
# with open("data.json", "r") as f:
#     data = json.load(f)
# t = insert_records(data)
# print(t)
r = []
t = extract_text("image-3.png")


data = t.name

r.append(data)

print(data)
print(r)

da = filter_records(r)
print(da)
