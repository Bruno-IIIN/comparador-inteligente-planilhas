from PySide6.QtWidgets import QSplashScreen
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


def show_splash(app):
    pixmap = QPixmap('assets/splash.png')

    splash = QSplashScreen(pixmap)
    splash.setWindowFlag(Qt.WindowStaysOnTopHint)
    splash.show()

    app.processEvents()

    return splash
