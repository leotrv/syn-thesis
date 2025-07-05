import argparse

def main():
    parser = argparse.ArgumentParser(description="Syn-Thesis: A multi-agent system for thesis writing.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Orchestrator commands
    orchestrator_parser = subparsers.add_parser("orchestrator", help="Interact with the orchestrator agent")
    orchestrator_parser.add_argument("task", type=str, help="The high-level task for the orchestrator")

    args = parser.parse_args()

    if args.command == "orchestrator":
        from src.agents.orchestrator.agent import Orchestrator

        orchestrator = Orchestrator()
        orchestrator.execute_task(args.task)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()