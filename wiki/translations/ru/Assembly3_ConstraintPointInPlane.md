---
 GuiCommand:
   Name/ru: Assembly3 ConstraintPointInPlane
   Icon: Assembly_ConstraintPointInPlane.svg
   Workbenches: Assembly3_Workbench/ru
---

# Assembly3 ConstraintPointInPlane/ru

## Описание

Этот инструмент создает связь между двумя объектами сборки и фиксирует расстояние между ними и ориентацию друг относительно друга. Выбранные элементы каждого объекта или, точнее, их неявные системы координат (ICS) используются для позиционирования одного объекта относительно другого.

Если первый объект уже заблокирован на месте через <img alt="" src=images/Assembly_ConstraintLock.svg‎‎  style="width:24px;"> [ограничение Lock](Assembly3_ConstraintLock.md), то следующий объект перемещается в положение, в котором начало координат точечного элемента лежит на плоскости xy элемента плоской грани.

Point elements have no stretch in any direction (zero length) and so there\'s no orientation detectable i.e. their ICS are only to match other elements\' settings. The orientation of the ICSs always stays the same as the global coordinate system\'s orientation and can not be used to reduce any degrees of freedom related to rotation.

Related to the first object the following object can still move along the x- and y-axis and spin around all three axes. This is leaving 5 degrees of freedom (DOFs) for each link unconstrained.

## Применение

1.  Place two objects into an assembly.
2.  Select one point element of one object and one planar face element of the other object.
3.  Press the **<img src="images/Assembly_ConstraintPointInPlane.svg" width=16px> [Point on plane](Assembly3_ConstraintPointInPlane.md)** button.



---
⏵ [documentation index](../README.md) > Assembly3 ConstraintPointInPlane/ru
