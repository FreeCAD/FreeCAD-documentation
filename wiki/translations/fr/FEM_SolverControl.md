---
- GuiCommand:
   Name:FEM SolverControl
   Name/fr:FEM Réglage du solveur
   MenuLocation:Résolution - Contrôle des tâches du solveur
   Workbenches:[FEM](FEM_Workbench/fr.md)
   Shortcut:**S** **T**
   SeeAlso:[FEM Résolution](FEM_SolverRun/fr.md)
---

# FEM SolverControl/fr

## Description

Cette commande est utilisée pour contrôler le solveur FEM (écrire le fichier d\'entrée, l\'éditer et lancer le solveur).



## Utilisation

1.  Sélectionnez l\'objet Solver dans la [vue en arborescence](Tree_view/fr.md), par exemple, pour le <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> **Solveur standard Calculix**.
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_SolverControl.svg" width=16px> [Contrôle des tâches du solveur](FEM_SolverControl/fr.md)**.
    -   Sélectionnez l\'option **Résolution → <img src="images/FEM_SolverControl.svg" width=16px> Contrôle des tâches du solveur** dans le menu.
    -   Utilisez le raccourci clavier : **S** puis **T**.
3.  Vous pouvez modifier le répertoire de travail.
4.  Vous pouvez sélectionner le type d\'analyse.
5.  Cliquez sur **Écrire le fichier .inp** pour écrire le fichier d\'entrée.
6.  Vous pouvez cliquer sur **Editer le fichier .inp**.
    -   Le fichier d\'entrée s\'ouvre pour que vous puissiez le modifier et l\'enregistrer par **Ctrl**+**S**.
7.  Cliquez sur **Lancer CalculiX** pour lancer le solveur.
    -   La solution peut prendre un temps considérable pour les grands modèles.



## Remarques

-   Le répertoire de travail par défaut peut être modifié dans **Édition → Préférences → FEM**.
-   Les commandes pour d\'autres solveurs peuvent différer.
-   La version simplifiée de la commande est <img alt="" src=images/FEM_SolverRun.svg  style="width:24px;"> [Lancer les calculs du solveur](FEM_SolverRun/fr.md).





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverControl/fr
