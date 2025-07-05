

class WriterAgent:
    def __init__(self):
        pass

    def write_section(self, plan: str, summaries: dict[str, str], citations: list[str]) -> str:
        print("\nWriterAgent received plan, summaries, and citations.")
        # This is a placeholder. In the future, this would use an LLM to write a section.
        section_text = r"""
\section{Introduction}

This is the introduction to the chapter. It is based on the following plan:

---

"""
        section_text += self._escape_latex(plan)
        section_text += "\n\n---\n\nHere are the summaries of the papers I read:\n\n"
        for paper, summary in summaries.items():
            section_text += f"- {self._escape_latex(summary)}\n"

        section_text += "\nI will be citing the following papers: \n\n"
        for citation in citations:
            section_text += f"- {self._escape_latex(citation)}\n"
        return section_text

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

