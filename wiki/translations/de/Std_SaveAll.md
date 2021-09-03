---
- GuiCommand:
   Name:Std SaveAll
   MenuLocation:File → Save All
   Workbenches:All
   SeeAlso:[Std Save](Std_Save.md)
---

## Beschreibung

The **Std SaveAll** command saves all open documents.

## Anwendung

1.  Select the **File → <img src="images/Std_SaveAll.svg" width=16px> Save All** option from the menu.
2.  For new documents: enter a filename in the dialog box and press the **Save** button.

## Optionen

-   For new documents: press **Esc** or the **Cancel** button to abort the command.

## Einstellungen

-   The last used file location is stored: **Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath**.

## Skripten


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To save a document use the `save` method of the document object. A new document must first be saved with the `saveAs` method of the document object. For a scripting example see [Std New](Std_New.md).


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  
