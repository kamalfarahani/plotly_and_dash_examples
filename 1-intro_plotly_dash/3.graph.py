import plotly.express as px

from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate


app = Dash(__name__)
app.layout = html.Div(
    [
        html.P("Select dataset", style={"font-weight": "bold"}),
        dcc.Dropdown(
            id="dropdown",
            options=[
                {"label": "Iris", "value": "iris"},
                {"label": "Car", "value": "car"},
            ],
            value="iris",
            style={"width": 200},
        ),
        dcc.Graph(id="graph"),
    ]
)


@app.callback(
    Output("graph", "figure"),
    [Input("dropdown", "value")],
)
def update_graph(dataset):
    if dataset is None:
        raise PreventUpdate
    if dataset == "iris":
        df = px.data.iris()
        fig = px.scatter(
            df,
            x="sepal_width",
            y="sepal_length",
            color="species",
        )
    elif dataset == "car":
        df = px.data.carshare()
        fig = px.scatter_mapbox(
            df,
            lat="centroid_lat",
            lon="centroid_lon",
            color="peak_hour",
            zoom=10,
            mapbox_style="carto-positron",
        )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
