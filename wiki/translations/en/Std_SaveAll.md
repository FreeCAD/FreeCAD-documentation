---
- GuiCommand:
   Name:Std SaveAll
   MenuLocation:File → Save All
   Workbenches:All
   SeeAlso:[Std Save](Std_Save.md)
---

# Std SaveAll/en

## Description

The **Std SaveAll** command saves all open documents.

## Usage

1.  Select the **File → <img src="images/Std_SaveAll.svg" width=16px> Save All** option from the menu.
2.  For new documents: enter a filename in the dialog box and press the **Save** button.

## Options

-   For new documents: press **Esc** or the **Cancel** button to abort the command.

## Preferences

-   The last used file location is stored: **Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath**.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To save a document use the `save` method of the document object. A new document must first be saved with the `saveAs` method of the document object. For a scripting example see [Std New](Std_New.md).





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std SaveAll/en
