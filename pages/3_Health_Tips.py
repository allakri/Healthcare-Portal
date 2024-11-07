import streamlit as st

def main():
    st.set_page_config(
        page_title="Health Tips & Information Center",
        page_icon="🏥",
        layout="wide"
    )

    st.title("Health Tips & Information Center")

    tab1, tab2, tab3 = st.tabs(["Health Tips", "Disease Information", "Health Resources"])

    with tab1:
        show_health_tips()
    
    with tab2:
        show_disease_info()
    
    with tab3:
        show_resources()

def show_health_tips():
    st.header("Health Tips")
    
    category = st.selectbox(
        "Choose a health category",
        ["Nutrition", "Exercise", "Mental Health", "Sleep", "Preventive Care"]
    )

    if category == "Nutrition":
        st.subheader("Nutrition Guidelines")
        diet_type = st.selectbox(
            "Select your diet type",
            ["Regular", "Vegetarian", "Vegan", "Keto", "Mediterranean"]
        )

        if diet_type == "Regular":
            st.write("### Daily Recommendations")
            st.write("- Proteins: 2-3 servings of lean meat, fish, or eggs")
            st.write("- Vegetables: 5-6 servings of varied colors")
            st.write("- Fruits: 2-3 servings")
            st.write("- Whole grains: 3-4 servings")
            st.write("- Dairy: 2-3 servings")
            st.write("- Water: 8-10 glasses")

        elif diet_type == "Vegetarian":
            st.write("### Daily Recommendations")
            st.write("- Plant Proteins: 3-4 servings of legumes, tofu, tempeh")
            st.write("- Vegetables: 6-7 servings of diverse colors")
            st.write("- Fruits: 3-4 servings")
            st.write("- Whole grains: 4-5 servings")
            st.write("- Dairy/Alternatives: 2-3 servings")
            st.write("- Nuts and Seeds: 1-2 servings")
            st.write("- Water: 8-10 glasses")

        elif diet_type == "Vegan":
            st.write("### Daily Recommendations")
            st.write("- Plant Proteins: 4-5 servings (legumes, tofu, tempeh, seitan)")
            st.write("- Vegetables: 7-8 servings of varied colors")
            st.write("- Fruits: 3-4 servings")
            st.write("- Whole grains: 4-5 servings")
            st.write("- Plant-based milk: 2-3 servings")
            st.write("- Nuts and Seeds: 2-3 servings")
            st.write("- B12 supplement: As recommended")
            st.write("- Water: 8-10 glasses")

        elif diet_type == "Keto":
            st.write("### Daily Recommendations")
            st.write("- Healthy Fats: 70-80% of daily calories")
            st.write("- Proteins: 20-25% of daily calories")
            st.write("- Carbohydrates: 5-10% of daily calories (20-50g net carbs)")
            st.write("- Recommended Foods:")
            st.write("  • Meats, fish, eggs")
            st.write("  • Low-carb vegetables")
            st.write("  • High-fat dairy")
            st.write("  • Nuts and seeds")
            st.write("  • Avocados and healthy oils")
            st.write("- Water: 8-10 glasses plus electrolytes")

        elif diet_type == "Mediterranean":
            st.write("### Daily Recommendations")
            st.write("- Vegetables: 6-7 servings")
            st.write("- Fruits: 3-4 servings")
            st.write("- Whole grains: 3-4 servings")
            st.write("- Olive oil: Primary fat source")
            st.write("- Fish: 2-3 times per week")
            st.write("- Legumes: At least 3 times per week")
            st.write("- Nuts and seeds: 1-2 servings")
            st.write("- Herbs and spices: Liberal use")
            st.write("- Red wine: Optional, moderate consumption")
            st.write("- Water: 8-10 glasses")

    elif category == "Exercise":
        st.subheader("Exercise Recommendations")
        fitness_level = st.selectbox(
            "Select your fitness level",
            ["Beginner", "Intermediate", "Advanced"]
        )

        if fitness_level == "Beginner":
            st.write("### Weekly Plan")
            st.write("- Walking: 30 minutes, 5 days/week")
            st.write("- Basic stretching: 10-15 minutes daily")
            st.write("- Light strength training: 2 days/week")
            st.write("- Rest days: 2 days/week")
            
            st.write("### Tips")
            st.write("1. Start slowly and gradually increase intensity")
            st.write("2. Focus on proper form")
            st.write("3. Stay hydrated")
            st.write("4. Warm up before exercise")

        elif fitness_level == "Intermediate":
            st.write("### Weekly Plan")
            st.write("- Cardio: 45-60 minutes, 4-5 days/week")
            st.write("- Strength training: 3-4 days/week")
            st.write("- HIIT workouts: 1-2 days/week")
            st.write("- Flexibility work: 15-20 minutes daily")
            st.write("- Rest days: 1-2 days/week")
            
            st.write("### Tips")
            st.write("1. Mix cardio and strength training")
            st.write("2. Track your progress")
            st.write("3. Include interval training")
            st.write("4. Focus on nutrition timing")

        elif fitness_level == "Advanced":
            st.write("### Weekly Plan")
            st.write("- High-intensity cardio: 60+ minutes, 4-5 days/week")
            st.write("- Advanced strength training: 4-5 days/week")
            st.write("- HIIT/Circuit training: 2-3 days/week")
            st.write("- Sports-specific training: As needed")
            st.write("- Recovery work: Daily mobility and flexibility")
            st.write("- Strategic rest: 1 day/week")
            
            st.write("### Tips")
            st.write("1. Periodize your training")
            st.write("2. Monitor recovery closely")
            st.write("3. Focus on performance metrics")
            st.write("4. Consider advanced nutrition strategies")

    elif category == "Sleep":
        st.subheader("Sleep Recommendations")
        st.write("### General Guidelines")
        st.write("- Adults need 7-9 hours of sleep per night")
        st.write("- Maintain consistent sleep schedule")
        st.write("- Create optimal sleep environment")
        
        st.write("### Sleep Hygiene Tips")
        st.write("1. Stick to a regular sleep schedule")
        st.write("2. Create a relaxing bedtime routine")
        st.write("3. Limit screen time before bed")
        st.write("4. Keep bedroom cool, dark, and quiet")
        st.write("5. Avoid caffeine and heavy meals before bed")
        
        st.write("### Warning Signs of Poor Sleep")
        st.write("- Difficulty falling asleep")
        st.write("- Frequent night waking")
        st.write("- Daytime fatigue")
        st.write("- Poor concentration")
        st.write("- Mood changes")

    elif category == "Preventive Care":
        st.subheader("Preventive Care Guidelines")
        st.write("### Regular Check-ups")
        st.write("- Annual physical examination")
        st.write("- Dental check-ups every 6 months")
        st.write("- Eye examination every 1-2 years")
        st.write("- Age-appropriate cancer screenings")
        
        st.write("### Vaccinations")
        st.write("- Annual flu shot")
        st.write("- Tetanus every 10 years")
        st.write("- Other age-appropriate vaccines")
        
        st.write("### Lifestyle Practices")
        st.write("1. Regular exercise")
        st.write("2. Balanced nutrition")
        st.write("3. Stress management")
        st.write("4. Adequate sleep")
        st.write("5. Regular health monitoring")

def show_disease_info():
    st.header("Disease Information")
    
    category = st.selectbox(
        "Select health condition",
        ["Heart Disease", "Diabetes", "Respiratory Conditions", "Mental Health Conditions"]
    )

    if category == "Heart Disease":
        st.subheader("Heart Disease Information")
        st.write("### Common Types")
        st.write("1. Coronary Artery Disease")
        st.write("2. Heart Failure")
        st.write("3. Arrhythmia")
        
        st.write("### Risk Factors")
        st.write("- High blood pressure")
        st.write("- High cholesterol")
        st.write("- Smoking")
        st.write("- Obesity")
        st.write("- Physical inactivity")

        st.write("### Prevention")
        st.write("1. Regular exercise")
        st.write("2. Healthy diet")
        st.write("3. Regular check-ups")
        st.write("4. Stress management")
        st.write("5. Adequate sleep")

    elif category == "Diabetes":
        st.subheader("Diabetes Information")
        st.write("### Types")
        st.write("1. Type 1 Diabetes")
        st.write("2. Type 2 Diabetes")
        st.write("3. Gestational Diabetes")

        st.write("### Symptoms")
        st.write("- Increased thirst")
        st.write("- Frequent urination")
        st.write("- Extreme hunger")
        st.write("- Unexplained weight loss")
        st.write("- Fatigue")

    elif category == "Respiratory Conditions":
        st.subheader("Respiratory Conditions Information")
        st.write("### Common Types")
        st.write("1. Asthma")
        st.write("2. COPD")
        st.write("3. Bronchitis")
        st.write("4. Pneumonia")
        
        st.write("### Common Symptoms")
        st.write("- Shortness of breath")
        st.write("- Chronic cough")
        st.write("- Wheezing")
        st.write("- Chest tightness")
        
        st.write("### Prevention & Management")
        st.write("1. Avoid smoking and second-hand smoke")
        st.write("2. Regular exercise")
        st.write("3. Clean air filters")
        st.write("4. Proper medication use")
        st.write("5. Regular check-ups")

    elif category == "Mental Health Conditions":
        st.subheader("Mental Health Information")
        st.write("### Common Conditions")
        st.write("1. Depression")
        st.write("2. Anxiety Disorders")
        st.write("3. Bipolar Disorder")
        st.write("4. PTSD")
        
        st.write("### Warning Signs")
        st.write("- Changes in mood")
        st.write("- Changes in sleep patterns")
        st.write("- Social withdrawal")
        st.write("- Difficulty concentrating")
        st.write("- Changes in appetite")
        
        st.write("### Treatment Options")
        st.write("1. Therapy/Counseling")
        st.write("2. Medication (if prescribed)")
        st.write("3. Support groups")
        st.write("4. Lifestyle changes")
        st.write("5. Stress management techniques")

def show_resources():
    st.header("Health Resources")
    
    resource_type = st.selectbox(
        "Select resource type",
        ["Emergency Contacts", "Online Tools", "Healthcare Providers"]
    )

    if resource_type == "Emergency Contacts":
        st.subheader("Emergency Numbers")
        st.write("- Emergency Services: 911")
        st.write("- Poison Control: 1-800-222-1222")
        st.write("- Mental Health Crisis: 988")
        st.write("- Suicide Prevention: 1-800-273-8255")
        
    elif resource_type == "Online Tools":
        st.subheader("Health Calculators and Tools")
        st.write("### BMI Calculator")
        weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
        height = st.number_input("Height (m)", min_value=1.0, max_value=2.5, value=1.7)
        if st.button("Calculate BMI"):
            bmi = weight / (height * height)
            st.write(f"Your BMI is: {bmi:.1f}")
            if bmi < 18.5:
                st.write("Category: Underweight")
            elif bmi < 25:
                st.write("Category: Normal weight")
            elif bmi < 30:
                st.write("Category: Overweight")
            else:
                st.write("Category: Obese")

    elif resource_type == "Healthcare Providers":
        st.subheader("Find Healthcare Providers")
        st.write("### Primary Care")
        st.write("- Family Physicians")
        st.write("- Internal Medicine Doctors")
        st.write("- Pediatricians")
        st.write("- Nurse Practitioners")
        
        st.write("### Specialists")
        st.write("- Cardiologists")
        st.write("- Dermatologists")
        st.write("- Orthopedists")
        st.write("- Psychiatrists")
        st.write("- Gynecologists")
        
        st.write("### Mental Health Professionals")
        st.write("- Psychologists")
        st.write("- Licensed Counselors")
        st.write("- Social Workers")
        st.write("- Psychiatrists")

if __name__ == "__main__":
    main()