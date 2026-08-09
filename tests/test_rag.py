from backend.rag import retrieve_context


def test_rag():

    context = retrieve_context(

        "What is Artificial Intelligence?"

    )

    assert isinstance(context, str)

    assert len(context) > 0

    print("RAG Test Passed")


if __name__ == "__main__":

    test_rag()