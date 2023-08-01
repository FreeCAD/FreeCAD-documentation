---
- GuiCommand:/ru
   Name:FEM ElementGeometry2D
   Name/ru:FEM ElementGeometry2D
   MenuLocation:Model →Shell plate tickness
   Workbenches:[FEM](FEM_Workbench/ru.md)
   Shortcut:**C** **S**
   SeeAlso:[FEM tutorial](FEM_tutorial/ru.md)
---

# FEM ElementGeometry2D/ru


</div>

## Описание


<div class="mw-translate-fuzzy">

ElementGeometry2D используется для определения толщины двумерных элементов МКЭ, всех или лежащих на выбранной поверхности.


</div>

## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/FEM_ElementGeometry2D.svg" width=16px> [FEM ElementGeometry2D](FEM_ElementGeometry2D.md)** button.
    -   Select the **Model → Element Geometry → <img src="images/FEM_ElementGeometry2D.svg" width=16px> Shell plate thickness** option from the menu.
2.  Define a thickness parameter.
3.  Optionally press the **Add** button in the task panel and then click on the face you want to have a prescribed thickness. If the face selection is empty, all remaining faces (whose thickness is not defined by other [FEM ElementGeometry2D](FEM_ElementGeometry2D.md) objects) will be automatically assigned.

## Ограничения

-   Анализ, объединяющий элементы оболочки с твердотельными или краевыми элементами, не поддерживается в текущей версии (FreeCAD 0.18).

## Свойства


**Thickness**

: specifies the thickness of the shell.

## Программирование

## Примечания

For viewing results from CalculiX solver on the mesh expanded to the prescribed thickness, property `Beam Shell Result Output 3D` in the [FEM SolverCalculixCxxtools](FEM_SolverCalculixCxxtools.md) need to be set to `True`.





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementGeometry2D/ru
