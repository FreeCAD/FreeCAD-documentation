---
- GuiCommand:/fr
   Name:PartDesign SubShapeBinder
   Name/fr:PartDesign Sous forme liée
   MenuLocation:Conception de pièces → Créer une forme liée du sous-objet(s)
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.19
   SeeAlso:[PartDesign Forme liée](PartDesign_ShapeBinder/fr.md), [PartDesign Clone](PartDesign_Clone.md)
---

# PartDesign SubShapeBinder/fr

## Description

[PartDesign Sous forme liée](PartDesign_SubShapeBinder/fr.md) importe un élément d\'un autre corps dans le [Corps](PartDesign_Body/fr.md) actif. Il peut prendre la [forme](Shape/fr.md) de, ou être \"lié\" à un ou plusieurs objets ou sous-éléments (bords ou faces) d\'un autre objet.

Ensuite, l\'objet liant résultant peut être déplacé ou être utilisé pour effectuer des opérations avancées comme **<img src="images/PartDesign_Boolean.svg" width=16px> [PartDesign Opérations booléennes](PartDesign_Boolean/fr.md)** ou **<img src="images/PartDesign_Pad.svg" width=16px> [PartDesign Protrusion](PartDesign_Pad/fr.md)**.

Il peut également se lier à des objets imbriqués dans des [Std Parts](Std_Part/fr.md) et il suivra le placement relatif de ces fonctions. Ceci est utile dans le contexte de la création d\'[Assemblages](Assembly/fr.md) car souvent, l\'utilisateur doit référencer des [PartDesign Fonctionnalités](PartDesign_Feature/fr.md) qui sont déjà correctement placées dans un autre sous-assemblage.

<img alt="" src=images/PartDesign_SubShapeBinder_example_1.png  style="width:" height="300px;"> <img alt="" src=images/PartDesign_SubShapeBinder_example_2.png  style="width:" height="300px;">



*A gauche: deux solides créés dans deux [Corps](PartDesign_Body/fr.md) distincts. À droite: deux Sous formes liées extraites du premier corps, importées dans le deuxième corps et déplacés vers une position différente.*

<img alt="" src=images/PartDesign_SubShapeBinder_example_3.png  style="width:" height="300px;"> 
*Les deux Sous formes liées sont utilisées pour créer une [soustraction booléenne](PartDesign_Boolean/fr.md) et une [protusion](PartDesign_Pad/fr.md) avec le deuxième corps.*

## Utilisation

1.  Commencez avec un **[<img src=images/PartDesign_Body.svg style="width:16px"> [corps](PartDesign_Body/fr.md)** déjà en place contenant une seule [fonction](PartDesign_Feature/fr.md), par exemple un **[<img src=images/PartDesign_AdditivePrism.svg style="width:16px">  [prisme](PartDesign_AdditivePrism/fr.md)**.
2.  Créez un second **[<img src=images/PartDesign_Body.svg style="width:16px"> [corps](PartDesign_Body/fr.md)** contenant une seule [fonction](PartDesign_Feature/fr.md), par exemple, un **[<img src=images/PartDesign_AdditiveBox.svg style="width:16px"> [cube additif](PartDesign_AdditiveBox/fr.md)**. Faites-en le [corps actif](PartDesign_Body/fr#Statut_actif.md).
3.  Sélectionnez le premier corps entièrement puis appuyez sur **[<img src=images/PartDesign_SubShapeBinder.svg style="width:16px"> [Créer une forme liée du sous-objet(s)](PartDesign_SubShapeBinder/fr.md)**.
4.  Modifiez les propriétés de cet objet liant, par exemple son placement.
5.  Utilisez-le avec une autre opération telle que **[<img src=images/PartDesign_Boolean.svg style="width:16px"> [Opération booléenne](PartDesign_Boolean/fr.md)**.

## Propriétés

[PartDesign Sous forme liée](PartDesign_SubShapeBinder/fr.md) est dérivée de [Part Feature](Part_Feature/fr.md) (classe `Part::Feature`). En plus des propriétés répertoriées dans [Part Feature](Part_Feature/fr.md), les propriétés suivantes sont disponibles dans l\'[Éditeur de propriétés](Property_editor/fr.md).

### Données


{{TitleProperty|Base}}

-    **Support|XLinkSubList|hidden**: support de la géométrie.

-    **Fuse|Bool**: si `True`, fusion les formes liées solides.

-    **Make Face|Bool**: si `True`, création d\'une face pour les polylignes liées.

-    **Claim Children|PropertyBool**: si `True`, donnera les objets liés en tant qu\'enfants dans la [vue en arborescence](Tree_view/fr.md).

-    **Relative|Bool**: si `True`, cela permettra d\'établir des liens relatifs entre les sous-objets.

-    **Bind Mode|Enumeration**: mode de liaison, {{value|Synchronized}}, {{Value|Frozen}}, {{Value|Detached}}.

-    **Partial Load|Bool**: si `True`, cela permettra le chargement partiel des objets.

-    **Context|XLink|hidden**: objet conteneur de cet objet liant.

-    **_Version|Integer|hidden**: version de ce type d\'objet.

-    **Shape|PartShape|hidden**: [Part TopoShape](Part_TopoShape/fr.md) de cet objet.


{{TitleProperty|Cache}}

-    **Body|Matrix|hidden**: matrice d\'unité de cet objet.

### Vue

Voir [Part Feature](Part_Feature/fr.md).

## Liens

-   [New Sublink Link Feature](https://forum.freecadweb.org/viewtopic.php?t=41450), explication d\'utilisation avec vidéo.





{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubShapeBinder/fr
