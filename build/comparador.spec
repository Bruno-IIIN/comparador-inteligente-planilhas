# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

project_path = Path.cwd()

block_cipher = None

a = Analysis(
    [str(project_path / "app" / "main.py")],
    pathex=[str(project_path)],
    binaries=[],
    datas=[
        (
            str(project_path / "app" / "assets"),
            "assets"
        )
    ],
    hiddenimports=[
        "PySide6.QtWebEngineWidgets",
        "plotly",
        "pandas",
        "openpyxl"
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
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=str(
        project_path / "app" / "assets" / "icon.ico"
    ),
)
