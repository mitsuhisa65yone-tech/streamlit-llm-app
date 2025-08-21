from dotenv import load_dotenv

load_dotenv()


import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain


st.title("Hello Streamlit!")


# アプリ概要・操作説明
st.markdown("""
### このアプリについて
このWebアプリは、医療・法律・ITの各分野の専門家AIに質問できるチャットサービスです。
""")
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
#### 操作方法
1. 画面上部のラジオボタンで相談したい専門家の種類を選択してください。
2. 下のテキストボックスに質問内容を入力してください。
3. Enterキーもしくは送信ボタンを押すと、選択した専門家AIがあなたの質問に回答します。

※ 回答はAIによる自動生成です。重要な判断は必ず専門家にご相談ください。
""")
st.markdown("<br>", unsafe_allow_html=True)


# 専門家の種類を最初に選択
st.markdown("#### 専門家の種類を選択してください")
expert_type = st.radio(
    "",
    ("医療専門家", "法律専門家", "ITエンジニア")
)
st.markdown("<br>", unsafe_allow_html=True)

system_messages = {
    "医療専門家": "あなたは優秀な医療専門家です。専門的かつ分かりやすく回答してください。",
    "法律専門家": "あなたは経験豊富な法律専門家です。法律的観点から丁寧に回答してください。",
    "ITエンジニア": "あなたは熟練したITエンジニアです。技術的な観点から分かりやすく回答してください。"
}

def get_expert_answer(user_input: str, expert_type: str) -> str:
    """
    入力テキストと専門家の種類を受け取り、LLMからの回答を返す
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_messages[expert_type]),
        ("human", "{input}")
    ])
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run({"input": user_input})
    return response

st.markdown("#### 入力してください")
user_input = st.text_input("")
send_button = st.button("送信")
st.markdown("<br>", unsafe_allow_html=True)

# エンターキー（user_inputが空でない）または送信ボタンのどちらでも送信
if (user_input and (send_button or st.session_state.get("_input_submitted", False))):
    response = get_expert_answer(user_input, expert_type)
    st.write("専門家({})の回答:".format(expert_type), response)

# st.text_inputでエンター送信時のフラグを管理
if user_input and not send_button:
    st.session_state["_input_submitted"] = True
else:
    st.session_state["_input_submitted"] = False