---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM ConstraintCentrif
   Name/fr: FEM Charge centrifuge
   MenuLocation: Modèle , Conditions limites et charges mécaniques , Charge centrifuge
   Workbenches: FEM_Workbench/fr
   Shortcut: 
   Version: 0.20
   SeeAlso: 
}}
{{GuiCommandFemInfo
   Solvers: CalculiX
}}
---

# FEM ConstraintCentrif/fr

## Description

Définit une charge centrifuge sur le corps.



## Utilisation

1.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintCentrif.svg" width=16px> [Charge centrifuge](FEM_ConstraintCentrif/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Conditions limites et charges mécaniques → <img src="images/FEM_ConstraintCentrif.svg" width=16px> Charge centrifuge** dans le menu.
2.  Spécifiez la fréquence de rotation en Hz.
3.  Cliquez sur **Ajouter** dans la fenêtre **Sélecteur de référence géométrique pour un solide** et sélectionnez un solide auquel la charge sera appliquée dans la [vue 3D](3D_view/fr.md).
4.  Cliquez sur **Ajouter** dans la fenêtre **Sélecteur de référence géométrique pour une arête** et sélectionnez une arête autour de laquelle la rotation se produira dans la [vue 3D](3D_view/fr.md).



## Remarques

-   Cette fonction utilise le [jeu de paramètres \*DLOAD de CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node190.html).





{{FEM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintCentrif/fr
