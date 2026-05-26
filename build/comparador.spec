# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path
from PyInstaller.utils.hooks import collect_submodules

project_path = Path.cwd()

hidden_imports = collect_submodules("plotly")

a = Analysis(
    [str(project_path / "app" / "main.py")],
    pathex=[str(project_path)],
    binaries=[],
    datas=[],
    hiddenimports=hidden_imports + [
        "PySide6.QtWebEngineWidgets",
        "pandas",
        "openpyxl",
        "qt_material"
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="ComparadorInteligente",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False
)
