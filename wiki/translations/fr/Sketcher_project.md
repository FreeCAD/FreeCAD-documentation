# Sketcher project/fr
**
Ce plan de développement est probablement obsolète. Pour plus d'informations, voir [Plan de développement](Development_roadmap/fr.md).<br>
Si vous n'êtes pas impliqué dans le développement discuté ici :<br>
!!! S'IL VOUS PLAÎT, NE MODIFIEZ PAS ET NE TRADUISEZ PAS !!!
**


{{TOCright}}

C\'est le projet d\'esquisse de **FreeCAD développement**. Il suit les règles de la \[<http://fr.wikipedia.org/wiki/Getting_Things_Done>\| Getting Things Done\] processus. Les projets sont collectées dans la [feuille de route de développement](Development_roadmap/fr.md).

## Buts et principes 

Il s\'agit d\'un projet de développement logiciel, visant à mettre en œuvre et en fonction des capacités d\'esquisse et de contraintes. Sa mise en œuvre sur certains éléments **Gui** et la liaison à la résolution de contraintes.

Les étapes de développement sont ici rabotées et suivies dans le système de suivi émission pour obtenir un journal des modifications bien informés sur : [Change Log.](http://www.freecadweb.org/tracker/)

## Résultats

## Réflexions

Afin d\'améliorer les performances de résolution, du **sketcher**, un partitionnement de graphe, basé sur le système de contraintes peut avoir lieu. L\'ensemble des contraintes et l\'ensemble de paramètres inconnus peuvent être représentés dans un **[graphe biparti](http://fr.wikipedia.org/wiki/Graphe_biparti)**, avec des contraintes correspondant à des noeuds gauche et droit, et des noeuds inconnus.**Fait**

Une étape de simple prétraitement, mais, souvent très utile est de reconnaître les sous-groupes disjoints, de sorte qu\'ils puissent être traités séparéments, dans le solveur.**Fait**

D'ailleurs on pourrait réduire le nombre de paramètres inconnus, qui sont prise en compte dans la solution. Au début d\'une solution, il faut vérifier que les contraintes ne sont pas déjà satisfaites. Par l\'analyse graphique on pouvait trouver un ensemble minimal de paramètres inconnus qui devraient être pris en compte afin de satisfaire toutes les contraintes non satisfaites.

Aller plus loin, sub-parts rigides d\'une esquisse pourraient être détectés et réduites à 3 degrés de liberté (x, y, rotation).

## Organisation

## Actions à venir 

Pour la 0.14:

1.  Glisser la souris pour une sélection multiple
2.  Liste des géométries dans le panneau de tâches (similaire à la liste des contraintes)
3.  Ajout d\'une option de menu contextuel pour convertir une contrainte de points coïncidents en contraintes de tangence
4.  Outil Polygone (commodité)
5.  Mise à jour de la documentation wiki sur la contrainte Symmetrie et l\'outil Polyligne (m-key)

Idée à travailler :

Interface utilisateur :

1\. Grille plein écran (unité courante)

2\. Auto-contraintes plus intelligentes :

-   2.a L\'algorithme ne tient compte que de la géométrie qui se trouve sur l\'écran pour augmenter les performances, et, améliorer les sélections

-   2.b Prévention les conflits de contraintes

3\. Conseils sur les lignes : horizontales, verticales, perpendiculaires, tangentes contraintes ?

4\. Révision des icônes de contraintes en les fusionnant en un seul Node

-   4.a Fusion pour constituer un Node pour améliorer les performances

-   4.b Suppression nécessaire pour ray, choisir d\'améliorer les performances

-   4.c Partage plus efficace de la mémoire de texture.

-   4.d Améliorer l\'algorithme pour prévenir le chevauchement

-   4.e Barre d\'outils pour visualiser les contraintes indépendamment

5\. Amélioration des références (label) :

-   5.a Le label du rayon peut être positionné à n\'importe quel angle

-   5.b Au besoin éffacer ce qui n\'est pas nécessaire pour le stocker dans SoImage

6\. Fixer la grille sur un bord

7\. Contraintes automatique, tout en faisant glisser (Point, Point d\'entrée sur la ligne coïncidente) ?

8\. Mise en évidence d\'entités ou, zoomer sur une zone précise du croquis

9\. Association à la conception de pièces (prise en charge de la transparente objets)

10\. Appliquer la fonction plan d\'esquisse avec l\'introduction du module d\'assemblage (Assembly module)

11\. Amélioration de la sélection de Points, en mettant en œuvre un nouveau \"nœud\" personnalisé.

12\. Possibilité de construction de lignes pointillées a la place de lignes pleines.

**Pour 0,13:**

1\. le support à arc/arc et arc/cercle dans la contrainte de tangence - FAIT \[logari81\]

2\. le support de la contrainte perpendiculaire aux arcs - FAIT \[logari81\]

3\. Zoom indépendants flèches (contrainte de symétrie)/lignes de cote - FAIT \[mrlukeparry\]

4\. géométrie externe/contraintes - FAIT \[logari81\]

5\. boîte de sélection - \[mrlukeparry\] **Fait**

**6**. faire glisser la souris sur la sélection multiple- **Ignorée pour 0.14**

7\. diagnostic meilleurs constraites (Issue \# 691) - FAIT \[logari81\]

8\. liste des formes géométriques dans le panneau des tâches (similaire à la liste des contraintes)

9\. support aux points des constructions géométriques - FAIT \[logari81\]

**10**. ajout d\'une option au menu contextuel, pour convertir une contrainte points coïncidents aux contraintes de tangence

*\' 11.*\' restreindre le travailler avec des points de symétrie, au lieu de lignes de symétrie (utile par exemple pour la définition du point central) - *\'FAIT* \"\[logari81\]

**Pour 0.12:**

1\. paramètres de contrainte (points de référence) modifiables dans la vue 3D FAIT \[jriegel\]

2\. synchronisation entre la sélection liste widget view - Sélection de vue 3D - FAIT \[wmayer\]

3\. éviter le chevauchement des symboles de contraintes FAIT - \[mrlukeparry\]

-   3a. faire des symboles des contraintes plus petit, sélectionner et éviter les chevauchements lors d\'un zoom FAIT - \[mrlukeparry\]

-   3b. créer des icônes de contraintes pour la vue 3D Inventor FAIT - \[mrlukeparry\]

-   3c. faire dépend de la taille donnée de texte sur zoom FAIT - \[mrlukeparry\]

-   3d. rendre le texte plus facilement sélectionnable donnée FAIT - \[mrlukeparry\]

3e. Éviter le chevauchement de texte sur les étiquettes Datum FAIT - \[mrlukeparry\]

4\. tester le nouveau solveur en mode autonome

5\. contraintes externes (ayant des contraintes avec des références en dehors du croquis, un certain avantage du modèle 3D par exemple) 0.13 \[jriegel\]

6\. auto-contraintes FAIT \[jriegel\]

-   6a. auto-contrainte perpendiculairement FAIT - \[mrlukeparry\]

7\. visualiser contraintes de tangence FAIT - \[mrlukeparry\]

8\. visualiser le point de contraintes de distance de ligne et point à point les contraintes de distance FAIT - \[logari81\]

9\. ajouter des index à des symboles contraintes en vue 3D afin de distinguer entre les contraintes de même nature FAIT - \[mrlukeparry\]

10\. contrainte rayon (y compris la visualisation) FAIT - \[logari81\]

11\. contrainte d\'angle (y compris la visualisation) FAIT - \[logari81\]

12\. mettre en œuvre un outil de filet dans le sketcheur FAIT \[mrlukeparry\]

-   12a. fournir une méthode de mise en rayon du congé (numéro 437)

13\. mettre en œuvre un outil Ajuster/Prolonger dans sketcheur FAIT \[logari81\]

-   13a. mettre en œuvre un outil d\'extention SKIPPED \[logari81\]

-   13b. couper en appuyant sur les arcs DONE \[mrlukeparry\]

14\. contrainte d\'égalité de longueurs (y compris dans la visualisation) FAIT - \[logari81\]

15\. diagnostic de contraintes - degré de liberté de comptage FAIT - \[logari81\]

16\. contrainte de symétrie (y compris la visualisation) FAIT - \[logari81\]

17\. point sur ​​la mise en œuvre de la contrainte d\'objet FAIT - \[mrlukeparry\]

18\. Assurez-Snap-Grille moins «gourmand» FAIT \[mrlukeparry\]

19\. Page wiki pour le Sketcher Workbench \[normandc\]


{{Sketcher Tools navi

}}  

_

---
[documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher project/fr
