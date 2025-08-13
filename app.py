import streamlit as st
from research_agent import run_research

def main():
    """Main Streamlit app function."""
    st.set_page_config(page_title="AI Research Agent", layout="wide")

    st.title(" AI Research Agent")
    st.markdown("Enter a company name and a job role to get a detailed research report.")

    company_name = st.text_input("Company Name", "Google")
    job_role = st.text_input("Job Role", "Software Engineer")

    if st.button("Generate Report", type="primary"):
        if not company_name or not job_role:
            st.warning("Please enter both a company name and a job role.")
            return

        with st.spinner("Our AI agent is researching... This may take a moment."):
            report = run_research(company_name, job_role)
            st.subheader(f"Research Report for {job_role} at {company_name}")
            st.markdown(report)

if __name__ == "__main__":
    main()