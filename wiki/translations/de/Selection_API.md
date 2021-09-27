# Selection API/de
<div class="mw-translate-fuzzy">


**(November 2018) Diese Information kann unvollständig und veraltet sein. Für die letzte API siehe die (engl.) [https://www.freecadweb.org/api autogenerierte API-Dokumentation].**


</div>

The selection submodule is part of the FreeCADGui module. Example: 
```python
import FreeCADGui
sel = FreeCADGui.Selection.getSelection()
```


{{APIFunction|addSelection|FreeCAD.Object|Adds an object to the selection| }}


{{APIFunction|clearSelection|[string]|Clears the selection of the given document name. If no document is given the complete selection is cleared.| }}


{{APIFunction|getSelection|[string]|Returns a list of selected document objects for a given document name. If no document is given the complete selection is returned.|a list of document objects in the order they were selected.}}


{{APIFunction|getSelectionEx|[string]|Returns a list of SelectionObject for a given document name. If no document is given the complete selection is returned. Used for selecting subobjects (ex some Edges of a Face).|a list of SelectionObjects in the order they were selected}}


{{APIFunction|isSelected|FreeCAD.Object|Checks if a given object is selected| }}


{{APIFunction|removeSelection|FreeCAD.Object|Removes an object from the selection| }}


 

_ _

---
[documentation index](../README.md) > [API](Category_API.md) > Selection API/de
