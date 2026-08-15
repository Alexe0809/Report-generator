import pandas as pd
from pathlib import Path


def load_data_csv():
    folder = Path('data/input')
    files = list(folder.glob('*.csv'))
    try:
        df = pd.read_csv(files[0]) # in test we will use only one file
    except Exception as e:
        print('Folder is empty')   
    return df


def load_data_excel():
    pass