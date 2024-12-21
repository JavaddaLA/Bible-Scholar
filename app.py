import streamlit as st
import openai

# Auth
openai.api_key = st.secrets['api-key']

# Title 
st.title('Bible Scholar')

st.header("Learning the Word")

instructions = st.text_area(
    "Ask me a theological question? "
)

