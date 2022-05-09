---
- GuiCommand   */fr
   Name   *TechDraw SectionView
   Name/fr   *TechDraw Vue en coupe
   MenuLocation   *TechDraw → Insérer une vue en coupe
   Workbenches   *[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso   *[TechDraw Vue](TechDraw_View/fr.md), [TechDraw Groupe de projection](TechDraw_ProjectionGroup/fr.md)
---

# TechDraw SectionView/fr

## Description

L\'outil Vue en coupe crée une vue en coupe en fonction d\'une vue existante d\'une pièce.

<img alt="" src=images/TechDraw_Section_example.png  style="width   *250px;"> 
*Vue en coupe déjà placée qui montre les trous internes et une surface de coupe ombrée*

## Utilisation

1.  Sélectionnez une vue de pièce dans la fenêtre ou l\'arborescence 3D.
2.  Appuyez sur le bouton **<img src="images/TechDraw_SectionView.svg" width=16px> [Insérer une vue en coupe](TechDraw_SectionView/fr.md)
**
3.  Une boîte de dialogue s\'ouvrira qui vous aidera à calculer les différentes propriétés de la section. La boîte de dialogue calcule des points de départ raisonnables pour SectionNormal et la direction de la vue mais ceux-ci peuvent être modifiés après la création pour des besoins spéciaux.
4.  Si vous faites une erreur ou changez d\'avis lors de la configuration des paramètres de la section, appuyez sur le bouton **Réinitialiser** et vous pouvez recommencer.

![](images/TechDraw_Section_Taskview.png ) 
*Boîte de dialogue pour définir la zone de la vue en coupe*

## Propriétés

### Données

#### Section

-    **Base View**   * La vue de référence sur laquelle cette coupe est basée.

-    **Section Normal**   * Un vecteur décrivant la direction normale au plan de coupe.

-    **Section Origin**   * Un vecteur décrivant un point sur le plan de coupe. Typiquement le centre de la pièce d\'origine.

-    **Fuse Before Cut**   * Fusionne les formes source avant d\'effectuer la coupe.

#### Format de surface coupée 

-    **Cut Surface Display**   * apparence de la surface de coupe. Options   *

    -   *Hide*   * Masque la surface coupée, seul le contour sera affiché.
    -   *Color*   * Colore la surface de coupe en utilisant le réglage de **Cut Surface Color** dans [TechDraw Préférences](TechDraw_Preferences/fr.md).
    -   *SvgHatch*   * hachure la section coupée à l\'aide de [Hachures](TechDraw_Hatch/fr.md)
    -   *PatHatch*   * hachure la section coupée à l\'aide de [Hachures géométriques](TechDraw_GeometricHatch/fr.md)

-    **File Hatch Pattern**   * chemin complet vers le fichier de motif de hachures SVG.

-    **File Geom Pattern**   * Chemin complet vers le fichier de modèle PAT.

-    **Svg Included**   * chemin complet vers le fichier de motif de hachures SVG inclus.

-    **Pat Included**   * chemin complet vers le fichier de modèle PAT inclus.

-    **Name Geom Pattern**   * nom du modèle PAT à utiliser (ignoré pour le paramètre *SvgHatch* de **Cut Surface Display**).

### Vue

#### Surface de section 

-    **Cut Surface Color**   * couleur unie pour la mise en évidence de la surface. Utilisé si **Cut Surface Display** est réglé sur *Color*.

#### Surface hachurée 

-    **Hatch Color**   * couleur des lignes de hachures de surface.

-    **Weight Pattern**   * épaisseur de ligne pour les lignes de hachures de surface.

### Base View 

Une vue de section hérite de toutes les propriétés applicables de la vue spécifiée comme **BaseView**. Dans les propriétés de la vue, vous pouvez modifier l\'apparence de la ligne de coupe   *

-    **Section Line Color**   * couleur de la ligne de coupe.

-    **Section Line Style**   * style de la ligne de coupe.

Les paramètres par défaut de ces paramètres sont définis via les paramètres **Section Line** et **Section Line Style** dans les [TechDraw Préférences](TechDraw_Preferences/fr.md).

## Script


**Voir aussi   ***

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Vue en coupe peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes   *


```python
view = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewPart','View')
rc = page.addView(view)
view.Source = box
view.Direction = (0.0,0.0,1.0)

section = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewSection','Section')
rc = page.addView(section)
section.Source = box
section.BaseView = view
section.Direction = (0.0,1.0,0.0)
section.SectionNormal = (0.0,0.0,1.0)
section.SectionOrigin = (5.0,5.0,5.0)
```

## Remarques

-   **Section Line Format**   * le format de ligne de section traditionnel (comme illustré ci-dessus) et la \"méthode de flèche de référence\" sont pris en charge. Cette option est contrôlée par le paramètre de préférence \"Mod/TechDraw/Format/SectionFormat\" (voir [Std Editeur des paramètres](Std_DlgParameter/fr.md)). 0 pour la ligne traditionnelle, 1 pour la méthode de la flèche de référence.
-   **CutSurfaceDisplay**   * la surface coupée peut être cachée, peinte dans une couleur unie, hachurée en utilisant un motif Svg (par défaut) ou hachurée en utilisant un motif PAT. Voir [Hachure](TechDraw_Hatching/fr.md).
-   **FuseBeforeCut**   * l\'opération de section échoue parfois à couper les formes source. Si FuseBeforeCut a la valeur true, les formes sources sont fusionnées en une seule forme avant que l\'opération de section ne soit tentée. Si vous rencontrez des problèmes avec l\'opération de section, essayez de retourner cette valeur.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SectionView/fr
