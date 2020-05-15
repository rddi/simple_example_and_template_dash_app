import dash_core_components as dcc
import dash_html_components as html

from app import app

def base_layout():
    """ Returns the basic layout of the app

    Returns:
        - layout (dash_html_components.html.Div): The layout content
    """
    layout = html.Div(children=[
        html.H1(children='Dash Tutorials'),
        dcc.Graph(id='hist-example',
            figure={
                'data': [
                    {
                        'x': [1, 2],
                        'y': [1, 2],
                        'type': 'bar',
                        'name': 'Ages'
                    },
                ],
                'layout': {
                    'title': 'Basic Dash Example'
                }
            }),
        html.Div(dcc.Input(id='input-on-submit', type='number')),
        html.Button('Submit', id='submit-button', n_clicks=0),
    ])
    return layout

def get_v2_layout():
    return html.Div([
        html.Button('Button 1', id='btn-nclicks-1', n_clicks=0),
        html.Button('Button 2', id='btn-nclicks-2', n_clicks=0),
        html.Button('Button 3', id='btn-nclicks-3', n_clicks=0),
        html.Div(id='container-button-timestamp')
    ])