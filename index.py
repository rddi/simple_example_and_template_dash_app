import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app

import controller
from view.polar_layouts import get_polar_layout
from view.time_series_layouts import get_time_series_layout
from view.header import get_navbar

app.layout = html.Div([
    get_navbar(),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Change the page depending on the url
@app.callback(Output('page-content', 'children'),
              [
                  Input('url', 'pathname')
              ],
              [
                  State('page-content', 'children')
              ])
def display_page(pathname, current_content):
    """ Return the page content based on the url get in paramter.
    
    Args:
        - pathname (str): The requested url the page content returned is based
            on.
        - current_content (dash component): The current dashboard contant in
            case the url is not valide.

    Returns:
        - page_content (dash component): The page content.
    """
    if pathname == "/polar":
        page_content = get_polar_layout()
    elif pathname == "/timeseries":
        page_content = get_time_series_layout()
    else:
        page_content = current_content
    return page_content

if __name__ == '__main__':
    app.run_server(
        debug=True,
        host='0.0.0.0',
        port=8050
    )

