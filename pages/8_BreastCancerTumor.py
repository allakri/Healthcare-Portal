import joblib
import streamlit as st

# Load the model
model = joblib.load('E:\\health\\flask\\models\\model.pkl')


# Example inputs based on typical feature values from the dataset
examples = [
    [13.54, 14.36, 87.46, 566.3, 0.09779, 0.08129, 0.06664, 0.04781, 0.1885, 0.05766, 
     0.2699, 0.7886, 2.058, 23.56, 0.008462, 0.0146, 0.02387, 0.01315, 0.0198, 0.0023, 
     15.11, 19.26, 99.7, 711.2, 0.144, 0.1773, 0.239, 0.1288, 0.2977, 0.07259],
    
    [15.78, 18.02, 102.5, 751.4, 0.1053, 0.07893, 0.06981, 0.05683, 0.1769, 0.06503, 
     0.3198, 0.8909, 2.192, 28.15, 0.01106, 0.01468, 0.01923, 0.01479, 0.01523, 0.00363, 
     18.98, 21.94, 126.9, 1132, 0.1674, 0.1553, 0.2032, 0.1249, 0.2722, 0.09556]
]

# Set page configuration
st.set_page_config(page_title="Breast Cancer Tumor Classification",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# page title
st.title('Breast Cancer Tumor Classification')

# Select example or manual input
use_example = st.selectbox("Choose an example or input manually:", ["Manual Input"] + [f"Example {i+1}" for i in range(len(examples))])

# Determine default values
if use_example != "Manual Input":
    example_idx = int(use_example.split(" ")[-1]) - 1
    defaults = examples[example_idx]
else:
    # Empty defaults for manual input
    defaults = ["" for _ in range(30)]  

# Define columns and input fields
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    mean_radius = st.text_input('mean radius', value=defaults[0])
    mean_texture = st.text_input('mean texture', value=defaults[1])
    mean_perimeter = st.text_input('mean perimeter', value=defaults[2])
    mean_area = st.text_input('mean area', value=defaults[3])
    mean_smoothness = st.text_input('mean smoothness', value=defaults[4])

with col2:
    mean_compactness = st.text_input('mean compactness', value=defaults[5])
    mean_concavity = st.text_input('mean concavity', value=defaults[6])
    mean_concave_points = st.text_input('mean concave points', value=defaults[7])
    mean_symmetry = st.text_input('mean symmetry', value=defaults[8])
    mean_fractal_dimension = st.text_input('mean fractal dimension', value=defaults[9])

with col3:
    radius_error = st.text_input('radius error', value=defaults[10])
    texture_error = st.text_input('texture error', value=defaults[11])
    perimeter_error = st.text_input('perimeter error', value=defaults[12])
    area_error = st.text_input('area error', value=defaults[13])
    smoothness_error = st.text_input('smoothness error', value=defaults[14])

with col4:
    compactness_error = st.text_input('compactness error', value=defaults[15])
    concavity_error = st.text_input('concavity error', value=defaults[16])
    concave_points_error = st.text_input('concave points error', value=defaults[17])
    symmetry_error = st.text_input('symmetry error', value=defaults[18])
    fractal_dimension_error = st.text_input('fractal dimension error', value=defaults[19])

with col5:
    worst_radius = st.text_input('worst radius', value=defaults[20])
    worst_texture = st.text_input('worst texture', value=defaults[21])
    worst_perimeter = st.text_input('worst perimeter', value=defaults[22])
    worst_area = st.text_input('worst area', value=defaults[23])
    worst_smoothness = st.text_input('worst smoothness', value=defaults[24])

with col6:
    worst_compactness = st.text_input('worst compactness', value=defaults[25])
    worst_concavity = st.text_input('worst concavity', value=defaults[26])
    worst_concave_points = st.text_input('worst concave points', value=defaults[27])
    worst_symmetry = st.text_input('worst symmetry', value=defaults[28])
    worst_fractal_dimension = st.text_input('worst fractal dimension', value=defaults[29])

# Trigger prediction on button press
if st.button('Breast Cancer Test Result'):
    # Collect all user inputs
    user_input = [
        mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness,
        mean_compactness, mean_concavity, mean_concave_points, mean_symmetry,
        mean_fractal_dimension, radius_error, texture_error, perimeter_error,
        area_error, smoothness_error, compactness_error, concavity_error,
        concave_points_error, symmetry_error, fractal_dimension_error,
        worst_radius, worst_texture, worst_perimeter, worst_area,
        worst_smoothness, worst_compactness, worst_concavity,
        worst_concave_points, worst_symmetry, worst_fractal_dimension
    ]
    # Convert inputs to floats
    user_input = [float(x) for x in user_input]

    # Make prediction
    Prediction = model.predict([user_input])

    # Interpret prediction
    Prediction = 'Benign' if Prediction[0] == 1 else 'Malignant'
    
    st.write(f"The breast cancer test result is: **{Prediction}**")
