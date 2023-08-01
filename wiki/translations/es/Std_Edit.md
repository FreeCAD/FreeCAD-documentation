# Std Edit/es
---
- GuiCommand:/es   Name:Std_Edit   Name/es:Std Edit   MenuLocation:[[Std_Edit_Menu/es   Edición]] -> Conmutar modo de edición|Workbenches:Todos   SeeAlso:...---


</div>


<div class="mw-translate-fuzzy">

#### Sinopsis


</div>


<div class="mw-translate-fuzzy">

Este comando permite entrar o abandonar el modo de edición de un objeto seleccionado. Un objeto debe estar seleccionado (para entrar en modo de edición) o en modo de edición (para abandonar el modo de edición) para que funcione este comando.


</div>

## Usage

1.  If no object is in edit mode: select a single object.
2.  Select the **Edit → <img src="images/Std_Edit.svg" width=16px> Toggle Edit mode** option from the menu.
3.  Either the default edit mode of the selected object is activated or the existing edit mode deactivated.

## Notes

-   Some tools will be disabled (greyed-out) in the user interface while an object\'s edit mode is active.
-   Not all object types have an edit mode.
-   The functionality available in edit mode depends on the object type.
-   An object\'s edit mode can also be activated by double-clicking it in the [Tree view](Tree_view.md). In that case the edit mode that is used can be defined with the [Std UserEditMode](Std_UserEditMode.md) command.


<div class="mw-translate-fuzzy">

#### Archivos de guión 


</div>


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Esto entra en el modo de edición de un objeto determinado:


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

Esto cierra ek modo de edición:


</div>


```python
import FreeCADGui

FreeCADGui.ActiveDocument.resetEdit()
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std Edit/es
