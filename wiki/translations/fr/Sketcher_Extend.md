---
 GuiCommand:
   Name: Sketcher Extend
   Name/fr: Sketcher Prolonger
   MenuLocation: Esquisse , Outils d'esquisse , Prolonger l'arête
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **Q**
   Version: 0.17
   SeeAlso: Sketcher_Trimming/fr
---

# Sketcher Extend/fr

## Description

L\'outil <img alt="" src=images/Sketcher_Extend.svg  style="width:24px;"> [Sketcher Prolonger](Sketcher_Extend/fr.md) permet de prolonger ou de raccourcir une ligne ou un arc jusqu\'à un emplacement arbitraire, ou jusqu\'à une arête ou un point cible.

<img alt="" src=images/Sketcher_Extend_example_01.png  style="width:600px;"> 
*À gauche (1), les deux éléments de l'esquisse avant l'opération<br>Au milieu (2), la ligne est prolongée jusqu'à l'arc<br>À droite (3), le résultat final.*



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_Extend.svg" width=16px> [Prolonger l'arête](Sketcher_Extend/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Outils d'esquisse → <img src="images/Sketcher_Extend.svg" width=16px> Prolonger l'arête** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_Extend.svg" width=16px> Prolonger l'arête** dans le menu contextuel.
    -   Utilisez le raccourci clavier : **G** puis **Q**.
2.  S\'il y a une sélection précédente, elle est effacée. L\'outil n\'accepte pas de présélection.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  Sélectionnez une ligne ou un arc.
5.  Déplacez le curseur dans la direction à prolonger ou à raccourcir.
6.  Effectuez l\'une des opérations suivantes :
    -   Cliquez sur un point arbitraire.
    -   Pour étendre/raccourcir vers une autre arête (Les [contraintes automatiques](Sketcher_Workbench/fr#Contraintes_automatiques.md) doivent être activées) : placez le curseur sur l\'arête cible. Lorsqu\'il est mis en surbrillance et que l\'icône de la <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:16px;"> [contrainte Point sur objet](Sketcher_ConstrainPointOnObject/fr.md) apparaît à côté du curseur, cliquez pour confirmer. La contrainte est ajoutée.
    -   Pour étendre/raccourcir un point (les contraintes automatiques doivent être activées) : placez le curseur sur le point cible. Lorsqu\'il est mis en surbrillance et que l\'icône de la <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:16px;"> [contrainte de coïncidence](Sketcher_ConstrainCoincident/fr.md) apparaît à côté du curseur, cliquez pour confirmer. La contrainte est ajoutée.
7.  Si l\'outil fonctionne en [mode continu](Sketcher_Workbench/fr#Modes_continus.md) :
    1.  Vous pouvez continuer à allonger/raccourcir les arêtes.
    2.  Pour terminer, cliquez dans une zone vide de la [vue 3D](3D_view/fr.md), cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.



## Remarques

-   Si la contrainte n\'est pas totale, l\'arête ou le point cible peut également être modifié.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Extend/fr
