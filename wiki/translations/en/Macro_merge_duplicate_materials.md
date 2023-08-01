# Macro merge duplicate materials/en
{{Macro
|Name=Macro merge duplicate materials
|Icon=Macro_merge_duplicate_materials.png
|Description=Merges materials that have the same base name (with different numeral endings like 001, 002,...) into one. Only the first one will be kept, and all the objects that link to the duplicates will be linking to the first one instead. So before using this macro, make sure your first material (either the one without numerical ending or the lowest number found) is the right one.
|Author=yorik
|Version=2.0
|Date=20197-07-12
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/e/ed/Macro_merge_duplicate_materials.png ToolBar Icon]
}}

## Description

Merges materials that have the same base name (with different numeral endings like 001, 002,\...) into one. Only the first one will be kept, and all the objects that link to the duplicates will be linking to the first one instead. So before using this macro, make sure your first material (either the one without numerical ending or the lowest number found) is the right one.

## Script

ToolBar Icon ![](images/Macro_merge_duplicate_materials.png )

**Merge duplicate materials.FCMacro**


{{MacroCode|code=
import FreeCAD,FreeCADGui
mats = [o for o in FreeCAD.ActiveDocument.Objects if o.isDerivedFrom("App::MaterialObject")]
todelete = []
for mat in mats:
    if mat.Label[-1].isdigit() and mat.Label[-2].isdigit() and mat.Label[-3].isdigit():
        orig = None
        for om in mats:
            if om.Label == mat.Label[:-3].strip():
                orig = om
                break
        if orig:
            for par in mat.InList:
                for prop in par.PropertiesList:
                    if getattr(par,prop) == mat:
                        print( "Changed property '"+prop+"' of object "+par.Label+" from "+mat.Label+" to "+orig.Label)
                        setattr(par,prop,orig)
            todelete.append(mat)
for tod in todelete:
    if not tod.InList:
        print( "Deleting material "+tod.Label)
        FreeCAD.ActiveDocument.removeObject(tod.Name)
    elif (len(tod.InList) == 1) and (tod.InList[0].isDerivedFrom("App::DocumentObjectGroup")):
        print( "Deleting material "+tod.Label)
        FreeCAD.ActiveDocument.removeObject(tod.Name)
    else:
        print( "Unable to delete material "+tod.Label+": InList not empty")

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro merge duplicate materials/en
