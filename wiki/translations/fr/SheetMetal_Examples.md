# SheetMetal Examples/fr
## Introduction

L\'<img alt="" src=images/Sheetmetal_workbench_icon.svg  style="width:24px;"> [atelier SheetMetal](SheetMetal_Workbench/fr.md) (un [atelier externe](External_workbenches/fr.md) disponible via le [Gestionnaire des extensions](Std_AddonMgr/fr.md)) est devenu assez puissant et mérite d\'être documenté de manière appropriée.

Pour éviter de surcharger les pages d\'outils avec des exemples, cette page a été ajoutée pour rassembler les pièces montrant et expliquant les caractéristiques spéciales de SheetMetal.

Phases planifiées pour générer du contenu :

1.  Collecte d\'images
2.  Ajout de descriptions de flux de travail
3.  Ajout de tutoriels plus détaillés



## Charnière

<img alt="" src=images/SheetMetal_Example-01.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-01a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-01b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-01c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-01d.png  style="width:200px;"> 
*Processus de travail pour une charnière:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/PartDesign_Pocket.svg" width=16px> [PartDesign Cavité](PartDesign_Pocket/fr.md)**,
**<img src="images/PartDesign_Hole.svg" width=16px> [PartDesign Perçage](PartDesign_Hole/fr.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold/fr.md)**.
}}


<div class="mw-collapsible mw-collapsed">

### Charnière étape par étape 


<div class="mw-collapsible-content toccolours">

1.  Créez un profil (une ligne et un arc tangent), de préférence en utilisant l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;">[atelier Sketcher](Sketcher_Workbench/fr.md).
2.  Activez <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Make Base Wall](SheetMetal_AddBase/fr.md) pour créer un objet BaseBend.
3.  Modifiez les paramètres de l\'objet BaseBend :
    -   Définissez **Mid Plane** sur `True` pour que le profil s\'étende symétriquement des deux côtés du plan de l\'esquisse.
    -   Donnez à **radius** et **thickness** les valeurs de votre choix.
4.  Créez un contour découpé avec l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;">[atelier Sketcher](Sketcher_Workbench/fr.md).
5.  Utilisez <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [PartDesign Cavité](PartDesign_Pocket/fr.md) pour couper la moitié du bout rond.
6.  Créez un modèle de trou avec l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;">[atelier Sketcher](Sketcher_Workbench/fr.md)
7.  Utilisez <img alt="" src=images/PartDesign_Hole.svg  style="width:16px;"> [PartDesign Perçage](PartDesign_Hole/fr.md). Évitez les options Chambrage et Fraisure pour que le corps reste dépliable.
8.  Activez la commande <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Unfold](SheetMetal_Unfold/fr.md) pour obtenir un objet déplié.
9.  C\'est fait !


</div>


</div>



## Clip papier 

<img alt="" src=images/SheetMetal_Example-02.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-02a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-02b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-02c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-02d.png  style="width:200px;"> 
*Processus de travail pour un clip papier:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Tôle de base](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/SheetMetal_SketchOnSheet.svg" width=16px> [Découper des trous](SheetMetal_SketchOnSheet/fr.md)**,
cloner, retourner et fusionner,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Déplier](SheetMetal_Unfold/fr.md)**.
}}


<div class="mw-collapsible mw-collapsed">

### Clip papier étape par étape 


<div class="mw-collapsible-content toccolours">

1.  Créez un profil, de préférence en utilisant l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;">[atelier Sketcher](Sketcher_Workbench/fr.md) sur le plan XZ.
    <img alt="Esquisse du profil" src=images/SheetMetal_Example-02e.png  style="width:300px;">
2.  Activez <img alt="" src=images/SheetMetal_AddBase.svg  style="width:16px;"> [Tôle de base](SheetMetal_AddBase/fr.md) pour créer un objet BaseBend.
3.  Modifiez les paramètres de l\'objet BaseBend dans le panneau des propriétés:
    <img alt="Objet BaseBend et esquisse en surbrillance" src=images/SheetMetal_Example-02f.png  style="width:200px;">.
    -   Définissez **mid plane** sur `True` pour que le profil s\'étende symétriquement des deux côtés du plan de l\'esquisse.
    -   Définissez **length** sur 32 mm.
    -   Donnez à **radius** la valeur 2 mm.
    -   Définissez **thickness** à 0,3 mm.
4.  Sélectionnez la face entre les sections rondes et activez l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;">[atelier Sketcher](Sketcher_Workbench/fr.md).
    <img alt="Face pour supporter l\'esquisse" src=images/SheetMetal_Example-02g.png  style="width:200px;">
5.  Pour cacher la partie recourbée, utilisez <img alt="" src=images/Sketcher_ViewSection.svg  style="width:16px;"> [Sketcher Vue de la section](Sketcher_ViewSection/fr.md).
6.  Créez le contour de la découpe.
    <img alt="Contour de la découpe" src=images/SheetMetal_Example-02h.png  style="width:" height="240px;"> <img alt="Contour découpé touchant légèrement la face sélectionnée" src=images/SheetMetal_Example-02i.png  style="width:" height="240px;">
7.  Terminez l\'esquisse en utilisant <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:16px;"> [Sketcher Quitter l\'esquisse](Sketcher_LeaveSketch/fr.md).
8.  Sélectionnez à nouveau la face et ajoutez l\'esquisse de découpe à la sélection.
    <img alt="Face et esquisse sélectionnées" src=images/SheetMetal_Example-02j.png  style="width:200px;">
9.  Utilisez l\'outil <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:16px;"> [Découper des trous](SheetMetal_SketchOnSheet/fr.md) pour découper autour de la partie recourbée.
    <img alt="Première moitié finie" src=images/SheetMetal_Example-02b.png  style="width:200px;">
10. Un côté est terminé. Nous devons maintenant trouver un moyen d\'inverser le corps.

*Options possibles pour la symétrie :*.

-   La commande <img alt="" src=images/PartDesign_Mirrored.svg  style="width:16px;"> [PartDesign Symétrie](PartDesign_Mirrored/fr.md) échoue car elle ne peut pas gérer les caractéristiques SheetMetal pour une raison inconnue. Cela ne fonctionne donc pas.
-   La commande <img alt="" src=images/Part_Mirror.svg  style="width:16px;"> [Part Objet en miroir](Part_Mirror/fr.md) crée une pièce miroir, mais celle-ci n\'est plus dépliable. Cela ne fonctionne pas non plus.
-   La seule solution qui peut fonctionner est d\'utiliser un clone. Celui-ci ne peut toujours pas être symétrisé, mais il peut utiliser la symétrie axiale (le tourner de 180°).
-   Un autre moyen qui fonctionne est d\'utiliser un objet de liaison.

**Symétrie utilisant un clone :**

1.  Sélectionnez le corps dans l\'arborescence.
2.  Utilisez <img alt="" src=images/PartDesign_Clone.svg  style="width:16px;"> [PartDesign Clone](PartDesign_Clone/fr.md). Cela ajoute un nouveau corps contenant un objet clone.
    Pour appliquer un retournement de 180°, réglez **Angle** sous la propriété Placement du corps ou du clone sur 180°. (L\'axe Z est par défaut et devrait convenir si vous avez commencé sur le plan XZ comme décrit).
    <img alt="Moitié clonée" src=images/SheetMetal_Example-02b.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="Moitié clonée inversée" src=images/SheetMetal_Example-02l.png  style="width:200px;">
3.  Avec le corps toujours actif, utilisez une <img alt="" src=images/PartDesign_Boolean.svg  style="width:16px;"> [PartDesign Opération booléenne](PartDesign_Boolean/fr.md) pour ajouter le corps du clone et fusionner les deux moitiés.
    <img alt="Moitiés fusionnées" src=images/SheetMetal_Example-02c.png  style="width:200px;">
4.  Activez le <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Unfold](SheetMetal_Unfold/fr.md) pour obtenir un objet déplié.
    <img alt="Clip et objet déplié" src=images/SheetMetal_Example-02m.png  style="width:200px;"> <img alt="Objet déplié" src=images/SheetMetal_Example-02d.png  style="width:200px;">
5.  C\'est fait !

**Symétrie utilisant un objet de liaison :**

1.  Sélectionnez le corps dans l\'arborescence.
2.  Utilisez la commande <img alt="" src=images/Std_LinkMake.svg  style="width:16px;"> [Créer un lien](Std_LinkMake/fr.md). Cela ajoute un nouvel objet lien.
3.  Dupliquez l\'objet lien en fixant la propriété **Element Count** à 2.
4.  Pour appliquer un retournement de 180°, définissez **Angle** sous la propriété Placement de l\'un ou l\'autre des objets sous-liés sur 180°. (L\'axe Z est la valeur par défaut et devrait convenir si vous avez commencé sur le plan XZ comme décrit).
5.  Sélectionnez les deux objets sous-liés dans l\'arborescence.
6.  Activez la fonction <img alt="" src=images/Part_Fuse.svg  style="width:16px;"> [Part Union](Part_Fuse/fr.md) pour fusionner les deux moitiés.
    <img alt="Moitiés fusionnées" src=images/SheetMetal_Example-02c.png  style="width:200px;">
7.  Activez la commande <img alt="" src=images/SheetMetal_Unfold.svg  style="width:16px;"> [Unfold](SheetMetal_Unfold/fr.md) pour obtenir un objet déplié.

<img alt="Clip et objet déplié" src=images/SheetMetal_Example-02m.png  style="width:200px;"> <img alt="Objet déplié" src=images/SheetMetal_Example-02d.png  style="width:200px;">

1.  C\'est fait !


</div>


</div>



## Collier oméga 

<img alt="" src=images/SheetMetal_Example-03.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-03a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-03b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-03.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-03c.png  style="width:200px;"> 
*Processus de travail pour un collier oméga:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/PartDesign_Hole.svg" width=16px> [PartDesign Perçage](PartDesign_Hole/fr.md)**,
**<img src="images/PartDesign_Fillet.svg" width=16px> [PartDesign Congé](PartDesign_Fillet/fr.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Unfold](SheetMetal_Unfold/fr.md)**.
}}



## Bol hexagonal 

<img alt="" src=images/SheetMetal_Example-04.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-04a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-04b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-04.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-04c.png  style="width:200px;"> 
*Processus de travail pour un bol hexagonal :
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Tôle de base](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/SheetMetal_AddWall.svg" width=16px> [Rebord](SheetMetal_AddWall/fr.md)**,
6x **<img src="images/SheetMetal_AddCornerRelief.svg" width=16px> [Grugeage](SheetMetal_AddCornerRelief/fr.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Déplier](SheetMetal_Unfold/fr.md)**.
}}

<img alt="" src=images/SheetMetal_Example-04d.png  style="width:200px;">

Lorsqu\'un grugeage d\'angle est ajouté (côté droit), il peut être nécessaire d\'ajuster la valeur de la propriété *Taille*.



## Pince à crayon 

<img alt="" src=images/SheetMetal_Example-05.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-05a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05d.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-05e.png  style="width:200px;"> 
*Processus de travail pour une pince à crayon :
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Tôle de base](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/PartDesign_Pocket.svg" width=16px> [PartDesign Cavité](PartDesign_Pocket/fr.md)**,
3x **<img src="images/SheetMetal_AddWall.svg" width=16px> [Rebord](SheetMetal_AddWall/fr.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Déplier](SheetMetal_Unfold/fr.md)**.
}}



## Exemple de dépliage 

<img alt="" src=images/SheetMetal_Example-06.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-06a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-06b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-06c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-06.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-06d.png  style="width:200px;"> 
*Processus de travail pour déplier:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Tôle de base](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/SheetMetal_AddWall.svg" width=16px> [Rebord](SheetMetal_AddWall/fr.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Prolonger une face](SheetMetal_Extrude/fr.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Prolonger une face](SheetMetal_Extrude/fr.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Déplier](SheetMetal_Unfold/fr.md)**.
}}

Pour la deuxième utilisation de **Extend Face**, une Esquisse avec deux contours est utilisée pour la forme de l\'extension(s) et avec la valeur de \"use subtraction\" réglée à true, elle fournit la forme pour les découpes aussi.



## Blindage d\'USB 

<img alt="" src=images/SheetMetal_Example-07.png  style="width:400px;">
<img alt="" src=images/SheetMetal_Example-07a.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-07b.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-07c.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-07d.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-07.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-07e.png  style="width:200px;"> 
*Processus de travail pour un blindage d'USB:
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Tôle de base](SheetMetal_AddBase/fr.md)*,
{{Button|<img src="images/SheetMetal_Extrude.svg" width=16px> [Prolonger une face](SheetMetal_Extrude/fr.md)**,
**<img src="images/PartDesign_Pocket.svg" width=16px> [PartDesign Cavité](PartDesign_Pocket/fr.md)**,
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Prolonger une face](SheetMetal_Extrude/fr.md)**,
**<img src="images/SheetMetal_AddWall.svg" width=16px> [Rebord](SheetMetal_AddWall/fr.md)**,
**<img src="images/SheetMetal_Unfold.svg" width=16px> [Déplier](SheetMetal_Unfold/fr.md)**.
}}

(La forme de la languette n\'est qu\'une vision artistique de ce qui pourrait être caché à l\'intérieur d\'une vraie prise).



## Propriétés de SheetMetal 

Cette section tente d\'expliquer les propriétés de chaque objet SheetMetal à l\'aide d\'images simples, le cas échéant.


<div class="mw-collapsible mw-collapsed">

### Objet BaseBend <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> 


<div class="mw-collapsible-content toccolours">

<img alt="" src=images/SheetMetal_Example-08a.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08b.png  style="width:200px;">



*Esquisse sélectionnée + 
**<img src="images/SheetMetal_AddBase.svg" width=16px> [Make Base Wall](SheetMetal_AddBase/fr.md)* 
→ Objet BaseBend avec les paramètres par défaut**

<img alt="" src=images/SheetMetal_Example-08b.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08c.png  style="width:200px;">



*Modification de **length* : Longueur par défaut → Longueur réduite**

<img alt="" src=images/SheetMetal_Example-08d.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08h.png  style="width:200px;">



*Bascule de **Mid Plane* de {{False** à `True` : Extrusion dans une seule direction → Extrusion symétrique}}

<img alt="" src=images/SheetMetal_Example-08d.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08e.png  style="width:200px;">



*Bascule de **Reverse* de {{False** à `True` : Direction par défaut → Direction inversée}}

<img alt="" src=images/SheetMetal_Example-08e.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08f.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08g.png  style="width:200px;">



*Sélection de **Bend Side* : {{value|Outside**. (par défaut) → {{value|Inside}} → {{value|Milieu}}}}

<img alt="" src=images/SheetMetal_Example-08e.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08i.png  style="width:200px;">



*Modification de **radius* : Rayon par défaut → Rayon agrandi.<br>
Cette propriété est le rayon intérieur des pliures créées aux sommets où deux arêtes de l'esquisse ont une transition non tangentielle.**

<img alt="" src=images/SheetMetal_Example-08e.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-08j.png  style="width:200px;">



*Modification de **thickness* : Épaisseur par défaut → Épaisseur agrandie**


</div>


</div>


<div class="mw-collapsible mw-collapsed">

### Objet Bend <img alt="" src=images/SheetMetal_AddWall.svg  style="width:24px;"> 


<div class="mw-collapsible-content toccolours">

Un objet Bend est constitué d\'ensembles comprenant chacun un pli cylindrique et une bande plane. Chaque paire s\'étend à partir d\'un bord sélectionné d\'une tôle.

<img alt="" src=images/SheetMetal_Example-09a.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09b.png  style="width:200px;">



*Bords sélectionnés + 
**<img src="images/SheetMetal_AddWall.svg" width=16px> [Rebord](SheetMetal_AddWall/fr.md)* → Plier les objets avec les paramètres par défaut <br>
(Deux objets pliés dans deux corps distincts.)**

Modifiez **radius** pour faire varier le rayon intérieur de tous les plis fournis par un objet Bend. (Voir l\'objet BaseBend ci-dessus)

Modifiez **length** pour faire varier la longueur de toutes les bandes planes s\'étendant depuis les plis d\'un objet Bend.

:   Ne confondez pas **length** avec une longueur de bride qui est la somme de cette longueur, du rayon et de l\'épaisseur (90° uniquement).

<img alt="" src=images/SheetMetal_Example-09b.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09c.png  style="width:200px;">



*Faire passer **invert* de {{FALSE** à `True` : Brides par défaut (objets Bend ) → Brides inversées}}

<img alt="" src=images/SheetMetal_Example-09c.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09d.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09e.png  style="width:200px;">



*Editer **angle* : Angle par défaut (90°) → Angle agrandi → Angle diminué**

Nous n\'avons pas à nous soucier de la coupe des bords, car **Auto Miter** est activé par défaut.
Si elle était désactivée, le résultat ressemblerait à ceci :

<img alt="" src=images/SheetMetal_Example-09m.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09f.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09g.png  style="width:200px;">



*Faites passer **Auto Miter* de {{TRUE** à `False` : Angle par défaut (90°) → Angle agrandi → Angle diminué.<br>
(Auto Miter n'a aucun effet sur les brides simples)}}

Pour réaliser manuellement l\'onglet d\'un bord de bride, on utilise *\'miterangle1* et *\'miterangle2* :

<img alt="" src=images/SheetMetal_Example-09m.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09n.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09o.png  style="width:200px;">



*Modifiez **miterangle1* et {{PropertyData|miterangle2** : Pas d'onglet (par défaut) → Bords à onglets différents, angle positif → Bords à onglets symétriques, angles négatifs}}

Les onglets n\'affectent que les bandes planes, pas les plis.

:   (Prise en compte de l\'ensemble du bord et ne peut donc pas être utilisé pour chanfreiner les bords des brides)

Pour montrer les différents choix de **Type de pliage**, nous introduisons un cuboïde auxiliaire qui extrude du même contour que la tôle et a la même hauteur que l\'objet Bend (sa longueur de bride).

<img alt="" src=images/SheetMetal_Example-09h.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09i.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09j.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09k.png  style="width:200px;">



*Sélectionnez **Bend Type* : {{value|Material Outside** (par défaut) → {{value|Material Inside}} → {{value|Thickness Outside}} → {{value|Offset}}}}

-   Extérieur : Le pli commence au bord sélectionné (l\'ensemble de l\'objet Bend se trouve à l\'extérieur du cuboïde).
-   Intérieur : Le côté extérieur du pli se termine sur la surface du cuboïde (l\'ensemble de l\'objet Bend se trouve à l\'intérieur du cuboïde).
-   Épaisseur extérieure : Le côté intérieur du pli se termine sur la surface du parallélépipède (seule la bande planaire dépasse de la surface du parallélépipède).
-   Décalage : Selon la valeur de **offset**, le pli est déplacé vers l\'extérieur à partir de sa position par défaut.

:   Une extension est insérée pour les valeurs positives (bande en surbrillance).
:   Les valeurs négatives permettent de déplacer le pli vers l\'intérieur.

Si nous ne voulons pas utiliser toute la longueur d\'un bord, nous pouvons utiliser **gap1** et **gap2**.

<img alt="" src=images/SheetMetal_Example-09c.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09l.png  style="width:200px;">



*Modifiez **gap1* et {{PropertyData|gap2** : Brides par défaut → Brides avec des valeurs différentes pour gap1 et gap2.}}

Si la longueur d\'un espace atteint ou dépasse la valeur de **min Relief Gap**, un grugeage sera ajouté à cet espace.
Les grugeages sont contrôlés par **relief Type**, **reliefd** (profondeur du grugeage), et **reliefw** (largeur du grugeage) qui ne sont activés que lorsqu\'une valeur d\'écart est définie.

<img alt="" src=images/SheetMetal_Example-09p.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09q.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09r.png  style="width:200px;">



*Modifiez **reliefd* et {{PropertyData|reliefw** : Valeurs par défaut → Profondeur du grugeage agrandi → Profondeur et largeur du grugeage agrandies}}

<img alt="" src=images/SheetMetal_Example-09r.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-09s.png  style="width:200px;">



*Faites passer **relief Type* de {{value|Rectangle** à {{value|Round}} : Grugeage rectangulaire par défaut → Grugeage rond}}

L\'option ronde ne sera appliquée que si la profondeur du grugeage est supérieure à la largeur du grugeage.

Faites passer **Use Relief Factor** de `False` (valeur par défaut) à `True` pour définir automatiquement les valeurs de **reliefd** et **reliefw**. Ces deux valeurs sont définies sur l\'épaisseur (héritée) de l\'objet multipliée par la valeur de **Relief Factor**.

:   Dans ce cas, l\'option ronde est inutile, puisque la profondeur du grugeage est aussi grande que la largeur du grugeage. (Voir ci-dessus)

Une nouvelle propriété **Length Spec** {{Version/fr|0.21}} nous permet de choisir comment mesurer la longueur de l\'objet Bend :

<img alt="" src=images/SheetMetal_Example-09t.png  style="width:500px;"> 
*Vue latérale de quatre brides de 120° avec une longueur par défaut (10 mm) et différentes valeurs de **Length Spec* : <br> {{value|Leg** (par défaut), {{value|Outer Sharp}}, {{value|Inner Sharp}}, {{value|Tangential}}}}

Lorsque l\'option {{value|Tangential}} est sélectionnée, la propriété **length** est l\'équivalent de la longueur de la bride.


{{value|Outer Sharp}}

et {{value|Tangential}} sont identiques pour des angles de 90°.


</div>


</div>


<div class="mw-collapsible mw-collapsed">

### Objet Extend <img alt="" src=images/SheetMetal_Extrude.svg  style="width:24px;"> 


<div class="mw-collapsible-content toccolours">

Un objet Extend permet de déplier une plaque de tôle sur une ou plusieurs faces ou bords sélectionnés.

<img alt="" src=images/SheetMetal_Example-10a.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10b.png  style="width:200px;">



*Faces et bords sélectionnés + 
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Extend Face](SheetMetal_Extrude/fr.md)* 
→ Un objet Extend avec des paramètres par défaut.**

Un premier problème se pose ici : bien que la propriété **Refine** soit mise à `True`, deux des extensions affichent toujours leurs lignes de couture. Seule l\'extension du dernier élément sélectionné sera affinée.

Pour affiner toutes les extensions, elles doivent être créées séparément :

<img alt="" src=images/SheetMetal_Example-10c.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10d.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10e.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10f.png  style="width:200px;">



*3x faces ou arêtes sélectionnées + 
**<img src="images/SheetMetal_Extrude.svg" width=16px> [Extend Face](SheetMetal_Extrude/fr.md)* 
→ Trois objets Extend complètement affinés et avec des paramètres par défaut.**

Les propriétés modifiées s\'appliquent à toutes les arêtes énumérées dans les **base Object** associées de l\'objet Extension.

Modifiez **length** pour ajuster la longueur de l\'extension.

<img alt="" src=images/SheetMetal_Example-10h.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Example-10g.png  style="width:200px;">



*Modifiez **gap1* et {{PropertyData|gap2** pour réduire la largeur de l'extension.<br>A gauche : objet Extension avec 3 bords. A droite : un des objets Extension avec un seul bord.}}

Liez une esquisse à la propriété **Sketch** pour former une extension. Les propriétés **length**, **gap1** et **gap2** seront ignorées une fois l\'esquisse liée. (Cela ne semble pas fonctionner avec des tôles encore non pliées).

<img alt="" src=images/SheetMetal_Example-10i.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10j.png  style="width:200px;">



*Une esquisse sélectionnée reposant sur le bord à prolonger → Extension résultante*

Il est évident que l\'arête sélectionnée pour l\'objet Extend n\'a pas d\'importance, la forme du bord est modifiée partout où la géométrie de l\'esquisse ressort, la nouvelle forme peut même contenir des parties déconnectées du bord d\'origine. Les multiples contours ne posent aucun problème, mais le bord n\'est pas découpé.

Cet exemple montre que les concepteurs sont responsables de leur construction et ne devraient pas se fier aux résultats de leurs outils, qui n\'ont pas de sens dans ce cas. L\'esquisse rattachée à un côté du bord est également problématique en raison du problème toponymique, mais pour cela une solution est en vue.

Mais il y a de meilleurs cas d\'utilisation pour cet outil impliquant des formes presque fermées comme l\'un des exemples de la page [SheetMetal Extrude](SheetMetal_Extrude/fr.md) :

<img alt="" src=images/SheetMetal_Example-10k.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10l.png  style="width:200px;">



*Un profil presque fermé → L'extension ajoutée par défaut est fusionnée avec le côté opposé, créant un profil fermé (un tube) qui n'est pas dépliable*

<img alt="" src=images/SheetMetal_Example-10l.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10m.png  style="width:200px;">



*Liez une esquisse rectangulaire à la propriété **Sketch* : profil fermé → Profil avec extension rectangulaire, encore fusionné**

<img alt="" src=images/SheetMetal_Example-10m.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Example-10n.png  style="width:200px;">



*Changez **Use Subtraction* à {{true** pour fournir un espace (à peine visible) par défaut entre l'objet Extension et le côté opposé, puis augmentez **Offset** pour élargir l'espace:<br>
Profilé fusionné → Profilé avec extension emboîtée, ce résultat final est dépliable}}


</div>


</div>


<div class="mw-collapsible mw-collapsed">

### Objet Fold <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:24px;"> 


<div class="mw-collapsible-content toccolours">

Un objet Fold est le résultat d\'une plaque de tôle pliée selon une ligne donnée.

Modifier la propriété **Position** pour contrôler la position du pli par rapport à la ligne de pliage.

<img alt="" src=images/SheetMetal_Example-10o.png  style="width:600px;">



*Coupe transversale du pliage : la ligne de pliage se trouve sur la face supérieure de l'ébauche (noire) avec un décalage de 10 mm par rapport au bord, sa position est indiquée par un pentagone. Elle définit également l'intersection virtuelle de l'ébauche et de la paroi pliée*

.


</div>


</div>



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal Examples/fr
