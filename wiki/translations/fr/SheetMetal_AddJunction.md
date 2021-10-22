---
- GuiCommand:/fr
   Name:SheetMetal Junction
   Name/fr:SheetMetal Découpe d'angle
   MenuLocation:SheetMetal → Make Junction
   Workbenches:[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut:**S** **J**
   SeeAlso:[SheetMetal Grugeage carré](SheetMetal_AddRelief/fr.md), [SheetMetal Transformation en pli](SheetMetal_AddBend/fr.md)
---

# SheetMetal AddJunction/fr

## Description

La commande <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:24px;"> [SheetMetal Découpe d\'angle](SheetMetal_AddJunction/fr.md) crée des jonctions ouvertes entre deux sections (parois/bords) d\'un objet en tôle. Sans ces jonctions, les sections de tôle reliées à la même base ne seront pas dépliables.

Cette commande est la deuxième des trois étapes permettant de convertir un objet coque réalisé avec l\'[atelier Part Workbench](Part_Workbench/fr.md) ou l\'[atelier PartDesign](PartDesign_Workbench/fr.md) en un objet tôle dépliable :

1.  [SheetMetal Grugeage carré](SheetMetal_AddRelief/fr.md).
2.  [SheetMetal Découpe d\'angle](SheetMetal_AddJunction/fr.md).
3.  [SheetMetal Transformation en pli](SheetMetal_AddBend/fr.md).

<img alt="" src=images/SheetMetal_ConvertShellObject-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-02.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-04.png  style="width:100px;"> 
*Faire une jonction - ouvrir les bords*

## Utilisation

1.  Sélectionnez une ou plusieurs arêtes.
2.  Activez la commande <img alt="" src=images/SheetMetal_AddJunction.svg  style="width:16px;"> **SheetMetal Découpe d\'angle**\' en utilisant l\'une des méthodes suivantes :
    -   Le bouton **<img src="images/SheetMetal_AddJunction.svg" width=16px> [SheetMetal AddJunction](SheetMetal_AddJunction/fr.md)**.
    -   L\'option de menu **SheetMetal → <img src="images/SheetMetal_AddJunction.svg" width=16px> Make Junction**.
    -   Le raccourci clavier : **S** puis **J**.

<img alt="" src=images/SheetMetal_ConvertShellObject-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-07.png  style="width:200px;">

## Remarques

Les commandes <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **_** et <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[SheetMetal Transformation en pli](SheetMetal_AddBend/fr.md)** fonctionnent mieux avec des cuboïdes creux, c\'est-à-dire des objets en forme de coque avec une épaisseur constante et seulement des angles de 90° entre les faces.

Voir [SheetMetal Grugeage carré](SheetMetal_AddRelief/fr#Remarque.md) pour des conseils sur la création d\'objets coques de cuboïdes.

## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal Découpe d\'angle est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Label|String}}: Valeur par défaut : Le nom modifiable par l\'utilisateur de cet objet, il peut être toute chaîne UTF8 arbitraire.

-    {{PropertyData/fr|Base Feature|Link|hidden}}: Fonctionnalité de base. Lien vers la caractéristique parent.

-    {{PropertyData/fr|_Body|LinkHidden|hidden}}: Lien caché vers le corps du parent.


{{Properties_Title|Parameters}}

-    {{PropertyData/fr|base Object|LinkSub}}: \"Objet de base\". Liens vers les arêtes définissant les positions d\'écart/de jonction.

-    {{PropertyData/fr|gap|Length}}: \"Écart de jonction\". Valeur par défaut : {{value|2,00 mm}}. Taille de l\'espace/jonction à ajouter.




_ _ _

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal AddJunction/fr
