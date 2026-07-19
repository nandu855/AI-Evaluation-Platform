from backend.agents.relevance_agent import RelevanceJudge

judge = RelevanceJudge()

result = judge.evaluate(
    question="When did Beyonce become famous?",
    response="Beyonce became famous in the late 1990s as the lead singer of Destiny's Child."
)

print(result)