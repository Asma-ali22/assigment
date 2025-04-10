import streamlit as st

st.set_page_config(page_title="My first Website",page_icon=" 🌏 ",layout="centered" \
"")
st.title("Welcome to my first python wbsite")

st.sidebar.title("Navigation")
page=st.sidebar.radio("Go to",["Home","About","Contact"])

if page == "Home":
    st.header("Home page")
    st.write("This is a simple home-page built with python and streamlit")
    name=st.text_input("What\'s your name? ")
    if name:
        st.success(f'Hello {name}! Thank for visiting.')


elif page == "About":
    st.header("About")
    st.write("This webite is built entirely using python and streamlit.")


elif page == "Contact":
    st.header("Contact Us")
    email=st.text_input("Your email")
    message=st.text_input("your message.")
    if st.button("Submit"):
        st.success("Thank you ! we have recieved your message.")