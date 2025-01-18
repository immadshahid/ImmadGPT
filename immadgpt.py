import streamlit as st
import openai

# Set up Azure OpenAI API credentials
openai.api_type = "azure"
openai.api_key = "OPEN-API-KEY"  # Replace with your actual key
openai.api_base = "https://mansai.openai.azure.com/"
openai.api_version = "2023-03-15-preview"  # Update if needed

# Streamlit app
st.title("ImmadGPT")
st.write("🤖 Hello! Ask me anything ;)")

# Initialize chat history if not already stored
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a friendly and conversational educational assistant that engages in interactive discussions."}
    ]

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg['content'])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(msg['content'])

# Input from user
user_input = st.chat_input("Type your message here...")

if user_input:
    # Append user input to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)
    
    with st.spinner("Thinking...;)"):
        try:
            # Get response from OpenAI
            response = openai.ChatCompletion.create(
                engine="gpt-4o",  # Replace with your Azure OpenAI deployment name
                messages=st.session_state.messages,
            )
            answer = response['choices'][0]['message']['content']
            
            # Append chatbot response to chat history
            st.session_state.messages.append({"role": "assistant", "content": answer})
            
            with st.chat_message("assistant"):
                st.markdown(answer)
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown("🤖 Powered by Azure OpenAI and Streamlit")
