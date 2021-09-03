---
- GuiCommand:/ru
   Name:Std OrthographicCamera
   Name/ru:Std OrthographicCamera
   MenuLocation:Вид → Параллельная проекция
   Workbenches:All
   Shortcut:**V** **O**
   SeeAlso:[Перспективная проекция](Std_PerspectiveCamera/ru.md)
---

## Описание

Команда **Std OrthographicCamera** переводит камеру в активном [трёхмерном виде](3D_view/ru.md) в режим ортогональной проекции. В этом режиме объекты, которые находятся дальше от камеры, выглядят не меньше, чем те, которые находятся ближе.

![](images/Std_OrthographicCamera_example.svg ) *Два куба с одинаковыми размерами в ортогональной проекции*

## Применение

1.  Есть несколько способов вызвать команду:
    -   Выберите в меню опцию {{MenuCommand|Вид → <img src="images/Std_PerspectiveCamera.svg" width=16px> Ортогональная проекция}}.
    -   Используйте клавиатурное сокращение: **V**, затем **O**.

## Примечания

-   It is also possible to switch to orthographic view mode via the Mini-cube menu of the [Navigation Cube](Navigation_Cube.md).

## Настройки

-   The camera type can be changed in the preferences: {{MenuCommand|Edit → Preferences... → Display → 3D View → Camera type}}. The selected type will be used for all 3D views of all opened documents and also for new documents. See [Preferences Editor](Preferences_Editor#3D_View.md).

## Scripting


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).

Чтобы изменить вид на ортографический, используйте метод `setCameraType` объекта ActiveView. Этот метод не доступен, когда FreeCAD в режиме консоли.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setCameraType('Orthographic')
FreeCADGui.ActiveDocument.ActiveView.getCameraType()
```





{{Std Base navi

}}  
