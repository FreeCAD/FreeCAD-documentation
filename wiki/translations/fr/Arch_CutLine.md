---
 GuiCommand:
   Name: Arch CutLine
   Name/fr: Arch Couper selon une ligne
   MenuLocation: Arch , Couper selon une ligne
   Workbenches: Arch_Workbench/fr
   Version: 0.19
   SeeAlso: Arch_CutPlane/fr
---

# Arch CutLine/fr

## Description

L\'outil **Arch Couper selon une ligne** coupe un objet solide Arch comme un [Arch Mur](Arch_Wall/fr.md) ou une [Arch Structure](Arch_Structure/fr.md) avec une arête droite. En se basant sur cette arête et sur la normale du [plan de travail](Draft_SelectPlane/fr.md), une face de coupe est générée.

<img alt="" src=images/Arch_CutLine_example_1.png  style="width:" height="300px;"> <img alt="" src=images/Arch_CutLine_example_2.png  style="width:" height="300px;">



*Un [Arch Mur](Arch_Wall/fr.md) coupé par une ligne.<br/>
À gauche : la boîte soustractive qui apparaît lors de l'utilisation de l'outil.<br/>
À droite : le mur résultant après la coupe.*



## Utilisation

1.  Si nécessaire, aligner le plan de travail :
    -   L\'arête sélectionnée peut ne pas être parallèle à la normale du plan de travail.
    -   La face de coupe générée sera perpendiculaire au plan de travail.
2.  Sélectionner l\'objet à découper dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md).
3.  Sélectionner une ligne droite. Celle-ci doit être sélectionnée dans la [vue 3D](3D_view/fr.md).
4.  Appuyer sur le **<img src="images/Arch_CutLine.svg" width=16px> [Couper selon une ligne](Arch_CutLine/fr.md)**.
5.  Choisir **Derrière** ou **Devant** pour indiquer de quel côté de la face de coupe la matière doit être enlevée.
6.  Appuyer sur le bouton **OK**.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch CutLine/fr
