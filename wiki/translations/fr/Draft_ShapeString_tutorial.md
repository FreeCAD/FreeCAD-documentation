# Draft ShapeString tutorial/fr
---
- TutorialInfo   */fr
   Topic   * Product design
   Level   * Débutant
   Time   *30 minutes
   Author   *r-frank et vocx
   FCVersion   *0.17 et suivantes
   Files   *[https   *//github.com/FreeCAD/Examples/blob/master/Draft_Shapestring_Tutorial_Examples/Draft_Shapestring_Tutorial_Text.FCStd?raw=true Draft_Shapestring_Text]
}}

## Introduction

Ce tutoriel a été écrit à l\'origine par Roland Frank († 2017, r-frank). Il a été réécrit et illustré par vocx.

Ce didacticiel décrit une méthode pour créer du texte 3D et l\'utiliser avec des objets solides dans l\'[atelier Part](Part_Workbench/fr.md) <img alt="" src=images/Workbench_Part.svg  style="width   *24px;">. Nous allons voir comment

-   insérer du texte avec l\'outil **![](images/)**,
-   l\'extruder pour qu\'il soit un solide 3D avec **[Part Extrude](File   *Part_Extrude.svg   16px]] [[Part_Extrude/fr.md)**,
-   le positionner dans l\'espace 3D en utilisant le [placement](placement.md) et **[Draft Move](File   *Draft_Move.svg   16px]] [[Draft_Move/fr.md)** (on utilise une esquisse comme géométrie auxiliaire) et
-   gravez le texte en appliquant une **[coupe Part](File   *Part_Cut.svg   16px]] [[Part_Cut/fr.md)**.

Pour utiliser ShapeStrings à l\'intérieur de l\'[atelier PartDesign](PartDesign_Workbench/fr.md) <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;">, le procédé est essentiellement le même qu\'avec l\'atelier Part, mais le ShapeString est placé à l\'intérieur du [corps PartDesign](PartDesign_Body/fr.md) pour l\'extruder. allez à la fin de ce didacticiel pour plus d\'informations.

![](images/08_T04_Part_ShapesString_Extrude_final_cut.png ) 
*Maquette finale du texte gravé.*

L\'[atelier Sketcher](Sketcher_Workbench/fr.md) est utilisé brièvement pour tracer une ligne auxiliaire. Pour plus d\'informations sur les outils de cet atelier, consultez

-   le [Tutoriel d\'introduction à Sketcher](Basic_Sketcher_Tutorial/fr.md)
-   le [Manuel de référence pour Sketcher](Sketcher_reference/fr.md)

## Installation

1\. Lancez FreeCAD, créez un nouveau document vide avec **Fichier → [Nouveau](File   *Std_New.svg   16px]] [[Std_New/fr.md)** et sélectionnez l\'[atelier Part](Part_Workbench/fr.md).

   *   1.1. Appuyez sur le bouton **[Vue isométrique](File   *Std_ViewIsometric.svg   16px]] [[Std_ViewIsometric/fr.md)** ou appuyez sur **0** dans le pavé numérique de votre clavier, pour changer la vue à isométrique pour mieux visualiser les solides 3D.
   *   1.2. Appuyez sur le bouton **[Tout afficher](File   *Std_ViewFitAll.svg   16px]] [[Std_ViewFitAll/fr.md)** chaque fois que vous ajoutez des objets afin de faire un panoramique et un zoom sur [Vue 3D](3D_view/fr.md) afin que tous les éléments soient visibles dans la vue.
   *   1.3. Maintenez **Ctrl** pendant que vous cliquez pour sélectionner plusieurs éléments. Si vous avez sélectionné quelque chose de mal ou souhaitez tout désélectionner, cliquez simplement sur un espace vide dans la [Vue 3D](3D_view/fr.md).

## Création de la forme de base 

2\. Insérer un cube primitif en cliquant sur **![](images/)**.

   *   2.1. Sélectionnez {{incode   Cube}} dans la [vue en arborescence](tree_view/fr.md).
   *   2.2. Modifiez les dimensions dans l\'onglet **Data** de l\'[éditeur de propriétés](property_editor.md).
   *   2.3. Mettez **Width** à {{incode   31 mm}}.

3\. Créer un chanfrein.

   *   3.1. Sélectionnez le bord supérieur ({{incode   Edge6}}) sur la face avant du {{incode   Cube}} dans la [Vue 3D](3D_view/fr.md).
   *   3.2. Appuyez sur **![](images/)**.
   *   3.3. Dans **Chamfer edges** [Panneau des tâches](task_panel/fr.md), se rendre à **Selection** puis choisir **Select edges**. En tant que **Fillet type**, choisissez {{incode   Constant length}} puis définissez **Length** à {{incode   5 mm}}.
   *   3.4. Appuyez sur {{Button     OK}}. Cela créera un objet {{incode   Chamfer}}.
   *   3,5. Dans la [vue en arborescence](tree_view.md), sélectionnez {{incode   Chamfer}}, dans l\'onglet **View**, changez la valeur de **Line Width** à {{incode   2.0}}.

![](images/01_T04_Part_Cube_base_long.png ) 
*Objet de base créé à partir d'un cube et d'une opération de chanfrein.*

## Insertion du texte avec l\'outil Dessin de ShapeString 

4\. Basculez vers l\'[atelier Draft](Draft_Workbench/fr.md).

   *   4.1. Assurez-vous que rien n\'est sélectionné dans [vue en arborescence](tree_view/fr.md).
   *   4.2. Établissez le plan de travail jusqu\'à XY (haut) en cliquant sur **[Plan de travail](File   *Draft_SelectPlane.svg   16px]] [[Draft_SelectPlane/fr.md)** et pressez **[Vue de dessus (XY)](File   *View-top.svg   16px]] [[Std_ViewTop/fr.md)**.

5\. Insérer le texte \"FreeCAD\".

   *   5.1. Appuyez sur **[ShapeString](File   *Draft_ShapeString.svg   16px]] [[Draft_ShapeString.md)**.
   *   5.2. Remplacez **X** en {{incode   0 mm}}.
   *   5.3. Remplacez **Y** en {{incode   0 mm}}.
   *   5.4. Remplacez **Z** en {{incode   0 mm}}.
   *   5,5. Ou appuyez sur **Reset point**.
   *   5.6. Remplacez **String** en {{incode   FreeCAD}}; remplacez **Height** en {{incode   5 mm}}; remplacez **Tracking** en {{incode   0 mm}}.
   *   5.7. Assurez-vous que **Font file** pointe vers une police valide, par exemple {{incode   /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf}}. Appuyez sur les points de suspension **...** pour ouvrir la boîte de dialogue du système d\'exploitation pour trouver une police.

       *   
        **Remarque   ***
        
        pour plus de détails sur le travail avec les polices, veuillez vous reporter à la section [Draft Formes à partir texte Remarques](Draft_ShapeString/fr#Remarques.md).
   *   5.8. Appuyez sur **OK**. Cela créera un objet {{incode   ShapeString}}.
   *   5.9. Recalculez le document en appuyant sur **[Rafraîchir](File   *Std_Refresh.svg   16px]] [[Std_Refresh/fr.md)**.
   *   5.10. Dans la [vue en arborescence](tree_view/fr.md), sélectionnez {{incode   ShapeString}}, dans l\'onglet **View**, changez la valeur de **Line Width** en {{incode   2.0}}.
   *   5.11. Dans la [vue en arborescence](tree_view/fr.md), sélectionnez {{incode   Chamfer}}, dans l\'onglet **View**, changez la valeur de **Visibility** en {{incode   false}} ou appuyez sur **Espace** sur le clavier. Cela masquera l\'objet afin que vous puissiez mieux voir le {{incode   ShapeString}}.
   *   5.12. Pour voir la ShapeString ci-dessus, changez la vue en appuyant sur **[Vue de dessus (XY)](File   *View-top.svg   16px]] [[Std_ViewTop/fr.md)** ou **2** dans le clavier.
   *   5.13. Pour restaurer la vue en isométrique, appuyez sur **[Vue isométrique](File   *Std_ViewIsometric.svg   16px]] [[Std_ViewIsometric/fr.md)** ou **0** sur le clavier.

![](images/02_T04_Part_ShapeString.png ) 
*Texte créé en tant que ShapeString, c'est-à-dire en tant que collection d'arêtes dans un plan.*

## Créer un texte 3D 

6\. Retour à l\'[atelier Part](Part_Workbench/fr.md).

   *   6.1. Dans la [vue en arborescence](tree_view/fr.md), sélectionnez {{incode   ShapeString}}, puis appuyez sur **[Extrusion](File   *Part_Extrude.svg   16px]] [[Part_Extrude/fr.md)**.
   *   6.2. Dans le [Panneau des tâches](task_panel/fr.md) **Extrusion** allez dans **Direction**, choisissez **Along normal**; dans **Length**, définissez **Along** sur {{incode   1 mm}}; cochez également l\'option **Create solid**.
   *   6.3. Appuyez sur **OK**. Cela créera un objet {{incode   Extrude}}.
   *   6.4. Dans la [vue en arborescence](tree_view/fr.md), sélectionnez {{incode   Extrude}}, dans l\'onglet **View**, changez la valeur de **Line Width** en {{incode   2.0}}.

![](images/03_T04_Part_ShapeString_Extrude.png ) 
*Texte créé comme un ShapeString et transformé en solide par extrusion.*

## Insérer l\'esquisse pour le positionnement 

Nous allons maintenant dessiner une simple esquisse qui sera utilisée comme géométrie auxiliaire pour positionner l\'extrusion ShapeString.

7\. Dans la [vue en arboresence](tree_view/fr.md), sélectionnez {{incode   Extrude}} et pressez **Espace** pour le rendre invisible.

8\. Basculez vers l\'[atelier Sketcher](Sketcher_Workbench/fr.md).

9\. Dans la [arborescence](tree_view.md), sélectionnez {{incode   Chamfer}}, puis appuyez sur **Espace** sur le clavier pour le rendre visible.

   *   9.1. Choisissez la face inclinée créée par l\'opération de chanfrein ({{incode   Face3}}).
   *   9.2. Cliquez sur **[Nouvelle esquisse](File   *Sketcher_NewSketch.svg   16px]] [[Sketcher_NewSketch/fr.md)**. Dans la boîte de dialogue **Sketch attachment**, sélectionnez {{incode   FlatFace}}, puis appuyez sur **OK**.
   *   9.3. La vue doit s\'ajuster automatiquement afin que la caméra soit parallèle au visage sélectionné.
   *   9.4. Tracez une ligne horizontale dans une position générale sur le dessus du visage. La longueur n\'est pas importante; nous sommes simplement intéressés par sa position.
   *   9.5. Contraindre l\'extrémité gauche à {{incode   2.5 mm}} de l\'axe X local et de l\'axe Y local, à l\'aide de **[Contrainte de distance horizontale](File   *Sketcher_ConstrainDistanceX.svg   16px]] [[Sketcher_ConstrainDistanceX.md)** et **[Contrainte distance verticale](File   *Sketcher_ConstrainDistanceY.svg   16px]] [[Sketcher_ConstrainDistanceY.md)**.
   *   9,6. Étant donné que l\'esquisse n\'est qu\'un objet auxiliaire, nous n\'avons pas besoin de le contraindre complètement. Vous pouvez le faire si vous le souhaitez en affectant une distance fixe, par exemple {{incode   20 mm}}, à nouveau avec **[Contrainte de distance horizontale](File   *Sketcher_ConstrainDistanceX.svg   16px]] [[Sketcher_ConstrainDistanceX.md)**.
   *   9.7. Fermez l\'esquisse.

<img alt="" src=images/04_T04_Part_ShapeString_support_sketch.png  style="width   *500px;"> 
*Ligne en cours de création avec l'esquisse, avec contraintes.*

<img alt="" src=images/05_T04_Part_ShapeString_support_sketch_3D.png  style="width   *500px;"> 
*Ligne d'esquisse créée au-dessus de la face solide, à utiliser comme guide de référence pour positionner le texte extrudé.*

## Positionnement du texte 3D dans l\'espace 3D 

10\. Dans la [vue en arboresence](tree_view/fr.md), sélectionnez {{incode   Extrude}} et pressez **Espace** pour le rendre visible.

11\. Dans la [vue en arboresence](tree_view/fr.md), sélectionnez {{incode   Extrude}}, dans l\'onglet **Data** de [éditeur de propriétés](property_editor/fr.md), cliquez sur **Placement** afin que le bouton points de suspension **...** apparaisse à droite.

   *   11.1. Cochez l\'option **Apply incremental changes**.
   *   11.2. Remplacez **Rotation** par {{incode   Rotation axis with angle}}; **Axis** en {{incode   Z}} et **Angle** par {{incode   90 deg}} puis cliquez sur **Apply**. Cela appliquera une rotation autour de l\'axe Z et remettra à zéro le champ **Angle**.
   *   11.3. Remplacez **Rotation** par {{incode   Rotation axis with angle}}; **Axis** en {{incode   Y}}, and **Angle** par {{incode   45 deg}}, puis cliquez sur {{Button     Apply}}. Cela appliquera une rotation autour de l\'axe Y et remettra à zéro le champ **Angle**.
   *   11.4. Cliquez sur **OK** pour fermer la boîte de dialogue.

12\. Basculez à nouveau vers l\'[Atelier Draft](Draft_Workbench/fr.md).

   *   12.1. Passez au style de dessin \"Filaire\" avec **Affichage → [16px](Std_DrawStyle/fr___Style_de_représentation]]_→_[[File   *DrawStyleWireFrame.svg.md) Filaire** ou appuyez sur **[Filaire](File   *DrawStyleWireFrame.svg   16px]] [[Std_DrawStyle/fr.md)** dans la barre d\'outils de la vue. Cela vous permettra de voir les objets derrière d\'autres objets.
   *   12.2. Assurez-vous que la méthode [Draft Accrochage](Draft_Snap/fr.md) \"Snap to endpoint\" est active. Cela peut être fait à partir du menu **Draft → Accrochage → [Activer/désactiver l'accrochage](File   *Draft_Snap_Lock.svg   16px]] [[Draft_Snap_Lock/fr.md)** puis ** → [Terminaison](File   *Snap_Endpoint.svg   16px]] [[Draft_Snap_Endpoint/fr.md)** ou en appuyant sur **[Activer/désactiver l'accrochage](File   *Draft_Snap_Lock.svg   16px]] [[Draft_Snap_Lock/fr.md)** et **[Terminaison](File   *Draft_Snap_Endpoint.svg   16px]] [[Draft_Snap_Endpoint/fr.md)** dans la barre d\'outils Snap.

13\. Dans la [Vue en arborescence](Tree_view/fr.md), sélectionnez {{incode   Extrude}}.

   *   13.1. Cliquez sur **[Déplacer](File   *Draft_Move.svg   16px]] [[Draft_Move/fr.md)**.
   *   13.2. Dans la [Vue 3D](3D_view/fr.md), cliquez sur le coin supérieur gauche de l\'objet {{incode   Extrude}} (1), puis cliquez sur le point le plus à gauche de la ligne tracée avec l\'esquisse (2).
   *   13.3. Si **[Terminaison](File   *Draft_Snap_Endpoint.svg   16px]] [[Draft_Snap_Endpoint/fr.md)** est actif, dès que vous déplacez le pointeur près d\'un sommet, vous devez voir qu\'il s\'y attache. exactement.
   *   
    **Remarque   ***si vous rencontrez des problèmes lors de l\'accrochage aux sommets, assurez-vous que seule la méthode **[Terminaison](File   *Draft_Snap_Endpoint.svg   16px]] [[Draft_Snap_Endpoint/fr.md)** est activée . Le fait d\'avoir plusieurs méthodes d\'accrochage actives en même temps peut rendre difficile la sélection de la bonne fonction.
   *   13.4. Le texte extrudé doit maintenant se trouver dans le corps de l\'objet {{incode   Fillet}}.

![](images/06_T04_Part_ShapeString_move.svg ) 
*La chaîne de forme extrudée doit être déplacée à la position de la ligne esquissée qui se trouve sur la face du corps de base.*

![](images/07_T04_Part_ShapesString_Extrude_in_place.png ) 
*Chaîne de forme extrudée positionnée dans le {{incode   Fillet*.}}

## Création de texte gravé 

14\. Revenez à l\'[Atelier Part](Part_Workbench/fr.md).

   *   14.1. Passez au style de dessin \"Comme actuellement\" avec **Affichage → [16px](Std_DrawStyle/fr___Style_de_représentation]]_→_[[File   *DrawStyleAsIs.svg.md) Comme actuellement** ou appuyez sur le **[Comme actuellement](File   *DrawStyleAsIs.svg   16px]] [[Std_DrawStyle.md)** bouton dans la barre d\'outils de la vue. Cela montrera tous les objets avec l\'ombrage et la couleur normaux.
   *   14.2. Dans la [Vue en arborescence](tree_view.md), sélectionnez {{incode   Sketch}} et appuyez sur **Espace** sur le clavier pour le rendre invisible.

15\. Dans la [Vue en arborescence](tree_view.md), sélectionnez d\'abord {{incode   Chamfer}} puis {{incode   Extrude}}.

   *   15.1. Appuyez ensuite sur **[Soustraction](File   *Part_Cut.svg   16px]] [[Part_Cut/fr.md)**. Cela créera un objet {{incode   Cut}}. Ceci est l\'objet terminé.
   *   
    **Remarque   ***l\'ordre dans lequel vous sélectionnez les objets est important pour l\'opération de découpe. L\'objet de base est sélectionné en premier et l\'objet soustractif arrive à la fin.
   *   15.2. Dans la [Vue en arborescence](tree_view.md), sélectionnez {{incode   Cut}}, dans l\'onglet **Affichage**, changez la valeur de **Line Width** en {{incode   2.0}}.

![](images/08_T04_Part_ShapesString_Extrude_final_cut.png ) 
*Modèle terminé d'un cube avec filet avec du texte gravé créé à partir des opérations ShapeString, extrusion et soustraction bouléenne.*

## Gravure de texte 3D avec l\'atelier PartDesign 

Un processus similaire à celui décrit ci-dessus peut être effectué avec l\'[Atelier PartDesign](PartDesign_Workbench/fr.md).

1.  Créez d\'abord le **[Draft Formes à partir texte](File   *Draft_ShapeString.svg   16px]] [[Draft_ShapeString/fr.md)**.
2.  Créez un **[PartDesign Corps](File   *PartDesign_Body_Tree.svg   16px]] [[PartDesign_Body/fr.md)**, rendez-le actif et ajoutez un solide de base en ajoutant des primitives ou en utilisant une esquisse et en l\'extrudant avec **[PartDesign Protrusion](File   *PartDesign_Pad.svg   16px]] [[PartDesign_Pad/fr.md)**.
3.  Déplacez l\'objet {{incode   ShapeString}} dans le corps actif.
4.  Attachez l\'objet {{incode   ShapeString}} à l\'une des faces du solide ou à un **[PartDesign Plan de référence](File   *PartDesign_Plane.svg   16px]] [[PartDesign Plane/fr.md)**, en utilisant **[Part Accrochage](File   *Part_EditAttachment.svg   16px]] [[Part_EditAttachment/fr.md)**.
5.  Créez maintenant un **[PartDesign Protrusion](File   *PartDesign_Pad.svg   16px]] [[PartDesign_Pad/fr.md)** ou un **[PartDesign Cavité](File   *PartDesign_Pocket.svg   16px]] [[PartDesign_Pocket/fr.md)** à partir de {{incode   ShapeString}}, afin de produire un additif ou une soustraction [PartDesign Feature](PartDesign_Feature/fr.md) du corps de base, respectivement.

Voir le fil du forum [How to use ShapeStrings in PartDesign](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=36623).

## Remarques

-   pour créer un texte courbé, vous pouvez utiliser <img alt="" src=images/FCCircularTextButtom.png  style="width   *32px;"> [Macro FCCircularText](Macro_FCCircularText/fr.md).
-   pour importer du texte depuis Inkscape, regardez l\' [Importation de texte à partir du tutoriel Inkscape](Import_text_and_geometry_from_Inkscape/fr.md).


  {{PartDesign Tools navi}} {{Sketcher Tools navi}} {{Userdocnavi
---



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Part](Category_Part.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > [Draft](Draft_Workbench.md) > Draft ShapeString tutorial/fr
