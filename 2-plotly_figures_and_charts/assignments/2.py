import pandas as pd
import plotly.express as px


def load_data() -> pd.DataFrame:
    df = pd.read_csv("./data/ski.csv")

    return df


def main() -> None:
    df = load_data()
    df_grouped_1 = df.groupby("Country", as_index=False).sum()
    fig_1 = px.bar(
        df_grouped_1,
        x="Country",
        y="TotalLifts",
        color="Country",
    )
    fig_1.show()

    df_grouped_2 = (
        df[["Country", "SurfaceLifts", "ChairLifts", "GondolaLifts"]]
        .groupby("Country", as_index=False)
        .sum()
    )
    fig_2 = px.bar(
        df_grouped_2,
        x="Country",
        y=["SurfaceLifts", "ChairLifts", "GondolaLifts"],
    )
    fig_2.show()


if __name__ == "__main__":
    main()
