---
- GuiCommand:
   Name/ru: Стерео с чередованием столбцов
   Name: Std_ViewIvStereoInterleavedColumns
   MenuLocation: Вид -> Стерео -> Stereo interleaved Columns
   Workbenches: Все
   SeeAlso: Std_ViewIvStereoRedGreen/ru, Std_ViewIvStereoQuadBuff/ru, Std_ViewIvStereoInterleavedRows/ru, Std_ViewIvStereoOff/ru
---

# Std ViewIvStereoInterleavedColumns/ru



## Описание

The **Std ViewIvStereoInterleavedColumns** command changes the active [3D view](3D_view.md) to interleaved columns stereo view mode. To use this stereo mode a special graphics card, a special display and [glasses with polarized lenses](https://en.wikipedia.org/wiki/Polarized_3D_system) are requires.



## Применение

1.  Select the **View → Stereo → <img src="images/Std_ViewIvStereoInterleavedColumns.svg" width=16px> Stereo interleaved Columns** option from the menu.



## Настройки

-   Расстояние между глаз может быть изменено в настройках: **Правка → Настройки... → Отображение → Трёхмерный вид → Расстояние между глаз для стерео режима**. Смотри [Редактор настроек](Preferences_Editor/ru#3D_View.md).



## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To change the view to interleaved columns stereo use the `setStereoType` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('InterleavedColumns')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewIvStereoInterleavedColumns/ru
