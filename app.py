import streamlit as st
from groq import Groq

st.set_page_config(page_title="Мой ИИ", layout="centered")
st.title("🤖 Мой личный ИИ")

# Открываем боковую панель сразу
with st.sidebar:
    st.header("Настройки")
    api_key = st.text_input("Вставь Groq API Key сюда:", type="password")
    st.info("Ключ начинается на gsk_...")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Спроси меня о чем угодно..."):
    if not api_key:
        st.warning("Сначала вставь API-ключ в меню слева!")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            client = Groq(api_key=api_key)
            # Используем самую новую и стабильную модель
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile", 
                messages=[{"role": "user", "content": prompt}]
            )
            
            response = completion.choices[0].message.content
            
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
            
        except Exception as e:
            st.error(f"Ошибка: {e}")
            st.info("Проверь, правильно ли скопирован ключ (без лишних пробелов).")
