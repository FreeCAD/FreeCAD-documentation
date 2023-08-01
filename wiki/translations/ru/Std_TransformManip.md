---
- GuiCommand:
   Name/ru:Преобразовать
   Name:Std_TransformManip
   MenuLocation:В контекстном меню древовидного обзора проекта - Преобразовать
Правка - Преобразовать
   Workbenches:Все
   SeeAlso:[Стандартные команды и инструменты](Std_Base/ru.md)
---

# Std TransformManip/ru



## Описание

Этот инструмент позволяет вам применять к объекту приращения поворота или приращения перемещения.

![](images/Manipulators.png )



## Применение

1.  Right-click on the object in the model [tree view](Tree_view.md). For some objects the tool is also available via double-clicking the object in the model tree.
    -   Press and hold the left mouse button on an axis arrow and drag to translate the object in that direction.
    -   Press and hold the left mouse button on a sphere and drag to rotate the object in that axis.
    -   The Increments parameters in the [Task panel](Task_panel.md) allow one to define the movement with precision
2.  The **OK** button allows you to quit the utility easily.



## Примечания

-   As soon as you rotate/move the object in the [3D view](3D_view.md), changes are applied.
-   There is no Cancel button. Pressing **OK** only serves to exit the utility.
-   It\'s possible to <img alt="" src=images/Std_Undo.svg  style="width:20px;"> [undo](Std_Undo.md) changes afterwards.
-   The value boxes are for increments, not absolute values.





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std TransformManip/ru
