# FreeCAD and Mesh Import
## Post-Import 

After import the model is (for FreeCAD), just an assembly of faces. You might want to convert the model into a shape FreeCAD can recognize and that could be altered in FreeCAD.

To do this:

1.  Switch to the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md)
2.  Select the mesh, and go to the **Part → _ button
3.  Click **OK** in the dialog
4.  Select the newly created shape
5.  Go to **Part → [Convert to solid](Part_MakeSolid.md)**
6.  Select the newly created solid
7.  Go to **Part → _ button

**Note:** The last step is not necessary, but it will clean the solid of most of its residual edges on planar and cylindrical surfaces.

## Errors

### \"cannot convert because shape is not a shell\" 

Well, your shell seems to have errors, maybe it is not closed (has holes). Since the capabilities of the mesh workbench in FreeCAD are a little limited at the moment, you might want to try examining and repairing of your model with third-party software. After doing that, you may try importing and converting of your model again.

## Third Party Programs 

-   [Meshlab](http://meshlab.sourceforge.net/)
    -   License: Open Source (GPL V2)
    -   Runs on Windows 32/64 bit, Linux and Mac OS X
-   [netFabb basic](http://www.netfabb.com/downloadcenter.php?basic=1)
    -   License: Freeware
    -   Runs on Windows XP/7/8, Linux and Mac OS X

## Tutorials

-   [Import from STL or OBJ](Import_from_STL_or_OBJ.md)
-   [Export to STL or OBJ](Export_to_STL_or_OBJ.md)

## Related

-   [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md)



_ _

---
[documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > FreeCAD and Mesh Import
