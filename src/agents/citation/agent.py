

import os

class CitationAgent:
    def __init__(self, bib_file_path="data/bib/references.bib"):
        self.bib_file_path = bib_file_path
        os.makedirs(os.path.dirname(bib_file_path), exist_ok=True)

    def add_citations(self, papers: list[str]):
        print("\nCitationAgent received papers:")
        bib_entries = ""
        for paper in papers:
            print(f"- {paper}")
            # This is a placeholder. In the future, this would generate
            # a proper BibTeX entry for each paper.
            if "Vaswani" in paper:
                bib_entries += """@article{vaswani2017attention,
  title={Attention is all you need},
  author={Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N and Kaiser, {Ł}ukasz and Polosukhin, Illia},
  journal={Advances in neural information processing systems},
  volume={30},
  year={2017}
}
"""
        self._save_bibliography(bib_entries)

    def _save_bibliography(self, content: str):
        print(f"\nSaving bibliography to {self.bib_file_path}")
        with open(self.bib_file_path, "w") as f:
            f.write(content)

