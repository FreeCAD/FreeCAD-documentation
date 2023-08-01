# FreeCAD Managing Expectations/fr
**Bien que nous accueillions et encouragions la croissance et la participation de la communauté, les demandes, les divagations émotionnelles et les revendications sauvages sont généralement mal reçues car notre communauté est composée de nombreux partisans expérimentés et passionnés de FreeCAD qui ont entendu des déclarations similaires à maintes reprises. Si vous trouvez qu'une fonctionnalité manque, ou que quelque chose vous gêne, nous vous encourageons vivement à envisager de vous engager dans le code lui-même. FreeCAD est largement développé par un groupe relativement restreint de personnes talentueuses qui ont toutes un emploi, une famille et d'autres intérêts que la programmation à la demande. Si vous avez les compétences (Python/C++) et la motivation pour participer, vos contributions peuvent aider à rendre FreeCAD encore meilleur qu'il ne l'est aujourd'hui. Vous pouvez trouver les bogues et les demandes de fonctionnalités suivis [https://github.com/FreeCAD/FreeCAD/issues ici].**


{{TOCright}}

## Objectif

Cette page wiki est destinée aux nouveaux utilisateurs de FreeCAD venant d\'autres solutions de CAO/FAO.

## Déclaration liminaire 

De nombreux amateurs, designers indépendants et petites entreprises cherchent souvent un refuge contre les coûts élevés et les restrictions de licence des logiciels commerciaux, ou peut-être avez-vous simplement choisi FreeCAD parce que vous croyez dans la philosophie du [FOSS](https://fr.wikipedia.org/wiki/Free/Libre_Open_Source_Software). Dans tous les cas, BIENVENUE ! Il y a de nombreux utilisateurs, tout comme vous, qui ont réussi la transition vers FreeCAD pour leurs besoins personnels et professionnels. Cette page wiki est conçue pour vous aider à vous mettre sur la voie du succès et à établir des attentes réalistes tout en vous plongeant dans la *Méthode FreeCAD*, qui est très probablement différent de ce à quoi vous vous êtes peut-être habitué avec d\'autres logiciels de CAO courants.

## Qu\'est-ce que je peux attendre ? 

À la base, FreeCAD est un puissant modeleur paramétrique. Il utilise un concept d\'\"atelier\" modulaire, où chaque atelier est responsable de tâches et de fonctions spécifiques. Ce concept est très souple et peut être utilisé avec succès à de nombreuses fins. FreeCAD est activement développé, utilisé en production, et assez stable ; mais comme tout autre programme de CAO, il n\'est pas stable à 100%.

Si vous venez d\'un autre programme de CAO, vous pouvez trouver la terminologie, la structure et l\'organisation de FreeCAD légèrement étranges. Vous aurez probablement besoin de faire quelques ajustements à vos flux de travail, d\'apprendre des solutions de contournement fonctionnelles ou d\'utiliser notre puissant écosystème des [macros](Macros/fr.md), mais dans la plupart des cas, vous serez en mesure d\'obtenir ce que vous voulez. Et si vous avez besoin d\'aide : nous avons un [forum](https://forum.freecad.org/index.php) très actif et réactif, prêt à vous aider. Parmi les membres du forum, il y a forcément des (anciens) utilisateurs de votre programme de CAO actuel. N\'hésitez donc pas à faire appel à cette ressource.

## Comment puis-je contribuer ? 

Il y a plusieurs façons de le faire : vous pouvez faire un [donation](Donate/fr.md), aider à répondre aux questions du [forum](https://forum.freecad.org/index.php), ou écrire de la documentation ou du code. Voir [Contribuer à FreeCAD](Help_FreeCAD/fr.md).

## Ressources pédagogiques 

### Officielles

-   [Ce wiki](Main_Page/fr.md)
-   [Le forum d\'aide](https://forum.freecadweb.org/viewforum.php?f=3)
-   [Solutions de contournement pour les problèmes connus](Workarounds/fr.md)

### Non officielles 

Les chaînes YouTube suivantes ont un contenu d\'assez bonne qualité centré sur FreeCAD (il est recommandé d\'ignorer les tutoriels basés sur la version 0.17 ou antérieure) :

-   *MangoJelly Solutions* (plusieurs listes de lecture de vidéos pour débutants, intermédiaires et avancés).
-   *Joko EngineeringHelp* (vidéos intermédiaires/avancées)
-   *Brodie Fairhall* (Quelques vidéos aidant les utilisateurs de Fusion 360 à passer à FreeCAD)
-   Et plus encore\...

## Questions et réponses 

### \"FreeCAD peut-il faire XYZ ?\" 

FreeCAD permet déjà d\'effectuer les types de travaux suivants :

-   Modélisation paramétrique basée sur des splines à l\'aide des ateliers [Part](Part_Workbench/fr.md), [Part Design](PartDesign_Workbench/fr.md) et [Sketcher](Sketcher_Workbench/fr.md).
-   Modélisation de surfaces et de courbes à l\'aide de NURBS
-   Importation/modification de [maillages](Mesh_Workbench/fr.md)
-   Simulation d\'assemblage (3 approches différentes, [A2+](A2plus_Workbench/fr.md), [ASM3](Assembly3_Workbench/fr.md), et [ASM4](Assembly4_Workbench/fr.md), sont toutes activement développées)
-   Conception [architecturale](Arch_Workbench/fr.md)/[BIM](BIM_Workbench/fr.md)
-   Analyse des contraintes mécaniques ([FEM/FEA](FEM_Workbench/fr.md))
-   Analyse numérique de la dynamique des fluides ([CFD](Cfd_Workbench/fr.md))
-   [Dessins techniques](TechDraw_Workbench/fr.md)/[Dessin](Draft_Workbench/fr.md)
-   Et d\'autres [ateliers](Workbenches/fr.md) et [ateliers externes](External_workbenches/fr.md)\...

### \"L\'interface utilisateur (UI/UX) est laide, étrange, déroutante ou ne ressemble pas au logiciel XYZ !\" 

FreeCAD permet une [personnalisation étendue](Interface_Customization/fr.md) de l\'interface utilisateur. Bien que nous soyons conscients que les couleurs ou la disposition des éléments par défaut peuvent ne pas plaire à tout le monde, nous vous encourageons à les adapter à vos propres besoins et flux de travail. Si vous pensez avoir trouvé un arrangement/un thème/des barres d\'outils personnalisées populaires, etc., n\'hésitez pas à tirer parti de la fonctions des [kits de préférence\|](Preference_Packs/fr.md) récemment ajoutée et à la partager avec la communauté. Peut-être vos efforts aideront-ils quelqu\'un d\'autre dans sa transition vers FreeCAD. Les logiciels libres prospèrent grâce à toutes sortes de contributions de la communauté et c\'est un sujet de discussion courant.

### \"Pourquoi cette fonctionnalité ne fonctionne-t-elle pas comme dans le logiciel XYZ ?\" 

FreeCAD a un historique de développement qui s\'étend sur plus de [20 ans](History/fr.md). Les fonctions et les comportements sont fortement revus, débattus et évalués avant d\'être ajoutés ou modifiés. Ayez l\'esprit ouvert, même si cela n\'est pas évident, il y a probablement une très bonne raison derrière ces choses. Cela ne veut pas dire que FreeCAD est parfait, mais considérez que ce à quoi vous vous êtes habitué n\'est peut-être pas la seule ou la meilleure façon de faire quelque chose.

### \"Je n\'arrive pas à comprendre le flux de travail de FreeCAD !\" 

La philosophie de FreeCAD est de ne pas dicter \"comment\" vous l\'utilisez. Il fournit plutôt des outils et un large éventail d\'options qui vous permettent de les utiliser. Cela signifie deux choses. Premièrement, le logiciel ne va pas nécessairement vous \"guider\" ou vous \"orienter\" vers un certain style ou flux de travail. Deuxièmement, cela signifie que vous pouvez expérimenter avec les outils et trouver ce qui fonctionne le mieux pour vous. Cela ne veut pas dire qu\'il n\'y a pas de [\"meilleures pratiques\"](Feature_editing/fr.md) générales à garder à l\'esprit en utilisant FreeCAD, mais ces meilleures pratiques s\'appliquent généralement à tout logiciel de conception professionnel lors de la création de modèles stables.

### \"C\'est quoi ce bordel avec tous ces ateliers ?\" 

L\'une des puissantes fonctions de FreeCAD est sa modularité. Ceci est réalisé en compartimentant le développement des outils dans des ateliers. Une fois que vous êtes familiarisé avec les outils fournis, ils peuvent souvent travailler en synergie pour créer des modèles très complexes et avancés. Une excellente analogie est que FreeCAD est structuré comme un coffre à outils roulant de mécanicien, et que chaque atelier est un tiroir d\'outils spécifiques. Vous pouvez utiliser ces outils pour construire une voiture, mais c\'est au mécanicien de comprendre comment les utiliser pour atteindre son objectif.

### \"FreeCAD est totalement cassé, mes modèles explosent !\" 

FreeCAD est construit autour d\'un noyau de modélisation géométrique open-source appelé \"[OpenCascade Technology](OpenCASCADE/fr.md)\" (ou OCC). Il s\'agit du noyau de modélisation open source le plus riche en fonctionnalités et le plus mature qui soit. Cependant, il présente des bogues, des bizarreries et des limitations. L\'un d\'entre eux est appelé le [\"Problème de dénomination topologique\"](Topological_naming_problem/fr.md) (ou Topological Naming Problem = TNP). Chaque fois qu\'un modèle est modifié, les noms internes des faces et des arêtes sont changés par le noyau, ce qui entraîne un comportement indésirable pour toutes les fonctionnalités du modèle qui y font référence. Le cycle de développement actuel est axé sur l\'implémentation d\'un algorithme de dénomination conçu pour atténuer cet effet dans la plupart des circonstances. Cependant, soyez conscient que l\'atténuation du TNP ne remplace pas [bonnes pratiques et techniques de modélisation](Feature_editing/fr.md).

## Noyau OpenCascade 

OpenCascade (OCC) est un noyau externe de CAO dont FreeCAD est totalement dépendant. Il y a de nombreux bogues ouverts \"en amont\" que la communauté FreeCAD a identifié et suit concernant OCC. Voir :

-   [Bugtracker](https://github.com/FreeCAD/FreeCAD/issues?q=is%3Aopen+is%3Aissue+label%3A%223rd+Party%3A+OCC%22)
-   [Bugs OCC dans le Bugtracker (fil du forum)](https://forum.freecad.org/viewtopic.php?t=20264)

## Liens supplémentaires 

-   [Discussion : FreeCAD n\'est pas prêt pour la 1.0 (fil du forum)](https://forum.freecadweb.org/viewtopic.php?f=8&t=43461)
-   [Pourquoi l\'équipe GIMP vous déteste manifestement\* (\*En fait, nous vous aimons. \*\*Principalement)](https://www.youtube.com/watch?v=JBmdbipkbrk) Pat David de la présentation de l\'équipe GIMP à SCaLE16x Californie 2016
-   [Gagner votre soutien au lieu de l\'acheter : un guide pratique de l\'assistance en matière de code source ouvert](https://vimeo.com/144089061) par [Ian Turton](https://twitter.com/ijturton) à la conférence FOSS4G Seoul 2015.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > FreeCAD Managing Expectations/fr
