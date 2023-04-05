# Here you will find the DataFrame used to generate the visualization
__all__ = ['df']

from modules import os, pandas as pd

if not __name__ == "__main__":
    module_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir + "\\games.csv"))
    
    df = pd.read_csv(module_path)
