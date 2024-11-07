import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# Set page title and description
st.title("🥗 Nutrition & Health Food Assistant")
st.markdown("Your personal guide for nutrition advice, dietary recommendations, and healthy eating!")

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="Llama3-8b-8192"
)

# Create nutrition-specific prompt template
nutrition_prompt = ChatPromptTemplate.from_template(
    """You are a knowledgeable nutritionist and dietary expert specialized in providing advice about:
    - Nutritional values and benefits of different foods
    - Dietary recommendations for specific health conditions
    - Essential vitamins, minerals, and nutrients
    - Healthy meal planning and food combinations
    - Natural remedies and food-based solutions for common health issues
    
    If the question is not related to nutrition, diet, or food, respond with: 'This chat is trained only for nutrition and dietary guidance.'

    User Question: {user_input}
    
    Please provide a detailed, professional response focusing on nutritional and dietary guidance. 
    When recommending foods, always mention their nutritional benefits and important minerals/vitamins they contain."""
)

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me about nutrition, healthy foods, or dietary advice!"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing nutritional advice..."):
            # Create the full prompt with the user's input
            formatted_prompt = nutrition_prompt.format(user_input=prompt)
            
            # Get response from Groq
            response = llm.invoke(formatted_prompt)
            
            # Display the response
            st.markdown(response.content)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response.content})

# Add nutritional information categories in the sidebar
with st.sidebar:
    st.markdown("""
    ### 🍎 Nutrition Guidelines
    
    #### Essential Categories:
    - **Macronutrients**
        - Proteins
        - Carbohydrates
        - Healthy Fats
    
    - **Micronutrients**
        - Vitamins
        - Minerals
        - Antioxidants
    
    #### Health Conditions:
    - Diabetes Management
    - Heart Health
    - Digestive Issues
    - Weight Management
    - Food Allergies
    - Immune System Support
    
    #### Special Diets:
    - Vegetarian/Vegan
    - Gluten-Free
    - Low-Carb
    - Mediterranean
    - DASH Diet
    
    Ask specific questions about any of these topics!
    """)