---
- GuiCommand:/fr
   Name:SheetMetal AddRelief
   Name/fr:SheetMetal Grugeage carré
   MenuLocation:SheetMetal → Make Relief
   Workbenches:[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut:**S** **R**
   SeeAlso:[SheetMetal Découpe d'angle](SheetMetal_AddJunction/fr.md), [SheetMetal Transformation en pli](SheetMetal_AddBend/fr.md)
---

# SheetMetal AddRelief/fr

## Description

La commande <img alt="" src=images/SheetMetal_Relief.svg  style="width:16px;"> [SheetMetal Grugeage carré](SheetMetal_AddRelief/fr.md) crée des dépouilles d\'angle, des découpes, aux points de rencontre de trois sections (base/parois/bords) d\'un objet en tôle. Sans ces grugeages, l\'objet ne pourra pas être déplié.

Cette commande est la première des trois étapes permettant de convertir un objet coque réalisé avec l\'[atelier Part Workbench](Part_Workbench/fr.md) ou l\'[atelier PartDesign](PartDesign_Workbench/fr.md) en un objet tôle dépliable :

1.  [SheetMetal Grugeage carré](SheetMetal_AddRelief/fr.md).
2.  [SheetMetal Découpe d\'angle](SheetMetal_AddJunction/fr.md).
3.  [SheetMetal Transformation en pli](SheetMetal_AddBend/fr.md).

<img alt="" src=images/SheetMetal_ConvertShellObject-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-03.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-04.png  style="width:100px;"> 
*Créer un grugeage - couper les coins*

## Utilisation

1.  Sélectionnez un ou plusieurs sommets d\'angle.
2.  Activez la commande <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **SheetMetal Grugeage carré**\' en utilisant l\'une des méthodes suivantes :
    -   Le bouton **<img src="images/SheetMetal_AddRelief.svg" width=16px> [SheetMetal AddRelief](SheetMetal_AddRelief/fr.md)**.
    -   L\'option de menu **SheetMetal → <img src="images/SheetMetal_AddRelief.svg" width=16px> Make Relief**.
    -   Le raccourci clavier : **S** puis **R**.

<img alt="" src=images/SheetMetal_ConvertShellObject-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-06.png  style="width:200px;">

## Remarques

Les commandes <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **_** et <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[SheetMetal Transformation en pli](SheetMetal_AddBend/fr.md)** fonctionnent mieux avec des cuboïdes creux, c\'est-à-dire des objets en forme de coque avec une épaisseur constante et seulement des angles de 90° entre les faces.

Les objets coques peuvent être créés avec des commandes de l\'<img alt="" src=images/Workbench_Part.svg  style="width:16px;"> _.

Pour créer un cuboïde creux avec l\'[atelier Part](Part_Workbench/fr.md) :

1.  Créez un solide en utilisant soit :
    -   <img alt="" src=images/Part_Box.svg  style="width:16px;"> [Part Cube](Part_Box/fr.md).
    -   <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Part Extrusion](Part_Extrude/fr.md) de :
        -   Un <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Draft Rectangle](Draft_Rectangle/fr.md).
        -   Une <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Draft Polyligne](Draft_Wire/fr.md).
        -   Une <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Esquisse](Sketcher_NewSketch/fr.md).
2.  Utilisez <img alt="" src=images/Part_Thickness.svg  style="width:16px;"> [Part Évidement](Part_Thickness/fr.md) pour créer un objet coque à partir du solide (typiquement avec la valeur d\'épaisseur de la tôle).

Pour créer un cuboïde creux avec l\'[atelier PartDesign](PartDesign_Workbench/fr.md) :

1.  Créez un solide en utilisant soit :
    -   Un <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:16px;"> [Cube additif](PartDesign_AdditiveBox/fr.md).
    -   Une <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> _.
2.  Utilisez <img alt="" src=images/Part_Thickness.svg  style="width:16px;"> [Part Évidement](Part_Thickness/fr.md) pour créer un objet coque à partir du solide (typiquement avec la valeur d\'épaisseur de la tôle).

## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal Grugeage carré est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Label|String}}: Valeur par défaut : Le nom modifiable par l\'utilisateur de cet objet, il peut être toute chaîne UTF8 arbitraire.

-    {{PropertyData/fr|Base Feature|Link|hidden}}: Fonctionnalité de base. Lien vers la caractéristique parent.

-    {{PropertyData/fr|_Body|LinkHidden|hidden}}: Lien caché vers le corps du parent.


{{Properties_Title|Parameters}}

-    {{PropertyData/fr|base Object|LinkSub}}: \"Objet de base\". Liens vers les sommets d\'angle définissant les positions de relief.

-    {{PropertyData/fr|relief|Length}}: \"Taille du grugeage\". Valeur par défaut : {{value|2,00 mm}}.




_ _ _

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal AddRelief/fr
