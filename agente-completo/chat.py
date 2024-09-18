import streamlit as st
from agent import Agent
from langchain_core.messages import HumanMessage, AIMessage

tools = None

prompt = "Be a helpful assistant"

if tools:
    agent = Agent(model_type="groq", tools=tools, prompt=prompt)
else:
    agent = Agent(model_type="groq", prompt=prompt)


st.title("Chatbot")

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
    st.session_state.messages.extend(response_messages)

    # Display only the last AI message with content
    last_message = response_messages[-1]
    if isinstance(last_message, AIMessage) and last_message.content:
        st.chat_message("assistant").markdown(last_message.content)