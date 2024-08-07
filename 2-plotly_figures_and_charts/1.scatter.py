import numpy as np
import pandas as pd
import plotly.express as px


def load_data() -> pd.DataFrame:
    stocks_df = px.data.stocks()

    goog = stocks_df[["date", "GOOG"]]
    aapl = stocks_df[["date", "AAPL"]]
    amzn = stocks_df[["date", "FB"]]
    nflx = stocks_df[["date", "NFLX"]]
    msft = stocks_df[["date", "MSFT"]]

    goog["type"] = "GOOG"
    aapl["type"] = "AAPL"
    amzn["type"] = "AMZN"
    nflx["type"] = "NFLX"
    msft["type"] = "MSFT"

    all_data = np.vstack(
        (
            goog.values,
            aapl.values,
            amzn.values,
            nflx.values,
            msft.values,
        )
    )

    data = pd.DataFrame(
        all_data,
        columns=["date", "value", "type"],
    )
    data["date"] = pd.to_datetime(data["date"])

    return data


def main() -> None:
    data_df = load_data()
    fig = px.scatter(
        data_df,
        x="date",
        y="value",
        color="type",
        trendline="ols",
        # animation_frame="type",
    )

    fig.show()


if __name__ == "__main__":
    main()
