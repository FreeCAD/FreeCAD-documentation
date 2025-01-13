---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM ConstraintMagnetization
   Name/fr: FEM Magnétisation
   MenuLocation: Modèle , Conditions limites électromagnétiques , Condition limite de magnétisation
   Workbenches: FEM_Workbench/fr
   Version: 0.21
   SeeAlso: FEM_EquationMagnetodynamic/fr, FEM_EquationMagnetodynamic2D/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: Elmer
}}
---

# FEM ConstraintMagnetization/fr

## Description

Crée une condition limite FEM pour la de magnétisation. A utiliser avec les équations [magnétodynamiques](FEM_EquationMagnetodynamic/fr.md) et [magnétodynamiques 2D](FEM_EquationMagnetodynamic2D/fr.md)



## Utilisation

1.  Appuyez sur le bouton **<img src="images/FEM_ConstraintMagnetization.svg" width=16px> [Condition limite de magnétisation](FEM_ConstraintMagnetization/fr.md)** ou utiliser **Modèle → Conditions limites électromagnétiques → <img src="images/FEM_ConstraintMagnetization.svg" width=16px> Condition limite de magnétisation** du menu.
2.  Appuyez sur le bouton **Ajouter**.
3.  Dans la [vue 3D](3D_view/fr.md), sélectionnez l\'objet auquel la condition limite doit être appliquée.

## Options

-   **Magnetization\_\*\_1** : partie réelle/imaginaire de la magnétisation dans la direction des x en A/m.Pour les systèmes de coordonnées autres que cartésien 3D, ce sera la première coordonnée du système au lieu de x.
-   **Magnetization\_\*\_2** : partie réelle/imaginaire de la magnétisation dans la direction des y en A/m.Pour les systèmes de coordonnées autres que cartésien 3D, ce sera la deuxième coordonnée du système au lieu de y.
-   **Magnetization\_\*\_3** : partie réelle/imaginaire de la magnétisation dans la direction des z en A/m.Pour les systèmes de coordonnées autres que cartésien 3D, ce sera la troisième coordonnée du système au lieu de z. Si le système de coordonnées n\'a pas de troisième coordonnée, ce paramètre sera ignoré.
-   **Magnetization\_\*\_\*\_Disabled** : indique si le paramètre correspondant est désactivé (supposé inconnu par le solveur).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintMagnetization/fr
