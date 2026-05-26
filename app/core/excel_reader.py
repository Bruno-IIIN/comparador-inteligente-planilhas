import pandas as pd


class ExcelReader:

    @staticmethod
    def load_excel(path: str):
        return pd.read_excel(path, engine='openpyxl')
