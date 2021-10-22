# PartDesign Feature/fr
## Introduction

[PartDesign Feature](PartDesign_Feature/fr.md) fait référence à une \"étape\" du processus de modélisation qui se produit à l\'intérieur d\'un [PartDesign Corps](PartDesign_Body/fr.md). Par exemple, chaque fois que vous ajoutez une boîte pleine avec [PartDesign Cube additif](PartDesign_AdditiveBox/fr.md), vous ajoutez une fonction. Lorsque vous ajoutez un chanfrein à une arête avec [PartDesign Chanfrein](PartDesign_Chamfer/fr.md), vous ajoutez une autre fonction. Lorsque vous découpez un trou à l\'aide d\'une [Esquisse](Sketch/fr.md) et [PartDesign Cavité](PartDesign_Pocket/fr.md), vous ajoutez une autre fonction.

<img alt="" src=images/PartDesign_Feature_example.png  style="width:600px;"> 
*Modification des fonctions dans un [PartDesign Corps](PartDesign_Body/fr.md) avec trois fonctions séquentielles.*

Il existe de nombreux types de fonctions qui peuvent ajouter ou supprimer du volume d\'un solide initial. Le mot «fonction» fait référence à l\'opération elle-même ainsi qu\'au solide résultant après cette opération.

Pour en savoir plus sur la création d\'objets solides avec l\'[Atelier PartDesign](PartDesign_Workbench/fr.md), voir [Édition de fonctions](feature_editing/fr.md).

## Utilisation

Presque tous les outils de l\'[Atelier PartDesign](PartDesign_Workbench/fr.md) sont destinés à ajouter des fonctions à un [PartDesign Corps](PartDesign_Body/fr.md). Ces outils sont accessibles à partir des boutons de menu et de barre d\'outils lorsqu\'un objet ou un sous-élément (sommet, arête, face) est sélectionné.

Les fonctionnalités peuvent être classées en différentes catégories:

-   Base d\'objet: fait référence à l\'objet d\'objet de base qui peut être créé dans un [PartDesign Corps](PartDesign_Body/fr.md).
-   Additif et soustractif
    -   Formes primitives: [Cube additif](PartDesign_AdditiveBox/fr.md), [Cône additif](PartDesign_AdditiveCone/fr.md), [Cylindre additif](PartDesign_AdditiveCylinder/fr.md), [Ellipsoïde additif](PartDesign_AdditiveEllipsoid/fr.md), [Prisme additif](PartDesign_AdditivePrism/fr.md), [Sphère additive](PartDesign_AdditiveSphere/fr.md), [Tore additif](PartDesign_AdditiveTorus/fr.md) et [Pyramide tronquée additive](PartDesign_AdditiveWedge/fr.md).
    -   Formes primitives soustractives: [Cube soustractif](PartDesign_SubtractiveBox/fr.md), [Cône soustractif](PartDesign_SubtractiveCone/fr.md), [Cylindre soustractif](PartDesign_SubtractiveCylinder/fr.md), [Ellipsoïde soustractif](PartDesign_SubtractiveEllipsoid/fr.md), [Prisme soustractif](PartDesign_SubtractivePrism/fr.md), [Sphère soustractive](PartDesign_SubtractiveSphere/fr.md), [Tore soustractif](PartDesign_SubtractiveTorus/fr.md) et [Pyramide tronquée soustractive](PartDesign_SubtractiveWedge/fr.md).
    -   Addition basée sur un profil: [Protrusion](PartDesign_Pad/fr.md), [Révolution](PartDesign_Revolution/fr.md), [Lissage additif](PartDesign_AdditiveLoft/fr.md), [Balayage additif](PartDesign_AdditivePipe/fr.md).
    -   Soustraction basée sur un profil : [Cavité](PartDesign_Pocket/fr.md), [Perçage](PartDesign_Hole/fr.md), [Rainure](PartDesign_Groove/fr.md), [Lissage soustractif](PartDesign_SubtractiveLoft/fr.md), [Balayage soustractif](PartDesign_SubtractivePipe/fr.md).
-   [Opérations booléennes](PartDesign_Boolean/fr.md) comprenant fusion, coupe et intersection.
-   Finition
    -   [Chanfrein](PartDesign_Chamfer/fr.md)
    -   [Dépouille](PartDesign_Draft/fr.md)
    -   [Congé](PartDesign_Fillet/fr.md)
    -   [Epaisseur](PartDesign_Thickness/fr.md)
-   Transformation
    -   [Répétition linéaire](PartDesign_LinearPattern/fr.md)
    -   [Symétrie](PartDesign_Mirrored/fr.md)
    -   [Transformation multiple](PartDesign_MultiTransform/fr.md)
    -   [Répétition circulaire](PartDesign_PolarPattern/fr.md)
    -   [Mise à l\'échelle](PartDesign_Scaled/fr.md)

## Héritage

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Diagramme simplifié des relations entre les objets centraux du programme. L'objet `PartDesign::Feature*  est destiné à construire des solides 3D paramétriques et est donc dérivé de l'objet de base {{incode|Part::Feature`.}}

## Script


**Voir aussi:**

[Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md) et [Objets créés par script](scripted_objects/fr.md).

Voir [Part Feature](Part_Feature/fr.md) pour les informations générales sur l\'ajout d\'objets à partir de la [console Python](Python_console/fr.md).

Voir [PartDesign Corps](PartDesign_Body.md) pour les informations générales sur l\'ajout d\'un corps. Une fois qu\'un corps existe, des fonctionnalités peuvent y être attachées à l\'aide de la méthode `addObject()` du corps.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject('PartDesign::Body', 'Body')
obj.Label = "Custom label"

feature = App.ActiveDocument.addObject('PartDesign::AdditiveBox', 'Box')
feature.Width = 200
feature.Length = 300
feature.Height = 500
obj.addObject(feature)
App.ActiveDocument.recompute()

feature2 = App.ActiveDocument.addObject('PartDesign::SubtractiveBox', 'Box')
feature2.Width = 50
feature2.Length = 200
feature2.Height = 400
obj.addObject(feature2)
App.ActiveDocument.recompute()
```


{{PartDesign Tools navi

}} {{Document objects navi}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Feature/fr
