---
 GuiCommand:
   Name/ru: Изометрическая
   Name: Std_ViewIsometric
   MenuLocation: Вид , Стандартные виды‏‎ , Axonometric , Изометрическая
   Workbenches: Все
   Shortcut: **0**
   SeeAlso: Std_ViewDimetric/ru, Std_ViewTrimetric/ru
---

# Std ViewIsometric/ru



## Описание

Команда **Std ViewIsometric** перестраивает камеру в активном [окне трёхмерного вида](3D_view/ru.md) для получения [изометрического](https://en.wikipedia.org/wiki/Isometric_projection) вида. Для истинно изометрического вида трехмерный вид должен находиться в [ортогональном режиме](Std_OrthographicCamera/ru.md), но команда также работает, если вид находится в [режиме перспективы](Std_PerspectiveCamera/ru.md).

![](images/Std_ViewIsometric_example.svg ) 
*The [axis cross](Std_AxisCross.md) and a cube in isometric view*



## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_ViewIsometric.svg" width=16px> [Isometric](Std_ViewIsometric.md)** button.
    -   Select the **View → Standard views → Axonometric → <img src="images/Std_ViewIsometric.svg" width=16px> Isometric** option from the menu.
    -   Select the **Standard views → <img src="images/Std_ViewIsometric.svg" width=16px> Isometric** option from the [3D view](3D_view.md) context menu.
    -   Select the **<img src="images/Std_ViewIsometric.svg" width=16px> Isometric** option from the Mini-cube menu of the [Navigation Cube](Navigation_Cube.md).
    -   Use the keyboard shortcut: **0**.



## Программирование


<div class="mw-translate-fuzzy">


**Смотрите так же:**

[Основы составления скриптов в FreeCAD](FreeCAD_Scripting_Basics/ru.md).


</div>

Use the `viewIsometric` method of the View object to change to isometric view. The `viewDimetric` and `viewTrimetric` methods are also available.


```python
import FreeCADGui

view = FreeCADGui.ActiveDocument.ActiveView
view.viewIsometric()
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > Std ViewIsometric/ru
