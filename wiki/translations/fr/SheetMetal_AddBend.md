---
- GuiCommand:/fr
   Name:SheetMetal AddBend
   Name/fr:SheetMetal Transformation en pli
   MenuLocation:SheetMetal → Make Bend
   Workbenches:[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut:**S** **B**
---

## Description

La commande <img alt="" src=images/SheetMetal_AddBend.svg  style="width:24px;"> **SheetMetal AddBend** plie une tôle selon une ligne choisie.

## Utilisation

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




[Category:SheetMetal](Category:SheetMetal.md) [Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md)
