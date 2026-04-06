import streamlit as st
from groq import Groq

st.title("Мой личный ИИ Помощник")

# Ввод ключа (чтобы не светить его в коде)
api_key = st.sidebar.text_input("Вставь сюда свой Groq API Key", type="password")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Показываем историю чата
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Поле ввода
if prompt := st.chat_input("Спроси меня о чем угодно..."):
    if not api_key:
        st.error("Пожалуйста, введи API ключ в боковой панели слева!")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Запрос к ИИ
        client = Groq(api_key=api_key)
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        
        response = completion.choices[0].message.content
        
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
