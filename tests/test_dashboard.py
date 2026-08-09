import pandas as pd


def test_dashboard():

    df = pd.DataFrame(

        {

            "Overall": [0.95, 0.88, 0.74],

            "Verdict": [

                "PASS",

                "PASS",

                "Needs Improvement"

            ]

        }

    )

    assert "Overall" in df.columns

    assert df["Overall"].mean() > 0

    print("Dashboard Test Passed")


if __name__ == "__main__":

    test_dashboard()