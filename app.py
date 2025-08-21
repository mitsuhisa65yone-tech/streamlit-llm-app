import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

# Streamlit画面タイトル
st.title("LLM質問アプリ")

# 入力フォーム
user_input = st.text_input("質問を入力してください：")

# OpenAI APIキーを環境変数から取得
openai_api_key = os.getenv("OPENAI_API_KEY")

# APIキーの存在確認
if not openai_api_key:
    st.error("OpenAI APIキーが設定されていません。環境変数OPENAI_API_KEYを設定してください。")
    st.stop()

# ChatOpenAIインスタンス
try:
    chat = ChatOpenAI(
        openai_api_key=openai_api_key,
        temperature=0.7,
        model="gpt-3.5-turbo"
    )
except Exception as e:
    st.error(f"ChatGPTの初期化に失敗しました: {str(e)}")
    st.stop()

# 送信ボタン
if st.button("送信"):
    if user_input:
        try:
            # メッセージの作成
            message = HumanMessage(content=user_input)
            
            # ChatGPTに問い合わせ
            with st.spinner("回答を生成中..."):
                response = chat([message])
            
            # 回答表示
            st.markdown("### 回答")
            st.write(response.content)
            
        except Exception as e:
            st.error(f"エラーが発生しました: {str(e)}")
    else:
        st.warning("質問を入力してください。")