## Global imports 
from dash.dependencies import Input, Output, State


## Local imports
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
def update_polar_layout(n_clicks, start_point, end_point,
        current_output_1_state, current_output_2_state):
    """A simple example of a call bakc function. Update the histograme based on
    the input recovered from the view with id input-on-submit and the data 
    recover via the model function get_n_first_line_of_data.

    Args:
        - n_clicks (int): The sumit button.
        - start_point (int): The input of the view corresponding to first point
            index to display.
        - end_point (int): The input of the view corresponding to last point
            index to display.
        - current_output_state (dict): The current data in the figure.

    Returns:
        - output (dict): The new data to display
    """
    if n_clicks == 0: # The clicks is call for the number zero
        output_1 = current_output_1_state
        output_2 = current_output_2_state
    else:
        x, y = get_location_data(start_point, end_point)
        output_1 = get_time_series_plot_figure_data(x)
        output_2 = get_time_series_plot_figure_data(y)
    return [output_1, output_2]