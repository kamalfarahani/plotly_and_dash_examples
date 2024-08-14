import plotly.express as px


def main() -> None:
    df = px.data.iris()
    fig = px.histogram(
        df,
        x="sepal_width",
        title="Sepal Width",
        nbins=20,
        histnorm="percent",
    )
    fig.show()


if __name__ == "__main__":
    main()
