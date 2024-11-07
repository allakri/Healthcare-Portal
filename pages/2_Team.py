import streamlit as st
from PIL import Image
import base64
from pathlib import Path

# Set page configuration
st.set_page_config(
    page_title="Healthcare Team Portal",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
    <style>
        .stApp {
            background-color: #f8f9fa;
        }
        .team-header {
            background: linear-gradient(135deg, #1e4b7a, #2980b9);
            padding: 2rem;
            border-radius: 0 0 20px 20px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .team-title {
            color: white;
            text-align: center;
            font-size: 3rem;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }
        .team-subtitle {
            color: #e0e0e0;
            text-align: center;
            font-size: 1.2rem;
            margin-top: 0.5rem;
        }
        .team-card {
            background: white;
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .team-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
        .member-image {
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 1rem;
        }
        .member-name {
            color: #1e4b7a;
            font-size: 1.5rem;
            font-weight: bold;
            margin: 0.5rem 0;
        }
        .member-title {
            color: #2980b9;
            font-size: 1.1rem;
            font-style: italic;
        }
        .member-spec {
            color: #666;
            font-size: 1rem;
            margin: 0.5rem 0;
        }
        .member-mission {
            background: #f8f9fa;
            padding: 0.8rem;
            border-radius: 10px;
            margin: 0.8rem 0;
        }
        .member-contact {
            margin-top: 1rem;
            padding-top: 0.8rem;
            border-top: 1px solid #eee;
        }
        .section-header {
            color: #1e4b7a;
            text-align: center;
            margin: 2rem 0;
            font-size: 2rem;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
    <div class="team-header">
        <h1 class="team-title">Our Healthcare Team</h1>
        <p class="team-subtitle">Dedicated to Innovation and Excellence in Healthcare</p>
    </div>
""", unsafe_allow_html=True)

# Team Section Header
st.markdown('<h2 class="section-header">Leadership Team</h2>', unsafe_allow_html=True)

def display_team_member(name, title, specialization, img_path, mission, contact_info):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # st.markdown('<div class="team-card">', unsafe_allow_html=True)
        
        # Image handling with error management
        try:
            img = Image.open(img_path)
            st.image(img, width=200, use_column_width=True, output_format="PNG", 
                        caption="", clamp=True)
        except Exception as e:
            st.image("https://via.placeholder.com/200x250?text=Photo+Not+Found", 
                    width=200, use_column_width=True)
        st.markdown(f"""
            <h3 class="member-name" style="color: brown;">{name}</h3>
            <p class="member-title" style="color: brown;">{title}</p>
            <p class="member-spec" style="color: brown;">🎯 Specialization: {specialization}</p>
            <div class="member-mission" style="color: brown;">
                <strong>Mission:</strong><br>
                {mission}
                <p class="member-contact" style="color: brown;">
                <strong>Connect:</strong><br>
                {contact_info}
            </p>
            </div>
            
        """, unsafe_allow_html=True)
        st.markdown('<div style="padding: 20px;"></div>', unsafe_allow_html=True)



# Team member data
team_members = [
    {
        "name": "Rai Abhishek",
        "title": "Lead Developer & Technical Architect",
        "specialization": "Full-Stack Development & Healthcare Systems",
        "img_path": "E:/health/flask/team_details/abhishek.png",
        "mission": "Driving innovation in healthcare technology through cutting-edge solutions and seamless integration.",
        "contact_info": "📧 raiabhishek@gmail.com<br>🔗 <a href='https://www.linkedin.com/in/johnsmith' target='_blank'>LinkedIn Profile</a>"
    },
    {
        "name": "Shashi",
        "title": "Senior Project Manager",
        "specialization": "Healthcare Project Management & Strategy",
        "img_path": "E:/health/flask/team_details/shashi.png",
        "mission": "Ensuring successful delivery of healthcare solutions while maintaining highest quality standards.",
        "contact_info": "📧 s.shashi@example.com<br>🔗 <a href='https://www.linkedin.com/in/sarahjohnson' target='_blank'>LinkedIn Profile</a>"
    },
    {
        "name": "Revanth",
        "title": "Lead Data Scientist",
        "specialization": "Healthcare Analytics & Machine Learning",
        "img_path": "E:/health/flask/team_details/revanth.png",
        "mission": "Leveraging data science to transform healthcare outcomes and patient experiences.",
        "contact_info": "📧 revanth@example.com<br>🔗 <a href='https://www.linkedin.com/in/michaelbrown' target='_blank'>LinkedIn Profile</a>"
    },
    {
        "name": "Rakesh",
        "title": "Senior UX/UI Designer",
        "specialization": "Healthcare Interface Design & User Research",
        "img_path": "E:/health/flask/team_details/rakesh.png",
        "mission": "Creating intuitive and accessible healthcare interfaces that enhance user experience.",
        "contact_info": "📧 rakesh@example.com<br>🔗 <a href='https://www.linkedin.com/in/michaelbrown' target='_blank'>LinkedIn Profile</a>"
    }
]

# Display team members
for member in team_members:
    display_team_member(
        member["name"],
        member["title"],
        member["specialization"],
        member["img_path"],
        member["mission"],
        member["contact_info"]
    )
