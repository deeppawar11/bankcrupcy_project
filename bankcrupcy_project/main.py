import numpy as np
import pickle
import streamlit as st
from PIL import Image

# loading the saved model
loaded_model = pickle.load(open(r'RandomForestClassifier','rb'))

def Cluster_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Bankcrupcy'
    else: 
      return 'Non-Bankcrupcy'


def main():
    
    # giving a title
    st.title('Bankcrupcy Prediction')
    
    # getting the input data from the user
    
    competitiveness = st.text_input('Enter competitiveness')
    financial_flexibility = st.text_input('Enter financial_flexibility')
    credibility = st.text_input('Enter credibility')
    management_risk = st.text_input('Enter management_risk')
   
    
    # code for Prediction
    Predict = ''
    
    # creating a button for Prediction
    
    if st.button('Submit'):
        Predict = Bankcrupcy_prediction([competitiveness,financial_flexibility,credibility,management_risk])

    st.success(Predict)
    
if __name__ == '__main__':
    main()
