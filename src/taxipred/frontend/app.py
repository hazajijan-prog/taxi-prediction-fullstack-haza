import streamlit as st 
import pandas as pd
import httpx 

URL = http://127.0.0.1:8000 
data = httpx.get(f"{URL}/taxi")

df = pd.DataFrame(data.json())

def main(): 
    st.markdown ("# Taxi prediction app")

    st.dataframe(df)

if __name__ == "__main__":
    main()
    