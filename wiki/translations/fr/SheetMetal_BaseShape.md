---
 GuiCommand:
   Name: SheetMetal BaseShape
   Name/fr: SheetMetal Forme de base
   MenuLocation: SheetMetal , Créer une forme de base
   Workbenches: SheetMetal_Workbench/fr
   Version: 0.3.10
   Shortcut: **H**
---

# SheetMetal BaseShape/fr

## Description

La commande <img alt="" src=images/SheetMetal_BaseShape.svg  style="width:24px;"> **SheetMetal Forme de base** crée un objet SheetMetal BaseShape à partir de paramètres.

<img alt="" src=images/SheetMetal_BaseShape-01.png  style="width:400px;">



*Les cinq formes de base disponibles : forme en L, forme en U, forme en baignoire, forme en chapeau et boîte*

Une sixième forme rectangulaire, appelée Plat, a été introduite dans la version 0.4.10.



## Utilisation

1.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/SheetMetal_BaseShape.svg" width=16px> [Créer une forme de base](SheetMetal_BaseShape/fr.md)**.
    -   Sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_BaseShape.svg" width=16px> Créer une forme de base** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **SheetMetal → <img src="images/SheetMetal_BaseShape.svg" width=16px> Créer une forme de base** dans le menu contextuel.
    -   Utilisez le raccourci clavier : **H**.
2.  Le [panneau des tâches](Task_panel/fr.md) **Générer une forme de base de la tôle** s\'ouvre.
3.  Sélectionnez la forme souhaitée dans les options **Type de forme de base**.
4.  Sélectionnez la position de l\'origine dans le widget **Emplacement de l\'origine de la pièce**.
5.  Vous pouvez ajuster les paramètres dans le panneau des tâches.
6.  Appuyez sur le bouton **OK** pour terminer la commande et fermer le panneau des tâches.
7.  Un objet **BaseShape** sera créé.
8.  Vous pouvez ajuster les paramètres dans l\'[éditeur de propriétés](Property_editor/fr.md).



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal BaseShape est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) ou, s\'il se trouve à l\'intérieur d\'un [PartDesign Corps](PartDesign_Body/fr.md), à partir d\'un objet [PartDesign Feature](PartDesign_Feature/fr.md), dont il hérite de toutes les propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{Properties_Title|Parameters}}

-    **fill Gaps|Bool**: prolonge les côtés et les rebords pour combler tous les espaces. Valeur par défaut : `True`.

-    **flangeWidth|Length**: largeur du rebord supérieure. Valeur par défaut : {{Value|5,00 mm}}.

-    **height|Length**: hauteur de la forme. Valeur par défaut : {{Value|10,00 mm}}.

-    **length|Length**: longueur de la forme. Valeur par défaut : {{Value|30,00 mm}}.

-    **origin Loc|Enumeration**: position de l\'origine.

    :   
        {{Value|-X,-Y}}
        
        , {{Value|-X,0}}, {{Value|-X,+Y}}, {{Value|0,-Y}}, {{Value|0,0}} (valeur par défaut), {{Value|0,+Y}}, {{Value|+X,-Y}}, {{Value|+X,0}} et {{Value|+X,+Y}}.

-    **radius|Length**: rayon de courbure. Valeur par défaut : {{Value|1,00 mm}}.

-    **shape Type|Enumeration**: type de forme de base.

    :   
        {{Value|Flat}}
        
        (introduite dans la V0.4.10), {{Value|L-Shape}} (valeur par défaut), {{Value|U-Shape}}, {{Value|Tub}}, {{Value|Hat}} et {{Value|Box}}.

-    **thickness|Length**: épaisseur de la tôle. Valeur par défaut : {{Value|1,00 mm}}.

-    **width|Length**: largeur de la forme. Valeur par défaut : {{Value|20,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal BaseShape/fr
