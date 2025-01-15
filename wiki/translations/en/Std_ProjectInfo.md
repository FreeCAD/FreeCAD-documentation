---
 GuiCommand:
   Name: Std ProjectInfo
   MenuLocation: File , Document information...
   Workbenches: All
   SeeAlso: Std_New
---

# Std ProjectInfo/en

## Description

The **Std ProjectInfo** command shows a dialog box with details of the active document. Some of this information can be edited.

## Usage

1.  Select the **File → <img src="images/Std_ProjectInfo.svg" width=16px> Document information...** option from the menu.
2.  A dialog box with the following information pops up:
    -   **Name**: The name of the document. Corresponds to the Label property of the document. *Not editable.*
    -   **Path**: The full path of the file. Blank if the file has not been saved. *Not editable.*
    -   **UUID**: FreeCAD automatically enters a checksum value. *Not editable.*
    -   **Program version**: The FreeCAD version used to save the file. Blank if the file has not been saved. *Not editable.*
    -   **Unit System**: The document unit system. *Initial value depends on the [Default unit system](Preferences_Editor#General_2.md).* <small>(v1.0)</small> 
    -   **Created by**: Enter an author name. *Can be preset.*
    -   **Creation date**: FreeCAD automatically enters the correct date. *Not editable.*
    -   **Last modified by**: Enter an author name. *Can be preset.*
    -   **Last modification date**: FreeCAD automatically enters the correct date. *Not editable.*
    -   **Company**: Enter a company name. *Can be preset.*
    -   **License information**: Select a license from the pulldown menu. *Can be preset.*
    -   **License URL**: The URL will change with the selected license, but can be overwritten. *Can be preset.*
    -   **Comment**: Enter any comment that may apply.
3.  Enter the required information and press the **OK** button.

## Options

-   Press **Esc** or the **Cancel** button to abort the command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md).

-   Some document properties: author name, company name and license information, can be preset: **Edit → Preferences... → General → Document → Authoring and License**.



---
⏵ [documentation index](../README.md) > Std ProjectInfo/en
