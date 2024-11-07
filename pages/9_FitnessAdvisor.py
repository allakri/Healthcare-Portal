import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# Set page title
st.title("🏋️‍♀️ AI Fitness Assistant")
st.markdown("Your personal guide for yoga, exercises, and fitness advice!")

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="Llama3-8b-8192"
)

# Create fitness-specific prompt template
fitness_prompt = ChatPromptTemplate.from_template(
    """You are a virtual fitness assistant specialized in yoga, exercises, and fitness guidance.
    Please provide helpful fitness advice and answer questions related to fitness.
    If the question is not related to fitness, respond with: 'This chat is trained for only fitness programs.'

    User Question: {user_input}
    
    Please provide a detailed, professional response focusing on fitness guidance."""
)

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me about fitness, yoga, or exercises!"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Create the full prompt with the user's input
            formatted_prompt = fitness_prompt.format(user_input=prompt)
            
            # Get response from Groq
            response = llm.invoke(formatted_prompt)
            
            # Display the response
            st.markdown(response.content)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response.content})

# Add some helpful information in the sidebar
with st.sidebar:
    st.markdown("""
    ### 💪 What can I help you with?
    - Yoga poses and techniques
    - Exercise routines
    - Fitness tips and advice
    - Workout planning
    - Stretching guidance
    - General fitness questions
    """)