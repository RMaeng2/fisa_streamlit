import streamlit as st
import pandas as pd # streamlit은 그냥 input output인

data = "./README.md"
slider_val = "ddsfwe"


df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

st.button("클릭 미")
st.download_button("Download file", data)
url='https://github.com/RMaeng2'
st.link_button("Go to gallery", url)
st.page_link("pages/app2.py", label="Home")
st.data_editor(df)
st.checkbox("I agree")
st.feedback("thumbs")
st.pills("Tags", ["Sports", "Politics"])
st.radio("Pick one", ["cats", "dogs"])
st.segmented_control("Filter", ["Open", "Closed"])
st.toggle("Enable")
st.selectbox("Pick one", ["cats", "dogs"])
st.multiselect("Buy", ["milk", "apples", "potatoes"])
st.slider("Pick a number", 0, 100)
st.select_slider("Pick a size", ["S", "M", "L"])
st.text_input("First name")
st.number_input("Pick a number", 0, 10)
st.text_area("Text to translate")
st.date_input("Your birthday")
st.time_input("Meeting time")
st.file_uploader("Upload a CSV")
st.audio_input("Record a voice message")
st.camera_input("Take a picture")
st.color_picker("Pick a color")

def foo():
    print('abc')

def b():
    pass

# Use widgets' returned values in variables:
for i in range(int(st.number_input("Num:"))):
    foo()
if st.sidebar.selectbox("I:",["f"]) == "f":
    b()

st.sidebar_val2 = st.sidebar.slider("Quinn Mallory")
st.write(sidebar_val2)
my_slider_val = st.slider("Quinn Mallory", 1, 88)
st.write(slider_val)

# Disable widgets to remove interactivity:
st.slider("Pick a number", 0, 100, disabled=True)

st.dataframe(df)
st.table(data.iloc[0:10])
st.json({"foo":"bar","fu":"ba"})
st.metric("My metric", 42, 2)

st.image("./header.png")
st.audio(data)
st.video(data)
st.video(data, subtitles="./subs.vtt")
st.logo("logo.jpg")