---
- GuiCommand:
   Name: FEM SolverCalculixCxxtools
   Name/fr: FEM Solveur CalculiX standard
   MenuLocation: Résolution -> Solveur CalculiX standard
   Workbenches: FEM_Workbench/fr
   Shortcut: **S** **X**
   SeeAlso: FEM_tutorial/fr
---

# FEM SolverCalculixCxxtools/fr

## Description

[Solveur CalculiX standard](FEM_SolverCalculixCxxtools/fr.md) permet d\'utiliser le solveur [CalculiX](https://fr.wikipedia.org/wiki/Calculix). Vous pouvez l\'utiliser pour :

1.  définir les paramètres d\'analyse
2.  sélectionner le répertoire de travail
3.  lancer le solveur CalculiX



## Utilisation

1.  Un <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:16px;"> Solveur CalculiX standard est créé automatiquement lors de la création d\'un <img alt="" src=images/FEM_Analysis.svg  style="width:16px;"> [Conteneur d\'analyse](FEM_Analysis/fr.md).
    Pour le créer manuellement, utilisez l\'une des alternatives suivantes :
    -   Sélectionnez **Résolution → <img src="images/FEM_SolverCalculixCxxtools.svg" width=16px> Solveur standard CalculiX** dans le menu.
    -   Appuyez sur les touches de raccourci **S** puis **X**.
2.  Vous pouvez modifier les propriétés de <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:16px;"> CalculiXcxxTools dans l\'[Éditeur de propriétés](Property_editor/fr.md).
3.  Double-cliquez sur l\'<img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:16px;"> objet solveur CalculiXcxxTools.
4.  Sélectionnez **Type d'analyse**.
5.  Cliquez sur le bouton **Écrire un fichier .inp**.
6.  Cliquez sur le bouton **Lancer CalculiX**.

## Options

Cliquez sur le bouton **Editer le fichier .inp** pour afficher et éditer manuellement le fichier d\'entrée de CalculiX avant d\'exécuter l\'analyse. Dans ce cas, il peut être utile de définir la propriété **Split Input Writer** à {{True}}.



## Propriétés

Les valeurs par défaut peuvent être définies dans le menu **Édition → Préférences → FEM → CalculiX**.

-    **Analysis Type**:

    -   static
    -   frequency
    -   thermomech - pour les charges mécaniques et thermiques
    -   check - pour vérifier uniquement le maillage
    -   buckling - pour les analyses de flambage {{Version/fr|0.20}}

-    **Beam Shell Result Output 3D**: notez que CalculiX développe en interne les éléments 1D et 2D en éléments 3D pour réaliser l\'analyse FE.

    -   false - les résultats des éléments 1D et 2D seront moyennés aux noeuds du maillage 1D ou 2D d\'origine (c\'est-à-dire qu\'un faisceau entièrement plié affichera 0 contrainte nodale due à la mise en moyenne)
    -   true - le maillage résultant contiendra des éléments 1D et 2D développés en éléments 3D

-    **Eigenmode High Limit**: les valeurs propres supérieures à cette limite ne seront pas calculées. **Remarque** : si les valeurs propres du modèle sont supérieures à la limite haute, CalculiX se terminera sans sortie.

-    **Eigenmode Low Limit**: les valeurs propres inférieures à cette limite ne seront pas calculées

-    **Eigenmodes Count**: nombre de modes propres les plus bas à calculer

-    **Geometric Nonlinearity**:

    -   linear - une analyse linéaire sera effectuée si le modèle ne contient pas de matériau non linéaire
    -   nonlinear - une analyse non linéaire sera effectuée

-    **Iterations Control parameter Cutb**: définit la deuxième ligne des [Paramètres d\'itération avancés de CalculiX](http://www.dhondt.de/ccx_2.17.pdf#subsection.8.24). Utilisé si **Iterations Control Parameter Time Use** est réglé à *true*.

-    **Iterations Control Parameter Iter**: définit la première ligne des [Paramètres d\'itération avancés de CalculiX](http://www.dhondt.de/ccx_2.17.pdf#subsection.8.24). Utilisé si **Iterations Control Parameter Time Use** est réglé à *true*.

-    **Iterations Control Parameter Time Use**-   true - active les options **Iterations Control parameter Cutb** et **Iterations Control Parameter Iter**
    -   false

-    **Iterations Thermo Mech Maximum**: nombre maximum d\'incréments dans l\'analyse thermomécanique après quoi le travail sera arrêté.

-    **Iterations User Defined Incrementations**:

    -   true - le contrôle d\'incrémentation automatique sera désactivé par le paramètre DIRECT
    -   false - le contrôle de l\'incrémentation sera automatique

-    **Iterations User Defined Time Step Length**:

    -   true - active les paramètres **Time End** et **Time Initial Step**
    -   false

-    **Material Nonlinearity**:

    -   linear - seules les propriétés des matériaux linéaires seront incluses dans l\'analyse
    -   nonlinear - les propriétés des matériaux non linéaires seront utilisées à partir de l\'oblet **<img src="images/FEM_MaterialMechanicalNonlinear.svg" width=24px> [FEM Matériau mécanique non linéaire](FEM_MaterialMechanicalNonlinear/fr.md)
**

-    **Matrix Solver Type**: type de solveur pour résoudre le système d\'équations dans l\'analyse FE. Il peut affecter de manière significative la vitesse de calcul et les besoins en mémoire. L\'adéquation dépend de votre modèle FE et du matériel disponible.

    -   default - sélectionne automatiquement le solveur matriciel en fonction des solveurs disponibles (il s\'agira probablement de Spooles)
    -   spooles - solveur direct avec prise en charge de plusieurs processeurs. Le nombre de processeurs doit être défini dans les [préférences](FEM_Preferences/fr#CalculiX.md) à la rubrique *Défauts du solveur → Nombre de processeurs à utiliser*.
    -   iterativescaling - solveur itératif avec des demandes de mémoire minimales, approprié si le modèle contient principalement des éléments 3D
    -   iterativecholesky - solveur itératif avec préconditionnement et faible demande de mémoire, adapté si le modèle contient principalement des éléments 3D

-    **Split Input Writer**:

    -   false - écrit toute l\'entrée dans un fichier \* .inp à utiliser par le solveur CalculiX
    -   true - divise les entrées du solveur en plusieurs fichiers \* .inp, ce qui permet de clarifier l\'édition manuelle

-    **Thermo Mechanical Steady State**:

    -   true - analyse thermomécanique à l\'état d\'équilibre
    -   false - analyse thermomécanique transitoire

-    **Time End**: période de temps de l\'étape, utilisée lorsque le paramètre **Iterations User Defined Incrementations** ou **Iterations User Defined Time Step Length** est à *true*

-    **Time Initial Step**: incrément de temps initial de l\'étape, utilisé lorsque le paramètre **Iterations User Defined Incrementations** ou **Iterations User Defined Time Step Length** est à *true*.

-    **Working Dir**: chemin du répertoire de travail qui sera utilisé pour les fichiers d'analyse CalculiX.

## Limitations

Lorsque vous exécutez un CalculiX, vous pouvez rencontrer l**\'erreur 4294977295**. Cela signifie que vous n\'avez pas assez de RAM. Vous avez alors 2 options :

1.  réduire le nombre de nœuds du maillage, de préférence en omettant la géométrie qui n\'est pas absolument nécessaire à votre analyse.
2.  acheter plus de RAM pour votre PC



## Remarques

La documentation originale de CalculiX se trouve à l\'adresse <http://dhondt.de/> dans le paragraphe \"ccx\".



## Script





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverCalculixCxxtools/fr
