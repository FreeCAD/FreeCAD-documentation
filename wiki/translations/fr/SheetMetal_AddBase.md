---
- GuiCommand:/fr
   Name:SheetMetal AddBase
   Name/fr:SheetMetal Tôle de base
   MenuLocation:SheetMetal → Make Base Wall
   Workbenches:[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut:**C** **B**
---

## Description

La commande <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> *SheetMetal AddBase* crée une paroi en tôle à partir d\'une esquisse.

## Utilisation

L\'outil crée une feuille à partir d\'une esquisse :

-   Un contour d\'esquisse ouvert est extrudé par une {{Parameter|length}} (longueur), créant une feuille de {{Parameter|thickness}} (épaisseur) avec des coins arrondis au {{Parameter|radius}} (rayon). Le paramètre {{Parameter|bend side}} (côté du pli) détermine l\'orientation de la feuille par rapport à la ligne.
-   Un contour d\'esquisse fermé est extrudé vers une feuille de {{Parameter|thickness}}. Dans ce cas, les paramètres {{Parameter|length}} et {{Parameter|radius}} ne sont pas utilisés.

<img alt="" src=images/Sheetmetal.png  style="width:400px;">

## Propriétés

See also: [Property editor](Property_editor.md).

A SheetMetal BaseBend object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Base}}

-    **Label|String**: Default value: The user editable name of this object, it may be any arbitrary UTF8 string.

-    **Base Feature|Link|hidden**: Base Feature. Link to the parent feature.

-    **_Body|LinkHidden|hidden**: Hidden link to the parent body.


{{Properties_Title|Parameters}}


<div class="mw-translate-fuzzy">

-    {{PropertyData/fr|bend side}}: Côté du pliage. Extérieur, Intérieur, Milieu

-    {{PropertyData/fr|mid plane}}: Milieu du pla. Booléen

-    {{PropertyData/fr|revers}}: Inverser. Booléen

-    {{PropertyData/fr|length}}: Longueur. Longueur du solide

-    {{PropertyData/fr|radius}}: Rayon de la courbure.

-    {{PropertyData/fr|thickness}}: Epaisseur du matériau.


</div>




[Category:SheetMetal{{\#translation:}}](Category:SheetMetal.md) [Category:Addons{{\#translation:}}](Category:Addons.md) [Category:External Command Reference{{\#translation:}}](Category:External_Command_Reference.md)
