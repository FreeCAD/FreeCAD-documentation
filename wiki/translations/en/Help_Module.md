# Help Module/en
## Description

The Help module is responsible for handling all requests for documentation, and displaying it in an appropriate manner. Up to FreeCAD version 0.21, the Help module is available as an [Addon](Std_AddonMgr.md), after that it is included in FreeCAD itself. There is no problem in leaving the Addon installed after version 0.21.

The Help module provides a preferences page under menu **Edit → Preferences → General → Help**, which allows to specify:

-   The source of the documentation: The documentation can be fetched from online locations such as the [official FreeCAD wiki](https://wiki.freecad.org) (default) or the [Markdown conversion](https://github.com/FreeCAD/FreeCAD-documentation), or from an offline location, such as a folder where the documentation can be downloaded with the [Addon manager](Std_AddonMgr.md).

-   The way the documentation must be displayed: in your desktop browser, in a separate, dockable dialog, that allows you for ex. to keep the documentation displayed while you are working (this is useful for tutorials), or a new FreeCAD tab. Note that in version 1.0 the 2nd and 3rd option require PySide Web components. If these are missing the 1st option will be used instead.

-   An alternative css file: This is used only when using the Markdown or offline sources above, and allows you to customize the styling of the documentation.

## Scripting

The Help module basically consists of a [single Python module](https://github.com/FreeCAD/FreeCAD/blob/main/src/Mod/Help/Help.py). Its main usage is using the {{Incode|show}} function. It can retrieve an URL, a local file (Markdown or html), or find a page automatically from the settings set under **Preferences → General → Help**.

It doesn\'t matter what you provide, the system will recognize if the contents are HTML or Markdown and render it appropriately.

Basic usage:


```python
import Help
Help.show("Draft Line")
Help.show("Draft_Line")  # works with spaces or underscores
Help.show("https://wiki.freecadweb.org/Draft_Line")
Help.show("https://gitlab.com/freecad/FreeCAD-documentation/-/raw/main/wiki/Draft_Line.md")
Help.show("/home/myUser/.FreeCAD/Documentation/Draft_Line.md")
Help.show("http://myserver.com/myfolder/Draft_Line.html")
```



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > [Help](Help_Workbench.md) > Help Module/en
