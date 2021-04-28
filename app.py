import streamlit as st 
# EDA Pkgs
import pandas as pd 
import numpy as np 
from PIL import Image
# Utils
import os
import pickle
gender_dict = {"male":1,"female":0}
feature_dict = {"No":0,"Yes":1}

def get_value(val):
	if val=='Yes':
		return 1
	else:
		return 0
def get_gender(val):
	if val=="male":
		return 1
	else:
		return 0
def load_model(model_file):
	loaded_model = pickle.load(open(os.path.join(model_file),"rb"))
	return loaded_model
def main():

	# filename='./random_forest.pkl'
	# with open(filename,'rb') as file:
	# 	random_forest=pickle.load(file)
    # df=pd.read_csv('./diabetes_data_upload.csv')
	st.header("Early stage diabetes prediction")
	st.subheader("Predictive Analytics")

	Age=st.number_input("Enter Your age in year",9,100)
	Gender= st.radio("what is your gender",tuple(gender_dict.keys()))
	# fatigue= st.radio("Do You Have Fatiue",tuple(feature_dict.keys()))
	Polyuria=st.radio("Do You Have Polyuria",tuple(feature_dict.keys()))            
	Polydipsia=st.radio("Do You Have Polydipsia",tuple(feature_dict.keys()))     
	sudden_weight_loss=st.radio("Do You Have sudden weight loss",tuple(feature_dict.keys()))
   
	# weakness =st.radio("Do You Have weakness ",tuple(feature_dict.keys()))
           
	# Polyphagia =st.radio("Do You Have Polyphagia",tuple(feature_dict.keys()))
           
	# Genital_thrush =st.radio("Do You Have Genital thrush",tuple(feature_dict.keys()))
      
	# visual_blurring  =st.radio("Do You Have visual blurring",tuple(feature_dict.keys()))
    
	Itching  =st.radio("Do You Have Itching",tuple(feature_dict.keys()))
            
	Irritability =st.radio("Do You Have Irritability",tuple(feature_dict.keys()))
         
	delayed_healing =st.radio("Do You Have delayed healing",tuple(feature_dict.keys()))
     
	partial_paresis=st.radio("Do You Have partial paresis",tuple(feature_dict.keys()))
     
	# muscle_stiffness =st.radio("Do You Have muscle stiffness ",tuple(feature_dict.keys()))
    
	Alopecia =st.radio("Do You Have Alopecia",tuple(feature_dict.keys()))      
	# Obesity=st.radio("Do You Have Obesity",tuple(feature_dict.keys()))
	values=[get_value(Polyuria), get_value(Polydipsia), Age, get_gender(Gender), get_value(partial_paresis),\
       			get_value(sudden_weight_loss), get_value(Irritability), get_value(delayed_healing), get_value(Alopecia),\
       			get_value(Itching)]

   	# st.checkbox("Check Result"):
   	# values=st.header('praneeth')
	options=['suggestions','Predict']
	value=st.selectbox('options',options)
	if value=='Predict':
		model=load_model('./random_forest.pkl')
		pred=model.predict([values])

		
		{"Polyuria":get_value(Polyuria)
		,"Polydipsia":get_value(Polydipsia),"Age":Age,"gender":get_gender(Gender), "partial_paresis":get_value(partial_paresis),\
       			"sudden_weight_loss":get_value(sudden_weight_loss), "Irritability":get_value(Irritability), "delayed_healing":get_value(delayed_healing), "Alopecia":get_value(Alopecia),\
       			"Itching":get_value(Itching)
       			}

       	# df=pd.read_csv('./')


		if pred==0:
			st.success('Safe')

		if pred==1:
			st.warning("High chances of Desease")

		# if pred==0:
		# 	st.warning('diseased')
		# if pred==1:
		# 	st.success('not deseased')


		# print(model.score([values]))





							
    





    # if result==1:
    #  	st.warning("Has higher chance of diabetes please go for lab tests")
    # elif result==0:
    #  	st.success('No diabetes')

      




  	




if __name__== "__main__":
	main()