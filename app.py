import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


df = pd.read_csv("dados_transporte_bh.csv", sep=";")
df.columns = df.columns.str.strip()
df["LINHA"] = df["LINHA"].astype(str).str.strip()
df = df[~df["PC"].isin([0, 3])]
viagens = df.groupby("LINHA").size().reset_index(name="viagens")


st.set_page_config(
    page_title="Prova Final De Python Frederico Rocha",
    page_icon="🔥",
    layout="wide"
)


df = pd.DataFrame(viagens)  

df_filtrado = df[
    (df["LINHA"] == "SC01A") &
    (df["PC"].isin["1", "2"])
].copy()

st.sidebar.title("Navegação do Painel")
pagina = st.sidebar.radio(
    "Ir para:",
    ["Tabela", "Gráfico"]
)

if pagina == "Tabela":
    st.title("Tabela das 10 viagens mais feitas")
    st.dataframe()


else:
    st.title("Gráfico Com as 10 viagens")
    st.dataframe(
            df_filtrado[["LINHA", "PC", "VIAGEM"]],
            hide_index=True,
            use_container_width=True
        )