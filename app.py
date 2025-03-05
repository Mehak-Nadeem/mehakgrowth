import streamlit as st
st.set_page_config(page_title= "growth mindset project", project_icon="★")
st.title("Growth Mindset Challenge: Web App with streamlit")
st.header("🚀 Welcome to Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI powered app helps you build a growth mindset with reflection, challenges, and achievement! 🌼")

#quote section
st.header("💡TOdays Growth Mindset Quotes")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts. Winston Churchill")
st.header(" 🔧 What's Your Challege you're Today?")
user_input = st.text("Describe a challenge you're facing:")

#CONDITION
if user_input:
    st.success(f" 💪You're facing:{user_input}. Keep pushing forward towards your goal!🚀")
else:
    st.warning("Tell us about your your challenge to get started!")
 
 #reflexing
st.header("Reflect on Your Learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f" ✨Great Insight| Your reflection: {reflection}")


else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")

    #acheivements
    st.header("🏆 Celebrate your Wins!")
acheivement = st.text_input("Share something you've recently accomlished")

if acheivement:
    st.success(f"🎉 Amazing! you achieved: {acheivement}")
else:
    st.info("Big or small , every acheivement counts! Share one now 😍")

    #FOOTER
    st.write("-  -  -")
    st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! ✨")
    st.write("* * ❤ Created by Mehak Nadeem ❤ * *")


