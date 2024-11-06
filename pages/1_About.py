import streamlit as st


# Set page configuration
st.set_page_config(
    page_title="About - Healthcare Portal",
    page_icon="🏥",
    layout="wide"
)

# Header
st.markdown("""
    <div style='background-color: #ffffff; padding: 1rem; border-bottom: 2px solid #1e4b7a;'>
        <h1 style='color: #1e4b7a; text-align: center;'>About Us</h1>
    </div>
""", unsafe_allow_html=True)

# Mission Statement
st.markdown("""
    <div style='background-color: #f0f9ff; padding: 2rem; border-radius: 10px; margin-bottom: 2rem;'>
        <h2 style='color: #1e4b7a;'>Our Mission</h2>
        <p style='font-size: 1.1rem;'>To provide accessible, high-quality healthcare services and information to our community.</p>
    </div>
""", unsafe_allow_html=True)

# About Content
col1, col2 = st.columns(2)

with col1:
    st.header("Who We Are")
    st.write("""
    We are a leading healthcare provider committed to excellence in patient care. 
    With over 20 years of experience, we have been serving our community with 
    dedication and compassion.
    """)

with col2:
    st.header("Our Values")
    st.write("""
    - Excellence in Healthcare
    - Patient-Centered Care
    - Innovation & Research
    - Community Service
    - Professional Development
    """)

# Statistics
st.header("Our Impact")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Patients Served", "50,000+")
col2.metric("Medical Staff", "200+")
col3.metric("Departments", "15")
col4.metric("Years of Service", "20+")

