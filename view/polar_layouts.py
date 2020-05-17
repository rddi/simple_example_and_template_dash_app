import dash_core_components as dcc
import dash_html_components as html

from app import app

def get_polar_plot_figure_from_x_y(x, y):
    """ Return the figure data in dictionnary based on the parameters.

    Args:
        - y (list): The y values of the data to display.
        - x (list): The x values of the data to display. If the value is left
                at None, the x will be [1, 2, ..., n].

    Retruns:
        - figure_data (dict): The data to use for the displayed figure.
    """
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
        dcc.Graph(id='polar-graph',
            figure=get_polar_plot_figure_from_x_y([], [])),
        html.Div(dcc.Input(id='start-point-pol', type='number', value=0)),
        html.Div(dcc.Input(id='end-point-pol', type='number', value=100)),
        html.Button('Submit', id='submit-button-pol', n_clicks=0),
    ])
    return layout

