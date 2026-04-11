import streamlit as st

# Set page configuration
st.set_page_config(page_title="Trustify Secure - Submit", page_icon="🛡️")

def main():
    st.title("🛡️ Trustify Secure")
    st.subheader("Forensic Phishing Detection & Evidence Packaging")
    
    st.markdown("""
    Welcome to the **Trustify Secure** submission portal. 
    Enter a suspicious URL or paste an email body below to begin the multimodal analysis.
    """)

    # Create a container for the input
    with st.container():
        input_type = st.radio("What would you like to analyze?", ["URL / Website Link", "Email Content"])
        
        if input_type == "URL / Website Link":
            user_input = st.text_input("Enter URL (e.g., http://suspicious-site.com)", placeholder="https://...")
        else:
            user_input = st.text_area("Paste Email Body", placeholder="Paste the full text of the suspicious email here...", height=200)

        # Action button
        if st.button("Start Analysis"):
            if user_input:
                st.info("Submission received. Redirecting to Analysis Engine...")
                # In the future, we will link this to 02_analyze.py
                st.session_state['current_submission'] = user_input
            else:
                st.warning("Please provide an input before proceeding.")

    # Sidebar info
    st.sidebar.header("Project Status")
    st.sidebar.success("Environment: Development")
    st.sidebar.info("The system uses DistilBERT for NLP and SHA-256 for evidence integrity.")

if __name__ == "__main__":
    main()