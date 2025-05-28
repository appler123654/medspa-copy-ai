import streamlit as st
import openai
import os

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("醫美文案自動產生器")

目的 = st.selectbox("選擇行銷目的", ["曝光", "促銷", "引流"])
風格 = st.selectbox("選擇語氣風格", ["專業", "溫柔", "青春活潑", "時尚有型"])
內容 = st.text_area("輸入活動/療程重點")

if st.button("產生文案"):
    prompt = f"請用{風格}語氣，針對醫美行銷目的「{目的}」，撰寫文案：{內容}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    result = response.choices[0].message.content
    st.success("文案產生完成")
    st.text_area("AI文案", result, height=200)
