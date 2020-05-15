from app import app

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import controller
from view.simple_example_layouts import base_layout, get_other_view_layout

# setup_base_layout(app)
app.layout = html.Div([
    dcc.Link('Navigate to "/base"', href='/base'),
    dcc.Link('Navigate to "/other_view"', href='/other_view'),
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
    if pathname == "/base":
        return base_layout()
    elif pathname == "/other_view":
        return get_other_view_layout()
    else:
        return current_content




if __name__ == '__main__':
    app.run_server(
        debug=True,
        host='0.0.0.0',
        port=8050
    )
