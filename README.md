# CSI5610_Smart_City_Management_System

Setup
---

1. Install at least Python 3.10.2+
2. Create virtual environment
    * ```python -m venv [ve_name]```
3. Load virtual environment
    * in CMD ```.\ve_name\Scripts\activate.bat```
    * in PowerShell ```.\ve_name\Scripts\Activate.ps1```
4. Install dependencies
    * ```python -m pip install requirements-dev.txt```

QT UI Design
---

* Start QT Designer with: ```pyqt5-tools designer```

There is two ways of using the generated *.ui file:

1. Generate python code ```pyuic5.exe [path_to_ui_file] -o [path_to_py_file]```
2. Load ui file during runtime: https://doc.qt.io/qtforpython-5/tutorials/basictutorial/uifiles.html