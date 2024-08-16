import pandas as pd
import plotly.express as px


def load_data() -> pd.DataFrame:
    df = pd.read_csv("./data/gdp.csv")

    return df


def main() -> None:
    df = load_data()

    fig = px.choropleth(
        df,
        locations="Country Code",
        color="2020",
        hover_name="Country Name",
        title="2020 GDP by Country",
        locationmode="ISO-3",
        color_continuous_scale=px.colors.sequential.Plasma,
        range_color=(0, 30 * 1e12),
    )

    fig.update_layout(
        coloraxis_colorbar=dict(
            title="GDP",
        )
    )

    fig.show()


if __name__ == "__main__":
    main()
