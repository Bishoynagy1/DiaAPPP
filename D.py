import pandas as pd
import pickle
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from IPython.display import display from main.py 

Doo=pickle.load(open(r'DiabetesApp.sav','rb'))

st.title('Diabetes Prediction Web App')
st.image('1.jpg')
st.info('Diabetes is a chronic, metabolic disease characterized by elevated levels of blood glucose (or blood sugar), which leads over time to serious damage to the heart, blood vessels, eyes, kidneys and nerves. ')
st.text('Check on yourself 👇 ')

Pregnancies=st.text_input('Pregnancies')
Glucose=st.text_input('Glucose')
BloodPressure=st.text_input('BloodPressure')
SkinThickness=st.text_input('SkinThickness')
Insulin=st.text_input('Insulin')
BMI=st.text_input('BMI')
DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction')
Age=st.text_input('Age')


da=pd.DataFrame({'Pregnancies':[Pregnancies],'Glucose':[Glucose],'BloodPressure':[BloodPressure],'SkinThickness':[SkinThickness],'Insulin':[Insulin],'BMI':[BMI],'DiabetesPedigreeFunction':[DiabetesPedigreeFunction],'Age':[Age]},index=[0])
con=st.button('Confirm')
if con:
    result=Doo.predict(da)
    st.write(result)
    if result == 0:
        st.sidebar.write( 'The Patiant Is Clear')
        st.sidebar.image('2.png')
    else:
         st.sidebar.write( 'The Patiant Has Diabetes') 
         st.sidebar.image('3.png')
         
   

