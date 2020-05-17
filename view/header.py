import dash_bootstrap_components as dbc

def get_navbar():
    """ Return the header of the main page.

    Returns:
        - header_dash_component (dash component): The header of the page.
    """
    header_dash_component = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Polar layout", href="/polar")),
            dbc.NavItem(dbc.NavLink("Time series layout", href="/timeseries")),
        ]
    )
    return header_dash_component

