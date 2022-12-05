---
- TutorialInfo:/fr
   Topic: Product design
   Level: Débutant
   Time:30 minutes
   Author:r-frank et vocx
   FCVersion:0.17 et suivantes
   Files:[https://github.com/FreeCAD/Examples/blob/master/Draft_Shapestring_Tutorial_Examples/Draft_Shapestring_Tutorial_Text.FCStd?raw=true Draft_Shapestring_Text]
---

# Draft ShapeString tutorial/fr





## Introduction

Ce tutoriel a été écrit à l\'origine par Roland Frank († 2017, r-frank). Il a été réécrit et illustré par vocx.

Ce tutoriel décrit une méthode pour créer du texte 3D et l\'utiliser avec des objets solides dans l\'[atelier Part](Part_Workbench/fr.md) <img alt="" src=images/Workbench_Part.svg  style="width:24px;">. Nous allons voir comment :

-   insérer du texte avec l\'outil **<img src="images/Draft_ShapeString.svg" width=16px> [Draft Formes à partir de texte](Draft_ShapeString/fr.md)**,
-   l\'extruder pour qu\'il soit un solide 3D avec **[<img src=images/Part_Extrude.svg style="width:16px"> [Part Extrusion](Part_Extrude/fr.md)**,
-   le positionner dans l\'espace 3D en utilisant le [placement](Placement/fr.md) et **[<img src=images/Draft_Move.svg style="width:16px"> [Draft Déplacer](Draft_Move/fr.md)** (on utilise une esquisse comme géométrie auxiliaire) et
-   graver le texte en appliquant une **[<img src=images/Part_Cut.svg style="width:16px"> [Part Soustraction](Part_Cut/fr.md)**.

Pour utiliser ShapeStrings à l\'intérieur de l\'[atelier PartDesign](PartDesign_Workbench/fr.md) <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;">, le procédé est essentiellement le même qu\'avec l\'atelier Part, mais le ShapeString est placé à l\'intérieur du [corps PartDesign](PartDesign_Body/fr.md) pour l\'extruder. allez à la fin de ce didacticiel pour plus d\'informations.

![](images/08_T04_Part_ShapesString_Extrude_final_cut.png ) 
*Maquette finale du texte gravé.*

L\'[atelier Sketcher](Sketcher_Workbench/fr.md) est utilisé brièvement pour tracer une ligne auxiliaire. Pour plus d\'informations sur les outils de cet atelier, consultez

-   le [Tutoriel d\'introduction à Sketcher](Basic_Sketcher_Tutorial/fr.md)
-   le [Manuel de référence pour Sketcher](Sketcher_reference/fr.md)

## Installation

1\. Lancez FreeCAD, créez un nouveau document vide avec **Fichier → [<img src=images/Std_New.svg style="width:16px"> [Nouveau](Std_New/fr.md)** et sélectionnez l\'[atelier Part](Part_Workbench/fr.md).

:   1.1. Appuyez sur le bouton **[<img src=images/Std_ViewIsometric.svg style="width:16px"> [Vue isométrique](Std_ViewIsometric/fr.md)** ou appuyez sur **0** dans le pavé numérique de votre clavier, pour changer la vue à isométrique pour mieux visualiser les solides 3D.
:   1.2. Appuyez sur le bouton **[<img src=images/Std_ViewFitAll.svg style="width:16px"> [Tout afficher](Std_ViewFitAll/fr.md)** chaque fois que vous ajoutez des objets afin de faire un panoramique et un zoom sur [Vue 3D](3D_view/fr.md) afin que tous les éléments soient visibles dans la vue.
:   1.3. Maintenez **Ctrl** pendant que vous cliquez pour sélectionner plusieurs éléments. Si vous avez sélectionné quelque chose de mal ou souhaitez tout désélectionner, cliquez simplement sur un espace vide dans la [Vue 3D](3D_view/fr.md).

## Création de la forme de base 

2\. Insérez un cube primitif en cliquant sur **<img src="images/Part_Box.svg" width=16px> [Cube](Part_Box/fr.md)**.

:   2.1. Sélectionnez `Cube` dans la [vue en arborescence](Tree_view/fr.md).
:   2.2. Modifiez les dimensions dans l\'onglet **Données** de l\'[éditeur de propriétés](Property_editor/fr.md).
:   2.3. Mettez **Width** à `31 mm`.

3\. Créer un chanfrein.

:   3.1. Sélectionnez le bord supérieur (`Arête6`) sur la face avant du `Cube` dans la [Vue 3D](3D_view/fr.md).
:   3.2. Appuyez sur **<img src="images/Part_Chamfer.svg" width=16px> [Chanfrein](Part_Chamfer/fr.md)**.
:   3.3. Dans le [Panneau des tâches](Task_panel/fr.md) de **Chanfreiner les arêtes**, se rendre à **Forme sélectionnée** puis choisir **Sélectionner les arêtes**. Comme **Type de chanfrein**, choisissez `Cote égale` puis définissez la **Longueur** à `5 mm`.
:   3.4. Appuyez sur **OK**. Cela créera un objet `Chamfer`.
:   3,5. Dans la [vue en arborescence](Tree_view/fr.md), sélectionnez `Chanfrein`, dans l\'onglet **Vue**, changez la valeur de **Line Width** à `2.0`.

![](images/01_T04_Part_Cube_base_long.png ) 
*Objet de base créé à partir d'un cube et d'une opération de chanfrein.*

## Insertion du texte avec l\'outil Dessin de ShapeString 

4\. Basculez vers l\'[atelier Draft](Draft_Workbench/fr.md).

:   4.1. Assurez-vous que rien n\'est sélectionné dans [vue en arborescence](Tree_view/fr.md).
:   4.2. Établissez le plan de travail jusqu\'à XY (haut) en cliquant sur **[<img src=images/Draft_SelectPlane.svg style="width:16px"> [Plan de travail](Draft_SelectPlane/fr.md)** et pressez **[<img src=images/View-top.svg style="width:16px"> [Vue de dessus (XY)](Std_ViewTop/fr.md)**.

5\. Insérer le texte \"FreeCAD\".

:   5.1. Appuyez sur **[<img src=images/Draft_ShapeString.svg style="width:16px"> [ShapeString](Draft_ShapeString/fr.md)**.
:   5.2. Remplacez **X** en `0 mm`.
:   5.3. Remplacez **Y** en `0 mm`.
:   5.4. Remplacez **Z** en `0 mm`.
:   5,5. Ou appuyez sur **Réinitialiser le point**.
:   5.6. Remplacez **Chaîne** en `FreeCAD`; mettez la **Hauteur** à `5 mm`; remplacez **Tracking** en `0 mm`.
:   5.7. Assurez-vous que **Fichier de police** pointe vers une police valide, par exemple `/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf`. Appuyez sur les points de suspension **...** pour ouvrir la boîte de dialogue du système d\'exploitation pour trouver une police.

    :   
        **Remarque :**
        
        pour plus de détails sur le travail avec les polices, veuillez vous reporter à la section [Draft Formes à partir texte Remarques](Draft_ShapeString/fr#Remarques.md).
:   5.8. Appuyez sur **OK**. Cela créera un objet `ShapeString`.
:   5.9. Recalculez le document en appuyant sur **[<img src=images/Std_Refresh.svg style="width:16px"> [Rafraîchir](Std_Refresh/fr.md)**.
:   5.10. Dans la [vue en arborescence](Tree_view/fr.md), sélectionnez `ShapeString`, dans l\'onglet **Vue**, changez la valeur de **Line Width** en `2.0`.
:   5.11. Dans la [vue en arborescence](Tree_view/fr.md), sélectionnez `Chamfer`, dans l\'onglet **Vue**, changez la valeur de **Visibility** à `false` ou appuyez sur **Espace** sur le clavier. Cela masquera l\'objet afin que vous puissiez mieux voir le `ShapeString`.
:   5.12. Pour voir la ShapeString ci-dessus, changez la vue en appuyant sur **[<img src=images/View-top.svg style="width:16px"> [Vue de dessus (XY)](Std_ViewTop/fr.md)** ou **2** au clavier.
:   5.13. Pour restaurer la vue en isométrique, appuyez sur **[<img src=images/Std_ViewIsometric.svg style="width:16px"> [Vue isométrique](Std_ViewIsometric/fr.md)** ou **0** au clavier.

![](images/02_T04_Part_ShapeString.png ) 
*Texte créé en tant que ShapeString, c'est-à-dire en tant que collection d'arêtes dans un plan.*

## Créer un texte 3D 

6\. Retour à l\'[atelier Part](Part_Workbench/fr.md).

:   6.1. Dans la [vue en arborescence](Tree_view/fr.md), sélectionnez `ShapeString`, puis appuyez sur **[<img src=images/Part_Extrude.svg style="width:16px"> [Extrusion](Part_Extrude/fr.md)**.
:   6.2. Dans le [Panneau des tâches](Task_panel/fr.md) **Extrusion** allez dans **Direction**, choisissez **Along normal**; dans **Length**, définissez **Along** sur `1 mm`; cochez également l\'option **Create solid**.
:   6.3. Appuyez sur **OK**. Cela créera un objet `Extrude`.
:   6.4. Dans la [vue en arborescence](Tree_view/fr.md), sélectionnez `Extrude`, dans l\'onglet **Vue**, changez la valeur de **Line Width** en `2.0`.

![](images/03_T04_Part_ShapeString_Extrude.png ) 
*Texte créé comme un ShapeString et transformé en solide par extrusion.*

## Insérer l\'esquisse pour le positionnement 

Nous allons maintenant dessiner une simple esquisse qui sera utilisée comme géométrie auxiliaire pour positionner l\'extrusion ShapeString.

7\. Dans la [vue en arboresence](Tree_view/fr.md), sélectionnez `Extrude` et pressez **Espace** pour le rendre invisible.

8\. Basculez vers l\'[atelier Sketcher](Sketcher_Workbench/fr.md).

9\. Dans la [vue en arborescence](Tree_view/fr.md), sélectionnez `Chamfer`, puis appuyez sur **Espace** sur le clavier pour le rendre visible.

:   9.1. Choisissez la face inclinée créée par l\'opération de chanfrein (`Face3`).
:   9.2. Cliquez sur **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Créer une esquisse](Sketcher_NewSketch/fr.md)**. Dans la boîte de dialogue **Sketch attachment**, sélectionnez `FlatFace`, puis appuyez sur **OK**.
:   9.3. La vue doit s\'ajuster automatiquement afin que la caméra soit parallèle au visage sélectionné.
:   9.4. Tracez une ligne horizontale dans une position générale sur le dessus du visage. La longueur n\'est pas importante; nous sommes simplement intéressés par sa position.
:   9.5. Contraindre l\'extrémité gauche à `2.5 mm` de l\'axe X local et de l\'axe Y local, à l\'aide de **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Contrainte de distance horizontale](Sketcher_ConstrainDistanceX/fr.md)** et **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [Contrainte de distance verticale](Sketcher_ConstrainDistanceY/fr.md)**.
:   9,6. Étant donné que l\'esquisse n\'est qu\'un objet auxiliaire, nous n\'avons pas besoin de le contraindre complètement. Vous pouvez le faire si vous le souhaitez en affectant une distance fixe, par exemple `20 mm`, à nouveau avec **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Contrainte de distance horizontale](Sketcher_ConstrainDistanceX/fr.md)**.
:   9.7. Fermez l\'esquisse.

<img alt="" src=images/04_T04_Part_ShapeString_support_sketch.png  style="width:500px;"> 
*Ligne en cours de création avec l'esquisse, avec contraintes.*

<img alt="" src=images/05_T04_Part_ShapeString_support_sketch_3D.png  style="width:500px;"> 
*Ligne d'esquisse créée au-dessus de la face solide, à utiliser comme guide de référence pour positionner le texte extrudé.*

## Positionnement du texte 3D dans l\'espace 3D 

10\. Dans la [vue en arboresence](Tree_view/fr.md), sélectionnez `Extrude` et pressez **Espace** pour le rendre visible.

11\. Toujours avec `Extrude` sélectionné, dans l\'onglet **Données** de l\'l\'[éditeur de propriétés](Property_editor/fr.md), cliquez sur la valeur **Placement** pour que le bouton points de suspension **...** apparaisse sur la droite et cliquez sur ce bouton.

:   11.1. Cochez l\'option **Appliquer des changements incrémentiels**.
:   11.2. Changez **Rotation** en `Axe de rotation avec angle`; **Axe** en `Z`. (en définissant les valeurs `X`, `Y` et `Z` des valeurs de l\'axe à `0`, `0` et `1` respectivement, `Z` étant la troisième entrée), et **Angle** à `90 deg`, puis cliquez sur **Appliquer**. Ceci appliquera une rotation autour de l\'axe Z et remettra le champ **Angle** à zéro.
:   11.3. Changez **Rotation** en `Axe de rotation avec angle`; **Axe** en `Y`. (en définissant les valeurs `X`, `Y` et `Z` des valeurs de l\'axe à `0`, `1` et `0` respectivement), et **Angle** à `45 deg`, puis cliquez sur **Appliquer**. Ceci appliquera une rotation autour de l\'axe Y et remettra le champ **Angle** à zéro.
:   11.4. Cliquez sur **OK** pour fermer la boîte de dialogue.

12\. Basculez à nouveau vers l\'[Atelier Draft](Draft_Workbench/fr.md).

:   12.1. Passez au style de dessin \"Filaire\" avec **Affichage → [Style de représentation](Std_DrawStyle/fr.md) → [<img src=images/DrawStyleWireFrame.svg style="width:16px"> Filaire** ou appuyez sur **[<img src=images/DrawStyleWireFrame.svg style="width:16px"> [Filaire](Std_DrawStyle/fr.md)** dans la barre d\'outils de la vue. Cela vous permettra de voir les objets derrière d\'autres objets.
:   12.2. Assurez-vous que la méthode [Draft Aimantation](Draft_Snap/fr.md) \"Aimantation Terminaison\" est active. Cela peut être fait à partir du menu **Draft → Aimantation → [<img src=images/Draft_Snap_Lock.svg style="width:16px"> [Verrouillage de l'aimantation](Draft_Snap_Lock/fr.md)** puis ** → [<img src=images/Draft_Snap_Endpoint.svg style="width:16px"> [Aimantation Terminaison](Draft_Snap_Endpoint/fr.md)** ou en appuyant sur **[<img src=images/Draft_Snap_Lock.svg style="width:16px"> [Verrouillage de l'aimantation](Draft_Snap_Lock/fr.md)** et **[<img src=images/Draft_Snap_Endpoint.svg style="width:16px"> [Terminaison](Draft_Snap_Endpoint/fr.md)** dans la barre d\'outils Snap.

13\. Dans la [vue en arborescence](Tree_view/fr.md), sélectionnez `Extrude`.

:   13.1. Cliquez sur **[<img src=images/Draft_Move.svg style="width:16px"> [Déplacer](Draft_Move/fr.md)**.
:   13.2. Dans la [Vue 3D](3D_view/fr.md), cliquez sur le coin supérieur gauche de l\'objet `Extrude` (1), puis cliquez sur le point le plus à gauche de la ligne tracée avec l\'esquisse (2).
:   13.3. Si **[<img src=images/Draft_Snap_Endpoint.svg style="width:16px"> [Terminaison](Draft_Snap_Endpoint/fr.md)** est actif, dès que vous déplacez le pointeur près d\'un sommet, vous devez voir qu\'il s\'y attache exactement.
:   
    **Remarque :**si vous rencontrez des problèmes lors de l\'aimantation aux sommets, assurez-vous que seule la méthode **[<img src=images/Draft_Snap_Endpoint.svg style="width:16px"> [Terminaison](Draft_Snap_Endpoint/fr.md)** est activée . Le fait d\'avoir plusieurs méthodes d\'aimantation actives en même temps peut rendre difficile la sélection de la bonne fonction.
:   13.4. Le texte extrudé doit maintenant se trouver dans le corps de l\'objet `Fillet`.

![](images/06_T04_Part_ShapeString_move.svg ) 
*La chaîne de forme extrudée doit être déplacée à la position de la ligne esquissée qui se trouve sur la face du corps de base.*

![](images/07_T04_Part_ShapesString_Extrude_in_place.png ) 
*Chaîne de forme extrudée positionnée dans le `Fillet*.`

## Création de texte gravé 

14\. Revenez à l\'[Atelier Part](Part_Workbench/fr.md).

:   14.1. Passez au style de dessin \"Comme actuellement\" avec **Affichage → [Style de représentation](Std_DrawStyle/fr.md) → [<img src=images/DrawStyleAsIs.svg style="width:16px"> Comme actuellement** ou appuyez sur le **[<img src=images/DrawStyleAsIs.svg style="width:16px"> [Comme actuellement](Std_DrawStyle/fr.md)** bouton dans la barre d\'outils de la vue. Cela montrera tous les objets avec l\'ombrage et la couleur normaux.
:   14.2. Dans la [Vue en arborescence](Tree_view/fr.md), sélectionnez `Sketch` et appuyez sur **Espace** sur le clavier pour le rendre invisible.

15\. Dans la [vue en arborescence](Tree_view/fr.md), sélectionnez d\'abord `Chamfer` puis `Extrude`.

:   15.1. Appuyez ensuite sur **[<img src=images/Part_Cut.svg style="width:16px"> [Soustraction](Part_Cut/fr.md)**. Cela créera un objet `Cut`. Ceci est l\'objet terminé.
:   
    **Remarque :**l\'ordre dans lequel vous sélectionnez les objets est important pour l\'opération de découpe. L\'objet de base est sélectionné en premier et l\'objet soustractif arrive à la fin.
:   15.2. Dans la [vue en arborescence](Tree_view/fr.md), sélectionnez `Cut`, dans l\'onglet **Vue**, changez la valeur de **Line Width** en `2.0`.

![](images/08_T04_Part_ShapesString_Extrude_final_cut.png ) 
*Modèle terminé d'un cube avec filet avec du texte gravé créé à partir des opérations ShapeString, extrusion et soustraction bouléenne.*

## Gravure de texte 3D avec l\'atelier PartDesign 

Un processus similaire à celui décrit ci-dessus peut être effectué avec l\'[Atelier PartDesign](PartDesign_Workbench/fr.md).

1.  Créez d\'abord le **[<img src=images/Draft_ShapeString.svg style="width:16px"> [Draft Formes à partir texte](Draft_ShapeString/fr.md)**.
2.  Créez un **[<img src=images/PartDesign_Body_Tree.svg style="width:16px"> [PartDesign Corps](PartDesign_Body/fr.md)**, rendez-le actif et ajoutez un solide de base en ajoutant des primitives ou en utilisant une esquisse et en l\'extrudant avec **[<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Protrusion](PartDesign_Pad/fr.md)**.
3.  Déplacez l\'objet `ShapeString` dans le corps actif.
4.  Attachez l\'objet `ShapeString` à l\'une des faces du solide ou à un **[<img src=images/PartDesign_Plane.svg style="width:16px"> [PartDesign Plan de référence](PartDesign_Plane/fr.md)**, en utilisant **[<img src=images/Part_EditAttachment.svg style="width:16px"> [Part Accrochage](Part_EditAttachment/fr.md)**.
5.  Créez maintenant un **[<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Protrusion](PartDesign_Pad/fr.md)** ou un **[<img src=images/PartDesign_Pocket.svg style="width:16px"> [PartDesign Cavité](PartDesign_Pocket/fr.md)** à partir de `ShapeString`, afin de produire un additif ou une soustraction [PartDesign Feature](PartDesign_Feature/fr.md) du corps de base, respectivement.

Voir le fil du forum [How to use ShapeStrings in PartDesign](https://forum.freecadweb.org/viewtopic.php?f=3&t=36623).

## Remarques

-   pour créer un texte courbé, vous pouvez utiliser <img alt="" src=images/FCCircularTextButtom.png  style="width:32px;"> [Macro FCCircularText](Macro_FCCircularText/fr.md).
-   pour importer du texte depuis Inkscape, regardez l\' [Importation de texte à partir du tutoriel Inkscape](Import_text_and_geometry_from_Inkscape/fr.md).


  {{PartDesign Tools navi}} {{Sketcher Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Part](Category_Part.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > [Draft](Draft_Workbench.md) > Draft ShapeString tutorial/fr
