# Headless FreeCAD
## Introduction

This wiki page will document various aspect of running FreeCAD in the console without enabling the GUI (Graphical User Interface) or what is called \'headless\'.

## Scenegraph Representation 

As it\'s not possible to create or access the [view provider](Viewprovider.md) in headless mode. What\'s possible is to load `FreeCADGui` in headless mode but there is no way to access the GUI document because it won\'t be created and consequently there exist no view providers.

However, what\'s possible is to create a [scenegraph](Scenegraph.md) representation of an object. This works this way:


{{Code|lang=python|code=
import FreeCADGui as Gui
from pivy import coin

Gui.setupWithoutGUI()
doc = App.newDocument()
obj = doc.addObject("Part::Box","Box")
doc.recompute()
view = Gui.subgraphFromObject(obj)
}}


:   reference: [forum thread](https://forum.freecadweb.org/viewtopic.php?f=10&t=55794&p=481586#p481586)

## Examples

### Searching FreeCAD Modules 

1.  Open the terminal

    :   
        `$ /path/to/FreeCAD -c`
        

        :   or

    :   
        `$ /path/to/FreeCADCmd`
        
2.  A python shell will start with a prompt. Type `help()`

    :   
        {{Code|lang=text|code=
        [FreeCAD Console mode <Use Ctrl-D (i.e. EOF) to exit.>]
        >>> help()
        Welcome to Python 3.x's help utility!

        If this is your first time using Python, you should definitely check out
        the tutorial on the Internet at https://docs.python.org/3.8/tutorial/.

        Enter the name of any module, keyword, or topic to get help on writing
        Python programs and using Python modules.  To quit this help utility and
        return to the interpreter, just type "quit".

        To get a list of available modules, keywords, symbols, or topics, type
        "modules", "keywords", "symbols", or "topics".  Each module also comes
        with a one-line summary of what it does; to list the modules whose name
        or summary contain a given string such as "spam", type "modules spam".

        help>
        }}
        
3.  Type `modules freecad`

    :   
        
```python
        help> modules freecad
        
```
        

## Related

-   [Embedding FreeCAD\#Using FreeCAD without GUI](Embedding_FreeCAD#Using_FreeCAD_without_GUI.md)
-   [Start up and Configuration\#Running FreeCAD without GUI .28headless.29](Start_up_and_Configuration#Running_FreeCAD_without_GUI_.28headless.29.md)

[Category:Developer Documentation](Embedding_FreeCAD#Using_FreeCAD_without_GUI.md)

[Category:Poweruser Documentation](Category:Poweruser_Documentation.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > Headless FreeCAD
