# Std New/ro
---
- GuiCommand:   Name:Std New   Name/ro:Std New   MenuLocation:[Workbenches:All   Shortcut:Ctrl+N   SeeAlso:[[Std Open/ro|Std Open](Std_File_Menu/ro___File]]_→_New.md),[Std Import](Std_Import/ro.md)---


</div>


<div class="mw-translate-fuzzy">

Creează un nou document gol. De asemenea, FreeCAD poate fi configurat pentru a crea un nou document gol la pornire, verificând setarea corespunzătoare din Edit → Preferences → General → Document tab.


</div>

The **Std New** command creates a new empty document and makes it the active document.

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_New.svg" width=16px> [Std New](Std_New.md)** button.
    -   Select the **File → <img src="images/Std_New.svg" width=16px> New** option from the menu.
    -   Use the keyboard shortcut: **Ctrl**+**N**.

## Preferences

-   FreeCAD will create a new document at start up if **Tools → Edit parameters... → BaseApp → Preferences → Document → CreateNewDoc** is set to `True`. This setting can also be changed in the [Preferences Editor](Preferences_Editor#Document.md).
-   Some document properties: author names, company name and license information, can be preset in the [Preferences Editor](Preferences_Editor#Document.md).

## Properties

Most properties can also be changed in the dialog box of the [Std ProjectInfo](Std_ProjectInfo.md) command.

-    **Comment**: Any comment that may apply.

-    **Company**: Company name. **Can be preset**.

-    **Created By**: Author name. **Can be preset**.

-    **Creation Date**: Automatic date stamp. **Not editable**.

-    **File Name**: The full path of the file. Blank if the document has not been saved. **Not editable**.

-    **Id**: Not implemented yet.

-    **Label**: The name that will appear in the [Tree view](Tree_view.md). By default the name of the document.

-    **Last Modified By**: Author name. **Can be preset**.

-    **Last Modified Date**: Automatic date stamp. **Not editable**.

-    **License**: License type. **Can be preset**.

-    **License URL**: License URL. **Can be preset**.

-    **Show Hidden**: If true, items that have been hidden in the [Tree view](Tree_view.md) will be displayed anyway. Hiding items in the tree can be useful when working on larger models.

-    **Tip**: Not implemented yet.

-    **Tip Name**: Not implemented yet.

-    **Transient Dir**: The transient directory used for recovery data. **Not editable**.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To create a new document use the `newDocument([name], [hidden<nowiki>=</nowiki>False])` method of the FreeCAD application. The document name must be unique, which is checked automatically. If no name is supplied, the document will be named \"Untitled\". If `hidden<nowiki>=</nowiki>True` is used, the new document won\'t be displayed in the GUI and no tab will appear for it.


```python
import FreeCAD
from pathlib import Path

# The folder and filename we will use:
fld = 'D:/testfiles/'
fnm = fld + 'test.FCStd'

# Make sure fld exists:
Path(fld).mkdir(parents=True, exist_ok=True)

doc = FreeCAD.newDocument()
doc.saveAs(fnm)

FreeCAD.closeDocument(doc.Name)

doc = FreeCAD.open(fnm)
doc.save()

FreeCAD.closeDocument(doc.Name)
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std New/ro
