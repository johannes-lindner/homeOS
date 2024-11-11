import streamlit as st
import pandas as pd
import numpy as np

#pg = st.navigation([
#    st.Page("app.py",title="HomeOS", icon="🪴"), st.Page("pages/stats.py", title="Stats")])


st.title('NANI APP')

st.image("cutecat.jpg", caption="A hungry but super cute cat")
left, middle, right = st.columns(3)
if left.button("Balloons", use_container_width=True):
    st.balloons()
if middle.button("Toast", icon="😃", use_container_width=True):
   st.toast('Yey!', icon='😍')
if right.button("Snow", icon=":material/mood:", use_container_width=True):
    st.snow()