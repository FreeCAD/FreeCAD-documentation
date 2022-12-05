# Macro Site From Contours/en
{{Macro
|Name=Macro Site From Contours
|Icon=Macro_Site_From_Contours.png
|Description=This macro allows you to select a series of objects containing level contours and create an Arch Site from them. The contours can be grouped in any number of objects, and don't need to form closed wires. All this will be taken care of by the macro. Internally, one bspline will be created from each contour, then ruled surfaces will be created between the contours, then these ruled surfaces will be united in a shell object, and finally an Arch Site will be created using this shell as its Terrain.
|Author=yorik
|Version=1.0
|Date=2018-08-30
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/File:Macro_Site_From_Contours.png ToolBar Icon]
}}

## Description

This macro allows you to select a series of objects containing level contours and create an Arch Site from them. The contours can be grouped in any number of objects, and don\'t need to form closed wires. All this will be taken care of by the macro. Internally, one bspline will be created from each contour, then ruled surfaces will be created between the contours, then these ruled surfaces will be united in a shell object, and finally an Arch Site will be created using this shell as its Terrain.

<img alt="" src=images/Macro_Site_From_Contour_Example.jpg  style="width:640px;">

## Script

ToolBar Icon ![](images/Macro_Site_From_Contours.png )

**Macro Site From Contours.FCMacro**


{{MacroCode|code=
# This macro builds an Arch Site object out of different level curves.
# It doesn't matter how many object contain the curves or if they
# are connected into wires or not.

import FreeCAD,FreeCADGui,Part,Draft,DraftGeomUtils,Arch

# first build a list of edges from selected objects

edges = []
for obj in FreeCADGui.Selection.getSelection():
    edges.extend(obj.Shape.Edges)

# sort our edges into connected wires

wires = DraftGeomUtils.findWires(edges)

# build a bspline for each wire

bsplines = []
for wire in wires:
    points = []
    for vert in wire.Vertexes:
        points.append(vert.Point)
    bspline = Draft.makeBSpline(points)
    bsplines.append(bspline)

# hide the bsplines

for bspline in bsplines:
    bspline.ViewObject.hide()

# sort the bsplines by elevation (we use the z of their first point to sort)

bsplines.sort(key=lambda b: b.Points[0].z)

# build one ruled surface from each pair of bsplines

ruledsurfaces = []
for i in range(len(bsplines)-1):
    ruled = FreeCAD.ActiveDocument.addObject('Part::RuledSurface', 'TerrainSection')
    ruled.Curve1 = (bsplines[i],[''])
    ruled.Curve2 = (bsplines[i+1],[''])
    ruledsurfaces.append(ruled)

# hide the ruled surfaces

for ruled in ruledsurfaces:
    ruled.ViewObject.hide()

# at this stade we need to recompute to build all the shapes before getting the faces

FreeCAD.ActiveDocument.recompute()

# make a shell object out of all the ruled surfaces

faces = []
for ruled in ruledsurfaces:
    faces.extend(ruled.Shape.Faces)
shell = Part.Shell(faces)
terrain = FreeCAD.ActiveDocument.addObject('Part::Feature', 'Terrain')
terrain.Shape = shell

# make a site object using our shell as terrain

site = Arch.makeSite()
site.Terrain = terrain

# recompute one last time

FreeCAD.ActiveDocument.recompute()
}}

## Link

The discussion forum [Create Toposurface from DXF](https://forum.freecadweb.org/viewtopic.php?f=3&t=30569)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Site From Contours/en
