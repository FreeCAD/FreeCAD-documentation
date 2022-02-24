---
- GuiCommand:/fr
   Name:TechDraw MoveView
   Name/fr:TechDraw Déplacer une vue
   MenuLocation:TechDraw → Déplacer une vue
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   Version:0.20
   SeeAlso:[TechDraw Copier une vue](TechDraw_ShareView/fr.md)
---

# TechDraw MoveView/fr

## Description

L\'outil <img alt="" src=images/TechDraw_MoveView.svg  style="width:24px;"> **TechDraw Déplacer une vue** déplace une vue et toutes ses dépendances (infobulles, cotes, etc.) vers une autre page.

## Utilisation

1.  Sélectionnez au choix une vue, une page de départ et une page d\'arrivée. Les pages doivent être sélectionnées dans cet ordre.
2.  Il existe plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/TechDraw_MoveView.svg" width=16px> [Déplacer une vue](TechDraw_MoveView/fr.md)**.
    -   Sélectionnez l\'option **TechDraw → <img src="images/TechDraw_MoveView.svg" width=16px> Déplacer la vue** à partir du menu.
3.  Une boîte de dialogue s\'ouvre pour vous permettre de sélectionner une Vue, de la Page de départ et à la Page d\'arrivée.
4.  Appuyez sur le bouton **OK**.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Déplacer une vue peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
import TechDrawTools
TechDrawTools.MoveView(viewName, fromPageName, toPageName)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw MoveView/fr
