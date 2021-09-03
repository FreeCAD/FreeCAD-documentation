---
- GuiCommand:/de
   Name:Std Bearbeiten
   MenuLocation:Bearbeiten → Umschalten Bearbeitungsmodus
   Workbenches:Alle
---

## Beschreibung


<div class="mw-translate-fuzzy">

Dieser Befehl erlaubt es Dir, den Bearbeitungsmodus eines ausgewählten Objekts aufzurufen oder zu verlassen. Ein Objekt muss entweder ausgewählt (dann wechselt es in den Bearbeitungsmodus) oder im Bearbeitungsmodus (dann verlässt es den Bearbeitungsmodus) sein, damit dieser Befehl funktioniert.


</div>

## Anwendung

1.  If no object is in edit mode: select a single object.
2.  Select the {{MenuCommand|Edit → <img src="images/Std_Edit.svg" width=16px> Toggle Edit mode}} option from the menu.
3.  Either the edit mode of the selected object is activated or the existing edit mode deactivated.

## Hinweise

-   Some tools will be disabled (greyed-out) in the user interface while an object\'s edit mode is active.
-   Not all object types have an edit mode.
-   The functionality available in edit mode depends on the object type.
-   Edit mode can also be activated by double-clicking an object in the [Tree view](Tree_view.md).

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


<div class="mw-translate-fuzzy">

Dies öffnet den Bearbeitungsmodus eines bestimmten Objekts:


</div>


```python
import FreeCADGui

FreeCADGui.ActiveDocument.setEdit("myObjectName",0)
```

The second argument is the EditMode. The following options are available:

0 = Default
1 = Transform
2 = Cutting
3 = Color


<div class="mw-translate-fuzzy">

Dies beendet den Bearbeitungsmodus:


</div>


```python
import FreeCADGui

FreeCADGui.ActiveDocument.resetEdit()
```





{{Std Base navi

}}  
