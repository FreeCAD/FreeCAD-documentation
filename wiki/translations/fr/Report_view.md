# Report view/fr
## Introduction

La [Vue rapport](Report_view/fr.md) est un panneau qui affiche les messages texte des processus FreeCAD. Il est disponible dans **Affichage → Panneaux → Vue rapport**.

Certaines propriétés de la vue, telles que la couleur du texte et son affichage automatiqueOpérations Booléenne en cas d'avertissements ou d'erreurs, peuvent être configurées dans l'onglet **Général → Fenêtre de sortie** de l\'[Éditeur des préférences](Preferences_Editor/fr#Fen.C3.AAtre_de_sortie.md).

<img alt="" src=images/FreeCAD_Report_view.png  style="width:800px;">



*La vue rapport montrant les messages lorsque FreeCAD vient de démarrer.*

## Messages


**Voir aussi :**

[Console API](Console_API/fr.md) et [Débuter avec les scripts sous Freecad](FreeCAD_Scripting_Basics/fr.md).

La vue rapport affiche les messages de la classe interne FreeCAD `Console`.

-    `FreeCAD.Console.PrintMessage("text")`imprime n\'importe quel type de message informatif qui n\'implique pas un mauvais comportement, par exemple: les coordonnées des points, le résultat d\'un calcul de distance, le nombre de points dans une forme, etc. Par défaut, en couleur noire.

-    `FreeCAD.Console.Console.PrintWarning("text")`imprime des messages destinés à avertir l\'utilisateur d\'un comportement étrange de l\'application. Des avertissements doivent être affichés lorsque certaines fonctionnalités sont manquantes mais que le logiciel fonctionne toujours de manière acceptable. Par défaut, de couleur jaune.

-    `FreeCAD.Console.PrintError("text")`imprime les messages qui sont destinés à être des messages d\'erreur, c\'est-à-dire, quand un composant critique manque qui fait échouer une certaine opération. Par défaut, de couleur rouge.

-    `FreeCAD.Console.PrintLog("text")`imprime les messages qui vont dans les logs. Ces messages peuvent être tout ce qui est utile pour résoudre un problème à l\'avenir en lisant les protocoles, par exemple, en démarrant ou en fermant un workbench. Par défaut, de couleur bleue.

Ces fonctions peuvent être utilisées à partir de la [console Python](Python_console/fr.md) directement, ou à partir de [Macros](Macros/fr.md) et des ateliers personnalisés.

<img alt="" src=images/FreeCAD_Report_view_example.png  style="width:800px;">



*Exemples de messages dans la vue rapport : un message général, un avertissement, une erreur et un message enregistré.*

## Actions

Un clic droit sur la Vue rapport ouvre un menu contextuel avec les commandes suivantes :

-    **Options**:

    -   
        **Afficher les types de messages**
        
        : voir [Éditeur des préférences](Preferences_Editor/fr#Fen.C3.AAtre_de_sortie.md).

    -   
        **Afficher la fenêtre de sortie sur**
        
        : idem.

    -   
        **Rediriger la sortie de Python**
        
        : idem.

    -   
        **Rediriger les erreurs de Python**
        
        : idem.

    -   
        **Aller à la fin**
        
        : si cette option est cochée, la Vue rapport défilera vers le bas lorsqu\'un nouveau message sera ajouté.

-    **Copier**: enregistre le texte sélectionné dans le presse-papiers pour le coller ultérieurement ; désactivé si rien n\'est sélectionné.

-    **Tout sélectionner**: sélectionne tout le texte dans la Vue rapport.

-    **Effacer**: efface tous les messages dans la Vue rapport. Ceci est utile si vous voulez dépanner un outil qui imprime des messages dans la Vue rapport, et si vous voulez être sûr qu\'il n\'y a pas d\'anciens messages provenant d\'outils précédents.

-    **Enregistrer sous...**: enregistre les messages de la Vue rapport dans un fichier texte.


{{Interface navi

}} {{Std Base navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Report view/fr
