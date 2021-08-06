# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 07:07:48 2021

Comparativa JARVIS

"""
#%%Llibreries

import streamlit as st
from PIL import Image
import pandas as pd

#%% Capçalera
hide_st_style="""
    <style>
    
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)
logo = Image.open('Logo batalle.jpg')

st.image(logo, width = 200)

st.title('Anàlisi Comparatiu Serres Jarvis')
st.markdown("""
S'analitzen costos de la serra Jarvis Pneumàtica i Hidràulica
""")


#%% Barra lateral i Panell Principal
#Barra lateral
st.sidebar.header('Opcions Entrada')

## barra lateral opcions
opcions = ['Especificacions','Comparativa Cost']
#base_price_unit 
seleccio = st.sidebar.selectbox('Selecciona la opció que vulguis observar', opcions)
#%% Funcions

def especificacions():
    st.title(' Especificacions')
    st.markdown("""Característiques i especificacions de les serres """)
    col1,col2 = st.beta_columns(2)
    col1.header("Jarvis Pneumàtica")
    esp_pneu=Image.open('Datasheet Pneumàtica.PNG')
    col1.image(esp_pneu,width=250)
    col1.success("""
                  - Menor pes
                  - Menors components
                  """)
    col1.error("""
                - Menor Potència
                - Menor velocitat de tall
                - Més vibració
                """)
    
    col2.header("Jarvis Hidràulica")
    esp_hidr=Image.open('Datasheet Hidràulica.PNG')
    col2.image(esp_hidr,width=450)
    col2.success("""
                  - Triple Potència
                  - 1000 rpm més
                  - Menor vibració
                  
                  """)
    col2.error("""
                - Major pes(0,5 kg)
                - Major instal·lació i components
                """)
def cost_compra():
    st.title('Cost de compra')
    col1,col2 = st.beta_columns(2)
    col1.header("Jarvis Pneumàtica")
    pres_pneu=Image.open('Pressupost Pneumatica.PNG')
    col1.image(pres_pneu,width=250)
    col1.markdown('El cost de compra és de ** 2.500€ ** però cal associar 300€ de latiguillos')
    col2.header("Jarvis Hidràulica")
    pres_hidr=Image.open('Pressupost Hidràulica.PNG')
    col2.image(pres_hidr,width=250)
    col2.markdown('El cost de compra és de ** 14.423 €**')
def cost_manteniment():
    st.title('Cost de Manteniment')
    col3,col4=st.beta_columns(2)
    col3.header("Jarvis Pneumàtica")
    df_pneu_mant=pd.read_csv('Manteniment Jarvis Pneumàtica.csv',sep=';')
    col3.write(df_pneu_mant)
    col3.markdown('Cost de recanvis anual aproximat ** 2.200€ **')
    col4.header("Jarvis Hidràulica")
    mant_hidr=Image.open('Cost Manteniment Hidr.PNG')
    col4.image(mant_hidr)
    col4.markdown('Cost de manteniment estimat ** 3.571 € **')
def cost_energ():
    st.title('Cost energètic')
    col5,col6=st.beta_columns(2)
    col5.header("Jarvis Pneumàtica")
    compr=Image.open('Compressors.PNG')
    col5.image(compr)
    col5.markdown("""Tenim 2 models de 75kW, un de 37kW i un de 45 kW un cabal total aproximat a 40 m3/min i consum aproximat anual de 400.000kWh/any. Com la serra consumeix 0,77 m3/min representa un consum aproximat de 7.700kWh a 0,09 €/kWh ** 693 € **""")
    col6.header("Jarvis Hidràulica")
    col6.markdown(""" La serra consumeix 1,865kW elèctrics i , suposant 9,5 hores i 248 dies/any té un consum de 4.400 kWh/any, considerant 0,09€/kWh tenim un cost de    ** 400€**""" )

def comparativa():
    st.markdown('# Comparativa')
    Columnes=['Pneumàtica','Hidràulica']
    Files=['Cost Compra','Cost Manteniment','Cost Energètic']
    valors=[[2800,14423],[2200,3571],[693,400]]
    df=pd.DataFrame(valors,columns=Columnes,index=Files)
    st.write(df)
    st.markdown("# Amortització ")
    st.markdown("Considerant un horitzó de 5 anys per Hidràulica i 2 anys pneumàtica:")
    valor=[14423/5,2800/2]
    amort=pd.DataFrame(valor,Columnes)
    st.write(amort)
    st.markdown("** Per igualar l'amortització de la serra pneumàtica cal 10 anys de la hidràulica **")
    

def costos():
    costos=['Cost de Compra','Cost de Manteniment','Cost Energètic','Comparativa i Amortització']
    cost=st.selectbox('Selecciona el cost',costos)
    if cost == 'Cost de Compra':
        cost_compra()
    elif cost == 'Cost de Manteniment':
        cost_manteniment()
    elif cost == 'Cost Energètic':
        cost_energ()
    elif cost == 'Comparativa i Amortització':
        comparativa()

    
if seleccio == 'Especificacions':
    especificacions()
if seleccio == 'Comparativa Cost':
    costos()
           
    



