import pandas as pd

def get_location_data(start_point, end_point):
    """ Return the n first line of the dataframe.

    Args:
        - start_point (int): the first line of the data to display.
        - end_point (int): the last line of the data to display.

    Returns:
        - x (list): The list of x coordinates.
        - y (list): The list of y coordinates.
    """
    df = pd.read_csv('location.csv')
    df = df[max(0, start_point) : min(len(df), end_point)]
    x = list(df['x'].values)
    y = list(df['y'].values)
    return x, y
