# FreeCAD documentation

This repository contains an automatic conversion of the FreeCAD wiki located at https://wiki.freecadweb.org to [markdown format](https://en.wikipedia.org/wiki/Markdown). The conversion is done automatically through the [migrate.py](./migrate.py) script located within this repository. The script downloads the wiki contents in XML format using the MediaWiki API and uses [pandoc](https://pandoc.org/) to convert between mediawiki and markdown formats.

The general idea is to keep allowing users to use the wiki to edit and add contents, while the markdown format for:

1. Better handling of the documentation within FreeCAD, have the ability to code an own help viewer better than the QAssistant viewer currently in use
2. Allow to use either an online or an offline version of the documentation
3. Automatic and easier backups, same as the FreeCAD source code
4. Better versioning and matching to FreeCAD versions
5. Better handling of translations

Further goals:

* Create a Help workbench with a md viewer
    * [QTextDocument](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QTextDocument.html#PySide2.QtGui.PySide2.QtGui.QTextDocument.setMarkdown) supports markdown (but might be problems with online images)
    * Maybe better to use an HTML viewer and convert the markdown content?
* Allow the help workbench to access both online or offline (local files) versions
* Allow the help workbench to access any translated version
* Tie the FreeCAD help system to the Help workbench
* Tie the FreeCAD what's this system to the Help workbench
* Allow to export parts of the documentation to other formats (PDF, ePub,...)



Read on to the [Documentation home page](wiki/main_page.md)



