---
 GuiCommand:
   Name: Sketcher CreateFillet
   Name/fr: Sketcher Congé
   MenuLocation: Esquisse , Outils d'esquisse , Créer un congé
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **F** **F**
   SeeAlso: 
---

# Sketcher CreateFillet/fr

## Description

L\'outil <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:24px;"> [Sketcher Congé](Sketcher_CreateFillet/fr.md) crée un congé entre deux arêtes non parallèles. {{Version/fr|1.0}} : l\'outil peut également créer un chanfrein.


<small>(v1.0)</small> 

: si deux arêtes droites reliées par une [contrainte de coïncidence](Sketcher_ConstrainCoincident/fr.md) reçoivent un congé ou un chanfrein, le point d\'angle peut éventuellement être préservé. L\'outil ajoute alors un [objet Point](Sketcher_CreatePoint/fr.md) qui aura une [contrainte de point sur l\'objet](Sketcher_ConstrainPointOnObject/fr.md) avec les deux arêtes. Les contraintes liées au point d\'angle sont alors transférées au nouvel objet point.

![](images/SketcherCreateFilletExample.png‎ )



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_CreateFillet.svg" width=16px> [Créer un congé](Sketcher_CreateFillet/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Outils d'esquisse → <img src="images/Sketcher_CreateFillet.svg" width=16px> Créer un congé** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_CreateFillet.svg" width=16px> Créer un congé** du menu contextuel.
    -   Utilisez le raccourci clavier : **G** puis **F**, puis **F**.
2.  S\'il y a une précédente sélection, elle est effacée. L\'outil n\'accepte pas de présélection.
3.  Le curseur se transforme en croix avec l\'icône du mode d\'outil en cours.
4.  La section **Paramètres du congé/chanfrein** ({{Version/fr|1.0}}) est ajoutée en haut de la [fenêtre de dialogue](Sketcher_Dialog/fr.md).
5.  Il est possible d\'appuyer sur la touche **U** ou de décocher la case **Conserver le coin** pour désactiver cette option. {{Version/fr|1.0}}
6.  Vous pouvez appuyer sur la touche **M** ou sélectionner dans la liste déroulante de la section des paramètres pour changer le mode de l\'outil :
    -   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:16px;"> 
**Congé**
    -   <img alt="" src=images/Sketcher_CreateChamfer.svg  style="width:16px;"> 
**Chanfrein**
7.  Faites l\'une des choses suivantes :
    -   Choisissez un point avec une [contrainte de coïncidence](Sketcher_ConstrainCoincident/fr.md) reliant deux arêtes droites non parallèles.
    -   Choisissez deux arêtes non parallèles. L\'une ou l\'autre arête peut être une [ligne](Sketcher_CreateLine/fr.md) droite, un [arc](Sketcher_CreateArc/fr.md), un [arc d\'ellipse](Sketcher_CreateArcOfEllipse/fr.md), un [arc d\'hyperbole](Sketcher_CreateArcOfHyperbola/fr.md) ou un [arc de parabole](Sketcher_CreateArcOfParabola/fr.md). Les [B-splines](Sketcher_Workbench/fr#Sketcher_CompCreateBSpline.md) ne sont actuellement pas pris en charge.
8.  Le congé ou le chanfrein est créé, y compris un objet ponctuel dans le cas d\'un coin conservé. Pour un chanfrein, un arc de géométrie de construction est également créé.
9.  Cet outil fonctionne toujours en mode continu : il est possible de continuer à sélectionner des points et/ou des arêtes.
10. Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



## Remarques

-   L\'arc géométrique de construction d\'un chanfrein n\'est pas visible en dehors de l\'esquisse. Il ne peut pas être supprimé sans casser la géométrie du chanfrein.
-   Certaines courbes ([coniques](Sketcher_Workbench/fr#Sketcher_CompCreateConic.md)) peuvent devoir être [ajustées](Sketcher_Trimming/fr.md) avant de recevoir un congé.
-   Le rayon du congé dépend de la méthode de sélection. Si une [contrainte de coïncidence](Sketcher_ConstrainCoincident/fr.md) reliant deux arêtes droites est sélectionnée, le rayon du congé est dérivé de la longueur de l\'arête la plus courte. Si deux arêtes sont sélectionnées, le rayon est la distance entre le premier point cliqué et l\'intersection (étendue) des arêtes.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateFillet/fr
