# Macro Constraint Draft/fr
{{Macro/fr
|Name=Constraint Draft
|Icon=Macro_Constraint_Draft.png
|Description=Crée une simulation en utilisant les [expressions](Expressions/fr.md) qui servent à lier les objets entre eux (La macro fonctionne avec FreeCAD version 16).
|Author=Mario52
|Version=1.0
|Date=2017-04-19
|FCVersion=0.16
|Download=Le fichier exemple [http://forum.freecadweb.org/download/file.php?id=36559 Constraint_Draft00.FCStd]<br />[https://www.freecadweb.org/wiki/images/d/d8/Macro_Constraint_Draft.png Icône pour la barre d'outils]
}}

## Description

Simple exemple d\'animation dans l\'atelier Draft en utilsant les [expressions](Expressions/fr.md) pour associer les différents objets et en produire une animation ou vérification du bon fonctionnement de la cinétique finale.

![ Animation utilisant des contraintes produites par les expressions](images/Constraint_Draft00.gif )



*Animation use the constraint expression*

## Utilisation

Téléchargez le fichier exemple [Constraint_Draft00.FCStd](http://forum.freecadweb.org/download/file.php?id=36559), ouvrez le dans FreeCAD

## Script

Pour copier le script, sélectionnez la ligne **Line005_with_Code** dans la Vue combinée sélectionnez l\'onglet Données puis → section → Memo code → Code for rotation → ** ... ** (La macro fonctionne avec FreeCAD version 16)

Sélectionnez le code complet et copiez le dans la console Python

(Si la console Python n\'est pas affichée, faites Menu → Affichage → Panneaux → Console Python)

Petite vidéo, comment copier le code

![Comment copier le code](images/Constraint_Draft_Code01.gif )

ToolBar Icon ![](images/Macro_Constraint_Draft.png )

**Macro_Constraint_Draft.FCMacro**


{{MacroCode|code=

# Copy and pate this snippet in the FreeCAD console Python 
# mario52 19/04/2017

import FreeCADGui
import FreeCAD

#FreeCAD.Console.PrintMessage(str(FreeCAD.Version()) + "\n")
if int(FreeCAD.Version()[1]) == 16:    # Version de FreeCAD
    try:
        for i in range(0,360,5):
            App.getDocument("Constraint_Draft00").Circle.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(i,0,0), App.Vector(0,0,0))
            FreeCADGui.updateGui()
            FreeCAD.ActiveDocument.recompute()
    except Exception:
        FreeCAD.Console.PrintMessage("You must download the Constraint_Draft00.FCStd file for run this macro" + "\n")
        import webbrowser 
        webbrowser.open("http://forum.freecadweb.org/download/file.php?id=36559")

else:
    FreeCAD.Console.PrintError("This macro run with the FreeCAD.Version 16 " + "\n")

}}

## Rotation avec les outils FreeCAD 

![Rotation avec les outils FreeCAD](images/Constraint_Draft01.gif )

## Lien

Discussion sur le forum [Sketch Feature to create linkage mechanism simulator](https://www.forum.freecadweb.org/viewtopic.php?f=22&t=21778&sid=28247565010ecdef0aa4f5c69e58f672)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Constraint Draft/fr
