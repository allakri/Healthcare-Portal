import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
# Ensure these paths are correct and the files exist
diabetes_model = pickle.load(open('E:/health/flask/models/models_diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('E:/health/flask/models/models_heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('E:/health/flask/models/models_parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# # Example inputs for Diabetes Prediction
# diabetes_examples = [
#     [5, 166, 72, 19, 175, 25.8, 0.587, 51],
#     [3, 150, 80, 25, 90, 22.0, 0.6, 50]
# ]
diabetes_examples = [
    # Example 1: A middle-aged woman with a higher BMI and family history
    [3, 178, 82, 28, 210, 32.5, 0.625, 47],
    
    # Example 2: A younger person with a lower glucose level and BMI
    [1, 110, 70, 15, 100, 22.0, 0.3, 28],
    
    # # Example 3: An older person with high glucose levels and obesity
    # [5, 190, 88, 35, 180, 35.2, 0.75, 60],
    
    # # Example 4: A woman with a healthy BMI and normal glucose levels
    # [2, 120, 70, 10, 80, 21.4, 0.4, 34],
    
    # # Example 5: An older man with high blood pressure and family history of diabetes
    # [4, 160, 85, 20, 150, 28.3, 0.5, 52],
    
    # # Example 6: A younger individual with normal glucose and insulin levels
    # [0, 105, 65, 12, 50, 18.5, 0.2, 25],
    
    # # Example 7: A person with a high insulin level, indicating insulin resistance
    # [6, 200, 95, 40, 250, 36.0, 0.8, 45]
]

# Example inputs for Heart Disease Prediction
heart_examples = [
    [40, 1, 0, 110, 167, 0, 0, 114, 1, 2, 1, 0, 3],
    [60, 1, 3, 120, 250, 0, 2, 130, 0, 1.0, 0, 0, 0]
]

# Example inputs for Parkinson's Prediction
parkinsons_examples = [
    [120.0, 150.0, 85.0, 0.005, 0.00005, 0.003, 0.004, 0.015, 0.02, 0.1, 
     0.01, 0.02, 0.03, 0.02, 0.03, 20.0, 0.5, 0.7, -5.0, 0.3, 2.5, 0.1],
    [237.32300, 243.70900, 229.25600, 0.00303, 0.00001, 0.00173, 0.00159, 0.00519, 0.01242, 0.11600, 
     0.00696, 0.00747, 0.00882, 0.02089, 0.00533, 24.67900, 0.384868, 0.626710, -7.018057, 0.176316, 1.852402, 0.091604]
]

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')
    
    # Dropdown to select example or manual input
    diab_use_example = st.selectbox("Choose an example or input manually:", 
                                    ["Manual Input"] + [f"Example {i+1}" for i in range(len(diabetes_examples))])

    # Set defaults based on selected example
    if diab_use_example != "Manual Input":
        example_idx = int(diab_use_example.split(" ")[-1]) - 1
        diab_defaults = diabetes_examples[example_idx]
    else:
        diab_defaults = [""] * 8  # Empty defaults for manual input
   
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', value=str(diab_defaults[0]))

    with col2:
        Glucose = st.text_input('Glucose Level', value=str(diab_defaults[1]))

    with col3:
        BloodPressure = st.text_input('Blood Pressure value', value=str(diab_defaults[2]))

    with col1:
        SkinThickness = st.text_input('Skin Thickness value', value=str(diab_defaults[3]))

    with col2:
        Insulin = st.text_input('Insulin Level', value=str(diab_defaults[4]))

    with col3:
        BMI = st.text_input('BMI value', value=str(diab_defaults[5]))

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', value=str(diab_defaults[6]))

    with col2:
        Age = st.text_input('Age of the Person', value=str(diab_defaults[7]))


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    heart_use_example = st.selectbox("Choose an example or input manually:", 
                                     ["Manual Input"] + [f"Example {i+1}" for i in range(len(heart_examples))])

    if heart_use_example != "Manual Input":
        example_idx = int(heart_use_example.split(" ")[-1]) - 1
        heart_defaults = heart_examples[example_idx]
    else:
        heart_defaults = [""] * 13

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age', value=str(heart_defaults[0]))

    with col2:
        sex = st.text_input('Sex', value=str(heart_defaults[1]))

    with col3:
        cp = st.text_input('Chest Pain types', value=str(heart_defaults[2]))

    with col1:
        trestbps = st.text_input('Resting Blood Pressure', value=str(heart_defaults[3]))

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl', value=str(heart_defaults[4]))

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl', value=str(heart_defaults[5]))

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results', value=str(heart_defaults[6]))

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', value=str(heart_defaults[7]))

    with col3:
        exang = st.text_input('Exercise Induced Angina', value=str(heart_defaults[8]))

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise', value=str(heart_defaults[9]))

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment', value=str(heart_defaults[10]))

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy', value=str(heart_defaults[11]))

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', value=str(heart_defaults[12]))

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    park_use_example = st.selectbox("Choose an example or input manually:", 
                                    ["Manual Input"] + [f"Example {i+1}" for i in range(len(parkinsons_examples))])

    if park_use_example != "Manual Input":
        example_idx = int(park_use_example.split(" ")[-1]) - 1
        park_defaults = parkinsons_examples[example_idx]
    else:
        park_defaults = [""] * 22

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)', value=str(park_defaults[0]))

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)', value=str(park_defaults[1]))

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)', value=str(park_defaults[2]))

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)', value=str(park_defaults[3]))

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', value=str(park_defaults[4]))

    with col1:
        RAP = st.text_input('MDVP:RAP', value=str(park_defaults[5]))

    with col2:
        PPQ = st.text_input('MDVP:PPQ', value=str(park_defaults[6]))

    with col3:
        DDP = st.text_input('Jitter:DDP', value=str(park_defaults[7]))

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer', value=str(park_defaults[8]))

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)', value=str(park_defaults[9]))

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3', value=str(park_defaults[10]))

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5', value=str(park_defaults[11]))

    with col3:
        APQ = st.text_input('MDVP:APQ', value=str(park_defaults[12]))

    with col4:
        DDA = st.text_input('Shimmer:DDA', value=str(park_defaults[13]))

    with col5:
        NHR = st.text_input('NHR', value=str(park_defaults[14]))

    with col1:
        HNR = st.text_input('HNR', value=str(park_defaults[15]))

    with col2:
        RPDE = st.text_input('RPDE', value=str(park_defaults[16]))

    with col3:
        DFA = st.text_input('DFA', value=str(park_defaults[17]))

    with col4:
        spread1 = st.text_input('spread1', value=str(park_defaults[18]))

    with col5:
        spread2 = st.text_input('spread2', value=str(park_defaults[19]))

    with col1:
        D2 = st.text_input('D2', value=str(park_defaults[20]))

    with col2:
        PPE = st.text_input('PPE', value=str(park_defaults[21]))

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)