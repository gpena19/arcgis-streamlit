import streamlit as st

st.set_page_config(
    page_title="Climate Heatmap Analysis",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Climate Heatmap Analysis Dashboard")
st.subheader("ArcGIS + Streamlit Project")

st.markdown("---")

left, right = st.columns([2, 1])

with left:
    st.markdown("""
    ## Project Overview

    This project analyzes the impact of **anthropogenic climate change** by combining
    environmental and demographic data to model and visualize risk over time.

    Historical climate data are used to explore predictive patterns and are overlaid
    with vulnerable population data to identify groups that may be disproportionately affected.
    """)

with right:
    st.info("""
    **Project Status**
    - Streamlit dashboard: Working
    - ArcGIS map: In progress
    - PostgreSQL pipeline: Included
    - Findings page: Ready
    """)

st.markdown("---")

st.markdown("## Key Focus Areas")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Climate & Environmental Risk
    - Extreme heat wave analysis
    - Sea level rise visualization
    - Historical climate trend exploration
    - Risk modeling over time
    """)

with col2:
    st.markdown("""
    ### Population Vulnerability
    - Low-income housing in the U.S.
    - Refugee camps in Pakistan, Jordan, Kenya, Tanzania, Ethiopia, and Sudan
    - Disproportionate climate impacts
    - Climate-driven displacement risk
    """)

st.markdown("---")

st.markdown("## Methodology")

m1, m2, m3 = st.columns(3)

with m1:
    st.metric("Database", "PostgreSQL")

with m2:
    st.metric("GIS Platform", "ArcGIS")

with m3:
    st.metric("Dashboard", "Streamlit")

st.markdown("""
- Data are stored and managed in a **PostgreSQL database**
- Geographic variables are processed and visualized in **ArcGIS**
- Results are presented through an interactive **Streamlit dashboard**
- The framework supports future expansion with additional datasets
""")

st.markdown("---")

st.markdown("## Purpose & Impact")

st.warning("""
This analysis emphasizes the importance of **education, preparation, and awareness**
as part of climate mitigation and adaptation.

By identifying vulnerable populations and high-risk areas, the project supports:
- emergency response planning
- infrastructure resilience
- risk assessment
- climate adaptation strategy
""")

st.markdown("---")

st.markdown("## System Architecture")

st.code(
    "PostgreSQL Database  →  ArcGIS Processing  →  Streamlit Dashboard",
    language="text"
)

st.markdown("---")

st.markdown("## Dashboard Navigation")
st.write("""
Use the pages on the left to explore:
- **Map** for spatial visualization
- **Data** for sample trends and summaries
- **Findings** for project meaning and impact
""")