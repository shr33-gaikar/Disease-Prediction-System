import streamlit as st

def predict_parkinsons(parkinsons_model):
    # Parkinson's Prediction Page title
    st.title("Parkinson's Disease Prediction using ML")

    # Displaying the image
    st.image("images/parkinsons_img.jpg")

    col1, col2, col3, col4, col5 = st.columns(5)

    # Input fields with default values and labels
    with col1:
        fo = st.slider('MDVP:Fo(Hz)', min_value=0, max_value=200, value=110, step=1)
    with col2:
        fhi = st.slider('MDVP:Fhi(Hz)', min_value=0, max_value=400, value=200, step=1)
    with col3:
        flo = st.slider('MDVP:Flo(Hz)', min_value=0, max_value=200, value=90, step=1)
    with col4:
        jitter_percent = st.slider('MDVP:Jitter(%)', min_value=0.0, max_value=1.0, value=0.005, step=0.001)
    with col5:
        jitter_abs = st.slider('MDVP:Jitter(Abs)', min_value=0.0, max_value=0.1, value=0.00005, step=0.00001)

    with col1:
        rap = st.slider('MDVP:RAP', min_value=0.0, max_value=0.1, value=0.002, step=0.001)
    with col2:
        ppq = st.slider('MDVP:PPQ', min_value=0.0, max_value=0.1, value=0.003, step=0.001)
    with col3:
        ddp = st.slider('Jitter:DDP', min_value=0.0, max_value=0.2, value=0.006, step=0.001)
    with col4:
        shimmer = st.slider('MDVP:Shimmer', min_value=0.0, max_value=0.5, value=0.02, step=0.01)
    with col5:
        shimmer_db = st.slider('MDVP:Shimmer(dB)', min_value=0.0, max_value=1.0, value=0.4, step=0.1)

    with col1:
        apq3 = st.slider('Shimmer:APQ3', min_value=0.0, max_value=0.1, value=0.015, step=0.001)
    with col2:
        apq5 = st.slider('Shimmer:APQ5', min_value=0.0, max_value=0.1, value=0.025, step=0.001)
    with col3:
        apq = st.slider('MDVP:APQ', min_value=0.0, max_value=0.1, value=0.03, step=0.01)
    with col4:
        dda = st.slider('Shimmer:DDA', min_value=0.0, max_value=0.2, value=0.04, step=0.01)
    with col5:
        nhr = st.slider('NHR', min_value=0.0, max_value=0.1, value=0.02, step=0.01)

    with col1:
        hnr = st.slider('HNR', min_value=0, max_value=50, value=25, step=1)
    with col2:
        rpde = st.slider('RPDE', min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    with col3:
        dfa = st.slider('DFA', min_value=0.0, max_value=1.0, value=0.7, step=0.1)
    with col4:
        spread1 = st.slider('spread1', min_value=-10.0, max_value=0.0, value=-5.0, step=0.1)
    with col5:
        spread2 = st.slider('spread2', min_value=0.0, max_value=1.0, value=0.5, step=0.1)

    with col1:
        d2 = st.slider('D2', min_value=0.0, max_value=5.0, value=2.5, step=0.1)
    with col2:
        ppe = st.slider('PPE', min_value=0.0, max_value=1.0, value=0.3, step=0.1)

    # Prediction logic for Parkinson's disease
    parkinsons_diagnosis = ''

    # Creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        # Converting user inputs to float
        user_input = [float(fo), float(fhi), float(flo), float(jitter_percent), float(jitter_abs),
                      float(rap), float(ppq), float(ddp), float(shimmer), float(shimmer_db),
                      float(apq3), float(apq5), float(apq), float(dda), float(nhr),
                      float(hnr), float(rpde), float(dfa), float(spread1),
                      float(spread2), float(d2), float(ppe)]

        # Make prediction
        parkinsons_prediction = parkinsons_model.predict([user_input])

        # Interpret prediction result
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)