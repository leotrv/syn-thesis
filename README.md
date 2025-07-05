# Syn-Thesis: A Multi-Agent System for Thesis Writing

Syn-Thesis is a multi-agent system designed to assist in the process of writing a master's thesis. It leverages large language models (LLMs) to automate various tasks, including planning, research, summarization, writing, and editing, with a focus on generating LaTeX-formatted output.

## Features

*   **Orchestrated Workflow:** A central Orchestrator agent manages the entire thesis writing process, delegating tasks to specialized agents.
*   **LLM-Powered Agents:**
    *   **Planner:** Generates detailed thesis outlines based on your topic.
    *   **Research Agent:** Identifies relevant academic papers.
    *   **Summarizer Agent:** Provides concise summaries of research papers.
    *   **Writer Agent:** Drafts thesis sections, incorporating plans, summaries, and citations.
    *   **Editor Agent:** Provides constructive feedback on written sections, enabling an iterative revision process.
*   **LaTeX Output:** Generates thesis content in LaTeX format, including proper structuring and citation handling.
*   **Persistent Writing:** Agents can read existing thesis content and continue writing or revise sections, allowing for progress over multiple sessions.
*   **Extensible Architecture:** Designed to easily integrate new agents and functionalities.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

*   **Leo Traven**

## Setup Instructions

Follow these steps to set up the Syn-Thesis project on your local machine.

### 1. Navigate to Your Target Folder

Open your terminal and navigate to the directory where you want to clone the repository:

```bash
cd /path/to/your/desired/directory
```

### 2. Clone the Repository

Clone the Syn-Thesis repository from GitHub:

```bash
git clone https://github.com/your-username/syn-thesis.git
cd syn-thesis
```
**Note:** Replace `https://github.com/your-username/syn-thesis.git` with the actual URL of your repository.

### 3. Set Up a Virtual Environment with `uv`

It is highly recommended to use `uv` for dependency management. If you don't have `uv` installed, you can install it via `pip`:

```bash
pip install uv
```

Once `uv` is installed, create a virtual environment and install the project dependencies:

```bash
uv venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
uv pip install .
```

### 4. Configure Environment Variables

Syn-Thesis requires access to a Google Cloud LLM. You need to provide your Google API Key and the desired model name.

1.  **Create a `.env` file:** In the root directory of the `syn-thesis` project, create a file named `.env`.
2.  **Populate `.env`:** Open the `.env` file and add the following lines, replacing `"YOUR_GOOGLE_API_KEY"` and `"YOUR_GOOGLE_MODEL_NAME"` with your actual values:

    ```
    GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
    GOOGLE_MODEL_NAME="YOUR_GOOGLE_MODEL_NAME"
    ```

    You can refer to the `.env.example` file for the correct format.

    **Important:**
    *   **Security:** Never commit your `.env` file to version control. It has been added to `.gitignore` to prevent accidental commits.
    *   **API Key:** Obtain your Google API Key from the Google Cloud Console.
    *   **Model Name:** Choose a suitable model name (e.g., `gemini-pro`, `gemini-1.5-flash`).

## How to Use Syn-Thesis

Syn-Thesis is controlled via a command-line interface.

### Writing a Thesis Chapter

To initiate the writing process for a thesis chapter, use the `thesis` command with the `write a chapter` goal and specify your topic:

```bash
python3 main.py thesis "write a chapter" --topic "The impact of quantum computing on cryptography"
```

Replace `"The impact of quantum computing on cryptography"` with your desired thesis topic.

The system will then:
1.  Generate a plan for the chapter.
2.  Research relevant papers.
3.  Summarize the papers.
4.  Write an initial draft of the section.
5.  Get feedback from the Editor agent.
6.  Revise the section based on the feedback.
7.  Generate or update the `thesis.tex` file in the `output/tex/` directory.

### Continuing Work on an Existing Thesis

The system is designed to be persistent. If a `thesis.tex` file already exists in `output/tex/`, the `WriterAgent` will read its content and attempt to continue writing or revise sections based on the new instructions. This allows you to work on your thesis over multiple sessions.

### Future Enhancements

*   More granular control over agent workflows (e.g., specifying which sections to write, controlling the number of revision cycles).
*   Integration with academic databases for more robust research.
*   Support for different LaTeX document classes and styles.
*   Advanced citation management (e.g., automatic BibTeX generation from research results).
*   User interface for easier interaction and progress visualization.

Feel free to explore the codebase and contribute to its development!
