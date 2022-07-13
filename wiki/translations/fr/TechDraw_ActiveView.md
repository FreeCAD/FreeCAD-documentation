---
- GuiCommand   */fr
   Name   *TechDraw ActiveView
   Name/fr   *TechDraw Vue active
   MenuLocation   *TechDraw → Insérer la vue active (dans la vue 3D)
   Workbenches   *[TechDraw](TechDraw_Workbench/fr.md)
   Version   *0.19
   SeeAlso   *[TechDraw Symbole SVG](TechDraw_Symbol/fr.md)
---

# TechDraw ActiveView/fr

## Description

L\'outil Vue active insère une copie d\'une fenêtre 3D dans une page de dessin.

![](images/TechDraw_ActiveView_example.png ) 
*Une vue simple du modèle 3D qui n'effectue aucun calcul complexe.*

## utilisation

1.  Aller à la bonne [Vue 3D](3D_view/fr.md).
2.  S\'il y a plusieurs pages de dessin dans le document    * sélectionnez éventuellement la page souhaitée dans la [Vue en arborescence](Tree_view/fr.md). Ceci n\'est pas optionnel pour {{VersionMinus/fr|0.19}}.
3.  Il existe plusieurs façons de lancer l\'outil    *
    -   Appuyez sur le bouton **<img src="images/TechDraw_ActiveView.svg" width=16px> [Insérer la vue active (dans la vue 3D)](TechDraw_ActiveView/fr.md)**.
    -   Sélectionnez le bouton **TechDraw → <img src="images/TechDraw_ActiveView.svg" width=16px> Insérer la vue active (dans la vue 3D)** dans le menu.
4.  S\'il y a plusieurs pages de dessin dans le document et que vous n\'avez pas encore sélectionné de page, la boîte de dialogue **Sélecteur de page** s\'ouvre    * {{Version/fr|0.20}}
    1.  Sélectionnez la page souhaitée.
    2.  Appuyez sur le bouton **OK**.
5.  Le panneau de tâches **De la vue active à la vue TechDraw** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
6.  Appuyez sur le bouton **OK**.

## Options

Les éléments suivants peuvent être spécifiés    *

-    **Largeur**   * La largeur de la vue générée.

-    **Hauteur**   * La hauteur de la vue générée.

-    **Décalage**   * La quantité d\'espace vide à laisser autour de la vue (mais dans les limites de la largeur x de la hauteur).

-    **Arrière-plan**   * Si la case est cochée, un arrière-plan de la couleur spécifiée est ajouté.

-    **Epaisseur de ligne**   * L\'épaisseur des lignes dans la vue.

-    **Type de rendu**   * Les modes disponibles sont    *

    -   
        {{Value|Comme maintenant}}
        
           * Rendu des primitives telles qu\'elles sont.

    -   
        {{Value|Filaire}}
        
           * Rendu des polygones sous forme filaire.

    -   
        {{Value|Points}}
        
           * Rendu uniquement des sommets des polygones et des lignes.

    -   
        {{Value|Superposition filaire}}
        
           * Rendu d\'une superposition filaire en plus du mode {{Value|Comme maintenant}}.

    -   
        {{Value|Lignes cachées}}
        
           * Comme {{Value|Filaire}}, mais élimine les lignes qui ne seraient pas affichées autrement en raison de l\'élimination géométrique.

    -   
        {{Value|Cadre de sélection}}
        
           * Affiche uniquement la boîte englobante de chaque objet.

## Remarques

-   Les vues actives sont statiques une fois générées, elles ne sont jamais mises à jour avec les modifications apportées au modèle 3D.
-   Une Vue active est en réalité un [Symbole](TechDraw_Symbol/fr.md). Sa **Scale Type** est donc toujours initialisée à {{Value|Custom}}.
-   Cet outil est encore quelque peu **Expérimental**.

## Propriétés

Voir [TechDraw Symbole SVG](TechDraw_Symbol/fr.md).

## Script


**See also   ***

[TechDraw API](TechDraw_API/fr.md) et [FreeCAD Script de Base](FreeCAD_Scripting_Basics/fr.md).

L\'outil ActiveView peut être utilisé dans [macros](macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes   *


```python
import TechDrawGui
TechDrawGui.copyActiveViewToSvgFile(Gui.ActiveDocument.ActiveView,"myFile.svg")
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ActiveView/fr
