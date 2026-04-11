import streamlit as st
import time

st.set_page_config(page_title="Trustify Secure - Analysis", page_icon="🔍")

def main():
    st.title("🔍 Forensic Analysis Engine")
    
    # Check if we have data from the submission page
    if 'current_submission' not in st.session_state:
        st.warning("No data found for analysis. Please go to the Submit page first.")
        if st.button("Go to Submit"):
            st.switch_page("pages/01_submit.py")
        return

    user_input = st.session_state['current_submission']
    
    st.info(f"Analyzing: **{user_input[:50]}...**")

    # --- Analysis Simulation ---
    progress_text = "Running Multimodal Classifiers..."
    my_bar = st.progress(0, text=progress_text)

    col1, col2 = st.columns(2)
    
    with col1:
        with st.status("NLP Analysis (DistilBERT)...", expanded=True) as status:
            time.sleep(1.5)
            st.write("Extracting linguistic features...")
            time.sleep(1)
            st.write("Checking for urgency and threat keywords...")
            status.update(label="NLP Analysis Complete!", state="complete")
            my_bar.progress(33)

        with st.status("URL/Domain Analysis...", expanded=True) as status:
            time.sleep(1.5)
            st.write("Calculating Levenshtein distance...")
            time.sleep(1)
            st.write("Checking WHOIS reputation...")
            status.update(label="URL Analysis Complete!", state="complete")
            my_bar.progress(66)

    with col2:
        with st.status("Vision & Layout Analysis...", expanded=True) as status:
            time.sleep(2)
            st.write("Running Logo Detection (EfficientNet)...")
            time.sleep(1)
            st.write("Comparing layout pHashes...")
            status.update(label="Vision Analysis Complete!", state="complete")
            my_bar.progress(100)

    # --- Results Preview ---
    st.divider()
    
    st.subheader("Initial Risk Assessment")
    risk_score = 85  # Placeholder for logic in pipeline/fusion.py
    
    if risk_score > 70:
        st.error(f"HIGH RISK: {risk_score}% probability of Phishing")
    else:
        st.success(f"LOW RISK: {risk_score}% probability of Phishing")

    if st.button("Generate Evidence Bundle"):
        st.switch_page("pages/03_evidence.py")

if __name__ == "__main__":
    main()