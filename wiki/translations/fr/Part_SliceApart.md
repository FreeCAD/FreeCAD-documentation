---
- GuiCommand:/fr
   Name:Part SliceApart
   Name/fr:Part Séparer/exploser
   MenuLocation:Part → Scinder → Séparer et exploser
   Workbenches:[Part](Part_Workbench/fr.md)
   Version:0.18
   SeeAlso:[Part Scinder](Part_Slice/fr.md), [Part Éclater le composé](Part_ExplodeCompound/fr.md)
---

# Part SliceApart/fr

## Description

Outil pour diviser des formes par intersection avec d\'autres formes. Par exemple, pour une boîte et un plan, deux solides sont créés. ![600px](images/Part_Slice_Demo.png)



*Ci-dessus : les morceaux ont été séparés manuellement par la suite pour révéler le découpage.*

[Séparer/exploser](Part_SliceApart/fr.md) est identique à <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Part Scinder](Part_Slice/fr.md) suivi de <img alt="" src=images/Part_ExplodeCompound.svg  style="width:24px;"> [Part Éclater le composé](Part_ExplodeCompound/fr.md). Alors que \"Slice to compound (Scinder vers composé)\" est totalement paramétrique et ne pose aucun problème lorsque le nombre de pièces change, \"Slice apart (Séparer/exploser)\" ne met pas à jour le nombre d\'objets lorsque le nombre de pièces change. Ils créent tous deux la fonction paramétrique Slice, qui place les morceaux scindés dans un composé, mais \"Slice apart\" fait exploser le composé résultant en objets séparés.

La forme de sortie occupe le même espace que l\'original. Mais elle est divisée là où elle croise d\'autres formes. Les pièces divisées sont des pièces individuelles.

Veuillez visiter la page [Part Scinder](Part_Slice/fr.md) pour plus d\'informations.

### Arborescence de Séparer/exploser 

La commande Séparer/exploser crée plus que l\'objet tranché. Dans l\'exemple suivant, un cube est découpé en tranches par une face.

Le tranchage est créé et pour chaque partie de celui-ci, un [Part Filtre composé](Part_CompoundFilter/fr.md) est créé. Ainsi, la même tranche se produit plusieurs fois sous chaque CompoundFilter (Filtre composé). Tous ces CompoundFilters sont réunis dans un Compound (Composé).

![](images/Part_SliceApartTree.png )

## Exemple

-   Faire un puzzle : Voir [Part Scinder](Part_Slice/fr.md) exemple étapes 1 à 6

## Script

L\'outil peut être utilisé dans une [macros](macros/fr.md) et à partir de la console python en utilisant la fonction suivante :

`BOPTools.SplitFeatures.makeSlice(name)`

Réglez le mode sur **Split** pour séparer/exploser

-   Crée une fonction Slice vide. Les propriétés \"Base\" et \"Outils\" doivent être attribuées explicitement, par la suite.
-   Renvoie l\'objet nouvellement créé.

Séparer/exploser peut également être appliqué à des formes simples, sans avoir besoin d\'un objet document via : 
```pythonBOPTools.SplitAPI.slice(base_shape, tool_shapes, mode, tolerance = 0.0)``` Cela peut être utile pour créer des fonctionnalités de script personnalisées Python.

Exemple : {{code|code=
import BOPTools.SplitFeatures
j = BOPTools.SplitFeatures.makeSlice(name= 'Slice')
j.Base = FreeCADGui.Selection.getSelection()[0]
j.Tools = FreeCADGui.Selection.getSelection()[1:]
}}

L\'outil lui-même est implémenté en Python, voir {{FileName|/Mod/Part/BOPTools/SplitFeatures.py}} ([lien GitHub](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/BOPTools/SplitFeatures.py)) là où FreeCAD est installé.

## Remarques

Séparer/exploser a été introduit dans FreeCAD v0.18.15506. FreeCAD doit être compilé avec OCC 6.9.0 ou une version ultérieure sinon, l\'outil n\'est pas disponible.

## Tutoriels vidéo 

-   <https://www.youtube.com/watch?v=tzHkQaHgrfQ> : FreeCad 0.18 PART WB using SLICE and SLICE APART (en anglais), auteur: Ha Gei

-   <https://www.youtube.com/watch?v=JJAL5JmqqKQ> : FreeCAD Slice und Slice Apart und andere Tricks (en allemand), auteur: Ha Gei



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part SliceApart/fr
