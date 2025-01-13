---
 GuiCommand:
   Name: SheetMetal AddBend
   Name/fr: SheetMetal Plier
   MenuLocation: SheetMetal , Créer un pliage
   Workbenches: SheetMetal_Workbench/fr
   Shortcut: **S** **B**
   SeeAlso: SheetMetal_AddRelief/fr, SheetMetal_AddJunction/fr
---

# SheetMetal AddBend/fr

## Description

La commande <img alt="" src=images/SheetMetal_AddBend.svg  style="width:24px;"> [SheetMetal Plier](SheetMetal_AddBend/fr.md) remplace les arêtes vives entre deux sections (base/parois/bords) d\'un objet en tôle par des plis arrondis. Sans ces plis, l\'objet ne sera pas dépliable.

Cette commande est la troisième des trois étapes permettant de convertir un objet coque réalisé avec l\'[atelier Part Workbench](Part_Workbench/fr.md) ou l\'[atelier PartDesign](PartDesign_Workbench/fr.md) en un objet tôle dépliable :

1.  [SheetMetal Grugeage carré](SheetMetal_AddRelief/fr.md).
2.  [SheetMetal Découpe d\'angle](SheetMetal_AddJunction/fr.md).
3.  [SheetMetal Plier](SheetMetal_AddBend/fr.md).

<img alt="" src=images/SheetMetal_ConvertShellObject-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-02.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-03.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-04.png  style="width:200px;"> 
*Make Bend - remplace les bords par des plis*



## Utilisation

1.  Sélectionnez une ou plusieurs arêtes.
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/SheetMetal_AddBend.svg" width=16px> [Créer un pliage](SheetMetal_AddBend/fr.md)**.
    -   Sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_AddBend.svg" width=16px> [Créer un pliage](SheetMetal_AddBend/fr.md)** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_AddBend.svg" width=16px> Créer un pliage** dans le menu contextuel.
    -   Utilisez le raccourci clavier : **S** puis **B**.
3.  Le [panneau des tâches](Task_panel/fr.md) *Paramètres de pliage des angles vifs* s\'ouvre (introduit dans la version 0.5.00).
4.  Vous pouvez appuyer sur le bouton **Sélectionner** pour ajouter d\'autres faces.
    -   Appuyez sur le bouton **Aperçu** pour terminer la sélection et afficher les changements.
5.  Vous pouvez ajuster les paramètres dans le panneau des tâches.
6.  Appuyez sur le bouton **OK** pour terminer la commande et fermer le panneau des tâches.
7.  Un objet **SolidBend** sera créé et consistera en une nouvelle courbure à chaque arête sélectionnée.
8.  Vous pouvez ajuster les paramètres dans l\'[éditeur de propriétés](Property_editor/fr.md).

<img alt="" src=images/SheetMetal_ConvertShellObject-07.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-08.png  style="width:200px;">



## Remarques

Les commandes <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **[SheetMetal Grugeage carré](SheetMetal_AddRelief/fr.md)**, <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> **[SheetMetal Découpe d\'angle](SheetMetal_AddJunction/fr.md)** et <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[SheetMetal Plier](SheetMetal_AddBend/fr.md)** fonctionnent mieux avec des cuboïdes creux, c\'est-à-dire des objets en forme de coque avec une épaisseur constante et seulement des angles de 90° entre les faces.

Voir [SheetMetal Grugeage carré](SheetMetal_AddRelief/fr#Remarque.md) pour des conseils sur la création d\'objets coques de cuboïdes.



## Propriétés

Voir aussi: [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal SolidBend est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) ou, s\'il se trouve à l\'intérieur d\'un [PartDesign Corps](PartDesign_Body/fr.md), à partir d\'un objet [PartDesign Feature](PartDesign_Feature/fr.md), dont il hérite de toutes les propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{Properties_Title|Parameters}}

-    **base Object|LinkSub**: objet de base. Liens vers les arêtes à plier.

-    **radius|Length**: rayon de courbure. Valeur par défaut : {{value|1,00 mm}}.

-    **thickness|Length**: épaisseur de la tôle. Valeur par défaut : {{value|1,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddBend/fr
