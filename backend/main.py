"""Phase 1 CLI entrypoint.

Loads .env, runs the ba -> dev graph on a hardcoded sample input, prints the
user stories, and writes generated files to ./output/.
"""

from __future__ import annotations

import json
from pathlib import Path

from dotenv import load_dotenv

from graph.orchestration import build_graph

OUTPUT_DIR = Path(__file__).parent / "output"

SAMPLE_INPUT = """
Scope: A command-line TODO app for a single user.
Actors: A user who manages personal tasks.
Steps: The user can add a task, list all tasks, mark a task as done, and delete a task.
Value: Helps the user keep track of what they need to do.
Assumptions: Tasks are stored in a local JSON file. No authentication needed.
"""

# SAMPLE_INPUT = """
# Scope: A REST API for a personal expense tracker.
# Actors: A registered user who records and reviews their spending.
# Steps: The user can create an expense (amount, category, date, note), list expenses filtered by category or date range, update an existing expense, delete an expense, and view a monthly total per category.
# Value: Lets the user understand where their money goes and stay within a budget.
# Assumptions: Data is stored in a SQLite database. Each user authenticates with a JWT token. Amounts are in a single currency (USD).
# """


def write_outputs(code_changes: dict[str, str]) -> None:
    for rel_path, content in code_changes.items():
        dest = OUTPUT_DIR / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")
        print(f"  wrote {dest.relative_to(Path(__file__).parent)}")


def main() -> None:
    load_dotenv()
    app = build_graph()

    initial_state = {"raw_input": SAMPLE_INPUT.strip()}
    final_state = app.invoke(initial_state)

    print("\n=== User Stories ===")
    print(json.dumps(final_state.get("user_stories", []), indent=2))

    print("\n=== Generated Files ===")
    write_outputs(final_state.get("code_changes", {}))

    print("\nDone.")


if __name__ == "__main__":
    main()
