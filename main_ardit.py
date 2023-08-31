import streamlit as st
import requests

# url data
api_key = "HLDKYwJQKZJDJAixMWok3AaESiWpLHDcxkjmdbiB"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# first response json (all data)
response = requests.get(url)
data = response.json()

# extracting data from json
title = data["title"]
text = data["explanation"]
image_url = data["url"]

# downloading image
response2 = requests.get(image_url)  # new request on image link
file_path = "img.jpg"  # storage file
with open(file_path, "wb") as file:  # opening the file in write-binary mode
    file.write(response2.content)  # writing content of response2 in a file

# display
st.title(title)
st.image("img.jpg")
st.info(text)

