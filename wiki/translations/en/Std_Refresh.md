---
- GuiCommand:
   Name: Std Refresh
   MenuLocation: Edit - Refresh
   Workbenches: All
   Shortcut: **F5**
---

# Std Refresh/en

## Description

The **Std Refresh** command recomputes the active document. The command is disabled if the document does not require a recompute.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_Refresh.svg" width=16px> [Std Refresh](Std_Refresh.md)** button.
    -   Select the **Edit → <img src="images/Std_Refresh.svg" width=16px> Refresh** option from the menu.
    -   Use the keyboard shortcut: **F5**.

## Options

-   To force a recompute select the document or one or more objects in the [Tree view](Tree_view.md), choose the **<img src="images/Std_MarkToRecompute.svg" width=16px> Mark to recompute** option from the context menu, and invoke the command.
-   For objects, but not for documents, you can also choose **Recompute object** from the same context menu.

## Notes

-   For a macro that will recompute the active document see: [Macro ForceRecompute](Macro_ForceRecompute.md).

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To recompute a document use the `recompute` method of the document object.


```python
import FreeCAD

doc = FreeCAD.newDocument()
doc.recompute()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std Refresh/en
