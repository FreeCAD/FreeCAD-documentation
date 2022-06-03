---
- GuiCommand   */ru
   Name   *Std SelBoundingBox
   Name/ru   *Std SelBoundingBox
   MenuLocation   *Вид → Bounding box
   Workbenches   *All
   SeeAlso   *[Std DrawStyle](Std_DrawStyle/ru.md)
---

# Std SelBoundingBox/ru


</div>

## Описание

The **Std SelBoundingBox** command toggles the global bounding box highlighting mode. If this mode is switched on, selected objects are marked in a [3D view](3D_view.md) with a highlighted bounding box even if their **Selection Style** is set to \'Shape\'.

## Применение

1.  There are several ways to invoke the command   *
    -   Press the **<img src="images/Std_SelBoundingBox.svg" width=16px> [Std SelBoundingBox](Std_SelBoundingBox.md)** button.
    -   Select the **View → <img src="images/Std_SelBoundingBox.svg" width=16px> Bounding box** option from the menu.

## Настройки

The related setting is stored   * **Tools → Edit parameters... → BaseApp → Preferences → View → ShowSelectionBoundingBox**. It is a boolean value, the default is `False`.

## Scripting


**Смотрите так же   ***

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To change the ShowSelectionBoundingBox setting use the `SetBool` method of the appropriate ParameterGrp. The code sample does not work if FreeCAD is in console mode.


```python
import FreeCAD, FreeCADGui

grp = FreeCAD.ParamGet('User parameter   *BaseApp/Preferences/View')
if grp.GetBool('ShowSelectionBoundingBox')   *
  grp.SetBool('ShowSelectionBoundingBox',False)
else   *
  grp.SetBool('ShowSelectionBoundingBox',True)

FreeCADGui.updateCommands()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std SelBoundingBox/ru
