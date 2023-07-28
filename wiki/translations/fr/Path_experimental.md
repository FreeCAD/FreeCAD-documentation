# Path experimental/fr
{{TOCright}}

## Description

L\'atelier Path contient un ensemble de commandes cachées. Elles sont cachées par défaut car elles sont expérimentales. Une commande peut être considérée comme expérimentale pour l\'une des raisons suivantes :

-   Elle est incomplète.
-   Elle présente des bogues.
-   Elle est instable.
-   Elle ne produit pas de chemins corrects, stables, sûrs.
-   Il ne s\'agit pas d\'une commande standard, régulièrement utilisée dans le déroulement traditionnel de la FAO.
-   Elle est mature mais n\'a pas encore été déplacée vers la liste d\'outils standard.
-   \... d\'autres raisons.



## Activer les commandes expérimentales 

Pour accéder aux commandes expérimentales masquées dans de l\'atelier Path, l\'utilisateur doit les activer dans l\'[éditeur des paramètres](Std_DlgParameter/fr.md).

1.  Ouvrez l\'[éditeur des paramètres](Std_DlgParameter/fr.md) via **Outils → Éditer les paramètres...**
2.  Une fois dans l\'éditeur, le chemin est **BaseApp → Preferences → Mod → Path**
3.  Pour activer les commandes [Path Surface](Path_Area/fr.md) et [Path Plan de travail](Path_Area_Workplane/fr.md) :
    -   Cliquez avec le bouton droit de la souris dans la zone de la liste des paramètres et sélectionnez **Nouveau → Nouvel article booléen** dans le menu contextuel.
    -   Nommez le nouveau paramètre : `EnableAdvancedOCLFeatures`. (sensible à la casse).
    -   Définissez-le à `True`.
4.  Pour activer les autres commandes expérimentales :
    -   Sélectionnez à nouveau **Nouveau → Nouvel article booléen** dans le menu contextuel.
    -   Nommez le nouveau paramètre : `EnableExperimentalFeatures`. (sensible à la casse).
    -   Définissez-le à `True`.
5.  Enregistrez les paramètres.
6.  Redémarrez FreeCAD.



## Informations supplémentaires 

En savoir plus sur les commandes expérimentales spécifiques sur les [pages du wiki qui renvoient à celle-ci](https://www.freecadweb.org/wiki/Special:WhatLinksHere/Path_experimental).


 {{Path Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Path](Path_Workbench.md) > Path experimental/fr
