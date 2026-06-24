"""POST /run-sdlc route — Phase 4.

Receives { raw_input }, streams LangGraph node progress via SSE,
returns final SDLCState as JSON.
"""

# TODO Phase 4: implement
#   - FastAPI APIRouter
#   - POST /run-sdlc  → builds SDLCState, calls app.stream(state)
#   - SSE events: "BA done", "Dev done", "QE done", "Retry N/max", "Final"
