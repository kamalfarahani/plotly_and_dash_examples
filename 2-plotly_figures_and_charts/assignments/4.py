import pandas as pd
import plotly.express as px


def load_data() -> pd.DataFrame:
    df = pd.read_csv("./data/ski.csv")

    return df


def main() -> None:
    df = load_data()

    lift_type_by_country = (
        df.groupby("Country", as_index=False)
        .agg(
            {
                "SurfaceLifts": "sum",
                "ChairLifts": "sum",
                "GondolaLifts": "sum",
                "TotalLifts": "sum",
            }
        )
        .sort_values(by="TotalLifts", ascending=False)
    )

    fig = px.bar(
        lift_type_by_country,
        x="Country",
        y="TotalLifts",
        color="Country",
    )

    fig.update_layout(
        title={
            "text": "Total Lifts by Country",
            "font": {
                "size": 24,
                "color": "green",
            },
        },
        xaxis_title="Country",
        yaxis_title="Total Lifts",
    )

    # add horizontal line
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor="black",
    )

    fig.show()


if __name__ == "__main__":
    main()
