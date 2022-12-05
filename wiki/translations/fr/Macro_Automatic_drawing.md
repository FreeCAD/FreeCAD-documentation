# Macro Automatic drawing/fr
{{Macro/fr
|Name=Automatic drawing
|Icon=Macro_Automatic_drawing.png
|Description=Ce script permet de générer une mise en plan avec 4 vues (face, dessus, iso et droite). Il requiert des modifications pour être parfaitement fonctionnel.
|Author=inconnu
|Version=1.0
|Date=2016-09-26
|FCVersion=Toutes version utilisant Drawing Workbench
|Download=[https://www.freecadweb.org/wiki/images/0/08/Macro_Automatic_drawing.png Icône de la barre d'outils]
}}

## Description

Ce script génère une [mise en plan](Drawing_Workbench/fr.md) incluant trois vues orthographiques (face, dessus et droite) alignées, ainsi qu\'une vue isométrique placée à la droite de la page. Le script calcule l\'échelle à partir de la taille du modèle 3D et de l\'espace disponible sur la feuille. La vue iso est dimensionnée à 2/3 de l\'échelle des vues ortho. La [projection européenne](http://fr.wikipedia.org/wiki/Dessin_technique#Correspondance_des_vues) est utilisée.

## Utilisation

Un objet doit être sélectionné avant de lancer la macro.

## Limitations

-   L\'échelle obtenue n\'est pas standard. Il faudra changer manuellement l\'échelle des vues pour une échelle standard.
-   Le script ne fonctionne qu\'avec un seul objet à la fois (ceci est une limitation de l\'atelier de Mise en plan)
-   Nécessite des modifications afin de générer une [projection américaine](http://fr.wikipedia.org/wiki/Dessin_technique#Correspondance_des_vues) telle qu\'utilisé aux États-Unis et au Canada.

## Le script 

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




## Links

The forum [Automatic drawing](https://forum.freecadweb.org/viewtopic.php?f=8&t=3361)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Automatic drawing/fr
