---
 GuiCommand:
   Name: Std SaveCopy
   MenuLocation: File , Save a Copy...
   Workbenches: All
   SeeAlso: Std_SaveAs, Std_Save
---

# Std SaveCopy/en

## Description

The **Std SaveCopy** command saves a copy of the active document under a new file name.

## Usage

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
⏵ [documentation index](../README.md) > Std SaveCopy/en
