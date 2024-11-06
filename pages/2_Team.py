import streamlit as st


# Set page configuration
st.set_page_config(
    page_title="Team - Healthcare Portal",
    page_icon="🏥",
    layout="wide"
)

# Header
st.markdown("""
    <div style='background-color: #ffffff; padding: 1rem; border-bottom: 2px solid #1e4b7a;'>
        <h1 style='color: #1e4b7a; text-align: center;'>Our Team</h1>
    </div>
""", unsafe_allow_html=True)

# Leadership Team
st.header("Leadership Team")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://placekitten.com/200/200", caption="Dr. John Smith")
    st.subheader("Dr. John Smith")
    st.write("Chief Medical Officer")
    st.write("Specialization: Cardiology")

with col2:
    st.image("https://placekitten.com/201/200", caption="Dr. Sarah Johnson")
    st.subheader("Dr. Sarah Johnson")
    st.write("Medical Director")
    st.write("Specialization: Neurology")

with col3:
    st.image("https://placekitten.com/202/200", caption="Dr. Michael Brown")
    st.subheader("Dr. Michael Brown")
    st.write("Head of Research")
    st.write("Specialization: Oncology")

# Departments
st.header("Our Departments")
departments = {
    "Cardiology": "Heart and cardiovascular care",
    "Neurology": "Brain and nervous system",
    "Pediatrics": "Child healthcare",
    "Orthopedics": "Bone and joint care",
    "Oncology": "Cancer treatment",
    "Emergency Medicine": "24/7 emergency care"
}

col1, col2 = st.columns(2)
for i, (dept, desc) in enumerate(departments.items()):
    with col1 if i % 2 == 0 else col2:
        st.subheader(dept)
        st.write(desc)

