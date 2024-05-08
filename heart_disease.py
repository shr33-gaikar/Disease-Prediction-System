import streamlit as st
def predict_heart_disease(heart_disease_model):
    # UI components for heart disease prediction
    st.title('Heart Disease Prediction using ML')

    # Displaying the image
    st.image("images/heart_disease_img.jpg")

    st.subheader('General Patient Information')
    age = st.slider('Age', 1, 100, 25)
    sex = st.radio('Sex', ('Male', 'Female'))

    st.subheader('Clinical Information')
    cp = st.selectbox('Chest Pain type', ['Typical Angina', 'Atypical Angina', 'Non Anginal', 'Asymptomatic'])
    trestbps = st.number_input('Resting Blood Pressure (mmHg)', value=120)
    chol = st.number_input('Serum Cholesterol (mg/dl)', value=200)
    fbs = st.checkbox('Fasting Blood Sugar > 120 mg/dl')

    st.subheader('Clinical Tests')
    restecg = st.selectbox('Resting ECG Results', ['Normal', 'ST-T Wave Abnormality', 'LV Hypertrophy'])
    thalach = st.slider('Maximum Heart Rate Achieved', 60, 220, 100)
    exang = st.checkbox('Exercise Induced Angina')
    oldpeak = st.number_input('ST Depression Induced by Exercise', value=0.0)
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
    ca = st.number_input('Major Vessels Colored by Fluoroscopy', value=0)
    thal = st.selectbox('Thal (Defect Type)', ['Normal', 'Fixed Defect', 'Reversible Defect'])

    # Prediction logic for heart disease
    heart_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Predict Heart Disease'):
        # Map user inputs to numerical values
        sex = 1 if sex == 'Male' else 0
        cp_mapping = {'Typical Angina': 1, 'Atypical Angina': 2, 'Non Anginal': 3, 'Asymptomatic': 4}
        cp = cp_mapping[cp]
        fbs = 1 if fbs else 0
        restecg_mapping = {'Normal': 0, 'ST-T Wave Abnormality': 1, 'LV Hypertrophy': 2}
        restecg = restecg_mapping[restecg]
        exang = 1 if exang else 0
        slope_mapping = {'Upsloping': 1, 'Flat': 2, 'Downsloping': 3}
        slope = slope_mapping[slope]
        thal_mapping = {'Normal': 1, 'Fixed Defect': 2, 'Reversible Defect': 3}
        thal = thal_mapping[thal]

        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person may have a heart disease'
        else:
            heart_diagnosis = 'The person may not have any heart disease'

    st.success(heart_diagnosis)
