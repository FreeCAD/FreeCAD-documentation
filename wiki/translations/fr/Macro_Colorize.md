# Macro Colorize/fr
{{Macro/fr
|Name=Macro Colorize
|Icon=Workbench_Image.svg
|Description=Définissez rapidement et facilement la couleur et la transparence des faces, arêtes et sommets individuels.
|Author=TheMarkster
|Version=1.02
|Date=2021-12-12
|FCVersion=Python3
|Download=[https://wiki.freecadweb.org/images/d/de/Workbench_Image.svg Icône de la barre d'outils]
}}

## Description

Cette macro permet de définir rapidement et facilement la couleur et la transparence des faces, arêtes et sommets individuellement.

## Utilisation

1.  Sélectionnez un ou plusieurs sous-objets.
2.  Exécutez la macro.
3.  La boîte de dialogue de couleur standard de Qt s\'ouvre.
4.  Sélectionnez la couleur.
5.  Définissez la transparence en modifiant le canal alpha (0 = totalement opaque, 255 = totalement transparent).
6.  Effectuez l\'une des opérations suivantes :
    -   Appuyez sur le bouton **OK** pour fermer la boîte de dialogue et appliquer la couleur et la transparence.
    -   Appuyez sur le bouton **Cancel** pour annuler la macro.
7.  Si vous avez appuyé sur le bouton **OK** et que les sous-objets appartiennent à plusieurs objets, la boîte de dialogue de couleur s\'ouvrira à nouveau pour l\'objet suivant.

## Remarques

-   La couleur actuelle du premier sous-objet sélectionné de l\'objet actuel sera la couleur par défaut dans le dialogue. Les deux premières couleurs personnalisées seront le gris par défaut pour les faces, et le noir par défaut pour les bords et les points. La valeur par défaut du canal alpha sera 0 (pas de transparence).
-   Vous pouvez utiliser la couleur de votre choix, mais vous devriez probablement éviter les couleurs utilisées pour les indicateurs de sélection (par défaut : vert) et de présélection (par défaut : jaune).
-   L\'option de transparence ne semble pas fonctionner pour les arêtes et les points, seulement pour les faces.
-   Une face transparente est toujours sélectionnable dans la vue 3D.
-   Si la face intérieure des faces apparaît noire et que vous préférez voir les couleurs des faces, changez la propriété Lighting de l\'objet de One side à Two side dans l\'onglet vue.
-   Les propriétés Couleur et Transparence d\'un objet sont des propriétés globales. Leur modification annule les changements apportés aux sous-objets individuels.

## Script

Icône de la barre d\'outils ![](images/Workbench_Image.svg )

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
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Colorize/fr
