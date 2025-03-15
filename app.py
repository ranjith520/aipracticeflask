import streamlit as st

st.title("Hello Streamlit-er 👋")
st.caption(":rainbow[Enjoy building Google IDX Platform]")
st.markdown(
    """ 
    This is a playground for you to try Streamlit and have fun. 

    **There's so much] you can build!**
    "Now update the app.py to customize your code/app"
    
    """
)

if st.button("Send balloons!"):
    st.balloons()