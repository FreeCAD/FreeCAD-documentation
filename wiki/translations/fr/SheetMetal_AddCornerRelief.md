---
- GuiCommand:/fr
   Name:SheetMetal AddCornerRelief
   Name/fr:SheetMetal Grugeage rond du coin
   MenuLocation:SheetMetal → Add Corner Relief
   Workbenches:[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut:**C** **R**
---

## Description

La commande <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width:24px;"> **SheetMetal AddCornerRelief** ajoute un perçage circulaire pour gruger un coin.

## Utilisation

## Propriétés

Voir aussi : [Éditeur de propriétés](Property_editor/fr.md)

Un objet SheetMetal Grugeage rond du coin est dérivé d\'un objet [Part Feature](Part_Feature/fr.md) et hérite de toutes ses propriétés. Il possède également les propriétés supplémentaires suivantes :

### Données


{{Properties_Title|Base}}

-    {{PropertyData/fr|Label|String}}: Valeur par défaut : Le nom modifiable par l\'utilisateur de cet objet, il peut être toute chaîne UTF8 arbitraire.

-    {{PropertyData/fr|Base Feature|Link|hidden}}: Fonctionnalité de base. Lien vers la caractéristique parent.

-    {{PropertyData/fr|_Body|LinkHidden|hidden}}: Lien caché vers le corps du parent.


{{Properties_Title|Parameters}}

-    {{PropertyData/fr|ReliefSketch|Enumeration}}: \"Type de relief d\'angle\". {{value|Circle}} (par défaut), {{value|Circle-Scaled}}, {{value|Square}}, {{value|Square-Scaled}}, {{value|Sketch}}.

-    {{PropertyData/fr|Size|Length}}: \"Taille de la forme\". Valeur par défaut : {{value|3,00 mm}}.

-    {{PropertyData/fr|Size Ratio|Float}}: \"Rapport de taille de la forme\". Valeur par défaut : {{value|1,50}}.

-    {{PropertyData/fr|base Object|LinkSub}}: \"Objet de base\". Liens vers la paire d\'arêtes définissant la position du Corner Relief.

-    {{PropertyData/fr|kfactor|FloatConstraint}}: \"Position de l\'axe neutre\". Valeur par défaut : {{value|0,50}}.


{{Properties_Title|Parameters1}}

-    {{PropertyData/fr|Sketch|Link}}: \"Esquisse du relief de l\'angle\".

-    {{PropertyData/fr|XOffset|Distance}}: \"Ecart par rapport au premier côté\". Valeur par défaut : {{value|0,00 mm}}.

-    {{PropertyData/fr|YOffset|Distance}}: \"Ecart du côté deux\". Valeur par défaut : {{value|0,00 mm}}.




[Category:SheetMetal](Category:SheetMetal.md) [Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md)
