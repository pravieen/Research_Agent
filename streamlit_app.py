import streamlit as st
import requests
import json

st.set_page_config(
    page_title="Research Paper Assistant",
    page_icon="🔬",
    layout="wide"
)

def main():
    st.title("📚 Research Paper Assistant")
    st.write("Enter a research topic and get AI-powered summaries of relevant papers")

    # User inputs
    query = st.text_input("Enter your research topic:", placeholder="e.g., brain tumor detection")
    max_results = st.slider("Number of papers to analyze:", min_value=1, max_value=10, value=5)

    if st.button("Search and Analyze", type="primary"):
        if not query:
            st.error("Please enter a research topic")
            return

        with st.spinner("🔍 Searching and analyzing papers..."):
            try:
                # Make API request to FastAPI backend
                response = requests.post(
                    "http://localhost:8000/api/v1/research/summarize",
                    json={"query": query, "max_results": max_results}
                )
                
                if response.status_code == 200:
                    data = response.json()
                    
                    # Display synthesis
                    st.header("📊 Research Overview")
                    st.write(data["synthesis"])
                    
                    # Display individual papers
                    st.header("📑 Paper Summaries")
                    for i, (paper, summary) in enumerate(zip(data["papers"], data["summaries"])):
                        with st.expander(f"Paper {i+1}: {paper['title']}", expanded=False):
                            st.write("**Authors:**", ", ".join(paper["authors"]))
                            st.write("**Published:**", paper["published"])
                            st.write("**Summary:**")
                            st.write(summary)
                            st.write("**Links:**")
                            st.write(f"- [Paper]({paper['url']})")
                            if paper.get("pdf_url"):
                                st.write(f"- [PDF]({paper['pdf_url']})")
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            
            except Exception as e:
                st.error(f"Error connecting to backend server: {str(e)}")

if __name__ == "__main__":
    main()