import streamlit as st
import requests

# data
api_key = "HLDKYwJQKZJDJAixMWok3AaESiWpLHDcxkjmdbiB"

url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)

content = response.json()

picture_text = content["explanation"]
picture_title = content["title"]
picture_url = content["url"]

# process
st.title(picture_title)
st.image(picture_url)
st.info(picture_text)

# presenting hd image url
hd_pic = content["hdurl"]
st.write("Here is HD version of today's picture:")
st.write(hd_pic)
