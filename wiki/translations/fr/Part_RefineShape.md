---
- GuiCommand:
   Name: Part RefineShape
   Name/fr: Part Affiner la forme
   MenuLocation: Part -> Créer une copie -> Affiner la forme
   Workbenches: Part_Workbench/fr
   SeeAlso: Part_SimpleCopy/fr, Part_TransformedCopy/fr, Part_ElementCopy/fr, OpenSCAD_RefineShapeFeature/fr
---

# Part RefineShape/fr

## Description

L\'outil **<img src="images/Part_RefineShape.svg" width=16px> [Part Affiner la forme](Part_RefineShape/fr.md)** produit une copie non paramétrique à la forme raffinée, c'est-à-dire que certains bords et certaines faces ont été nettoyés.

Après certaines opérations booléennes, comme [Part Union](Part_Fuse/fr.md), certaines lignes des formes précédentes peuvent rester visibles. Cet outil produit une copie de ce résultat booléen et nettoie ces coutures.

**Autre façon**, pour produire d'autres copies non paramétriques, utilisez **<img src="images/Part_SimpleCopy.svg" width=16px> [Part Copie simple](Part_SimpleCopy/fr.md)
**, **<img src="images/Part_TransformedCopy.svg" width=16px>[Part Copie transformée](Part_TransformedCopy.md)** et **<img src="images/Part_ElementCopy.svg" width=16px> [Part Copie d'un élément](Part_ElementCopy.md)**

![](images/PartRefineShape_it.png ) 
*Résultat booléen initial avec 11 faces (à gauche) et copie de la forme raffinée avec 7 faces (à droite).*



## Utilisation

1.  Sélectionnez un objet que vous souhaitez nettoyer et copier.
2.  Cliquez sur le menu **Part → Créer une copie → <img src="images/Part_RefineShape.svg" width=16px> Affiner la forme**.
3.  Une copie nettoyée et indépendante de l\'objet original est créée. L\'objet original est rendu invisible.

Depuis la {{VersionPlus/fr|0.19}}, le résultat est par défaut une copie paramétrique (liée).

Ce comportement peut être modifié dans l\'<img alt="" src=images/Std_DlgParameter.svg  style="width:24px;"> [Editeur des paramètres](Std_DlgParameter/fr.md)

1.  Accédez au sous-groupe: `BaseApp/Preferences/Mod/Part`
2.  Remplacez `ParametricRefine` de type `Boolean` par `False` pour obtenir l\'ancien comportement (copie indépendante).

Voir les autres paramètres dans [Réglage fin](Fine-tuning/fr.md).



## Remarques

-   Cette fonction peut être utilisée comme dernière étape du travail de modélisation pour nettoyer les formes dans un flux de travail traditionnel de [géométrie solide constructive](constructive_solid_geometry/fr.md).
-   Cette fonction peut aider à nettoyer le modèle avant d\'appliquer une autre caractéristique, comme un [Congé](Part_Fillet/fr.md).
-   Ce nettoyage peut empêcher les imprimantes 3D d\'imprimer des bords indésirables une fois que le modèle solide est exporté vers un format de maillage.
-   Cette fonction peut également être utilisée après la conversion d\'un maillage en une forme ([Part Forme à partir du maillage](Part_ShapeFromMesh/fr.md)) pour nettoyer les bords résiduels sur les faces planes.
-   Des informations intéressantes sur ce qui se passe avec le placement et sur la manière d\'y accéder en Python peuvent être trouvées sur ce [fil du forum](https://forum.freecad.org/viewtopic.php?t=77568#p675456).

## Limitations

-   L\'algorithme de raffinement ne fonctionne que sur des coques (shells). Il itére donc sur les coques de la forme d\'entrée et crée ensuite pour chaque coque une nouvelle coque avec des faces jointes lorsque cela est possible. Cela signifie que si votre forme d\'entrée n\'est qu\'une face, un fil, un bord ou un sommet, l\'algorithme ne fait rien.
-   Par opposition à la commande <img alt="" src=images/OpenSCAD_RefineShapeFeature.svg  style="width:24px;"> [OpenSCAD Affinage de la forme](OpenSCAD_RefineShapeFeature/fr.md), <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> [Part Affiner la forme](Part_RefineShape/fr.md) ne sera pas mise à jour lorsque les formes précédentes seront modifiées.



## Script

La commande Python pour affiner une forme est la suivante:


```python
shape.removeSplitter()
```



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part RefineShape/fr
