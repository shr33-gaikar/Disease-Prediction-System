import streamlit as st
from streamlit_option_menu import option_menu
from parkinsons import predict_parkinsons
from kidney_disease import predict_kidney_disease
from breast_cancer import predict_breast_cancer
from heart_disease import predict_heart_disease
from diabetes import predict_diabetes
from liver_disease import predict_liver_disease
import pickle

# Load the models
parkinsons_model = pickle.load(open('models/trained_model_parkinsons.sav', 'rb'))
kidney_disease_model = pickle.load(open('models/trained_model_kidney.pkl', 'rb'))
breast_cancer_model = pickle.load(open('models/trained_model_breast_cancer.pkl', 'rb'))
heart_disease_model = pickle.load(open('models/trained_model_heart.sav', 'rb'))
diabetes_model = pickle.load(open('models/trained_model_diabetes.sav', 'rb'))
liver_disease_model = pickle.load(open('models/trained_model_liver.pkl', 'rb'))

st.set_page_config(page_title="Multiple Disease Prediction System", page_icon="hospital", layout="wide")

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Home Page',
                            'Heart Disease Prediction', 'Diabetes Prediction', 'Kidney Disease Prediction',
                            'Liver Disease Prediction', 'Breast Cancer Prediction', 'Parkinsons Prediction'],
                           menu_icon='hospital',
                           icons=['info', 'activity', 'eyedropper', 'lungs-fill',
                                  'caret-right-fill', 'balloon-heart', 'bug'],
                           default_index=0)

# General Instructions Page
if selected == 'Home Page':
    st.title('Welcome to Multiple Disease Prediction System!')
    st.write("Please select a disease prediction system from the sidebar.")
    st.image("images/dis_pred_img.jpg")

# Disease Prediction Pages
elif selected == 'Kidney Disease Prediction':
    predict_kidney_disease(kidney_disease_model)
elif selected == 'Breast Cancer Prediction':
    predict_breast_cancer(breast_cancer_model)
elif selected == 'Heart Disease Prediction':
    predict_heart_disease(heart_disease_model)
elif selected == 'Diabetes Prediction':
    predict_diabetes(diabetes_model)
elif selected == 'Liver Disease Prediction':
    predict_liver_disease(liver_disease_model)
elif selected == 'Parkinsons Prediction':
    predict_parkinsons(parkinsons_model)
