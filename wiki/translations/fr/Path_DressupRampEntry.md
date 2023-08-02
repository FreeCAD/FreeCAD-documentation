---
- GuiCommand:
   Name: Path DressupRampEntry
   Name/fr: Path Rampe d'entrée
   MenuLocation: Path -> Finition du parcours -> Rampe d'entrée
   Workbenches: Path_Workbench/fr
   SeeAlso: Path_DressupTag/fr, Path_DressupDogbone/fr, Path_DressupDragKnife/fr
---

# Path DressupRampEntry/fr

## Description

L\'outil <img alt="" src=images/Path_DressupRampEntry.svg  style="width:24px;"> [Rampe d\'entrée](Path_DressupRampEntry/fr.md) ajoute une rampe d\'entrée au parcours existant.



## Utilisation

1.  Sélectionner un objet contour ou profil
2.  Sélectionnez l\'option **Path → Finition du parcours → <img src="images/Path_DressupRampEntry.svg" width=16px> Rampe d'entrée** du menu.



## Propriétés

-   **Vitesse d\'avance dans la rampe** : peut être la vitesse d\'avance verticale ou horizontale en cours ou une autre valeur personnalisée
-   **Angle** : angle de la rampe par rapport à l\'axe vertical. Une valeur plus faible rend la rampe plus raide.
-   **Méthode** : permet de sélectionner différents modes de rampe:
    -   *Méthode rampe 1* : descend à l\'angle de la rampe et se déplace horizontalement vers le point cible
    -   *Méthode rampe 2* : passe d\'abord à l\'horizontale puis à l\'angle de la rampe jusqu\'au point cible
    -   *Méthode rampe 3* : passe en zigzag
    -   *Hélice* : descend en spirale
-   **Profondeur de départ cible** : distance au-dessus du niveau cible où la rampe commence.
-   **Profondeur de départ de la rampe** : indique que la rampe ne commence pas au-dessus du niveau du brut. Si elle n\'est pas définie à true, la première rampe peut être plus raide que prévue.

<img alt="" src=images/Ramp_method_1.png  style="width:" height="250px;"> <img alt="" src=images/Ramp_method_2.png  style="width:" height="250px;"> <img alt="" src=images/Ramp_method_3.png  style="width:" height="250px;"> 
*De gauche à droite : méthode de rampe 1, 2 et 3*

<img alt="" src=images/Ramp_method_Helix.png  style="width:" height="250px;"> 
*Méthode de rampe Hélice*





{{Path_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Path](Path_Workbench.md) > Path DressupRampEntry/fr
