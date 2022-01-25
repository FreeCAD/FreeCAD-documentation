# Macro Solid Sweep/fr
{{Macro/fr
|Name=Balayage solide
|Icon=Macro_Solid_Sweep.png
|Description=Créé un solide en balayant un profil le long d'une trajectoire.
|Author=Normandc
|Version=1.0
|Date=2011-12-03
|FCVersion=Toutes versions
|Download=[https://www.freecadweb.org/wiki/images/6/6d/Macro_Solid_Sweep.png 
Icône pour votre barre d'outils]
}}

## Description

Cette macro créé un solide en balayant un profil le long d\'une trajectoire, les deux éléments ayant précédemment été sélectionnés dans la vue 3D. Les éléments 2D peuvent être créés à l\'aide des outils existants de l\'interface graphique de FreeCAD.

Il est à noter que le solide généré ne sera **pas** paramétrique. Si vous décidez de modifier le profil ou la trajectoire, vous devrez exécuter la macro à nouveau.

<img alt="Quelques exemples de balayages utilisant une même section oblongue et trois types de trajectoires." src=images/Solid_sweep.png‎  style="width:500px;">

## Utilisation

1.  Créez deux éléments 2D, un pour la section et un pour la trajectoire, des types répertoriés ci-dessous.
2.  Sélectionnez, soit dans la [vue en arborescence](Tree_view/fr.md) soit dans [Vue 3D](3D_view/fr.md) (**L\'ordre est important!**):
    1.  La trajectoire
    2.  Puis le profil
3.  Ouvrez le [Gestionnaire de macros](Macros/fr.md)
4.  Sélectionnez la macro **Solid Sweep**
5.  Cliquez sur **Execute**

**Résultat:** un **Balayage** sera créé dans l\'arborescence du Projet.

## Éléments 2D supportés 

-   Filaires
-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Esquisses](Sketcher_Workbench/fr.md)
-   <img alt="" src=images/Draft_BSpline.svg  style="width:24px;"> [BSplines](Draft_BSpline/fr.md)
-   Primitives 2D depuis le menu *Pièce → <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> [Créer des primitives](Part_Primitives/fr.md)\...* (cercle, hélice)

## Conseils

-   La section doit être un profil fermé sinon la forme résultante ne sera pas solide.
-   La section n\'a pas besoin d\'être située sur la trajectoire, mais il est préférable qu\'elle lui soit normale (perpendiculaire).
-   La trajectoire peut indifféremment être un profil ouvert ou fermé (cercle, ou une suite de segments de lignes et d\'arcs) mais tous les éléments doivent être tangents, sinon le résultat pourrait être inattendu. Par exemple, une trajectoire avec des coins carrés comme un rectangle ne produira pas un solide.
-   S\'il y a un nœud dans la forme résultante, modifiez la macro et changez la valeur *isFrenet* à 0 (zéro), puis essayez à nouveau.
-   Réglez la variable *makeSolid* à 0 (zéro) pour obtenir une forme non solide faite de surfaces avec des extrémités ouvertes.

## Le script 

ToolBar Icon ![](images/Macro_Solid_Sweep.png )

**Macro\_Solid\_Sweep.FCMacro**


{{MacroCode|code=
import Part, FreeCAD, math, PartGui, FreeCADGui
from FreeCAD import Base

# get the selected objects, with first selection for the trajectory and second for the section
s = FreeCADGui.Selection.getSelection()
try:
     shape1=s[0].Shape
     shape2=s[1].Shape
except:
     print "Wrong selection"

traj = Part.Wire([shape1])
section = Part.Wire([shape2])

# create Part objec in the current document
myObject=App.ActiveDocument.addObject("Part::Feature","Sweep")

# variable makeSolid = 1 to create solid, 0 to create surfaces
makeSolid = True #1
isFrenet = True #1

# create a 3D shape and assigh it to the current document
Sweep = Part.Wire(traj).makePipeShell([section],makeSolid,isFrenet)
myObject.Shape = Sweep

}}

## Remerciements

Merci à [Wmayer](User_Wmayer.md) sans l\'aide de qui je n\'aurais pu rédiger ce script.

Deux exemples d\'utilisation peuvent être consultés dans [cette discussion du forum (en anglais)](http://forum.freecadweb.org/viewtopic.php?f=8&t=1222&start=50#p11120), ainsi que des liens de téléchargement des fichiers FCStd. En utilisant une hélice comme trajectoire, un balayage solide peut être utilisé pour créer un filet de vis.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Solid Sweep/fr
