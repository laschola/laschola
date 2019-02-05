import os
import sys

from cx_Freeze import setup,Executable

os.environ['TCL_LIBRARY'] = 'C:/Users/admin/Anaconda3/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'C:/Users/admin/Anaconda3/tcl/tk8.6'

build_exe_options = {'includes':['numpy.core._methods', 'numpy.lib.format',"matplotlib.backends.backend_qt4agg"]}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

directory_table = [
    (
        'ProgramMenuFolder',
        'TARGETDIR',
        ".",


    ),
    (
        'CFRP_slicer_MyProgramMenu',
        'ProgramMenuFolder',
        'CFRP_slicer'


    ),
]

msi_data = {
    'Directory': directory_table
}


setup(
    name='CFRP_slicer',
    version='1.0.0',
    packages=['slicer', 'slicer.views', 'slicer.config', 'slicer.models', 'slicer.models.tool_path'],
    url='http://www.mech.cst.nihon-u.ac.jp/studies/ueda/',
    license='MIT',
    author='Kakeru Kojima',
    author_email='kakerukojima0313@gmail.com',
    description='',
    options={'build_exe': build_exe_options,
             'bdist_msi': {'data' : msi_data}},
    executables= [
        Executable(
            'main.py',
            base = base,
            shortcutName='CFRP_slicer',
            shortcutDir='CFRP_slicer_MyProgramMenu'
        )
    ]
)

