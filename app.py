import streamlit as st
import pandas as pd
import numpy as np
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

#pg = st.navigation([
#    st.Page("app.py",title="HomeOS", icon="🪴"), st.Page("pages/stats.py", title="Stats")])
# --- USER AUTHENTICATION ---
names = ["Johannes"]
usernames = ["jo"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_credentials = pickle.load(file)

authenticator = stauth.Authenticate(hashed_credentials,
    "homeOS", "auth", cookie_expiry_days=30)


try:
    authenticator.login()
except ValueError as e:
    st.error(f"An error occurred during login: {e}")


if st.session_state.get('authentication_status'):
    with st.sidebar:
        authenticator.logout()

    st.title('NANI APP')

    st.image("cutecat.jpg", caption="A hungry but super cute cat")
    left, middle, right = st.columns(3)
    if left.button("Balloons", use_container_width=True):
        st.balloons()
    if middle.button("Toast", icon="😃", use_container_width=True):
       st.toast('Yey!', icon='😍')
    if right.button("Snow", icon=":material/mood:", use_container_width=True):
        st.snow()

    
elif st.session_state.get('authentication_status') is False:
    st.error('Username/password is incorrect')
elif st.session_state.get('authentication_status') is None:
    st.warning('Please enter your username and password')