import dash_bootstrap_components as dbc


def get_navbar():
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Polar layout", href="/polar")),
            dbc.NavItem(dbc.NavLink("Time series layout", href="/timeseries")),
        ])