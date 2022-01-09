import streamlit as st

# Custom imports 
from multipage import MultiPage
import landing

# Create an instance of the app 
app = MultiPage()

# Configuration of the main page
st.set_page_config(page_title="Team Lion", layout="wide")

# Add all your applications (pages) here
app.add_page("Get Your Cat Video", landing.app)

# The main app
app.run()
