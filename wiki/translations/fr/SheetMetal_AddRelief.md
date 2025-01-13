---
 GuiCommand:
   Name: SheetMetal AddRelief
   Name/fr: SheetMetal Grugeage carré
   MenuLocation: SheetMetal , Créer un grugeage carré
   Workbenches: SheetMetal_Workbench/fr
   Shortcut: **S** **R**
   SeeAlso: SheetMetal_AddJunction/fr, SheetMetal_AddBend/fr
---

# SheetMetal AddRelief/fr

## Description

La commande <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> [SheetMetal Grugeage carré](SheetMetal_AddRelief/fr.md) crée des dépouilles d\'angle, des découpes, aux points de rencontre de trois sections (base/parois/bords) d\'un objet en tôle. Sans ces grugeages, l\'objet ne pourra pas être déplié.

Cette commande est la première des trois étapes permettant de convertir un objet coque réalisé avec l\'[atelier Part](Part_Workbench/fr.md) ou l\'[atelier PartDesign](PartDesign_Workbench/fr.md) en un objet tôle dépliable :

1.  [SheetMetal Grugeage carré](SheetMetal_AddRelief/fr.md).
2.  [SheetMetal Découpe d\'angle](SheetMetal_AddJunction/fr.md).
3.  [SheetMetal Plier](SheetMetal_AddBend/fr.md).

<img alt="" src=images/SheetMetal_ConvertShellObject-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-03.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-04.png  style="width:100px;"> 
*Créer un grugeage "découpe" des coins*



## Utilisation

1.  Sélectionnez un ou plusieurs sommets d\'angle.
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/SheetMetal_AddRelief.svg" width=16px> [Créer un grugeage carré](SheetMetal_AddRelief/fr.md)**.
    -   Sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_AddRelief.svg" width=16px> Créer un grugeage carré** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_AddRelief.svg" width=16px> Créer un grugeage carré** dans le menu contextuel.
    -   Utilisez le raccourci clavier : **S** puis **R**.
3.  Le [panneau des tâches](Task_panel/fr.md) **Ajouter un grugeage au solide** s\'ouvre (introduit dans la version 0.5.00).
4.  Vous pouvez appuyer sur le bouton **Sélectionner** pour ajouter d\'autres sommets.
    -   Appuyez sur le bouton **Aperçu** pour terminer la sélection et afficher les changements.
5.  Vous pouvez ajuster les paramètres dans le panneau des tâches.
6.  Appuyez sur le bouton **OK** pour terminer la commande et fermer le panneau des tâches.
7.  Un objet **CornerRelief** sera créé, composé d\'un nouveau grugeage carré à chaque sommet sélectionné.
8.  Vous pouvez ajuster les paramètres dans l\'[éditeur de propriétés](Property_editor/fr.md).

<img alt="" src=images/SheetMetal_ConvertShellObject-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-06.png  style="width:200px;">



## Remarques

Les commandes <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **[SheetMetal Grugeage carré](SheetMetal_AddRelief/fr.md)**, <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> **[SheetMetal Découpe d\'angle](SheetMetal_AddJunction/fr.md)** et <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[SheetMetal Plier](SheetMetal_AddBend/fr.md)** fonctionnent mieux avec des cuboïdes creux, c\'est-à-dire des objets en forme de coque avec une épaisseur constante et seulement des angles de 90° entre les faces.

Les objets coques peuvent être créés avec des commandes de l\'<img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [atelier Part](Part_Workbench/fr.md) ou de l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [atelier PartDesign](PartDesign_Workbench/fr.md).

Pour créer un cuboïde creux avec l\'[atelier Part](Part_Workbench/fr.md) :

1.  Créez un solide en utilisant soit :
    -   Un <img alt="" src=images/Part_Box.svg  style="width:16px;"> [Part Cube](Part_Box/fr.md).
    -   Une <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Part Extrusion](Part_Extrude/fr.md) à partir de :
        -   Un <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Draft Rectangle](Draft_Rectangle/fr.md).
        -   Une <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Draft Polyligne](Draft_Wire/fr.md).
        -   Une <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Esquisse](Sketcher_NewSketch/fr.md).
2.  Utilisez <img alt="" src=images/Part_Thickness.svg  style="width:16px;"> [Part Évider](Part_Thickness/fr.md) pour créer un objet coque à partir du solide (typiquement avec la valeur d\'épaisseur de la tôle).

Pour créer un cuboïde creux avec l\'[atelier PartDesign](PartDesign_Workbench/fr.md) :

1.  Créez un solide en utilisant soit :
    -   Un <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:16px;"> [Cube additif](PartDesign_AdditiveBox/fr.md).
    -   Une <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> [PartDesign Protrusion](PartDesign_Pad/fr.md) à partir d\'une <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [esquisse](Sketcher_NewSketch/fr.md).
2.  Utilisez <img alt="" src=images/Part_Thickness.svg  style="width:16px;"> [Part Évider](Part_Thickness/fr.md) pour créer un objet coque à partir du solide (typiquement avec la valeur d\'épaisseur de la tôle).



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal Relief est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) ou, s\'il se trouve à l\'intérieur d\'un [PartDesign Corps](PartDesign_Body/fr.md), à partir d\'un objet [PartDesign Feature](PartDesign_Feature/fr.md), dont il hérite de toutes les propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{Properties_Title|Parameters}}

-    **base Object|LinkSub**: objet de base. Liens vers les sommets d\'angle définissant les positions de relief.

-    **relief|Length**: taille du grugeage carré. Valeur par défaut : {{value|2,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddRelief/fr
