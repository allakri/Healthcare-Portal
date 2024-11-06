import streamlit as st

def main():
    # Page Configuration
    st.set_page_config(
        page_title="Health Tips & Information Center",
        page_icon="🏥",
        layout="wide"
    )

    # Custom CSS
    apply_custom_css()

    # Main Header
    st.markdown("<h1 class='main-header'>Health Tips & Information Center</h1>", unsafe_allow_html=True)

    # Main Navigation
    tab1, tab2, tab3 = st.tabs(["Health Tips", "Disease Information", "Health Resources"])

    with tab1:
        show_health_tips_section()
    
    with tab2:
        show_disease_information()
    
    with tab3:
        show_health_resources()

def apply_custom_css():
    st.markdown("""
        <style>
        .main-header {
            color: #1e4b7a;
            text-align: center;
            padding: 1.5rem;
            background: linear-gradient(to right, #f0f9ff, #e6f3ff);
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        .category-header {
            color: #2c5282;
            padding: 1rem 0;
            border-bottom: 2px solid #e2e8f0;
        }
        .info-box {
            background-color: #f8fafc;
            padding: 1.5rem;
            border-radius: 10px;
            border: 1px solid #e2e8f0;
            margin: 1rem 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        .tip-card {
            background: white;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #3b82f6;
            margin: 1rem 0;
        }
        .resource-card {
            background: #f0f9ff;
            padding: 1.5rem;
            border-radius: 8px;
            margin: 1rem 0;
        }
        </style>
    """, unsafe_allow_html=True)

def show_health_tips_section():
    st.markdown("<h2 class='category-header'>Daily Health Tips</h2>", unsafe_allow_html=True)
    
    # Categories Selection
    category = st.selectbox(
        "Choose a health category",
        ["Nutrition", "Exercise", "Mental Health", "Sleep", "Preventive Care"]
    )

    if category == "Nutrition":
        show_nutrition_tips()
    elif category == "Exercise":
        show_exercise_tips()
    elif category == "Mental Health":
        show_mental_health_tips()
    elif category == "Sleep":
        show_sleep_tips()
    else:
        show_preventive_care_tips()

def show_nutrition_tips():
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    
    diet_type = st.selectbox(
        "Select your dietary preference",
        ["General", "Vegetarian", "Vegan", "Keto", "Mediterranean"]
    )

    goal = st.selectbox(
        "Select your health goal",
        ["Weight Management", "Muscle Building", "Heart Health", "Energy Boost", "Immune Support"]
    )

    # Display personalized nutrition tips
    st.markdown("### Your Personalized Nutrition Plan")
    
    # Example for General diet with Weight Management goal
    if diet_type == "General" and goal == "Weight Management":
        st.markdown("""
        #### Recommended Daily Intake
        - 🍎 Fruits: 2-3 servings
        - 🥬 Vegetables: 4-5 servings
        - 🍗 Lean Protein: 2-3 servings
        - 🥖 Whole Grains: 3-4 servings
        - 💧 Water: 8-10 glasses
        
        #### Key Tips
        1. Practice portion control
        2. Eat slowly and mindfully
        3. Plan meals in advance
        4. Track your calories
        5. Include protein in every meal
        """)

    st.markdown("</div>", unsafe_allow_html=True)

def show_exercise_tips():
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    
    fitness_level = st.select_slider(
        "Your fitness level",
        options=["Beginner", "Intermediate", "Advanced"]
    )

    goal = st.selectbox(
        "Your fitness goal",
        ["Weight Loss", "Muscle Gain", "Endurance", "Flexibility", "Overall Fitness"]
    )

    # Show personalized workout plan
    st.markdown("### Your Weekly Workout Plan")
    
    if fitness_level == "Beginner" and goal == "Weight Loss":
        st.markdown("""
        #### Monday - Cardio
        - 🚶‍♂️ 30 min brisk walking
        - 🧘‍♀️ 10 min stretching
        - 💪 Basic bodyweight exercises
        
        #### Wednesday - Strength
        - 🏋️‍♂️ Bodyweight squats (3x10)
        - 💪 Modified push-ups (3x5)
        - 🧘‍♀️ Planks (3x20 sec)
        
        #### Friday - Mixed
        - 🚲 20 min stationary bike
        - 💪 Basic resistance band exercises
        - 🧘‍♀️ Yoga for beginners
        """)

    st.markdown("</div>", unsafe_allow_html=True)

def show_mental_health_tips():
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    
    concern = st.selectbox(
        "What's your primary concern?",
        ["Stress", "Anxiety", "Depression", "Work-Life Balance", "General Wellness"]
    )

    st.markdown("### Mental Wellness Strategies")
    
    if concern == "Stress":
        st.markdown("""
        #### Daily Practices
        1. 🧘‍♀️ 10-minute meditation
        2. 📝 Journaling
        3. 🚶‍♂️ Nature walks
        4. 🎵 Music therapy
        5. 🌬️ Deep breathing exercises
        
        #### When to Seek Help
        - Persistent feelings of overwhelm
        - Physical symptoms of stress
        - Sleep disturbances
        - Changes in appetite
        """)

    st.markdown("</div>", unsafe_allow_html=True)

def show_sleep_tips():
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    
    sleep_issue = st.selectbox(
        "What sleep issues are you experiencing?",
        ["Difficulty Falling Asleep", "Waking Up Frequently", "Poor Sleep Quality", "Irregular Sleep Schedule"]
    )

    st.markdown("### Sleep Improvement Plan")
    
    if sleep_issue == "Difficulty Falling Asleep":
        st.markdown("""
        #### Evening Routine
        1. 🌅 Set consistent bedtime
        2. 📱 No screens 1 hour before bed
        3. 🫖 Calming tea (chamomile)
        4. 🛁 Warm bath or shower
        5. 📚 Light reading
        
        #### Environment Optimization
        - 🌡️ Cool room temperature (65-68°F)
        - 🌙 Complete darkness
        - 🔇 White noise if needed
        """)

    st.markdown("</div>", unsafe_allow_html=True)

def show_preventive_care_tips():
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    
    age_group = st.selectbox(
        "Select your age group",
        ["18-30", "31-50", "51-70", "70+"]
    )

    st.markdown("### Preventive Care Checklist")
    
    if age_group == "31-50":
        st.markdown("""
        #### Regular Screenings
        - 🩺 Annual physical exam
        - 🦷 Dental checkup every 6 months
        - 👁️ Eye exam every 2 years
        - 💉 Vaccinations as recommended
        
        #### Lifestyle Habits
        1. Regular exercise
        2. Balanced diet
        3. Stress management
        4. Regular sleep schedule
        """)

    st.markdown("</div>", unsafe_allow_html=True)

def show_disease_information():
    st.markdown("<h2 class='category-header'>Disease Information Center</h2>", unsafe_allow_html=True)
    
    # Add disease information content here
    pass

def show_health_resources():
    st.markdown("<h2 class='category-header'>Health Resources</h2>", unsafe_allow_html=True)
    
    # Add health resources content here
    pass

if __name__ == "__main__":
    main()
