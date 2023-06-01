import openai
import streamlit as st

API_KEY = "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"

@st.cache_resource
def get_openai_chat_completion_model(question, solution):  # type: ignore
    openai.api_key = API_KEY
    completion = openai.ChatCompletion.create(  # type: ignore
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "아래에 주어진 question에 대한 solution이 맞는지 틀렸는지 판별해라."},
            {"role": "user", "content": "solution이 틀렸을 때 '맞겠냐'라고 답해라. solution이 맞았을 때 '좀치네'라고 답해라."},
            {"role": "user", "content": "solution이 틀렸을 때 '맞겠냐'라고 답하고 '&&&'를 출력하고 올바른 풀이를 제공해라."},
            {"role": "user", "content": question},
            {"role": "user", "content": solution}
        ],
        temperature=0.8,
        max_tokens=2048
    )
    return completion["choices"][0]["message"]["content"].encode("utf-8").decode()  # type: ignore

def check_answer(question, solution):  # type: ignore
    model = get_openai_chat_completion_model(question, solution)  # ChatCompletion 객체 가져오기 #type: ignore
    return model  # type: ignore
