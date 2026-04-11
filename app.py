import streamlit as st

st.title("Trustify Secure: AI & Blockchain Evidence")
st.subheader("Combined Team Project")

user_input = st.text_area("Paste suspicious content here:")

if st.button("Analyze"):
    st.write("AI is analyzing...")
    # This is where your DistilBERT model will go later!
    st.success("Analysis Complete (Mockup)")    