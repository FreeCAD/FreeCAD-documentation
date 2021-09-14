# Macro Automatic drawing/cs

 {{Macro/cs
|Name=Automatic drawing
|Translate=Makro Automatický výkres
|Icon=Macro_Automatic_drawing.png
|Description=Tento kód umožňuje uživateli vytvořit pohled na výkres se 4 různými pozicemi vybraného objektu (zepředu, shora, iso, zprava). Aby byl dokonale efektivní, potřeboval by ještě pár úprav.
|Author=unknown
|Version=1.0
|Date=2016-09-26
|FCVersion=All version using Drawing Workbench
|Download=[https://www.freecadweb.org/wiki/images/0/08/Macro_Automatic_drawing.png ToolBar icon]
}}


<div class="mw-translate-fuzzy">

## Description

Tento kód generuje stránku [Výkresu](Drawing_Workbench/cs.md) se třemi ortografickými vzájemně zarovnanými pohledy (zepředu, shora a zprava) a izometrický pohled umístěný vpravo nahoře stránky. Vypočítá měřítko založené na velikosti modelu a rozměru a dostupnému místu na stránce. Izo pohled je v poměru 2/3 k orto pohledům.
Používá [pravoúhlé promítání](http://en.wikipedia.org/wiki/Multiview_orthographic_projection#First-angle_projection).


</div>


<div class="mw-translate-fuzzy">

## Použití

Před spuštěním makra musí být vybrán objekt.


</div>

## Omezení

-   Měřítko není standardní. Možná budete muset měnit pohledy ručně abyste se dostali na standardní měřítko.
-   Funguje pouze s jedním objektem (to je omezení z pracovní plochy Výkres)
-   Pro použití v [third-angle projection](http://en.wikipedia.org/wiki/Multiview_orthographic_projection#Third-angle_projection) používaným v USA a Kanadě musí být provedeny určité úpravy.

## Skript

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




## Odkaz

Diskuse na fóru [Automatic drawing](https://forum.freecadweb.org/viewtopic.php?f=8&t=3361)
