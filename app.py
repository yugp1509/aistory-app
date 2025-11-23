import streamlit as st
import openai

# Set your OpenAI API key via Streamlit Secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Streamlit frontend
st.set_page_config(page_title="AI Story Generator", page_icon="📖")
st.title("📖 AI Story Generator")
st.write("Generate creative stories using AI!")

# User input
prompt = st.text_area("Enter your story idea or prompt:")

# Story length
length = st.slider("Story Length (number of words)", 50, 1000, 300)

# Generate story button
if st.button("Generate Story"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt!")
    else:
        with st.spinner("Generating story..."):
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=f"Write a creative story about: {prompt}",
                    max_tokens=length,
                    temperature=0.7,
                )
                story = response.choices[0].text.strip()
                st.subheader("Generated Story")
                st.write(story)
            except Exception as e:
                st.error(f"Error: {e}")
