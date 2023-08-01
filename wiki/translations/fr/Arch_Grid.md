---
- GuiCommand:
   Name:Arch Grid
   Name/fr:Arch Grille
   MenuLocation:Arch - Outils pour les axes - Grille
   Workbenches:[Arch](Arch_Workbench/fr.md)
   SeeAlso:[Arch Axes](Arch_Axis/fr.md), [Arch Système d'axes](Arch_AxisSystem/fr.md)
---

# Arch Grid/fr

## Description

L\'outil **<img src="images/Arch_Grid.svg" width=16px> [Arch Grille](Arch_Grid/fr.md)** vous permet de placer un objet de type grille dans le document. Cet objet est destiné à servir de base pour construire des objets Arch nécessitant un cadre régulier mais complexe, comme des fenêtres, des murs-rideaux, des grilles de colonnes, des garde-corps, etc. L\'objet Grille est modifiable comme une feuille de calcul où vous pouvez ajouter ou supprimer colonnes et lignes, définissent leur taille et fusionnent les cellules.

La grille est un objet 2D et peut donc être utilisée partout où une forme 2D, tel qu\'un [Dessin](Draft_Workbench/fr.md) ou une [Esquisse](Sketcher_Workbench/fr.md) sont nécessaires, mais elle peut aussi se comporter comme un [Arch Système d\'axes](Arch_AxisSystem/fr.md) et être utilisée pour propager le placement d\'autres objets Arch.

<img alt="" src=images/Arch_Grid_example.jpg  style="width:600px;"> 
*Un tableau de colonnes, un système de garde-corps et une fenêtre, chacun basé sur un objet [Grille](Arch_Grid/fr.md).*

## Utilisation

1.  Appuyez sur le bouton **<img src="images/Arch_Grid.svg" width=16px> [Grille](Arch_Grid/fr.md)**.
2.  Définissez la **Largeur** et la **Hauteur** de la grille dans les propriétés.
3.  Entrez en mode d\'édition en double-cliquant sur l\'objet de grille dans l\'arborescence.
4.  Ajouter des lignes et des colonnes.
5.  Définissez la largeur et la hauteur souhaitées des lignes et des colonnes en double-cliquant sur les en-têtes de ligne ou de colonne.

## Options

-   Une largeur de colonne ou une hauteur de ligne de 0 signifie que sa taille sera automatiquement adaptée à la largeur/hauteur totale de la grille.
-   Les cellules peuvent être fusionnées et non fusionnées en les sélectionnant et en cliquant sur le bouton approprié.
-   Lorsqu\'elle est utilisée comme propriété **Axis** des autres objets Arch, la grille pilotera le positionnement de ces objets. La propriété **Points Output** définit la manière dont les autres objets sont placés sur la grille : au niveau des sommets, des points médians ou des centres de faces.
-   En définissant les propriétés **Auto Height** ou **Auto Width** sur une valeur différente de zéro, le nombre total de lignes/colonnes et leurs hauteurs/largeurs individuelles est ignoré. Au lieu de cela, le nombre maximal de colonnes ou de lignes de la largeur/hauteur automatique donnée est automatiquement créé.

## Propriétés

-    **Rows**: nombre de lignes

-    **Columns**: nombre de colonnes

-    **Row Size**: tailles pour les lignes

-    **Column Size**: tailles des colonnes

-    **Points Output**: type de points 3D produits par cet objet de grille

-    **Width**: largeur totale de cette grille

-    **Height**: hauteur totale de cette grille

-    **Auto Width**: crée des divisions de colonnes automatiques (définies sur 0 pour désactiver)

-    **Auto Height**: crée des divisions de ligne automatiques (définie sur 0 pour désactiver)

-    **Reorient**: en mode point central, si la grille doit réorienter ses doublures le long de la normales des bords ou non

En mode Point centre d\'arête, si la grille doit réorienter ses doublures le long des normales aux arêtes ou non

-    **Hidden Faces**: les indices des faces à cacher

## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Grille peut être utilisé dans une [macro](Macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante :


```python
Grid = makeGrid(name="Grid")
```

-   Créer un objet `Grid`.

Ses attributs `Width`, `Height`, `Rows` et `Columns` peuvent être modifiés directement pour définir l\'apparence de la grille.


```python
import FreeCAD, Draft, Arch
Grid = Arch.makeGrid()

Grid.Width = 5000
Grid.Height = 5000
Grid.Rows = 4
Grid.Columns = 6
FreeCAD.ActiveDocument.recompute()

Structure = Arch.makeStructure(length=200, width=200, height=100)
Draft.move(Structure, FreeCAD.Vector(-100, 0, 0))
Structure.Axis = Grid
FreeCAD.ActiveDocument.recompute() 
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Grid/fr
