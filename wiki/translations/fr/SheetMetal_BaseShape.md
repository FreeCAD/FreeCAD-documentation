---
 GuiCommand:
   Name: SheetMetal BaseShape
   Name/fr: SheetMetal Forme de base
   MenuLocation: SheetMetal , Add base shape
   Workbenches: SheetMetal_Workbench/fr
   Version: 0.3.10
   Shortcut: **H**
---

# SheetMetal BaseShape/fr

## Description

La commande <img alt="" src=images/SheetMetal_BaseShape.svg  style="width:24px;"> **SheetMetal Forme de base** crée un objet SheetMetal BaseShape à partir de paramètres.

<img alt="" src=images/SheetMetal_BaseShape-01.png  style="width:400px;">



*Les cinq formes de base disponibles : forme en L, forme en U, forme en baignoire, forme en chapeau et boîte*



## Utilisation

1.  Activez la commande <img alt="" src=images/SheetMetal_BaseShape.svg  style="width:16px;"> **SheetMetal BaseShape** en utilisant l\'une des méthodes suivantes :
    -   Le bouton **<img src="images/SheetMetal_BaseShape.svg" width=16px> [Add base shape](SheetMetal_BaseShape/fr.md)**.
    -   L\'option de menu **SheetMetal → <img src="images/SheetMetal_BaseShape.svg" width=16px> Add base shape**.
    -   Le raccourci clavier : **H**.
2.  Le panneau des tâches **Unfold sheet metal object** s\'ouvre.
3.  Sélectionnez la forme désirée dans les options **Base shape type**.
4.  Ajustez les paramètres.
5.  Appuyez sur **OK** pour terminer la commande.



## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal Forme de base est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :



### Données


{{Properties_Title|Base}}

-    **Label|String**: Valeur par défaut : Le nom modifiable par l\'utilisateur de cet objet, il peut être toute chaîne UTF8 arbitraire.


{{Properties_Title|Parameters}}

-    **fill Gaps|Bool**: prolonge les côtés et les brides pour combler tous les espaces. Valeur par défaut : `True`.

-    **flangeWidth|Length**: largeur de la bride supérieure. Valeur par défaut : {{Value|5,00 mm}}.

-    **height|Length**: hauteur de la forme. Valeur par défaut : {{Value|10,00 mm}}.

-    **length|Length**: longueur de la forme. Valeur par défaut : {{Value|30,00 mm}}.

-    **radius|Length**: rayon de courbure. Valeur par défaut : {{Value|1,00 mm}}.

-    **shape Type|Enumeration**: type de forme de base. {{Value|L-Shape}} (valeur par défaut), {{Value|U-Shape}}, {{Value|Tub}}, {{Value|Hat}}, {{Value|Box}}.

-    **thickness|Length**: épaisseur de la tôle. Valeur par défaut : {{Value|1,00 mm}}.

-    **width|Length**: largeur de la forme. Valeur par défaut : {{Value|20,00 mm}}.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal BaseShape/fr
