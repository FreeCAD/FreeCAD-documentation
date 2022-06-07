# SheetMetal Examples/fr
{{TOCright}}

## Introduction

L\'atelier SheetMetal est devenu très puissant et exige une documentation appropriée.

Pour éviter de surcharger les pages d\'outils avec des exemples, cette page a été ajoutée pour rassembler les pièces montrant et expliquant les caractéristiques spéciales de SheetMetal.

Phases planifiées pour générer du contenu    *

1.  Collecte d\'images
2.  Ajout de descriptions de flux de travail
3.  Ajout de tutoriels plus détaillés

## Charnière

<img alt="" src=images/SheetMetal_Example-01.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-01a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-01b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-01c.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-01d.png  style="width   *200px;"> 
*Processus de travail pour une charnière   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/PartDesign_Pocket.svg" width=16px> [PartDesign Cavité](PartDesign_Pocket/fr.md)**,
**<img src="images/PartDesign_Hole.svg" width=16px> [PartDesign Perçage](PartDesign_Hole/fr.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold/fr.md)**.
}}


<div class="mw-collapsible mw-collapsed">

### Charnière étape par étape 


<div class="mw-collapsible-content toccolours">

1.  Créez un profil (une ligne et un arc tangent), de préférence en utilisant l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;">[atelier Sketcher](Sketcher_Workbench/fr.md).
2.  Activez <img alt="" src=images/SheetMetal_AddBase.svg  style="width   *16px;"> [Make Base Wall](SheetMetal_AddBase/fr.md) pour créer un objet BaseBend.
3.  Modifiez les paramètres de l\'objet BaseBend    *
    -   Définissez **Mid Plane** sur `True` pour que le profil s\'étende symétriquement des deux côtés du plan de l\'esquisse.
    -   Donnez à **radius** et **thickness** les valeurs de votre choix.
4.  Créez un contour découpé avec l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;">[atelier Sketcher](Sketcher_Workbench/fr.md).
5.  Utilisez <img alt="" src=images/PartDesign_Pocket.svg  style="width   *16px;"> [PartDesign Cavité](PartDesign_Pocket/fr.md) pour couper la moitié du bout rond.
6.  Créez un modèle de trou avec l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;">[atelier Sketcher](Sketcher_Workbench/fr.md)
7.  Utilisez <img alt="" src=images/PartDesign_Hole.svg  style="width   *16px;"> [PartDesign Perçage](PartDesign_Hole/fr.md). Évitez les options Chambrage et Fraisure pour que le corps reste dépliable.
8.  Activez la commande <img alt="" src=images/SheetMetal_Unfold.svg  style="width   *16px;"> [Unfold](SheetMetal_Unfold/fr.md) pour obtenir un objet déplié.
9.  C\'est fait !


</div>


</div>

## Clip papier 

<img alt="" src=images/SheetMetal_Example-02.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-02a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-02b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-02c.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-02d.png  style="width   *200px;"> 
*Processus de travail pour un clip papier   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/SheetMetal_SketchOnSheet.svg" width=16px> [Sketch on Sheet](SheetMetal_SketchOnSheet/fr.md)**,
cloner, retourner et fusionner,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold/fr.md)**.
}}


<div class="mw-collapsible mw-collapsed">

### Clip papier étape par étape 


<div class="mw-collapsible-content toccolours">

1.  Créez un profil, de préférence en utilisant l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;">[atelier Sketcher](Sketcher_Workbench/fr.md) sur le plan XZ.
    <img alt="Esquisse du profil" src=images/SheetMetal_Example-02e.png  style="width   *300px;">
2.  Activez <img alt="" src=images/SheetMetal_AddBase.svg  style="width   *16px;"> [Make Base Wall](SheetMetal_AddBase/fr.md) pour créer un objet BaseBend.
3.  Modifiez les paramètres de l\'objet BaseBend dans le panneau des propriétés   *
    <img alt="Objet BaseBend et esquisse en surbrillance" src=images/SheetMetal_Example-02f.png  style="width   *200px;">.
    -   Définissez **mid plane** sur `True` pour que le profil s\'étende symétriquement des deux côtés du plan de l\'esquisse.
    -   Définissez **length** sur 32 mm.
    -   Donnez à **radius** la valeur 2 mm.
    -   Définissez **thickness** à 0,3 mm.
4.  Sélectionnez la face entre les sections rondes et activez l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width   *16px;">[atelier Sketcher](Sketcher_Workbench/fr.md).
    <img alt="Face pour supporter l\'esquisse" src=images/SheetMetal_Example-02g.png  style="width   *200px;">
5.  Pour cacher la partie recourbée, utilisez <img alt="" src=images/Sketcher_ViewSection.svg  style="width   *16px;"> [Sketcher Vue en section](Sketcher_ViewSection/fr.md).
6.  Créez le contour de la découpe.
    <img alt="Contour de la découpe" src=images/SheetMetal_Example-02h.png  style="width   *" height="240px;"> <img alt="Contour découpé touchant légèrement la face sélectionnée" src=images/SheetMetal_Example-02i.png  style="width   *" height="240px;">
7.  Terminez l\'esquisse en utilisant <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width   *16px;"> [Sketcher Quitter l\'esquisse](Sketcher_LeaveSketch/fr.md).
8.  Sélectionnez à nouveau la face et ajoutez l\'esquisse de découpe à la sélection.
    <img alt="Face et esquisse sélectionnées" src=images/SheetMetal_Example-02j.png  style="width   *200px;">
9.  Utilisez l\'outil <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width   *16px;"> [Sketch on Sheet](SheetMetal_SketchOnSheet/fr.md) pour découper autour de la partie recourbée.
    <img alt="Première moitié finie" src=images/SheetMetal_Example-02b.png  style="width   *200px;">
10. Un côté est terminé. Nous devons maintenant trouver un moyen d\'inverser le corps.

*Options possibles pour la symétrie    **.

-   La commande <img alt="" src=images/PartDesign_Mirrored.svg  style="width   *16px;"> [PartDesign Symétrie](PartDesign_Mirrored/fr.md) échoue car elle ne peut pas gérer les caractéristiques SheetMetal pour une raison inconnue. Cela ne fonctionne donc pas.
-   La commande <img alt="" src=images/Part_Mirror.svg  style="width   *16px;"> [Part Miroir](Part_Mirror/fr.md) crée une pièce miroir, mais celle-ci n\'est plus dépliable. Cela ne fonctionne pas non plus.
-   La seule solution qui peut fonctionner est d\'utiliser un clone. Celui-ci ne peut toujours pas être symétrisé, mais il peut utiliser la symétrie axiale (le tourner de 180°).
-   Un autre moyen qui fonctionne est d\'utiliser un objet de liaison.

**Symétrie utilisant un clone    ***

1.  Sélectionnez le corps dans l\'arborescence.
2.  Utilisez <img alt="" src=images/PartDesign_Clone.svg  style="width   *16px;"> [PartDesign Clone](PartDesign_Clone/fr.md). Cela ajoute un nouveau corps contenant un objet clone.
    Pour appliquer un retournement de 180°, réglez **Angle** sous la propriété Placement du corps ou du clone sur 180°. (L\'axe Z est par défaut et devrait convenir si vous avez commencé sur le plan XZ comme décrit).
    <img alt="Moitié clonée" src=images/SheetMetal_Example-02b.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="Moitié clonée inversée" src=images/SheetMetal_Example-02l.png  style="width   *200px;">
3.  Avec le corps toujours actif, utilisez une <img alt="" src=images/PartDesign_Boolean.svg  style="width   *16px;"> [PartDesign Opération booléenne](PartDesign_Boolean/fr.md) pour ajouter le corps du clone et fusionner les deux moitiés.
    <img alt="Moitiés fusionnées" src=images/SheetMetal_Example-02c.png  style="width   *200px;">
4.  Activez le <img alt="" src=images/SheetMetal_Unfold.svg  style="width   *16px;"> [Unfold](SheetMetal_Unfold/fr.md) pour obtenir un objet déplié.
    <img alt="Clip et objet déplié" src=images/SheetMetal_Example-02m.png  style="width   *200px;"> <img alt="Objet déplié" src=images/SheetMetal_Example-02d.png  style="width   *200px;">
5.  C\'est fait !

**Symétrie utilisant un objet de liaison    ***

1.  Sélectionnez le corps dans l\'arborescence.
2.  Utilisez la commande <img alt="" src=images/Std_LinkMake.svg  style="width   *16px;"> [Créer un lien](Std_LinkMake/fr.md). Cela ajoute un nouvel objet lien.
3.  Dupliquez l\'objet lien en fixant la propriété **Element Count** à 2.
4.  Pour appliquer un retournement de 180°, définissez **Angle** sous la propriété Placement de l\'un ou l\'autre des objets sous-liés sur 180°. (L\'axe Z est la valeur par défaut et devrait convenir si vous avez commencé sur le plan XZ comme décrit).
5.  Sélectionnez les deux objets sous-liés dans l\'arborescence.
6.  Activez la fonction <img alt="" src=images/Part_Fuse.svg  style="width   *16px;"> [Part Union](Part_Fuse/fr.md) pour fusionner les deux moitiés.
    <img alt="Moitiés fusionnées" src=images/SheetMetal_Example-02c.png  style="width   *200px;">
7.  Activez la commande <img alt="" src=images/SheetMetal_Unfold.svg  style="width   *16px;"> [Unfold](SheetMetal_Unfold/fr.md) pour obtenir un objet déplié.

<img alt="Clip et objet déplié" src=images/SheetMetal_Example-02m.png  style="width   *200px;"> <img alt="Objet déplié" src=images/SheetMetal_Example-02d.png  style="width   *200px;">

1.  C\'est fait !


</div>


</div>

## Collier oméga 

<img alt="" src=images/SheetMetal_Example-03.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-03a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-03b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-03.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-03c.png  style="width   *200px;"> 
*Processus de travail pour un collier oméga   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/PartDesign_Hole.svg" width=16px> [PartDesign Perçage](PartDesign_Hole/fr.md)**,
**<img src="images/PartDesign_Fillet.svg" width=16px> [PartDesign Congé](PartDesign_Fillet/fr.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold/fr.md)**.
}}

## Bol hexagonal 

<img alt="" src=images/SheetMetal_Example-04.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-04a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-04b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-04.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-04c.png  style="width   *200px;"> 
*Processus de travail pour un bol hexagonal   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/SheetMetal_AddWall.svg" width=16px> [Make Wall](SheetMetal_AddWall/fr.md)**,
6x **<img src="images/SheetMetal_AddCornerRelief.svg" width=16px> [Add Corner Relief](SheetMetal_AddCornerRelief/fr.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold/fr.md)**.
}}

<img alt="" src=images/SheetMetal_Example-04d.png  style="width   *200px;">

Lorsqu\'un grugeage d\'angle est ajouté (côté droit), il peut être nécessaire d\'ajuster la valeur de la propriété *Taille*.

## Pince à crayon 

<img alt="" src=images/SheetMetal_Example-05.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-05a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-05b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-05c.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-05d.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-05.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-05e.png  style="width   *200px;"> 
*Processus de travail pour une pince à crayon   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/PartDesign_Pocket.svg" width=16px> [PartDesign Cavité](PartDesign_Pocket/fr.md)**,
3x **<img src="images/SheetMetal_AddWall.svg" width=16px> [Make Wall](SheetMetal_AddWall/fr.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold/fr.md)**.
}}

## Exemple de dépliage 

<img alt="" src=images/SheetMetal_Example-06.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-06a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-06b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-06c.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-06.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-06d.png  style="width   *200px;"> 
*Processus de travail pour déplier   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/SheetMetal_AddWall.svg" width=16px> [Make Wall](SheetMetal_AddWall/fr.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Extend Face](SheetMetal_Extrude/fr.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Extend Face](SheetMetal_Extrude/fr.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold/fr.md)**.
}}

Pour la deuxième utilisation de **Extend Face**, une Esquisse avec deux contours est utilisée pour la forme de l\'extension(s) et avec la valeur de \"use subtraction\" réglée à true, elle fournit la forme pour les découpes aussi.

## Blindage d\'USB 

<img alt="" src=images/SheetMetal_Example-07.png  style="width   *400px;">
<img alt="" src=images/SheetMetal_Example-07a.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-07b.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-07c.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-07d.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-07.png  style="width   *200px;"> <img alt="" src=images/SheetMetal_Example-07e.png  style="width   *200px;"> 
*Processus de travail pour un blindage d'USB   *
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/SheetMetal_Extrude.svg" width=16px> [Extend Face](SheetMetal_Extrude/fr.md)**,
**<img src="images/PartDesign_Pocket.svg" width=16px> [PartDesign Cavité](PartDesign_Pocket/fr.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Extend Face](SheetMetal_Extrude/fr.md)**,
**<img src="images/SheetMetal_AddWall.svg" width=16px> [Make Wall](SheetMetal_AddWall/fr.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold/fr.md)**.
}}

(La forme de la languette n\'est qu\'une vision artistique de ce qui pourrait être caché à l\'intérieur d\'une vraie prise).

## Propriétés de SheetMetal 

Cette section tente d\'expliquer les propriétés de chaque objet SheetMetal à l\'aide d\'images simples, le cas échéant.


<div class="mw-collapsible mw-collapsed">

### Objet BaseBend <img alt="" src=images/SheetMetal_AddBase.svg  style="width   *24px;"> 


<div class="mw-collapsible-content toccolours">

<img alt="" src=images/SheetMetal_Example-08a.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08b.png  style="width   *200px;">



*Esquisse sélectionnée + 
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase/fr.md)* 
→ Objet BaseBend avec les paramètres par défaut**

<img alt="" src=images/SheetMetal_Example-08b.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08c.png  style="width   *200px;">



*Modification de **length*    * Longueur par défaut → Longueur réduite**

<img alt="" src=images/SheetMetal_Example-08d.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08h.png  style="width   *200px;">



*Bascule de **Mid Plane* de {{False** à `True`    * Extrusion dans une seule direction → Extrusion symétrique}}

<img alt="" src=images/SheetMetal_Example-08d.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08e.png  style="width   *200px;">



*Bascule de **Reverse* de {{False** à `True`    * Direction par défaut → Direction inversée}}

<img alt="" src=images/SheetMetal_Example-08e.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08f.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08g.png  style="width   *200px;">



*Sélection de **Bend Side*    * {{value|Outside**. (par défaut) → {{value|Inside}} → {{value|Milieu}}}}

<img alt="" src=images/SheetMetal_Example-08e.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08i.png  style="width   *200px;">



*Modification de **radius*    * Rayon par défaut → Rayon agrandi.<br>
Cette propriété est le rayon intérieur des pliures créées aux sommets où deux arêtes de l'esquisse ont une transition non tangentielle.**

<img alt="" src=images/SheetMetal_Example-08e.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-08j.png  style="width   *200px;">



*Modification de **thickness*    * Épaisseur par défaut → Épaisseur agrandie**


</div>


</div>


<div class="mw-collapsible mw-collapsed">

### Bend object <img alt="" src=images/SheetMetal_AddWall.svg  style="width   *24px;"> 


<div class="mw-collapsible-content toccolours">

A Bend object consists of sets of one cylindrical bend and one planar strip each. Each pair extends from a selected edge of a blank.

<img alt="" src=images/SheetMetal_Example-09a.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09b.png  style="width   *200px;">



*Selected edges + 
**<img src="images/SheetMetal_AddWall.svg" width=16px> [Make Wall](SheetMetal_AddWall.md)* 
→ Bend objects with default settings <br>
(Two Bend objects in two separate bodies.)**

Edit **radius** to vary the inner radius of all bends supplied by a Bend object. (See BaseBend object above)

Edit **length** to vary the length of all planar strips extending from the bends of a Bend object.

   *   Don\'t confuse the **length** with a flange length which is the sum of this length, radius, and thickness (90° only).

<img alt="" src=images/SheetMetal_Example-09b.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09c.png  style="width   *200px;">



*Switch **invert* from {{FALSE** to `True`   *Default flanges (Bend objects) → Inverted flanges}}

<img alt="" src=images/SheetMetal_Example-09c.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09d.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09e.png  style="width   *200px;">



*Edit **angle*   *Default angle (90°) → Enlarged angle → Decreased angle**

We don\'t have to care about trimming the edges, because **Auto Miter** is activated by default.
If deactivated, the result would look like this   *

<img alt="" src=images/SheetMetal_Example-09m.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09f.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09g.png  style="width   *200px;">



*Switch **Auto Miter* from {{TRUE** to `False`   * Default angle (90°) → Enlarged angle → Decreased angle<br>
(Auto Miter has no effect on single flanges)}}

To manually miter a flange edge **miterangle1** and **miterangle2** are used   *

<img alt="" src=images/SheetMetal_Example-09m.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09n.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09o.png  style="width   *200px;">



*Edit **miterangle1* and {{PropertyData|miterangle2**   * No miter (default) → Differently mitered edges, positive angle → Symmetrically mitered edges, negative angles}}

Mitering only effects the planar strips, not the bends.

   *   (It takes the whole edge into account and so cannot be used to chamfer flange edges)

To display the different choices of **Bend Type** we introduce an auxiliary cuboid that extrudes from the same outline as the blank and has the same height as the Bend object (its flange length).

<img alt="" src=images/SheetMetal_Example-09h.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09i.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09j.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09k.png  style="width   *200px;">



*Select **Bend Type*   * {{value|Material Outside** (default) → {{value|Material Inside}} → {{value|Thickness Outside}} → {{value|Offset}}}}

-   Outside   * The bend starts at the selected edge (The whole Bend object lies outside the cuboid).
-   Inside   * The outer side of the bend ends on the cuboid surface (The whole Bend object lies inside the cuboid).
-   Thickness Outside   * The inner side of the bend ends on the cuboid surface (only the planar strip is protruding from the cuboid surface).
-   Offset   * According to the value of **offset** the bend is moved in outward direction from its default position.

   *   An extension is inserted for positive values (high-lighted strip).
   *   Negative values are allowed to move the bend inwards.

If we don\'t want to use the whole length of an edge we can use **gap1** and **gap2**.

<img alt="" src=images/SheetMetal_Example-09c.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09l.png  style="width   *200px;">



*Edit **gap1* and {{PropertyData|gap2**   * Default flanges → Flanges with different values for gap1 and gap2}}

If the length of a gap reaches or extends the value of **min Relief Gap**, a relief will be added to the gap.
Reliefs are controlled by **relief Type**, **reliefd** (relief depth), and **reliefw** (relief width) which are enabled only when a gap value is set.

<img alt="" src=images/SheetMetal_Example-09p.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09q.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09r.png  style="width   *200px;">



*Edit **reliefd* and {{PropertyData|reliefw**   * Default values → Relief depth enlarged → Relief depth and width enlarged}}

<img alt="" src=images/SheetMetal_Example-09r.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_Example-09s.png  style="width   *200px;">



*Switch **relief Type* from {{value|Rectangle** to {{value|Round}}   * Default rectangular relief → Round relief}}

The round option will only be applied, if the relief depth is larger than the relief width.

Switch **Use Relief Factor** from `False` (default) to `True` to set the values of **reliefd** and **reliefw** automatically. Both are set to the object\'s (inherited) thickness multiplied by the value of **Relief Factor**.

   *   In this case the round option is useless, since the relief depth is as large as the relief width. (See above)


</div>


</div>

[Category   *SheetMetal](Category_SheetMetal.md) [Category   *Addons](Category_Addons.md) [Category   *External Command Reference](Category_External_Command_Reference.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Examples/fr
