import streamlit as st

st.title("Prueba Chat Sidebar")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Using "with" notation to put chat in sidebar
with st.sidebar:
    # Create a container for messages
    chat_container = st.container()
    
    # Create a container for input at the bottom
    input_container = st.container()
    
    # Display chat messages in the chat container
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    # Put the input field in the input container
    with input_container:
        st.markdown("---")  # Separator line
        if prompt := st.chat_input("What is up?"):
            # Display user message in chat message container
            with chat_container:
                st.chat_message("user").markdown(prompt)
                # Add user message to chat history
                st.session_state.messages.append({"role": "user", "content": prompt})

                response = f"Echo: {prompt}"
                # Display assistant response in chat message container
                with st.chat_message("assistant"):
                    st.markdown(response)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
