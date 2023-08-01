---
- GuiCommand:/fr
   Name:SheetMetal AddBend
   Name/fr:SheetMetal Transformation en pli
   MenuLocation:SheetMetal → Make Bend
   Workbenches:[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut:**S** **B**
   SeeAlso:[SheetMetal Grugeage carré](SheetMetal_AddRelief/fr.md), [SheetMetal Découpe d'angle](SheetMetal_AddJunction/fr.md)
---

# SheetMetal AddBend/fr

## Description

La commande <img alt="" src=images/SheetMetal_AddBend.svg  style="width:24px;"> [SheetMetal Transformation en pli](SheetMetal_AddBend/fr.md) remplace les arêtes vives entre deux sections (base/parois/bords) d\'un objet en tôle par des plis arrondis. Sans ces plis, l\'objet ne sera pas dépliable.

Cette commande est la troisième des trois étapes permettant de convertir un objet coque réalisé avec l\'[atelier Part Workbench](Part_Workbench/fr.md) ou l\'[atelier PartDesign](PartDesign_Workbench/fr.md) en un objet tôle dépliable :

1.  [SheetMetal Grugeage carré](SheetMetal_AddRelief/fr.md).
2.  [SheetMetal Découpe d\'angle](SheetMetal_AddJunction/fr.md).
3.  [SheetMetal Transformation en pli](SheetMetal_AddBend/fr.md).

<img alt="" src=images/SheetMetal_ConvertShellObject-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-02.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-03.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-04.png  style="width:200px;"> 
*Make Bend - remplace les bords par des plis*

## Utilisation

1.  Sélectionnez une ou plusieurs arêtes.
2.  Activez la commande <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **SheetMetal Transformation en pli** en utilisant l\'une des commandes suivantes :
    -   Le bouton **<img src="images/SheetMetal_AddBend.svg" width=16px> [Make Bend](SheetMetal_AddBend/fr.md)**.
    -   L\'option de menu **SheetMetal → <img src="images/SheetMetal_AddBend.svg" width=16px> Make Bend**.
    -   Le raccourci clavier : **S** puis **B**.

<img alt="" src=images/SheetMetal_ConvertShellObject-07.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-08.png  style="width:200px;">

## Remarques

Les commandes <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **[SheetMetal Grugeage carré](SheetMetal_AddRelief/fr.md)**, <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> **[SheetMetal Découpe d\'angle](SheetMetal_AddJunction/fr.md)** et <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[SheetMetal Transformation en pli](SheetMetal_AddBend/fr.md)** fonctionnent mieux avec des cuboïdes creux, c\'est-à-dire des objets en forme de coque avec une épaisseur constante et seulement des angles de 90° entre les faces.

Voir [SheetMetal Grugeage carré](SheetMetal_AddRelief/fr#Remarque.md) pour des conseils sur la création d\'objets coques de cuboïdes.

## Propriétés

Voir aussi: [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal Transformation en pli est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Label|String}}: Valeur par défaut : Le nom modifiable par l\'utilisateur de cet objet, il peut être toute chaîne UTF8 arbitraire.

-    {{PropertyData/fr|Base Feature|Link|hidden}}: Fonctionnalité de base. Lien vers la caractéristique parent.

-    {{PropertyData/fr|_Body|LinkHidden|hidden}}: Lien caché vers le corps du parent.


{{Properties_Title|Parameters}}

-    {{PropertyData/fr|base Object|LinkSub}}: \"Objet de base\". Liens vers les arêtes à plier.

-    {{PropertyData/fr|radius|Length}}: \"Rayon de courbure\". Valeur par défaut : {{value|1,00 mm}}.

-    {{PropertyData/fr|thickness|Length}}: \"Epaisseur de la tôle\". Valeur par défaut : {{value|1,00 mm}}.



---
![](images/Button_right.svg) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddBend/fr
