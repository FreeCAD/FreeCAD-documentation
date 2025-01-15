---
 GuiCommand:
   Name: Arch Panel Cut
   Name/fr: Arch Découpe de panneau
   MenuLocation: Utilitaires , Outils pour les panneaux , Découpe de panneau
   Workbenches: BIM_Workbench/fr
   Shortcut: **P** **C**
   Version: 0.17
   SeeAlso: Arch_Panel/fr, Arch_Panel_Sheet/fr, Arch_Nest/fr
---

# Arch Panel Cut/fr

## Description

L\'outil **Arch Découpe de panneau** crée, dans le document 3D, une vue 2D plane d\'un objet [Panneau](Arch_Panel/fr.md), à inclure dans une [Arch Feuille de panneaux](Arch_Panel_Sheet/fr.md) ou directement exportée vers un [DXF](Draft_DXF/fr.md). Les objets Découpe de panneau sont également pris en charge par l\'[atelier CAM](CAM_Workbench/fr.md).

<img alt="" src=images/Arch_Wikihouse_02.jpg  style="width:1024px;">



## Utilisation

1.  Sélectionner un ou plusieurs objets [Arch Panneau](Arch_Panel/fr.md)
2.  Sélectionner l\'option **Utilitaires → Outils pour les panneaux → <img src="images/Arch_Panel_Cut.svg" width=16px> Découpe de panneau** du menu.
3.  Ajuster les propriétés désirées

## Options

-   Si le panneau n\'est pas plat (par exemple un panneau ondulé), le relief n\'apparaîtra pas dans la découpe du panneau. Cet outil est surtout utile pour les panneaux plats.
-   La découpe du panneau peut afficher une balise. Cette balise peut être une ligne de texte personnalisée ou peut automatiquement afficher la balise, l\'étiquette ou la description du panneau auquel elle est liée.
-   Pour être utile à l\'usinage CNC, la balise doit être écrite en utilisant une police de caractères bâton, où les lettres sont des polylignes simples qui sont faciles à suivre par la machine. Lors de sa création, l\'objet Panel Cut utilise automatiquement la police spécifiée dans Édition → Préférences → Draft → Textes et cotes → Fichier de la police par défaut de Formes à partir de texte.
-   Un double-clic sur la découpe de panneau dans la vue en arborescence après sa création vous permet d\'entrer en mode édition et de modifier la position de la balise.
-   Lorsque vous avez besoin de mettre en page différentes découpes de panneaux ensemble, les découpes de panneaux peuvent afficher une marge, ce qui est utile pour s\'assurer qu\'un certain espace est toujours présent entre une coupe et une autre.



## Propriétés



### Données

-    **Source**: l\'objet [Arch Panneau](Arch_Panel/fr.md) montré par cette découpe.

-    **Tag Text**: le texte à afficher. Peut être %tag%, %label% ou %description% pour afficher la balise ou l\'étiquette du panneau.

-    **Tag Size**: taille du texte de l\'étiquette

-    **Tag Position**: position du texte de l\'étiquette. Laisser à (0,0,0) pour une position centrale automatique.

-    **Tag Rotation**: rotation du texte de l\'étiquette

-    **Font File**: police du texte de l\'étiquette

-    **Make Face**: si mis à vrai, le panneau est une Part Face, sinon une Part Polyligne.



### Vue

-    **Margin**: marge à afficher hors du panneau coupé.

-    **Show Margin**: active/désactive l\'affichage de la marge



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Découpe de panneau peut être utilisé dans une [macro](Macros/fr.md) et dans la console [Python](Python/fr.md) en utilisant le code suivant : 
```python
View = makePanelCut(panel, name="PanelView")```

-   Crée un objet `View` (projection 2D) à partir du `panel` existant.

Exemple : 
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

-   [Tutoriel de portage Wikihouse](Wikihouse_porting_tutorial/fr.md)



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Panel Cut/fr
