import streamlit as st


def main():
    # Set page configuration
    st.set_page_config(
        page_title="Healthcare Portal",
        page_icon="🏥",
        layout="wide"
    )

    # Header
    st.markdown("""
        <div style='background-color: #ffffff; padding: 1rem; border-bottom: 2px solid #1e4b7a;'>
            <h1 style='color: #1e4b7a; text-align: center;'>Healthcare Portal</h1>
        </div>
    """, unsafe_allow_html=True)

    # Home Page Content
    st.title("Welcome to Healthcare Portal")
    
    # Hero Section
    st.markdown("""
        <div style='background-color: #f0f9ff; padding: 2rem; border-radius: 10px;'>
            <h2 style='color: #1e4b7a;'>Your Health, Our Priority</h2>
            <p style='font-size: 1.2rem;'>Providing quality healthcare services and information to our community.</p>
        </div>
    """, unsafe_allow_html=True)

    # Featured Services
    st.header("Our Services")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🏥 Emergency Care")
        st.write("24/7 emergency medical services")

    with col2:
        st.markdown("### 👨‍⚕️ Expert Doctors")
        st.write("Experienced healthcare professionals")

    with col3:
        st.markdown("### 🧪 Modern Facilities")
        st.write("State-of-the-art medical equipment")

    # Latest Updates
    st.header("Latest Updates")
    st.info("COVID-19 Vaccination Drive: Schedule your appointment today!")
    st.success("New Department: Pediatric Care Unit Now Open")


if __name__ == "__main__":
    main() 