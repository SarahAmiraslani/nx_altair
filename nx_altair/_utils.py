import numpy as np
import pandas as pd

def is_arraylike(obj):
    """Return True if array-like (accepts lists, pandas.Series
    pandas.DataFrame, numpy.ndarray).
    """
    return isinstance(obj, (list, np.ndarray, pd.Series, pd.DataFrame))


def despine(chart):
    """Despine altair chart.
    """
    chart = chart.configure_axis(
        ticks=False,
        grid=False,
        domain=False,
        labels=False)
    return chart
