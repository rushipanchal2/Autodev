from autodev.pipeline.orchestrator import ProjectState, run_pipeline


def test_run_pipeline_returns_state():
    state = run_pipeline("Build a URL shortener")
    assert isinstance(state, ProjectState)
    assert state.idea == "Build a URL shortener"
