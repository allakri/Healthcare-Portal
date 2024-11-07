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
        <h2 style='color: #1e4b7a;'>Our Mission</h2>
        <p style='font-size: 1.1rem;'>To provide accessible and high-quality healthcare services to our community.</p>
    </div>
""", unsafe_allow_html=True)

# About Content
col1, col2 = st.columns(2)

with col1:
    st.header("Who We Are")
    st.write("""
    We are a dedicated healthcare provider focused on excellence in patient care.
    """)

with col2:
    st.header("Our Values")
    st.write("""
    - Patient-Centered Care
    - Community Service
    - Professional Integrity
    """)

# Statistics
st.header("Our Impact")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Patients Served", "50,000+")
col2.metric("Medical Staff", "200+")
col3.metric("Departments", "15")
col4.metric("Years of Service", "20+")

# Footer
st.markdown("""
    <div style='text-align: center; margin-top: 2rem;'>
        <p style='color: #1e4b7a;'>Together, we can achieve better health for all.</p>
    </div>
""", unsafe_allow_html=True)
