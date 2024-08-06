from dash import Dash, html, dcc
from dash.dependencies import Input, Output


app = Dash(__name__)

default_color = "blue"

app.layout = html.Div(
    [
        html.P(
            "Color: ",
            style={"font-weight": "bold"},
        ),
        dcc.Dropdown(
            options=[
                {"label": "Red", "value": "red"},
                {"label": "Green", "value": "green"},
                {"label": "Blue", "value": "blue"},
            ],
            value=default_color,
            id="color-dropdown",
            style={"width": 200},
        ),
        html.P(
            f"Selected color: {default_color}",
            style={
                "font-weight": "bold",
                "color": default_color,
            },
            id="selected-color",
        ),
    ],
)


@app.callback(
    Output("selected-color", "children"),
    [Input("color-dropdown", "value")],
)
def display_selected_color(color):
    return f"Selected color: {color}"


@app.callback(
    Output("selected-color", "style"),
    [Input("color-dropdown", "value")],
)
def display_selected_color(color):
    return {
        "font-weight": "bold",
        "color": color,
    }


if __name__ == "__main__":
    app.run(debug=True)
