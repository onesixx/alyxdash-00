# alyxdash/utils.py
import pandas as pd


def formatter_2_decimals(x):
    return "{:.2f}".format(x)


def rleid(seq):
    char = "sixx"
    group = 0
    result = []
    for i in range(0, len(seq)):
        if seq[i] == char:
            result.append(group)
        else:
            group = group + 1
            result.append(group)
            char = seq[i]
    return result


def make_pdata_undup(df, col):
    pdata = df[~(pd.Series(rleid(df[col])).duplicated(keep='first')) |
               ~(pd.Series(rleid(df[col])).duplicated(keep='last'))]
    return pdata


def clean_data(data):
    """
    A function to clean data before processing.
    """
    # implementation code here
    cleaned_data = ...
    return cleaned_data


def validate_input(input):
    """
    A function to validate user input.
    """
    # implementation code here
    valid_input = ...
    return valid_input


def format_output(output):
    """
    A function to format the output of a process or calculation.
    """
    # implementation code here
    formatted_output = ...
    return formatted_output
