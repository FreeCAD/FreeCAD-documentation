---
- GuiCommand:/ru
   Name:Std ViewIvIssueCamPos
   Name/ru:Std ViewIvIssueCamPos
   MenuLocation:Вид → Стерео → Выводить положения камеры
   Workbenches:All
   SeeAlso:[Std FreezeViews](Std_FreezeViews/ru.md)
---

# Std ViewIvIssueCamPos/ru

## Описание

The **Std ViewIvIssueCamPos** command prints the camera settings of the active [3D view](3D_view.md) in the [Report view](Report_view.md) and the [Python console](Python_console.md).


```python   OrthographicCamera {   viewportMapping ADJUST_CAMERA   position 57.73505 -57.73502 57.735027   orientation 0.74290609 0.30772209 0.59447283  1.2171158   nearDistance 81.588844   farDistance 109.60551   aspectRatio 1   focalDistance 100   height 100  } 
```



*Example output: camera settings after changing to [isometric view](Std_ViewIsometric.md) in a new document*

## Применение

1.  Выберите из меню опцию **Вид → Стерео → <img src="images/Std_ViewIvIssueCamPos.svg" width=16px> Выводить положения камеры**.

## Примечания

-   The camera settings can be used to add frozen views to a \*.cam file. See [Std FreezeViews](Std_FreezeViews.md).

## Scripting


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

The `getCamera` method of the ActiveView object returns the same camera settings in a single string. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.getCamera()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewIvIssueCamPos/ru
