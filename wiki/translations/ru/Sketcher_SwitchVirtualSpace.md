---
 GuiCommand:
   Name/ru: Переключение виртуального пространства
   Name: Sketcher_SwitchVirtualSpace
   MenuLocation: Sketch , Виртуальное пространство эскиза , Переключение виртуального пространства
   Workbenches: Sketcher_Workbench/ru
   Version: 0.17
---

# Sketcher SwitchVirtualSpace/ru


</div>



## Описание

The <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width:24px;"> [Sketcher SwitchVirtualSpace](Sketcher_SwitchVirtualSpace.md) tool either (un)hides constraints or switches the visible virtual space.

A sketch has two virtual spaces that can contain constraints. All constraints are created in the main virtual space, but they can be hidden which moves them to the other virtual space.



## Применение

### (Un)hide constraints 

1.  Select one or more constraints. Constraints that are not visible in the current virtual space can be selected in the [Constraints section of the Sketcher Dialog](Sketcher_Dialog#Constraints.md).
2.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_SwitchVirtualSpace.svg" width=16px> [Switch virtual space](Sketcher_SwitchVirtualSpace.md)** button.
    -   Select the **Sketch → Sketcher visual →  <img src="images/Sketcher_SwitchVirtualSpace.svg" width=16px> Switch virtual space** option from the menu.
    -   Use the keyboard shortcut: **Z** then **Z**.

### Switch virtual space 

1.  Make sure no constraints have been selected.
2.  Invoke the tool as described above.
3.  Hidden constraints are made visible and unhidden constraints invisible, or vice versa.

## Notes

-   Constraints can also be (un)hidden from the [Sketcher Dialog](Sketcher_Dialog#Constraints.md).
-   The virtual space setting of a sketch is only used in the current session, it is not stored in the FreeCAD file.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SwitchVirtualSpace/ru
