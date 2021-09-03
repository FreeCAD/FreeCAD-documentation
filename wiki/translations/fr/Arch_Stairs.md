---
- GuiCommand:/fr
   Name:Arch Stairs
   Name/fr:Arch Escalier
   MenuLocation:Arch → Escalier
   Workbenches:[Arch](Arch_Module/fr.md)
   Shortcut:**S** **R**
   Version:0.14
   SeeAlso:[Arch Structure](Arch_Structure/fr.md), [Arch Equipement](Arch_Equipment/fr.md)
---


</div>

## Description

L\'outil [escaliers](Arch_Stairs/fr.md) vous permet de construire automatiquement plusieurs types d\'escaliers. À l\'heure actuelle, seuls les escaliers droits (avec ou sans palier central) sont pris en charge. Les escaliers peuvent être construits à partir de zéro, ou d\'une ligne droite [Draft Ligne](Draft_Line/fr.md), auquel cas les escaliers suivent la ligne. Si la ligne n\'est pas horizontale mais a une inclinaison verticale, les escaliers suivront également sa pente.

Voir : [Terminologie Escalier](https://fr.wikipedia.org/wiki/Escalier#Terminologie) pour une définition des différents termes utilisés pour décrire les parties d\'un escaliers.

<img alt="" src=images/Arch_Stairs_example.jpg  style="width:640px;"> 
*Deux escaliers ont été créés: l'un avec une structure massive et un palier et un autre avec un seul limon.*

## Options

-   L\'outil stairs (escalier) partage les propriétés communes et les comportements de tous [Arch Composants](Arch_Component/fr.md)

## Utilisation

1.  Appuyez sur le bouton **<img src="images/Arch_Stairs.svg" width=16px> [Crée un objet escalier](Arch_Stairs/fr.md)** ou appuyez sur la touche **S**, **R**.
2.  Ajustez les propriétés souhaitées. Certaines parties de l\'escalier, comme la structure, peuvent ne pas apparaître immédiatement, si l\'une des propriétés rend la construction impossible, par exemple une épaisseur de structure égal à 0.

## Propriétés

Base

-    {{PropertyData/fr|Align}}: L\'alignement de ces escaliers sur leur niveau de référence, le cas échéant.

-    {{PropertyData/fr|Base}}: La base de ces marches, le cas échéant.

-    {{PropertyData/fr|Height}}: La hauteur totale de ces escaliers, s\'ils ne reposent pas sur une base de référence, ou la ligne de base est horizontale.

-    {{PropertyData/fr|Length}}: La longueur totale de ces escaliers si aucune ligne de base n\'est définie.

-    {{PropertyData/fr|Width}}: La largeur de ces marches.

Marche

-    {{PropertyData/fr|Nosing}}: La taille du nez.

-    {{PropertyData/fr|Number of Steps}}: Le nombre de marches (Contremarches) dans ces escaliers.

-    {{PropertyData/fr|Riser Height}}: La hauteur des contremarches.

-    {{PropertyData/fr|Tread Depth}}: La profondeur des marche

-    {{PropertyData/fr|Tread Thickness}}: L\'épaisseur des marches.

Structure

-    {{PropertyData/fr|Landings}}: Le type de paliers.

-    {{PropertyData/fr|Stringer Offset}}: Le décalage entre le bord de l\'escalier et de la structure.

-    {{PropertyData/fr|Stringer Width}}: La largeur des limons

-    {{PropertyData/fr|Structure}}: Le type de structure de ces escaliers.

-    {{PropertyData/fr|Structure Thickness}}: L\'épaisseur de la structure.

-    {{PropertyData/fr|Winders}}: Le type de marches.

## Limitations

-   Seuls les escaliers droits sont disponible pour le moment
-   Voir la [forum entry](http://forum.freecadweb.org/viewtopic.php?f=23&t=6534) pour les escaliers circulaires
-   Voir la [forum announcement](http://forum.freecadweb.org/viewtopic.php?f=9&t=4564).

## Procédure


**Voir aussi:**

[API](Arch_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

Les escaliers peuvent être créés à partir de scripts [Python](Python/fr.md) et de [macro](macros/fr.md) en utilisant la fonction suivante: 
```python
Stairs = makeStairs(baseobj=None, length=None, width=None, height=None, steps=None, name="Stairs")
```

-   Crée un objet avec les attributs donnés
-   Retourne le nouvel objet escalier

-   Crée un objet `Stairs` à partir de `baseobj` donné.
-   Si `baseobj` n\'est pas indiqué, il utilisera `length`, `width`, `height` et `steps` pour construire un objet solide.

Exemple: 
```python
import Arch

Stairs = Arch.makeStairs(length=5000, width=1200, height=3000, steps=14)
```


<div class="mw-translate-fuzzy">





</div>


 
