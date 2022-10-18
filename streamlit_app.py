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
def pandas_sellout(source, x="mês", y='real'):
    # Create a selection that chooses the nearest point & selects based on x-value
    hover = alt.selection_single(
        fields=[x],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(source)
        .mark_line(point="transparent")
        .encode(x=x, y=y)
        #.transform_calculate(color='datum.delta < 0 ? "red" : "green"')
    )

    # Draw points on the line, highlight based on selection, color based on delta
    points = (
        lines.transform_filter(hover)
        .mark_circle(size=65)
        .encode(color=alt.Color("color:N", scale=None))
    )

    # Draw an invisible rule at the location of the selection
    tooltips = (
        alt.Chart(source)
        .mark_rule(opacity=0)
        .encode(
            x=x,
            y=y,
            #tooltip=[x, y, alt.Tooltip("delta", format=".2%")]
            ,
        )
        .add_selection(hover)
    )

    return (lines + points).interactive()

df_filtrado = dados[(dados.ds_subcategoria == time_frame) & (dados['mês'] >= start_date.strftime("%Y-%m-%d"))][['mês', 'real']]                   
st.altair_chart(pandas_sellout(df_filtrado), use_container_width=True)
