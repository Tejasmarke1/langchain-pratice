from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
chat_model = ChatOpenAI(model="gpt-4")
response = chat_model.invoke([{"role": "user", "content": "Tell me a joke about computers."}])
print(response)
