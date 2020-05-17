import dash_core_components as dcc
import dash_html_components as html

from app import app

def get_time_series_plot_figure_data(y, x=None, display_title=""):
    """ Return the figure data in dictionnary based on the parameters.

    Args:
        - y (list): The y values of the data to display.
        - x (list): The x values of the data to display. If the value is left
                at None, the x will be [1, 2, ..., n].
        - display_title (str): The title to display on the graph.

    Retruns:
        - figure_data (dict): The data to use for the displayed figure.
    """
    if not x:
        x = list(range(len(y)))
    figure_data = {
        'data': [
            {
                'x': x,
                'y': y,
                'mode': 'lines+markers',
                'marker': {'size': 12}
            },
        ],
        'layout': {
            'title': display_title,
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
        html.H1(children='Time series layout'),
        dcc.Graph(id='time-series-graph-1',
            figure=get_time_series_plot_figure_data([],
            display_title="x location over time")),
        dcc.Graph(id='time-series-graph-2',
            figure=get_time_series_plot_figure_data([],
            display_title="y location over time")),
        html.Div(dcc.Input(id='start-point-ts', type='number', value=0)),
        html.Div(dcc.Input(id='end-point-ts', type='number', value=100)),
        html.Button('Submit', id='submit-button-ts', n_clicks=0),
    ])
    return layout

