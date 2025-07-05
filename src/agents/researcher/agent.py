
from src.llm_utils import get_gemini_model

class ResearchAgent:
    def __init__(self):
        self.model = get_gemini_model()

    def find_papers(self, topic: str) -> list[str]:
        print(f"ResearchAgent received topic: {topic}")
        prompt = f"List 3-5 highly relevant academic papers (title and primary author) for a master's thesis chapter on the topic: {topic}. Format the output as a numbered list, e.g., '1. Paper Title by Author et al.'."
        response = self.model.generate_content(prompt)
        papers_text = response.text
        
        papers = []
        for line in papers_text.split('\n'):
            line = line.strip()
            if line and line[0].isdigit() and '. ' in line:
                papers.append(line[line.find('. ') + 2:])
        return papers
