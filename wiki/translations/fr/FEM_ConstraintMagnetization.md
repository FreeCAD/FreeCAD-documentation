---
- GuiCommand:/fr
   Name:FEM ConstraintMagnetization
   Name/fr:FEM Contrainte de magnétisation
   MenuLocation:Modèle → Contraintes électromagnétiques → Contrainte de magnétisation
   Workbenches:[FEM](FEM_Workbench/fr.md)
   Version:0.21
   SeeAlso:[FEM Équation magnétodynamique](FEM_EquationMagnetodynamic/fr.md), [FEM Équation magnétodynamique 2D](FEM_EquationMagnetodynamic2D/fr.md)
---

# FEM ConstraintMagnetization/fr

## Description

Crée une contrainte FEM pour la de magnétisation. A utiliser avec les équations [magnétodynamique](FEM_EquationMagnetodynamic/fr.md), [magnétodynamique 2D](FEM_EquationMagnetodynamic2D/fr.md)



## Utilisation

1.  Appuyez sur le bouton **<img src="images/FEM_ConstraintMagnetization.svg" width=16px> [Contrainte de magnétisation](FEM_ConstraintMagnetization/fr.md)** ou utilisez le menu **Modèle → Contraintes électromagnétiques → <img src="images/FEM_ConstraintMagnetization.svg" width=16px> Contrainte de magnétisation**.
2.  Dans la [vue 3D](3D_view/fr.md), sélectionnez l\'objet auquel la contrainte doit être appliquée.
3.  Appuyez sur le bouton **Ajouter**.

## Options

-   **Magnetization\_\*\_1** : partie réelle/imaginaire de la magnétisation dans la direction des x en A/m.Pour les systèmes de coordonnées autres que cartésien 3D, ce sera la première coordonnée du système au lieu de x.
-   **Magnetization\_\*\_2** : partie réelle/imaginaire de la magnétisation dans la direction des y en A/m.Pour les systèmes de coordonnées autres que cartésien 3D, ce sera la deuxième coordonnée du système au lieu de y.
-   **Magnetization\_\*\_3** : partie réelle/imaginaire de la magnétisation dans la direction des z en A/m.Pour les systèmes de coordonnées autres que cartésien 3D, ce sera la troisième coordonnée du système au lieu de z. Si le système de coordonnées n\'a pas de troisième coordonnée, ce paramètre sera ignoré.
-   **Magnetization\_\*\_\*\_Disabled** : indique si le paramètre correspondant est désactivé (supposé inconnu par le solveur).





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintMagnetization/fr
