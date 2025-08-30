import base64
from pathlib import Path
from pydantic import BaseModel
from .openai_client import openai_client

client = openai_client()


class Product(BaseModel):
    name: str


def extract_text(image_path: str):
    with open(image_path, "rb") as f:
        base64_image = base64.b64encode(f.read()).decode("utf-8")

    prompt = "Based on the given product photo, extract the product name. Do not include the company name - only the product name"

    response = client.chat.completions.parse(
        model="gpt-4.1",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ],
        response_format=Product,
    )

    return response.choices[0].message.parsed
