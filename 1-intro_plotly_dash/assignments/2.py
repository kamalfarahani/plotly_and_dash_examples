import pandas as pd
import plotly.express as px

from dash import Dash, html, dcc
from dash.dependencies import Input, Output


gdp_df = pd.read_csv("./data/gdp.csv")
countries = gdp_df["Country Name"].unique()

app = Dash(__name__)
app.layout = html.Div(
    [
        html.P("Select Country", style={"font-weight": "bold"}),
        dcc.Dropdown(
            id="dropdown",
            options=[{"label": country, "value": country} for country in countries],
            value=countries[0],
            style={"width": 500},
        ),
        dcc.Graph(id="graph"),
    ]
)


@app.callback(
    Output("graph", "figure"),
    [Input("dropdown", "value")],
)
def update_graph(country):
    years = gdp_df.columns[2:]
    gdps = gdp_df[gdp_df["Country Name"] == country].iloc[0].values[2:]

    df = pd.DataFrame(
        {
            "Year": years,
            "GDP": gdps,
        }
    )

    fig = px.line(
        df,
        x="Year",
        y="GDP",
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
