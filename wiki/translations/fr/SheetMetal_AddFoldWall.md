---
 GuiCommand:
   Name: SheetMetal AddFoldWall
   Name/fr: SheetMetal Plier une tôle
   MenuLocation: SheetMetal , Plier une tôle
   Workbenches: SheetMetal_Workbench/fr
   Shortcut: **C** **F**
---

# SheetMetal AddFoldWall/fr

## Description

La commande <img alt="" src=images/SheetMetal_AddFoldWall.svg  style="width:24px;"> **SheetMetal Plier une tôle** plie une tôle (brute) selon une ligne choisie.

Elle peut être utilisée avec une plaque prédécoupée pour

-   créer une zone de pliage perforée
-   laisser des sections planes dans la zone de pliage et au-delà, par exemple des languettes. (nécessite des espaces dans la ligne de pliage)

<img alt="" src=images/SheetMetal_AddFoldWall-13.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddFoldWall-14.png  style="width:300px;">



*Plaque prédécoupée et ligne de pliage avec deux espaces → zone de pliage perforée avec une géométrie encore plane*



## Utilisation

1.  Sélectionnez le côté à plier.
2.  Maintenez la touche **Ctrl** (ou la touche **Commande** sur macOS).
3.  Sélectionnez la face coplanaire de l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [esquisse](Sketcher_Workbench/fr.md) (c\'est-à-dire située sur le même plan) contenant la **ligne de pliage (segments)** (de préférence à partir de la [vue en arborescence](Tree_view/fr.md)).
4.  Relâchez la touche **Ctrl** (ou la touche **Commande**).
5.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/SheetMetal_AddFoldWall.svg" width=16px> [Plier une tôle](SheetMetal_AddFoldWall/fr.md)**.
    -   Sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_AddFoldWall.svg" width=16px> Plier une tôle** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_AddFoldWall.svg" width=16px> Plier une tôle** dans le menu contextuel.
    -   Utilisez le raccourci clavier : **C** Puis **F**.
6.  Le [panneau des tâches](Task_panel/fr.md) *Générer une forme de base de la tôle* s\'ouvre (introduit dans la version 0.5.00).
7.  Vous pouvez appuyer sur le bouton **Objet de base** et sélectionnez une face différente.
8.  Vous pouvez appuyer sur le bouton **Ligne de pliage** et sélectionnez une autre esquisse.
9.  Vous pouvez ajuster les paramètres dans panneau des tâches.
10. Appuyez sur le bouton **OK** pour terminer la commande et fermer le panneau des tâches.
11. Un objet **Fold** sera créé.
12. Vous pouvez ajuster les paramètres dans l\'[éditeur de propriétés](Property_editor/fr.md).

<img alt="" src=images/SheetMetal_AddFoldWall-15.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_AddFoldWall-14.png  style="width:300px;">



*La ou les lignes de pliage situées au milieu de la perforation → pour que le pliage soit centré de la même manière, la propriété **Position* doit être définie sur {{value|middle**}}



### Remarques

-   La ligne de pliage doit être **coplanaire** à la face sélectionnée.

-   Les segments de la ligne de pliage doivent être **colinéaires** les uns par rapport aux autres.



## Propriétés

Voir aussi: [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal Fold est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) ou, s\'il se trouve à l\'intérieur d\'un [PartDesign Corps](PartDesign_Body/fr.md), à partir d\'un objet [PartDesign Feature](PartDesign_Feature/fr.md), dont il hérite de toutes les propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{Properties_Title|Parameters}}

-    **Bend Line|Link**: liste des lignes de référence de pliage. Liens vers les objets de la ligne de pliage.

-    **Position|Enumeration**: position de la ligne de pliage.

    :   
        {{value|intersection of planes}}
        
        (introduit dans la version 0.4.12), {{value|forward}} (valeur par défaut), {{value|middle}}, {{value|backward}}.

-    **angle|Angle**: angle de pliage. Angle par défaut : {{value|90,00°}}.

-    **base Object|LinkSub**: objet de base. Lien vers la face planaire à plier.

-    **invert|Bool**: inverser la direction du pliage. Valeur par défaut : `False`.

-    **invertbend|Bool**: inverser la direction de pliage du solide. Valeur par défaut : `False`.

    :   
        `True`
        
        permute le côté de la ligne à plier.

-    **kfactor|FloatConstraint**: position de l\'axe neutre. Valeur par défaut : {{value|0,50}}.

-    **radius|Length**: rayon de pliage . Valeur par défaut : {{value|1,00 mm}}.

-    **unfold|Bool**: pliage déplié. Valeur par défaut : `False`.



## Exemple

<img alt="" src=images/SheetMetal_AddFoldWall-01.png  style="width:300px;"> 
*Un simple clip*


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">



### Préparation

Ce clip est fait d\'un blanc qui reçoit trois plis et donc nous avons besoin de quatre schémas préparés à l\'avance :

:   \- un pour le contour plus la fente (vierge)
:   \- un pour le pliage de la pointe
:   \- un pour le pliage vers le haut
:   \- un pour le pliage vers le bas

La façon la plus simple de garantir qu\'une face de la découpe et toutes les lignes de pliage sont coplanaires est de créer toutes les esquisses sur le même plan - le **XY_Plane** dans ce cas.

Les lignes de pliage pourraient être créées avec d\'autres outils, mais bon, nous avons une <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;">[esquisse](Sketcher_Workbench/fr.md) !

<img alt="" src=images/SheetMetal_AddFoldWall-21.png  style="width:280px;"> <img alt="" src=images/SheetMetal_AddFoldWall-20.png  style="width:200px;"> 
*Esquisses sur leur plan commun et leur représentation dans l'arbre de conception*



### Déroulement des tâches 

1.  Créer une ébauche
    1.  Sélectionnez l\'esquisse de contour
    2.  Appuyez sur le bouton ou utilisez le raccourci clavier :  <img alt="" src=images/SheetMetal_AddFoldWall-02.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-03.png  style="width:280px;"> 
2.  Plier la pointe
    1.  Sélectionner la **face inférieure** de l\'ébauche.
    2.  Sélectionnez l**\'esquisse** nommée ***Tip Fold line*** (de préférence à partir de l\'arborescence)  (et n\'oubliez pas la touche contrôle/commande ).
    3.  Appuyez sur le ou utilisez le raccourci clavier : <img alt="" src=images/SheetMetal_AddFoldWall-10.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-04.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-05.png  style="width:280px;">
    4.  Le pli doit être à 90° vers le bas et donc certaines valeurs dans la fenêtre des propriétés doivent être définies par exemple :  - la valeur **angle** à 60°  - la valeur **inverser** à true pour un pliage vers le haut  .
3.  Créer le pli vers le bas
    1.  Sélectionnez la **face inférieure** de l\'ébauche.
    2.  Et ensuite l**\'esquisse** nommée ***Down-Fold line***.
    3.  Appuyez sur le ou utilisez le raccourci clavier : <img alt="" src=images/SheetMetal_AddFoldWall-11.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-06.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-07.png  style="width:280px;">
    4.  Réglez la valeur *angle* à 92°.
    5.  Si la mauvaise section de la pièce a bougé, réglez la valeur **invertbend** sur true  .
    6.  Pour créer le pliage vers le haut
    7.  sélectionnez la **face inférieure** de la pièce brute.
    8.  puis le **sketch** nommé ***Up-Fold line***.
    9.  Appuyez sur le bouton ou utilisez le raccourci clavier : <img alt="" src=images/SheetMetal_AddFoldWall-12.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-08.png  style="width:120px;"> <img alt="" src=images/SheetMetal_AddFoldWall-09.png  style="width:280px;">
    10. Définissez la valeur **angle** à 80°.
    11. Si le pli est vers le bas définir la valeur **invert** à true.
    12. Si nécessaire, mettez la valeur **invertbend** à true.  

C\'est fait!

Remarque : dans la vie réelle, le pliage vers le haut doit être effectué avant le pliage vers le bas. Seul le monde virtuel de la CAO nous permet de plier à travers un matériau solide. De cette façon, l\'orientation de la section statique ne change pas.  Toutes les esquisses se trouvent sur le même plan pour éviter les esquisses attachées aux faces mobiles.


</div>


</div>



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddFoldWall/fr
