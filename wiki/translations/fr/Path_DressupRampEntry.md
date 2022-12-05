---
- GuiCommand:/fr
   Name:Path DressupRampEntry
   Name/fr:Path Rampe d'entrée
   MenuLocation:Path → Trajectoires additionelles → Rampe d'entrée
   Workbenches:[Path](Path_Workbench/fr.md)
   SeeAlso:[Path Attaches](Path_DressupTag/fr.md), [Path Dégagement d'angles](Path_DressupDogbone/fr.md), [Path Lame rotative](Path_DressupDragKnife/fr.md)
---

# Path DressupRampEntry/fr

## Description

Cet outil ajoute au tracé existant une rampe d\'entrée à l\'usinage

## Utilisation

1.  Sélectionnez un objet contour ou profil [Path](Path_Workbench/fr.md)
2.  cliquez sur l\'élément de menu <img alt="" src=images/Path_DressupRampEntry.svg  style="width:16px;"> [Rampe d\'entrée](Path_DressupRampEntry/fr.md)

## Propriétés

-   **Ramp Feed Rate** peut être la vitesse d\'avance verticale ou horizontale actuelle ou une autre valeur personnalisée
-   **Angle** de la rampe par rapport à l\'axe vertical. Une valeur plus faible rend la rampe plus raide.
-   **Method** permet de sélectionner différents modes de rampe:
    -   RampMethod1 descend à l\'angle de la rampe et se déplace horizontalement vers le point cible
    -   RampMethod2 passe d\'abord à l\'horizontale puis à l\'angle de la rampe jusqu\'au point cible
    -   RampMethod3 passe en zigzag
    -   Helix descend en spirale
-   **Dressup Start Depth** est la distance au-dessus du niveau cible où la rampe commence
-   **UseStartDepth** indique que la rampe ne commence pas au-dessus du niveau des stocks. Si elle n\'est pas définie sur true, la première rampe peut être plus raide que prévue.

<img alt="" src=images/Ramp_method_1.png  style="width:" height="250px;"> <img alt="" src=images/Ramp_method_2.png  style="width:" height="250px;"> <img alt="" src=images/Ramp_method_3.png  style="width:" height="250px;"> 
*De gauche à droite : Méthode de rampe 1, 2 et 3*

<img alt="" src=images/Ramp_method_Helix.png  style="width:" height="250px;"> 
*Méthode de rampe Hélice*





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path DressupRampEntry/fr
