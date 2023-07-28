# <img alt="Icône de l\'atelier FEM FrontISTR" src=images/FrontISTR.svg  style="width:64px;"> FEM FrontISTR Workbench/fr


{{TOCright}}

## Introduction

L\'atelier <img alt="" src=images/FrontISTR.svg  style="width:24px;"> FEM FrontISTR est une extension de FreeCAD qui permet d\'utiliser FrontISTR, un programme FEM parallèle à grande échelle open source pour l\'analyse structurelle non linéaire.

<img alt="" src=images/FEM_FrontISTR_bikeframe_screenshot.png  style="width:512px;">



### Déroulement des tâches 

1.  Configurer un modèle d\'analyse par l\'atelier FEM (de la même manière que calculiX).
2.  Passer à l\'atelier **FrontISTR** et créer un objet solveur FrontISTR en cliquant sur le bouton de la barre d\'outils <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;">.
3.  Double-cliquez sur l\'objet solveur dans l\'arbre du document et définissez le répertoire de travail.
4.  Cliquez sur le bouton **Write input file**.
5.  Cliquez sur le bouton **Exécuter FrontISTR**.
6.  Vérifier les résultats FISTR_Results pour le post-traitement.



## Fonctions

-   Analyse statique, vérification des éléments
-   Analyse géométrique linéaire et non linéaire
-   Eléments : tétraèdre du 1er/2ème ordre
-   Charges : mécaniques concentrées et réparties, gravité
-   Frontières : points fixes ou déplacement
-   Contrôle des étapes : incrémentation et réduction automatiques du temps.
-   Solveur d\'équations linéaires
    -   itératif
        -   préconditionneur : AMG, SSOR, Diagonal, ILU(k)(k=0,1,2)
        -   méthode : CG, BiCGSTAB, GMRES, GPBiCG
    -   direct : MUMPS
-   Format du fichier de sortie : AVS, VTK (paraview requis)



### Fonctions prévues à l\'avenir 

-   Analyse : transfert thermique, dynamique, propre, fréquence
-   Matériaux (mécanique) : élastoplastique, hyper élastique, fluage, visco élastique.
-   Contact
-   MPC(TIE)
-   Eléments : prisme, hexa, poutre, coque, treillis, etc.



### Limitations

-   FISTR_Results ne contient que les résultats pour les surfaces. Si vous avez besoin des résultats intérieurs, changez le format du fichier de sortie en VTK et visualisez les résultats avec paraview.
-   Le banc d\'essai FEM FrontISTR ne supporte pas encore les analyses thermiques. FISTR lui-même peut effectuer des analyses thermiques et le support pour ceci est prévu dans un futur proche.
-   Les analyses mécaniques pour différents matériaux dans un modèle ne sont pas encore possibles.



### Résultats de comparaison 

Voir <https://github.com/FrontISTR/FEM_FrontISTR/tree/master/sample/benchmarks>.

## Installation



### Gestionnaire des extensions 

FEM_FrontISTR peut facilement être installé via le <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md) à partir du menu **Outils → Gestionnaire des extensions**. FEM_FrontISTR est en cours de développement actif et reçoit de nouvelles fonctionnalités fréquemment. Vous devez donc le mettre à jour régulièrement en utilisant également le menu **Outils → Gestionnaire des extensions**. Le code de FEM_FrontISTR est hébergé et développé [sur GitHub](https://github.com/FrontISTR/FEM_FrontISTR).



### Manuellement

Voir [Comment installer des ateliers supplémentaires](How_to_install_additional_workbenches/fr.md)



### Prérequis

-   FreeCAD v0.19 ou plus récent
-   [Paraview](https://www.paraview.org/) (optionnel)



### Installation du solveur FrontISTR 

Les binaires de FrontISTR seront automatiquement téléchargés et installés lors de la première exécution. Si le téléchargement ne se fait pas, veuillez suivre les étapes ci-dessous pour installer le solveur.

#### Windows

1.  Télécharger [le dernier zip FrontISTR](https://www.frontistr.com/download/link.php?https://frontistr-commons.gitlab.io/FrontISTR/release/x86_64-w64-mingw32-msmpi/FrontISTR-latest.zip)
2.  Créer le répertoire FEM_FrontISTR/bin
3.  Extraire FrontISTR-latest.zip et mettre tous les fichiers dans le répertoire FEM_FrontISTR/bin.

#### Linux

En préparation.

#### Mac

En préparation.



## Outils

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> **Solver FrontISTR Standard** : crée un nouveau solveur FrontISTR pour cette analyse.



## Références

-   Auteur : kinagaki rigarashi
-   Code source : [Github.com](https://github.com/FrontISTR/FEM_FrontISTR)
-   Forum FreeCAD : [58019](https://forum.freecadweb.org/viewtopic.php?t=58019)
-   Tutoriels : <https://frontistr-commons.gitlab.io/FEM_FrontISTR/en/>
-   Documentation du solveur FrontISTR : <https://manual.frontistr.com/en/>
-   Rapporter les bogues : Veuillez signaler les bogues à [Github.com](https://github.com/FrontISTR/FEM_FrontISTR).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > FEM FrontISTR Workbench/fr
