#!/usr/bin/env python
# coding: utf-8

# In[11]:


from langchain.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,AIMessagePromptTemplate,HumanMessagePromptTemplate

from src.Content import Papers_With_Code
from src.OpenAI import ChatAgent

import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


# In[12]:


class WhatsappBot:
    def __init__(self):
        self.__Paper = self.__Get_Paper()
        self.__Agent = self.__Get_Chat_Agent()

    def __Get_Paper(self):
        PaperObject = Papers_With_Code()
        ContentDict = PaperObject.Get_Content()
        return ContentDict
    
    def __Get_Chat_Agent(self):
        AgentObject = ChatAgent()
        Agent = AgentObject.Get_Chat_Agent()
        return Agent
    
    def __Read_System_Prompt(self,file='./Prompts/SystemPrompt.txt'):
        System_Prompt = open(file,'r').read()
        return SystemMessagePromptTemplate.from_template(System_Prompt)
    
    def __Read_Chat_Prompt(self):
        return ChatPromptTemplate.from_messages([self.__System_Message_Prompt])
    
    def Create_Post(self):
        self.__System_Message_Prompt = self.__Read_System_Prompt()
        self.__Chat_Message_Prompt = self.__Read_Chat_Prompt()

        ContentDict = self.__Paper
        Title = ContentDict['Title']
        Abstract = ContentDict['Abstract']
        Github_Link = ContentDict['Github']
        ARXIV_Link = ContentDict['Arxiv']
        Media = ContentDict['Media']
        Output = self.__Agent(self.__Chat_Message_Prompt.format_prompt(title=Title,abstract=Abstract,github=Github_Link,arxiv=ARXIV_Link).to_messages())
        return Output

    def Upload_To_Whatsapp(self,Msg,Phone_numbers):
        for phone in Phone_numbers:
            try:
                pywhatkit.sendwhatmsg_instantly(phone, Msg)
                time.sleep(10)
                time.sleep(2)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(3)
            except Exception as e:
                print(str(e))


# In[13]:


obj = WhatsappBot()
post = obj.Create_Post().content + '\n----------'
print(post)


# In[14]:


Phone_numbers = []
with open('./PhoneNumbers.txt','r') as f:
    Phone_numbers = f.read().split('\n')
obj.Upload_To_Whatsapp(post,Phone_numbers)

