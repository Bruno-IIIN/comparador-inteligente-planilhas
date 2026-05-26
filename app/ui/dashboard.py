import pandas as pd
import plotly.express as px

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem
)

from PySide6.QtWebEngineWidgets import (
    QWebEngineView
)


class Dashboard(QWidget):

    def __init__(self, result):

        super().__init__()

        self.setWindowTitle(
            "Dashboard Comparativo"
        )

        self.resize(1400, 900)

        layout = QVBoxLayout()

        summary = result["summary"]

        summary_label = QLabel(
            f"""
            Total Antigo: {summary['total_antigo']} |
            Total Novo: {summary['total_novo']} |
            Novos: {summary['novos_registros']} |
            Removidos: {summary['removidos']} |
            Linhas Alteradas: {summary['linhas_alteradas']} |
            Total Alterações: {summary['total_alteracoes']}
            """
        )

        summary_label.setStyleSheet(
            '''
            font-size: 16px;
            padding: 10px;
            '''
        )

        layout.addWidget(summary_label)

        labels = [
            "Novos",
            "Removidos",
            "Alterados"
        ]

        values = [
            summary["novos_registros"],
            summary["removidos"],
            summary["linhas_alteradas"]
        ]

        fig = px.pie(
            names=labels,
            values=values,
            hole=0.5,
            title="Distribuição de Alterações"
        )

        graph = QWebEngineView()

        graph.setHtml(
            fig.to_html(
                include_plotlyjs="cdn"
            )
        )

        layout.addWidget(graph)

        table = QTableWidget()

        changed = result["changed"]

        total_rows = sum(
            len(item["alteracoes"])
            for item in changed
        )

        table.setRowCount(total_rows)

        table.setColumnCount(5)

        table.setHorizontalHeaderLabels([
            "ID",
            "Coluna",
            "Valor Antigo",
            "Valor Novo",
            "Tipo"
        ])

        row_index = 0

        for item in changed:

            row_id = item["id"]

            for change in item["alteracoes"]:

                table.setItem(
                    row_index,
                    0,
                    QTableWidgetItem(str(row_id))
                )

                table.setItem(
                    row_index,
                    1,
                    QTableWidgetItem(
                        str(change["coluna"])
                    )
                )

                table.setItem(
                    row_index,
                    2,
                    QTableWidgetItem(
                        str(change["valor_antigo"])
                    )
                )

                table.setItem(
                    row_index,
                    3,
                    QTableWidgetItem(
                        str(change["valor_novo"])
                    )
                )

                table.setItem(
                    row_index,
                    4,
                    QTableWidgetItem(
                        str(change["tipo"])
                    )
                )

                row_index += 1

        layout.addWidget(table)

        self.setLayout(layout)
