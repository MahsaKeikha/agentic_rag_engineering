def evaluate_grounding_gate(state, approve=False):
    blocked=bool(state.unresolved_questions or state.conflicts or state.risks)
    return "blocked" if blocked else ("approved_for_human_follow_through" if approve else "awaiting_human_approval")
