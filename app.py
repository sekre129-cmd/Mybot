import streamlit as st

st.title("Мой первый ИИ бот")
st.write("Привет! Если ты это видишь, значит бот на GitHub работает.")

user_input = st.chat_input("Напиши мне что-нибудь...")
if user_input:
    st.write(f"Ты написал: {user_input}")
    st.info("Чтобы я стал умным, нужно подключить API-ключ, но пока я просто повторяю за тобой!")
