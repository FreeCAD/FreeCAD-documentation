# FreeCADGui API/de
<div class="mw-translate-fuzzy">


**(November 2018) Diese Information kann unvollständig und veraltet sein. Für die letzte API siehe die (engl.) [https://www.freecadweb.org/api autogenerierte API-Dokumentation].**


</div>

This module is the counterpart of the FreeCAD module. It contains everything related to the User interface and the 3D views. Example: 
```python
import FreeCAD as App
import FreeCADGui as Gui

# get the 3D model document
doc = App.ActiveDocument    

# get the visual representation model document
gui_doc = Gui.ActiveDocument

gui_doc.activateWorkbench("myWorkbench")
```


{{APIFunction|activateWorkbench|string|Activates a workbench by name|nothing}}


{{APIFunction|activeDocument| | |the active document or None if no one exists}}


{{APIFunction|activeWorkbench| | |the active workbench object}}


{{APIFunction|addCommand|string, object|Adds a FreeCAD command. String is the name of the command and object is a classname defining the command| }}


{{APIFunction|addIcon|string, string or list|Adds an icon as file name or in XPM format to the system| }}


{{APIFunction|addIconPath|string|Add a new path to the system where to find icon files| }}


{{APIFunction|addPreferencePage|string,string|Adds a UI form to the preferences dialog. The first argument specifies the file name and the second specifies the group name| }}


{{APIFunction|addWorkbench|string, object|Adds a workbench under a defined name. The string is the workbench name and the object is a classname defining the workbench| }}


{{APIFunction|createDialog|string|Opens a UI file| }}


{{APIFunction|getDocument|string|Gets a document by its name|the document}}


{{APIFunction|getWorkbench|string|Gets a workbench by its name|the workbench}}


{{APIFunction|insert|string|Open a macro, Inventor or VRML file|the document}}


{{APIFunction|listWorkbenches| |Shows a list of all workbenches|a list}}


{{APIFunction|open|string|Opens a macro, Inventor or VRML file|the openend document}}


{{APIFunction|removeWorkbench|string|Removes a workbench by name| }}


{{APIFunction|runCommand|string|Runs a FreeCAD command by name| }}


{{APIFunction|updateGui| |Updates the main window and all its windows| }}


 

_ _

---
[documentation index](../README.md) > [API](Category_API.md) > FreeCADGui API/de
