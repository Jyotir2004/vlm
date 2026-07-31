from ollama import chat

response=chat(
model="qwen2.5vl",
messages=[{
"role":"user",
"content":"what is in the image",
"images":["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgpI3xkYAWIYKZhNxNAqZpdT82uLyyOHRqQs27V3Gbcg&s=10.jpg"]

}]


)
print(response["messages"],["content"])

# from ollama import chat

# response = chat(
#     model="qwen2.5vl",
#     messages=[
#         {
#             "role": "user",
#             "content": "What is in this image?",
#             "images": ["image.jpg"]
#         }
#     ]
# )

# print(response["message"]["content"])