import streamlit as st
from model import load_model, predict_maturity_index

def main():
    st.title('Red Banana Maturity Predictor')

    fruit_weight = st.number_input('Fruit Weight (g):')
    fruit_length = st.number_input('Fruit Length (cm):')
    fruit_girth = st.number_input('Fruit Girth (cm):')
    caliper = st.number_input('Caliper (mm):')

    if st.button('Predict'):
        # Make a prediction using the trained model
        input_data = [fruit_weight, fruit_length, fruit_girth, caliper]
        maturity_index = predict_maturity_index(input_data)

        # Display the result
        st.success(f'Maturity Index: {maturity_index}')

if __name__ == '__main__':
    main()
