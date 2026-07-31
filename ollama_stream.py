from langchain_ollama import ChatOllama

model=ChatOllama(model="gemma3:4b")

while True:
    user_input="",
    user_input=input(),
    response=model.stream(user_input)
    
    print(response)

    for chunk in response:
        print(chunk.content,end="",flush=True)
