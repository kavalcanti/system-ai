#!/usr/bin/env python3

import openai
import os
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.memory import ConversationBufferWindowMemory
import pathlib


load_dotenv(os.path.join(pathlib.Path(__file__).parent.resolve(),'.env'))
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("MODEL")


def convo():
    ### BASE & SUMMARY IMPLEMENTATION
    # chat mode instance
    _DEFAULT_TEMPLATE = """A system manual and support AI responds to questions from a user.
                        The AI provides short, direct, concise and factual explanations for Linux, Unix and Windows terminal commands.
                        The AI makes consistent use of examples and lists.
                        When a command has common additional parameters or flags those are mentioned.
                        If the AI does not know the answer to a question, it truthfully says it does not know.
                        {chat_history_lines}
                        Human: {input}
                        AI:"""

    prompt = PromptTemplate(
        input_variables=["input", "chat_history_lines"], template=_DEFAULT_TEMPLATE
    )
    
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    conv_memory = ConversationBufferWindowMemory(k=4, return_messages=True, memory_key="chat_history_lines", input_key="input")
    llm = ChatOpenAI(streaming=True, model=MODEL, callback_manager=callback_manager, verbose=True, temperature=0)
    
    convo = ConversationChain(memory=conv_memory, prompt=prompt, llm=llm)
    
    print('Welcome to the System Manual Submind.\n\nThis submind has limited contextual memory.\nKeep queries short and to the point!')

    msg = ''
    while msg is not None:
        msg = input('\nMSG: ')
        if msg:
            print('SMS')
            convo.predict(input=msg)
            print('')
        else:
            break
            

if __name__ == '__main__':
    convo()