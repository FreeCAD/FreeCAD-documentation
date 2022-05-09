---
- GuiCommand   */fr
   Name   *Arch Panel Cut
   Name/fr   *Arch Découpe de panneaux
   MenuLocation   *Arch → Outils pour les panneaux → Panneau de coupe
   Workbenches   *[Arch](Arch_Workbench/fr.md), [Path](Path_Workbench/fr.md)
   Shortcut   ***P** **C**
   Version   *0.17
   SeeAlso   *[Arch Panneaux](Arch_Panel/fr.md), [Arch Panneau feuille](Arch_Panel_Sheet/fr.md), [Arch Calepinage](Arch_Nest/fr.md)
---

# Arch Panel Cut/fr

## Description

Cet outil crée, dans le document 3D, une vue 2D plane d\'un objet [Panneaux](Arch_Panel/fr.md), à inclure dans un [Arch Panneau feuille](Arch_Panel_Sheet/fr.md) ou directement exportée vers [DXF](Draft_DXF/fr.md). Les objets Découpe de panneaux sont également pris en charge par l\'[atelier Path](Path_Workbench/fr.md).

<img alt="" src=images/Arch_Wikihouse_02.jpg  style="width   *1024px;">

## Utilisation

1.  Sélectionner un ou plusieurs objets [Arch Panneaux](Arch_Panel/fr.md)
2.  Presser la touche **<img src="images/Arch_Panel_Cut.svg" width=16px> [Panneau de coupe](Arch_Panel_Cut/fr.md)
** ou presser les touches **P** et **C**
3.  Ajuster les propriétés désirées

## Options

-   Si le panneau n\'est pas plat (par exemple un panneau ondulé), le relief n\'apparaîtra pas dans la coupe du panneau. Cet outil est utile principalement pour les panneaux plats
-   La découpe du panneau peut afficher une étiquette. Cette balise peut être une ligne de texte personnalisée ou peut afficher automatiquement la balise, l\'étiquette ou la description de son panneau est liée.
-   Pour être utile à l\'usinage CNC, l\'étiquette doit être écrite en utilisant une police collante, où les lettres sont de simples polylignes que la machine peut facilement suivre. Lors de sa création, l\'objet Panel Cut utilisera automatiquement la police spécifiée dans Édition → Préférences → Brouillon → Textes et dimensions → Police ShapeString
-   Après sa création double-cliquer dans l\'arborescence sur le panneau coupé vous fait passer en mode édition et vous permet de modifier la position du tag
-   Lorsque vous devez mettre en forme différentes découpes de panneaux, les découpes de panneaux peuvent afficher une marge, ce qui est utile pour s\'assurer qu\'un certain espace est toujours présent entre une découpe et une autre

## Propriétés

### Données

-    **Source**   * L\'objet [Arch Panneaux](Arch_Panel/fr.md) montré par cette coupe.

-    **Tag Text**   * Le texte à afficher. Peut être %tag%, %label% ou %description% pour afficher la balise ou l\'étiquette du panneau.

-    **Tag Size**   * La taille du texte de la balise

-    **Tag Position**   * La position du texte de la balise. Conservez (0,0,0) pour une position centrale automatique.

-    **Tag Rotation**   * La rotation du texte de la balise

-    **Font File**   * La police du texte de la balise

-    **Make Face**   * Si True, le panneau est un Part Face, sinon une Part Polyligne.

### Vue

-    **Margin**   * La marge à afficher hors du panneau coupé.

-    **Show Margin**   * Tourne l\'affichage des marges oui/non.

## Script


**Voir aussi   ***

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil panneau peut être utilisé dans une [macro](Macros/fr.md) et dans la console [Python](Python/fr.md) en utilisant le code suivant   * 
```python
View = makePanelCut(panel, name="PanelView")```

-   Crée un objet `View` (projection 2D) à partir du `panel` existant.

Exemple   * 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(500, 0, 0)
p3 = FreeCAD.Vector(500, 50, 0)
p4 = FreeCAD.Vector(550, 50, 0)
p5 = FreeCAD.Vector(600, 0, 0)
p6 = FreeCAD.Vector(1000, 0, 0)
p7 = FreeCAD.Vector(1000, 400, 0)
p8 = FreeCAD.Vector(600, 400, 0)
p9 = FreeCAD.Vector(600, 350, 0)
p10 = FreeCAD.Vector(550, 350, 0)
p11 = FreeCAD.Vector(500, 400, 0)
p12 = FreeCAD.Vector(0, 400, 0)

Wire = Draft.makeWire([p1, p2, p3, p4, p5, p6,
                       p7, p8, p8, p9, p10, p11, p12], closed=True)
Panel = Arch.makePanel(Wire, thickness=36)
FreeCAD.ActiveDocument.recompute()

View = Arch.makePanelCut(Panel)
View.ViewObject.LineWidth = 3
FreeCAD.ActiveDocument.recompute()
```

## Tutoriels

-   [tutoriel Wikihouse](Wikihouse_porting_tutorial/fr.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Panel Cut/fr
