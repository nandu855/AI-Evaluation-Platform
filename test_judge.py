from backend.agents.judge import Judge

judge = Judge()

result = judge.evaluate(

    question="When did Beyonce become famous?",

    response="Beyonce became famous in the late 1990s as the lead singer of Destiny's Child.",

    reference="She became famous in the late 1990s.",

    retrieved_context="Beyonce rose to fame during the late 1990s as the lead singer of Destiny's Child."

)

print(result)