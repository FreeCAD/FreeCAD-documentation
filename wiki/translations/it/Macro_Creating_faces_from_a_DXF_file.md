# Macro Creating faces from a DXF file/it
{{Macro/it
|Name=Creating faces from a DXF file
|Icon=Macro_Creating_faces_from_a_DXF_file.png
|Translate=Facce da DXF
|Description=Questa macro crea delle facce dai file DXF.
|Author=shoogen
|Version=1.0
|Date=2014-10-29
|FCVersion=Tutte versione
|Download=[https   *//www.freecadweb.org/wiki/images/0/03/Macro_Creating_faces_from_a_DXF_file.png Icona per la ToolBar]}}

## Descrizione

Questa macro crea facce da un file DXF, i \"Layer\" sono riconosciuti separatamente e inseriti in gruppi.

Nel file ci devono essere i gruppi.

## Uso

Avviare la macro e tutti gli oggetti vengono analizzati e trasformati in facce.

Nota   * un oggetto non chiuso restituisce un errore

## Script

ToolBar Icon ![](images/Macro_Creating_faces_from_a_DXF_file.png )

**Macro_Creating_faces_from_a\_DXF_file.FCMacro**


{{MacroCode|code=
import FreeCAD,Part,OpenSCAD2Dgeom
doc = App.ActiveDocument
for group in doc.findObjects('App   *   *DocumentObjectGroup')   *
    try   *
        edges=sum((obj.Shape.Edges for obj in group.Group \
                if hasattr(obj,'Shape')),[])
        face = OpenSCAD2Dgeom.edgestofaces(edges)
        faceobj = doc.addObject('Part   *   *Feature','face_%s' % group.Name)
        faceobj.Label = 'face_%s' % group.Label
        faceobj.Shape = face
    except Part.OCCError   * # Exception   * # 
        FreeCAD.Console.PrintError('Error in Group %s (%s)' % (group.Name,group.Label)+"\n")
}}

## Link

Nel forum [Creating faces from a DXF file](http   *//forum.freecadweb.org/viewtopic.php?f=3&t=8144)

Questo è un esempio   * [Generate 3D solid from intersection of three imported 2D](http   *//forum.freecadweb.org/viewtopic.php?f=3&t=8280&p=67863#p67840)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Creating faces from a DXF file/it
