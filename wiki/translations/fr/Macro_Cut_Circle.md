# Macro Cut Circle/fr
{{Macro/fr
|Name=Macro Cut Circle
|Name/fr=Macro Cut Circle
|Icon=Macro_Cut_Circle.png
|Description=Découpe les cercles ou les arcs en plusieurs arcs. Les arcs créés peuvent être colorés alternativement pour les distinguer.<br/>{{ColoredText|(Ligne de commande, coller la macro complète dans la console Python)}}.
|Author=mario52
|Version=00.03
|Date=2019-07-02
|FCVersion=Toutes
|Download=[https://wiki.freecad.org/images/9/93/Macro_Cut_Circle.png Icône de la barre d'outils]
}}

## Description

Cette macro découpe les cercles ou les arcs en plusieurs arcs. Les arcs créés peuvent être colorés alternativement pour les distinguer.

<img alt="" src=images/Macro_CutCircle_00.png  style="width:400px;"> 
*CutCircle*



## Utilisation

1.  Collez la macro **cutCirle** dans la [console Python](Python_console/fr.md).
2.  Appuyez sur **Entrée** (le code est maintenant en mémoire).
3.  Sélectionnez un ou plusieurs cercles ou arcs.
4.  Lancez la fonction {{Incode|cutCircle()}} avec 1 ou 2 arguments depuis la console Python :
    -   Exemple avec 1 argument : {{Incode|cutCircle(4)}}. Ceci créera 4 nouveaux arcs pour chaque cercle ou arc sélectionné et s\'arrêtera là (pas de coloration).
    -   Exemple avec 2 arguments : {{Incode|cutCircle(6, 1)}}. Ceci créera 6 nouveaux arcs pour chaque cercle ou arc sélectionné, colorés alternativement en rouge et blanc comme indiqué dans l\'image.
5.  L\'objet original n\'est pas supprimé.

## Script

Icône de la barre d\'outils ![](images/Macro_Cut_Circle.png )

**Macro_Cut_Circle.FCMacro**


{{MacroCode|code=

# selection circle(s) (circles and arcs)
# give number of cut, biColor 0/1
# cut the circle to x arcs
# if biColor is <> 0 the arcs are colored alternately Red White Red White ....
# 
 
__title__   = "cutCircle"
__author__  = "Mario52"
__date__    = "02/07/2019"
__version__ = "00.03"

import Draft
global biscolor ; biscolor = 0
def cutCircle(number = 2, biColor = 0):
    global biscolor
    def defbiColor(objet):
        global biscolor
        if biscolor == 0:
            FreeCADGui.ActiveDocument.getObject(objet.Name).LineColor = (1.0,0.0,0.0) # 255 = 1 (10 = (1/255 * 10 ))
            biscolor = 1
        else:
            FreeCADGui.ActiveDocument.getObject(objet.Name).LineColor = (1.0,1.0,1.0) # 255 = 1 (10 = (1/255 * 10 ))
            biscolor = 0
    selection = FreeCADGui.Selection.getSelection()
    for piece in selection:
        nom = piece.Name
        if (nom[:6] == "Circle") or (nom[:8] == "Cylinder"):
            circonference = piece.Shape.Length
            rayon = piece.Radius
            placem = piece.Placement
 
            if (nom[:8] == "Cylinder"):
                pivot0 = float(piece.Angle/number)
                FreeCAD.Console.PrintMessage("Cylinder"+"\n")
            else:
                pivot0 = float(360/number)
                FreeCAD.Console.PrintMessage("Circle"+"\n")
            pivot1 = 0.0
            for i in range(number):
                cercle = Draft.makeCircle(radius=rayon,placement=placem,face=False,startangle=(pivot1),endangle=(pivot0+pivot1),support=None)
                if biColor != 0:
                    defbiColor(cercle)
                pivot1 += pivot0
        elif nom[:3] == "Arc":
            FreeCAD.Console.PrintMessage("Arc"+"\n")
            circonference = piece.Shape.Length
            rayon = piece.Radius
            placem = piece.Placement
            First = float(piece.FirstAngle)
            Last  = float(piece.LastAngle)
            pivot0 = abs((First - Last) / number)
            pivot1 = 0.0
            for i in range(number):
                cercle = Draft.makeCircle(radius=rayon,placement=placem,face=False,startangle=(pivot1+First),endangle=(pivot0+pivot1+First),support=None)
                if biColor != 0:
                    defbiColor(cercle)
                pivot1 += pivot0
    App.ActiveDocument.recompute()

#cutCircle(5, 1)  # here with 5 arcs and colored
#cutCircle(4)     #

}}



## Exemple


```python
cutCircle(5, 1)  # here with 5 arcs and colored
cutCircle(4)     #
```



## Projet

Couper des cercles d\'un cylindre.

## Version

ver 00.03 02/07/2019 : ajout \"App.ActiveDocument.recompute()\"

ver 00.02 09/03/2015 : ajout de création des arcs colorés alternativement rouge et blanc ou non.

ver 00.01 24/02/2015 :



---
⏵ [documentation index](../README.md) > Macro Cut Circle/fr
