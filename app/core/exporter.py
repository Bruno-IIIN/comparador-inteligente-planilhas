import pandas as pd


class Exporter:

    @staticmethod
    def export_excel(data, path):
        with pd.ExcelWriter(path, engine='xlsxwriter') as writer:
            data['added'].to_excel(writer, sheet_name='Adicionados')
            data['removed'].to_excel(writer, sheet_name='Removidos')
