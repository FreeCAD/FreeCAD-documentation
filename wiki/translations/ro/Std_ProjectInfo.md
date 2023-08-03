# Std ProjectInfo/ro
---
 GuiCommand:   Name: Std ProjectInfo   Name/ro: Informații despre proiect   MenuLocation: Std File Menu/ro   File , Informații despre proiect||Workbenches: All   Shortcut:    SeeAlso: ---


</div>


<div class="mw-translate-fuzzy">

## Descriere

Furnizează informații ausupra proiectului .


</div>

The **Std ProjectInfo** command shows a dialog box with project information belonging to the active document. Some of this information can be edited.


<div class="mw-translate-fuzzy">

## Utilizare

Alegeți ** File** → **Informații despre proiect...** din meniul de sus/top
Apoi, următoarele informații pot fi introduse într-o fereastră:

-   Name: (Inițial numele fișierului va fi inserat aici)
-   Path: (Inițial calea pentru salvarea fișierului va fi introdus aici)
-   UUID: o sumă de control creată de către FreeCAD va fi introdusă aici
-   Created by: inițial blanc, poate fi introdus aici manual
-   Creation date: Data și timpul creării fișierului va fi completat aici
-   Last modified by: inițial blank, poate fi introdus manual
-   Last modification date: va fi completat în FreeCAD
-   Company: inițial necompletat , poate fi introdus manual
-   License Information: alegeți tipul Licenței din pull-down-menu, Standard este \"All rights reserved\"
-   License URL: Standard este un link către wikipedia-\"All rights reserved\"-page. Poate fi supra scris.
-   Comment: inițial necompletat, poate fi introdus manual


</div>

1.  Select the **File → <img src="images/Std_ProjectInfo.svg" width=16px> Project information...** option from the menu.
2.  A dialog box with the following information pops up:
    -   **Name**: The name of the document. **Not editable**. Corresponds to the Label property of the document which can be changed in the [Property editor](Property_editor.md).
    -   **Path**: The full path of the file. Blank if the document has not been saved. **Not editable**.
    -   **UUID**: FreeCAD automatically enters a checksum value. **Not editable**.
    -   **Created by**: Enter an author name. **Can be preset**.
    -   **Creation date**: FreeCAD automatically enters the correct date. **Not editable**.
    -   **Last modified by**: Enter an author name. **Can be preset**.
    -   **Last modification date**: FreeCAD automatically enters the correct date. **Not editable**.
    -   **Company**: Enter a company name. **Can be preset**.
    -   **License Information**: Select a license from the pulldown menu. **Can be preset**.
    -   **License URL**: The URL will change with the selected license, but can be overwritten. **Can be preset**.
    -   **Comment**: Enter any comment that may apply.
3.  Enter the required information and press the **OK** button.

## Options

-   Press **Esc** or the **Cancel** button to abort the command.

## Preferences

-   The values for the author names, company name and license information can be preset in the [Preferences Editor](Preferences_Editor#Document.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ProjectInfo/ro
