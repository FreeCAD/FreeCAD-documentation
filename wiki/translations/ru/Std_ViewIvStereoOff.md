---
- GuiCommand:
   Name:Std_ViewIvStereoOff
   Name/ru:Выключить стерео
   MenuLocation:Вид - Стерео - View - Выключить стерео
   SeeAlso:[Std ViewIvStereoRedGreen](Std_ViewIvStereoRedGreen/ru.md), [Std ViewIvStereoQuadBuff](Std_ViewIvStereoQuadBuff/ru.md), [Std ViewIvStereoInterleavedRows](Std_ViewIvStereoInterleavedRows/ru.md), [Std ViewIvStereoInterleavedColumns](Std_ViewIvStereoInterleavedColumns/ru.md)
---

# Std ViewIvStereoOff/ru

## Описание

Команда **Выключить стерео** выключает стерео режим в активном [3D view](3D_view/ru.md).

## Применение

1.  Выберите из меню опцию **Вид → Стерео → <img src="images/Std_ViewIvStereoOff.svg" width=16px> Выключить стерео**.

## Программирование


**Смотрите так же:**

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
![](images/Button_right.svg) [documentation index](../README.md) > Std ViewIvStereoOff/ru
