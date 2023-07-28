# Scripting PartDesign Workbench
{{TOCright}}

## Introduction

Here we will explain to you how to control the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench.md) using a script. Be sure to browse the [Scripting](Scripting.md) section and the [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md) pages if you need more information about how Python scripting works in FreeCAD. If you are new to Python, it is a good idea to first read the [Introduction to Python](Introduction_to_Python.md).

This code aim to replicate the solid shown in:

<https://wiki.freecad.org/Basic_Part_Design_Tutorial_019>

Following are some preamble lines, that will ease the process.

using this code, when relaunching the script, if there is an existing document with the specified name, it will be emptied and all the objects are rebuild, avoiding to have many documents that will pollute the interface.

In case of some intermediate work, is interesting, you could always save it using **File → Save As**.

## Code Preamble 


```python
"""Script to replicate Part Design Tutorial Example.

https://wiki.freecad.org/Basic_Part_Design_Tutorial_019

This code was written for this wiki page:

https://wiki.freecad.org/Scripting_PartDesign_Workbench

Name: 20230302_pdtut_ew.py

Authors: Carlo Dormeletti - onnekk
         edwilliams16

Copyright: 2023
Licence: CC BY-NC-ND 4.0

"""
import os

import FreeCAD  # noqa
import FreeCADGui  # noqa
import Sketcher
import Part

from FreeCAD import Placement, Rotation  # noqa

V3d = FreeCAD.Vector

def activate_doc(doc_name):
    """Activate a specific document."""
    FreeCAD.setActiveDocument(doc_name)
    FreeCAD.ActiveDocument = FreeCAD.getDocument(doc_name)
    FreeCADGui.ActiveDocument = FreeCADGui.getDocument(doc_name)
    print(f"Document: {doc_name} activated")


def clear_doc(doc_name):
    """Clear the document deleting all the objects.

    Parameters:
    name       type        description
    doc_name   string      document name
    """
    doc = FreeCAD.getDocument(doc_name)
    try:
        while len(doc.Objects) > 0: 
            doc.removeObject(doc.Objects[0].Name)
    except Exception as e:
        print(f'Exception:  {e}')


def setview(doc):
    """Rearrange View."""
    try:
        doc_v = FreeCAD.Gui.activeView()
        FreeCAD.Gui.SendMsgToActiveView("ViewFit")
        doc_v.viewAxometric()
    except Exception:
        pass


def check_exist(doc_name):
    """Check the existence of a FC document named doc_name.

    If it not exist create one.
    """
    try:
        doc = FreeCAD.getDocument(doc_name)
    except NameError:
        doc = FreeCAD.newDocument(doc_name)

    return doc


# Some handy abbreviations

VEC0 = V3d(0, 0, 0)
ROT0 = Rotation(0, 0, 0)

# CODE start here

```

### See also 

-   [Part scripting](Part_scripting.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Scripting PartDesign Workbench
