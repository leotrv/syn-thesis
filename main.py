import argparse

def main():
    parser = argparse.ArgumentParser(description="Syn-Thesis: A multi-agent system for thesis writing.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Thesis commands
    thesis_parser = subparsers.add_parser("thesis", help="Manage your master thesis with the multi-agent system")
    thesis_parser.add_argument("goal", type=str, help="The high-level goal for your thesis (e.g., 'write a chapter', 'research a topic')")
    thesis_parser.add_argument("--topic", type=str, help="The specific topic for the goal")

    args = parser.parse_args()

    if args.command == "thesis":
        from src.agents.orchestrator.agent import Orchestrator

        orchestrator = Orchestrator()
        orchestrator.handle_thesis_command(args.goal, args.topic)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()