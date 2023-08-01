---
- GuiCommand:
   Name:Std SaveAs
   MenuLocation:File - Save As...
   Workbenches:All
   SeeAlso:[Std SaveCopy](Std_SaveCopy.md), [Std Save](Std_Save.md)
---

# Std SaveAs/en

## Description

The **Std SaveAs** command saves the active document under a new file name.

## Usage

1.  Select the **File → <img src="images/Std_SaveAs.svg" width=16px> Save As...** option from the menu.
2.  Enter a filename in the dialog box.
3.  Press the **Save** button.

## Options

-   Press **Esc** or the **Cancel** button to abort the command.

## Notes

-   This command can also be used to save dependency graphs. See [Std DependencyGraph](Std_DependencyGraph.md).

## Preferences

-   The last used file location is stored: **Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath**.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To save a document under a new name use the `saveAs` method of the document object. For a scripting example see [Std New](Std_New.md).





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std SaveAs/en
