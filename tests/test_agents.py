from src.agents import AGENT_MANIFEST, build_agents


def test_agent_team_is_explicit_and_specialized():
    agents = build_agents()
    assert len(agents) == 5
    assert len({a.name for a in agents}) == 5
    assert all(a.responsibility for a in agents)
    assert len(AGENT_MANIFEST) == 5


def test_agent_names_are_stable():
    assert [a.name for a in build_agents()] == [
        "ingestion", "retrieval", "context_reranking", "grounding_citation", "evaluation"
    ]
