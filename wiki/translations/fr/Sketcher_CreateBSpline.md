---
 GuiCommand:
   Name: Sketcher CreateBSpline
   Name/fr: Sketcher B-spline simple
   MenuLocation: Esquisse , Géométries d'esquisse , Créer une B-spline
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **B** **B**
   Version: 0.17
   SeeAlso: Sketcher_CreatePeriodicBSpline/fr
---

# Sketcher CreateBSpline/fr

## Description

L\'outil <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:24px;"> [Sketcher B-spline simple](Sketcher_CreateBSpline/fr.md) crée une courbe [B-spline](B-Splines/fr.md) par des points de contrôle. <small>(v1.0)</small>  : ou éventuellement par des points de nœuds.

![](images/Sketcher_CreateBSpline_Example.png ) 
*Courbe B-spline (en blanc) définie par 5 points de contrôle.<br>
Le polygone de contrôle (vert) relie les points de contrôle (marqués par des cercles de poids en jaune foncé).<br>
Le chiffre 3 (vert, sans parenthèses) au centre fait référence au [degré](Sketcher_BSplineIncreaseDegree/fr#Description.md) de la B-spline.<br>
Les nombres (1) et (4) (verts, entre parenthèses) correspondent à la [multiplicité](Sketcher_BSplineDecreaseKnotMultiplicity/fr#Description.md) des points des nœuds.<br>
Les nombres [1.00] (verts, entre parenthèses) correspondent aux poids des points de contrôle.*



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_CreateBSpline.svg" width=16px> [B-spline par les points de contrôle](Sketcher_CreateBSpline/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Géométries d'esquisse → <img src="images/Sketcher_CreateBSpline.svg" width=16px> Créer une B-spline** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_CreateBSpline.svg" width=16px> Créer une B-spline** du menu contextuel. {{Version/fr|0.22}}
    -   Utilisez le raccourci clavier : **G** puis **B**, puis **B**.
2.  Le curseur se transforme en croix avec l\'icône de l\'outil.
3.  La section **Paramètres de la B-spline** ({{Version/fr|1.0}}) est ajoutée en haut de la [fenêtre de dialogue de Sketcher](Sketcher_Dialog/fr.md).
4.  Il est possible d\'appuyer sur la touche **M** ou de choisir dans la liste déroulante de la section des paramètres pour changer le mode de l\'outil :
    -   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:16px;"> **Par points de contrôle** :
        1.  Possibilité de changer le **Degré** (également possible après que les points aient été choisis) :
            -   Entrez un nombre supérieur à zéro.
            -   Appuyez sur la touche **U** pour augmenter le degré.
            -   Appuyez sur la touche **J** pour diminuer le degré.
    -   <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:16px;"> **Par des nœuds** : {{Version/fr|1.0}}
        1.  Les B-splines par des noeuds sont toujours créées avec un degré 3. Mais leur degré peut être changé plus tard. Voir [Remarques](#Remarques.md).
5.  Vous pouvez également appuyer sur la touche **R** ou cocher la case **Périodique** pour créer une B-spline fermée (également possible après que les points aient été choisis). {{Version/fr|1.0}}
6.  Choisissez plusieurs points.
7.  Appuyez éventuellement sur la touche **F** avant de terminer pour supprimer le dernier point. {{Version/fr|1.0}}
8.  Cliquez avec le bouton droit de la souris ou appuyez sur **Échap** pour terminer la saisie.
9.  La B-spline est créée, y compris un ensemble de géométrie interne (cercles de poids et points de nœuds).
10. Si l\'outil fonctionne en [continue mode](Sketcher_Workbench/fr#Modes_continus.md) :
    1.  Vous pouvez continuer à créer des B-splines.
    2.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



## Remarques

-   Les éléments de la géométrie interne peuvent être supprimés. Ils peuvent être recréés à tout moment avec [Sketcher Géométrie interne d\'alignement](Sketcher_RestoreInternalAlignmentGeometry/fr.md).
-   Après la création d\'une B-spline, il est possible de définir le poids des points de contrôle en modifiant les rayons des cercles de poids. Les contraintes d\'égalité sur les cercles doivent d\'abord être supprimées. La contrainte de rayon est arbitraire, le poids des points de contrôle sera défini par les rayons relatifs des cercles. Le fonctionnement est similaire à celui de la gravité : plus un cercle est grand par rapport aux autres, plus la courbe sera attirée vers ce point de contrôle.
-   Le degré d\'une B-spline créée peut être [augmenté](Sketcher_BSplineIncreaseDegree/fr.md) ou [diminué](Sketcher_BSplineDecreaseDegree/fr.md) et la multiplicité de ses nœuds peut être [augmentée](Sketcher_BSplineIncreaseKnotMultiplicity/fr.md) ou [diminuée](Sketcher_BSplineIncreaseKnotMultiplicity/fr.md) également.
-   La visibilité du [degré](Sketcher_BSplineDegree/fr.md), du [polygone de contrôle](Sketcher_BSplinePolygon/fr.md), du [peigne de courbure](Sketcher_BSplineComb/fr.md), de la [multiplicité des nœuds](Sketcher_BSplineKnotMultiplicity/fr.md) et du [poids des points de contrôle](Sketcher_BSplinePoleWeight/fr.md) peut être activée/désactivée à partir de la barre d\'outils [Affichage de Sketcher](Sketcher_Workbench/fr#Affichage.md).

## Limitations

-   Plusieurs contraintes ne sont pas prises en charge pour le moment.

-   La multiplicité des nœuds définie n\'est pas toujours respectée :
    -   Pour une spline périodique, le premier nœud (coïncidant avec le dernier) a toujours une multiplicité de 2.
    -   Pour une spline non périodique, le premier et le dernier nœuds ont toujours une multiplicité de 4.
    -   Si les points juste avant et juste après ont des multiplicités \>=3, le morceau entre ces deux points est entièrement continu, et ce point (du milieu) ne sera contraint que par un point sur l\'objet. Si un nœud est nécessaire, envisagez d\'utiliser l\'outil [insérer un nœud](Sketcher_BSplineInsertKnot/fr.md).



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateBSpline/fr
