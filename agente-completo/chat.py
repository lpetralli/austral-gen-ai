import streamlit as st
from agent import Agent
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
import re
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from tool import create_retriever_tool_from_vectorstore, create_get_car_price_tool


persist_directory = "./chroma_db" 

try:
    vectorstore = Chroma(
        collection_name="rag-chroma",
        embedding_function=OpenAIEmbeddings(),
        persist_directory=persist_directory
    )
    tools = [create_retriever_tool_from_vectorstore(vectorstore), create_get_car_price_tool()]
except Exception as e:
    st.write(f"Error creating vectorstore: {e}")
    tools = None


prompt = """
You are a helpful assistant that can answer questions and help with tasks about AutoCare. Always use the retriever tool to search for information about the company.
"""

if tools:
    agent = Agent(model_type="openai", prompt=prompt, tools=tools)
else:
    st.write("No tools available")
    agent = Agent(model_type="openai", prompt=prompt)


st.title("Agent Chat Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display all previous chat messages
for message in st.session_state.messages:
    if isinstance(message, (HumanMessage, AIMessage)) and message.content:
        with st.chat_message("user" if isinstance(message, HumanMessage) else "assistant"):
            st.markdown(message.content)


# React to user input
if prompt := st.chat_input("User input"):
    # Create a HumanMessage and add it to chat history
    human_message = HumanMessage(content=prompt)
    st.session_state.messages.append(human_message)

    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)

    # Invoke the agent to get a list of AI messages, including potentially retrieved documents
    response_messages = agent.invoke(st.session_state.messages)

    # Update the session state with the new response
    st.session_state.messages = response_messages["messages"]

    # Display only the last AI message with content
    last_message = response_messages["messages"][-1]


    if isinstance(last_message, AIMessage) and last_message.content:
        st.chat_message("assistant").markdown(last_message.content)

