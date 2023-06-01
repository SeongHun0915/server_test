from back import *
import streamlit as st
from streamlit_option_menu import option_menu


def add_symbol1(symbol):
    question = st.session_state["question"]
    question += symbol
    st.session_state["question"] = question

def add_symbol2(symbol):
    solution = st.session_state["solution"]
    solution += symbol
    st.session_state["solution"] = solution

st.title('수학 증명 계산기')

with st.sidebar:
    selected = option_menu("목록", ["계산기", "계산기 가이드"],
        icons=['house', 'caret-right-square'], menu_icon="cast", default_index=0)
    selected

if selected == '계산기':

    st.subheader("문제 입력")

    if "question" not in st.session_state:
        st.session_state["question"] = ""

    # 문제 입력
    question = st.session_state["question"]
    question = st.text_input("", question, key="question")
    gptQuestion = "question: " + question


    symbol1 = ["√", "^", "sin", "cos", "tan", "log", "∫"]
    button_col1 = st.columns(5)
    for i, symbol in enumerate(symbol1):
        if button_col1[i % 5].button(symbol, key=f"button1_{i}"):
            add_symbol1(symbol)


    st.subheader('문제 풀이 입력')

    if "solution" not in st.session_state:
        st.session_state["solution"] = ""

    # 문제 풀이 입력
    solution = st.session_state["solution"]
    solution = st.text_input(" ", solution, key="solution")
    gptSolution = "solution: " + solution

    symbol2 = ["√", "^", "sin", "cos", "tan", "log", "∫"]
    button_col2 = st.columns(5)
    for i, symbol in enumerate(symbol2):
        if button_col2[i % 5].button(symbol, key=f"button2_{i}"):
            add_symbol2(symbol)


    st.subheader("정답 확인")
    is_correct = check_answer(gptQuestion, gptSolution)
    sub = is_correct.split("&&&")

    if st.button("OX 확인"):

        if question and solution:  # type: ignore
            st.write(is_correct)
            if "좀치네" in is_correct:
                st.success("정답입니다!")
            elif "맞겠냐" in is_correct:
                st.error("틀렸습니다. 다시 확인해보세요.")
            else:
                st.write("멍청한 gpt")

        show_solution = st.checkbox("풀이를 확인하시겠습니까?")
        if show_solution:
            st.write(sub[1])
