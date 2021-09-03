 {{Macro
|Name=Macro Creating faces from a DXF file
|Icon=Macro_Creating_faces_from_a_DXF_file.png
|Description=This macro create face from a DXF file, the "Layer" are recognized separate and trained in groups.
|Author=shoogen
|Version=01.00
|Date=2014-10-29
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/0/03/Macro_Creating_faces_from_a_DXF_file.png ToolBar Icon]
}}

## Description

This macro create face from a DXF file, the \"Layer\" are recognized separate and trained in groups.

There must be groups in the file.

## Uses

Launch the macro all objects are analyzed and transformed into faces.

Note: an unclosed object return an error

## Script

ToolBar Icon ![](images/Macro_Creating_faces_from_a_DXF_file.png )

**Macro\_Creating\_faces\_from\_a\_DXF\_file.FCMacro**


{{MacroCode|code=
import FreeCAD,Part,OpenSCAD2Dgeom
doc = App.ActiveDocument
for group in doc.findObjects('App::DocumentObjectGroup'):
    try:
        edges=sum((obj.Shape.Edges for obj in group.Group \
                if hasattr(obj,'Shape')),[])
        face = OpenSCAD2Dgeom.edgestofaces(edges)
        faceobj = doc.addObject('Part::Feature','face_%s' % group.Name)
        faceobj.Label = 'face_%s' % group.Label
        faceobj.Shape = face
    except Part.OCCError: # Exception: # 
        FreeCAD.Console.PrintError('Error in Group %s (%s)' % (group.Name,group.Label)+"\n")
}}

## Link

Forum [Creating faces from a DXF file](http://forum.freecadweb.org/viewtopic.php?f=3&t=8144)

Here an example [Generate 3D solid from intersection of three imported 2D](http://forum.freecadweb.org/viewtopic.php?f=3&t=8280&p=67863#p67840) 
