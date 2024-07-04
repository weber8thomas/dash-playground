import dash
from dash_iconify import DashIconify

from dash import html, Output, Input, State, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

import plotly.express as px

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])



def create_nav_link(label, href):
    return dmc.NavLink(
        label=label,
        href=href,
        style={"display": "inline-block"},
    )


data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x="year", y="pop")


app.layout = dmc.MantineProvider(
    children=[
        dmc.Container(
            [
                dmc.Navbar(
                    p="md",
                    fixed=False,
                    width={"base": 300},
                    hidden=True,
                    hiddenBreakpoint="md",
                    position="right",
                    height="100vh",
                    id="sidebar",
                    children=[
                        html.Div(
                            [
                                dmc.NavLink(
                                    label="HOME",
                                    icon=DashIconify(icon="ant-design:home-filled", width=20),
                                    href="/",
                                ),
                            ],
                            style={"white-space": "nowrap"},
                        )
                    ],
                    style={
                        "overflow": "hidden",
                        "transition": "width 0.3s ease-in-out",
                    },
                ),
                dmc.Drawer(
                    title="Company Name",
                    id="drawer-simple",
                    padding="md",
                    zIndex=10000,
                    size=300,
                    overlayOpacity=0.1,
                    children=[],
                ),
                dmc.Container(
                    [
                        dmc.Header(
                            height=60,
                            children=[
                                dmc.Group(
                                    [
                                        dmc.MediaQuery(
                                            [
                                                dmc.Button(
                                                    DashIconify(
                                                        icon="ci:hamburger-lg",
                                                        width=24,
                                                        height=24,
                                                        color="#c2c7d0",
                                                    ),
                                                    variant="subtle",
                                                    p=1,
                                                    id="sidebar-button",
                                                )
                                            ],
                                            smallerThan="md",
                                            styles={"display": "none"},
                                        ),
                                        dmc.MediaQuery(
                                            [
                                                dmc.Button(
                                                    DashIconify(
                                                        icon="ci:hamburger-lg",
                                                        width=24,
                                                        height=24,
                                                        color="#c2c7d0",
                                                    ),
                                                    variant="subtle",
                                                    p=1,
                                                    id="drawer-demo-button",
                                                )
                                            ],
                                            largerThan="md",
                                            styles={"display": "none"},
                                        ),
                                        # dmc.Text("Company Name"),
                                    ]
                                )
                            ],
                            p="10px",
                            style={"backgroundColor": "#fff"},
                        ),
                        dmc.Container(
                            [
                                html.Div(dbc.Container(dcc.Graph(figure=fig), fluid=True)),
                            ],
                            # id="page-container",
                            # p=0,
                            # fluid=True,
                            # style={"background-color": "#f4f6f9", "width": "100%", "margin": "0", "maxWidth": "100%", "overflow": "auto", "flexShrink": "1", "maxHeight": "100%"},
                        ),
                    ],
                    # size="100%",
                    # p=0,
                    # m=0,
                    # style={"display": "flex", "maxWidth": "100vw", "overflow": "hidden", "flexGrow": "1", "maxHeight": "100%", "flexDirection": "column"},
                    # id="content-container",
                ),
            ],
            size="100%",
            p=0,
            m=0,
            style={"display": "flex", "maxWidth": "100vw", "overflow": "hidden", "maxHeight": "100vh", "position": "absolute", "top": 0, "left": 0, "width": "100vw"},
            id="overall-container",
        ),
    ],
)


@app.callback(
    Output("sidebar", "width"),
    Input("sidebar-button", "n_clicks"),
    State("sidebar", "width"),
    prevent_initial_call=True,
)
def drawer_demo(n, width):
    if n:
        if width["base"] == 300:
            return {"base": 70}
        else:
            return {"base": 300}
    else:
        raise dash.exceptions.PreventUpdate


@app.callback(
    Output("drawer-simple", "opened"),
    Input("drawer-demo-button", "n_clicks"),
    prevent_initial_call=True,
)
def drawer_dem(n_clicks):
    return True


if __name__ == "__main__":
    app.run_server(debug=True)
