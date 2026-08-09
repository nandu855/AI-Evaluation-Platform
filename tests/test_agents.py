from backend.agents.judge import Judge


judge = Judge()


def test_agents():

    result = judge.evaluate(

        question="Explain Deep Learning.",

        response="Deep Learning is a subset of Machine Learning using neural networks.",

        reference="Deep Learning is a subset of Machine Learning using neural networks.",

        retrieved_context="Deep Learning is a subset of Machine Learning using neural networks."

    )

    assert "relevance" in result

    assert "accuracy" in result

    assert "hallucination" in result

    assert "completeness" in result

    print("Judge Agents Test Passed")


if __name__ == "__main__":

    test_agents()