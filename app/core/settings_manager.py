from PySide6.QtCore import QSettings


class SettingsManager:

    settings = QSettings('ComparadorInteligente', 'Planilhas')

    @classmethod
    def save(cls, key, value):
        cls.settings.setValue(key, value)

    @classmethod
    def load(cls, key, default=None):
        return cls.settings.value(key, default)
