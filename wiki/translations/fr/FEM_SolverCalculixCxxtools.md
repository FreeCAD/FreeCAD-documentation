---
 GuiCommand:
   Name: FEM SolverCalculixCxxtools
   Name/fr: FEM Solveur CalculiX standard
   MenuLocation: Résolution , Solveur CalculiX standard
   Workbenches: FEM_Workbench/fr
   Shortcut: **S** **X**
   SeeAlso: FEM_tutorial/fr
---

# FEM SolverCalculixCxxtools/fr

## Description

Le [Solveur CalculiX standard](FEM_SolverCalculixCxxtools/fr.md) permet d\'utiliser le solveur [CalculiX](https://fr.wikipedia.org/wiki/Calculix). Vous pouvez l\'utiliser pour :

1.  définir les paramètres d\'analyse
2.  sélectionner le répertoire de travail
3.  lancer le solveur CalculiX



## Utilisation

1.  Un <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:16px;"> Solveur CalculiX standard est créé automatiquement lors de la création d\'un <img alt="" src=images/FEM_Analysis.svg  style="width:16px;"> [Conteneur d\'analyse](FEM_Analysis/fr.md).
    Pour le créer manuellement, utilisez l\'une des alternatives suivantes :
    -   Appuyer sur le bouton **<img src="images/FEM_SolverCalculixCxxtools.svg" width=16px> [Solveur standard CalculiX](FEM_SolverCalculixCxxtools/fr.md)**.
    -   Sélectionner **Résolution → <img src="images/FEM_SolverCalculixCxxtools.svg" width=16px> Solveur standard CalculiX** du menu.
    -   Appuyer sur les touches de raccourci **S** puis **X**.
2.  Vous pouvez modifier les propriétés de <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:16px;"> CalculiXcxxTools dans l\'[éditeur de propriétés](Property_editor/fr.md).
3.  Double-cliquer sur l\'<img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:16px;"> objet solveur CalculiXcxxTools.
4.  Sélectionner **Type d'analyse**.
5.  Cliquer sur le bouton **Écrire un fichier .inp**.
6.  Cliquer sur le bouton **Lancer CalculiX**.

## Options

Cliquer sur le bouton **Editer le fichier .inp** pour afficher et éditer manuellement le fichier d\'entrée de CalculiX avant d\'exécuter l\'analyse. Dans ce cas, il peut être utile de définir la propriété **Split Input Writer** à {{True}}.



## Propriétés

Les valeurs par défaut peuvent être définies dans le menu **Édition → Préférences → FEM → CalculiX**.

-    **Analysis Type**:

    -   static : analyse des contraintes statiques.
    -   frequency : analyse modale (fréquence naturelle).
    -   thermomech : analyse thermomécanique.
    -   check : pas de calcul, vérifie les données d\'entrée.
    -   buckling : analyse de flambage linéaire {{Version/fr|0.20}}.

-    **Beam Reduced Integration**{{Version/fr|1.0}} :

    -   true : utilise des éléments de type poutre avec intégration réduite (B31R ou B32R), requis lorsqu\'une section de type poutre tubulaire est utilisée, peut également permettre d\'obtenir [des résultats précis avec la plasticité](https://forum.freecad.org/viewtopic.php?t=61233).
    -   false : utilise des éléments réguliers de type poutre (entièrement intégrés).

-    **Beam Shell Result Output 3D**: notez que CalculiX développe en interne les éléments 1D et 2D en éléments 3D pour réaliser l\'analyse d\'éléments finis.

    -   true : le maillage résultant contiendra des éléments 1D et 2D développés en éléments 3D.
    -   false : les résultats des éléments 1D et 2D seront moyennés aux noeuds du maillage 1D ou 2D d\'origine (c\'est-à-dire qu\'un modèle de type poutre entièrement plié affichera 0 de contrainte nodale due à la mise en moyenne).

-    **Buckling Accuracy**: définit la précision de l\'évaluation des valeurs propres de flambement. Dans la plupart des cas, la valeur par défaut (0.01) peut être laissée, mais il peut parfois être nécessaire de l\'abaisser (par exemple à 0.0001) pour capturer la première valeur propre. {{Version/fr|1.1}}

-    **Eigenmode High Limit**: les valeurs propres supérieures à cette limite ne seront pas calculées. **Remarque** : si les valeurs propres du modèle sont supérieures à la limite haute, CalculiX se terminera sans valeur de sortie.

-    **Eigenmode Low Limit**: les valeurs propres inférieures à cette limite ne seront pas calculées.

-    **Eigenmodes Count**: nombre de modes propres les plus bas à calculer.

-    **Geometric Nonlinearity**:

    -   linear : une analyse linéaire sera effectuée si le modèle ne contient pas de matériau non linéaire.
    -   nonlinear : une analyse non linéaire sera effectuée.

-    **Iterations Control parameter Cutb**: définit la deuxième ligne des [Paramètres d\'itération avancés de CalculiX](http://www.dhondt.de/ccx_2.17.pdf#subsection.8.24). Utilisé si **Iterations Control Parameter Time Use** est réglé à *true*.

-    **Iterations Control Parameter Iter**: définit la première ligne des [Paramètres d\'itération avancés de CalculiX](http://www.dhondt.de/ccx_2.17.pdf#subsection.8.24). Utilisé si **Iterations Control Parameter Time Use** est réglé à *true*.

-    **Iterations Control Parameter Time Use**-   true : active les options **Iterations Control parameter Cutb** et **Iterations Control Parameter Iter**.
    -   false

-    **Iterations Thermo Mech Maximum**: nombre maximum d\'incréments après lesquels le travail sera arrêté.

-    **Iterations User Defined Incrementations**:

    -   true : le contrôle d\'incrémentation automatique sera désactivé par le paramètre DIRECT.
    -   false : le contrôle de l\'incrémentation sera automatique.

-    **Iterations User Defined Time Step Length**:

    -   true : active les paramètres **Time End** et **Time Initial Step**.
    -   false

-    **Material Nonlinearity**:

    -   linear : seules les propriétés des matériaux linéaires seront incluses dans l\'analyse.
    -   nonlinear : les propriétés des matériaux non linéaires seront utilisées à partir de l\'objet **<img src="images/FEM_MaterialMechanicalNonlinear.svg" width=24px> [FEM Matériau mécanique non linéaire](FEM_MaterialMechanicalNonlinear/fr.md)
**

-    **Matrix Solver Type**: type de solveur pour résoudre le système d\'équations dans l\'analyse d\'éléments finis. Il peut affecter de manière significative la vitesse de calcul et les besoins en mémoire. L\'adéquation dépend de votre modèle d\'éléments finis et du matériel disponible.

    -   default : sélectionne automatiquement le solveur de matrice en fonction des solveurs disponibles (typiquement Spooles).
    -   pastix : l\'un des solveurs les plus rapides (avec Pardiso), disponible (et par défaut) dans les versions officielles depuis ccx 2.18. Il peut encore causer des problèmes occasionnels. {{Version/fr|1.0}}
    -   pardiso : l\'un des solveurs les plus rapides (avec PaStiX) mais non open-source. Il nécessite une version différente de CalculiX (ccx_dynamic) et des bibliothèques supplémentaires non fournies avec FreeCAD. Il est plus fiable que PaStiX. {{Version/fr|1.0}}
    -   spooles : solveur direct avec le support de plusieurs CPUs. Le nombre de CPU doit être défini dans les [préférences](FEM_Preferences/fr#CalculiX.md) à *Défauts du solveur → Nombre de processeurs à utiliser*.
    -   iterativescaling : solveur itératif avec la plus faible demande de mémoire, approprié si le modèle contient principalement des éléments 3D.
    -   iterativecholesky : solveur itératif avec préconditionnement et faible demande de mémoire, adapté si le modèle contient principalement des éléments 3D.

-    **Model Space**: permet de passer d\'une analyse 3D à une analyse 2D, ces dernières nécessitent une géométrie de surface sur le plan XY (à droite de l\'axe Y dans le cas axisymétrique) avec une [définition de l\'épaisseur](FEM_ElementGeometry2D/fr.md) (valeur ignorée dans le cas axisymétrique) et des conditions limites appropriées ([condition limite de déplacement](FEM_ConstraintDisplacement/fr.md) avec degrés de liberté X et Y doit être utilisé au lieu de [condition limite fixe](FEM_ConstraintFixed/fr.md)) et des charges dans le plan appliquées aux arêtes. {{Version/fr|1.0}}

    -   3D : des éléments solides/coques/éléments de titre poutre sont utilisés.
    -   Contraintes planes : des éléments solides 2D de contraintes planes sont utilisés.
    -   Déformation plane : des éléments solides 2D de déformation plane sont utilisés.
    -   Axisymétrique : des éléments solides 2D axisymétriques sont utilisés.

-    **Output Frequency**: définit la fréquence d\'écriture des résultats par incréments (le réglage par défaut de 1 signifie que les résultats sont écrits à chaque incrément, le réglage 2 sauvegarde les résultats tous les 2 incréments et ainsi de suite), particulièrement utile pour les simulations non linéaires et transitoires, aide à réduire l\'encombrement dans l\'arborescence puisque actuellement une paire d\'objets de résultats (CCX_Results et Pipeline_CCX_Results) est créée pour chaque trame de résultats. {{Version/fr|1.0}}

-    **Split Input Writer**:

    -   false : écrit toute l\'entrée dans un fichier \* .inp à utiliser par le solveur CalculiX.
    -   true : divise les entrées du solveur en plusieurs fichiers \* .inp, ce qui permet de clarifier l\'édition manuelle.

-    **Thermo Mech Steady State**:

    -   true : analyse thermomécanique à l\'état d\'équilibre.
    -   false : analyse thermomécanique transitoire.

-    **Thermo Mech Type**{{Version/fr|1.0}} :

    -   couplé : analyse thermomécanique couplée
    -   découplée : analyse thermomécanique découplée
    -   transfert de chaleur pur : analyse purement thermique (*\*HEAT TRANSFER*)

-    **Time End**: période de temps de l\'étape, utilisée lorsque le paramètre **Iterations User Defined Incrementations** ou **Iterations User Defined Time Step Length** est à *true*.

-    **Time Initial Step**: incrément de temps initial de l\'étape, utilisé lorsque le paramètre **Iterations User Defined Incrementations** ou **Iterations User Defined Time Step Length** est à *true*.

-    **Time Maximum Step**: incrément de temps maximum de l\'étape, utilisé lorsque le paramètre **Iterations User Defined Incrementations** ou **Iterations User Defined Time Step Length** est *vrai*. {{Version/fr|1.0}}

-    **Time Minimum Step**: incrément de temps minimum de l\'étape, utilisé lorsque le paramètre **Iterations User Defined Incrementations** ou **Iterations User Defined Time Step Length** est *vrai*. {{Version/fr|1.0}}

-    **Working Dir**: chemin d\'accès du répertoire de travail qui sera utilisé pour les fichiers d'analyse CalculiX.

## Limitations

Lorsque vous exécutez un CalculiX, vous pouvez rencontrer l**\'erreur 4294977295**. Cela signifie que vous n\'avez pas assez de RAM. Vous avez alors 2 options :

1.  réduire le nombre de nœuds du maillage, de préférence en omettant la géométrie qui n\'est pas absolument nécessaire à votre analyse.
2.  acheter plus de RAM pour votre PC.



## Remarques

La documentation originale de CalculiX se trouve à l\'adresse <http://dhondt.de/> dans le paragraphe \"ccx\".



## Script





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverCalculixCxxtools/fr
