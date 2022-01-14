# PartDesign Scaled/fr
{{GuiCommand/fr
|Name=PartDesign_Scaled
|Name/fr=PartDesign Mise à l'échelle
|Workbenches=[PartDesign](PartDesign_Workbench/fr.md), Complet
|MenuLocation=Part Design → Créer une transformation multiple
}}

## Introduction

\'Scale features\' - Cet outil prend un ensemble d\'une ou plusieurs entités sélectionnées comme entrée (les \'originaux\') et les met à l\'échelle selon un facteur donné. Étant donné que la mise à l\'échelle se fait autour du centre de gravité des entités sélectionnées, elles disparaissent généralement à l\'intérieur des versions mises à l\'échelle. Par conséquent, il n\'est normalement utile d\'utiliser la mise à l\'échelle que dans le cadre de la fonction MultiTransform.

## Note

Depuis FreeCAD 0.15, cette fonctionnalité n'est pas disponible directement, mais est incluse en tant que [MultiTransform](PartDesign_MultiTransform/fr.md) composant

## Options

+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <img alt="" src=images/Scaled_parameters.png  style="width:240px;"> | Lorsque vous utilisez la fonction **[16px|text-top=Echelle|link=PartDesign_Scaled/fr](File:PartDesign_Scaled.png.md) [Echelle](PartDesign_Scaled/fr.md)**, la boîte de dialogue des paramètres d\'**[16px|text-top=Echelle|link=PartDesign_Scaled/fr](File:PartDesign_Scaled.png.md) [Echelle](PartDesign_Scaled/fr.md)**, offre les options suivantes : |
|                                                                 |                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                 | ### Selection des originaux                                                                                                                                                                                                                                                                                                                                |
|                                                                 |                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                 | La fenêtre affiche les **originaux**, des objets qui doivent être mis à l\'**[16px|text-top=Echelle|link=PartDesign_Scaled/fr](File:PartDesign_Scaled.png.md) [Echelle](PartDesign_Scaled/fr.md)**. En cliquant sur un objet, il sera ajouté à la liste.                                                                                                               |
|                                                                 |                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                 | ### Facteur et Occurrences                                                                                                                                                                                                                                                                                                                                  |
|                                                                 |                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                 | Spécifie le nombre et le facteur maximal à donner aux objets, qui vont être mis à l\'**[16px|text-top=Echelle|link=PartDesign_Scaled/fr](File:PartDesign_Scaled.png.md) [Echelle](PartDesign_Scaled/fr.md)**, (y compris la sélection originale).                                                                                                                      |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+




## Limitations

-   L\'**[16px|text-top=Echelle|link=PartDesign_Scaled/fr](File:PartDesign_Scaled.png.md) [Echelle](PartDesign_Scaled/fr.md)** a toujours comme centre de gravité, le point de base.
-   Une transformation mise à l\'échelle ne doit pas être la première de la liste
-   La transformation mise à l\'échelle doit avoir le même nombre d\'occurrences que la transformation la précédant immédiatement dans la liste.
-   Allez sur **![](images/)_[_Répétition_Linéaire_de_Modéle](_PartDesign_LinearPattern/fr.md)**, pour voir les autres limitations.

-   Voir [MultiTransform](PartDesign_MultiTransform.md) pour plus de détails

## Exemples

![c\|center\|800px](images/mt_example2.png ) Le plus petit pad a d\'abord été configuré trois fois dans la direction X, puis redimensionné en deux (les trois occurrences ont donc les facteurs d\'échelle 1.0, 1.5 et 2.0). Ensuite, un motif polaire a été appliqué avec 8 occurrences.

Étant donné que la mise à l\'échelle est effectuée par rapport au centre de gravité, dans le cas d\'un pad, il est nécessaire que le pad pénètre également dans le corps principal, sinon les objets à mettre à l\'échelle flotteront, se détachent du corps. Pour avoir un pad qui coupe le corps principal, vous pouvez utiliser le type \"deux dimensions\" ou l\'option \"simmetric to plane\".

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Scaled/fr
