import streamlit as st
import pandas as pd
import pickle

def main():

    #load model
    with open('final_model_xgb.pkl', 'rb') as file:
        xgb = pickle.load(file)

    #inference
    st.title("Smoker Detector!")
    st.write("Enter your health details below:")

    gender = st.selectbox('gender', options=['M', 'F'])
    age = st.slider('age', 0, 100)
    height = st.slider('height(cm)', 0, 300)
    weight = st.slider('weight(kg)', 0, 300)
    waist = st.slider('waist(cm)', 0, 200)
    eyesight_left = st.slider('eyesight left', 0, 10)
    eyesight_right = st.slider('eyesight right', 0, 10)
    hearing_left = st.slider('hearing left', 1, 2)
    hearing_right = st.slider('hearing right', 1, 2)
    systolic = st.slider('systolic', 0, 300)
    relaxation = st.slider('relaxation', 0, 300)
    fasting_blood_sugar = st.slider('fasting blood sugar', 0, 1000)
    cholesterol = st.slider('cholesterol', 0, 500)
    tiglyceride = st.slider('tiglyceride', 0, 500)
    HDL = st.slider('HDL', 0, 500)
    LDL = st.slider('LDL', 0, 500)
    hemoglobin = st.slider('hemoglobin', 0, 50)
    urine_protein = st.slider('urine_protein', 0, 10)
    serum_creatinine = st.slider('serum_creatinine', 0, 10)
    AST = st.slider('AST', 0, 100)
    ALT = st.slider('ALT', 0, 100)
    Gtp = st.slider('Gtp', 0, 200)
    oral = st.selectbox('oral', options=['Y', 'N'])
    dental_caries = st.selectbox('dental_caries', options=[0, 1])
    tartar = st.selectbox('tartar', options=['Y', 'N'])

    data_inf = {
        'gender' : gender,
        'age' : age,
        'height(cm)' : height,
        'weight(kg)' : weight,
        'waist(cm)' : waist,
        'eyesight(left)' : eyesight_left,
        'eyesight(right)' : eyesight_right,
        'hearing(left)' : hearing_left,
        'hearing(right)' : hearing_right,
        'systolic' : systolic,
        'relaxation' : relaxation,
        'fasting blood sugar' : fasting_blood_sugar,
        'Cholesterol' : cholesterol,
        'triglyceride' : tiglyceride,
        'HDL' : HDL,
        'LDL' : LDL,
        'hemoglobin' : hemoglobin,
        'Urine protein' : urine_protein,
        'serum creatinine' : serum_creatinine,
        'AST' : AST,
        'ALT' : ALT,
        'Gtp' : Gtp,
        'oral' : oral,
        'dental caries' : dental_caries,
        'tartar' : tartar
    }
    data_inf = pd.DataFrame([data_inf])
    data_inf

    if st.button("Predict"):
        pred = xgb.predict(data_inf)
        if pred == 0:
            st.write('You are not a smoker!')
        else:
            st.write('You are a smoker!')



    