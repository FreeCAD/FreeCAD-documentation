---
- GuiCommand:
   Name: PartDesign_WizardShaft
   Name/fr: PartDesign Conception d'arbre
   MenuLocation: Part Design - Conception d'arbre...
   Workbenches: [PartDesign](PartDesign_Workbench/fr.md)
---

# PartDesign WizardShaft/fr

## Description

Cet outil vous permet de créer un arbre à partir d\'un tableau de valeurs et d\'analyser les forces et les moments.



## Utilisation

Vous pouvez démarrer l\'assistant par la commande **Part Design → [<img src=images/PartDesign_WizardShaft.svg style="width:20px"> Conception d'arbre...**.

L\'assistant démarre et affiche un tableau par défaut, la partie de l\'arbre correspondante et les graphiques des forces/moments.

<img alt="" src=images/WizardShaft_Part.jpg  style="width:780px;">

La partie supérieure de la fenêtre est occupée par le tableau. Elle est organisée en colonnes numérotées qui correspondent aux segments de l\'arbre. Un segment d\'arbre est caractérisé par une certaine longueur et un certain diamètre. La fenêtre principale présente deux onglets. L\'un est la partie de l\'arbre elle-même (une fonction de révolution), voir l\'image ci-dessus. Le second onglet montre les graphiques des forces de cisaillement et des moments créés par les charges définies dans le tableau.

<img alt="" src=images/shaftwizard1.jpg  style="width:1024px;">



## Prérequis

L\'assistant de conception d\'arbre dépend de la bibliothèque [matplotlib](http://matplotlib.org/) pour créer et afficher des graphiques de force de cisaillement et de moment de flexion. Sur les systèmes basés sur Debian/Ubuntu, il est disponible via le paquet python-matplotlib.



## Paramètres

Pour chaque segment de l\'arbre, les paramètres suivants peuvent être définis,

-   La longueur du segment.
-   Le diamètre du segment.
-   Type de charge. Notez que vous devez cliquer sur l\'entrée désirée dans le menu après l\'avoir fait défiler sinon elle ne sera pas sélectionnée.
    -   None : aucune charge.
    -   Fixed : l\'arbre est fixé à une extrémité, (par exemple soudé à une autre pièce). Ce type de charge ne peut pas être défini pour le premier ou le dernier segment.
    -   Static : il y a une charge statique sur le segment de l\'arbre.
-   Charge sur le segment de l\'arbre.
-   L\'emplacement où la charge est appliquée sur le segment. L\'emplacement est comptabilisé à partir du bord gauche du segment.

(D\'autres lignes et types de charges existent mais aucune fonctionnalité n\'a encore été appliquée)

## Menus

Pour ajouter un nouveau segment d\'arbre, cliquez avec le bouton droit de la souris dans l\'espace vide à droite du tableau et choisissez \"Ajouter une colonne\".

## Limitations

-   Il n\'est pas possible d\'avoir des segments d\'arbre adjacents de même diamètre.



## Fonctionnalités prévues 

-   Chanfreins et arrondis sur les bords de l\'arbre, gérés par la table.
-   Reconnaissance d\'une partie de l\'assistant d\'arbre précédemment créée et initialisation des valeurs de la table à partir de celle-ci.
-   Calcul des contraintes sur l\'arbre.
-   Visualisation des charges sur l\'arbre (peut utiliser la même fonctionnalité que pour le module FEM).
-   Définition des charges en tant que Document Object (peut utiliser la même fonctionnalité que pour le module FEM).
-   Base de données des matériaux.
-   Permet les charges dans la direction Z ainsi que dans la direction Y (nécessite la définition des charges en tant que Document Object, sinon le tableau deviendra très long).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign WizardShaft/fr
