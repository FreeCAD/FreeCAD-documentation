# Help Module
The Help module is responsible for handling all requests for documentation, and displaying it in an appropriate manner. Up to FreeCAD version 0.21, the Help module is available as an [Addon](Std_AddonMgr.md), after that it will be included in FreeCAD itself. There is no problem in leaving the addon installed after version 0.21.

The Help module provides a preferences page under menu Help -\> Preferences -\> General -\> Help, which allows to specify:

-   The source of the documentation: The documentation can be fetched from online locations such as the [official FreeCAD wiki](https://wiki.freecad.org) (default) or the [markdown conversion](https://github.com/FreeCAD/FreeCAD-documentation), or from an offline location, such as a folder where the documentation can be downloaded with the [Addon manager](Std_AddonMgr.md).

-   The way the documentation must be displayed: In a new FreeCAD tab, in a separate, dockable dialog, that allows you for ex. to keep the documentation displayed while you are working (this is useful for tutorials), or in your desktop browser.

-   An alternative css file: This is used only when using the markdown or offline sources above, and allows you to customize the styling of the documentation.

#### Scripting

The Help module basically consists of a [single python module](https://github.com/FreeCAD/FreeCAD/blob/main/src/Mod/Help/Help.py). Its main usage is using the \"show\" function. It can retrieve an URL, a local file (markdown or html), or find a page automatically from the settings set under Preferences -\> General -\> Help.

It doesn\'t matter what you provide, the system will recognize if the contents are HTML or Markdown and render it appropriately.

Basic usage:

   import Help
   Help.show("Draft Line")
   Help.show("Draft_Line") # works with spaces or underscores
   Help.show("[https://wiki.freecadweb.org/Draft_Line](https://wiki.freecadweb.org/Draft_Line)")
   Help.show("[https://gitlab.com/freecad/FreeCAD-documentation/-/raw/main/wiki/Draft_Line.md](https://gitlab.com/freecad/FreeCAD-documentation/-/raw/main/wiki/Draft_Line.md)")
   Help.show("/home/myUser/.FreeCAD/Documentation/Draft_Line.md")
   Help.show("[http://myserver.com/myfolder/Draft_Line.html](http://myserver.com/myfolder/Draft_Line.html)")

Preferences keys (in \"User parameter:BaseApp/Preferences/Mod/Help\"):

-   optionBrowser/optionTab/optionDialog (bool): Where to open the help dialog
-   optionOnline/optionOffline (bool): where to fetch the documentation from
-   URL (string): online location
-   Location (string): offline location
-   Suffix (string): a suffix to add to the URL, ex: /fr
-   StyleSheet (string): optional CSS stylesheet to style the output



---
⏵ [documentation index](../README.md) > [Help](Help_Workbench.md) > Help Module
