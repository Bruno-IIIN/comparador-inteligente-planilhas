import plotly.express as px
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView


class Dashboard(QWidget):

    def __init__(self, result):
        super().__init__()

        layout = QVBoxLayout()

        labels = ['Novos', 'Removidos', 'Alterados']
        values = [
            len(result['added']),
            len(result['removed']),
            len(result['changed'])
        ]

        fig = px.pie(
            names=labels,
            values=values,
            title='Distribuição de Alterações'
        )

        graph = QWebEngineView()
        graph.setHtml(fig.to_html(include_plotlyjs='cdn'))

        layout.addWidget(graph)

        self.setLayout(layout)
