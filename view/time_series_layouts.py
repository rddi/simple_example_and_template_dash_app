import dash_core_components as dcc
import dash_html_components as html

from app import app

def get_time_series_plot_figure_data(y, x=None):
    if not x:
        x = list(range(len(y)))
    figure_data = {
        'data': [
            {
                'x': x,
                'y': y,
                'mode': '+markers',
                'marker': {'size': 12},
                'name': 'Ages'
            },
        ],
        'layout': {
            'title': 'Time series display',
            'height': 500,
            'width': 1000,
            'yaxis': {'range': [-7, 7]},
        }
    }
    return figure_data

def get_time_series_layout():
    """ Returns the basic layout of the app

    Returns:
        - layout (dash_html_components.html.Div): The layout content
    """
    layout = html.Div(children=[
        html.H1(children='Polar layout'),
        dcc.Graph(id='time-series-graph-1',
            figure=get_time_series_plot_figure_data([])),
        dcc.Graph(id='time-series-graph-2',
            figure=get_time_series_plot_figure_data([])),
        html.Div(dcc.Input(id='start-point-ts', type='number', value=0)),
        html.Div(dcc.Input(id='end-point-ts', type='number', value=100)),
        html.Button('Submit', id='submit-button-ts', n_clicks=0),
    ])
    return layout