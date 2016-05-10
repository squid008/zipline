"""
Utilities for working with pandas objects.
"""
import pandas as pd


def explode(df):
    """
    Take a DataFrame and return a triple of

    (df.index, df.columns, df.values)
    """
    return df.index, df.columns, df.values


try:
    # This branch is hit in pandas 17
    sort_values = pd.DataFrame.sort_values
    july_5th_holiday_observance = lambda dtix: dtix[dtix.year != 2013]
except AttributeError:
    # This branch is hit in pandas 16
    sort_values = pd.DataFrame.sort
    july_5th_holiday_observance = lambda dt: None if dt.year == 2013 else dt
