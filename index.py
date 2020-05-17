from app import app

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import controller
from view.polar_layouts import get_polar_layout
from view.time_series_layouts import get_time_series_layout
from view.header import get_navbar

# setup_base_layout(app)
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
    if pathname == "/polar":
        return get_polar_layout()
    elif pathname == "/timeseries":
        return get_time_series_layout()
    else:
        return current_content




if __name__ == '__main__':
    app.run_server(
        debug=True,
        host='0.0.0.0',
        port=8050
    )
