---
- GuiCommand   */ru
   Name   *Std ViewIvStereoOff
   Name/ru   *Std ViewIvStereoOff
   MenuLocation   *Вид → Стерео → View → Выключить стерео
   SeeAlso   *[Std ViewIvStereoRedGreen](Std_ViewIvStereoRedGreen/ru.md), [Std ViewIvStereoQuadBuff](Std_ViewIvStereoQuadBuff/ru.md), [/ruStd ViewIvStereoInterleavedRows](Std_ViewIvStereoInterleavedRows.md), [Std ViewIvStereoInterleavedColumns](Std_ViewIvStereoInterleavedColumns/ru.md)
---

# Std ViewIvStereoOff/ru

## Описание

Команда **Std ViewIvStereoOff** выключает стерео режим в активном [3D view](3D_view/ru.md).

## Применение

1.  Выберите из меню опцию **Вид → Стерео → <img src="images/Std_ViewIvStereoOff.svg" width=16px> Выключить стерео**.

## Scripting


**Смотрите так же   ***

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

Чтобы изменить вид на отмену стерео, используйте метод `setStereoType` объекта ActiveView. Этот метод не доступен, когда FreeCAD в режиме консоли.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('None')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewIvStereoOff/ru
