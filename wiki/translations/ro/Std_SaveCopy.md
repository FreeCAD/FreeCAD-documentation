# Std SaveCopy/ro
---
- GuiCommand:/ro   Name:Std SaveaCopy   Name/ro:Std SaveaCopy   MenuLocation:[Workbenches:All   Shortcut:C   SeeAlso:[[Std_Save/ro|Save](Std_File_Menu/ro___File]]_→_Save_a_Copy....md), [Save as...](Std_SaveAs/ro.md) ---


</div>

## Descriere

Salvați o copie a documentului sub un nou nume de fișier.

The **Std SaveCopy** command saves a copy of the active document under a new file name.

## Use

Alegeți ** File** → ** Save a Copy...** din meniul principal.

1.  Select the **File → <img src="images/Std_SaveCopy.svg" width=16px> Save a Copy...** option from the menu.
2.  Enter a filename in the dialog box.
3.  Press the **Save** button.

## Options

-   Press **Esc** or the **Cancel** button to abort the command.

## Preferences

-   The last used file location is stored: **Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath**.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To save a copy of a document use the `saveCopy` method of the document object.


```python
import FreeCAD
from pathlib import Path

# The folder and filename we will use:
fld = 'D:/testfiles/'
fnm = fld + 'testCopy.FCStd'

# Make sure fld exists:
Path(fld).mkdir(parents=True, exist_ok=True)

doc = FreeCAD.newDocument()
doc.saveCopy(fnm)
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std SaveCopy/ro
