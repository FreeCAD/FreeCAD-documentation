---
- GuiCommand:
   Name/ru: Четверная буферизация стерео
   Name: Std_ViewIvStereoQuadBuff
   MenuLocation: Вид - Стерео - Четверная буферизация стерео
   Workbenches: Все
   SeeAlso: [Стерео красный/голубой](Std_ViewIvStereoRedGreen/ru.md), [Стерео с чередованием строк](Std_ViewIvStereoInterleavedRows/ru.md), [Стерео с чередованием столбцов](Std_ViewIvStereoInterleavedColumns/ru.md), [Выключить стерео](Std_ViewIvStereoOff/ru.md)
---

# Std ViewIvStereoQuadBuff/ru



## Описание

The **Std ViewIvStereoQuadBuff** command changes the active [3D view](3D_view.md) to quad buffer stereo view mode. To use this stereo mode a special graphics card, a special display and [shutter glasses](https://en.wikipedia.org/wiki/Active_shutter_3D_system) are requires.



## Применение

1.  Select the **View → Stereo → <img src="images/Std_ViewIvStereoQuadBuff.svg" width=16px> Stereo quad buffer** option from the menu.



## Настройки

-   Расстояние между глаз может быть изменено в настройках: **Правка → Настройки... → Отображение → Трёхмерный вид → Расстояние между глаз для стерео режима**. Смотри [Редактор настроек](Preferences_Editor/ru#3D_View.md).



## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To change the view to quad buffer stereo use the `setStereoType` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('QuadBuffer')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewIvStereoQuadBuff/ru
