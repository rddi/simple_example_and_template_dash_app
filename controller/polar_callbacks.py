from dash.dependencies import Input, Output, State

from app import app
from model.location_model import get_location_data
from view.polar_layouts import get_polar_plot_figure_from_x_y

@app.callback(
    Output(component_id='polar-graph', component_property='figure'),
    [
        Input(component_id='submit-button-pol', component_property='n_clicks')
    ],
    [
        State(component_id='start-point-pol', component_property='value'),
        State(component_id='end-point-pol', component_property='value'),
        State(component_id='polar-graph', component_property='figure')
    ]
)
def update_polar_layout(n_clicks, start_point, end_point, current_output_state):
    """ Update the polar plot when the submit button is clicked.

    Args:
        - n_clicks (int): The number of time the sumit button has been clicked.
        - start_point (int): The input of the view corresponding to first point
            index to display.
        - end_point (int): The input of the view corresponding to last point
            index to display.
        - current_output_state (dict): The current data in the figure.

    Returns:
        - output (dict): The new data to display in figure.
    """
    if n_clicks == 0: # The clicks is call for the number zero
        output = current_output_state
    else:
        x, y = get_location_data(start_point, end_point)
        output = get_polar_plot_figure_from_x_y(x, y)
    return output

