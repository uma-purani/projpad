pip install openai

import streamlit as st
import openai
import os

#api key
openai.api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="ProjPad: The Student's Creative Assistant", layout="centered")

# Set up sidebar for toggle settings
st.sidebar.title("ProjPad Settings")

tone = st.sidebar.radio("Select Assistant's Tone:", ["Academic", "Gentle", "Encouraging"])
project_type = st.sidebar.selectbox("What are you creating today?", ["Essay", "Short Story", "Presentation", "Research Idea", "Other"])
focus_mode = st.sidebar.checkbox("Focus Mode (If you want to freewrite)", value=False)

# Set up main interface
st.title("ProjPad: Your Creative Assistant")
st.caption("The intuitive assistant for ADHD students building creative projects.")

if not focus_mode:
    st.markdown("Let's Go!")
    st.markdown("How do you want to get started?")

    option = st.radio("Idea Entry Method:", [
        "Brain Dump",
        "Start with Keywords",
        "Describe a Scene",
        "Problem-Solution Outline"
    ])

    user_input = st.text_area("Tell me your thoughts...", height=200)

    if st.button("Generate a Suggestion"):
        st.markdown("ProjPad's Suggestion")

        system_prompt = f"You are a supportive, neurodivergent-friendly writing coach. Respond in a {tone.lower()} tone. Help the user develop a {project_type.lower()} idea based on the method '{option}'. Give practical suggestions in a friendly voice."


        with st.spinner("Thinking..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_input}
                    ],
                    temperature=0.7
                )
                suggestion = response.choices[0].message.content.strip()
                st.success(suggestion)
            except Exception as e:
                st.error(f"Something went wrong: {e}")

else:
    st.header("Focus Mode")
    st.text_area("Write freely here...", height=300)
