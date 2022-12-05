# Std Edit/ro
---
- GuiCommand:   Name:Std Edit   MenuLocation:[[Std_Edit_Menu   Edit]] → Toggle Editmode|Workbenches:All   SeeAlso:...---


</div>


<div class="mw-translate-fuzzy">

#### Rezumat


</div>


<div class="mw-translate-fuzzy">

Această comandă permite intrarea sau ieșirea din modul de editare al unui obiect selectat. Un obiect trebuie să fie selectată (apoi intră în modul de editare) sau în modul de editare (apoi iese din modul de editare) pentru ca această comandă să funcționeze.


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

### Script


</div>


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Aceasta intră în modul de editare al unui obiect determinat:


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

Aceasta închide modul de editare:


</div>


```python
import FreeCADGui

FreeCADGui.ActiveDocument.resetEdit()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Edit/ro
