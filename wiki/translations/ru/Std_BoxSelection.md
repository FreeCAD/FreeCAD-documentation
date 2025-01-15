---
 GuiCommand:
   Name: Std_BoxSelection
   Name/ru: Выделить область
   MenuLocation: Правка , Выделить область
   Workbenches: Все
   Shortcut: **Shift**+**B**
   SeeAlso: Std_BoxElementSelection/ru, Std_SelectAll/ru
---

# Std BoxSelection/ru



## Описание

The **Std BoxSelection** command selects objects from a user defined rectangular area, a box, in the [3D view](3D_view.md).



## Применение

1.  There are several ways to invoke the command:
    -   Select the **Edit → <img src="images/Std_BoxSelection.svg" width=16px> Box selection** option from the menu.
    -   Use the keyboard shortcut: **Shift**+**B**.
2.  Do one of the following:
    -   Drag a rectangle from left to right to select objects whose geometric center lies inside the rectangle.
    -   Drag a rectangle from right to left to select objects whose bounding box is (partially) inside the rectangle, or touches it.



## Примечания

-   Use the [Std BoxElementSelection](Std_BoxElementSelection.md) command to box select faces instead of objects.
-   This command cannot be used to select elements in a sketch. See [Sketcher Workbench](Sketcher_Workbench#Selection_methods.md).



---
⏵ [documentation index](../README.md) > Std BoxSelection/ru
