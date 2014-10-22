# -*- mode: python -*-
a = Analysis(['obsanity.py'],
             pathex=['c:\\dev\\obsanity'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)

a.binaries = a.binaries - TOC([
 ('user32.dll', '', ''),
 ('gdi32.dll', '', ''),
 ('comctl32.dll', '', '')])

pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='obsanity.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False)
