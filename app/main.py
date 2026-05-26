import sys
from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet

from ui.main_window import MainWindow
from ui.splash_screen import show_splash


def main():
    app = QApplication(sys.argv)

    apply_stylesheet(app, theme='dark_teal.xml')

    splash = show_splash(app)

    window = MainWindow()
    window.show()

    splash.finish(window)

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
