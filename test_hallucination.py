from backend.agents.hallucination_agent import HallucinationJudge

judge = HallucinationJudge()

result = judge.evaluate(
    response="""
    Beyonce became famous in the late 1990s as the lead singer of Destiny's Child.
    She won an Oscar in 2001.
    """,
    retrieved_context="""
    Beyonce rose to fame during the late 1990s as the lead singer of Destiny's Child.
    """
)

print(result)