---
- GuiCommand:
   Name: Draft SubelementHighlight
   MenuLocation: Modification - Subelement highlight
   Workbenches: [Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Shortcut: **H** **S**
   Version: 0.19
   SeeAlso: [Draft Move](Draft_Move.md), [Draft Rotate](Draft_Rotate.md), [Draft Scale](Draft_Scale.md)
---

# Draft SubelementHighlight/en

## Description

The <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:24px;"> **Draft SubelementHighlight** command temporarily highlights selected objects, or the base objects of selected objects. It is intended to be used in conjunction with the subelement mode of the [Draft Move](Draft_Move.md) command, the [Draft Rotate](Draft_Rotate.md) command or the [Draft Scale](Draft_Scale.md) command. Currently subelement mode only works properly for [Draft Lines](Draft_Line.md) and [Draft Wires](Draft_Wire.md).

![](images/Draft_SubelementHighlight_example.png ) 
*An Arch Wall whose base, a Draft Wire, has been highlighted*

## Usage

1.  Optionally select one or more [Draft Lines](Draft_Line.md) or [Draft Wires](Draft_Wire.md), or objects whose **Base** objects are [Draft Lines](Draft_Line.md) or [Draft Wires](Draft_Wire.md).
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_SubelementHighlight.svg" width=16px> [Draft SubelementHighlight](Draft_SubelementHighlight.md)** button.
    -   Select the **Modification → <img src="images/Draft_SubelementHighlight.svg" width=16px> Subelement highlight** option from the menu.
    -   Use the keyboard shortcut: **H** then **S**.
3.  If you have not yet selected an object: select an object in the [3D view](3D_view.md).
4.  The selected objects are made visible (if required), their **Line Color** and **Point Color** are changed to red, and their **Point Size** is changed to {{Value|10}}.
5.  It is advisable to now deselect the existing selection, for example by clicking a random point in the [3D view](3D_view.md).
6.  Select one or more subelements, edges or points, of the objects that have been marked in red.
7.  Invoke [Draft Move](Draft_Move.md), [Draft Rotate](Draft_Rotate.md) or [Draft Scale](Draft_Scale.md).
8.  Toggle subelement mode in the task panel of that command by checking the **Modify subelements** checkbox.
9.  Modify the selected sublements and complete the Draft modify command.
10. Press **Esc** to revert the temporary visual changes of the objects.

## Notes

-   If objects have been highlighted with this command the temporary visual changes should be reverted before saving and reopening the file.
-   Highlighted objects should not be copied if subelement mode is off. The temporary visual changes cannot be reverted for copies created in this manner.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SubelementHighlight/en
