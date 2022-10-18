import streamlit as st
import pandas as pd
from datetime import date, datetime
import altair as alt
alt.themes.enable("streamlit")
st.title('Teste - Título')


dados = pd.read_csv('final_processed_df_streamlit.csv', encoding='iso-8859-1', sep=';')
dados.loc[:, 'mês'] = pd.to_datetime(dados['mês'])

################################### Filtros ###################################
time_frame = st.selectbox("Produtos", ('Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E', 'Produto F', 'Produto G', 'Produto H', 'Produto I'))
    
################################### Gráfico ###################################
df_filtrado = dados[(dados.ds_subcategoria == time_frame) & (dados['mês'] >= start_date.strftime("%Y-%m-%d"))][['mês', 'real']].set_index('mês')
st.line_chart(filtra(dados), use_container_width=True)
