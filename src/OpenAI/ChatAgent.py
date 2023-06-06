from langchain.chat_models import ChatOpenAI
import os
import dotenv

class ChatAgent:
    def __init__(self):
        self.__Setup_Chat_Agent()
    
    def __Setup_Chat_Agent(self):
        dotenv.load_dotenv('Credentials.env')
        os.getenv('OPENAI_API_KEY')
        self.Agent = ChatOpenAI(temperature=0)
    
    def Get_Chat_Agent(self):
        return self.Agent