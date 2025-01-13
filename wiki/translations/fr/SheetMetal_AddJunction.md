---
 GuiCommand:
   Name: SheetMetal Junction
   Name/fr: SheetMetal Découpe d'angle
   MenuLocation: SheetMetal , Créer une découpe d'angle
   Workbenches: SheetMetal_Workbench/fr
   Shortcut: **S** **J**
   SeeAlso: SheetMetal_AddRelief/fr, SheetMetal_AddBend/fr
---

# SheetMetal AddJunction/fr

## Description

La commande <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:24px;"> [SheetMetal Découpe d\'angle](SheetMetal_AddJunction/fr.md) crée des jonctions ouvertes entre deux sections (parois/bords) d\'un objet en tôle. Sans ces jonctions, les sections de tôle reliées à la même base ne seront pas dépliables.

Cette commande est la deuxième des trois étapes permettant de convertir un objet coque réalisé avec l\'[atelier Part](Part_Workbench/fr.md) ou l\'[atelier PartDesign](PartDesign_Workbench/fr.md) en un objet tôle dépliable :

1.  [SheetMetal Grugeage carré](SheetMetal_AddRelief/fr.md).
2.  [SheetMetal Découpe d\'angle](SheetMetal_AddJunction/fr.md).
3.  [SheetMetal Plier](SheetMetal_AddBend/fr.md).

<img alt="" src=images/SheetMetal_ConvertShellObject-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-02.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-04.png  style="width:100px;"> 
*Créer une découpe d'angle "ouvre" les bords*



## Utilisation

1.  Sélectionnez une ou plusieurs arêtes.
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/SheetMetal_AddJunction.svg" width=16px> [Créer une découpe d'angle](SheetMetal_AddJunction/fr.md)**.
    -   Sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_AddJunction.svg" width=16px> Créer une découpe d'angle** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_AddJunction.svg" width=16px> Créer une découpe d'angle** dans le menu contextuel.
    -   Utilisez le raccourci clavier : **S** puis **J**.
3.  Le [panneau des tâches](Task_panel/fr.md) *Ajouter les paramètres de la découpe d\'angle* s\'ouvre (introduit dans la version 0.5.00).
4.  Vous pouvez appuyer sur le bouton **Sélectionner** pour ajouter d\'autres faces.
    -   Appuyez sur le bouton **Aperçu** pour terminer la sélection et afficher les changements.
5.  Vous pouvez ajuster les paramètres dans le panneau des tâches.
6.  Appuyez sur le bouton **OK** pour terminer la commande et fermer le panneau des tâches.
7.  Un objet **Junction** sera créé, composé d\'une ouverture à chaque bord sélectionné.
8.  Vous pouvez ajuster les paramètres dans l\'[éditeur de propriétés](Property_editor/fr.md).

<img alt="" src=images/SheetMetal_ConvertShellObject-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-07.png  style="width:200px;">



## Remarques

-   Les commandes <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **[SheetMetal Grugeage carré](SheetMetal_AddRelief/fr.md)**, <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> **[SheetMetal Découpe d\'angle](SheetMetal_AddJunction/fr.md)** et <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[SheetMetal Plier](SheetMetal_AddBend/fr.md)** fonctionnent mieux avec des cuboïdes creux, c\'est-à-dire des objets en forme de coque avec une épaisseur constante et seulement des angles de 90° entre les faces.
-   Voir [SheetMetal Grugeage carré](SheetMetal_AddRelief/fr#Remarques.md) pour des conseils sur la création d\'objets coques de cuboïdes.

-   Dans ce cas, la *jonction* n\'est pas le résultat de cet outil, qui est un espace entre des faces planes adjacentes, mais décrit plutôt l\'endroit où deux faces planes de l\'objet fini du monde réel se rencontrent, pour être soudées, par exemple.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal Junction est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) ou, s\'il se trouve à l\'intérieur d\'un [PartDesign Corps](PartDesign_Body/fr.md), à partir d\'un objet [PartDesign Feature](PartDesign_Feature/fr.md), dont il hérite de toutes les propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{Properties_Title|Parameters}}

-    **base Object|LinkSub**: objet de base. Liens vers les arêtes définissant les positions des découpes.

-    **gap|Length**: taille de la découpe. Valeur par défaut : {{value|2,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddJunction/fr
