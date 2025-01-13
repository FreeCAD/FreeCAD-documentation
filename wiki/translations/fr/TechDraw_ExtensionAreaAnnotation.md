---
 GuiCommand:
   Name: TechDraw ExtensionAreaAnnotation
   Name/fr: TechDraw Surface
   MenuLocation: TechDraw , Extensions : attributs/modifications , Calculer la surface des faces sélectionnées
   Workbenches: TechDraw_Workbench/fr
   Shortcut: 
   Version: 0.20
   SeeAlso: TechDraw_AreaDimension/fr
---

# TechDraw ExtensionAreaAnnotation/fr

## Description

L\'outil **TechDraw Surface** calcule la surface des faces sélectionnées et insère une annotation de surface.

<img alt="" src=images/TechDraw_ExtensionAreaAnnotationExample.png  style="width:400px;"> 
*A droite, l'annotation de la zone insérée*



## Utilisation

1.  Sélectionner une ou plusieurs faces.
2.  Il existe plusieurs façons de lancer l\'outil :
    -   Appuyez sur le **<img src="images/TechDraw_ExtensionAreaAnnotation.svg" width=16px> [Calculer la surface des faces sélectionnées](TechDraw_ExtensionAreaAnnotation/fr.md)**.
    -   Sélectionnez l\'option **TechDraw → Extensions : attributs/modifications → <img src="images/TechDraw_ExtensionAreaAnnotation.svg" width=16px> Calculer la surface des faces sélectionnées** du menu.
3.  La surface totale des faces est calculée et une annotation de surface est insérée.

## Limitation


{{VersionMinus/fr|0.21}}

: l\'outil ne peut pas gérer les faces avec des bords incurvés.

-   Les trous (îlots) dans la face sélectionnée sont ignorés. Ce [fil du forum](https://forum.freecad.org/viewtopic.php?p=783325#p783325) montre une solution de contournement. Vous pouvez également utiliser [TechDraw Cote de surface](TechDraw_AreaDimension/fr.md) mais vous devez alors définir correctement la propriété **References 3D** de la cote créée.
-   La surface calculée n\'est pas liée dynamiquement à la face. Si la surface de la face change, le texte n\'est pas mis à jour.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExtensionAreaAnnotation/fr
