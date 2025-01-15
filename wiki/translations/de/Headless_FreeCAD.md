# Headless FreeCAD/de
## Einleitung

Diese Wiki-Seite dokumentiert verschiedene Aspkte des Betriebs von FreeCAD in der Konsole, ohne die Benutzerschnittstelle (GUI) zu aktivieren, was auch \'kopflos\' (headless) genannt wird.

## Scenegraph Representation 

As it\'s not possible to create or access the [view provider](Viewprovider.md) in headless mode. What\'s possible is to load `FreeCADGui` in headless mode but there is no way to access the GUI document because it won\'t be created and consequently there exist no view providers.

However, what\'s possible is to create a [scenegraph](Scenegraph.md) representation of an object:


{{Code|lang=python|code=
import FreeCADGui as Gui
from pivy import coin

Gui.setupWithoutGUI()
doc = App.newDocument()
obj = doc.addObject("Part::Box","Box")
doc.recompute()
view = Gui.subgraphFromObject(obj)
}}

See: [forum thread](https://forum.freecadweb.org/viewtopic.php?f=10&t=55794&p=481586#p481586).

## Examples

### Searching FreeCAD Modules 

1.  Open the terminal and type:

    :   
        `$ /path/to/FreeCAD -c`
        

        :   or

    :   
        `$ /path/to/FreeCADCmd`
        
2.  A python shell will start with a prompt. Type `help()`.
3.  A help text is displayed.
4.  Type `modules freecad`.

## Related

-   [Embedding FreeCAD](Embedding_FreeCAD#Using_FreeCAD_without_GUI.md)
-   [Start up and Configuration](Start_up_and_Configuration#Running_FreeCAD_without_GUI_(headless).md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Poweruser Documentation](Category_Poweruser%20Documentation.md) > Headless FreeCAD/de
