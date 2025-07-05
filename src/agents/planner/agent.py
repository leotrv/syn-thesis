

class Planner:
    def __init__(self):
        pass

    def create_plan(self, topic: str) -> str:
        print(f"Planner received topic: {topic}")
        # In the future, this will use an LLM to generate a detailed plan.
        plan = (
            "1. Introduction\n"
            "   1.1. Hook\n"
            "   1.2. Thesis Statement\n"
            "2. Literature Review\n"
            "   2.1. Historical Context\n"
            "   2.2. Key Theories\n"
            "3. Methodology\n"
            "4. Results\n"
            "5. Discussion\n"
            "6. Conclusion\n"
        )
        return plan

