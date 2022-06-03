---
- GuiCommand   *
   Name   *Std CloseAllWindows
   MenuLocation   *File → Close All
   Workbenches   *All
   SeeAlso   *[Std Close](Std_CloseActiveWindow.md)
---

# Std CloseAllWindows/ro

## Descriere

Comanda închide toate documentele proiectului, chiar și cele care nu sunt active. Cu această comandă nu ieșiți din FreeCAD.

The **Std CloseAllWindows** command closes all windows, thereby closing all documents.

## Utilizare

1.  Select the **File → <img src="images/Std_CloseAllWindows.svg" width=16px> Close All** option from the menu.
2.  If there are unsaved documents a dialog box will prompt you to save them   *
    -   Press the **Save** button to save the active document. If required enter a filename first.
    -   Press the **Discard** button to discard the active document and lose all changes.

## Options

-   When the dialog box is displayed   * press **Esc** or the **Cancel** button to abort the command.
-   If there are multiple unsaved documents   * check the {{CheckBox|TRUE|Apply answer to all}} checkbox to avoid being prompted for each unsaved document separately.

## Notes

-   A document can also be closed by right-clicking it in the [Tree view](Tree_view.md) and selecting **Close document** from the context menu.

## Preferences

-   The last used file location is stored   * **Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath**.

## Scripting


**See also   ***

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To close a document use the `closeDocument` method of the FreeCAD application. For a scripting example see [Std New](Std_New.md).





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std CloseAllWindows/ro
