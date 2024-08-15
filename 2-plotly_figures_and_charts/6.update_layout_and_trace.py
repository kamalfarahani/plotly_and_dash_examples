import plotly.express as px


def main() -> None:
    df = px.data.iris()

    df = (
        df[["sepal_length", "petal_length"]]
        .groupby("petal_length", as_index=False)
        .mean()
    )

    fig = px.line(
        df,
        x="petal_length",
        y="sepal_length",
        title="Iris",
    )

    fig.update_layout(
        title="Iris",
        xaxis_title="Petal Length",
        yaxis_title="Sepal Length",
    )

    fig.update_traces(
        mode="markers+lines",
        opacity=0.5,
    )

    fig.show()


if __name__ == "__main__":
    main()
