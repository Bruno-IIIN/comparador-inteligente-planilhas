from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout
from ui.styles import CARD_STYLE


class DashboardCard(QFrame):

    def __init__(self, title, value):
        super().__init__()

        self.setStyleSheet(CARD_STYLE)

        layout = QVBoxLayout()

        title_label = QLabel(title)
        value_label = QLabel(str(value))

        value_label.setStyleSheet('font-size: 28px; font-weight: bold;')

        layout.addWidget(title_label)
        layout.addWidget(value_label)

        self.setLayout(layout)
