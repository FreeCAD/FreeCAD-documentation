---
 GuiCommand:
   Name/ru: Область выбора элементов
   Name: Std_BoxElementSelection
   MenuLocation: Правка , Область выбора элементов
   Workbenches: Все
   Shortcut: **Shift**+**E**
   SeeAlso: Std_BoxSelection/ru, Std_SelectAll/ru
---

# Std BoxElementSelection/ru


</div>



## Описание

The **Std BoxElementSelection** command selects faces from a user defined rectangular area, a box, in the [3D view](3D_view.md).

Note that if a whole object falls inside the rectangle, the object itself, instead of its faces, is selected. To avoid this create two box selections for each object (hold down **Ctrl** while dragging the 2nd rectangle), or use the [Part BoxSelection](Part_BoxSelection.md) command instead.



## Применение

1.  There are several ways to invoke the command:
    -   Select the **Edit → <img src="images/Std_BoxElementSelection.svg" width=16px> Box element selection** option from the menu.
    -   Use the keyboard shortcut: **Shift**+**E**.
2.  Do one of the following:
    -   Drag a rectangle from left to right to select faces whose geometric center lies inside the rectangle.
    -   Drag a rectangle from right to left to select faces that are (partially) inside the rectangle, or touched by it.



## Примечания

-   Use the [Std BoxSelection](Std_BoxSelection.md) command to box select objects instead of faces.
-   This command cannot be used to select elements in a sketch. See [Sketcher Workbench](Sketcher_Workbench#Selection_methods.md).



---
⏵ [documentation index](../README.md) > Std BoxElementSelection/ru
