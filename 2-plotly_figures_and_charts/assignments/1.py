import numpy as np
import pandas as pd
import plotly.express as px


def main() -> None:
    iris_df = px.data.iris()

    iris_df["sepal_area"] = iris_df["sepal_width"] * iris_df["sepal_length"]
    iris_df["petal_area"] = iris_df["petal_width"] * iris_df["petal_length"]

    fig = px.scatter(
        iris_df,
        x="sepal_area",
        y="petal_area",
        color="species",
        trendline="ols",
    )

    fig.update_layout(
        title="Iris",
        xaxis_title="Sepal Area",
        yaxis_title="Petal Area",
    )

    fig.show()


if __name__ == "__main__":
    main()
