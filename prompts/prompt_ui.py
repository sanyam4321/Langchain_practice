from langchain_ollama import ChatOllama
import streamlit as st
from langchain_core.prompts import load_prompt
import os

model = ChatOllama(model="llama3.2", temperature=1.1, num_predict=1000)


with st.form(key="user_prompt"):
    paper_input = st.selectbox("Select Research paper name", [
        "Select",
        "Attention is all you need",
        "Bert: Pre-training of Deep Bidirectional Transformers",
        "GPT-3 Language Models are few-shot learners",
        "Diffusion model beats GANs on Image Synthesis"
    ])

    style_input = st.selectbox("Select Explanation Style", [
        "Select",
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ])

    length_input = st.selectbox("Select Explaination Length", [
        "Select",
        "Short(1-2 paragraph)",
        "Medium(3-5 paragraph)",
        "Long(detailed explanation)"
    ])

    template = load_prompt(os.path.join(os.getcwd(), "prompts", "template.json"))

    

    submit_btn = st.form_submit_button("Summarize")

if submit_btn:
        with st.spinner("Generating Output: "):
            chain = template | model
            result = chain.invoke({
            'paper_input': paper_input,
            'style_input': style_input,
            'length_input': length_input
            })
            st.write(result.content)