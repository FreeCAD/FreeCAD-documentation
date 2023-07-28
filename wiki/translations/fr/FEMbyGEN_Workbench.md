# <img alt="Icône de l\'atelier externe FEMbyGEN" src=images/FEMbyGEN.svg  style="width:64px;"> FEMbyGEN Workbench/fr


{{TOCright}}

## Introduction

FEMbyGEN est une extension de FreeCAD. Il fournit une interface simple pour choisir la meilleure solution en montrant le comportement structurel de vos conceptions à l\'écran pour l\'analyse paramétrique et les situations de chargement multiples.

<img alt="" src=images/Generative_Design.png  style="width:512px;">



### Déroulement des tâches 

1.  Cliquez sur le bouton **Initiate** pour créer les paramètres de l\'analyse paramétrique.
2.  Utilisez le bouton **Alias** pour faire correspondre la taille et le nom des paramètres.
3.  Associez la [feuille de calcul,](Spreadsheet_Workbench/fr.md) et votre modèle.
4.  Configurez le(s) modèle(s) d\'analyse avec l\'[atelier FEM](FEM_Workbench/fr.md).
5.  Revenez à l\' *atelier FEMbyGEN* et avec le bouton **Generate**, créez toutes les générations.
6.  Cliquez sur le bouton **FEA** et lancez FEA pour exécuter les simulations.
7.  Vous pouvez vérifier les fichiers de simulation en cliquant sur les lignes de la génération correspondante.
8.  Cliquez sur le bouton **Results** pour obtenir les résultats dans le fichier maître.
9.  La somme des résultats de tous les cas de charge se trouvera également sous Results dans la [Vue en arborescence](Tree_view/fr.md).



### Fonctions

-   Analyse FEM paramétrique
-   Supporte les cas de charge multiples
-   Récapitulation de tous les résultats dans un tableau
-   Trier les résultats par poids de sortie
-   Somme de tous les cas de charge



### Fonctions prévues à l\'avenir 

-   Analyse topologique
-   Méthode Taguchi pour générer des variations paramétriques

### Limitations

-   Ne fonctionne qu\'avec Calculix Solver

## Installation



### Gestionnaire des extensions 

FEMbyGEN peut facilement être installé via le <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Gestionnaire d\'Addons](Std_AddonMgr/fr.md) de FreeCAD depuis menu **Outils → Gestionnaire d'Addons**.

FEMbyGEN est en cours de développement actif et sera doté de nouvelles fonctionnalités fréquemment. Vous devez donc le mettre à jour régulièrement en utilisant également le menu **Outils → Gestionnaire d'Addons**.

Le code de FEMbyGEN est hébergé et développé ici [FEMbyGEN sur GitHub.com](https://github.com/Serince/FEMbyGEN).



### Manuellement

Voir [Comment installer des ateliers supplémentaires](How_to_install_additional_workbenches/fr.md)



### Prérequis

-   FreeCAD 0.19 ou plus récent



## Références

-   Auteur : Serdar Ince, Ögeday Yavuz, Rahul Jhuree
-   Code source : [FEMbyGEN sur GitHub.com](https://github.com/Serince/FEMbyGEN).
-   Forum de FreeCAD : <https://forum.freecadweb.org/viewtopic.php?p=626306>
-   Rapport de bogues : veuillez signaler les bogues à l\'adresse [FEMbyGEN sur GitHub.com](https://github.com/Serince/FEMbyGEN).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > FEMbyGEN Workbench/fr
