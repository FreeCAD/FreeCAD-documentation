 {{Macro/it
|Name=MatrixTransform
|Icon=Macro_MatrixTransform.png
|Translate=Trasformazioni
|Description=Trasforma una forma utilizzando una matrice 3x3 (parametrica).<br/> {{ColoredText|#ff0000|#ffff00|Questa macro è composta da 2 macro: '''MatrixTransform.FCMacro''' (launcher) e '''MatrixTransform.py''' (executor).}} <br/> Il '''.FCMacro''' è installato con AddonManager, è necessario installare manualmente la macro '''.py'''. <br/> Collegamento di queste due macro: <br/> [https://github.com/DeepSOIC/FreeCAD-Macros/raw/master/MatrixTransform/MatrixTransform.FCMacro MatrixTransform.FCMacro] (launcher) <br/> [https://github.com/DeepSOIC/FreeCAD-Macros/raw/master/MatrixTransform/MatrixTransform.py MatrixTransform.py] (esecutore)
|Author=DeepSOIC
|Version=1.0
|Date=2016-05-25
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/d/db/Macro_MatrixTransform.png ToolBar Icon]
}}

## Descrizione

Applica a una forma una trasformazione lineare definita da una matrice 3x3. È possibile:

-   applicare una scalatura non lineare ad una forma
-   tosare una forma (accorciarla)
-   ruotare una forma

The transformation in the macro is linear. Lines remain straight, planes remain planar, parallel things remain parallel, only angles are distorted.


{{Codeextralink|https://raw.githubusercontent.com/DeepSOIC/FreeCAD-Macros/master/MatrixTransform/MatrixTransform.FCMacro}}

## Installazione:

Scaricare questi due file e salvarli nella directory delle macro:

<https://github.com/DeepSOIC/FreeCAD-Macros/raw/master/MatrixTransform/MatrixTransform.FCMacro>

<https://github.com/DeepSOIC/FreeCAD-Macros/raw/master/MatrixTransform/MatrixTransform.py>

## Uso:

1.  Selezionare la forma da trasformare
2.  Nel menu di FreeCAD: Macro -\> Macros\... -\> fare doppio click su MatrixTransform.FCMacro . Viene creato un nuovo oggetto.
3.  Selezionare il nuovo oggetto, e editare le proprietà v1,v2,v3 nella scheda dati per impostare la matrice di trasformazione.

La matrice è definita da tre vettori:

          v1x   v2x   v3x                  
   M = (  v1y   v2y   v3y )                  
          v1z   v2z   v3z                  

Quì, v1,v2,v3 sono vettori che possono essere definiti nelle proprietà. essi corrispondono alle nuove direzioni di quelle che erano gli assi X, Y, Z originali

### Esempi di matrici 

#### Nessuna trasformazione 

   1  0  0
   0  1  0
   0  0  1

#### Scalatura non uniforme 

   scaleX    0      0
      0   scaleY    0
      0      0   scaleZ

#### Tosatura

(operazione che fa testo normale in corsivo (italic inclinato); assumendo che il testo è nel piano XY)

   1  shear  0
   0    1    0
   0    0    1

\'Shear\' Coefficiente definisce la quantità di taglio. 0 non c\'è tosatura. 1 inclina il testo in corsivo di 45°. -1 inclna all\'indietro.

Avvertimento. Tutta la geometria viene convertita in B-spline, anche se non deve. Ciò può causare ogni sorta di guai. Utilizzare solo se assolutamente necessaria.

## Lo Script 

ToolBar Icon ![](images/Macro_MatrixTransform.png )




**MatrixTransform.py:** {{MacroCode|code=

#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2015 - Victor Titov (DeepSOIC)                          *
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

__title__="Macro MatrixTransform"
__author__ = "DeepSOIC"
__doc__ = '''
Macro MatrixTransform.
Distorts geometry according to vector transformation defined by the matrix.

Matrix is defined by three vectors:
       v1x   v2x   v3x                  
M = (  v1y   v2y   v3y )                  
       v1z   v2z   v3z                  
Here, v1,v2,v3 are vectors that can be defined in properties. They correspond
to new directions of what was originally X,Y,Z axes.

exmaple matrices:

No transformation:
1  0  0
0  1  0
0  0  1

non-uniform scaling:
scaleX    0      0
   0   scaleY    0
   0      0   scaleZ

shearing (operation that makes regular text into italic; assuming text is in XY
plane):
1  shear  0
0    1    0
0    0    1
('shear' coefficient defines the amount of shearing. 0 is no shearing. 1 makes
the text italic by 45 degrees. -1 shears in backslash-like fashion.)


Warning. All geometry is converted to B-splines, even if it doesn't have to.
This can cause all sorts of trouble. Use only if absolutely necessary.
'''

import FreeCAD as App
if App.GuiUp:
    import FreeCADGui as Gui
import Part

def makeMatrixTransformFeature():
    '''makeMatrixTransformFeature(): makes a MatrixTransform parametric feature object. Returns the new object.'''
    obj = App.ActiveDocument.addObject("Part::FeaturePython","Transform")
    MatrixTransform(obj)
    ViewProviderMatrixTransform(obj.ViewObject)
    return obj

class MatrixTransform:
    "The FuseCompound object"
    def __init__(self,obj):
        obj.addProperty("App::PropertyLink","Base","MatrixTransform","Input shape")
        obj.addProperty("App::PropertyVector","v1","MatrixTransform","Vector for new X axis; first column of transform matrix.")
        obj.addProperty("App::PropertyVector","v2","MatrixTransform","Vector for new Y axis; second column of transform matrix.")
        obj.addProperty("App::PropertyVector","v3","MatrixTransform","Vector for new Z axis; third column of transform matrix.")
        obj.v1 = App.Vector(1,0,0)
        obj.v2 = App.Vector(1,1,0)
        obj.v3 = App.Vector(0,0,1)
        obj.Proxy = self
        

    def execute(self,obj):
        v1 = obj.v1
        v2 = obj.v2
        v3 = obj.v3
        m = App.Matrix(  v1.x, v2.x, v3.x, 0,
                         v1.y, v2.y, v3.y, 0,
                         v1.z, v2.z, v3.z, 0,
                         0,    0,    0,    1   )
        obj.Shape = obj.Base.Shape.transformGeometry(m)

class ViewProviderMatrixTransform:def __init__(self,vobj):
        vobj.Proxy = self
       
    def getIcon(self):
        return ""

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
        return [self.Object.Base]
        
    def onDelete(self, feature, subelements): # subelements is a tuple of strings
        try:
            self.Object.Base.ViewObject.show()
        except Exception as err:
            App.Console.PrintError("Error in onDelete: " + err.message)
        return True

def run():
    sel = Gui.Selection.getSelection()
    try:
        if len(sel) != 1:
            raise Exception("Select a shape to transform, first! Then run this macro.")
        obj = makeMatrixTransformFeature()
        obj.Base = sel[0]
        obj.Proxy.execute(obj)
    except Exception as err:
        from PySide import QtGui
        mb = QtGui.QMessageBox()
        mb.setIcon(mb.Icon.Warning)
        mb.setText(err.message)
        mb.setWindowTitle("Macro MatrixTransform")
        mb.exec_()
}}

**Macro MatrixTransform.FCMacro**


{{MacroCode|code=
#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2015 - Victor Titov (DeepSOIC)                          *
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

__title__="Macro MatrixTransform"
__author__ = "DeepSOIC"
__doc__ = '''
Macro MatrixTransform.
Distorts geometry according to vector transformation defined by the matrix.

Matrix is defined by three vectors:
       v1x   v2x   v3x                  
M = (  v1y   v2y   v3y )                  
       v1z   v2z   v3z                  
Here, v1,v2,v3 are vectors that can be defined in properties. They correspond
to new directions of what was originally X,Y,Z axes.

exmaple matrices:

No transformation:
1  0  0
0  1  0
0  0  1

non-uniform scaling:
scaleX    0      0
   0   scaleY    0
   0      0   scaleZ

shearing (operation that makes regular text into italic; assuming text is in XY
plane):
1  shear  0
0    1    0
0    0    1
('shear' coefficient defines the amount of shearing. 0 is no shearing. 1 makes
the text italic by 45 degrees. -1 shears in backslash-like fashion.)


Instruciotns:
Select the object to be sheared, then run the macro. A new object will be
created, with shear matrix filled in by default. Edit values of v1, v2, v3 to
change the behavior.

Warning. All geometry is converted to B-splines, even if it doesn't have to.
This can cause all sorts of trouble. Use only if absolutely necessary.
'''

import MatrixTransform
MatrixTransform.run()


}}

**Run the macro**

MatrixTransform.FCMacro: 
```python
import MatrixTransform
MatrixTransform.run()
```
