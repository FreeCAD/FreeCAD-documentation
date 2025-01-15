---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM ConstraintTie
   Name/fr: FEM Contrainte de liaison
   MenuLocation: Modèle , Conditions limites et charges mécaniques , Contrainte de liaison
   Workbenches: FEM_Workbench/fr
   Version: 0.19
   SeeAlso: FEM_ConstraintPressure/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: CalculiX
}}
---

# FEM ConstraintTie/fr

## Description

Définit une contrainte de liaison qui relie les deux surfaces sélectionnées de telle sorte que (par opposition à la façon dont le contact fonctionne) elles ne peuvent pas se séparer ou glisser l\'une sur l\'autre tout au long de l\'analyse. Ainsi, les surfaces restent collées en permanence.


<small>(v1.0)</small> 

: peut également être utilisé pour définir la symétrie cyclique.



## Utilisation

1.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintTie.svg" width=16px> [Contrainte de liaison](FEM_ConstraintTie/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Conditions limites et charges mécaniques → <img src="images/FEM_ConstraintTie.svg" width=16px> Contrainte de liaison** du menu.

2.  Appuyez sur le bouton **Ajouter** du panneau des tâches et cliquez sur la face que vous souhaitez ajouter à la définition de la contrainte de liaison. Deux faces exactement doivent être ajoutées, l\'une après l\'autre. La première face sélectionnée sera la face esclave tandis que la seconde sera la face maître.

3.  Vous pouvez définir une tolérance : la contrainte de liaison ne sera appliquée qu\'aux nœuds de la surface esclave séparés de la surface maître par une distance inférieure ou égale à celle spécifiée ici.

4.  
    {{Version/fr|1.0}}: vous pouvez cocher la case *Activer l\'ajustement* pour permettre aux nœuds de la surface esclave d\'être automatiquement déplacés pour s\'appuyer sur la surface maître s\'ils sont concernés par la contrainte (c\'est-à-dire s\'ils respectent le critère de tolérance).



## Symétrie cyclique 


{{Version/fr|1.0}}

: la contrainte de liaison peut également être utilisée pour définir la symétrie cyclique. Cela permet d\'analyser les modèles présentant une symétrie périodique de rotation (motifs circulaires répétitifs autour d\'un axe de symétrie) à l\'aide d\'un seul secteur représentatif. Elle peut être particulièrement utile pour les rotors, les arbres, les turbines, les ventilateurs, les volants d\'inertie et les pièces similaires, souvent en combinaison avec la [charge centrifuge](FEM_ConstraintCentrif/fr.md) (la charge doit également présenter cette forme de symétrie).. La symétrie cyclique peut être définie en sélectionnant les deux faces de la coupe pour la contrainte de liaison et en définissant les propriétés suivantes :

-    **Cyclic Symmetry**: la valeur *true* active la symétrie cyclique.

-    **Sectors**: nombre total de secteurs, égal à 360° divisé par l\'angle du secteur représentatif (par exemple 8 pour un secteur de 45° ou 6 pour un secteur de 60°).

-    **Connected Sectors**: nombre de secteurs affichés dans les résultats, le fixer au même nombre que **Sectors** si vous voulez visualiser toute la partie à 360°.

-    **Symmetry Axis**: axe de symétrie cyclique - axe Z global par défaut, peut être déplacé en appliquant la transformation Placement au verseur Z (similaire à ce qui peut être fait avec des [Part Lignes](Part_Line.md) - pour comprendre comment déplacer l\'axe de symétrie, il peut être utile de changer le placement de la ligne qui est généralement nécessaire pour la charge centrifuge).

Une limitation importante de cette fonction dans l\'atelier FEM est que les conditions limites ne peuvent pas être appliquées aux nœuds de la surface esclave de la symétrie cyclique (surface esclave dans la définition de la contrainte de liaison), car cela entraînerait une surcontrainte. Dans certains cas, il peut donc s\'avérer nécessaire de supprimer de la définition des conditions limites les nœuds situés sur le bord entre la face soumise à la condition limite et la surface esclave de symétrie cyclique. Malheureusement, FreeCAD n\'opère pas sur des ensembles de nœuds et les nœuds individuels ne peuvent pas être désélectionnés. Il faudrait donc utiliser des solutions de contournement comme l\'ajout d\'une étroite [partition de face](FEM_Geometry_Preparation_and_Meshing/fr#Partitionnement_de_la_géométrie.md) comme transition entre la surface esclave et la surface avec la condition limite.



## Remarques

-   Cette fonction utilise le \[<https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node251>. jeu de paramètres \*TIE de CalculiX\].

-    {{Version/fr|1.0}}: la symétrie cyclique utilise également le[jeu de paramètres \*CYCLIC SYMMETRY MODEL de CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node183.html).





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintTie/fr
