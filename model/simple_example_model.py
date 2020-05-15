import pandas as pd

def get_n_first_line_of_data(n):
    """ Return the n first line of the dataframe.

    Args:
        - n (int): the number of line to display.

    Returns:
        - x (list): The list of names.
        - y (list): The list of ages.
    """
    df = pd.read_csv('example.csv')
    df = df[:min(len(df), n)]
    x = list(df['Name'].values)
    y = list(df['Age'].values)
    return x, y