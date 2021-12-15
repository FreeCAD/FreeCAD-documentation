---
- GuiCommand:/fr
   Name:TechDraw GeometricHatch
   Name/fr:TechDraw Hachures géométriques
   MenuLocation:TechDraw → Appliquer un motif de hachure géométrique à une face
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso:[TechDraw Hachures par motif](TechDraw_Hatch/fr.md), [TechDraw Hachures](TechDraw_Hatching/fr.md)
---

# TechDraw GeometricHatch/fr

## Description

L\'outil Hachures géométriques remplit une région fermée dans une vue avec un motif basé sur une spécification de hachures AutoDesk PAT. **Alternativement**, l\'outil [TechDraw Hachures par motif](TechDraw_Hatch/fr.md) utilise un fichier [SVG](SVG/fr.md) ou [bitmap](bitmap/fr.md) comme motif de hachures, voir [TechDraw Hachures](TechDraw_Hatching/fr.md) pour plus de détails.

<img alt="" src=images/TechDraw_GeomHatch_example.png  style="width:300px;"> 
*Motif de hachures géométriques sur une face*

## Utilisation

1.  Sélectionnez une région fermée dans une vue. La région deviendra verte.
2.  Appuyez sur le bouton **<img src="images/TechDraw_GeometricHatch.svg" width=16px> [Appliquer un motif de hachure géométrique à une face](TechDraw_GeometricHatch/fr.md)
**
3.  Une boîte de dialogue s\'ouvrira où vous pourrez sélectionner votre motif, l\'échelle, l\'épaisseur du trait et la couleur.

## Remarques

-   Les objets hachurés sont vulnérables au \"[problème de nommage topologique](Topological_naming_problem/fr.md)\". Voir [TechDraw Cote de longueur](TechDraw_LengthDimension/fr.md) pour plus d\'informations. Il est recommandé que le hachurage soit l\'une des dernières étapes de votre processus de dessin.

Un petit ensemble de modèles d\'échantillons est disponible dans:


```python
$INSTALL_DIR/data/Mod/TechDraw/PAT/FCPAT.pat
```


`$INSTALL_DIR`

est le répertoire où FreeCAD a été installé, par exemple


```python
/usr/share/freecad/data/Mod/TechDraw/PAT/FCPAT.pat
```

## Propriétés

-    **Source**: vue et la face pour recevoir le motif de hachures.

-    **File Pattern**: emplacement du fichier PAT à utiliser.

-    **Name Pattern**: nom de la spécification PAT dans File Pattern.

-    **Scale Pattern**: échelle à appliquer au motif (doit être\> 0.0).

-    **Weight Pattern**: épaisseur des lignes de motif.

-    **Color Pattern**: couleur des lignes de motif.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Hachures géométriques peut être utilisé dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
hatch = FreeCAD.ActiveDocument.addObject('TechDraw::DrawGeomHatch','GeomHatch')
hatch.Source = (view1,["Face0"])
hatch.FilePattern = "path/to/myPATfile.pat"
hatch.NamePattern = "Diamond"
rc = page.addView(hatch)
```

Il est également possible d\'utiliser le moteur de hachures géométriques de TechDraw pour produire un objet composé dans l\'espace 3D. Il faut faire attention que la face de base se trouve sur le plan XY, car l\'algorithme n\'est pas encore adapté aux autres cas :


```python
import TechDraw
face = Part.makePlane(10,10)
patfile = "path/to/myPATfile.pat"
pattern = "Diamond"
scale = 10
hatch = TechDraw.makeGeomHatch(face, scale, pattern, patfile)
Part.show(hatch)
```





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw GeometricHatch/fr
