---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM ConstraintPressure
   Name/fr: FEM Charge de pression
   MenuLocation: Modèle , Conditions limites et charges mécaniques , Charge de pression
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_ConstraintForce/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: CalculiX, Elmer
}}
---

# FEM ConstraintPressure/fr

## Description

Applique une charge de pression à une face.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyer sur le bouton **<img src="images/FEM_ConstraintPressure.svg" width=16px> [Charge de pression](FEM_ConstraintPressure/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Conditions limites et charges mécaniques → <img src="images/FEM_ConstraintPressure.svg" width=16px> Charge de pression** du menu.
2.  Appuyez sur le bouton **Ajouter** et sélectionnez la/les face(s) dans la [vue 3D](3D_view/fr.md). Vous pouvez appuyer sur le bouton **Supprimer** et cliquez sur les faces que vous souhaitez supprimer de la sélection.
3.  Modifiez la fenêtre appropriée pour spécifier la charge de pression en MPa.
4.  Cochez la case pour inverser la direction si nécessaire.



## Remarques

-   La répartition de la pression sur une face est toujours uniforme et toujours perpendiculaire à la face.

-    {{VersionMinus/fr|0.21}}: la charge de pression peut être appliquée aux coques, mais seulement lorsque [Gmsh](FEM_MeshGmshFromShape/fr.md) est utilisé pour le maillage et que le maillage de groupe est réglé à true. Ce paramètre est codé en dur à true, de sorte que l\'utilisateur n\'a pas à s\'en préoccuper. Cependant, en raison d\'un bogue, la charge de pression peut nécessiter un remaillage pour fonctionner sur des coques.

-   Cette fonction utilise le [jeu de paramètres \*DLOAD de CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node190.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintPressure/fr
