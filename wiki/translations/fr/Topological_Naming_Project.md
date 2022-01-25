# Topological Naming Project/fr
Cette page est consacrée à la description de l\'idée du projet Google Summer of Code concernant la dénomination topologique. Pour le sujet en lui-même, veuillez consulter [Projet de dénomination](Naming_project/fr.md). La page wiki liée peut également servir de point de départ pour aborder le problème de dénomination.

## Aperçu

FreeCAD est un système de modélisation paramétrique, par conséquent, différentes étapes de modélisation dépendent d\'une ou plusieurs étapes précédentes. Les modifications apportées à un objet se propagent à travers l\'historique de modélisation à tous les objets dépendants. Ceci est réalisé grâce à un système de liaison, implémenté avec des propriétés. Cette liaison est très robuste lorsqu\'elle est effectuée sur une base d\'objet entier. Cependant, de nombreux liens doivent être plus fins et liés à des sous-parties d\'un objet. Dans l\'environnement de l\'atelier Part, par exemple, de nombreux liens vont vers des entités topologiques spéciales telles que des sommets, des arêtes ou des faces. La stabilité de ces liens dépend de la dénomination exacte des éléments de topologie après un recalcul. Cela n\'est actuellement pas garanti dans FreeCAD, ce qui peut entraîner de nombreuses erreurs dans les étapes de modélisation dépendantes après de simples modifications d\'un objet de base. Comme la direction actuelle du développement de FreeCAD semble conduire à une utilisation plus forte de ces liens, le problème de dénomination doit être résolu.

Le projet GSoC vise à jeter les bases pour résoudre ce problème et à prouver l\'approche choisie sur les cas de test. L\'approche privilégiée pour résoudre le problème est décrite [ici](https://docs.google.com/document/d/1-d2JD8RH13ar7QPh_SpX2H5eiNND4DiCPBmGwA2R9Ug/edit), avec une implémentation démarrée [ici](https://github.com/ickby/FreeCAD_sf_master/tree/Naming).

## Détails

1.  Familiarisez-vous avec opencascade, le noyau de modélisation géométrique FreeCADs et apprenez comment fonctionne la structure des données de la topologie et comment les algorithmes partagent, modifient et génèrent la topologie. De préférence, l\'étudiant a déjà travaillé avec opencascade, car la bibliothèque est complexe et s\'y mettre prend du temps.
2.  Familiarisez-vous avec le système de liaison FreeCAD et comment il est lié aux entités de topologie dans les infrastructures de données ouvertes. Il est également important de comprendre l\'utilisation d\'occ dans FreeCAD, l\'utilisation d\'une classe de topologie dédiée combinée à l\'utilisation directe d\'algorithmes occ en dehors de cette classe. Cette double approche peut ne pas être idéale pour une solution du problème de dénomination, donc une bonne compréhension de celui-ci est nécessaire.
3.  Commencez à implémenter une classe Identifier qui stocke l\'historique de création d\'une forme. Identifiez toutes les données nécessaires pour la rendre unique et détaillez l\'interface.
4.  Intégrez la classe d\'identifiant dans la structure de données Topologie et portez quelques premiers algorithmes pour l\'utiliser. Étendez également l\'interface python de la classe Topologie pour permettre l\'utilisation des identificateurs pour l\'extraction des sous-formes.
5.  Créez un ensemble de cas de test pour montrer l\'efficacité de l\'implémentation.

## Résultat attendu 

1.  Une première implémentation dans FreeCAD pour montrer l\'algorithme de travail
2.  Un ensemble de cas de test intégré au système de test disponible qui montre les cas majeurs du problème de nommage topologique et comment ils sont résolus par la mise en œuvre du prototype

## Possibilités futures 

Si ce projet est terminé avec succès, une intégration complète dans la source FreeCAD peut faire partie d\'une contribution supplémentaire ou même d\'un projet GSoC propre

## Propriétés du projet 

### Compétences

-   Langage de programmation C ++
-   Compréhension approfondie et utilisation des API de FreeCAD et d\'opencascade
-   Capacité à lire et comprendre des textes et articles scientifiques
-   La connaissance de la modélisation 3D, de la topologie et de la géométrie informatique est un plus

### Difficulté

Difficile

### Information Supplémentaire



---
![](images/Right_arrow.png) [documentation index](../README.md) > Topological Naming Project/fr
