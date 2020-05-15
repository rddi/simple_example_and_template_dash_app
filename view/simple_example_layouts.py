import dash_core_components as dcc
import dash_html_components as html

from app import app

def base_layout():
    """ Returns the basic layout of the app

    Returns:
        - layout (dash_html_components.html.Div): The layout content
    """
    layout = html.Div(children=[
        html.H1(children='Dash Simple dashboard example'),
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

def get_other_view_layout():
    return html.Div([
        html.H3('This is an alternative view')
    ])