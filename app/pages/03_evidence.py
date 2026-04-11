import streamlit as st
import datetime

st.set_page_config(page_title="Trustify Secure - Evidence", page_icon="📜")

def main():
    st.title("📜 Forensic Evidence Bundle")
    
    # Placeholder for the risk score we generated in the previous step
    risk_score = 85 
    
    st.success("Analysis finalized. Evidence package is ready for forensic export.")

    with st.expander("View Forensic Details", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Timestamp:**", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            st.write("**Analysis Integrity:** SHA-256 Verified")
        with col2:
            st.write("**Legal Admissibility Score:** 92/100")
            st.write("**Blockchain Status:** Pending Sync...")

    # Display a simulated hash
    st.code("SHA-256: 7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069", language="bash")

    st.markdown("### Download Options")
    st.button("📥 Download JSON Evidence Report")
    st.button("📄 Export PDF for Legal Use")
    
    if st.button("Back to New Submission"):
        st.switch_page("pages/01_submit.py")

if __name__ == "__main__":
    main()
    