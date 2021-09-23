# Macro Overlap/it



<div class="mw-translate-fuzzy">


{{Macro/it
|Name=Boolean Overlap
|Translate=Sovrapposizione Booleana
|Icon=Macro_Overlap.png
|Description=Strumento booleano intermedio tra [Part Union](Part_Union/it.md) e [Part Common](Part_Common/it.md). Parametrico.
|Author=DeepSOIC
|Version=0.2
|Date=2018-08-31
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/a/ac/Macro_Overlap.png ToolBar Icon]
}}


</div>

<img alt="" src=images/Macro_Boolean_Overlap_Screenshot.png  style="width:1000px;">


<div class="mw-translate-fuzzy">

Sovrapposizione Booleana costruisce una forma che copre lo spazio occupato da non meno del \'OverlapIndex\' forme. \'OverlapIndex\' è una proprietà che può essere modificata. Il valore 1 fornisce il risultato equivalente a Part Union. Il valore pari al numero di forme rende lo strumento equivalente a Part Union. Il valore predefinito è 2, vale a dire il risultato riempie lo spazio in cui non vi è alcuna sovrapposizione.


</div>

Richiede FreeCAD v0.17+ costruito su OCC non inferiore a 6.9.0 (provato con 7.0.0).

## Installazione

Scaricare il file MacroOverlap.py e salvarlo nella directory delle macro:

<https://github.com/DeepSOIC/FreeCAD-Macros/raw/master/Overlap/MacroOverlap.py>

## Uso

1.  Selezionare tre forme\* o più per calcolare sovrapposizione tra loro. È anche possibile selezionare un singolo composto contenente le forme.
2.  In FreeCAD menu: Macro → Macros\... → doppio-click su MacroOverlap.py. Viene creato un nuovo oggetto.
3.  Selezionare il nuovo oggetto, e se necessario modificare la proprietà \'Overlap Index\' nella scheda Dati


<div class="mw-translate-fuzzy">

\* si può fare anche due forme, ma l\'azione dello strumento è equivalente a Part Common or Part Fuse, e quindi si consiglia di utilizzare gli strumenti di Part.


</div>

## Script

ToolBar Icon <img alt="" src=images/Macro_Overlap.png  style="width:64px;"> 

**MacroOverlap.py**


{{MacroCode|code=
#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2016 - Victor Titov (DeepSOIC)                          *
#*                                               <vv.titov@gmail.com>      *  
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************

__Title__ = "Macro Overlap"
__Author__ = "DeepSOIC"
__Version__ = "0.2"
__Date__    = "31/08/2018"

__Comment__ = "Extension of Part Common boolean operation"
__Web__ = "http://forum.freecadweb.org/viewtopic.php?f=8&t=17755"
__Wiki__ = "http://www.freecadweb.org/wiki/index.php?title=Macro_Boolean_Overlap"
__Status__ = "experimental"
__Requires__ = "freecad 0.17.8053 with OCC 6.9.0+"
__Communication__ = "http://www.freecadweb.org/wiki/index.php?title=User:DeepSOIC" 
__Help__ = '''
Macro Overlap.
Requires FreeCAD v0.17.8053+ and OCC 6.9.0+

Instructions:
Select three or more shapes to compute Overlap between. A single compound will do, too.
Then, run this macro. Parametric Overlap object is created.
'''

if __name__ == "__main__": #being run as a macro
    import MacroOverlap
    MacroOverlap.run()

import FreeCAD as App
if App.GuiUp:
    import FreeCADGui as Gui
import Part

def makeOverlapFeature():
    '''makeOverlapFeature(): makes a Overlap parametric feature object. Returns the new object.'''
    selfobj = App.ActiveDocument.addObject("Part::FeaturePython","Overlap")
    Overlap(selfobj)
    ViewProviderOverlap(selfobj.ViewObject)
    return selfobj

class Overlap:
    "The Overlap feature object"
    def __init__(self,selfobj):
        selfobj.addProperty("App::PropertyLinkList","Objects","Overlap","Input shape")
        selfobj.addProperty("App::PropertyInteger", "OverlapIndex", "Overlap", "minimum overlap order to output")
        selfobj.OverlapIndex = 2
        selfobj.Proxy = self

    def execute(self,selfobj):
        import BOPTools
        import BOPTools.Utils as Utils
        from BOPTools.GeneralFuseResult import GeneralFuseResult
        
        list_of_shapes = [obj.Shape for obj in selfobj.Objects]
        if len(list_of_shapes) == 1 and list_of_shapes[0].ShapeType == "Compound":
            list_of_shapes = list_of_shapes[0].childShapes()

        list_of_shapes = Utils.upgradeToAggregateIfNeeded(list_of_shapes)
        pieces, map = list_of_shapes[0].generalFuse(list_of_shapes[1:])
        gr = GeneralFuseResult(list_of_shapes, (pieces,map))
        gr.explodeCompounds()
        gr.splitAggregates()
        pieces_to_keep = []
        for piece in gr.pieces:
            if len(gr.sourcesOfPiece(piece)) >= selfobj.OverlapIndex:
                pieces_to_keep.append(piece)
        selfobj.Shape = BOPTools.ShapeMerge.mergeShapes(pieces_to_keep)

class ViewProviderOverlap:
    def __init__(self,vobj):
        vobj.Proxy = self
       
    def getIcon(self):
        return ":/icons/Part_Overlap.svg"

    def attach(self, vobj):
        self.ViewObject = vobj
        self.Object = vobj.Object
  
    def setEdit(self,vobj,mode):
        return Falsedef unsetEdit(self,vobj,mode):
        return

    def __getstate__(self):
        return None

    def __setstate__(self,state):
        return None

    def claimChildren(self):
        return self.Object.Objects
        
    def onDelete(self, feature, subelements): # subelements is a tuple of strings
        try:
            for f in self.Object.Objects:
                f.ViewObject.show()
        except Exception as err:
            App.Console.PrintError("Error in onDelete: " + err.message)
        return True

class CommandMacroOverlap:
    "Command to create Overlap feature"
    def GetResources(self):
        return {'Pixmap'  : ":/icons/Part_Overlap.svg",
                'MenuText': "Overlap",
                'Accel': "",
                'ToolTip': "Macro_Overlap: boolean overlap. Collects space filled by at least 2 shapes."}

    def Activated(self):
        run()
    def IsActive(self):
        if App.ActiveDocument:
            return True
        else:
            return False

if App.GuiUp and __name__ != "__main__":
    Gui.addCommand("Macro_Overlap", CommandMacroOverlap())

def run():
    sel = Gui.Selection.getSelectionEx()
    try:
        if len(sel) < 1:
            raise Exception("Select two shapes to compute Overlap between, first! Then run this macro.")
        try:
            App.ActiveDocument.openTransaction("Macro Overlap")
            selfobj = makeOverlapFeature()
            selfobj.Objects = [it.Object for it in sel]
            for f in selfobj.Objects:
                f.ViewObject.hide()
            
            selfobj.Proxy.execute(selfobj)
        finally:
            App.ActiveDocument.commitTransaction()
    except Exception as err:
        from PySide import QtGui
        mb = QtGui.QMessageBox()
        mb.setIcon(mb.Icon.Warning)
        mb.setText(err.message)
        mb.setWindowTitle("Macro Overlap")
        mb.exec_()
}}

