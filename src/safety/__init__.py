def grounded_release_allowed(result):return result.get("status")=="approved_for_human_follow_through" and not result.get("risks") and not result.get("unresolved_questions")
