import streamlit as st
import json
import requests
import datetime

# Set page title and emoji icon
st.set_page_config(page_title="Unstoppable Mindset", page_icon="🔥")

# Load User Data
def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"streak": 0, "last_entry": None}

# Save User Data
def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f)

# Get Motivational Quote from API with SSL handling
def get_quote():
    url = "https://api.quotable.io/random"  # Example API for quotes
    try:
        response = requests.get(url, verify=False, timeout=10)  # Disable SSL verification
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        data = response.json()
        return f"💭 _{data['content']}_ – {data['author']}"
    except requests.exceptions.RequestException as e:
        return f"⚠️ Unable to fetch quote: {e}"

# Update Streak
def update_streak(user_data):
    today = str(datetime.date.today())
    if user_data.get("last_entry") != today:
        user_data["streak"] = user_data.get("streak", 0) + 1
    user_data["last_entry"] = today
    save_data(user_data)
    return user_data

# Initialize user data
user_data = load_data()
user_data = update_streak(user_data)

# App Title
st.title("🔥 Unstoppable Mindset: Unlock Your Full Potential 🚀")

# Welcome Header
st.header("💡 Welcome to Your Journey of Growth!")
st.write("Every challenge is an opportunity. This AI-powered app helps you **embrace struggles, reflect on progress, and celebrate victories!** 🌟")

# Display Quote
st.header("💬 Today's Power Quote")
st.write(get_quote())

# User Challenge Input
st.header("🚑 What’s Holding You Back Today?")
user_input = st.text_input("💭 Describe a challenge you're currently facing:")
if user_input:
    user_data["challenge"] = user_input
    save_data(user_data)
    st.success(f"✅ You're confronting: **{user_input}**. Keep pushing forward! 💪🔥")
else:
    st.warning("⚡ Growth starts with awareness. Share your challenge and take the first step! 🏆")

# Reflection Section
st.header("🔄 Turn Struggles into Strength")
reflection = st.text_area("📝 What have you learned from your experiences?")
if reflection:
    user_data["reflection"] = reflection
    save_data(user_data)
    st.success(f"💡 Powerful insight! Your reflection: **{reflection}** 🎯")
else:
    st.info("🔍 Self-reflection fuels progress. 🚀")

# Achievements Section
st.header("🏆 Claim Your Victory!")
achievement = st.text_input("🎉 Share a recent success, big or small:")
if achievement:
    user_data["achievement"] = achievement
    save_data(user_data)
    st.success(f"🔥 Incredible! You accomplished: **{achievement}** 🎯")
else:
    st.info("🌟 Success is a habit—celebrate your progress! 🚀")

# Show Streak Progress
st.write(f"🔥 **Current Streak: {user_data.get('streak', 0)} days! Keep going! 💪**")

# Footer
st.write("---")
st.write("💪 **Your journey to greatness begins now. Keep moving forward!** 🚀🔥")
st.write("✨ **Created by Zeenat Yameen** ✨")
