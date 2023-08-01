---
- GuiCommand:
   Name:Std PythonHelp
   MenuLocation:Help → Automatic python modules documentation
   Workbenches:All
   SeeAlso:[Std FreeCADPowerUserHub](Std_FreeCADPowerUserHub.md)
---

# Std PythonHelp

## Description

The **Std PythonHelp** command starts a web server that communicates with the system\'s default Internet browser over a local socket. The web server displays information about the available [Python](Python.md) modules, classes and functions of FreeCAD. The required pages are generated automatically.

The web server is based on Python\'s [pydoc](https://docs.python.org/3.8/library/pydoc.html#module-pydoc) module, and thus extracts the docstrings of Python files (`.py`), and textual documentation defined in the Python wrappers (`.xml`) which expose the underlying C++ code.

## Usage

1.  Select the **Help → <img src="images/Std_PythonHelp.svg" width=16px> Automatic python modules documentation** option from the menu.
2.  Click on any of the links to go to the documentation of a specific class or function.




 {{Std Base navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std PythonHelp
