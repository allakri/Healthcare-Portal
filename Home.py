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
    st.title("Welcome to the Healthcare Portal")
    
    # Hero Section
    st.markdown("""
        <div style='background-color: #ffffff; padding: 2rem; border-radius: 10px; text-align: center;'>
    <h2 style='color: #1e4b7a;'>Your Health, Our Priority</h2>
    <p style='font-size: 1.2rem; color: black;'>Providing quality healthcare services and information to our community.</p>
    <p style='font-size: 1.2rem; font-weight: bold; color: black;'>Explore our services below!</p>
</div>
    """, unsafe_allow_html=True)

    # Featured Services
    st.header("Our Services")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("### 🏥 Healthcare Take")
        st.write("Comprehensive health check-ups and consultations.")

    with col2:
        st.markdown("### 📊 Report Analysis")
        st.write("In-depth analysis of your health reports.")

    with col3:
        st.markdown("### 🥗 Food & Nutrition Advisor")
        st.write("Personalized dietary advice for a healthier you.")

    with col4:
        st.markdown("### 💊 Medication Advisor")
        st.write("Guidance on medications and treatment plans.")

if __name__ == "__main__":
    main()
