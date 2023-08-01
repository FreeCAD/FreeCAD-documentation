---
- GuiCommand:/fr
   Name:Image CreateImagePlane
   Name/fr:Image Créer un plan d'image
   MenuLocation:
   Workbenches:[Image](Image_Workbench/fr.md)
   SeeAlso:[Image Ouvrir](Image_Open/fr.md), [Image Redimensionner une image](Image_Scaling/fr.md)
---

# Image CreateImagePlane/fr

## Description

L\'outil [Créer un plan d\'image](Image_CreateImagePlane/fr.md) importe une image [bitmap](bitmap/fr.md) et la place sur l\'un des plans XY, YZ ou XZ.



## Utilisation

1.  Appuyez sur le bouton **<img src="images/Image_CreateImagePlane.svg" width=16px> [Créer un plan d'image...](Image_CreateImagePlane/fr.md)**.
2.  Sélectionnez l\'image souhaitée dans votre système.
3.  Choisissez le plan dans lequel l\'image sera placée, indiquez une valeur de décalage puis appuyez sur **OK**.

L\'objet ImagePlane résultant utilise le rapport de 1 pixel pour 1 millimètre. Pour que l'image s'affiche bien, elle doit avoir une résolution suffisante.

Lors de l\'importation de l\'image, vous pouvez ajouter un décalage de `-0,1 mm` afin de placer l\'image légèrement derrière le plan de travail. Cela facilitera le traçage de l\'image avec les outils de l\'[atelier Draft](Draft_Workbench/fr.md) ou de l\'[atelier Sketcher](Sketcher_Workbench/fr.md).

Si aucun décalage n\'est initialement attribué à l\'image, sa position peut toujours être ajustée dans l\'[Éditeur de propriétés](Property_editor/fr.md).



## Propriétés


{{Properties_Title|Base}}

-    **Position**: spécifie les coordonnées du point de base du plan image.

-    **Angle**: spécifie l\'angle de rotation du plan image.

-    **Axis**: spécifie l\'axe utilisé pour l\'angle de rotation.


{{Properties Title|Image Plane}}

-    **Image File**: spécifie l\'image à utiliser pour ce plan.

-    **XSize**: spécifie la largeur du plan de l\'image.

-    **YSize**: spécifie la hauteur du plan de l\'image.





{{Image Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Image](Image_Workbench.md) > Image CreateImagePlane/fr
