---
- GuiCommand   *
   Name   *Std ProjectInfo
   MenuLocation   *File → Project information...
   Workbenches   *All
   SeeAlso   *[Std New](Std_New.md)
---

# Std ProjectInfo

## Description

The **Std ProjectInfo** command shows a dialog box with project information belonging to the active document. Some of this information can be edited.

## Usage

1.  Select the **File → <img src="images/Std_ProjectInfo.svg" width=16px> Project information...** option from the menu.
2.  A dialog box with the following information pops up   *
    -   **Name**   * The name of the document. **Not editable**. Corresponds to the Label property of the document which can be changed in the [Property editor](Property_editor.md).
    -   **Path**   * The full path of the file. Blank if the document has not been saved. **Not editable**.
    -   **UUID**   * FreeCAD automatically enters a checksum value. **Not editable**.
    -   **Created by**   * Enter an author name. **Can be preset**.
    -   **Creation date**   * FreeCAD automatically enters the correct date. **Not editable**.
    -   **Last modified by**   * Enter an author name. **Can be preset**.
    -   **Last modification date**   * FreeCAD automatically enters the correct date. **Not editable**.
    -   **Company**   * Enter a company name. **Can be preset**.
    -   **License Information**   * Select a license from the pulldown menu. **Can be preset**.
    -   **License URL**   * The URL will change with the selected license, but can be overwritten. **Can be preset**.
    -   **Comment**   * Enter any comment that may apply.
3.  Enter the required information and press the **OK** button.

## Options

-   Press **Esc** or the **Cancel** button to abort the command.

## Preferences

-   The values for the author names, company name and license information can be preset in the [Preferences Editor](Preferences_Editor#Document.md).




 {{Std Base navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ProjectInfo
