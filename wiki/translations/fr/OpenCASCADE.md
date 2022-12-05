# OpenCASCADE/fr
{{TOCright}}

## Description

[OpenCASCADE Technology](OpenCASCADE/fr.md), **OCC** ou **OCCT** pour faire court, est une collection de bibliothèques C ++ qui constituent ensemble un noyau professionnel de conception assistée par ordinateur (CAO) pour la modélisation 2D et 3D objets et la construction d\'outils spécialisés pour la fabrication, la simulation ou la visualisation. OpenCASCADE est le cœur des fonctionnalités géométriques de FreeCAD.

Les classes géométriques d\'OCCT sont pour la plupart implémentées et rendues disponibles dans FreeCAD via l\'[atelier Part](Part_Workbench/fr.md), dont dépendent la plupart des autres [ateliers](Workbenches/fr.md). Il fournit également des fonctions internes pour lire et écrire différents formats de fichiers comme STEP et IGES, et pour effectuer des projections 2D, qui peuvent être utilisées pour créer des dessins techniques dans l\'[atelier TechDraw](TechDraw_Workbench/fr.md).

<img alt="" src=images/Part_Workbench_relationships.svg  style="width:600px;">



*OpenCASCADE fournit les classes géométriques de base et les fonctions de dessin à l'[atelier Part](Part_Workbench/fr.md) qui sont ensuite utilisées par tous les ateliers de FreeCAD.*

OpenCASCADE ne doit pas être confondu avec [OpenSCAD](https://www.openscad.org/), qui est un autre projet open source pour construire des modèles 3D et qui est accessible via l\'[atelier OpenSCAD](OpenSCAD_Workbench/fr.md).

OpenCASCADE est un logiciel libre régi par les termes de la GNU Lesser General Public License (LGPL) version 2.1 avec une exception supplémentaire.

## Installation

OpenCASCADE est un composant central de FreeCAD, donc si vous installez FreeCAD à partir de l\'un des liens de la page [Téléchargement](Download/fr.md), vous l\'aurez installé et aucune autre installation n\'est nécessaire.

Cependant, si vous souhaitez développer des applications qui utilisent OCCT ou si vous souhaitez contribuer au code C ++ à FreeCAD, vous devez installer les fichiers de développement d\'OCCT. Dans ce cas, la procédure est expliquée dans [Compilation](Compiling/fr.md) pour chacun des principaux systèmes, Linux, Windows et MacOS.

## Édition communautaire 

Une \"édition communautaire\" d\'OpenCASCADE, abrégée OCE, a été publiée en 2011, basée sur les sources officielles d\'OpenCASCADE (OCCT) de la version 6.5. En théorie, l\'édition communautaire OCE devrait être compatible avec la version principale OCCT dans la plupart des aspects, tout en ayant du code supplémentaire fourni par la communauté.

Cependant, cette distribution alternative a arrêté le développement actif vers 2017 et a pris du retard par rapport à la version principale en termes de fonctionnalités et de corrections de bogues. Pour cette raison, depuis FreeCAD v0.17, FreeCAD est compilé exclusivement avec OCCT et OCE n\'est pas testé.

Dans certaines distributions Linux plus anciennes, FreeCAD est compilé avec OCE 0.18, équivalent à OCCT 6.9.x, causant divers problèmes qui ont déjà été résolus dans les principales versions d\'OCCT 7.x. Si tel est le cas, essayez de supprimer OCE et d\'installer OCCT à la place. Si ce n\'est pas possible, utilisez [AppImage](AppImage/fr.md) pour obtenir un FreeCAD récent avec une version OCCT mise à jour.

## Histoire

Le noyau géométrique Cas.CADE était à l\'origine fermé, mais il est devenu open source sous son nom actuel vers l\'an 2000. Peu de temps après, le projet FreeCAD a été lancé, les fichiers les plus anciens datant de janvier 2001. En savoir plus dans [Histoire](History/fr.md).

La version 6.6 d\'OpenCASCADE et les versions antérieures étaient régies par sa propre \"licence publique OCCT\", ce qui en faisait un \"logiciel libre\". Ce problème a été résolu avec la sortie d\'OCCT 6.7 (2013), lors de l\'adoption de la licence LGPL2.

## OCCT concepts géométriques 

Dans la terminologie OpenCascade, nous faisons la distinction entre les primitives géométriques et les formes (topologiques). Une primitive géométrique peut être un point, une ligne, un cercle, un plan, etc. ou même certains types plus complexes, comme une courbe B-Spline ou une surface. Une forme (shape en anglais) peut être un sommet, une arête, un fil, une face, un solide ou un composé d\'autres formes. Les primitives géométriques ne sont pas faites pour être affichées directement sur la scène 3D, mais plutôt pour être utilisées comme géométrie de construction des formes. Par exemple, une arête peut être construite à partir d\'une ligne ou d\'une partie de cercle.

Pour résumer, les primitives géométriques sont des blocs de construction \"informes\", tandis que les [entités géométriques spatialessont](Part_TopoShape/fr.md) les véritables formes construites sur ces blocs.

Une liste complète de toutes les primitives et formes se réfère à la [documentation OCC](https://dev.opencascade.org/resources/documentation) (Alternative: [sourcearchive.com](https://www.opencascade.com/doc/occt-7.4.0/refman/html/)) et recherchez **Geom\_\*** (pour les primitives géométriques) et **TopoDS\_\*** (pour les formes). Là, vous pouvez également en savoir plus sur les différences entre eux. Veuillez noter que la documentation officielle de l\'OCC n\'est pas disponible en ligne (vous devez télécharger une archive) et est principalement destinée aux programmeurs, pas aux utilisateurs finaux. Mais j\'espère que vous trouverez suffisamment d\'informations pour commencer ici. Voir également [Guide de l\'utilisateur des données de modélisation](https://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__modeling_data.html).

> *À un niveau très élevé, la topologie indique de quelles pièces un objet est fait et les relations logiques entre elles. Une forme est constituée d\'un certain ensemble de faces. Une face est délimitée par un certain ensemble d\'arêtes. Deux faces sont adjacentes si elles partagent une arête commune.*

> *La topologie seule ne vous indique pas la taille, la courbure ou les emplacements 3D de ces pièces. Cependant, chaque élément de la topologie connaît sa géométrie sous-jacente. Une face sait sur quelle surface elle se trouve. Un bord sait sur quelle courbe il se trouve. La géométrie connaît la courbure et l\'emplacement dans l\'espace.* - [Source](https://www.opencascade.com/content/geometry-and-topology)


<hr />

> *Ainsi, la topologie définit la relation entre des entités géométriques simples qui peuvent être liées entre elles pour représenter des formes complexes.* - [Modeling Data User\'s Guide](https://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__modeling_data.html)

![](images/ClassTopoDS_Shape_inherit_graph.png )

**Remarque :** Seuls 3 types d\'objets topologiques ont des représentations géométriques - sommet, arête et face ([Source](https://opencascade.blogspot.com/2009/02/topology-and-geometry-in-open-cascade.html)).

Les types géométriques peuvent en fait être divisés en deux groupes principaux: les courbes et les surfaces. Sur les courbes (ligne, cercle\...) vous pouvez directement créer une arête, sur les surfaces (plan, cylindre\...) une face peut être construite. Par exemple, la ligne primitive géométrique est illimitée, c\'est à dire qu\'elle est définie par un vecteur de base et un vecteur directeur tandis que la forme associée (et représentée) doit être quelque chose de limité par un début et de fin. Et un cube \-- un solide \-- peut être créée par six plans limités.

A partir d\'une arête ou d\'une face, on peut aussi revenir à son équivalent géométrique primitif.

Ainsi, à partir de formes, vous pouvez créer des pièces très complexes ou, inversement, extraire toutes les sous-formes dont une forme plus complexe est constituée.

<img alt="" src=images/Part_TopoShape_relationships.svg  style="width:600px;">



*La classe `Part::TopoShape* est l'objet géométrique visible à l'écran. Essentiellement, tous les ateliers utilisent ces [TopoShapes](Part_TopoShape/fr.md) en interne pour créer et afficher des arêtes, des faces et des solides.`

## En relation 

-   OpenCASCADE Technology (OCCT) [site principale](http://www.opencascade.com)
-   OCCT [portail de développement](https://dev.opencascade.org/)
-   OCCT [dernière version](https://www.opencascade.com/content/latest-release)
-   OCCT [dépôt git](https://git.dev.opencascade.org/gitweb/?p=occt.git)
-   OpenCASCADE Community Edition (OCE) [dépôt git](https://github.com/tpaviot/oce)
-   [Open Cascade Technology OCCT](https://fr.wikipedia.org/wiki/Open_CASCADE_Technology) sur Wikipedia
-   Glossaire, [Open CASCADE](Glossary/fr#Open_CASCADE.md)
-   Suivi des bogues OCCT dans le bugtracker de FreeCAD [(fil du forum)](https://forum.freecadweb.org/viewtopic.php?f=10&t=20264)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > OpenCASCADE/fr
