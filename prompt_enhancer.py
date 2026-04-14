import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Prompt Enhancer", page_icon="")
st.title("Prompt Engineer — PJ's Prompt Enhancer")
st.caption("Powered by OpenAI gpt-4o-mini")

# --- Sidebar: API Key ---
st.sidebar.header("Authentication")
st.sidebar.write("Enter your OpenAI API key to use the app.")
api_key = st.sidebar.text_input("OpenAI API Key", type="password", placeholder="sk-...", help="Your API key is only used for this session and not stored.")

# optional: show a short security note
st.sidebar.markdown(
    """
    **Security note:**  
    Do **not** share your API key. It is not saved to disk by this app.
    """
)

# If the user provided an API key, create the client and show the main UI.
if not api_key:
    st.warning("Please enter your OpenAI API key in the sidebar to continue.")
else:
    client = OpenAI(api_key=api_key)

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
                try:
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

                    # Pull assistant content (SDK returns choices[])
                    enhanced = response.choices[0].message.content
                    st.success("Enhanced Prompt")
                    st.text_area("Enhanced Prompt Output", value=enhanced, height=200)

                except Exception as e:
                    st.error(f"Error: {e}")
