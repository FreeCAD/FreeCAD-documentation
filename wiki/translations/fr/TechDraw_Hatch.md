---
- GuiCommand:/fr
   Name:TechDraw Hatch
   Name/fr:TechDraw Hachures par motif
   MenuLocation:TechDraw → Hachurer une face en utilisant un fichier image
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso:[TechDraw Hachures géométriques](TechDraw_GeometricHatch/fr.md), [TechDraw Hachures](TechDraw_Hatching/fr.md)
---

# TechDraw Hatch/fr

## Description

L\'outil Hachures remplit une région fermée dans une vue avec un motif de hachures, qui peut être des fichiers [SVG](SVG/fr.md) ou [bitmap](bitmap/fr.md). Au contraire, l\'outil <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:24px;"> [TechDraw Hachures géométriques](TechDraw_GeometricHatch/fr.md) utilise un fichier de modèle PAT spécifique, voir [Hachures](TechDraw_Hatching/fr.md) pour plus de détails.

<img alt="" src=images/TechDraw_Hatch_example.png  style="width:300px;">



*Motif de hachures SVG sur une face*

## Utilisation

1.  Sélectionnez une région fermée dans une vue. La région deviendra verte.
2.  Appuyez sur le bouton **<img src="images/TechDraw_Hatch.svg" width=16px> [Hachurer une face en utilisant un fichier image](TechDraw_Hatch/fr.md)
**
3.  Une boîte de dialogue s\'ouvre dans laquelle vous pouvez sélectionner le fichier de motif, l\'échelle et la couleur.

## Notes

-   Les objets hachurés sont vulnérables au \"[problème de nommage topologique](Topological_naming_problem/fr.md)\". Voir [TechDraw Cote de longueur](TechDraw_LengthDimension/fr.md) pour plus d\'informations. Il est recommandé que le hachurage soit l\'une des dernières étapes de votre processus de dessin.
-   Des exemples de modèles [SVG](SVG/fr.md) sont disponibles localement dans:


```python
$INSTALL_DIR/data/Mod/TechDraw/Patterns
```

où `$INSTALL_DIR` est le répertoire où FreeCAD a été installé, par exemple 
```python
/usr/share/freecad/data/Mod/TechDraw/Patterns
``` et aussi à l\'adresse [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Mod/TechDraw/Patterns).

## Propriétés

-    **Source**: la vue et la région qui va recevoir le motif de hachures.

-    **Hatch Pattern**: chemin d\'accès complet et nom de fichier vers un fichier de motif SVG.

-    **Hatch Color**: le motif de hachures sera affiché dans cette couleur.

-    **Hatch Scale**: modificateur de taille de motif de hachures.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Hachures par motif peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
hatch = FreeCAD.ActiveDocument.addObject('TechDraw::DrawHatch','Hatch')
hatch.Source = (view1,["Face0"])
hatch.HatchPattern = hatchFileSpec
rc = page.addView(hatch)
```





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Hatch/fr
