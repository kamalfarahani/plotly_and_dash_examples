import plotly.express as px


def main() -> None:
    iris_df = px.data.iris()

    iris_df["sepal_area"] = iris_df["sepal_width"] * iris_df["sepal_length"]
    iris_df["petal_area"] = iris_df["petal_width"] * iris_df["petal_length"]

    iris_df["area"] = iris_df["sepal_area"] + iris_df["petal_area"]

    fig = px.bar(
        iris_df,
        x="species",
        y="area",
        color="species",
        color_discrete_sequence=px.colors.qualitative.Vivid,
    )

    fig.show()


if __name__ == "__main__":
    main()
