from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import chainlit as cl

@cl.on_chat_start
async def start():
    """
    Initializes the bot when a new chat starts.

    This asynchronous function creates a new instance of the retrieval QA bot,
    sends a welcome message, and stores the bot instance in the user's session.
    """
    welcome_message = cl.Message(content="Starting the bot...")
    await welcome_message.send()
    welcome_message.content = (
        "Hi, Welcome to Chat With Documents using Ollama (mistral model) and LangChain."
    )
    await welcome_message.update()
    # cl.user_session.set("chain", chain)


# @cl.step
# def proccess_message(message: str):
#     """
#     This function processes the user's message.

#     Args:
#         message: The user's message.

#     Returns:
#         None.
#     """
#     # Process the message
#     return chain.invoke({"input": message})


@cl.on_message  # this function will be called every time a user inputs a message in the UI
async def main(message: cl.Message):
    """
    This function is called every time a user inputs a message in the UI.
    It sends back an intermediate response from the tool, followed by the final answer.

    Args:
        message: The user's message.

    Returns:
        None.
    """
    # Call the tool
    
    # result = proccess_message(message=message.content)
    result = chain.invoke({"input": message.content})
    print(type(result))
    # Send the final answer.
    await cl.Message(content=result).send()

llm = Ollama(model="mistral")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are Astana Travel Guide."),
    ("user", "{input}")
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

# result = chain.invoke({"input": "Hello, I want to make 3 day trip Astana. Can you help me with that?"})

