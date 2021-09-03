---
- GuiCommand:/de
   Name:Std New
   Name/de:Std Neu
   MenuLocation:Datei → Neu
   Workbenches:Alle
   Shortcut:**Strg**+**N**
   SeeAlso:[Öffnen](Std_Open/de.md),[Import](Std_Import/de.md)
---

## Beschreibung

Der Befehl **Std Neu** erzeugt ein neues leeres Dokument und macht es zum aktiven Dokument.

## Anwendung

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Std_New.svg" width=16px> [Std New](Std_New.md)** button.
    -   Select the {{MenuCommand|File → <img src="images/Std_New.svg" width=16px> New}} option from the menu.
    -   Use the keyboard shortcut: **Ctrl**+**N**.

## Einstellungen

-   FreeCAD will create a new document at start up if {{MenuCommand|Tools → Edit parameters... → BaseApp → Preferences → Document → CreateNewDoc}} is set to `True`. This setting can also be changed in the [Preferences Editor](Preferences_Editor#Document.md).
-   Some document properties: author names, company name and license information, can be preset in the [Preferences Editor](Preferences_Editor#Document.md).

## Eigenschaften

Die meisten Eigenschaften können auch im Dialogfeld des [Std ProjektInfo](Std_ProjectInfo/de.md) Befehls geändert werden.

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

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


<div class="mw-translate-fuzzy">

Um ein neues Dokument zu erstellen, verwende die `newDocument` Methode der FreeCAD Anwendung.


</div>


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


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  
