---
 GuiCommand:
   Name: Assembly3 MovePart
   Icon: Assembly_Move.svg
   MenuLocation: Assembly3 , Move part
   Workbenches: Assembly3_Workbench/ru
   Shortcut: **A** then **M**
---

# Assembly3 MovePart/ru

## Описание

Команда <img alt="" src=images/Assembly_Move.svg‎‎  style="width:24px;"> [Move part](Assembly3_MovePart.md) даёт инструмент для перемещения детали в контексте сборки.  Он состоит из 3 колец для вращения детали и 6 ручек (перекрещенные двойные стрелки) для перемещения детали без вращения.  Кольца и ручки располагаются и ориентируются в соответствии с неявной системой координат выбранного объекта (ICS).

<img alt="" src=images/Assembly3_MovePart.png  style="width:400px;">

## Применение

1.  Select either a face, an edge, or a vertex of the 3D part or the whole part in the assembly tree.
2.  Activate the <img alt="" src=images/Assembly_Move.svg‎‎  style="width:16px;"> **Move part** command using one of the following:
    -   The **<img src="images/Assembly_Move.svg‎‎" width=16px> [Move part](Assembly3_MovePart.md)** button.
    -   The **Assembly3 → <img src="images/Assembly_Move.svg‎‎" width=16px> Move part** menu option.
    -   The keyboard shortcut: **A** then **M**.
3.  Drag the rings and handles to reposition the part.
4.  Press **Esc** to fix the position and leave the tool.

## Примечания

The handles move the part parallel to one of the basic planes of the selected object\'s ICS; pressing and holding **shift** while dragging limits the movement to one axis.



---
⏵ [documentation index](../README.md) > Assembly3 MovePart/ru
