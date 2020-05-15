## Global imports 
from dash.dependencies import Input, Output, State


## Local imports
#
from app import app
from model.simple_example_model import get_n_first_line_of_data





@app.callback(
    Output(component_id='hist-example', component_property='figure'),
    [
        Input(component_id='submit-button', component_property='n_clicks')
    ],
    [
        State(component_id='input-on-submit', component_property='value'),
        State(component_id='hist-example', component_property='figure')
    ]
)
def ctrl_func(n_clicks, n, current_output_state):
    """A simple example of a call bakc function. Update the histograme based on
    the input recovered from the view with id input-on-submit and the data 
    recover via the model function get_n_first_line_of_data.

    Args:
        - n_clicks (int): The sumit button.
        - n (int): The input of the view corresponding to the number of bars
            to display.
        - current_output_state (dict): The current data in the figure.

    Returns:
        - output (dict): The new data to display
    """
    if n_clicks == 0: # The clicks is call for the number zero
        output = current_output_state
    else:
        x, y = get_n_first_line_of_data(n)
        output = {
                'data': [
                    {
                        'x': x,
                        'y': y,
                        'type': 'bar',
                        'name': 'Ages'
                    },
                ],
                'layout': {
                    'title': 'Basic Dash Example'
                }
            }
    return output