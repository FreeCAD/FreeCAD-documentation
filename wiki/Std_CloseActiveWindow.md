---
- GuiCommand   *
   Name   *Std CloseActiveWindow
   MenuLocation   *File → Close
   Workbenches   *All
   Shortcut   ***Ctrl**+**F4**
   SeeAlso   *[Std CloseAllWindows](Std_CloseAllWindows.md)
---

# Std CloseActiveWindow

## Description

The **Std CloseActiveWindow** command closes the active window. To close a document all its windows must be closed.

## Usage

1.  There are several ways to invoke the command   *
    -   Select the **File → <img src="images/Std_CloseActiveWindow.svg" width=16px> Close** option from the menu.
    -   Use the keyboard shortcut   * **Ctrl**+**F4**.
2.  To close a document   * repeat this for all windows belonging to it.
3.  When closing the last window of a document that has not been saved, a dialog box will prompt you to save it   *
    -   Press the **Save** button to save the document. If required enter a filename first.
    -   Press the **Discard** button to discard the document and lose all changes.

## Options

-   When the dialog box is displayed   * press **Esc** or the **Cancel** button to abort the command.

## Notes

-   The command can only close [docked](Std_ViewDockUndockFullscreen.md) windows.
-   A document can also be closed by right-clicking it in the [Tree view](Tree_view.md) and selecting **Close document** from the context menu.

## Preferences

-   The last used file location is stored   * **Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath**.

## Scripting


**See also   ***

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To close a document use the `closeDocument` method of the FreeCAD application. For a scripting example see [Std New](Std_New.md).




 {{Std Base navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std CloseActiveWindow
