import pandas as pd
import plotly.express as px


def load_data() -> pd.DataFrame:
    df = pd.read_csv("./data/fast_foods.csv")

    return df


def main():
    df = load_data()

    fig = px.scatter_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        hover_name="address",
        zoom=3,
        center={
            "lat": 37.0902,
            "lon": -95.7129,
        },
        title="Fast Food in the United States",
        mapbox_style="open-street-map",  # This should be specified
    )

    fig.show()


if __name__ == "__main__":
    main()
