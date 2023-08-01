---
- GuiCommand:
   Name:Draft Drawing
   Name/fr:Draft Dessin
   Workbenches:[Drawing](Drawing_Workbench/fr.md), [Draft](Draft_Workbench/fr.md), [Arch](Arch_Workbench/fr.md)
   SeeAlso:[TechDraw Vue d'un objet Draft](TechDraw_DraftView/fr.md)
---

# Draft Drawing/fr

## Description

La commande <img alt="" src=images/Draft_Drawing.svg  style="width:24px;"> **Draft Dessin** insère des vues des objets sélectionnés dans une page de [dessin](Drawing_Workbench/fr.md).

Cette commande est similaire à la commande [Drawing Insérer une vue dans la page](Drawing_View.md) mais est optimisée pour les objets de [Draft](Draft_Workbench/fr.md). Contrairement à cette commande, elle peut gérer des objets spécifiques tels que des [Draft Dimensions](Draft_Dimension/fr.md) et des [Draft Textes](Draft_Text/fr.md), et elle peut faire le rendu des faces.

Cette commande est maintenant obsolète. Utilisez plutôt l\'[atelier TechDraw](TechDraw_Workbench/fr.md) et la commande [TechDraw Vue d\'un objet Draft](TechDraw_DraftView/fr.md).

<img alt="" src=images/Draft_drawing_example.jpg  style="width:640px;"> 
*A gauche, les objets Draft sélectionnés. A droite, les vues de dessin créées.*



## Utilisation

1.  Pour utiliser cette commande dans FreeCAD version 0.19 et suivantes, vous devez ajouter un bouton à une barre d\'outils personnalisée. Voir [Personnalisation de l\'interface](Interface_Customization/fr.md).
2.  Sélectionnez un ou plusieurs objets. Une vue séparée sera créée pour chaque objet.
3.  Ajoutez éventuellement une page de [Drawing](Drawing_Workbench/fr.md) à la sélection. Si vous ne le faites pas, la vue est insérée dans la première page du document. S\'il n\'y a pas de page dans le document, une nouvelle page est d\'abord créée.
4.  Appuyez sur le bouton **<img src="images/Draft_Drawing.svg" width=16px> [Draft Dessin](Draft_Drawing/fr.md)**.
5.  Il y a un bug dans la version 0.19 de la commande dans FreeCAD. La valeur initiale de la propriété **Direction** est {{Value|[0, 0, 0]}} ce qui n\'est pas autorisé. Pour les objets situés sur un plan parallèle au plan XY du système de coordonnées global, elle doit être modifiée en {{Value|[0, 0, 1]}}. Après avoir modifié cette propriété, il se peut que la page et la vue doivent être [recalculées](Std_Refresh/fr.md).



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Drawing/fr
