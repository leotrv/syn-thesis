

from src.llm_utils import get_gemini_model

class WriterAgent:
    def __init__(self):
        self.model = get_gemini_model()

    def write_section(self, plan: str, summaries: dict[str, str], citations: list[str], existing_thesis_content: str) -> str:
        print("\nWriterAgent received plan, summaries, and citations.")
        
        summaries_text = "\n".join([f"- {summary}" for summary in summaries.values()])
        citations_text = "\n".join([f"- {citation}" for citation in citations])

        if existing_thesis_content:
            existing_content_prompt = f"You are continuing to write a master's thesis. Here is the current content of the thesis:\n\n{existing_thesis_content}\n\nYour task is to write the next logical section or expand on an existing section based on the provided plan. Do not rewrite the entire thesis. Only provide the new or updated section content. Ensure proper LaTeX structure and continuity."
        else:
            existing_content_prompt = ""

        prompt = fr"""Based on the following plan, summaries of research papers, and citations, write a detailed section for a master's thesis. Focus on the content and structure as outlined in the plan. Incorporate insights from the summaries and reference the citations where appropriate. Ensure the output is in LaTeX format.

{existing_content_prompt}
Plan:
{plan}

Summaries of Research Papers:
{summaries_text}

Citations to be used:
{citations_text}

Begin writing the section now, starting with the \section{{{...}}} command as per the plan's first section. Ensure all LaTeX special characters are properly escaped.
"""
        response = self.model.generate_content(prompt)
        section_content = response.text

        # Escape LaTeX special characters in the generated content
        section_content = self._escape_latex(section_content)

        return section_content

    def revise_section(self, original_text: str, feedback: str) -> str:
        print("\nWriterAgent received feedback for revision.")
        prompt = f"""You are a writer. Revise the following text based on the provided feedback. Ensure the revised text addresses all points in the feedback, maintains an academic tone, and is in LaTeX format. Pay close attention to clarity, coherence, and grammar. Ensure all LaTeX special characters are properly escaped.

Original Text:
{original_text}

Feedback:
{feedback}

Revised Text:
"""
        response = self.model.generate_content(prompt)
        revised_content = response.text
        revised_content = self._escape_latex(revised_content)
        return revised_content

    def _escape_latex(self, text: str) -> str:
        # Basic LaTeX escaping
        text = text.replace("\\", "\\textbackslash{}") # Escape backslashes first
        text = text.replace("&", "\\&")
        text = text.replace("%", "\\%")
        text = text.replace("$", "\\$")
        text = text.replace("#", "\\#")
        text = text.replace("_", "\\_")
        text = text.replace("{", "\\{")
        text = text.replace("}", "\\}")
        text = text.replace("~", "\\textasciitilde{}")
        text = text.replace("^", "\\textasciicircum{}")
        text = text.replace("<", "\\textless{}")
        text = text.replace(">", "\\textgreater{}")
        return text

