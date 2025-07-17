import os
import streamlit as st
from post_generator import generate_post, idea_generator

st.set_page_config(page_title="Startup Post Generator")
st.title("🚀 LinkedIn Post Generator for Startups")

brand = st.text_input("Startup Name", "MyStartup")
tone  = st.selectbox("Tone", ["Professional", "Inspirational", "Casual"])
topic_choice = st.radio("Topic Source", ["My own topic", "Surprise me!"])

if topic_choice == "My own topic":
    topic = st.text_input("Enter your topic")
else:
    topic = idea_generator(brand)
    st.success(f"Try this topic: {topic}")

if st.button("Generate Post"):
    with st.spinner("Generating…"):
        post = generate_post(brand, topic, tone.lower())
        st.markdown("### ✍️ Your LinkedIn Post")
        st.write(post)
        st.markdown("**Copy & paste to LinkedIn or Buffer!**")
