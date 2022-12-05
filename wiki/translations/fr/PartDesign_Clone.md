---
- GuiCommand:/fr
   Name:PartDesign Clone
   Name/fr:PartDesign Clone
   MenuLocation:Part Design → Créer un clone
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   Version:0.17
   SeeAlso:[Draft Clone](Draft_Clone/fr.md)
---

# PartDesign Clone/fr

## Description

**PartDesign Clone** crée une copie liée d\'un objet sélectionné, qui suivra toutes les modifications ultérieures apportées à l\'objet d\'origine (sauf le placement). Par exemple, un cas d\'utilisation survient lorsque vous souhaitez effectuer une opération [PartDesign Booléenne](PartDesign_Boolean/fr.md) sur un objet créé dans un autre atelier. La plupart des types d\'objets sont acceptés, à condition qu\'il s\'agisse de solides simples. Si vous avez besoin de cloner plusieurs objets (corps) ou un [Part](Std_Part/fr.md), vous pouvez utiliser l\'outil [Draft Clone](Draft_Clone/fr.md). Un inconvénient est que le clone de l\'atelier Part Design définit l\'emplacement en cours du clone à zéro (translation cartésienne et orientation spatiale). Tandis que le clone de l\'ateliers Draft calcule et définit les valeurs numériques du placement et de l\'orientation en cours des objets clonés par rapport au conteneur de l\'objet cloné.

![*Clone of the inner gear while being translated in 3D space as an independent object*](images/clone.png ) 
*Clone de l'engrenage interne tout en étant traduit dans l'espace 3D en tant qu'objet indépendant*

## Utilisation

1.  Dans l\'arborescence du modèle, sélectionnez l\'objet à cloner.
2.  Appuyez sur le bouton **[<img src=images/PartDesign_Clone.svg style="width:24px"> '''Créer un clone'''**.

## Propriétés

-    **Base Feature**: Définit l\'objet d\'origine sur lequel le clone est basé. Pour le remplacer, appuyez sur le bouton **...** pour obtenir la liste des objets disponibles.

-    **Placement**: Définit l\'orientation et la position du Clone dans l\'espace 3D. Voir [Placement](Placement/fr.md).

-    **Label**: Etiquette donnée à l\'objet Clone. Changez en fonction de vos besoins.

## Limitations

-   Un seul objet peut être utilisé pour un clone PartDesign.
-   Seuls les objets qui consistent en un solide unique sont pris en charge. Donc, les [composés (Compound)](Glossary/fr#Compound.md) comme le [Part Conteneur](Std_Part/fr.md), le [Part Composé](Part_Compound/fr.md) ou le [Draft Réseau orthogonal](Draft_OrthoArray/fr.md) ne sont pas pris en charge.





{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Clone/fr
