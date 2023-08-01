---
- GuiCommand:
   Name:Sketcher ConstrainCoincident
   Name/fr:Sketcher Contrainte de coïncidence
   MenuLocation:Esquisse → Contraintes d'esquisse → Contrainte coïncidente
   Workbenches:[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut:**C**
   SeeAlso:[Sketcher Contrainte fixe](Sketcher_ConstrainLock/fr.md), [Sketcher Contrainte point sur objet](Sketcher_ConstrainPointOnObject/fr.md)
---

# Sketcher ConstrainCoincident/fr

## Description

Associe un point à (coïncider avec) un ou plusieurs autres points. {{Version/fr|0.21}} : agit comme une contrainte concentrique si deux ou plusieurs cercles, arcs, ellipses ou arcs d\'ellipses sont sélectionnés.



## Utilisation

1.  Faites l\'une des actions suivantes :
    -   Sélectionnez deux points ou plus.
    -   Sélectionner deux ou plusieurs arêtes de cercles, d\'arcs, d\'ellipses ou d\'arcs d\'ellipses.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **[<img src=images/Sketcher_ConstrainCoincident.svg style="width:16px"> [Contrainte coïncidente](Sketcher_ConstrainCoincident/fr.md)** dans la barre d\'outils.
    -   Utilisez le raccourci clavier **C**.
    -   Utilisez l\'entrée **Esquisse → Contraintes d'esquisse → [<img src=images/Sketcher_ConstrainCoincident.svg style="width:16px"> Contrainte coïncidente** dans le menu supérieur.



## Alternatives à la contrainte de coïncidence 

Les deux éléments contraints d\'une contrainte [Coincidente](Sketcher_ConstrainCoincident/fr.md) doivent être des points de départ ou des sommets de point finaux, ou des points centraux d\'arcs, de cercles ou d\'ellipses. Certaines combinaisons qui ne sont pas possibles avec une contrainte coïncidente peuvent être émulées à l\'aide d\'autres contraintes:

-   La contrainte <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;"> [Symétrie](Sketcher_ConstrainSymmetric/fr.md) peut être utilisée pour placer un point de départ, un point final ou un point central sur le milieu d\'une ligne droite.
-   Un placement de milieu à milieu de deux lignes droites peut être obtenu en créant un nouveau <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:24px;"> [Point](Sketcher_CreatePoint/fr.md) et en utilisant deux <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:24px;"> [Symétrie](Sketcher_ConstrainSymmetric/fr.md) contraintes de sorte qu\'il se trouve au milieu des deux lignes.
-   Un sommet peut être contraint de se trouver le long d\'une arête à l\'aide d\'une contrainte <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [Contrainte point sur objet](Sketcher_ConstrainPointOnObject/fr.md). Notez qu\'avec cette contrainte, le point peut se trouver n\'importe où sur l\'extension complète d\'un segment ou d\'une courbe (c\'est-à-dire également avant le point de départ ou au-delà du point final).
-   Un placement colinéaire de deux lignes droites peut être obtenu en leur appliquant une contrainte <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;"> [Tangente](Sketcher_ConstrainTangent/fr.md), ou en combinant une <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:24px;"> [Contrainte point sur objet](Sketcher_ConstrainPointOnObject/fr.md) et une contrainte <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:24px;"> [Parallèle](Sketcher_ConstrainParallel/fr.md).
-   Deux arêtes peuvent être rendues identiques en utilisant deux contraintes de <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Coincidence](Sketcher_ConstrainCoincident/fr.md), une pour chaque paire d\'extrémités.
-   Deux cercles peuvent être rendus identiques en utilisant une contrainte <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:24px;"> [Coincidence](Sketcher_ConstrainCoincident/fr.md) pour fusionner les centres, et en appliquant une contrainte <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;"> [Egalité](Sketcher_ConstrainEqual/fr.md) à leurs bords. Pour les arcs, cela garantira que les deux arcs font partie du même cercle, tout en leur permettant d\'avoir des points de départ et d\'arrivée différents.



## Script

La contrainte peut être créée à partir de [macros](Macros/fr.md) et de la console [Python](Python/fr.md) à l\'aide de la commande suivante :


```pythonSketch.addConstraint(Sketcher.Constraint('Coincident',LineFixed,PointOfLineFixed,LineMoving,PointOfLineMoving)) 
```

où :

-    `Sketch`est un objet d\'esquisse

-    `LineFixed`est le numéro de la ligne qui ne bougera pas en appliquant la contrainte

-    `PointOfLineFixed`indique quel sommet de `LineFixed` doit remplir la contrainte

-    `LineMoving`est le numéro de la ligne, qui se déplacera en appliquant la contrainte

-    `PointOfLineMoving`indique quel sommet de `LineMoving` doit remplir la contrainte

Comme les noms `LineFixed` et `LineMoving` l\'indiquent, si les deux sommets contraints sont libres de se déplacer dans n\'importe quelle direction, le premier (le premier à être sélectionné dans l\'interface graphique) restera fixe et l\'autre on bougera. En présence de contraintes existantes, cependant, les deux bords peuvent bouger.

La page [Sketcher : Écrire un script](Sketcher_scripting/fr.md) explique les valeurs qui peuvent être utilisées pour `LineFixed`, `PointOfLineFixed`, `LineMoving` et `PointOfLineMoving`, et contient d\'autres exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainCoincident/fr
