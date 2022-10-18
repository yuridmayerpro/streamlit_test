import streamlit as st
import pandas as pd
from datetime import date, datetime

st.title('Teste - Título')


dados = pd.read_csv('final_processed_df_streamlit.csv', encoding='iso-8859-1')


col1, col2, = st.columns(2)

with col1:
    start_date = st.date_input(
        "Select start date",
        date(2017, 1, 1),
        min_value=datetime.strptime("2017-01-01", "%Y-%m-%d"),
        max_value=datetime.now(),
    )

with col2:
    time_frame = st.selectbox(
        "Produtos", ('Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E', 'Produto F', 'Produto G', 'Produto H', 'Produto I')
    )



