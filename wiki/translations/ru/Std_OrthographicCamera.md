---
 GuiCommand:
   Name/ru: Ортогональная проекция
   Name: Std_OrthographicCamera
   MenuLocation: Вид , Ортогональная проекция
   Workbenches: Все
   Shortcut: **V** **O**
   SeeAlso: Std_PerspectiveCamera/ru
---

# Std OrthographicCamera/ru


</div>



## Описание

Команда **Std OrthographicCamera** переводит камеру в активном [трёхмерном виде](3D_view/ru.md) в режим ортогональной проекции. В этом режиме объекты, которые находятся дальше от камеры, выглядят не меньше, чем те, которые находятся ближе.

![](images/Std_OrthographicCamera_example.svg ) 
*Два куба с одинаковыми размерами в ортогональной проекции*



## Применение


<div class="mw-translate-fuzzy">

1.  Есть несколько способов вызвать команду:
    -   Выберите в меню опцию **Вид → <img src="images/Std_PerspectiveCamera.svg" width=16px> Ортогональная проекция**.
    -   Используйте клавиатурное сокращение: **V**, затем **O**.


</div>



## Настройки

See also: [Preferences Editor](Preferences_Editor.md).

-   The camera type can be changed: **Edit → Preferences... → Display → 3D View → Camera type**. The selected type will be used for all 3D views of all opened documents and also for new documents.



## Программирование


<div class="mw-translate-fuzzy">


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).


</div>


<div class="mw-translate-fuzzy">

Чтобы изменить вид на ортографический, используйте метод `setCameraType` объекта ActiveView. Этот метод не доступен, когда FreeCAD в режиме консоли.


</div>


```python
import FreeCADGui

view = FreeCADGui.ActiveDocument.ActiveView
view.setCameraType("Perspective")
view.setCameraType("Orthographic")
view.getCameraType()
```



---
⏵ [documentation index](../README.md) > Std OrthographicCamera/ru
