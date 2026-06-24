"""LangGraph wiring for Phase 1: ENTRY -> ba -> dev -> END."""

from __future__ import annotations

from langgraph.graph import END, START, StateGraph

from .agents.ba_agent import ba_agent
from .agents.dev_agent import dev_agent
from .state import SDLCState


def build_graph():
    """Compile and return the Phase 1 SDLC graph."""
    graph = StateGraph(SDLCState)

    graph.add_node("ba", ba_agent)
    graph.add_node("dev", dev_agent)

    graph.add_edge(START, "ba")
    graph.add_edge("ba", "dev")
    graph.add_edge("dev", END)

    return graph.compile()
