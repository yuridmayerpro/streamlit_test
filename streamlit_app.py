import streamlit as st
import pandas as pd

st.title('Teste - Título')


dados = pd.read_excel('final_processed_df_streamlit.xlsx', engine='openpyxl')


