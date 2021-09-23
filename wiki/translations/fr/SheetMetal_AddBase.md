---
- GuiCommand:/fr
   Name:SheetMetal AddBase
   Name/fr:SheetMetal Tôle de base
   MenuLocation:SheetMetal → Make Base Wall
   Workbenches:[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut:**C** **B**
---

# SheetMetal AddBase/fr

## Description

La commande <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> *SheetMetal AddBase* crée une paroi en tôle à partir d\'une esquisse.

## Utilisation

L\'outil crée une feuille à partir d\'une esquisse :

-   Un contour d\'esquisse ouvert est extrudé par une {{Parameter|length}} (longueur), créant une feuille de {{Parameter|thickness}} (épaisseur) avec des coins arrondis au {{Parameter|radius}} (rayon). Le paramètre {{Parameter|bend side}} (côté du pli) détermine l\'orientation de la feuille par rapport à la ligne.
-   Un contour d\'esquisse fermé est extrudé vers une feuille de {{Parameter|thickness}}. Dans ce cas, les paramètres {{Parameter|length}} et {{Parameter|radius}} ne sont pas utilisés.

<img alt="" src=images/Sheetmetal.png  style="width:400px;">

## Propriétés

Voir aussi: [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal Tôle de base est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Label|String}}: Valeur par défaut : Le nom modifiable par l\'utilisateur de cet objet, il peut être toute chaîne UTF8 arbitraire.

-    {{PropertyData/fr|Base Feature|Link|hidden}}: Fonctionnalité de base. Lien vers la caractéristique parent.

-    {{PropertyData/fr|_Body|LinkHidden|hidden}}: Lien caché vers le corps du parent.


{{Properties_Title|Parameters}}

-    {{PropertyData/fr|Bend Side|Enumeration}}: \"Relief Type\". {{value|Outside}} (par défaut), {{value|Inside}}, {{value|Middle}}.

-    {{PropertyData/fr|Bend Sketch|Link}}: \"Objet Esquisse de mur\". Lien vers l\'esquisse de profil/de contour.

-    {{PropertyData/fr|Mid Plane|Bool}}: \"Extruder symétriquement au plan\".   `True`, le profil s\'étend symétriquement sur les deux côtés du plan d\'esquisse.

-    {{PropertyData/fr|Reverse|Bool}}: \"Inverse la direction d\'extrusion\". Valeur par défaut : `False`.

-    {{PropertyData/fr|length|Length}}: \"Longueur du mur\". Valeur par défaut : {{value|100,00 mm}}.

-    {{PropertyData/fr|radius|Length}}: \"Rayon de courbure\". Valeur par défaut : {{value|1,00 mm}}.

-    {{PropertyData/fr|thickness|Length}}: \"Epaisseur de la tôle\". Valeur par défaut : {{value|1,00 mm}}.




[Category:SheetMetal](Category:SheetMetal.md) [Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md)

---
[documentation index](../README.md) > [SheetMetal](Category:SheetMetal.md) > SheetMetal AddBase/fr
