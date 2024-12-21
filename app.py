import streamlit as st
import openai

# Auth
openai.api_key = st.secrets['api_key']

# Title 
st.title('Bible Scholar')

st.header("Learning the Word")

instructions = st.text_area(
    "Ask me a theological question? "
)
if (instructions) < 1000:
    if st.button("Show Options"):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Act like a theologian that is well versed in bible studies and doctrines"},
                {"role": "user", "content": instructions}
            ],
            temperature=0,
            max_tokens=1000,
         )

        output = response.choices[0].message.content 
        # Access the message content correctly

else:
        st.warning (
             "Query too long. Write a shorter query."
        )