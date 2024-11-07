import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# Set page title and description
st.title("🏥 Medical Emergency Assistant")
st.markdown("Your AI guide for medical advice and emergency first aid information")

# Important Disclaimer
st.error("""
**IMPORTANT MEDICAL DISCLAIMER**
- This is an AI assistant providing general medical information and first aid guidance
- In case of serious medical emergencies, IMMEDIATELY CALL YOUR LOCAL EMERGENCY SERVICES
- This tool is not a replacement for professional medical advice
- Never take medications without consulting a healthcare professional
- Always get prescriptions from licensed doctors
""")

# Emergency Numbers Section
st.warning("""
**Emergency Contact Numbers:**
- Emergency Services: 911 (US/Canada)
- Poison Control: 1-800-222-1222 (US)
- Emergency Services: 112 (EU)
""")

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="Llama3-8b-8192"
)

# Create medical-specific prompt template
medical_prompt = ChatPromptTemplate.from_template(
    """You are a medical assistant AI trained to provide general medical information and emergency first aid guidance. 
    
    Important Response Guidelines:
    1. Start with urgency level:
       🟢 General Information
       🟡 Seek Medical Attention
       🔴 EMERGENCY - Call emergency services immediately
    
    2. Structure your response in this format:
       - Condition Assessment
       - Immediate Steps
       - General Treatment Category (NO SPECIFIC MEDICINE NAMES)
       - When to Seek Professional Help
    
    3. For medication-related queries:
       - Only mention general categories of medicines (e.g., "pain relievers" not specific brands)
       - Always emphasize "Consult a doctor for proper prescription"
       - Never suggest specific medications or dosages
    
    4. For emergencies:
       - Always start with "Call emergency services immediately"
       - Provide first aid steps while waiting for help
    
    5. If not medical-related:
       Respond with: 'This assistant is trained only for medical and first aid guidance.'

    User Question: {user_input}

    Provide a clear, structured response following the above guidelines."""
)

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask about medical conditions or first aid procedures (Note: For specific medications, please consult a doctor)"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing medical information..."):
            formatted_prompt = medical_prompt.format(user_input=prompt)
            response = llm.invoke(formatted_prompt)
            st.markdown(response.content)
            st.session_state.messages.append({"role": "assistant", "content": response.content})

# Add medical information categories in the sidebar
with st.sidebar:
    st.markdown("""
    ### 🚑 Medical Guidelines
    
    #### First Aid Essentials
    - CPR Steps
    - Bleeding Control
    - Burn Care
    - Choking Response
    - Basic Wound Care
    
    #### Common Conditions
    - Fever Management
    - Allergic Reactions
    - Minor Injuries
    - Common Cold/Flu
    - Digestive Issues
    
    #### When to Call Emergency
    - Chest Pain
    - Severe Bleeding
    - Difficulty Breathing
    - Head Injuries
    - Loss of Consciousness
    
    **Important:** 
    - Always consult healthcare professionals
    - Never self-medicate
    - Get proper prescriptions
    """)

# Footer with additional disclaimer
st.markdown("""
---
**⚕️ Medical Safety Notes:**
- Always consult healthcare professionals for proper diagnosis
- Never take medications without proper prescription
- Keep emergency numbers readily available
- Learn basic first aid from certified instructors
""")