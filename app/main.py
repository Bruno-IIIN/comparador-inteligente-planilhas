import sys

from PySide6.QtWidgets import QApplication

from app.ui.main_window import MainWindow
from app.ui.splash_screen import show_splash

from qt_material import apply_stylesheet


def main():

    app = QApplication(sys.argv)

    apply_stylesheet(
        app,
        theme='dark_teal.xml'
    )

    splash = show_splash(app)

    window = MainWindow()

    window.show()

    splash.finish(window)

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
