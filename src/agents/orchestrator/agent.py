
from src.agents.planner.agent import Planner
from src.agents.researcher.agent import ResearchAgent
from src.agents.citation.agent import CitationAgent
from src.agents.summarizer.agent import SummarizerAgent
from src.agents.writer.agent import WriterAgent
from src.agents.latex.agent import LatexAgent
from src.agents.editor.agent import EditorAgent

class Orchestrator:
    def __init__(self):
        self.planner = Planner()
        self.researcher = ResearchAgent()
        self.citation_agent = CitationAgent()
        self.summarizer_agent = SummarizerAgent()
        self.writer_agent = WriterAgent()
        self.latex_agent = LatexAgent()
        self.editor_agent = EditorAgent()

    def handle_thesis_command(self, goal: str, topic: str | None = None):
        print(f"Orchestrator received goal: {goal} with topic: {topic}")

        if goal == "write a chapter":
            if not topic:
                print("Error: 'topic' is required for 'write a chapter' goal.")
                return
            print(f"Orchestrator is executing task: Write a chapter on {topic}")
            plan = self.planner.create_plan(topic)
            print("\n--- Plan Created ---")
            print(plan)

            papers = self.researcher.find_papers(topic)
            print("\n--- Found Papers ---")
            for paper in papers:
                print(f"- {paper}")

            self.citation_agent.add_citations(papers)

            summaries = self.summarizer_agent.summarize_papers(papers)
            print("\n--- Summaries ---")
            for paper, summary in summaries.items():
                print(f"- {paper}: {summary}")

            # Initial writing
            section = self.writer_agent.write_section(plan, summaries, papers)
            print("\n--- Initial Section Written ---")
            print(section)

            # Feedback loop
            feedback = self.editor_agent.provide_feedback(section)
            print("\n--- Editor Feedback ---")
            print(feedback)

            revised_section = self.writer_agent.revise_section(section, feedback)
            print("\n--- Revised Section Written ---")
            print(revised_section)

            self.latex_agent.create_latex_document(revised_section)
        else:
            print(f"Unknown goal: {goal}")

