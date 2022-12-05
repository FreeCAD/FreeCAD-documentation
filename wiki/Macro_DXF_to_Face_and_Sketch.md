# Macro DXF to Face and Sketch
{{Macro
|Name=DXF to Face and Sketch
|Icon=Macro_DXF_to_Face_and_Sketch.png
|Description=This macro create face and sketch from a DXF file.
|Author=shoogen,  easyw-fc
|Version=02.00
|Date=2017-10-23
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/6/6d/Macro_DXF_to_Face_and_Sketch.png ToolBar Icon]
}}

## Description

This macro converts selected elements of imported dxf to face and sketch.

It can be used also to convert \'Shape2DView\' to Sketch and it works also if BSPlines are present.

## Uses

-   Import a DXF file
-   Select the items to be processed
-   Launch the macro, all selected objects are analysed and transformed into faces and sketches.

## Options

-   Change create_face=True or create_sketch=True to False to generate only one item

## Script



ToolBar Icon ![](images/Macro_DXF_to_Face_and_Sketch.png )

**Macro_DXF_to_Face_and_Sketch.FCMacro**


{{MacroCode|code=
##    Select the items to be processed
##    Launch the macro, all selected objects are analyzed and transformed into faces and sketches.
##    change create_face=True or create_sketch=True to False to generate only one item
## todo: fix closed curves for bsplines method

import FreeCAD,Part,Path
from PathScripts import PathUtils

import sys, os
#sys.path.append('C:\Cad\Progetti_K\3D-FreeCad-tools/')
#sys.path.append(os.path.realpath(__file__)) #workaround to test OpenSCAD2DgeomMau
#import OpenSCAD2DgeomMau #OpenSCAD2Dgeom
#reload(OpenSCAD2DgeomMau)
import OpenSCAD2Dgeom

import PySide
from PySide import QtGui, QtCore


import DraftGeomUtils
import Draft
from DraftGeomUtils import geomType

create_face=True
create_sketch=True
dqd = 0.02 #discretize(QuasiDeflection=d) => gives a list of points with a maximum deflection 'd' to the edge (faster)


def clear_console():
    #clearing previous messages
    mw=FreeCADGui.getMainWindow()
    c=mw.findChild(QtGui.QPlainTextEdit, "Python console")
    c.clear()
    r=mw.findChild(QtGui.QTextEdit, "Report view")
    r.clear()

def shape2Sketch(shape):
    # replace shape.edges with arcs
    newEdges = PathUtils.cleanedges(shape.Edges,0.1)
    wire = Part.Wire([Part.Edge(i) for i in newEdges])
    sketch = Draft.makeSketch(wire,autoconstraints=True,delete=True)
    return sketch

def Discretize(shape, addToName=None):
    ##http://forum.freecadweb.org/viewtopic.php?f=12&t=16336#p129468
    ##Discretizes the edge and returns a list of points.
    ##The function accepts keywords as argument:
    ##discretize(Number=n) => gives a list of 'n' equidistant points
    ##discretize(QuasiNumber=n) => gives a list of 'n' quasi equidistant points (is faster than the method above)
    ##discretize(Distance=d) => gives a list of equidistant points with distance 'd'
    ##discretize(Deflection=d) => gives a list of points with a maximum deflection 'd' to the edge
    ##discretize(QuasiDeflection=d) => gives a list of points with a maximum deflection 'd' to the edge (faster)
    ##discretize(Angular=a,Curvature=c,[Minimum=m]) => gives a list of points with an angular deflection of 'a'
    ##and a curvature deflection of 'c'. Optionally a minimum number of points
    ##can be set which by default is set to 2. 

    global dqd

    # lng=(abs(FreeCAD.ActiveDocument.getObject(skt_name).Shape.BoundBox.XLength)+abs(FreeCAD.ActiveDocument.getObject(skt_name).Shape.BoundBox.YLength))
    # dv=int(dvm*lng) #discretize auto setting
    # #dv=int(0.5*lng) #discretize auto setting COARSE for testing
    # #print( dv)
    # if dv < 20:
    #     dv=20
    #b=FreeCAD.ActiveDocument.getObject(skt_name)
    #l=b.Shape.copy().discretize(dv)
    #l=b.Shape.copy().discretize(QuasiDeflection=0.02)
    l=shape.copy().discretize(QuasiDeflection=dqd)
    f=Part.makePolygon(l)
    Part.show(f)
    sh_name=FreeCAD.ActiveDocument.ActiveObject.Name
    if addToName is None:
        Draft.makeSketch(FreeCAD.ActiveDocument.ActiveObject,autoconstraints=True)
    else:
        Draft.makeSketch(FreeCAD.ActiveDocument.ActiveObject,autoconstraints=True, addTo=addToName)
    s_name=FreeCAD.ActiveDocument.ActiveObject.Name
    FreeCAD.ActiveDocument.removeObject(sh_name)
    #FreeCAD.ActiveDocument.removeObject(skt_name)
    FreeCAD.ActiveDocument.recompute() 
    return s_name
    #stop

def WireDiscretize(wire):
    ##http://forum.freecadweb.org/viewtopic.php?f=12&t=16336#p129468
    ##Discretizes the edge and returns a list of points.
    ##The function accepts keywords as argument:
    ##discretize(Number=n) => gives a list of 'n' equidistant points
    ##discretize(QuasiNumber=n) => gives a list of 'n' quasi equidistant points (is faster than the method above)
    ##discretize(Distance=d) => gives a list of equidistant points with distance 'd'
    ##discretize(Deflection=d) => gives a list of points with a maximum deflection 'd' to the edge
    ##discretize(QuasiDeflection=d) => gives a list of points with a maximum deflection 'd' to the edge (faster)
    ##discretize(Angular=a,Curvature=c,[Minimum=m]) => gives a list of points with an angular deflection of 'a'
    ##and a curvature deflection of 'c'. Optionally a minimum number of points
    ##can be set which by default is set to 2. 

    global dqd

    l=wire.copy().discretize(QuasiDeflection=dqd)
    f=Part.makePolygon(l)
    Part.show(f)
    sh_name=FreeCAD.ActiveDocument.ActiveObject.Name
    FreeCAD.ActiveDocument.recompute() return sh_name
    #stop
#creating face from dxf
doc = App.ActiveDocument
clear_console()

if FreeCADGui.Selection.getSelection():

    try:
        edges=sum((obj.Shape.Edges for obj in \
        FreeCADGui.Selection.getSelection() if hasattr(obj,'Shape')),[])
        for edge in edges:
            print( "geomType ",DraftGeomUtils.geomType(edge))
        face = OpenSCAD2Dgeom.edgestofaces(edges)
        #face = OpenSCAD2DgeomMau.edgestofaces(edges)
        face.check() # reports errors
        face.fix(0,0,0)
        faceobj = doc.addObject('Part::Feature','face_%s' % "dxf")
        faceobj.Label = 'face_%s' % "dxf"
        faceobj.Shape = face
        for obj in FreeCADGui.Selection.getSelection():
            Gui.ActiveDocument.getObject(obj.Name).Visibility=False   
        #creating sketch from face from dxf
        #wires,_faces = Draft.downgrade(FreeCADGui.Selection.getSelection(),delete=False)
        if create_sketch:
            if create_face:
                wires,_faces = Draft.downgrade(faceobj,delete=False)
            else:
                wires,_faces = Draft.downgrade(faceobj,delete=True)
            if 0: #try:
                sketch = Draft.makeSketch(wires[0:1])
                sketch.Label = "Sketch_dxf"
                for wire in wires[1:]:
                    Draft.makeSketch([wire],addTo=sketch)
                for wire in wires:
                    FreeCAD.ActiveDocument.removeObject(wire.Name)
            else: #except:
                FreeCAD.Console.PrintWarning("\nConverting Bezier curves to Arcs\n")
                #FreeCAD.ActiveDocument.removeObject(FreeCAD.ActiveDocument.ActiveObject.Name)
                
                #print()
                sketchesList=[]
                #for wire in wires:
                #    for e in wire.Shape.Edges:
                #        if geomType(e) == "BSplineCurve" or geomType(e) == "BezierCurve":
                #        #if 'spline' in e.Curve:
                #            sk_name = Discretize(e)
                #            sketchesList.append(sk_name)
                #        else:
                #            sketch = Draft.makeSketch(Part.Wire(e))
                #            sketchesList.append(sketch.Name)
                #print( sketchesList)
                
                newShapeList = []
                newShapes = []
                for wire in wires:
                    for e in wire.Shape.Edges:
                        if geomType(e) == "BSplineCurve" or geomType(e) == "BezierCurve":
                        #if 'spline' in e.Curve:
                            w = Part.Wire(e)
                            w_name =WireDiscretize(w)
                            newShapeList.append(w_name)
                            wn=FreeCAD.ActiveDocument.getObject(w_name)
                            newShapes.append(wn)
                        else:
                            w = Part.Wire(e)
                            Part.show(w)
                            newShapes.append(w)
                            w_name = FreeCAD.ActiveDocument.ActiveObject.Name
                            newShapeList.append(w_name)
                            
                #print( newShapes)
                sketch = Draft.makeSketch(newShapes[0])
                FreeCAD.ActiveDocument.ActiveObject.Label="Sketch_dxf"
                for w in newShapes[1:]:
                    Draft.makeSketch([w],addTo=sketch)    
                for wire in wires:
                    FreeCAD.ActiveDocument.removeObject(wire.Name)
                for w_name in newShapeList:
                    FreeCAD.ActiveDocument.removeObject(w_name)
                
                #stop
                #WireDiscretize(wire)
                
                
                #stop
                #sk_name=FreeCAD.ActiveDocument.ActiveObject.Name
                #skObj=FreeCAD.ActiveDocument.getObject(sk_name)
                #for wire in wires[1:]:
                #    Discretize(wire.Shape,skObj)
                    
                #for wire in wires:
                #    FreeCAD.ActiveDocument.removeObject(wire.Name)
                    
                #for wire in wires[1:]:
                #    Discretize(wire.Shape,sketch)
                #for wire in wires:
                #    FreeCAD.ActiveDocument.removeObject(wire.Name)
                #for wire in wires:
                #    FreeCAD.ActiveDocument.removeObject(wire.Name)
                #sketch = shape2Sketch(face)
                #sketch = Discretize(FreeCAD.ActiveDocument.getObject(faceobj.Name).Shape)
                #sketch = Discretize(FreeCAD.ActiveDocument.getObject(f1.Name))
                
    except Part.OCCError: # Exception: #
        FreeCAD.Console.PrintError('Error in dxf %s (%s)' % (faceobj.Name,faceobj.Label)+"\n")
else:
    #FreeCAD.Console.PrintError("Select elements from dxf imported file\n")
    FreeCAD.Console.PrintWarning("Select elements from dxf imported file\n")


}}



## Link

-   Forum [Creare uno sketch partendo da un file dxf importato](http://forum.freecadweb.org/viewtopic.php?f=28&t=16686)
-   Macros_recipes [Macro Creating faces from a DXF file](http://www.freecadweb.org/wiki/index.php?title=Macros_recipes)
-   Previous version [Macro Creating faces from a DXF file](Macro_Creating_faces_from_a_DXF_file.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro DXF to Face and Sketch
