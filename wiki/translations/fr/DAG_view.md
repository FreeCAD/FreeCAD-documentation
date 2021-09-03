

## Introduction


{{TOCright}}

La [Vue DAG](DAG_view/fr.md) signifie [Directed Acyclic Graph (Graphe orienté acyclique)](https://fr.wikipedia.org/wiki/Graphe_orient%C3%A9_acyclique). Elle montre les relations entre les différents objets du document. Elle est principalement destinée à montrer comment certains objets dépendent d\'autres objets dans un modèle complexe comportant de nombreuses fonctionnalités et références, telles que celles pouvant être créées avec l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [atelier PartDesign](PartDesign_Workbench/fr.md).

La vue DAG ressemble au graphe qui peut être produit à partir d'un référentiel Git et de ses branches. Associée à la [vue en arborescence](tree_view/fr.md) et au [Graphique de dépendance](Std_DependencyGraph/fr.md), la vue DAG est un outil permettant d\'inspecter l\'historique paramétrique des objets d\'un document.

## Exemple

Un modèle simple sera vu avec différentes vues.

![](images/FreeCAD_DAG_view_3D.png ) *Modèle avec des formes 2D et 3D.*

<img alt="" src=images/FreeCAD_DAG_view_Tree_view.png ) ![](images/FreeCAD_DAG_view.png  style="width:" height="500px;">


*A gauche: objets affichés dans la [vue en arborescence](tree_view.md) standard. A droite: objets affichés dans la vue DAG.*

![](images/FreeCAD_DAG_view_Std_DependencyGraph.png )


*Relations entre les objets affichés dans le [Graphique de dépendance](Std_DependencyGraph/fr.md).*

## Activation de la vue DAG {#activation_de_la_vue_dag}

La vue DAG a été introduite dans la version 0.17 en tant que fonctionnalité expérimentale pour les utilisateurs expérimentés et les développeurs, afin de leur permettre de dépanner des modèles complexes; de ce fait, la vue DAG n\'est pas disponible par défaut.

Pour utiliser cette vue, utilisez l\'[éditeur des paramètres](Std_DlgParameter/fr.md). Créez le sous-groupe suivant s\'il n\'existe pas

-    `BaseApp/Preferences/DockWindows/DAGView`
    

puis ajoutez le paramètre`Enabled` de type `Boolean`, et le mettre régler sur `True`.

Redémarrez FreeCAD et activez la vue DAG : {{MenuCommand|{{StdMenu|[Affichage](Std_View_Menu/fr.md)}} → Panneaux → Vue DAG}}.

Dans l\'[Editeur des paramètres](Std_DlgParameter/fr.md), vous pouvez également modifier certaines propriétés dans le sous-groupe suivant

-    `BaseApp/Preferences/DAGView`
    

-   FontPointSize - Définissez la taille de la police du texte et peut aider à la lisibilité avec les écrans à haute résolution. Définissez sur 0 pour la taille de police par défaut.

-   Mode de selection
    -   0 - un seul clic sélectionne un élément. Ctrl-clic pour ajouter des éléments à la sélection.
    -   1 - chaque clic ajoute / supprime un élément à la sélection.

-   Direction - l\'ordre dans lequel les éléments sont affichés.
    -   1 - enfant en haut, parent en dessous
    -   -1 - parent en haut, enfants en dessous

## Liens

See also:

-   [DAGView](https://forum.freecadweb.org/viewtopic.php?f=20&t=11276), fil de discussion présentant le nouvel outil.
-   [easter egg of PartDesign Next: DAG View](https://forum.freecadweb.org/viewtopic.php?f=20&t=15375), y compris la vue avec la mise à jour de PartDesign.


{{Interface navi

}} {{Std Base navi}} 
