# Draft Constrain/fr
## Description

En plus de la saisie de coordonnées ou de l\'utilisation de l\'[aimantation](Draft_Snap/fr.md), il existe une fonctionnalité appelée contrainte qui vous aide à dessiner avec précision dans l\'<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [atelier Draft](Draft_Workbench/fr.md) et l\'<img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [atelier Arch](Arch_Workbench/fr.md). Pour chaque point consécutif, vous pouvez contraindre le mouvement du curseur à la direction X, Y ou Z du système de coordonnées du [plan de travail](Draft_SelectPlane/fr.md). Ceci peut par exemple être utilisé pour créer une ligne parfaitement verticale.

La contrainte est disponible avec la plupart des commandes de [Draft](Draft_Workbench/fr.md) et [Arch](Arch_Workbench/fr.md).

![](images/Draft_Constrain_taskpanel_example.png ) 
*Lorsque le curseur est contraint, le panneau de tâches verrouille les valeurs qui ne sont pas modifiées.*



## Utilisation des contraintes horizontales et verticales 

1.  Choisir une commande de [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) pour créer votre géométrie.
2.  Choisir un premier point. Un point précédent est nécessaire.
3.  Effectuer l\'une des opérations suivantes :
    -   Pour une contrainte horizontale : déplacer le curseur à gauche ou à droite du point précédent.
    -   Pour une contrainte verticale : déplacer le curseur au-dessus ou au-dessous du point précédent.
4.  Maintenir la touche **Maj** enfoncée.
5.  Le curseur est maintenant contraint.
6.  Choisir le point suivant.
7.  Si la commande est toujours active : vous pouvez relâcher **Maj** pour désactiver la contrainte.
8.  Toujours relâcher **Maj** lorsque la commande est terminée.



## Utilisation des contraintes X, Y et Z 

1.  Choisir une commande de [Draft](Draft_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md) pour créer votre géométrie.
2.  Choisir un premier point. Un point précédent est nécessaire.
3.  Appuyer sur **X**, **Y** ou **Z** pour spécifier la direction.
4.  Le curseur est maintenant contraint.
5.  Choisir le point suivant.
6.  Si la commande est toujours active, effectuer l\'une des opérations suivantes :
    -   Appuyer sur la même touche pour désactiver la contrainte.
    -   Appuyer sur l\'une des deux autres touches pour contraindre dans une autre direction.
7.  Les contraintes X, Y et Z sont automatiquement désactivées lorsque la commande est terminée.



## Remarques

-   La contrainte peut être combinée avec l\'[aimantation](Draft_Snap/fr.md).
-   La commande [Draft Décaler](Draft_Offset/fr.md) et la commande [Draft Ajuster ou prolonger](Draft_Trimex/fr.md) utilisent un type de contrainte différent, à savoir restreindre l\'opération à un certain segment.



## Préférences

Voir aussi : [Réglage des préférences](Preferences_Editor/fr.md) et [Draft Préférences](Draft_Preferences/fr.md).

-   La touche par défaut **Modificateur de contrainte**, **Maj**, peut être modifiée : **Édition → Préférences... → Draft → Grille et aimantation → Modificateur de contrainte**.
-   Les raccourcis **X**, **Y** et **Z** peuvent être modifiés : **Édition → Préférences... → Draft → Interface → Raccourcis de commandes**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Constrain/fr
