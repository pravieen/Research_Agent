# agents/research_agent.py
from src.tools.arxiv import search_arxiv
from src.agents.summarizer_agent import summarize_full_text, synthesize_overview
from src.tools.pdf import download_and_extract_pdf


class ResearchAgent:
    def run(self, query: str, max_results: int = 5):
        # Step 1: Fetch paper metadata from arXiv
        print("🔍 Step 1: Searching arXiv for:", query)
        papers = search_arxiv(query, max_results)

        if not papers:
            return {"error": "No papers found"}

        # Step 2: Download and extract full text from each paper (PDF)
        print(f"📄 Step 2: Downloading and extracting text from {len(papers)} papers")
        full_texts = []

        for i, paper in enumerate(papers):
            title = paper["title"]
            pdf_url = paper.get("pdf_url")

            if not pdf_url:
                print(f"⚠️ No PDF URL for '{title}'")
                continue

            try:
                print(f"📥 [{i+1}/{len(papers)}] Downloading and extracting: {title[:80]}...")
                full_text = download_and_extract_pdf(pdf_url)

                if len(full_text.strip()) == 0:
                    print(f"❌ Empty content from PDF: {title}")
                    continue

                full_texts.append({
                    "title": title,
                    "full_text": full_text
                })

            except Exception as e:
                print(f"❌ Error processing '{title}': {str(e)}")

        if not full_texts:
            return {"error": "No valid paper content could be extracted from PDFs"}

        # Step 3: Summarize each paper's full text
        print("🧠 Step 3: Summarizing papers with LLM")
        summaries = []
        for i, item in enumerate(full_texts):
            title = item["title"]
            full_text = item["full_text"]

            print(f"📝 [{i+1}/{len(full_texts)}] Summarizing: {title[:60]}...")

            try:
                summary = summarize_full_text(full_text[:12000])  # Limit input size
                summaries.append(f"Title: {title}\nSummary: {summary}")
            except Exception as e:
                print(f"⚠️ Failed to summarize '{title}': {str(e)}")

        # Step 4: Synthesize an overall report
        print("🧩 Step 4: Synthesizing overview of all papers")
        synthesis = synthesize_overview(summaries)

        return {
            "papers": papers,
            "summaries": summaries,
            "synthesis": synthesis
        }