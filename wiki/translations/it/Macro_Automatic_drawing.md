# Macro Automatic drawing/it
{{Macro/it
|Name=Automatic drawing
|Translate=Proiezioni Automatiche
|Icon=Macro_Automatic_drawing.png
|Description=Questo codice consente di ottenere in un disegno 4 viste diverse dell'oggetto (anteriore, superiore, iso e destra). Ha bisogno di qualche modifica per essere completamente efficace.
|Author=Normandc
|Version=1.0
|Date=2016-09-26
|FCVersion=Tutte versione utilizzando Drawing Workbench
|Download=[https://www.freecadweb.org/wiki/images/0/08/Macro_Automatic_drawing.png ToolBar icon]
}}

## Descrizione

Questo codice genera una pagina di [Drawing](Drawing_Workbench/it.md) ( Disegno) con tre viste ortogonali (frontale, dall\'alto e laterale destra) allineate, più una vista isometrica posto in alto a destra della pagina. Calcola la scala basandosi sulle dimensioni del modello e sullo spazio disponibile nel foglio. La vista iso viene ridimensionata a 2/3 delle altre.

Utilizza il [first-angle projection](http://en.wikipedia.org/wiki/Multiview_orthographic_projection#First-angle_projection) ovvero il [Sistema di rappresentazione europeo](http://en.wikipedia.org/wiki/Multiview_orthographic_projection#First-angle_projection).

## Utilizzo

Prima di avviare la macro è necessario selezionare un oggetto.

## Limitazioni

-   La scala non è standard. Può essere necessario modificare manualmente la vista per adattarla ad una scala standard.
-   Funziona solo con un singolo oggetto (questa è una limitazione del Modulo Drawing)
-   Richiede delle modifiche per farla funzionare secondo il [third-angle projection](http://en.wikipedia.org/wiki/Multiview_orthographic_projection#Third-angle_projection) ovvero il [Sistema di rappresentazione americano](http://en.wikipedia.org/wiki/Multiview_orthographic_projection#Third-angle_projection) utilizzato negli Stati Uniti e in Canada.

## La macro 

ToolBar icon ![](images/Macro_Automatic_drawing.png )

**Macro_Automatic_drawing.FCMacro**


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




## Link

Nel forum [Automatic drawing](https://forum.freecadweb.org/viewtopic.php?f=8&t=3361)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Automatic drawing/it
