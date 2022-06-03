# Macro Easy cutouts for Enclosure Design
{{Macro
|Name=Easy cutouts for Enclosure Design
|Icon=Macro_Easy_cutouts_for_Enclosure_Design_icon.png
|Description=This macro makes Cutouts for Enclosures in a very handy way. Just select a face of the object that is the base for the cutout and the macro will create a clone of the external outline with a margin of 0.5mm (set in the macro)<br/>{{ColoredText|#ff0000|This macro needs to be upgraded}}
|Author=maurice
|Version=0.25
|Date=2016-11-26
|FCVersion=0.16
|Download=[https   *//www.freecadweb.org/wiki/images/7/71/Macro_Easy_cutouts_for_Enclosure_Design_icon.png ToolBar Icon]
}}

## Description

This macro makes Cutouts for Enclosures in a very handy way

Just select a face of the object that is the base for the cutout and the macro will create a clone of the external outline with a margin of 0.5mm (set in the macro)

<img alt="" src=images/easy-cutouts.gif  style="width   *1000px;"> 
*Here a demo with an Arduino Uno enclosure*

## Usage

Just select a face of the object that is the base for the cutout and the macro will create a clone of the external outline with a margin of 0.5mm (set in the macro)

## Script

The Icon for you ToolBar ![](images/Macro_Easy_cutouts_for_Enclosure_Design_icon.png )



**Macro\_Easy\_cutouts\_for\_Enclosure\_Design.FCMacro**


{{MacroCode|code=
# -*- coding   * utf-8 -*-
# clone, enlarge & center clone-obj to selected obj
#
 
__title__   = "Clone-Enlarge-Center Face for cutouts"
__author__  = "maurice"
__url__     = "kicad stepup"
__version__ = "0.25"
__date__    = "11.2016"

import FreeCAD, FreeCADGui, Draft, Part, DraftTools
from FreeCAD import Base


def say(msg)   *
    FreeCAD.Console.PrintMessage(msg)
    FreeCAD.Console.PrintMessage('\n')

def sayw(msg)   *
    FreeCAD.Console.PrintWarning(msg)
    FreeCAD.Console.PrintWarning('\n')
 
def getNormal(self)   *
    return self.Object.Shape.Faces[0].normalAt(0,0)

#Init        
if Gui.ActiveDocument <> None   *
    #say (Gui.ActiveDocument)

    cx = 1  # center x -> 1  
    cy = 1  # center y -> 1 
    cz = 1  # center z -> 1 # scaleX = 1.1 # scale factor for Clone
    # scaleY = 1.1 # scale factor for Clone
    # scaleZ = 1.1 # scale factor for Clonemargin = 0.5 #margin in mm
    extrudeLenght = 10 #10mm    
    #selEx = FreeCADGui.Selection.getSelectionEx()
    sel = FreeCADGui.Selection.getSelection()#print sel[0].Label
    #objs = [selobj.Object for selobj in selEx]
    selF = FreeCADGui.Selection.getSelectionEx()#if len(Gui.Selection.getSelectionEx()[0].SubElementNames) <1   *
    #    stopif len(sel) > 0   *
        FreeCADGui.Selection.removeSelection(sel[0])
    #for o in FreeCADGui.ActiveDocument.getObjects()   *
    #    FreeCADGui.Selection.removeSelection(o.Name)
    coords = []
    j = 0
    #if len(sel) == 1   * # only 1 object selected
    #if len(selF) == 1   * # only 1 object selected
    if len(sel) > 0   *
        if len(selF[0].SubElementNames) ==1   *
            f_names=[]
            f = Draft.makeFacebinder(selF)
            f1=App.ActiveDocument.getObject(f.Name)
            face=0
            try   *
                norm = f1.Shape.Faces[0].normalAt(0,0)
                say (norm)
                face=1
            except   *
                App.Console.PrintMessage("Select ONLY one single Face of object!"+"\n")
                # stop
            if face==1   *
                l = Draft.downgrade(f,delete=False)
                k = 0; bbM = 0
                for o in l   *
                    for w in o   *
                        #print w.Name
                        f_names.append (w.Name)
                        say(w.Name)
                        if "Facebinder" not in w.Name   *
                            bb=w.Shape.BoundBox
                            bbX=float(bb.XLength)
                            bbY=float(bb.YLength)
                            bbZ=float(bb.ZLength)
                            say (str(bbX)+";"+str(bbY)+";"+str(bbZ))
                            if bbX > bbM   *
                                bbM = bbX; m = k
                            if bbY > bbM   *
                                bbM = bbY; m = k
                            if bbZ > bbM   *
                                bbM = bbZ; m = k
                        k=k+1
                print f_names
                k = 0
                #f_names=[]
                for o in l   *
                    for w in o   *
                        say(w.Name)
                        #f_names.append (w.Name)
                        if k!=m   *
                            say ( "deleting "+f_names[k] )
                            FreeCAD.ActiveDocument.removeObject(f_names[k])
                        else   *
                            FreeCADGui.ActiveDocument.getObject(f_names[k]).Visibility=False
                            f = FreeCAD.ActiveDocument.addObject('Part   *   *Extrusion', 'Extrude_for_cut')
                            f = FreeCAD.ActiveDocument.getObject(f.Name)
                            f.Base = FreeCAD.ActiveDocument.getObject(f_names[k])
                            f.Dir = norm * extrudeLenght * -1
                            f.Solid = (True)
                            f.TaperAngle = (0)
                        k=k+1        
                #FreeCAD.ActiveDocument.removeObject(f_names[len(l)])
                say( f_names )
                say( f_names[m] )
                say( bbM )
                
                FreeCADGui.Selection.addSelection(FreeCAD.ActiveDocument.getObject(f.Name))
                FreeCAD.ActiveDocument.recompute()
                
                sel = FreeCADGui.Selection.getSelection()   
                #objs = [selobj.Object for selobj in selEx]
                
                coords = []
                j = 0
                s = sel[0].Shape
                
                bb=s.BoundBox
                
                bbX=float(bb.XLength)
                bbY=float(bb.YLength)
                bbZ=float(bb.ZLength)
                # boundBox
                boundBox_ = s.BoundBox
                
                a = str(boundBox_)
                a,b = a.split('(')
                c = b.split(',')
                oripl_X = float(c[0])
                oripl_Y = float(c[1])
                oripl_Z = float(c[2])
                coords.append ([oripl_X+bbX/2, oripl_Y+bbY/2, oripl_Z+bbZ/2])
                App.Console.PrintMessage(str(boundBox_)+"\r\n")
                App.Console.PrintMessage("BBox              * "+str(bbX)+" x "+str(bbY)+" x "+str(bbZ)+"\r\n")
                App.Console.PrintMessage("Base Pos          * "+str(oripl_X)+" x "+str(oripl_Y)+" x "+str(oripl_Z)+"\r\n")
                App.Console.PrintMessage("Center Pos        * "+str(oripl_X+bbX/2)+" x "+str(oripl_Y+bbY/2)+" x "+str(oripl_Z+bbZ/2)+"\r\n")
                App.Console.PrintMessage("Coords            * "+str(coords[j])+"\r\n")
            
                #objC = FreeCAD.ActiveDocument.addObject('Part   *   *AttachableObjectPython', 'Clone_for_cut')
                #objC = FreeCAD.ActiveDocument.getObject(objC.Name)
                objC=Draft.clone(sel)
                if bbX!=0   *
                    scaleX = (bbX + 2*margin) / bbX
                else   *
                    scaleX = 1
                if bbY!=0   *
                    scaleY = (bbY + 2*margin) / bbY
                else   *
                    scaleY = 1
                if bbZ!=0   *
                    scaleZ = (bbZ + 2*margin) / bbZ
                else   *
                    scaleZ = 1
                objC.Scale = (scaleX,scaleY,scaleZ)
                #Draft.scale(objC,delta=App.Vector(scaleX,scaleY,scaleZ),center=App.Vector(0,0,0),copy=True,legacy=True)
                
                oL = sel[0].Label + "_enlarged"
                objC.Label = oL
                FreeCADGui.Selection.addSelection(objC)
                
                FreeCAD.ActiveDocument.recompute()
            
                selEx = FreeCADGui.Selection.getSelectionEx()
                objs = [selobj.Object for selobj in selEx]
                coords = []
                j = 0
                if len(objs) >= 1   *
                    for obj in objs   *
                        #s = objs[0].Shape
                        s = obj.Shape
                        
                        # boundBox
                        boundBox_ = s.BoundBox
                        boundBoxLX = boundBox_.XLength
                        boundBoxLY = boundBox_.YLength
                        boundBoxLZ = boundBox_.ZLength
                        
                        a = str(boundBox_)
                        a,b = a.split('(')
                        c = b.split(',')
                        oripl_X = float(c[0])
                        oripl_Y = float(c[1])
                        oripl_Z = float(c[2])
                        coords.append ([oripl_X+boundBox_.XLength/2, oripl_Y+boundBox_.YLength/2, oripl_Z+boundBox_.ZLength/2])
                        App.Console.PrintMessage(str(boundBox_)+"\r\n")
                        App.Console.PrintMessage("BBox              * "+str(boundBox_.XLength)+" x "+str(boundBox_.YLength)+" x "+str(boundBox_.ZLength)+"\r\n")
                        App.Console.PrintMessage("Base Pos          * "+str(oripl_X)+" x "+str(oripl_Y)+" x "+str(oripl_Z)+"\r\n")
                        App.Console.PrintMessage("Center Pos        * "+str(oripl_X+boundBox_.XLength/2)+" x "+str(oripl_Y+boundBox_.YLength/2)+" x "+str(oripl_Z+boundBox_.ZLength/2)+"\r\n")
                        App.Console.PrintMessage("Coords            * "+str(coords[j])+"\r\n")
                        if j>0   *
                            if cx==1   *
                                coordNx=coords[0][0]-coords[j][0]
                            else   *
                                coordNx=0
                            if cy==1   *
                                coordNy=coords[0][1]-coords[j][1]
                            else   *
                                coordNy=0
                            if cz==1   *
                                coordNz=coords[0][2]-coords[j][2]
                            else   *
                                coordNz=0
                            obj.Placement.move(App.Vector(coordNx,coordNy,coordNz))
                            App.Console.PrintMessage("Moved        * "+str(coordNx)+" "+str(coordNy)+" "+str(coordNz)+"\r\n")
                        j=j+1
                    
                        App.Console.PrintMessage("_____________________"+"\r\n")
                        
                    FreeCADGui.Selection.removeSelection(objs[0])
                    FreeCADGui.ActiveDocument.getObject(objs[0].Name).Visibility=False
                    FreeCADGui.ActiveDocument.getObject(objs[1].Name).Transparency=70
                    App.ActiveDocument.recompute() 
            
        else   *
            App.Console.PrintMessage("Select ONLY one single Face of object!"+"\n")
    else   *
        App.Console.PrintMessage("Select ONLY one single Face of object!"+"\n")
else   *
    sayw("no document to work with")   
    #http   *//forum.freecadweb.org/viewtopic.php?t=4625

}}



## Link

Forum    * [Easy cutouts for Enclosure Design Macro](http   *//forum.freecadweb.org/viewtopic.php?f=22&t=18488)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Easy cutouts for Enclosure Design
