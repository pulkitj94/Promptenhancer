import streamlit as st
st.set_page_config(page_title="Prompt Enhancer", page_icon="📝")
st.title("📝 Prompt Engineer — General Prompt Enhancer")

st.caption("Demo Mode - Learn how to structure better prompts!")

st.subheader("Enter Context, Constraint, Structure, Checkpoint, Review (CC-SC-R)")
context = st.text_input("Context", value="Enter a detailed context for the task")
constraint = st.text_area("Constraint", value="Enter the constraint(s) to keep in mind")
structure = st.text_area("Structure", value="Enter the structure of the desired output")
checkpoint = st.text_area("Checkpoint", value="Define any checkpoint or validations to be considered while processing the output")
review = st.text_area("Review", value="Enter the review or approval process for the output")

st.subheader("Paste your rough prompt")

draft = st.text_area("Your draft prompt:", height=300)

if st.button("Enhance Prompt"):
    if not draft.strip():


        st.warning("Please enter a draft prompt.")

    else:
        # Demo output - shows structured approach
        instruction = (
            "Generate an enhanced, structured prompt using CC-SC-R.\n"
            "1) Improve clarity and completeness\n"
            "2) Ask ONE clarifying question\n"
            "3) Specify output format (3 bullets, ≤12 words each)\n"
        )
        demo_output = (
            f"CONTEXT: {context}\n"
            f"CONSTRAINT: {constraint}\n"
            f"STRUCTURE: {structure}\n"
            f"CHECKPOINT: {checkpoint}\n"
            f"REVIEW: {review}\n"
            f"USER DRAFT:\n{draft}\n\n"
            "OUTPUT FORMAT:\n- 3 concise bullets\n- 1 clarifying question"
        )
        
        st.success("Enhanced Prompt (Demo Mode)")
        st.code(instruction + "\n" + demo_output, language="markdown")
        
        st.info("💡 This is demo mode showing the CC-SC-R structure. In live mode, AI would generate the actual enhanced prompt!")




