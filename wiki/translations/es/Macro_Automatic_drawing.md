# Macro Automatic drawing/es

 {{Macro/es
|Name=Automatic drawing
|Translate=Automatic drawing
|Icon=Macro_Automatic_drawing.png
|Description=Este código permite al usuario poner la vista de su objeto en una hoja de dibujo con 4 posiciones diferentes (alzado,planta,isométrica,perfil derecho). Necesita algunos cambios para ser perfectamente efectiva
|Author=Normandc
|Version=1.0
|Date=2016-09-26
|FCVersion=All version using Drawing Workbench
|Download=[https://www.freecadweb.org/wiki/images/0/08/Macro_Automatic_drawing.png ToolBar icon]
}}


<div class="mw-translate-fuzzy">

## Descripción

Este código genera una Hoja de [Dibujo](Drawing_Workbench/es.md) con tres vistas ortográficas (alzado, planta y perfil derecho) alineadas entre sí, y una vista isométrica situada en la parte superior derecha de la hoja. Calcula la escala basada en el tamaño del modelo y el espacio disponible en la hoja. La vista isométrica está escalada a 2/3 de las otras.

Utiliza el [Sistema de representación europeo](http://en.wikipedia.org/wiki/Multiview_orthographic_projection#First-angle_projection).


</div>


<div class="mw-translate-fuzzy">

## Cómo se utiliza 

Es necesario seleccionar un objeto antes de ejecutar la macro.


</div>

## Limitaciones

-   La eslaca no es estándar. Puedes tener que cambiar las vistas manualmente a una escala estándar.
-   Sólo funciona con un único objeto (esta es una limitación del entorno de Dibujo)
-   Es necesario modificarla para que trabaje en el [sistema americano de representación](http://en.wikipedia.org/wiki/Multiview_orthographic_projection#Third-angle_projection) utilizado en los EE.UU. y Canada.

## Script

ToolBar icon ![](images/Macro_Automatic_drawing.png )

**Macro\_Automatic\_drawing.FCMacro**


{{MacroCode|code=

import FreeCAD, Part, Drawing
if len(Gui.Selection.getSelectionEx())>1:
   App.Console.PrintError("Warning: Only the first item is generate")
if len(Gui.Selection.getSelectionEx())==0:
   App.Console.PrintError("Warning: Need to select one item")
Piece=Gui.Selection.getSelectionEx()[0]
App.activeDocument().addObject('Drawing::FeaturePage','AutoDrawing')
App.activeDocument().AutoDrawing.Template = App.getResourceDir()+'Mod/Drawing/Templates/A3_Landscape.svg'
DH=20
DL=30
L=Piece.Object.Shape.BoundBox.XMax
H=Piece.Object.Shape.BoundBox.ZMax
P=Piece.Object.Shape.BoundBox.YMax
Sc=(400-3*DL)/(L+H)
Sc2=(250-3*DH)/(P+H)
if Sc>Sc2 : 
   Sc=Sc2
TopX=DL+Sc*L
FrontX=DL+Sc*L
RightX=2*DL+Sc*L
IsoX=2*DL+Sc*(L)
TopY=DH+Sc*P
RightY=DH+P*Sc
FrontY=2*DH+Sc*(P+H)
IsoY=2*DH+Sc*P

print TopX,RightX,TopY,FrontY

#Create topView
App.activeDocument().addObject('Drawing::FeatureViewPart','topView')
App.activeDocument().topView.Source =Piece.Object
App.activeDocument().topView.Direction = (0,0,1)
App.activeDocument().topView.Rotation=180
App.activeDocument().topView.X = TopX
App.activeDocument().topView.Y = TopY
App.activeDocument().topView.ShowHiddenLines=True
App.activeDocument().AutoDrawing.addObject(App.activeDocument().topView)
App.activeDocument().topView.Scale = Sc
#Create FrontView
App.activeDocument().addObject('Drawing::FeatureViewPart','FrontView')
App.activeDocument().FrontView.Source =Piece.Object
App.activeDocument().FrontView.Direction = (0,-1,0)
App.activeDocument().FrontView.Rotation=90
App.activeDocument().FrontView.Scale = Sc
App.activeDocument().FrontView.X = FrontX
App.activeDocument().FrontView.Y = FrontY
App.activeDocument().FrontView.ShowHiddenLines=True
App.activeDocument().AutoDrawing.addObject(App.activeDocument().FrontView)
#Create RightView
App.activeDocument().addObject('Drawing::FeatureViewPart','RightView')
App.activeDocument().RightView.Source =Piece.Object
App.activeDocument().RightView.Direction = (1,0,0)
App.activeDocument().RightView.Scale = Sc
App.activeDocument().RightView.X = RightX
App.activeDocument().RightView.Y = RightY
App.activeDocument().RightView.ShowHiddenLines=True
App.activeDocument().AutoDrawing.addObject(App.activeDocument().RightView)
#Create IsotView
App.activeDocument().addObject('Drawing::FeatureViewPart','IsoView')
App.activeDocument().IsoView.Source =Piece.Object
App.activeDocument().IsoView.Direction = (1,1,1)
App.activeDocument().IsoView.Rotation=60
App.activeDocument().IsoView.Scale = Sc*.6
App.activeDocument().IsoView.X = IsoX
App.activeDocument().IsoView.Y = IsoY
App.activeDocument().IsoView.ShowHiddenLines=True
App.activeDocument().AutoDrawing.addObject(App.activeDocument().IsoView)

}}




## Enlazar

El foro [Automatic drawing](https://forum.freecadweb.org/viewtopic.php?f=8&t=3361)
