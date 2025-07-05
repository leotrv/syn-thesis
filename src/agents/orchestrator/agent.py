
from src.agents.planner.agent import Planner
from src.agents.researcher.agent import ResearchAgent
from src.agents.citation.agent import CitationAgent
from src.agents.summarizer.agent import SummarizerAgent
from src.agents.writer.agent import WriterAgent
from src.agents.latex.agent import LatexAgent

class Orchestrator:
    def __init__(self):
        self.planner = Planner()
        self.researcher = ResearchAgent()
        self.citation_agent = CitationAgent()
        self.summarizer_agent = SummarizerAgent()
        self.writer_agent = WriterAgent()
        self.latex_agent = LatexAgent()

    def execute_task(self, task: str):
        print(f"Orchestrator is executing task: {task}")
        plan = self.planner.create_plan(task)
        print("\n--- Plan Created ---")
        print(plan)

        papers = self.researcher.find_papers(task)
        print("\n--- Found Papers ---")
        for paper in papers:
            print(f"- {paper}")

        self.citation_agent.add_citations(papers)

        summaries = self.summarizer_agent.summarize_papers(papers)
        print("\n--- Summaries ---")
        for paper, summary in summaries.items():
            print(f"- {paper}: {summary}")

        section = self.writer_agent.write_section(plan, summaries, papers)
        print("\n--- Section Written ---")
        print(section)

        self.latex_agent.create_latex_document(section)

