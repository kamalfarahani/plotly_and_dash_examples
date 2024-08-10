import plotly.express as px


def main() -> None:
    df = px.data.iris()
    df = df.groupby("species", as_index=False).mean()

    fig_1 = px.pie(
        df,
        values="sepal_width",
        names="species",
        color="species",
        color_discrete_map={
            "setosa": "red",
            "versicolor": "green",
            "virginica": "blue",
        },
    )

    # Donut
    fig_2 = px.pie(
        df,
        values="sepal_width",
        names="species",
        color="species",
        color_discrete_map={
            "setosa": "red",
            "versicolor": "green",
            "virginica": "blue",
        },
        hole=0.5,
    )

    fig_1.show()
    fig_2.show()


if __name__ == "__main__":
    main()
