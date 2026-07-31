from langchain_ollama import ChatOllama

model=ChatOllama(model="gemma3:4b")

while True:
    user_input="",
    user_input=input("hey:"),
    response=model.invoke(user_input)

    print(response.content)

