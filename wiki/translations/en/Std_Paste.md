---
 GuiCommand:
   Name: Std Paste
   MenuLocation: Edit , Paste
   Workbenches: All
   Shortcut: **Ctrl**+**V**
   SeeAlso: Std_Cut, Std_Copy, Std_DuplicateSelection
---

# Std Paste/en

## Description

The **Std Paste** command pastes objects from the Clipboard into the active document.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_Paste.svg" width=16px> [Paste](Std_Paste.md)** button.
    -   Select the **Edit → <img src="images/Std_Paste.svg" width=16px> Paste** option from the menu.
    -   Select the **<img src="images/Std_Paste.svg" width=16px> Paste** option from the [Tree view](Tree_view.md) context menu. Note that this option is only available when an existing object has been selected.
    -   Use the keyboard shortcut: **Ctrl**+**V**.

## Notes

-   FreeCAD will automatically change the internal names and, depending on the preferences, labels of objects to avoid name conflicts.
-   A spreadsheet cell alias that already exists in the spreadsheet will not be pasted.
-   When you are working in a FreeCAD text window, an input box or a spreadsheet, the standard keyboard shortcut **Ctrl**+**V**, in almost all cases, does not call this command but uses the Paste function from the OS instead.
-   It is not possible to copy-paste native objects between FreeCAD and other applications.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md).

-   To allow duplicate labels check the **Edit → Preferences... → General → Document → Allow duplicate object labels in one document** option. But this is not recommended.





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std Paste/en
