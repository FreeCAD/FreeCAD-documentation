---
- GuiCommand:
   Name: Arch CutLine
   Name/fr: Arch Couper selon une ligne
   MenuLocation: Arch -> Couper selon une ligne
   Workbenches: Arch_Workbench/fr
   Version: 0.19
   SeeAlso: Arch_CutPlane/fr
---

# Arch CutLine/fr

## Description

L\'outil [Arch Couper selon une ligne](Arch_CutLine/fr.md) vous permet de couper un objet solide Arch comme un [Arch Mur](Arch_Wall/fr.md) ou [Arch Structure](Arch_Structure/fr.md) à l\'aide d\'une ligne qui traverse l\'objet.

<img alt="" src=images/Arch_CutLine_example_1.png  style="width:" height="300px;"> <img alt="" src=images/Arch_CutLine_example_2.png  style="width:" height="300px;">



*Un [Arch Mur](Arch_Wall/fr.md) coupé par une ligne. À gauche : boîte soustractive qui apparaît lors de l'utilisation de l'outil. À droite : le mur résultant après la coupe.*



## Utilisation

1.  Sélectionnez l\'objet à couper dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md).
2.  Puis sélectionnez la ligne à utiliser pour couper l\'objet, par exemple, un [Draft Polyligne](Draft_Wire/fr.md). Cet objet doit être sélectionné dans la [vue 3D](3D_view/fr.md) uniquement.
3.  Appuyez sur le bouton **<img src="images/Arch_CutLine.svg" width=16px> [Couper selon une ligne](Arch_CutLine/fr.md)**.
4.  Choisissez **Derrière** ou **Devant** pour indiquer quelle partie du solide sera supprimée.
5.  Cliquez sur le bouton **OK**.



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch CutLine/fr
