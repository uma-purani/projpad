import streamlit as st

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

        # Simulate response based on tone and project type
        response = f"({tone} tone) Here's a structured starting point for your {project_type.lower()} based on what you shared:"

        if option == "Brain Dump":
            response += "Start with your core excitement. \n Then narrow the scope. \n End with a question you'd like to explore."
        elif option == "Start with Keywords":
            response += "Define each keyword briefly. \n Link them together into a theme. \n Expand with real-world examples."
        elif option == "Describe a Scene":
            response += "Set the scene vividly. \n Identify the conflict or core action. \n Translate it into a topic or problem statement."
        elif option == "Problem-Solution Outline":
            response += "What’s the problem? \n Why does it matter? \n What’s a possible angle or solution you want to explore?"

        st.success(response)

else:
    st.header("Focus Mode")
    st.text_area("Write freely here...", height=300)
