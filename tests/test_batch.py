from backend.agents.judge import Judge


judge = Judge()


dataset = [

    {

        "question": "What is AI?",

        "answer": "Artificial Intelligence enables machines to simulate human intelligence."

    },

    {

        "question": "What is Machine Learning?",

        "answer": "Machine Learning enables systems to learn from data."

    }

]


def test_batch():

    results = []

    for item in dataset:

        result = judge.evaluate(

            question=item["question"],

            response=item["answer"],

            reference=item["answer"],

            retrieved_context=item["answer"]

        )

        results.append(result)

    assert len(results) == len(dataset)

    print("Batch Evaluation Test Passed")


if __name__ == "__main__":

    test_batch()