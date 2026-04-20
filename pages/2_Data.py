import streamlit as st
import pandas as pd

st.title("📊 Climate Data Dashboard")

df = pd.read_csv("../refugee_temp_all_view.csv")

# Fix types (important)
df["year"] = pd.to_numeric(df["year"])
df["avg_surface_temp_c"] = pd.to_numeric(df["avg_surface_temp_c"])

st.write("Total rows:", len(df))

# Dropdown
countries = sorted(df["country_name"].unique())
selected_country = st.selectbox("Choose a country", countries)

# Filter
country_df = df[df["country_name"] == selected_country].sort_values("year")

# Table
st.dataframe(country_df, use_container_width=True)

# Chart
st.line_chart(country_df.set_index("year")["avg_surface_temp_c"])