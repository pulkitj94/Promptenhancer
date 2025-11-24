import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# --- Load .env ---
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

st.set_page_config(page_title="Prompt Enhancer", page_icon="📝")
st.title("📝 Prompt Engineer — General Prompt Enhancer")
st.caption("Powered by OpenAI gpt-4o-mini")

# --- Inputs ---
st.subheader("Enter Context, Constraint, Structure, Checkpoint, Review (CC-SC-R)")

context = st.text_input("Context")
constraint = st.text_area("Constraint")
structure = st.text_area("Structure")
checkpoint = st.text_area("Checkpoint")
review = st.text_area("Review")

st.subheader("Paste your rough prompt")
draft = st.text_area("Your draft prompt:", height=300)

# --- Enhance Prompt ---
if st.button("Enhance Prompt"):
    if not draft.strip():
        st.warning("Please enter a draft prompt.")
    else:
        with st.spinner("Enhancing using gpt-4o-mini..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert prompt engineer. Rewrite prompts using CC-SC-R structure."
                    },
                    {
                        "role": "user",
                        "content": f"""
                    CONTEXT: {context}
                    CONSTRAINT: {constraint}
                    STRUCTURE: {structure}
                    CHECKPOINT: {checkpoint}
                    REVIEW: {review}

                    USER DRAFT:
                    {draft}

                    Please:
                    - Improve clarity and completeness
                    - Ask ONE clarifying question
                    - Output in 3 bullets (max 12 words each)
                    """
                    }
                ]
            )

            enhanced = response.choices[0].message.content

        st.success("Enhanced Prompt")
        st.write(enhanced)
