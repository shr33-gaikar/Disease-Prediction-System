import streamlit as st
def predict_diabetes(diabetes_model):
    # UI components for diabetes prediction
    st.title('Diabetes Prediction using ML')

    # Displaying the image
    st.image("images/diabetes_img.png")

    st.subheader('General Patient Information')
    pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=17, value=3, step=1)
    glucose = st.number_input('Glucose Level (mg/dl)', min_value=0, max_value=200, value=120, step=1)
    blood_pressure = st.number_input('Blood Pressure (mmHg)', min_value=0, max_value=122, value=70, step=1)
    skin_thickness = st.number_input('Skin Thickness (mm)', min_value=0, max_value=110, value=20, step=1)
    insulin = st.number_input('Insulin Level (mu U/ml)', min_value=0, max_value=846, value=79, step=1)
    bmi = st.number_input('BMI', min_value=0.0, max_value=67.1, value=32.0, step=0.1)
    diabetes_pedigree = st.slider('Diabetes Pedigree Function', min_value=0.078, max_value=2.42, value=0.3725,
                                  step=0.001)
    age = st.number_input('Age', min_value=21, max_value=88, value=29, step=1)

    # Prediction logic for diabetes
    diabetes_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Predict Diabetes'):
        user_input = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]
        diabetes_prediction = diabetes_model.predict([user_input])

        if diabetes_prediction[0] == 1:
            diabetes_diagnosis = 'The person is predicted to have diabetes.'
        else:
            diabetes_diagnosis = 'The person is predicted to be diabetes-free.'

    st.success(diabetes_diagnosis)
