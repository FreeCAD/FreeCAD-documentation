---
- GuiCommand   */fr
   Name   *Arch Panel Sheet
   Name/fr   *Arch Feuille de panneau
   MenuLocation   *Arch → Outils pour les panneaux → Panneau de feuille
   Workbenches   *[Arch](Arch_Workbench/fr.md)
   Shortcut   ***P** **S**
   SeeAlso   *[Arch Panneau](Arch_Panel/fr.md), [Arch Découpe de panneaux](Arch_Panel_Cut/fr.md), [Arch Calepinage](Arch_Nest/fr.md)
---

# Arch Panel Sheet/fr

## Description

Cet outil permet de construire une feuille 2D, comprenant un nombre quelconque d\'objets [Panneaux coupés](Arch_Panel_Cut/fr.md), ou tout autre objet 2D tel que ceux réalisés par l\'[atelier Draft](Draft_Workbench/fr.md) et l\'[atelier Sketcher](Sketcher_Workbench/fr.md). La feuille de panneau est généralement réalisée pour mettre en page les coupes à effectuer par une machine CNC. Ces feuilles peuvent ensuite être exportées vers un fichier [DXF](Draft_DXF/fr.md).

<img alt="" src=images/Arch_Wikihouse_03.jpg  style="width   *1024px;">

<img alt="" src=images/Arch_Wikihouse_04.jpg  style="width   *1024px;">

*L\'image ci-dessus montre comment les panneaux apparaissent lors de l\'exportation au format DXF.*

## Comment l\'utiliser 

1.  Sélectionnez un ou plusieurs objets [Arch Découpe de panneaux](Arch_Panel_Cut/fr.md) ou tout autre objet 2D qui se trouve sur le plan XY.
2.  Appuyez sur le bouton **<img src="images/Arch_Panel_Sheet.svg" width=16px> [Feuille de panneau](Arch_Panel_Sheet/fr.md)**, ou appuyez sur les touches **P** puis **S**.
3.  Réglez les propriétés souhaitées.

## Options

-   Après la création du panneau, avec ou sans objets enfants, tout autre objet enfant peut être ajouté/supprimé du panneau en double-cliquant dessus dans l\'arborescence et en ajoutant ou supprimant des objets de son Groupe
-   Double-cliquer sur le panneau dans l\'arborescence permet également de déplacer les objets contenus dans cette feuille, ou de déplacer son tag
-   Il est possible de faire automatiquement des panneaux composés de plusieurs feuilles de matériaux, en élevant sa propriété Sheets
-   Les feuilles des panneaux peuvent afficher une marge, ce qui est utile pour s\'assurer qu\'un certain espace est toujours présent entre les objets intérieurs et la bordure de la feuille
-   Lorsque les panneaux sont exportées au format DXF, les contours, les trous intérieurs et les étiquettes de leurs enfants intérieurs sont placés sur des calques différents, comme indiqué sur l\'image ci-dessus

## Propriétés

### Données

-    **Height**   * La hauteur de la feuille

-    **Width**   * La largeur de la feuille

-    **Fill Ratio**   * Le pourcentage de la surface de la feuille qui est remplie par des coupes (automatique)

-    **Tag Text**   * Le texte à afficher

-    **Tag Size**   * La taille du texte de l\'étiquette

-    **Tag Position**   * La position du texte de l\'étiquette. Conserver (0,0,0) pour la position centrale automatique

-    **Tag Rotation**   * La rotation du texte de l\'étiquette

-    **Font File**   * La police du texte de l\'étiquette

-    **Make Face**   * Si face est réglé sur True, le panneau est une face de la pièce, sinon un fil (contour) de pièce

-    **Grain Direction**   * Cela vous permet donner la direction principale de la fibre du panneau (dans le sens des aiguilles d\'une montre, 0° signifie le haut du panneau)

### Vue

-    **Margin**   * Affichage d\'une marge à l\'intérieur de la bordure du panneau.

-    **Show Margin**   * Active/désactive l\'affichage de la marge.

-    **Show Grain**   * Affiche une texture de fibre (Make Face doit être défini à True).

## Script


**Voir aussi   ***

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Panneau peut être utilisé dans une [macro](Macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant la fonction suivante   *


```python
Sheet = makePanelSheet(panels=[], name="PanelSheet")
```

-   Crée un objet `Sheet` à partir de `panels` qui est une liste d\'objets [Arch Panneaux](Arch_Panel/fr.md).

Exemple   *


```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(500, 200)
Polygon = Draft.makePolygon(5, 750)

p1 = FreeCAD.Vector(1000, 0, 0)
p2 = FreeCAD.Vector(2000, 400, 0)
p3 = FreeCAD.Vector(1250, 800, 0)
Wire = Draft.makeWire([p1, p2, p3], closed=True)

Panel1 = Arch.makePanel(Rect, thickness=36)
Panel2 = Arch.makePanel(Polygon, thickness=36)
Panel3 = Arch.makePanel(Wire, thickness=36)
FreeCAD.ActiveDocument.recompute()

Cut1 = Arch.makePanelCut(Panel1)
Cut2 = Arch.makePanelCut(Panel2)
Cut3 = Arch.makePanelCut(Panel3)
Cut1.ViewObject.LineWidth = 3
Cut2.ViewObject.LineWidth = 3
Cut3.ViewObject.LineWidth = 3
FreeCAD.ActiveDocument.recompute()

Sheet = Arch.makePanelSheet([Cut1, Cut2, Cut3])
```

## Tutoriels

-   [Tutoriel de portage Wikihouse](Wikihouse_porting_tutorial/fr.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Panel Sheet/fr
