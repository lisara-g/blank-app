import streamlit as st

st.title("hello WOF fans")
a = 1
b = 10
c = a + b

for i in range(20):

    st.write(
        f"hi im lisara. I am {i} years old .head over to [docs.streamlit.io](https://docs.streamlit.io/)."
    )

    st.write(f"hey guys {i}")
