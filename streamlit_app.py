import streamlit as st
import pandas as pd
from datetime import date, datetime
import altair as alt

st.title('Teste - Título')


dados = pd.read_csv('final_processed_df_streamlit.csv', encoding='iso-8859-1', sep=';')
dados.loc[:, 'mês'] = pd.to_datetime(dados['mês'])

################################### Filtros ###################################
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
    
################################### Consctução do gráfico de sellout ###################################
def get_chart(source, x="mês", y='real'):
    # Create a selection that chooses the nearest point & selects based on x-value
    hover = alt.selection_single(
        fields=[x],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(source, height=500, title="Sellout")
        .mark_line()
        .encode(
            x=alt.X("mês", title="Data"),
            y=alt.Y("real", title="Sellout"),
            color="symbol",
        )
    )
    
    # Draw points on the line, and highlight based on selection
    points = lines.transform_filter(hover).mark_circle(size=65)
    
    # Draw a rule at the location of the selection
    tooltips = (
        alt.Chart(source)
        .mark_rule()
        .encode(
            x="yearmonthdate(date)",
            y="price",
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("mês", title="Data"),
                alt.Tooltip("real", title="Sellout"),
            ],
        )
        .add_selection(hover)
    )

    return (lines + points + tooltips).interactive()

    
    
    
    

df_filtrado = dados[(dados.ds_subcategoria == time_frame) & (dados['mês'] >= start_date.strftime("%Y-%m-%d"))][['mês', 'real']]                   
st.altair_chart(get_chart(df_filtrado), use_container_width=True)
