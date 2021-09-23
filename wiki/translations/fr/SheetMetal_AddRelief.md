---
- GuiCommand:/fr
   Name:SheetMetal AddRelief
   Name/fr:SheetMetal Grugeage carré
   MenuLocation:SheetMetal → Make Relief
   Workbenches:[SheetMetal](SheetMetal_Workbench/fr.md)
   Shortcut:**S** **R**
---

## Description

La commande <img alt="" src=images/SheetMetal_Relief.svg  style="width:24px;"> **SheetMetal AddRelief**\...

<img alt="" src=images/PostRelief.png  style="width:320px;"> 
*Créer un espace pour le pliage de la tôle.*

## Utilisation

Pour ajouter un dégagement au coin du pli :

1.  Commencez avec une plaque de base ou une feuille, sélectionnez un sommet d\'angle pour appliquer un dégagement
2.  Cliquez sur l\'outil <img alt="" src=images/SheetMetal_Relief.svg  style="width:24px;"> **Relief** pour ajouter un dégagement coupé au coin.


**Remarque**

: L\'atelier ne possède pas d\'outil pour créer une plaque de base, vous devez donc démarrer votre modèle avec l\'une des méthodes suivantes:

:\* Méthode 1: <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Cube](Part_Box/fr.md)

:\* Méthode 2: Un solide extrudé fait avec une <img alt="" src=images/Part_Extrude.svg  style="width:24px;"> [Part Extrusion](Part_Extrude/fr.md) à partir d\'un:

::\* <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Draft Rectangle](Draft_Rectangle/fr.md) ou d\'un

::\* <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Fil](Draft_Wire/fr.md) ou d\'une

::\* <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketcher Nouvelle esquisse](Sketcher_NewSketch/fr.md)

::\* Utilisez <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> [Part Epaisseur](Part_Thickness/fr.md) pour créer une coque (**Typiquement avec la valeur d'épaisseur de la tôle.**)

:\* Méthode 3: <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Corps](PartDesign_Body/fr.md) contenant soit un

::\* <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:24px;"> [PartDesign Cube additif](PartDesign_AdditiveBox/fr.md) ou une

::\* <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Protrusion](PartDesign_Pad/fr.md) réalisée à partir d\'une <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketcher Nouvelle esquisse](Sketcher_NewSketch/fr.md).

::\* Utilisez <img alt="" src=images/PartDesign_Thickness.svg  style="width:24px;"> [PartDesign Epaisseur](PartDesign_Thickness/fr.md) pour créer une coque (**Typiquement avec la valeur d'épaisseur de la tôle.**)

:   

    :   Si vous commencez avec un <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> PartDesign Corps, vous pouvez mélanger des fonctions de tôlerie avec des fonctions PartDesign telles que <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [PartDesign Cavité](PartDesign_Pocket/fr.md) or <img alt="" src=images/PartDesign_Hole.svg  style="width:24px;"> [PartDesign Perçages](PartDesign_Hole/fr.md).

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




[Category:SheetMetal](Category:SheetMetal.md) [Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md)
