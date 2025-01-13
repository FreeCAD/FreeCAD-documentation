---
 GuiCommand:
   Name/ru: Габариты
   Name: Std_SelBoundingBox
   MenuLocation: Вид , Габариты
   Workbenches: Все
   Version: 0.19
   SeeAlso: Std_DrawStyle/ru
---

# Std SelBoundingBox/ru



## Описание

The **Std SelBoundingBox** command toggles the global bounding box highlighting mode. If this mode is switched on, selected objects are marked in a [3D view](3D_view.md) with a highlighted bounding box even if their **Selection Style** is set to \'Shape\'.



## Применение

1.  Select the **View → <img src="images/Std_SelBoundingBox.svg" width=16px> Bounding box** option from the menu.



## Программирование


<div class="mw-translate-fuzzy">


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).


</div>

To change the ShowSelectionBoundingBox parameter use the `SetBool` method of the appropriate ParameterGrp.


```python
import FreeCAD, FreeCADGui

grp = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/View")
if grp.GetBool("ShowSelectionBoundingBox"):
    grp.SetBool("ShowSelectionBoundingBox", False)
else:
    grp.SetBool("ShowSelectionBoundingBox", True)

FreeCADGui.updateCommands()
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std SelBoundingBox/ru
