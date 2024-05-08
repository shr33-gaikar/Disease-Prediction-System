import streamlit as st

def predict_kidney_disease(kidney_disease_model):
    # Kidney Disease Prediction Page title
    st.title("Kidney Disease Prediction using ML")

    # Displaying the image
    st.image("images/kidney_disease_img.jpg")

    col1, col2, col3, col4, col5 = st.columns(5)

    # Input fields with default values and labels
    with col1:
        age = st.number_input('Age', value=50)
    with col2:
        blood_pressure = st.number_input('Blood Pressure', value=80)
    with col3:
        specific_gravity = st.number_input('Specific Gravity', value=1.02, step=0.01)
    with col4:
        albumin = st.number_input('Albumin', value=0)
    with col5:
        sugar = st.number_input('Sugar', value=0)

    with col1:
        red_blood_cells = st.radio('Red Blood Cell', ('Normal', 'Abnormal'))
    with col2:
        pus_cell = st.radio('Pus Cell', ('Normal', 'Abnormal'))
    with col3:
        pus_cell_clumps = st.radio('Pus Cell Clumps', ('Present', 'Not Present'))
    with col4:
        bacteria = st.radio('Bacteria', ('Present', 'Not Present'))
    with col5:
        blood_glucose_random = st.number_input('Blood Glucose Random', value=100)

    with col1:
        blood_urea = st.number_input('Blood Urea', value=40)
    with col2:
        serum_creatinine = st.number_input('Serum Creatinine', value=0.9, step=0.1)
    with col3:
        sodium = st.number_input('Sodium', value=138)
    with col4:
        potassium = st.number_input('Potassium', value=4)
    with col5:
        haemoglobin = st.number_input('Haemoglobin', value=12)

    with col1:
        packed_cell_volume = st.number_input('Packet Cell Volume', value=40)
    with col2:
        white_blood_cell_count = st.number_input('White Blood Cell Count', value=8000)
    with col3:
        red_blood_cell_count = st.number_input('Red Blood Cell Count', value=5)
    with col4:
        hypertension = st.radio('Hypertension', ('Yes', 'No'))
    with col5:
        diabetes_mellitus = st.radio('Diabetes Mellitus', ('Yes', 'No'))

    with col1:
        coronary_artery_disease = st.radio('Coronary Artery Disease', ('Yes', 'No'))
    with col2:
        appetite = st.radio('Appetite', ('Good', 'Poor'))
    with col3:
        pedal_edema = st.radio('Pedal Edema', ('Yes', 'No'))
    with col4:
        anemia = st.radio('Anemia', ('Yes', 'No'))

    # Prediction logic for Kidney Disease
    kidney_diagnosis = ''

    # Creating a button for Prediction
    if st.button("Kidney Disease Test Result"):
        # Converting user inputs to numerical values
        red_blood_cells_mapping = {'Normal': 0, 'Abnormal': 1}
        pus_cell_mapping = {'Normal': 0, 'Abnormal': 1}
        pus_cell_clumps_mapping = {'Present': 1, 'Not Present': 0}
        bacteria_mapping = {'Present': 1, 'Not Present': 0}
        hypertension_mapping = {'Yes': 1, 'No': 0}
        diabetes_mellitus_mapping = {'Yes': 1, 'No': 0}
        coronary_artery_disease_mapping = {'Yes': 1, 'No': 0}
        appetite_mapping = {'Good': 1, 'Poor': 0}
        pedal_edema_mapping = {'Yes': 1, 'No': 0}
        anemia_mapping = {'Yes': 1, 'No': 0}

        red_blood_cells = red_blood_cells_mapping[red_blood_cells]
        pus_cell = pus_cell_mapping[pus_cell]
        pus_cell_clumps = pus_cell_clumps_mapping[pus_cell_clumps]
        bacteria = bacteria_mapping[bacteria]
        hypertension = hypertension_mapping[hypertension]
        diabetes_mellitus = diabetes_mellitus_mapping[diabetes_mellitus]
        coronary_artery_disease = coronary_artery_disease_mapping[coronary_artery_disease]
        appetite = appetite_mapping[appetite]
        pedal_edema = pedal_edema_mapping[pedal_edema]
        anemia = anemia_mapping[anemia]

        # Make prediction
        prediction = kidney_disease_model.predict([[age, blood_pressure, specific_gravity, albumin, sugar,
                                                    red_blood_cells, pus_cell, pus_cell_clumps, bacteria,
                                                    blood_glucose_random, blood_urea, serum_creatinine, sodium,
                                                    potassium, haemoglobin, packed_cell_volume,
                                                    white_blood_cell_count, red_blood_cell_count, hypertension,
                                                    diabetes_mellitus, coronary_artery_disease, appetite,
                                                    pedal_edema, anemia]])

        # Interpret prediction result
        if prediction[0] == 1:
            kidney_diagnosis = "The person has Kidney Disease"
        else:
            kidney_diagnosis = "The person does not have Kidney Disease"

    st.success(kidney_diagnosis)
