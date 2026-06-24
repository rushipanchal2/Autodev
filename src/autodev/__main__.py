"""CLI entry point: `python -m autodev "<product idea>"`."""

import sys

from autodev.pipeline.orchestrator import run_pipeline


def main() -> int:
    if len(sys.argv) < 2:
        print('Usage: python -m autodev "<product idea>"')
        return 1
    idea = " ".join(sys.argv[1:])
    run_pipeline(idea)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
