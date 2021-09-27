# Datum/fr
## Introduction

Dans FreeCAD, le mot \"[Datum](Datum/fr.md)\" est normalement utilisé pour faire référence à la géométrie auxiliaire dans l\'[Atelier PartDesign](PartDesign_Workbench/fr.md). Ces éléments géométriques ne feront pas partie de la [Shape](Shape/fr.md) (forme) finale du [Body](Body/fr.md) (corps) mais peuvent être utilisés comme références et supports pour les [Esquisses](Sketch/fr.md) et d\'autres types de [features](Feature/fr.md) (fonctions).

Les éléments suivants correspondent aux éléments dérivés de la classe `Part::Datum`, elle-même dérivée de [Part Feature](Part_Feature/fr.md):

-   [PartDesign Point](PartDesign_Point/fr.md)
-   [PartDesign Ligne](PartDesign_Line/fr.md)
-   [PartDesign Plan](PartDesign_Plane/fr.md)
-   [PartDesign Système de coordonnées](PartDesign_CoordinateSystem/fr.md)

Les éléments suivants sont dérivés directement de [Part Feature](Part_Feature/fr.md):

-   [PartDesign Forme liée](PartDesign_ShapeBinder.md)
-   [PartDesign Sous forme liée](PartDesign_SubShapeBinder.md)

## Utilisation

1.  Basculez vers l\'[atelier PartDesign](PartDesign_Workbench/fr.md).
2.  Appuyez sur **<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Corps](PartDesign_Body/fr.md)**.
3.  Sélectionnez l\'origine du corps et rendez-la visible en appuyant sur la barre **Espace** de votre clavier.
4.  Appuyez sur **<img src=images/PartDesign_Plane.svg style="width:16px"> [PartDesign Plan](PartDesign_Plane/fr.md)** pour ouvrir le plan [Panneau des tâches](Task_Panel/fr.md).
5.  Dans la [vue 3D](3D_view/fr.md), cliquez sur l\'un des plans standards, par exemple le plan XY. Appuyez ensuite sur **OK** pour fermer le panneau des tâches.
6.  Maintenant, dans la <img src=images/PartDesign_NewSketch.svg style="width:vue en arborescence](tree_view/fr.md), sélectionnez le nouveau plan de référence, puis appuyez sur **[16px"> [PartDesign Nouvelle esquisse](PartDesign_NewSketch/fr.md)**.
7.  Créez un fil fermé, puis utilisez **<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Protrusion](PartDesign_Pad/fr.md)** pour extruder l\'esquisse et créer un solide initial.

Vous pouvez maintenant déplacer et faire pivoter le plan de référence comme vous le souhaitez en modifiant ses propriétés dans [Éditeur de propriétés](Property_editor/fr.md). L\'esquisse et la protrusion suivront le nouveau [Placement](Placement/fr.md).

Vous pouvez ajouter d\'autres types de références à utiliser avec d\'autres esquisses et fonctions.

## Remarques

Depuis leur apparition dans la v0.17, les objets de référence étaient destinés à être utilisés dans [PartDesign Corps](PartDesign_Body/fr.md). Cependant, comme ce sont des objets de \"référence\" utiles avec différentes méthodes d\'[Ancrage](Part_EditAttachment/fr.md), il a été proposé qu\'ils soient disponibles en dehors de l\'[atelier PartDesign](PartDesign_Workbench/fr.md). De cette façon, ils seront utilisables dans tous les établis comme support de géométrie, notamment dans le cadre de la création d\'[assemblages](Assembly/fr.md).

-   [Create and display local coordinate system](https://forum.freecadweb.org/viewtopic.php?f=10&t=2604)
-   [Datum objects in App::Part](https://forum.freecadweb.org/viewtopic.php?f=22&t=33654)
-   [Structure toolbar and datums](https://forum.freecadweb.org/viewtopic.php?t=42759)
-   [Local CS cannot be used in Part Wb?](https://forum.freecadweb.org/viewtopic.php?f=3&t=42960)


{{PartDesign Tools navi

}} {{Document objects navi}} 

_

---
[documentation index](../README.md) > [Glossary](Category_Glossary.md) > Datum/fr
