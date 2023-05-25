#!/usr/bin/env python3
 import os
import time
from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain.callbacks import BaseCallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.memory import ConversationBufferWindowMemory

script_path = os.path.realpath(__file__)
dir_path = os.path.dirname(script_path)

load_dotenv(os.path.join(dir_path,'.env'))
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("MODEL")

message = [
'-------------------------------------------------------------------------',
'|   _____ __  __  _____                                                 |',
'|  / ____|  \/  |/ ____|  The System Manual Submind assists with CLI.   |',
'| | (___ | \  / | (___    This instance has limited contextual memory.  |',
'|  \___ \| |\/| |\___ \                                                 |',
'|  ____) | |  | |____) |  Keep queries short and on topic!              |',
'| |_____/|_|  |_|_____/   Hit escape on empty message field to exit.    |',
'-------------------------------------------------------------------------'
]
for line in message:
    print(line)
    time.sleep(0.03)


def convo():
    ### BASE & SUMMARY IMPLEMENTATION
    # chat mode instance
    _DEFAULT_TEMPLATE = """A system manual and support AI responds to questions from a user.
                        The AI provides short, direct, concise and factual explanations for Linux, Unix and Windows terminal commands.
                        The AI makes consistent use of examples and provides listed and markdown commands when possible.
                        When a command has common additional parameters or flags those are mentioned.
                        If the AI does not know the answer to a question, it truthfully says it does not know.
                        {chat_history_lines}
                        User: {input}
                        AI:"""

    prompt = PromptTemplate(
        input_variables=["input", "chat_history_lines"], template=_DEFAULT_TEMPLATE
    )

    callback_manager = BaseCallbackManager([StreamingStdOutCallbackHandler()])
    conv_memory = ConversationBufferWindowMemory(k=4, return_messages=True, memory_key="chat_history_lines", input_key="input")
    llm = ChatOpenAI(streaming=True, model=MODEL, callback_manager=callback_manager, verbose=True, temperature=0)

    convo = ConversationChain(memory=conv_memory, prompt=prompt, llm=llm)

    msg = ''
    while msg is not None:
        msg = input('\nUSR:')
        if msg:
            print('\nSMS:')
            convo.predict(input=msg)
            print('')
        else:
            print('\nSMS:\nGoodbye!')
            break


if __name__ == '__main__':
    convo()
