---
- GuiCommand:/ru
   Name/ru:Перспективная проекция
   Name:Std_PerspectiveCamera
   MenuLocation:Вид → Перспективная проекция
   Workbenches:Все
   Shortcut:**V** **P**
   SeeAlso:[Ортогональная проекция](Std_OrthographicCamera/ru.md)
---

# Std PerspectiveCamera/ru

## Описание

Команда **Std PerspectiveCamera** переводит камеру в активном [трёхмерном виде](3D_view/ru.md) в режим перспективы. В этом режиме объекты, которые находятся дальше от камеры, выглядят меньше, чем те, которые находятся ближе.

![](images/Std_PerspectiveCamera_example.svg ) 
*Два куба с одинаковыми размерами в перспективе*

## Применение

1.  :Есть несколько способов вызвать команду:
    -   Выберите в меню опцию **Вид → <img src="images/Std_PerspectiveCamera.svg" width=16px> Перспективная проекция**.
    -   Используйте клавиатурное сокращение: **V**, затем **P**.

## Примечания

-   It is also possible to switch to perspective view mode via the Mini-cube menu of the [Navigation Cube](Navigation_Cube.md).

## Настройки

-   The camera type can be changed in the preferences: **Edit → Preferences... → Display → 3D View → Camera type**. The selected type will be used for all 3D views of all opened documents and also for new documents. See [Preferences Editor](Preferences_Editor#3D_View.md).

## Программирование


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

To change the view to perspective use the `setCameraType` method of the ActiveView object. This method is not available if FreeCAD is in console mode.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setCameraType('Perspective')
FreeCADGui.ActiveDocument.ActiveView.getCameraType()
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std PerspectiveCamera/ru
