from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate


app = Dash(__name__)

app.layout = html.Div(
    [
        html.P(
            "Select the State",
            style={
                "font-weight": "bold",
            },
        ),
        dcc.Dropdown(
            id="dropdown",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montreal", "value": "MTL"},
                {"label": "San Francisco", "value": "SF"},
            ],
            value="MTL",
        ),
        html.P(
            "Selected State: ",
            id="selected-state",
            style={"font-weight": "bold"},
        ),
    ]
)


@app.callback(
    Output("selected-state", "children"),
    [Input("dropdown", "value")],
)
def display_selected_state(state):
    if state is None:
        raise PreventUpdate
    return f"Selected State: {state}"


if __name__ == "__main__":
    app.run(debug=True)
