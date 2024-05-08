import streamlit as st

def predict_liver_disease(liver_disease_model):
    # Liver Disease Prediction Page title
    st.title("Liver Disease Prediction using ML")

    # Displaying the image
    st.image("images/liver_disease_img.jpg")

    col1, col2, col3, col4, col5 = st.columns(5)

    # Input fields with default values and labels
    with col1:
        age = st.number_input('Age', value=50)
    with col2:
        gender = st.radio('Gender', ('Male', 'Female'))
    with col3:
        total_bilirubin = st.number_input('Total Bilirubin', value=0.5, step=0.1)
    with col4:
        direct_bilirubin = st.number_input('Direct Bilirubin', value=0.2, step=0.1)
    with col5:
        alkaline_phosphotase = st.number_input('Alkaline Phosphotase', value=200)

    with col1:
        alamine_aminotransferase = st.number_input('Alamine Aminotransferase', value=25)
    with col2:
        aspartate_aminotransferase = st.number_input('Aspartate Aminotransferase', value=35)
    with col3:
        total_proteins = st.number_input('Total Proteins', value=6.0, step=0.1)
    with col4:
        albumin = st.number_input('Albumin', value=3.5, step=0.1)
    with col5:
        albumin_and_globulin_ratio = st.number_input('Albumin and Globulin Ratio', value=1.0, step=0.1)

    # Prediction logic for Liver Disease
    liver_diagnosis = ''

    # Creating a button for Prediction
    if st.button("Liver Disease Test Result"):
        # Converting user inputs to numerical values
        gender_mapping = {'Male': 1, 'Female': 0}

        gender = gender_mapping[gender]

        # Make prediction
        prediction = liver_disease_model.predict([[age, gender, total_bilirubin, direct_bilirubin,
                                                    alkaline_phosphotase, alamine_aminotransferase,
                                                    aspartate_aminotransferase, total_proteins,
                                                    albumin, albumin_and_globulin_ratio]])

        # Interpret prediction result
        if prediction[0] == 1:
            liver_diagnosis = "The person has Liver Disease"
        else:
            liver_diagnosis = "The person does not have Liver Disease"

    st.success(liver_diagnosis)
