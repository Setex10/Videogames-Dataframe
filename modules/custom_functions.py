# In this file you can find the custom functions that I use in the project

from modules import re
from modules import pandas
from modules import plt
from modules import seaborn as sns


def format_number(value: str) -> float:
    """
    ## Function that transform a string to a number
    Args:
        value (str): Is a number with the format 1.2k or 1k or semething like that
        
    Returns:
        float: Return the number with the format 1200.0 or 1000.0 or something like that
    """
    regexs = [r"(k|K)$", r"[.]"]
    
    def _modify_value(number: int) -> str:
        """
        ## Function that modify the value of the string

        Args:
            number (int): Is a number that you want to modify the format value to string

        Returns:
            str: return the value with the format 1200.0
        """
        try:
            new_value = re.sub(pattern = regexs[0], repl = "000", string = value)
            return float(new_value) * number
        except TypeError:
            print("Invalid type of value")
            return value
        
    conditions = {
        "k": lambda x: re.search(pattern = regexs[0], string = x),
        "point": lambda x: re.search(pattern = regexs[1], string = x)
    }
    
    try:
        if conditions["k"](value) and conditions["point"](value):
            return _modify_value(1000)
        elif conditions["k"](value):
            return _modify_value(1)
    except TypeError:
        return value
        

def clean_string(value: str) -> str:
    """
    ## Function that delete the characters "[" and "]"  

    Args:
        value (str): String that you want to clean

    Returns:
        str: Return the string that was cleaned 
    """
    regex = r"[\[\]']"
    try:
        new_string = re.sub(pattern=regex, string=f"{value}", repl="")
        return new_string
    except TypeError:
        print("The type of the value is not recognized")
        return value

def generate_visualization(df: pandas.DataFrame, columns: list, visualization: str):
    """
    ## Function that generate a visualization from a dataframe
    
    Args:
        df (pandas.DataFrame): Is a dataframe
        colums (list): Is a list of columns that you want to visualize
        visualization (str): Is the type of visualization that you want to generate
            for visualization, and in the moment, only one visualization is available: histplot
    
    Returns:
        fig, ax: Is a tuple with the figure and the axis
    """
    if len(columns) == 0:
        print("The list of colums is empty")
    else:
        n = len(columns)
        n_rows = 0
        n_cols = 2
    
        dict_visualiations = {
            "histplot": sns.histplot,
        }
    
        if n % 2 == 0:
            n_rows = int(n / 2)
        else:
            n_rows = int((n + 1) / 2)
    
        fig, ax = plt.subplots(nrows = n_rows, ncols = n_cols, figsize = (20, 10))
    
        for idx, col in enumerate(columns):
            dict_visualiations[visualization](data = df[col], 
                                            ax = ax[idx//n_cols, idx%n_cols], 
                                            color = "red")
        return fig, ax