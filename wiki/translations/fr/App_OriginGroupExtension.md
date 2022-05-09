# App OriginGroupExtension/fr
## Introduction

Un objet [App Origin](App_OriginGroupExtension/fr.md), ou formellement un `App   *   *OriginGroupExtension`, est une classe fournissant des éléments sélectionnables qui représentent les trois axes standard (X, Y, Z) et les trois plans standard (XY, XZ et YZ) aux objets destinés à disposer différents types de géométrie dans l\'espace.

Les objets <img alt="" src=images/Std_Part.svg  style="width   *16px;"> [Std Part](Std_Part/fr.md) [(App Part)](App_Part/fr.md) et les objets <img alt="" src=images/PartDesign_Body.svg  style="width   *16px;"> [PartDesign Corps](PartDesign_Body/fr.md) sont créés avec des objets Origin par défaut. Si nécessaire, des objets Origin peuvent être aussi ajoutés à des objets <img alt="" src=images/Assembly_Assembly_Tree.svg  style="width   *16px;"> [Assembly](Assembly3_CreateAssembly/fr.md) de l\'atelier <img alt="" src=images/Assembly3_workbench_icon.svg  style="width   *16px;"> [Assembly3](Assembly3_Workbench/fr.md).

<img alt="Tree view" src=images/App_OriginGroupExtension_example.png  style="width   *200px;"> <img alt="3D view" src=images/App_OriginGroupExtension-02.png  style="width   *400px;"> 
*A gauche    * La [Vue en arborescence](Tree_view/fr.md) montrant trois objets qui utilisent des objets Origin. A droite    * Représentation des éléments d'origine dans la [Vue 3D](3D_view/fr.md).*

Les axes et les plans sont des objets de type `App   *   *Line` et `App   *   *Plane` respectivement. Chacun de ces éléments peut être masqué et démasqué individuellement avec la barre **Espace**. Cela peut être utile pour sélectionner la référence correcte pour créer d\'autres objets, par exemple des [esquisses](Sketch/fr.md).

<img alt="" src=images/FreeCAD_core_objects.svg  style="width   *800px;">



*Diagramme simplifié des relations entre les objets principaux du programme. Deux d'entre eux ont un objet Origine pour contrôler le placement des objets regroupés sous eux.*


{{Document_objects_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > App OriginGroupExtension/fr
