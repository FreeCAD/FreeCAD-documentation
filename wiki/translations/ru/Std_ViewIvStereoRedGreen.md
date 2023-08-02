---
- GuiCommand:
   Name/ru: Стерео красный/голубой
   Name: Std_ViewIvStereoRedGreen
   MenuLocation: Вид -> Стерео -> Стерео красный/голубой
   Workbenches: Все
   SeeAlso: Std_ViewIvStereoQuadBuff/ru, Std_ViewIvStereoInterleavedRows/ru, Std_ViewIvStereoInterleavedColumns/ru, Std_ViewIvStereoOff/ru
---

# Std ViewIvStereoRedGreen/ru



## Описание

The **Std ViewIvStereoRedGreen** command changes the active [3D view](3D_view.md) to red/cyan, [anaglyph](https://en.wikipedia.org/wiki/Anaglyph_3D), stereo view mode. To use this stereo mode glasses with colored lenses are required.



## Применение

1.  Select the **View → Stereo → <img src="images/Std_ViewIvStereoRedGreen.svg" width=16px> Stereo red/cyan** option from the menu.



## Настройки

-   Расстояние между глаз может быть изменено в настройках: **Правка → Настройки... → Отображение → Трёхмерный вид → Расстояние между глаз для стерео режима**. Смотри [Редактор настроек](Preferences_Editor/ru#3D_View.md).



## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To change the view to red/cyan stereo use the `setStereoType` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setStereoType('Anaglyph')
FreeCADGui.ActiveDocument.ActiveView.getStereoType()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewIvStereoRedGreen/ru
