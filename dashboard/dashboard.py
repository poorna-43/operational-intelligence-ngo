import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="NGO Operational Intelligence",
    layout="wide"
)

st.title("NGO Operational Intelligence Dashboard")

summary_api = "http://127.0.0.1:8000/summary"
programs_api = "http://127.0.0.1:8000/programs"
insights_api = "http://127.0.0.1:8000/insights"

summary_data = requests.get(summary_api).json()
programs_data = requests.get(programs_api).json()
insights_data = requests.get(insights_api).json()

program_df = pd.DataFrame(programs_data)

st.subheader("Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Programs", summary_data["total_programs"])
col2.metric("Total People Helped", summary_data["total_people_helped"])
col3.metric("Total Cost", summary_data["total_cost"])
col4.metric("Total Volunteers", summary_data["total_volunteers"])

st.subheader("People Helped per Program")

fig1 = px.bar(
    program_df,
    x="program_name",
    y="people_helped",
    title="People Helped per Program"
)

st.plotly_chart(fig1, use_container_width=True)

st.subheader("Cost per Program")

fig2 = px.bar(
    program_df,
    x="program_name",
    y="cost",
    title="Cost per Program"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("Volunteers per Program")

fig3 = px.bar(
    program_df,
    x="program_name",
    y="volunteers",
    title="Volunteers per Program"
)

st.plotly_chart(fig3, use_container_width=True)

st.subheader("NGO Decision Insights")

st.info(f"Highest Impact Program: {insights_data['highest_impact_program']}")
st.info(f"Most Cost Efficient Program: {insights_data['most_cost_efficient_program']}")

