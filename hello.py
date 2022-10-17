import streamlit as st
import time
import pandas as pd
import numpy as np
import seaborn as sns
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
#import pickle  #to load a saved model
import base64  #to open .gif files in streamlit app
from pandas.api.types import is_numeric_dtype
from streamlit_option_menu import option_menu
import plotly.express as px
import json
import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import matplotlib.pyplot as plt

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
           
            footer {visibility: hidden;}
          
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


st.sidebar.image('covid19.jpeg')
st.sidebar.title("DATASET ON COVID-19")

@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value


    
#app_mode = st.sidebar.selectbox('Select Work',['HOME','',]) #tree pages

# 1. as sidebar menu
with st.sidebar:
    app_mode= option_menu("Main Menu", ['Data_Exploring','Home','Data Visualization','Contact'], 
        icons=["list-task",'house',"list-task",'envelope'],menu_icon="cast", default_index=1)
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }    
    app_mode
    
if app_mode=='Home':
        def load_lottiefile(filepath: str):
            with open(filepath, "r") as f:
                return json.load(f)
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        lottie_coding = load_lottiefile("welcome.json")  # replace link to local lottie file
        lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_69HH48.json")

        st_lottie(
            lottie_hello,
            speed=1,
            reverse=False,
            loop=True,
            quality="low", # medium ; high
            #renderer="svg", # canvas
            height=None,
            width=None,
            key=None,
        )
        st.balloons() 
        st.title ("Coronavirus Pandemic in World (COVID-19 ANALYSIS)")
        st.markdown('Coronavirus Country Profiles built 207 country profiles which allow you to explore the statistics on the coronavirus pandemic for every country in the world.In a fast-evolving pandemic it is not a simple matter to identify the countries that are most successful in making progress against it. For a comprehensive assessment, we track the impact of the pandemic across our publication and we built country profiles for 207 countries to study in depth the statistics on the coronavirus pandemic for every country in the world.')

elif app_mode=='Data_Exploring':
        a=st.sidebar.slider('Enter a number of head', 1, 10)
        b=st.sidebar.slider('Enter a number of tail', 1, 10)
       
        st.title('Exploretion of Dataset :')     
        with st.spinner('Wait for it...'):
             time.sleep(5)

        data = pd.read_csv("coviddata.csv")
        AgGrid(data)
        st.markdown('Display the head of Dataset')
        st.write(data.head(a))
        st.markdown('Display the tail of Dataset')
        st.write(data.tail(b))
       

        app_mod = st.sidebar.selectbox('Statistic Describetive',['Shape of Dataset','Vue a Sample', 'Summe of Duplications','Type of Dataset','Nomber of Columns','Miss_value','Summary','Covariate','Correlation',])

        if app_mod=='Type of Dataset':
             st.markdown('The Type of the Dataset')
             st.write(type(data))

        elif app_mod=='Shape of Dataset':
              st.markdown('The Shape of the Dataset')
              st.write(data.shape)
        elif app_mod=='Vue a Sample':
              st.markdown('Display the sample of Dataset')
              c=st.sidebar.slider('Enter a number of sample', 1, 20)
              st.write(data.sample(c))

        elif app_mod=='Summe of Duplications':
              st.markdown('The Summe of all Duplication')
              st.write(data.duplicated().sum())

        elif app_mod=='Nomber of Columns':
              st.markdown('The Nomber of Columns')
              st.write(data.columns)

        elif app_mod=='Miss_value':    
              st.markdown('Display the Miss value in Dataset')
              st.write(data.isna().sum())

        elif app_mod=='Summary': 
              st.markdown('Display a Summary of Dataset')
              st.write(data.describe())

        elif app_mod=='Covariate':
              st.markdown('Summary for the covariate')
              st.write(data.cov())

        elif app_mod=='Correlation':
              st.markdown('Summary for the corelation')
              st.write(data.corr())

        

elif app_mode=='Data Visualization':
      with st.spinner('Wait for it...'):
        time.sleep(7)
        st.title('Visualisation of COVID-19')
      def load_lottiefile(filepath: str):
            with open(filepath, "r") as f:
                return json.load(f)
      def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

      lottie_coding = load_lottiefile("dat.json")
      lottie_hello = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_qp1q7mct.json")

      st_lottie(
            lottie_hello,
            speed=1,
            reverse=False,
            loop=True,
            quality="low", # medium ; high
            #renderer="svg", # canvas
            height=None,
            width=None,
            key=None,
       )
    
        

      #f = px.data.grapminder()
      df = pd.read_csv("coviddata.csv")

      year_options = df['continent'].unique().tolist()
      data = st.selectbox('Which continent would you like to see?',year_options, 0)
      df = df[df['continent']==data]
      fig = px.scatter(df, x = 'new_deaths',y='hosp_patients',
                         color= 'continent', hover_name = 'continent', 
                         log_x = True, size_max=55,range_x =[100,100000], range_y=[25,90])
      #ig.update_loyout(width=800)
      #t.write(fig)
      #hart_data = df,columns=['continent', 'hosp_patients']

      
      st.sidebar.button('Graph')
      st.line_chart(df.new_deaths)
        
   


        #and=np.random.normal(1, 2, size=20)
      columns=['new_deaths', 'hosp_patients']
      st.line_chart(df.hosp_patients)
    
     #st.sidebar.button('Bar_graph')
      #t.sidebar.button('Bar_chart')
        
      

        

else:
    
      def load_lottiefile(filepath: str):
            with open(filepath, "r") as f:
                return json.load(f)
      def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

      lottie_coding = load_lottiefile("h.json")
      lottie_hello = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_M9p23l.json")

      st_lottie(
            lottie_hello,
            speed=1,
            reverse=False,
            loop=True,
            quality="low", # medium ; high
            #renderer="svg", # canvas
            height=None,
            width=None,
            key=None,
       )
    
        
      st.title("PAUSTI")
      st.header("Option:Msc Data Science")
      st.header('Reg: MD300-0006/2021')
      st.header("Name: Abdoul Aziz Diallo")
      st.header('Email:dialloa513@gmail.com')
    
