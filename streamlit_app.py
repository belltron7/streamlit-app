import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Page setup
st.set_page_config(page_title="My Streamlit Dashboard", layout="wide")

# Title and intro text
st.title("📊 My First Streamlit Dashboard")
st.write("Welcome! This dashboard shows interactive charts and input widgets.")

# Sidebar controls
with st.sidebar:
    st.header("🔧 Controls")
    name = st.text_input("Enter your name", placeholder="Ada Lovelace")
    show_data = st.checkbox("Show random data table")

# Main content
st.subheader("👋 Greeting")
if name:
    st.success(f"Hello, {name}! 👋")
else:
    st.info("Please enter your name in the sidebar.")

# Generate some sample data
df = pd.DataFrame({
    'x': range(1, 21),
    'y': np.random.randn(20).cumsum()
})

# Chart
st.subheader("📈 Example Line Chart")
chart = alt.Chart(df).mark_line(point=True).encode(
    x='x',
    y='y'
)
st.altair_chart(chart, use_container_width=True)

# Optional data table
if show_data:
    st.subheader("🧮 Raw Data")
    st.dataframe(df)

