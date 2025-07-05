

import os

class LatexAgent:
    def __init__(self, output_dir="output/tex"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def create_latex_document(self, content: str, filename="thesis.tex"):
        print(f"\nCreating LaTeX document at {os.path.join(self.output_dir, filename)}")
        latex_template = r"""\documentclass{{article}}

\title{{My Thesis}}
\author{{Your Name}}
\date{{\today}}

\begin{{document}}

\maketitle

{content}

\end{{document}}
""".format(content=content)
        with open(os.path.join(self.output_dir, filename), "w") as f:
            f.write(latex_template)

    def read_latex_document(self, filename="thesis.tex") -> str:
        file_path = os.path.join(self.output_dir, filename)
        if os.path.exists(file_path):
            print(f"\nReading existing LaTeX document from {file_path}")
            with open(file_path, "r") as f:
                return f.read()
        else:
            print(f"\nNo existing LaTeX document found at {file_path}. Starting fresh.")
            return ""

