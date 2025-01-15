# Std Paste/ro
---
 GuiCommand:   Name: Std_Paste   MenuLocation: Edit , Paste   Shortcut: Ctrl+V   Workbenches: All   SeeAlso: Std_Copy, Std_DuplicateSelection---


</div>




<div class="mw-translate-fuzzy">

## Descriere

The Paste command is involved in replicating [Document](Document_structure.md) objects. It places the current \"clipboard\" contents into the current document. Objects may be copy/pasted between Documents.


</div>

The **Std Paste** command pastes objects from the Clipboard into the active document.




<div class="mw-translate-fuzzy">

## Cum se folosește 

1.  Make the target Document active by clicking on it in the Project tab or Document window.
2.  Press the **[16px|Paste](File:Std_Paste.png.md)** icon, **ctrl** + **V** keys or use menu choices Edit → Paste.


</div>

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



---
⏵ [documentation index](../README.md) > Std Paste/ro
