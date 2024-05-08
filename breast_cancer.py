import streamlit as st

def predict_breast_cancer(breast_cancer_model):
    # Breast Cancer Prediction Page title
    st.title("Breast Cancer Prediction using ML")

    # Displaying the image
    st.image("images/breast_cancer_img.jpg")

    # Input fields for the 22 features
    radius_mean = st.slider('Radius Mean', min_value=5.0, max_value=30.0, value=17.99, step=0.1)
    texture_mean = st.slider('Texture Mean', min_value=0.0, max_value=50.0, value=10.38, step=0.1)
    perimeter_mean = st.number_input('Perimeter Mean', min_value=40.0, max_value=200.0, value=122.8, step=0.1)
    area_mean = st.number_input('Area Mean', min_value=0, max_value=3000, value=1001, step=1)
    smoothness_mean = st.slider('Smoothness Mean', min_value=0.0, max_value=0.3, value=0.1184, step=0.0001)
    compactness_mean = st.slider('Compactness Mean', min_value=0.0, max_value=0.5, value=0.2776, step=0.0001)
    concavity_mean = st.slider('Concavity Mean', min_value=0.0, max_value=1.0, value=0.3001, step=0.0001)
    concave_points_mean = st.slider('Concave Points Mean', min_value=0.0, max_value=0.5, value=0.1471, step=0.0001)
    symmetry_mean = st.slider('Symmetry Mean', min_value=0.0, max_value=1.0, value=0.2419, step=0.0001)
    fractal_dimension_mean = st.slider('Fractal Dimension Mean', min_value=0.0, max_value=0.1, value=0.07871, step=0.0001)
    radius_se = st.slider('Radius SE', min_value=0.0, max_value=5.0, value=1.095, step=0.01)
    texture_se = st.slider('Texture SE', min_value=0.0, max_value=5.0, value=0.9053, step=0.01)
    perimeter_se = st.number_input('Perimeter SE', min_value=0.0, max_value=100.0, value=8.589, step=0.01)
    area_se = st.number_input('Area SE', min_value=0.0, max_value=2000.0, value=153.4, step=0.1)
    smoothness_se = st.slider('Smoothness SE', min_value=0.0, max_value=0.1, value=0.006399, step=0.00001)
    compactness_se = st.slider('Compactness SE', min_value=0.0, max_value=0.5, value=0.04904, step=0.0001)
    concavity_se = st.slider('Concavity SE', min_value=0.0, max_value=1.0, value=0.05373, step=0.0001)
    concave_points_se = st.slider('Concave Points SE', min_value=0.0, max_value=0.5, value=0.01587, step=0.0001)
    symmetry_se = st.slider('Symmetry SE', min_value=0.0, max_value=1.0, value=0.03003, step=0.0001)
    fractal_dimension_se = st.slider('Fractal Dimension SE', min_value=0.0, max_value=0.1, value=0.006193, step=0.0001)
    radius_worst = st.number_input('Radius Worst', min_value=0.0, max_value=50.0, value=25.38, step=0.01)
    texture_worst = st.number_input('Texture Worst', min_value=0.0, max_value=50.0, value=17.33, step=0.01)

    # Prediction logic for Breast Cancer
    cancer_diagnosis = ''

    # Creating a button for Prediction
    if st.button("Breast Cancer Test Result"):
        # Make prediction
        prediction = breast_cancer_model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
                                                    compactness_mean, concavity_mean, concave_points_mean,
                                                    symmetry_mean, fractal_dimension_mean,
                                                    radius_se, texture_se, perimeter_se, area_se, smoothness_se,
                                                    compactness_se, concavity_se, concave_points_se,
                                                    symmetry_se, fractal_dimension_se,
                                                    radius_worst, texture_worst]])

        # Interpret prediction result
        if prediction[0] == 1:
            cancer_diagnosis = "The tumor is Malignant (Cancerous)"
        else:
            cancer_diagnosis = "The tumor is Benign (Non-cancerous)"

    st.success(cancer_diagnosis)


