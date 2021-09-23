---
- GuiCommand:/fr
   Name:TechDraw ActiveView
   Name/fr:TechDraw Vue active
   MenuLocation:TechDraw → Insérer la vue active (dans la vue 3D)
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   Version:0.19
   SeeAlso:[TechDraw Symbole SVG](TechDraw_Symbol/fr.md)
---

# TechDraw ActiveView/fr

## Description

L\'outil Vue active insère une copie d\'une fenêtre 3D dans une page de dessin.

![](images/TechDraw_ActiveView_example.png )


*Une vue simple du modèle 3D qui n'effectue aucun calcul complexe.*

## utilisation

1.  Naviguez jusqu\'à la fenêtre 3D que vous souhaitez copier.
2.  Si votre document contient plusieurs pages de dessin, vous devez également sélectionner la page souhaitée dans l\'arborescence.
3.  Appuyez sur le bouton **<img src="images/TechDraw_ActiveView.svg" width=16px> [Insérer la vue active (dans la vue 3D)](TechDraw_ActiveView/fr.md)**.
4.  Une boîte de dialogue s\'ouvre pour vous permettre de spécifier la taille, la bordure et la couleur d\'arrière-plan de la copie.

## Remarques

-   Les vues actives sont statiques une fois générées, elles ne sont jamais mises à jour avec les modifications apportées au modèle 3D.
-   Vue active est en coulisses un <img alt="" src=images/TechDraw_Symbol.svg  style="width:24px;">[Symbole](TechDraw_Symbol/fr.md). Sa {{PropertyData/fr|Scale Type}} est donc toujours initialisé comme *Personnalisé*.
-   Cet outil est encore quelque peu **Expérimental**.

## Propriétés

Voir <img alt="" src=images/TechDraw_Symbol.svg  style="width:16px;"> [TechDrawSymbol](TechDraw_Symbol/fr.md)

### Champs de dialogue 

-    {{PropertyData/fr|Width}}: La largeur de la vue générée.

-    {{PropertyData/fr|Height}}: hauteur de la vue générée.

-    {{PropertyData/fr|Border}}: La quantité d\'espace vide à laisser autour de la vue (mais dans la largeur x la hauteur).

-    {{PropertyData/fr|Background}}: affiche ou masque un arrière-plan.

-    {{PropertyData/fr|Background Color}}: Couleur pour peindre le fond, le cas échéant.

-    {{PropertyData/fr|Line Width}}: Épaisseur des lignes individuelles dans la vue.

-    {{PropertyData/fr|Render Mode}}: Le [mode de rendu](https://grey.colorado.edu/coin3d/classSoRenderManager.html#a4b8d99cff0fd91e31bc2c5d33610f6eb) de la bibliothèque [Coin3d](https://en.wikipedia.org/wiki/Coin3D). Les modes possibles sont:

    -   **AS\_IS** rendu des primitives telles qu\'elles sont
    -   **WIREFRAME** rendu des polygones en filaire
    -   **POINTS** rendu uniquement des sommets des polygones et des lignes
    -   **WIREFRAME\_OVERLAY** rendu d\'une superposition filaire en plus du mode **AS\_IS**
    -   **HIDDEN\_LINE** comme **WIREFRAME** mais élimine les lignes qui autrement ne seraient pas affichées en raison de l\'abattage géométrique
    -   **BOUNDING\_BOX** n\'affiche que la boîte englobante de chaque objet

## Script


**See also:**

[TechDraw API](TechDraw_API/fr.md) et [FreeCAD Script de Base](FreeCAD_Scripting_Basics/fr.md).

L\'outil ActiveView peut être utilisé dans [macros](macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
import TechDrawGui
TechDrawGui.copyActiveViewToSvgFile(Gui.ActiveDocument.ActiveView,"myFile.svg")
```





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ActiveView/fr
