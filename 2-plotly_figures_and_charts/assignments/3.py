import pandas as pd
import plotly.express as px


def load_data() -> pd.DataFrame:
    df = pd.read_csv("./data/ski.csv")

    return df


def main() -> None:
    df = load_data()

    fig_1 = px.scatter(
        df,
        x="TotalLifts",
        y="LiftCapacity",
        color="Country",
        size="GondolaLifts",
    )

    fig_1.show()

    highest_lift_capacity = df.loc[df["LiftCapacity"].argmax()]
    data = [
        highest_lift_capacity["SurfaceLifts"],
        highest_lift_capacity["ChairLifts"],
        highest_lift_capacity["GondolaLifts"],
    ]

    fig_2 = px.pie(
        values=data,
        names=[
            "Surface",
            "Chair",
            "Gondola",
        ],
        hole=0.8,
    )

    fig_2.show()


if __name__ == "__main__":
    main()
