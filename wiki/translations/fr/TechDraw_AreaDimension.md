---
 GuiCommand:
   Name: TechDraw AreaDimension
   Name/fr: TechDraw Cote de surface
   MenuLocation: TechDraw , Cotes , Insérer une cote de surface
   Workbenches: TechDraw_Workbench/fr
   Version: 0.19
   SeeAlso: TechDraw_ExtensionAreaAnnotation/fr
---

# TechDraw AreaDimension/fr



## Description

L\'outil **TechDraw Cote de surface** ajoute une cote de surface à une face dans une vue de pièce.

![](images/TechDraw_AreaDimension_Example.png ) 
*Cote de surface d'une face avec un trou. Voir [Limitations](#Limitations.md).*



## Utilisation

1.  Sélectionnez une face. La géométrie peut être sélectionnée dans la [vue 3D](3D_view/fr.md) ou dans le dessin.
2.  Si vous avez sélectionné la géométrie dans la vue 3D : ajoutez la bonne vue TechDraw à la sélection en la sélectionnant dans la [vue en arborescence](Tree_view/fr.md).
3.  Il y a plusieurs façons de lancer l\'outil :
    -   Si la [préférence](TechDraw_Preferences/fr#Cotes/fr.md) **Outils de cotation** est réglé sur {{Value|Outil unique}} (par défaut) : appuyez sur la flèche vers le bas à droite de l\'outil **<img src="images/TechDraw_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** et sélectionnez l\'option **<img src="images/TechDraw_AreaDimension.svg" width=16px> Insérer une cote de surface** dans le menu déroulant.
    -   Si cette préférence a une valeur différente : appuyez sur le bouton **<img src="images/TechDraw_AreaDimension.svg" width=16px>[Insérer une cote de surface](TechDraw_AreaDimension/fr.md)**.
    -   Sélectionnez l\'option **TechDraw → Cotes → <img src="images/TechDraw_AreaDimension.svg" width=16px> Insérer une annotation de zone** du menu.
4.  Une cote est ajoutée à la vue.
5.  La cote peut être déplacée jusqu\'à la position souhaitée.
6.  Si nécessaire, ajoutez des tolérances comme décrit sur [cette page](TechDraw_Geometric_dimensioning_and_tolerancing/fr#Tolérances.md).

## Limitations

-    {{VersionMinus/fr|1.0}}: l\'outil ne peut détecter que les trous (îlots) dans les faces sélectionnées dans la vue 3D. Pour obtenir la bonne surface pour une telle face sélectionnée dans le dessin, procédez comme suit :

    1.  Définissez la bonne propriété **References 3D** avec ![\|x16px](images/TechDraw_DimensionRepair.svg ) [TechDraw Réparation des cotes](TechDraw_DimensionRepair/fr.md).
    2.  Changez la propriété **Measure Type** en {{Value|True}}.
    3.  Appuyez sur ![\|x16px](images/Std_Refresh.svg ) [Std Recalculer](Std_Refresh/fr.md) si nécessaire.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw AreaDimension/fr
