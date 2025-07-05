

from src.llm_utils import get_gemini_model

class SummarizerAgent:
    def __init__(self):
        self.model = get_gemini_model()

    def summarize_papers(self, papers: list[str]) -> dict[str, str]:
        print("\nSummarizerAgent received papers:")
        summaries = {}
        for paper in papers:
            print(f"- {paper}")
            prompt = f"Provide a concise summary of the academic paper titled: {paper}"
            response = self.model.generate_content(prompt)
            summaries[paper] = response.text
        return summaries

