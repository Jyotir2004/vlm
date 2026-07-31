import requests
from ollama import chat
import os

image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpSk86m5nPN1QAB-t7JmlLB-kPQOBGp_-JML69lwYjsA&s=10"

# Download the image
response = requests.get(image_url)
response.raise_for_status()

image_path = "temp_image.jpg"

with open(image_path, "wb") as f:
    f.write(response.content)

# Send the image to Ollama
response = chat(
    model="qwen2.5vl",
    messages=[
        {
            "role": "user",
            "content": "Describe this image in detail.",
            "images": [image_path],
        }
    ],
)

print(response.message.content)

# Optional: remove the temporary file
os.remove(image_path)