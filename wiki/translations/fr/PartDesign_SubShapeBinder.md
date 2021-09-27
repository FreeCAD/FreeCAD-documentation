---
- GuiCommand:/fr
   Name:PartDesign SubShapeBinder
   Name/fr:PartDesign Sous forme liée
   MenuLocation:Part Design → Create a sub-object shape binder
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   Version:0.19
   SeeAlso:[PartDesign Forme liée](PartDesign_ShapeBinder/fr.md), [PartDesign Clone](PartDesign_Clone.md)
---

# PartDesign SubShapeBinder/fr

## Description

[PartDesign Sous forme liée](PartDesign_SubShapeBinder/fr.md) importe un élément d\'un autre corps dans le [Corps](PartDesign_Body/fr.md) actif. Il peut prendre la [Shape](Shape/fr.md) de, ou être \"lié\" à un ou plusieurs objets ou sous-éléments (bords ou faces) d\'un autre objet.

Ensuite, l\'objet liant résultant peut être déplacé ou être utilisé pour effectuer des opérations avancées comme [PartDesign Opérations booléennes](PartDesign_Boolean/fr.md) ou [PartDesign Protrusion](PartDesign_Pad/fr.md).

Il peut également se lier à des objets imbriqués dans des [Std Parts](Std_Part/fr.md) et il suivra le placement relatif de ces fonctions. Ceci est utile dans le contexte de la création d\'[Assemblages](Assembly/fr.md) car souvent, l\'utilisateur doit référencer des [PartDesign Fonctionnalités](PartDesign_Feature/fr.md) qui sont déjà correctement placées dans un autre sous-assemblage.

<img alt="" src=images/PartDesign_SubShapeBinder_example_1.png  style="width:" height="300px;"> <img alt="" src=images/PartDesign_SubShapeBinder_example_2.png  style="width:" height="300px;">


*A gauche: deux solides créés dans deux [Corps](PartDesign_Body/fr.md) distincts. À droite: deux Sous formes liées extraites du premier corps, importées dans le deuxième corps et déplacés vers une position différente.*

<img alt="" src=images/PartDesign_SubShapeBinder_example_3.png  style="width:" height="300px;"> 
*Les deux Sous formes liées sont utilisées pour créer une [soustraction booléenne](PartDesign_Boolean/fr.md) et une [protusion](PartDesign_Pad/fr.md) avec le deuxième corps.*

## Utilisation

1.  Commencez avec un **<img src=images/PartDesign_Body.svg style="width:16px"> <img src=images/PartDesign_AdditivePrism.svg style="width:Corps](PartDesign_Body/fr.md)** déjà en place contenant une seule [fonctionnalité](PartDesign_Feature/fr.md), par exemple un **[16px">  [Prisme](PartDesign_AdditivePrism/fr.md)**.
2.  Créez un second **<img src=images/PartDesign_Body.svg style="width:16px"> <img src=images/PartDesign_AdditiveBox.svg style="width:Corps](PartDesign_Body/fr.md)** contenant une seule [fonctionnalité](PartDesign_Feature/fr.md), par exemple, un **[16px"> [Cube additif](PartDesign_AdditiveBox/fr.md)**. Ce sera le corps actif.
3.  Sélectionnez le premier corps entièrement puis appuyez sur **<img src=images/PartDesign_SubShapeBinder.svg style="width:16px"> [SubShapeBinder](PartDesign_SubShapeBinder/fr.md)**.
4.  Modifiez les propriétés de cet objet liant, par exemple son placement.
5.  Utilisez-le avec une autre opération telle que **<img src=images/PartDesign_Boolean.svg style="width:16px"> [Opération booléenne](PartDesign_Boolean/fr.md)**.

## Propriétés

_, les propriétés suivantes sont disponibles dans l\'[Éditeur de propriétés](Property_editor/fr.md).

### Données


{{TitleProperty/fr|Base}}

-    {{PropertyData/fr|Support|XLinkSubList|hidden}}: support de la géométrie.

-    {{PropertyData/fr|Fuse|Bool}}: si c\'est `True`, il fusionnera les formes liées solides.

-    {{PropertyData/fr|Make Face|Bool}}: si c\'est `True`, il créera une face pour les fils liés.

-    {{PropertyData/fr|Claim Children|PropertyBool}}: s\'il s\'agit de `True`, il réclamera les objets liés en tant qu\'enfants dans la [vue en arborescence](Tree_view/fr.md).

-    {{PropertyData/fr|Relative|Bool}}: s\'il s\'agit de `True`, il activera la liaison de sous-objet relative.

-    {{PropertyData/fr|Bind Mode|Enumeration}}: mode de liaison, {{value|Synchronized}}, {{Value|Frozen}}, {{Value|Detached}}.

-    {{PropertyData/fr|Partial Load|Bool}}: si c\'est `True`, cela permettra le chargement partiel des objets.

-    {{PropertyData/fr|Context|XLink|hidden}}: objet conteneur de cet objet liant.

-    {{PropertyData/fr|_Version|Integer|hidden}}: version de ce type d\'objet.

-    {{PropertyData/fr|Shape|PartShape|hidden}}: [Part TopoShape](Part_TopoShape/fr.md) de cet objet.


{{TitleProperty/fr|Cache}}

-    {{PropertyData/fr|Body|Matrix|hidden}}: matrice d\'unité de cet objet.

### Vue

Voir [Part Fonctionnalité](Part_Feature/fr.md).

## Liens

-   [New Sublink Link Feature](https://forum.freecadweb.org/viewtopic.php?t=41450), explication d\'utilisation avec vidéo.





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubShapeBinder/fr
