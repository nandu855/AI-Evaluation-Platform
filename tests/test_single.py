from backend.agents.judge import Judge


judge = Judge()


def test_single_evaluation():

    result = judge.evaluate(

        question="What is Artificial Intelligence?",

        response="Artificial Intelligence is the simulation of human intelligence by machines.",

        reference="Artificial Intelligence is the simulation of human intelligence by machines.",

        retrieved_context="Artificial Intelligence is the simulation of human intelligence by machines."

    )

    assert result["overall_score"] >= 0

    assert "verdict" in result

    print("Single Evaluation Test Passed")


if __name__ == "__main__":

    test_single_evaluation()