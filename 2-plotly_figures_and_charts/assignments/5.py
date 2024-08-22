import pandas as pd
import plotly.express as px


def load_data() -> pd.DataFrame:
    df = pd.read_csv("./data/ski.csv")

    return df


def main() -> None:
    df = load_data()

    lift_by_country = (
        df[["Country", "LiftCapacity"]].groupby("Country", as_index=False).sum()
    )

    fig = px.choropleth(
        lift_by_country,
        locations="Country",
        locationmode="country names",
        color="LiftCapacity",
        hover_name="Country",
        hover_data=["LiftCapacity"],
        color_continuous_scale=px.colors.sequential.Plasma,
        title="Total Lift Capacity by Country",
        scope="europe",
    )

    fig.show()


if __name__ == "__main__":
    main()
