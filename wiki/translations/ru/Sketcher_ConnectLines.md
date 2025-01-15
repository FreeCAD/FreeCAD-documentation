---
 GuiCommand:
   Name/ru: Соединить края
   Name: Sketcher_ConnectLines
   MenuLocation: Sketch , Инструменты для эскиза , Соединить края
   Workbenches: Sketcher_Workbench/ru
   Shortcut: **Ctrl**+**Shift**+**K**
   Version: 0.15
   SeeAlso: Sketcher_ConstrainCoincident/ru
---

# Sketcher ConnectLines/ru


</div>



## Описание

Applies [Coincident constraints](Sketcher_ConstrainCoincident.md) to endpoints with the same coordinates of the selected elements.



## Применение

1.  Select the unconnected elements in the [3D view](3D_view.md) or in the [Task panel](Task_panel.md) on the left side of the screen
2.  Invoke the command using several methods:
    -   Press the **[<img src=images/Sketcher_ConnectLines.svg style="width:16px"> [Connect edges](Sketcher_ConnectLines.md)** button.
    -   Use the **Z** then **J** keyboard shortcut.
    -   Use the **Sketch → Sketcher tools → [<img src=images/Sketcher_ConnectLines.svg style="width:16px"> Connect edges** entry from the top menu.



## Примечания

Before using this command make sure that obvious constraints (horizontal, vertical, tangential) are already applied to the elements. Selecting the elements in a counter-clock-wise order seems to produce better results.


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConnectLines/ru
