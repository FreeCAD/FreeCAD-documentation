# Macro merge duplicate materials/it

 {{Macro/it
|Name=Macro merge duplicate materials
|Translate=Unisci materiali duplicati
|Icon=Macro_merge_duplicate_materials.png
|Description=Unisce i materiali che hanno lo stesso nome di base
|Author=yorik
|Version=2.0
|Date=20197-07-12
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/e/ed/Macro_merge_duplicate_materials.png ToolBar Icon]
}}

## Descrizione

Fonde i materiali che hanno lo stesso nome di base (con differenti terminazioni numerali come 001, 002, \...) in uno solo. Viene mantenuto solo il primo, e tutti gli oggetti che puntano ai duplicati sono invece indirizzati al primo. Quindi, prima di utilizzare questa macro, assicurarsi che il primo materiale sia quello giusto (sia quello senza finale numerico o con il numero più basso presente).

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




