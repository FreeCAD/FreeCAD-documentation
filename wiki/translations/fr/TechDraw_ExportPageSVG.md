---
- GuiCommand   */fr
   Name   *TechDraw ExportPageSVG
   Name/fr   *TechDraw Exporter au format SVG
   MenuLocation   *TechDraw → Exporter une page au format SVG
   Workbenches   *[TechDraw](TechDraw_Workbench/fr.md)
   Version   *0.19
   SeeAlso   *[TechDraw Modèles](TechDraw_Templates/fr.md), [Draft SVG](Draft_SVG/fr.md)
---

# TechDraw ExportPageSVG/fr

## Description

L\'outil Exporter la page enregistre la page de dessin en cours sous forme de fichier [SVG](SVG/fr.md).

## Utilisation

1.  Appuyez sur le bouton **<img src="images/TechDraw_ExportPageSVG.svg" width=16px> [Exporter une page au format SVG](TechDraw_ExportPageSVG/fr.md)**.
2.  Une boîte de dialogue d\'enregistrement de fichier s\'ouvrira. Sélectionnez un emplacement et un nom de fichier.

## Remarques

-   Les modèles [TechDraw Hachures par motifs](TechDraw_Hatch/fr.md) ne sont pas exportés vers [SVG](SVG/fr.md) en raison d\'une limitation de la prise en charge SVG de Qt4.
-   Les positions et tailles de texte ne sont pas correctes dans le fichier exporté. L\'utilisation de la police par défaut \"système\" dans le dessin améliore considérablement le problème de taille.

## Script


**Voir aussi   ***

[TechDrawGui API](TechDrawGui_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Exporter au format SVG peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes   *


```python
TechDrawGui.exportPageAsSvg(DrawPageObject,FilePath)
```

Notez que le module FreeCADGui doit être actif pour utiliser cette fonction.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExportPageSVG/fr
