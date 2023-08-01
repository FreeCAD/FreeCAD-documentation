---
- GuiCommand:
   Name:EM FHInputFile
   MenuLocation:EM → FHInputFile
   Workbenches:[EM](EM_Workbench.md)
   Shortcut:**E** **I**
   Version:0.17
   SeeAlso:[EM FHSolver](EM_FHSolver.md)
---

# EM FHInputFile

## Description

The FHInputFile tool creates the input FastHenry file based on the Document EM workbench objects.

## Usage

To create a FastHenry input file:

1.  Create one [EM FHSolver](EM_FHSolver.md) object and other EM workbench objects representing the 3D geometry as required for your model.
2.  Press the **<img src="images/EM_FHInputFile.svg" width=16px> [EM FHInputFile](EM_FHInputFile.md)** button, or press **E** then **I** keys.

### Remarks

-   In case a file with the same name in the given folder as specified in the [EM FHSolver](EM_FHSolver.md) object already exists, you will be prompted to overwrite or not.

-   The Document can also contain non-EM Workbench objects. They will be ignored when creating the FastHenry input file. So you can use any other kind of FreeCAD object as guide for your EM Workbench models.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The FHInputFile command can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:

 
```python
node = createFHInputFile(doc=None,filename=None,folder=None)
```

-   Outputs a FastHenry input file based on the active document geometry.

-    `doc`is the Document object that must contain at least one EM_FHSolver object and the relevant geometry. If no `doc` is given, the active document is used, if any.

-    `filename`is the filename to use. If not passed as an argument, the **Filename** property of the FHSolver object contained in the document will be used. If the **Folder** string in the FHSolver object is empty, the function builds a filename concatenating the document name with the default extension `EMFHSOLVER_DEF_FILENAME`.

-    `folder`is the folder where the file will be stored. If not passed as an argument, the **Folder** property of the FHSolver object contained in the document will be used. If the **Folder** string in the FHSolver object is empty, the function defaults to the user\'s home path (e.g. in Windows \"C:\\Documents and Settings\\username\\My Documents\", in Linux \"/home/username\")

Example:

 
```python
import FreeCAD, EM

fhsolver = EM.createFHInputFile()
```

 


{{EM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [EM](Category_EM.md) > EM FHInputFile
