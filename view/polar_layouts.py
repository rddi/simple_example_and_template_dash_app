import dash_core_components as dcc
import dash_html_components as html

from app import app

def get_polar_plot_figure_from_x_y(x, y):
    figure_data = {
        'data': [
            {
                'x': x,
                'y': y,
                'mode': 'markers',
                'marker': {'size': 12},
                'name': 'Ages'
            },
        ],
        'layout': {
            'title': 'Polar layout',
            'height': 1000,
            'width': 1000,
            'xaxis': {'range': [-7, 7]},
            'yaxis': {'range': [-7, 7]},
        }
    }
    return figure_data

def get_polar_layout():
    """ Returns the basic layout of the app

    Returns:
        - layout (dash_html_components.html.Div): The layout content
    """
    layout = html.Div(children=[
        html.H1(children='Polar layout'),
        dcc.Graph(id='hist-example',
            figure=get_polar_plot_figure_from_x_y([], [])),
        html.Div(dcc.Input(id='start_point', type='number', value=0)),
        html.Div(dcc.Input(id='end_point', type='number', value=100)),
        html.Button('Submit', id='submit-button', n_clicks=0),
    ])
    return layout

def get_other_view_layout():
    return html.Div([
        html.H3('This is an alternative view')
    ])