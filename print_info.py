# original source:
#https://stackoverflow.com/questions/43976830/pandas-info-to-html
import pandas as pd
from io import StringIO

def print_info(df: pd.DataFrame):
    stream = StringIO()
    df.info(buf=stream)
    str = stream.getvalue()

    # split the output of info() by newline char
    lines = str.split("\n")

    #create a table from the text omitting first 5 and last 3 
    # to only capture the table data
    table = StringIO("\n".join(lines[5:-3])) 
        
    datatypes = pd.read_table(table, delim_whitespace=True, 
                   names=["column", "count", "value_type", "dtype"])
    datatypes.set_index("column", inplace=True)

    # create the info string containing RangeIndex info
    # and data type summary
    info = "\n".join(lines[1:2] + (lines[-3:-2]))

    display(datatypes)
    print(info)

    return info, datatypes