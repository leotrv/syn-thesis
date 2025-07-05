from src.llm_utils import get_gemini_model

class EditorAgent:
    def __init__(self):
        self.model = get_gemini_model()

    def provide_feedback(self, text: str) -> str:
        print("\nEditorAgent received text for feedback.")
        prompt = f"Review the following text and provide constructive feedback for improvement. Focus on clarity, coherence, academic tone, and grammar. Suggest specific changes where possible.\n\nText:\n{text}"
        response = self.model.generate_content(prompt)
        feedback = response.text
        return feedback
