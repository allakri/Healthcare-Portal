# AI Healthcare Portal

## Overview

The AI Healthcare Portal is a web application built using Streamlit, designed to provide users with a comprehensive range of healthcare-related functionalities. By leveraging both AIML and generative AI technologies, this project aims to deliver valuable insights and personalized advice for various health conditions.

## Features

- 🏥 **Healthcare Take**: Comprehensive health check-ups and consultations.
- 📊 **Report Analysis**: In-depth analysis of your health reports.
- 🥗 **Food & Nutrition Advisor**: Personalized dietary advice for a healthier you.
- 💊 **Medication Advisor**: Guidance on medications and treatment plans.
- **Health Predictions**: Predictive analytics for heart disease, diabetes, breast cancer, and Parkinson's disease using trained models.

## Technologies Used

- **Framework**: Streamlit
- **AI Models**: Open-source trained models for health predictions
- **APIs**: 
  - Google Gemmini API
  - Groq API
- **Libraries**:
  - `streamlit`
  - `google-generativeai`
  - `python-dotenv`
  - `langchain`
  - `PyPDF2`
  - `chromadb`
  - `faiss-cpu`
  - `langchain_google_genai`
  - `scikit-learn`

## Setup Instructions


Make sure you have Python installed on your machine. 


### Prerequisites

- Python 3.7 or later
- pip (Python package installer)

### Step 1: Clone the Repository

Open your terminal or command prompt and run the following command to clone the repository:

bash
git clone <your-repo-url>
cd <your-repo-name>




### Virtual Environment

1. Create a virtual environment:                                python -m venv venv

activate the env :                                              venv\Scripts\activate

Install the required packages:                                  pip install -r requirements.txt

"Run the Application"
To run the Streamlit application, use the following command:    streamlit run app.py