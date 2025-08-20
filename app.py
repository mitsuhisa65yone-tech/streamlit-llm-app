
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Streamlit画面タイトル
st.title("LLM質問アプリ")

# 入力フォーム
user_input = st.text_input("質問を入力してください：")

# LangChain LLMインスタンス（APIキーは環境変数やSecretsで管理してください）
llm = OpenAI(temperature=0.7)

# 送信ボタン
if st.button("送信"):
	if user_input:
		# プロンプトテンプレート（必要に応じてカスタマイズ）
		prompt = PromptTemplate(
			input_variables=["question"],
			template="{question}"
		)
		formatted_prompt = prompt.format(question=user_input)
		# LLMに問い合わせ
		response = llm(formatted_prompt)
		# 回答表示
		st.markdown("### 回答")
		st.write(response)
	else:
		st.warning("質問を入力してください。")