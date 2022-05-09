---
- GuiCommand   */fr
   Name   *TechDraw ShareView
   Name/fr   *TechDraw Copier une vue
   MenuLocation   *TechDraw → Copier une vue
   Workbenches   *[TechDraw](TechDraw_Workbench/fr.md)
   Version   *0.20
   SeeAlso   *[TechDraw Déplacer une vue](TechDraw_MoveView/fr.md)
---

# TechDraw ShareView/fr

## Description

L\'outil <img alt="" src=images/TechDraw_ShareView.svg  style="width   *24px;"> **TechDraw Copier une vue** rend visible une vue et toutes ses dépendances (infobulles, cotes, etc.) sur une deuxième page.

## Utilisation

1.  Sélectionnez éventuellement une vue, une page de départ et une page d\'arrivée. Les pages doivent être sélectionnées dans cet ordre.
2.  Il existe plusieurs façons de lancer l\'outil    *
    -   Appuyez sur le bouton **<img src="images/TechDraw_ShareView.svg" width=16px> [Copier la vue](TechDraw_ShareView/fr.md)**.
    -   Sélectionnez l\'option **TechDraw → <img src="images/TechDraw_ShareView.svg" width=16px> Copier la vue** à partir du menu.
3.  Une boîte de dialogue s\'ouvre pour vous permettre de sélectionner une Vue, de la Page de départ et à la Page d\'arrivée.
4.  Appuyez sur le bouton **OK**.

## Script


**Voir aussi   ***

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Copier une vue peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes   *


```python
import TechDrawTools
#MoveView with a True parameter in the last position performs a copy
TechDrawTools.MoveView(viewName, fromPageName, toPageName, True)
```

## Remarques

Il n\'y a qu\'un seul objet Vue après l\'opération de partage. Toute modification apportée à la vue sera répercutée sur les deux pages. Si la vue est supprimée d\'une page, elle sera également supprimée de l\'autre.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ShareView/fr
