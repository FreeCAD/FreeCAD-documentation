# Macro Colorize
{{Macro
|Name=Colorize
|Icon=Workbench_Image.svg
|Description=Quickly and easily set colors of individual faces, edges, and vertices, including transparency
|Author=TheMarkster
|Version=1.02
|Date=2021-12-12
|FCVersion=python3 builds
|Download=[https://wiki.freecadweb.org/images/d/de/Workbench_Image.svg ToolBar Icon]
}}

## Description

Allows to quickly and easily set the colors and transparency levels for individual faces, edges, and vertices. Usage: Select the subobjects and run the macro. The standard Qt color picker dialog will appear. Select the color and set the desired alpha (0 = fully opaque, 255 = fully transparent), click OK to close the dialog and use the color, or Cancel to cancel the macro. If more than one object is selected a different dialog will appear for each object.

The current color of the first selected subobject of the current object will be the default color in the dialog. The first 2 custom colors will be the default gray for faces and the default black for edges and points. Alpha channel default will be 0 (no transparency).

Notes: You may color any edge, vertex, or face any color you like, but bear in mind you should probably stay away from the default colors used for selection (green) and preselection (yellow) indicators. Transparency option does not appear to function for edges and points, only for faces. When making a face transparent, it is still selectable in the 3D view. If the interior appears black and you would prefer to see the face colors set in the view tab the Lighting property from One side to Two side. Transparency is a global property for the entire object, so if you change it in the view tab it will override the transparency settings made for individual faces using this macro.

## Script

ToolBar Icon ![](images/Workbench_Image.svg )

 **Macro\_Colorize.FCMacro**


{{MacroCode|code=

# -*- coding: utf-8 -*-
#Colorize macro, 2021, by <TheMarkster> LGPL2.1 or later
#Usage: Select subobjects, run macro
#A color picker dialog will appear
#Select the color for the selected subobjects.
#The alpha channel corresponds to the transparency
# 0 = no transparency, 255 = full transparency
# first 2 custom colors are the default gray and black
# used for faces and edges/points

__version__ = "1.02"
from PySide import QtGui,QtCore
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class ColorDlg (QtGui.QColorDialog):
    def __init__(self,title,flags):
        QtGui.QColorDialog.__init__(self)
        self.title = title
        self.flags = flags

    def getClr(self, currentColor):
        current = QtGui.QColor(currentColor[0]*255,currentColor[1]*255,currentColor[2]*255,currentColor[3]*255)
        self.setCustomColor(0,QtGui.QColor.fromRgb(204,204,204,0)) # gray, default face color
        self.setCustomColor(2,QtGui.QColor.fromRgb(0,0,0,0)) #black, default line and point color
        clr = self.getColor(current,None,self.title, self.flags)
        return clr

def getIdx(sen):
    '''get subelement index from sub element name, e.g. from "Face6"  we get 5'''
    if 'Face' in sen or 'Edge' in sen or 'Wire' in sen:
        val = int(sen[4:])
    elif 'Vertex' in sen:
        val = int(sen[6:])
    return val-1

def buildDefaultColorArray(color, count):
    clr = (color[0],color[1],color[2],0.0)
    return[clr] * count

def getCurrentColor(obj,subName):
    idx = getIdx(subName)
    if "Face" in subName:
        ary = obj.ViewObject.DiffuseColor
    elif "Edge" in subName:
        ary = obj.ViewObject.LineColorArray
    elif "Vertex" in subName:
        ary = obj.ViewObject.PointColorArray
    if len(ary) >= idx:
        return ary[idx]
    else:
        return ary[0]


def setColors():
    selx = Gui.Selection.getSelectionEx()
    for sel in selx:
        if sel.HasSubObjects:
            defaultColor = QtCore.Qt.gray if "Face" in sel.SubElementNames[0] else QtCore.Qt.black
            currentColor = getCurrentColor(sel.Object,sel.SubElementNames[0])
            subs = sel.SubElementNames
            faces = [name for name in subs if "Face" in name]
            edges = [name for name in subs if "Edge" in name]
            vertices = [name for name in subs if "Vertex" in name]
            objname = sel.Object.Name
            if sel.Object.Name != sel.Object.Label:
                objname += " ("+sel.Object.Label+")"
            dlg = ColorDlg('Colorize v'+__version__+' object: '+objname,QtGui.QColorDialog.ShowAlphaChannel.__or__(QtGui.QColorDialog.DontUseNativeDialog))
            col = dlg.getClr(currentColor)
            if not col.isValid(): #user canceled
                return
            col = col.getRgbF()

            if faces:
                dc = sel.Object.ViewObject.DiffuseColor
                if len(dc) == 1:
                    dc = buildDefaultColorArray(dc[0], len(sel.Object.Shape.Faces))
                indices = [getIdx(name) for name in faces]
                for idx in indices:
                    dc[idx] = col
                sel.Object.ViewObject.DiffuseColor = dc
            if edges:
                lca = sel.Object.ViewObject.LineColorArray
                if len(lca) == 1:
                    lca = buildDefaultColorArray(lca[0], len(sel.Object.Shape.Edges))
                indices = [getIdx(name) for name in edges]
                for idx in indices:
                    lca[idx] = col
                sel.Object.ViewObject.LineColorArray = lca

            if vertices:
                pca = sel.Object.ViewObject.PointColorArray
                if len(pca) == 1:
                    pca = buildDefaultColorArray(pca[0], len(sel.Object.Shape.Vertexes))
                indices = [getIdx(name) for name in vertices]
                for idx in indices:
                    pca[idx] = col
                sel.Object.ViewObject.PointColorArray = pca

        else:
            FreeCAD.Console.PrintError("No subobjects selected\n")

setColors()
}}

---
[documentation index](../README.md) > Macro Colorize
