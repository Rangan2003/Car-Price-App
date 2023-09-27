import pandas as pd
import pickle
import streamlit as st
import linear_regression_model as lrm
import numpy as np


# loading the saved model
loaded_model= pickle.load(open('P:/Python/Machine Learning/Car Price ML/car_price_trained_model.sav', 'rb'))


def main():
    html_temp="""
    <div style="background -color:lightblue;padding:16px">
    <h1 style="color:Cyan;text-align:center;">Car Price Prediction Using ML</h1>
    </div>
    """ 
    st.markdown(html_temp,unsafe_allow_html=True) 
    st.write("")
    st.write("")
    st.markdown("Are You Planning to Sell Your Car?")
    st.markdown("We'll Predict your car's Selling Price.......")
    st.write("")
    st.write("Ok, Let's Predict:")
    p1=st.number_input("What is the Buying Price of the Car (in Lakhs)",2.5,25.0,step=0.5)
    p2=st.number_input("How many Kilometers the car has travelled: ",10,100000000000,step=100)
    s1=st.selectbox("What is your fuel type of your car: ",("Petrol","Diesel","CNG"))
    if s1=="Petrol":
        p3=0
    elif s1=="Diesel":
        p3=1
    elif s1=="CNG":
        p3=2
    s2=st.selectbox("Are You a Dealer or Individual",("Dealer","Individual"))  
    if s2=="Dealer":
        p4=0
    elif s2=="Individual":
        p4=1
    s3=st.selectbox("Transmission Type(Manual/Automatic):",("Manual","Auntomatic"))     
    if s3=="Manual":
        p5=0
    elif s3=="Automatic":
        p5=1
    p6=st.slider("Number of Owners the car previously had? :",0,3)
    p7=st.number_input("Enter the Age of the Car: ",0,30,step=1)
    data_new=pd.DataFrame({
        'Present_Price':p1,
        'Kms_Driven':p2,
        'Fuel_Type':p3,
        'Seller_Type':p4,
        'Transmission':p5,
        'Owner':p6,
        'Age':p7
    },index=[0])
    # input_data=[p1,p2,p3,p4,p5,p6,p7]
    # input_data_as_numpy_array = np.asarray(input_data)
    # # reshape the array as we are predicting for one instance
    # input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(data_new)
    # print(prediction)

    #prediction part
    if st.button("Predict"):
        st.success("You Can Sell your Car for {:.2f} Lakhs".format(prediction))

        st.balloons()

if __name__=='__main__':
    main()
