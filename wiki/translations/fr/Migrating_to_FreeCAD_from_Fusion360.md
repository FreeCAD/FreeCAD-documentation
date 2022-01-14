# Migrating to FreeCAD from Fusion360/fr
{{TOCright}}

## Contexte

Cette page est destinée aux utilisateurs qui souhaitent migrer vers FreeCAD depuis l\'univers Fusion 360.

## Que dois-je faire ? 

1.  La première chose que vous voulez faire est de sortir vos fichiers des formats et du stockage propriétaires. Commencez par exporter vos modèles du cloud vers votre machine locale.
    -   Une méthode populaire consiste à utiliser ce script [Fusion360 total exporter](https://github.com/Jnesselr/fusion-360-total-exporter).
2.  Nous vous recommandons d\'exporter au format STEP.

## Glossaire


**Veuillez également faire référence au projet en cours [CAD Rosetta Stone](CAD_Rosetta_Stone.md) pour connaître les noms analogues utilisés par les CAO propriétaires populaires**

Reportez-vous à la page [glossaire](Glossary/fr.md) en général. Ici une courte liste de termes spécifiques que les utilisateurs de F360 peuvent trouver particulièrement utiles:

-   Contrainte de tangence - Forme FreeCAD de **Contrainte colinéaire**. Voir <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;"> [Sketch Contrainte tangente](Sketcher_ConstrainTangent/fr#Entre_deux_lignes_.28colin.C3.A9aire.29.md).
-   Extrusion - La fonction **extruder** dans FreeCAD. Lisez la documentation <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Protrusion](PartDesign_Pad/fr.md) pour en savoir plus.
-   Toponymie - Abréviation de [Problème de dénomination topologique](Topological_naming_problem/fr.md). Très bien couvert dans les [vidéos youtube de Brodie Fairhall](https://www.youtube.com/watch?v=6p2vqEEmWq4)\].

## FAQ

1.  Quels formats supportez-vous dans FreeCAD ?
    -   Le format de fichier natif dans FreeCAD est BREP, [BREP](https://fr.wikipedia.org/wiki/B-Rep), fourni par le noyau de géométrie interne [OpenCASCADE (OCCT)](OpenCASCADE/fr.md).
    -   FreeCAD supporte tous les formats que OCCT supporte, donc STEP et IGES au moins.
2.  Quels formats dois-je utiliser pour migrer vers FreeCAD ?
    -   STEP est le meilleur format car c\'est un format solide [Shape](Shape/fr.md), par opposition à un format de [Maillage](Mesh/fr.md) (STL, OBJ, DAE). Exemple, [Importing Step with Colors](https://forum.freecadweb.org/viewtopic.php?f=3&t=50308).
    -   L\'importation d\'un STL est possible, mais ce format de maillage sera difficile à modifier par la suite. Nous recommandons de convertir les maillages importés en formes solides en utilisant **[<img src=images/Part_ShapeFromMesh.svg style="width:16px">. [Part Forme à partir du maillage](Part_ShapeFromMesh/fr.md)**. Remodeler l\'objet dans FreeCAD, tout en utilisant le maillage comme référence, est le meilleur conseil.

## Astuces

-   \@MPetrika ([twitter](https://twitter.com/MPetrikas/status/1362051484704264198)) recommande d\'installer [Atelier ModernUI](ModernUI_Workbench/fr.md) de HakanSeven12

## Ressources de formation 

-   [Introduction Fusion360 vers FreeCAD - Introduction](https://www.youtube.com/watch?v=_GxJkB23ZHM), vidéo de Brodie Fairhall.
-   [Fusion360 to FreeCAD - Part 2](https://www.youtube.com/watch?v=IESZD4QS3P8), vidéo de Brodie Fairhall.
-   [V0.19 Benchmarking\--2019 Monthly Challenges](https://forum.freecadweb.org/viewtopic.php?f=36&t=50492), une série d\'objets créés avec Fusion360 sont remodelés à l\'aide de FreeCAD, par l\'utilisateur expérimenté ppemawm.
-   [Tutoriel écrit pour débutants : de la première partie au dessin technique](https://github.com/macdroid53/LearningFreeCAD) par macdroid53.
-   [Une ressource en ligne pour nous, utilisateurs réguliers de FreeCAD](https://www.freecad.info/).

## Vidéos comparatives 

-   [Modéliser une turbine de compresseur dans FreeCAD et Fusion360](https://www.youtube.com/watch?v=kirDbZd0dvI&feature=youtu.be)

## Aide

Cette page wiki manque-t-elle quelque chose? Veuillez faire une demande de [permissions wiki](https://forum.freecadweb.org/viewtopic.php?f=21&t=6830) sur le forum pour éditer cette page.

## En relation 

-   [Migrer de OnShape vers FreeCAD](Migrating_to_FreeCAD_from_OnShape/fr.md)

---
[documentation index](../README.md) > Migrating to FreeCAD from Fusion360/fr
