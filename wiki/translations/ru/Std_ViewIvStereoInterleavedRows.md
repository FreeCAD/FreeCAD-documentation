---
- GuiCommand:/ru
   Name/ru:Стерео с чередованием строк
   Name:Std_ViewIvStereoInterleavedRows
   MenuLocation:Вид → Стерео → Stereo interleaved Rows
   Workbenches:Все
   SeeAlso:[Стерео красный/голубой](Std_ViewIvStereoRedGreen/ru.md), [Четверная буферизация стерео](Std_ViewIvStereoQuadBuff/ru.md), [Стерео с чередованием столбцов](Std_ViewIvStereoInterleavedColumns/ru.md), [Выключить стерео](Std_ViewIvStereoOff/ru.md)
---

# Std ViewIvStereoInterleavedRows/ru



## Описание

The **Std ViewIvStereoInterleavedRows** command changes the active [3D view](3D_view.md) to interleaved rows stereo view mode. To use this stereo mode a special graphics card, a special display and [glasses with polarized lenses](https://en.wikipedia.org/wiki/Polarized_3D_system) are requires.



## Применение

1.  Select the **View → Stereo → <img src="images/Std_ViewIvStereoInterleavedRows.svg" width=16px> Stereo interleaved Rows** option from the menu.



## Настройки

-   Расстояние между глаз может быть изменено в настройках: **Правка → Настройки... → Отображение → Трёхмерный вид → Расстояние между глаз для стерео режима**. Смотри [Редактор настроек](Preferences_Editor/ru#3D_View.md).

## Scripting


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To change the view to interleaved rows stereo use the `setStereoType` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('InterleavedRows')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewIvStereoInterleavedRows/ru
