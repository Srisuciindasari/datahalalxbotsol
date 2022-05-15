import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('INOVBOYO')

def load_data():
    df = pd.read_csv("botsolready.csv")
    return df

dataready=load_data()

cari = st.text_input("Cari Warung/Restaurant")
cariflag=False  
mydata =[]
if(st.button('Submit')):
	result = cari.title()
	if(result):
		st.write("Hasil Pencarian "+result)
		
	else:
		st.error("Masukkan input ya")



#Mengurutkan berdasarkan Review
st.header("Nama Warung/Restoran berdasarkan review")
values = st.slider("Jumlah Warung/Restoran", 5, 20, step=5)
st.table(dataready[['Name','Reviews']].sort_values("Reviews",ascending=False).head(values))


#Data Botsol x Halal
def data_halalbotsol():
    df = pd.read_csv("botsolxhalaladded.csv")
    return df

databotsolhalal=data_halalbotsol()


#Data Warung/Restoran bersetifikat halal
st.header("Nama Warung/Restoran Bersertifikat Halal")
databotsolhalal.round({"No Sertifikat":1})
st.table(databotsolhalal[['Name','Address','Kecamatan','No Sertifikat']].sort_values("No Sertifikat",ascending=False).head(values))