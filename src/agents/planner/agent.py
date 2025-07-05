

from src.llm_utils import get_gemini_model

class Planner:
    def __init__(self):
        self.model = get_gemini_model()

    def create_plan(self, topic: str) -> str:
        print(f"Planner received topic: {topic}")
        prompt = f"Create a detailed outline for a master's thesis chapter on the topic: {topic}. Include Introduction, Literature Review, Methodology, Results, Discussion, and Conclusion sections, with at least two sub-sections for each major section. Format the output as a numbered list with sub-sections indented."
        response = self.model.generate_content(prompt)
        plan = response.text
        return plan

