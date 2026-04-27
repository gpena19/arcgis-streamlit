import streamlit as st
import pandas as pd

st.title("📊 Climate Data Dashboard")

df = pd.read_csv("pages/refugee_temp_all_view.csv")

df["year"] = pd.to_numeric(df["year"])
df["avg_surface_temp_c"] = pd.to_numeric(df["avg_surface_temp_c"])

st.write("Total rows:", len(df))

countries = sorted(df["country_name"].unique())
selected_country = st.selectbox("Choose a country", countries)

country_df = df[df["country_name"] == selected_country].sort_values("year")

st.dataframe(country_df, use_container_width=True)

st.line_chart(country_df.set_index("year")["avg_surface_temp_c"])