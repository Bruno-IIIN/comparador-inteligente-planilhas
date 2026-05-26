from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
    QMessageBox,
    QHBoxLayout,
    QApplication
)

from app.core.excel_reader import ExcelReader
from app.core.comparator import SpreadsheetComparator
from app.ui.dashboard import Dashboard


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.old_file = None
        self.new_file = None

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(
            'Comparador Inteligente de Planilhas'
        )

        self.resize(1200, 800)

        layout = QVBoxLayout()

        title = QLabel(
            'Comparador Inteligente de Planilhas'
        )

        title.setStyleSheet(
            '''
            font-size: 32px;
            font-weight: bold;
            padding: 20px;
            '''
        )

        layout.addWidget(title)

        buttons_layout = QHBoxLayout()

        self.old_btn = QPushButton(
            'Selecionar Planilha Anterior'
        )

        self.new_btn = QPushButton(
            'Selecionar Planilha Atual'
        )

        self.compare_btn = QPushButton('Comparar')

        self.old_btn.clicked.connect(self.load_old)
        self.new_btn.clicked.connect(self.load_new)
        self.compare_btn.clicked.connect(self.compare)

        buttons_layout.addWidget(self.old_btn)
        buttons_layout.addWidget(self.new_btn)
        buttons_layout.addWidget(self.compare_btn)

        layout.addLayout(buttons_layout)

        self.status = QLabel(
            'Nenhum arquivo carregado'
        )

        layout.addWidget(self.status)

        self.setLayout(layout)

    def load_old(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            'Selecionar Planilha Anterior',
            '',
            'Excel Files (*.xlsx *.xls)'
        )

        if path:
            self.old_file = path

            self.status.setText(
                f'Anterior: {path}'
            )

    def load_new(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            'Selecionar Planilha Atual',
            '',
            'Excel Files (*.xlsx *.xls)'
        )

        if path:
            self.new_file = path

            self.status.setText(
                f'Atual: {path}'
            )

    def compare(self):
        if not self.old_file or not self.new_file:
            QMessageBox.warning(
                self,
                'Aviso',
                'Selecione ambas as planilhas.'
            )
            return

        QApplication.setOverrideCursor(
            Qt.WaitCursor
        )

        try:
            old_df = ExcelReader.load_excel(
                self.old_file
            )

            new_df = ExcelReader.load_excel(
                self.new_file
            )

            key_column = old_df.columns[0]

            comparator = SpreadsheetComparator(
                old_df,
                new_df,
                key_column
            )

            result = comparator.compare()

            self.dashboard = Dashboard(result)
            self.dashboard.show()

        except Exception as e:
            QMessageBox.critical(
                self,
                'Erro',
                str(e)
            )

        finally:
            QApplication.restoreOverrideCursor()
