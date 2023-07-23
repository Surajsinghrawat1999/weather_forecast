import streamlit as st

st.title("Weather Forecast For The Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1,
                 max_value=5,
                 help="Select the number of days of forecast")
option = st.selectbox("Select data to view",
                      ("Temperature", "sky"))
st.subheader(f"{option} for the next {days} days in {place}")
