# Std Paste/de
---
- GuiCommand:/de   Name/de:Std_Paste   MenuLocation:Bearbeiten → Einfügen   Shortcut:**Strg**+**V**   Workbenches:Alle   SeeAlso:[Kopieren](Std_Copy/de.md), [Auswahl duplizieren](Std_DuplicateSelection/de.md)---


</div>


<div class="mw-translate-fuzzy">

## Beschreibung

Der Einfügen-Befehl wird bei der Replizierung von Objekten des aktuellen [Dokuments](Document_structure/de.md) verwendet. Er platziert die Objekte aus der *Zwischenablage* im aktuellen Dokument. Objekte können zwischen geöffneten Dokumenten kopiert werden.


</div>

The **Std Paste** command pastes objects from the Clipboard into the active document.


<div class="mw-translate-fuzzy">

## Anwendung

1.  Aktiviere das Zieldokument durch Anklicken im Projekt-Reiter oder dem Dokumenten-Fenster.
2.  Drücke das **_**-Piktogramm, die **Strg** + **V**-Tasten oder benutze aus der Menüleiste **Bearbeiten** → **Einfügen**.


</div>

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_Paste.svg" width=16px> [Std Paste](Std_Paste.md)** button.
    -   Select the **Edit → <img src="images/Std_Paste.svg" width=16px> Paste** option from the menu.
    -   Select the **<img src="images/Std_Paste.svg" width=16px> Paste** option from the [Tree view](Tree_view.md) context menu. Note that this option is only available when an exiting object has been selected.
    -   Use the keyboard shortcut: **Ctrl**+**V**.

## Notes

-   FreeCAD will automatically change the internal names and, depending on the preferences, labels of objects to avoid name conflicts.
-   A spreadsheet cell alias that already exists in the spreadsheet will not be pasted.
-   When you are working in a FreeCAD text window, an input box or a spreadsheet, the standard keyboard shortcut **Ctrl**+**V**, in almost all cases, does not call the **Std Paste** command but uses the Paste function from the OS instead.
-   It is not possible to copy-paste native objects between FreeCAD and other applications.

## Preferences

-   Duplicate labels are allowed if **Tools → Edit parameters... → BaseApp → Preferences → Document → DuplicateLabels** is set to `True`. This setting can also be changed in the [Preferences Editor](Preferences_Editor#Document.md).





{{Std Base navi

}}

---
[documentation index](../README.md) > Std Paste/de
