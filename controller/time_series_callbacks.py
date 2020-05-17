from dash.dependencies import Input, Output, State

from app import app
from model.location_model import get_location_data
from view.time_series_layouts import get_time_series_plot_figure_data

@app.callback(
    [
        Output(component_id='time-series-graph-1', component_property='figure'),
        Output(component_id='time-series-graph-2', component_property='figure')
    ],
    [
        Input(component_id='submit-button-ts', component_property='n_clicks')
    ],
    [
        State(component_id='start-point-ts', component_property='value'),
        State(component_id='end-point-ts', component_property='value'),
        State(component_id='time-series-graph-1', component_property='figure'),
        State(component_id='time-series-graph-2', component_property='figure')
    ]
)
def update_time_series_layout(n_clicks, start_point, end_point,
        current_output_1_state, current_output_2_state):
    """ Update the two time series plot when the submit button is clicked.

    Args:
        - n_clicks (int): The number of time the sumit button has been clicked.
        - start_point (int): The input of the view corresponding to first point
            index to display.
        - end_point (int): The input of the view corresponding to last point
            index to display.
        - current_output_1_state (dict): The current data in the figure 1.
        - current_output_2_state (dict): The current data in the figure 2.

    Returns:
        - output_1 (dict): The new data to display in figure 1.
        - output_2 (dict): The new data to display in figure 2.
    """
    if n_clicks == 0: # The clicks is call for the number zero
        output_1 = current_output_1_state
        output_2 = current_output_2_state
    else:
        x, y = get_location_data(start_point, end_point)
        output_1 = get_time_series_plot_figure_data(x)
        output_2 = get_time_series_plot_figure_data(y)
    return [output_1, output_2]