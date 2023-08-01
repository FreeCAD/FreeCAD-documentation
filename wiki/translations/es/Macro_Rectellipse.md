# Macro Rectellipse/es
{{Macro/es
|Name=Rectellipse Macro
|Icon=Macro_Rectellipse.png
|Translate=Rectellipse Macro
|Description=Crea una rectelipse paramétrica
|Author=fcaponi78
|Version=1.0
|Date=2013-12-24
|FCVersion=Todas
|Download=[https://www.freecadweb.org/wiki/images/b/bf/Macro_Rectellipse.png ToolBar Icon]
}}

## Descripción

Crea un rectellipse paramétrico.

![](images/Rectellipse.png )

## Script

ToolBar Icon ![](images/Macro_Rectellipse.png )

**Macro_Rectellipse.FCMacro**


{{MacroCode|code=
from __future__ import division # allows floating point division from integers
import FreeCAD, Part, math
from FreeCAD import Base

class RectEllipseShape:
   def __init__(self, obj):
      ''' Add the properties: Radius, Eccentricity, Height, Segments (see Property View) '''
      obj.addProperty("App::PropertyLength","a","Rectellipse","A - horizontal radius").a = 16.0
      obj.addProperty("App::PropertyLength","b","Rectellipse","B - vertical radius").b = 9.0
      obj.addProperty("App::PropertyFloat","n","Rectellipse","N ").n=0.2
      obj.addProperty("App::PropertyBool","createFace","Rectellipse","Wheter to create a face or not").createFace=True
      obj.Proxy = self

   def onChanged(self, fp, prop):
      if prop == "a" or prop == "b" or prop == "n" or prop == "segments" or prop == "height" or prop == "createFace":
         #if one of these is changed
         self.execute(fp)

   def execute(self, fp):
      r1=fp.a
      r2=fp.b
      s=fp.n
      z=0.0
      p=1.0
      ####w=2**0.5/2.0 #Ellipse
      w=2**0.5/2.0/(1-s**p)
      curve=Part.BSplineCurve()
      curve.setPeriodic()
      curve.increaseDegree(2) #quadratic
      curve.insertKnots([i*1.0/(4) for i in (1,2,3)],[2]*(3)) #5Knots 8 Poles
      curve.setPole(1,FreeCAD.Vector(0,-r2,z),1)
      curve.setPole(2,FreeCAD.Vector(-r1,-r2,z),w)
      curve.setPole(3,FreeCAD.Vector(-r1,0,z),1)
      curve.setPole(4,FreeCAD.Vector(-r1,r2,z),w)
      curve.setPole(5,FreeCAD.Vector(0,r2,z),1)
      curve.setPole(6,FreeCAD.Vector(r1,r2,z),w)
      curve.setPole(7,FreeCAD.Vector(r1,0,z),1)
      curve.setPole(8,FreeCAD.Vector(r1,-r2,z),w)
      if fp.createFace == True:
         fp.Shape = Part.Face(Part.Wire(curve.toShape()))
      else:
         fp.Shape = curve.toShape()

def makeRectellipseBlock():
   doc = FreeCAD.activeDocument()
   if doc == None:
      doc = FreeCAD.newDocument()
   obj=doc.addObject("Part::FeaturePython","RectEllipseShape") #add object to document
   obj.Label = "RectEllipsse"
   RectEllipseShape(obj)
   obj.ViewObject.Proxy=0
   viewObject = Gui.ActiveDocument.getObject(obj.Name)
   viewObject.ShapeColor = (0.00,0.33,1.00)
   viewObject.DisplayMode = "Flat Lines"
   obj.Shape.check()

if __name__ == "__main__":
   #feature will be generated after macro execution
   makeRectellipseBlock()

}}

## Enlazar

[Get the code from Github here!](https://github.com/FreeCAD/FreeCAD-macros/blob/master/ParametricObjectCreation/Rectellipse.FCMacro)



---
⏵ [documentation index](../README.md) > Macro Rectellipse/es
