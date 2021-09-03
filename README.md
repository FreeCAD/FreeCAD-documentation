# FreeCAD documentation

This repository contains an automatic conversion of the FreeCAD wiki located at https://wiki.freecadweb.org to [markdown format](https://en.wikipedia.org/wiki/Markdown). The conversion is done automatically through the [migrate.py](./migrate.py) script located within this repository. The script downloads the wiki contents in XML format using the MediaWiki API and uses [pandoc](https://pandoc.org/) to convert between mediawiki and markdown formats.

The general idea is to keep allowing users to use the wiki to edit and add contents, while the markdown format for:

1. Better handling of the documentation within FreeCAD, have the ability to code an own help viewer better than the QAssistant viewer currently in use
2. Allow to use either an online or an offline version of the documentation
3. Automatic and easier backups, same as the FreeCAD source code
4. Better versioning and matching to FreeCAD versions
5. Better handling of translations

Read on to the [Documentation home page](wiki/main_page.md)

