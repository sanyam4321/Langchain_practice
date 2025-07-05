import streamlit as st
import time

@st.cache_data(ttl=60)
def fetch_data():
    time.sleep(3)
    return {"data": "cached data"}

st.write("Fetching data...")
data = fetch_data()
st.write(data)