## Global imports 
from dash.dependencies import Input, Output, State


## Local imports
#
from app import app
from model.location_model import get_location_data
from view.polar_layouts import get_polar_plot_figure_from_x_y





@app.callback(
    Output(component_id='hist-example', component_property='figure'),
    [
        Input(component_id='submit-button', component_property='n_clicks')
    ],
    [
        State(component_id='start_point', component_property='value'),
        State(component_id='end_point', component_property='value'),
        State(component_id='hist-example', component_property='figure')
    ]
)
def update_polar_layout(n_clicks, start_point, end_point, current_output_state):
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
        output = current_output_state
    else:
        x, y = get_location_data(start_point, end_point)
        output = get_polar_plot_figure_from_x_y(x, y)
    return output