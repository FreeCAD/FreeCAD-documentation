---
- GuiCommand:
   Name: Sketcher Extend
   Name/fr: Sketcher Prolonger
   MenuLocation: Esquisse - Géométries d'esquisse - Prolonger l'arête
   Workbenches: [Sketcher](Sketcher_Workbench/fr.md)
   Shortcut: **G** **Q**
   Version: 0.17
   SeeAlso: [Sketcher Ajuster](Sketcher_Trimming/fr.md)
---

# Sketcher Extend/fr

## Description

L\'outil **Prolonger** étend une arête vers une position arbitraire dans l\'esquisse, ou à une arête cible ou un objet Point.

<img alt="" src=images/Sketcher_Extend_example_01.png  style="width:600px;"> 
*Sur la gauche (1), les deux éléments d’esquisse avant l’opération ; au milieu (2), la ligne est prolongée jusqu'à l'arc ; à droite (3), le résultat final.*



## Utilisation

1.  Appuyez sur le bouton **[<img src=images/Sketcher_Extend.svg style="width:16px"> [Prolonger l'arête](Sketcher_Extend/fr.md)**.
2.  Sélectionnez une ligne ou un arc.
3.  Dans la vue 3D, déplacez le pointeur de la souris dans la direction du prolongement.
4.  Cliquez sur un emplacement quelconque dans l\'espace ou
5.  Pour prolonger sur une autre arête, placez le pointeur de la souris sur l\'arête cible; lorsqu\'elle est mise en surbrillance et que l\'icône **[<img src=images/Sketcher_ConstrainPointOnObject.svg style="width:16px"> [Sketcher Contrainte point sur objet](Sketcher_ConstrainPointOnObject/fr.md)** apparaît à côté du pointeur de la souris, cliquez pour confirmer. Une contrainte point sur objet sera ajoutée.
6.  Pour prolonger vers un point de l\'esquisse, placez le pointeur de la souris sur le point cible; lorsqu\'il est mis en surbrillance et que l\'icône **[<img src=images/Sketcher_ConstrainCoincident.svg style="width:16px"> [Sketcher Contrainte de coïncidence](Sketcher_ConstrainCoincident/fr.md)** apparaît à côté du pointeur de la souris, cliquez pour confirmer. Une contrainte de coïncidence sera ajoutée.



## Remarques

-   Seuls les arcs et les lignes peuvent être étendus pour le moment.
-   L\'objet cible (arête ou point) peut également être modifié s\'il n\'est pas entièrement contraint.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Extend/fr
