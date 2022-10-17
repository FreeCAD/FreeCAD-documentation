# Macro Colorize
{{Macro
|Name=Macro Colorize
|Icon=Workbench_Image.svg
|Description=Quickly and easily set the color and transparency of individual faces, edges, and vertices.
|Author=TheMarkster
|Version=1.02
|Date=2021-12-12
|FCVersion=Python3 builds
|Download=[https   *//wiki.freecadweb.org/images/d/de/Workbench_Image.svg ToolBar Icon]
}}

## Description

This macro allows to quickly and easily set the color and transparency of individual faces, edges, and vertices.

## Usage

1.  Select one or more subobjects.
2.  Run the macro.
3.  The standard Qt color dialog opens.
4.  Select the color.
5.  Set the transparency by changing the alpha channel (0 = fully opaque, 255 = fully transparent).
6.  Do one of the following   *
    -   Press the **OK** button to close the dialog and apply the color and transparency.
    -   Press the **Cancel** button to cancel the macro.
7.  If you have pressed **OK** and the subobjects belong to more than one object, the color dialog will re-open for the next object.

## Notes

-   The current color of the first selected subobject of the current object will be the default color in the dialog. The first 2 custom colors will be the default gray for faces, and the default black for edges and points. The default for the alpha channel will be 0 (no transparency).
-   You can use any color you like, but you should probably avoid the colors used for selection (default   * green) and preselection (default   * yellow) indicators.
-   The transparency option does not appear to function for edges and points, only for faces.
-   A transparent face is still selectable in the 3D view.
-   If the interior side of faces appears black and you would prefer to see the face colors, change the Lighting property of the object from One side to Two side on the View tab.
-   The Color properties and the Transparency property of an object are global properties. Changing them will override any changes made to individual subobjects.

## Script

ToolBar Icon ![](images/Workbench_Image.svg )

 **Macro_Colorize.FCMacro**


{{MacroCode|code=

# -*- coding   * utf-8 -*-
#Colorize macro, 2021, by <TheMarkster> LGPL2.1 or later
#Usage   * Select subobjects, run macro
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

class ColorDlg (QtGui.QColorDialog)   *
    def __init__(self,title,flags)   *
        QtGui.QColorDialog.__init__(self)
        self.title = title
        self.flags = flags

    def getClr(self, currentColor)   *
        current = QtGui.QColor(currentColor[0]*255,currentColor[1]*255,currentColor[2]*255,currentColor[3]*255)
        self.setCustomColor(0,QtGui.QColor.fromRgb(204,204,204,0)) # gray, default face color
        self.setCustomColor(2,QtGui.QColor.fromRgb(0,0,0,0)) #black, default line and point color
        clr = self.getColor(current,None,self.title, self.flags)
        return clr

def getIdx(sen)   *
    '''get subelement index from sub element name, e.g. from "Face6"  we get 5'''
    if 'Face' in sen or 'Edge' in sen or 'Wire' in sen   *
        val = int(sen[4   *])
    elif 'Vertex' in sen   *
        val = int(sen[6   *])
    return val-1

def buildDefaultColorArray(color, count)   *
    clr = (color[0],color[1],color[2],0.0)
    return[clr] * count

def getCurrentColor(obj,subName)   *
    idx = getIdx(subName)
    if "Face" in subName   *
        ary = obj.ViewObject.DiffuseColor
    elif "Edge" in subName   *
        ary = obj.ViewObject.LineColorArray
    elif "Vertex" in subName   *
        ary = obj.ViewObject.PointColorArray
    if len(ary) >= idx   *
        return ary[idx]
    else   *
        return ary[0]


def setColors()   *
    selx = Gui.Selection.getSelectionEx()
    for sel in selx   *
        if sel.HasSubObjects   *
            defaultColor = QtCore.Qt.gray if "Face" in sel.SubElementNames[0] else QtCore.Qt.black
            currentColor = getCurrentColor(sel.Object,sel.SubElementNames[0])
            subs = sel.SubElementNames
            faces = [name for name in subs if "Face" in name]
            edges = [name for name in subs if "Edge" in name]
            vertices = [name for name in subs if "Vertex" in name]
            objname = sel.Object.Name
            if sel.Object.Name != sel.Object.Label   *
                objname += " ("+sel.Object.Label+")"
            dlg = ColorDlg('Colorize v'+__version__+' object   * '+objname,QtGui.QColorDialog.ShowAlphaChannel.__or__(QtGui.QColorDialog.DontUseNativeDialog))
            col = dlg.getClr(currentColor)
            if not col.isValid()   * #user canceled
                return
            col = col.getRgbF()

            if faces   *
                dc = sel.Object.ViewObject.DiffuseColor
                if len(dc) == 1   *
                    dc = buildDefaultColorArray(dc[0], len(sel.Object.Shape.Faces))
                indices = [getIdx(name) for name in faces]
                for idx in indices   *
                    dc[idx] = col
                sel.Object.ViewObject.DiffuseColor = dc
            if edges   *
                lca = sel.Object.ViewObject.LineColorArray
                if len(lca) == 1   *
                    lca = buildDefaultColorArray(lca[0], len(sel.Object.Shape.Edges))
                indices = [getIdx(name) for name in edges]
                for idx in indices   *
                    lca[idx] = col
                sel.Object.ViewObject.LineColorArray = lca

            if vertices   *
                pca = sel.Object.ViewObject.PointColorArray
                if len(pca) == 1   *
                    pca = buildDefaultColorArray(pca[0], len(sel.Object.Shape.Vertexes))
                indices = [getIdx(name) for name in vertices]
                for idx in indices   *
                    pca[idx] = col
                sel.Object.ViewObject.PointColorArray = pca

        else   *
            FreeCAD.Console.PrintError("No subobjects selected\n")

setColors()
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Colorize
