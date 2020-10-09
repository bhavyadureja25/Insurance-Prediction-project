import streamlit as st
import numpy as np
import pandas as pd
import pickle
#loading the linear regression model
filename='insmodel.pkl'
regression=pickle.load(open(filename,'rb'))

# Load the standardise data
filename2 = 'insscaler.pkl'
scaler = pickle.load(open(filename2, 'rb'))

def predicting_insurance_premium(age,bmi, children,region,gender, smoker):
    if gender=="Male":
        gender=1
    else:
        gender=0

    if smoker=='Yes'
        smoker=1
    else:
        smoker=0

    if region=='SouthWest':
        region=0
    elif region=='Southeast':
        region=1
    elif region=='Northwest':
        region=2
    else:
        region=3


data=np.array([[age, bmi,children,region,gender,smoker]])
data_s=scalar.transform(data)
prediction=regression.pred(data_s)[0,:]
return(prediction)


def main()
    st.sidebar.header('About')
    st.sidebar.info('This app is created to predict Medical Insurance')
    st.sidebar.info('The dataset consist of 1338 people divided into 4 regions such as Southeast, Southwest, Nrtheast,Northwest')


from PIL import image
image=image.open()

st.sidebar.image(image,width=300)

st.title("Medical Insurance Prediction App")

html_temp = """
      <div style="background-color:#ADD8E6;padding:5px">
       <h2 style="color:white;text-align:center;">Web app Build using Streamlit, Deployed on Heroku </h2>
      </div>
      """
st.markdown(html_temp, unsafe_allow_html=True)

age=st.number_input("Age", min_value=0, max_value=150, value=0)
bmi=st.number_input('BMI', min_value=0, max_value=100, value=0)
Children=st.number_input('Number of Children', min_value=0, max_value=100, value=0)
region=st.selectbox('Please select your region',('Southeast','Southwest','Northeast','Northwest'))
gender=st.selectbox('Please select your gender',('Male','Female'))
smoker=st.selectbox('Do you smoke?',('Yes','No'))

if st.button("Predict"):
    result=predict(age, bmi, gender, children, region, gender, smoker)
    print(result)
