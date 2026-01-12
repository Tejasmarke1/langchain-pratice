from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
chat_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

response = chat_model.invoke("what is capital of india?")
print(response.content)
