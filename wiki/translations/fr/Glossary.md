# Glossary/fr
Cette page est le glossaire des termes et définitions fréquemment utilisées dans FreeCAD.

Aller à la lettre : {{CompactTOC|center=yes}}

## 0-9


{{gloss}}


{{term|3D view|content=[3D view](3D_view/fr.md)}}


{{defn|defn=La vue 3D est un composant de l'[interface](Interface/fr.md) de FreeCAD. Elle montre une représentation 3D du modèle.}}


{{glossend}}

## A


{{gloss}}


{{term|term=Arc}}


{{defn|defn=Une portion ou segment d'un cercle.}}


{{term|App}}


{{defn|defn=La couche App de FreeCAD.}}


{{term|Arch|content=[Arch](Arch_Workbench/fr.md)}}


{{defn|defn=Abréviation de l'[atelier](#Workbench.md) d'architecture, qui sert principalement à modéliser des bâtiments et des structures. Elle est étroitement liée à l'atelier [Draft](#Draft.md).}}


{{term|Assembly|content=[Assembly](Assembly/fr.md)}}


{{defn|no=1|defn=Un ensemble de [pièces](#Part.md) qui ont des positions définies les unes par rapport aux autres.}}


{{defn|no=2|defn=Un [atelier](#Workbench.md) qui vise à faciliter la création d'assemblages. FreeCAD ne dispose pas actuellement d'un tel atelier intégré, mais il existe plusieurs [ateliers externes d'assemblage](External_workbenches/fr.md).}}


{{term|Axes}}


{{defn|defn=Pluriel de [Axis](#Axis.md)}}


{{term|Axis}}


{{defn|defn=Ligne imaginaire passant par l'origine de l'espace de travail. Il existe 3 axes normaux. Ils portent les noms classiques de X, Y et Z. X correspond à un déplacement latéral. Y est le haut et le bas. Z représente l'entrée et la sortie de la page/de l'écran.}}


{{glossend}}

## B


{{gloss}}


{{term|Backtrace}}


{{defn|defn=Sortie d'un programme de débogage qui affiche une série d'instrucion que  FreeCAD suivait avant qu'un problème ne survienne.}}


{{term|Bezier Curve|content=[https://fr.wikipedia.org/wiki/Courbe_de_B%C3%A9zier Bezier Curve]}}


{{defn|defn=Un type de courbe paramétrique.}}


{{term|Blueprint}}


{{defn|defn=Ancien terme utilisé pour une feuille de dessin ([Drawing](#Drawing.md)), et désigné par son [https://fr.wikipedia.org/wiki/Blueprint procédé de reproduction Blueprint].}}


{{term|Body}}


{{defn|defn=Corps de pièce. Un type de container utilisé dans l'[atelier](#Workbench.md) [PartDesign](PartDesign_Workbench.md) et qui regroupe une séquence d'opérations ([esquisses](#Sketch.md), géométrie de construction et [fonctions](#Feature.md)) pour créer un solide unique contigu. (Introduit dans FreeCAD V0.17.)}}


{{term|Boolean Logic}}


{{defn|defn=Une méthode de manipulation de données utilisé dans les opérandes : And, Or, Not (et, ou, pas).}}


{{term|Boolean Operation}}


{{defn|defn= Méthode de manipulation d'objets en utilisant la logique Booléenne. Dans FreeCAD, les opérations Booléennes sont : [Union](#Fuse.md), [Différence](#Cut.md), Intersection, et Section.}}


{{term|Boolean OPerations check}}


{{defn|defn=Voir [BOPcheck](#BOPcheck.md).}}


{{term|BOPcheck}}


{{defn|defn=Paramètre permettant aux outils Check Geometry des ateliers Part et OpenSCAD de vérifier également la géométrie créée à partir de la [logique booléenne](#Boolean_Logic.md). Le paramètre par défaut de BOPcheck est "false" (ou désactivé). L'utilisateur peut activer BOPcheck pour obtenir plus de précision lors de l'exécution de l'outil Check Geometry, mais cela se fait au détriment de délais de traitement plus longs. À partir de FreeCAD 0.19, le paramètre BOPcheck est plus facilement activable à partir de la partie Paramètres du widget Check Geometry.}}


{{term|brep}}


{{defn|defn=Format de fichier natif [Open CASCADE](#Open_CASCADE.md) partagé et utilisé par beaucoup d'applications. FreeCAD peut sauver des fichiers dans le format *.brep.}}


{{term|B-rep}}


{{defn|defn=Standard pour une [http://fr.wikipedia.org/wiki/B-Rep représentation par les bords], qui est l'un des deux types de représentation en 3D que supporte FreeCAD (l'autre étant [mesh](#Mesh.md)).}}


{{term|B-spline}}


{{defn|defn=Un type de courbe paramétrique. Voir [https://fr.wikipedia.org/wiki/Spline Spline] et [http://fr.wikipedia.org/wiki/B-spline B-spline]}}


{{glossend}}

## C


{{gloss}}


{{term|Callout}}


{{defn|defn=Chaîne ou texte connecté à une ligne pointant sur un objet dans le [dessin](#Drawing.md).}}


{{term|Chamfer}}


{{defn|defn=Coupure d'un bord avec un angle donné, en vue de le transformer en biseau (chanfrein).}}


{{term|1=Clipping Plane}}


{{defn|defn=Le plan de coupe est utilisé pour obtenir une vue en coupe de l'objet dans la vue 3D. C'est juste une aide visuelle qui ne fait aucune modification sur la forme l'objet.}}


{{term|Clone}}


{{defn|defn=C'est une copie d'un objet qui conserve un lien vers les paramètres de l'original. Lorsque l'objet original est modifié, le clone change aussi et adopte toutes les modifications apportées à l'objet original auquel il reste attaché.}}


{{term|Coin}}


{{defn|defn=Aussi appelé Coin3D. Bibliothèque logicielle utilisée par FreeCAD pour la représentation 3D.}}


{{term|COLLADA}}


{{defn|defn=Un format de fichier interchangeable pour le modèle de [maillage](#Mesh.md). L'extension du fichier est *.dae.}}


{{term|Command|content=[Command](Command/fr.md)}}


{{defn|defn=Commande. Une action invoqué depuis la [GUI](#GUI.md) (interface graphique) en cliquant un bouton ou en tappant un raccourcis clavier ou tapé directement dans la console Python.}}


{{term|Compound}}


{{defn|defn=Groupe d'objets réunis entre eux sans utiliser d'opération [booléenne](#Boolean_Operation.md) de fusion.}}


{{term|CompSolid}}


{{defn|defn=Solide composé. Ensemble de [solides](#Solid.md) connectés par leurs [faces](#Face.md). Les solides composés sont nécessaires dans les simulations par éléments finis ([FEM](#FEM.md)) où plusieurs matériaux sont utilisés au sein d'un seul maillage FEM.}}


{{term|Constraint}}


{{defn|defn=Si une contrainte a une valeur, elle est désignée comme référence (par exemple, une contrainte de distance a une valeur - la longueur d'une ligne imaginaire reliant les deux points). Une contrainte qui n'a pas de valeur est parfois appelé géométrique.}}


{{term|Constructive Solid Geometry|content=[https://fr.wikipedia.org/wiki/G%C3%A9om%C3%A9trie_de_construction_de_solides Constructive Solid Geometry]}}


{{term|Coordinate}}


{{defn|defn=Un nombre défini de positions d'un objet dans l'espace en faisant référence au [http://fr.wikipedia.org/wiki/Coordonn%C3%A9es_cart%C3%A9siennes système cartésien de coordonnées].}}


{{term|Coplanar}}


{{defn|defn=Qui se situe dans le même plan.}}


{{term|CSG}}


{{defn|defn=Raccourci pour [Constructive Solid Geometry](#Constructive_Solid_Geometry.md) en Français : Géométrie de construction de solides.}}


{{term|Cut}}


{{defn|defn=Appliquer une [différence booléenne](#Boolean_Operation.md) entre objets.}}


{{glossend}}

## D


{{gloss}}


{{term|DAG}}


{{defn|defn=Voir [Directed Acyclic Graph.](#Directed_Acyclic_Graph.md) (Graphe Orienté Acyclique)}}


{{term|Degrees Of Freedom}}


{{defn|defn=Degrés de Liberté. Le nombre de manières dont une géométrie d'[esquisse](#Sketch.md) peut varier. Par exemple, si nous avons une esquisse constituée de seulement un point, et qu'à ce point aucune [contrainte](#Constraint.md) n'a été appliquée, alors ce point a deux [DOF](#DOF.md). En effet, il est libre de se déplacer à la fois verticalement et horizontalement. De la même manière, une esquisse constituée d'un unique cercle non contraint a trois [DOF](#DOF.md) parce que ce cercle est libre de se déplacer à la fois verticalement et horizontalement et son rayon peut varier. C'est une bonne pratique de contraindre une esquisse jusqu'à ce qu'elle ne présente plus aucun [DOF](#DOF.md), dans ce cas, on dit qu'elle est [entièrement contrainte](#Fully_Constrained.md).}}


{{defn|defn=Outil graphique tiers utilisé pour montrer comment les objets d'un modèle FreeCAD sont utilisés ou sont liés les uns aux autres. Pour plus d'informations, reportez-vous à la page [Graphique de dépendance](Std_DependencyGraph/fr.md).}}


{{term|Difference}}


{{defn|no=1|defn=Le résultat, ou reste, après une soustraction.}}


{{defn|no=2|defn=Une [opération booléenne](#Boolean_operation.md) dans l'atelier Part qui soustrait une géométrie d'une autre; son résultat apparaît comme une [différence](#Cut.md).}}


{{term|Directed Acyclic Graph}}

(acronyme : \"DAG\") {{defn|defn=Un type de [graphe de dépendance](#Dependency_Graph.md) où les relations entre objets s'organisent de façon linéaire, du début à la fin, sans aucune dépendance circulaire. Si l'on parcourt un "DAG" on ne trouvera pas de chemin, ou relation, d'un objet A vers un ou plusieurs autres objets qui puisse revenir vers l'objet A. Dans FreeCAD, le graphe d'un modèle doit toujours être un "DAG".}} {{term|DOF}} {{defn|defn=[Degrees Of Freedom](#Degrees_Of_Freedom.md)}} {{term|Draft|content=[Draft](Draft_Workbench/fr.md)}} {{defn|no=1|defn=Un [atelier](#Workbench.md) de FreeCAD utilisé principalement pour le travail en 2 dimensions.}} {{defn|no=2|defn=Angle de dépouille sur un moule afin de permettre le démoulage du produit final. Voir [PartDesign Dépouille](PartDesign_Draft/fr.md).}} {{term|Drawing}} {{defn|defn=Décrit une représentation de la géométrie par l'utilisation de vues bidimensionnelles. Également appelé plan ou [blueprint](#Blueprint.md).}} {{glossend}}

## E


{{gloss}}


{{term|Edge}}


{{defn|no=1|defn=Un segment joignant deux [points](#Vertices.md). Ce segment peut être une ligne droite ou une courbe. Le [noyau de modélisation géométrique](#Geometric_modeling_kernel.md) définit un segment de la façon suivante : une forme à une dimension correspondant à une courbe et limitée à chaque extrémité par un vertex. Ainsi un cercle fermé n'a qu'un seul vertex qui constitue à la fois son début et sa fin. Voir [https://dev.opencascade.org/doc/overview/html/occt__tutorial.html#OCCT_TUTORIAL_SUB2_3 "Open CASCADE Technology, Profile: Defining the Topology"].}}


{{defn|no=2|defn=Ligne de jonction entre deux faces. Elle peut être une droite ou une courbe.}}


{{term|Element}}


{{defn|defn=Un élément d'une géométrie d'esquisse comme un point, une ligne, un arc, un cercle, etc.}}


{{term|Expression}}


{{defn|no=1|defn=Terme général utilisé en mathématiques et en programmation.}}


{{defn|no=2|defn=Dans FreeCAD, les [expressions](Expressions/fr.md) sont utilisées pour calculer des valeurs. Elles peuvent référencer et piloter les propriétés des objets. Elles sont utilisées dans les [feuilles de calcul](Spreadsheet_Workbench.md) et pour contrôler les modèles paramétriques.}}


{{term|Extrude}}


{{defn|defn=Terme général désignant l'extension d'un objet 2D en 3D dans une direction. Voir aussi [Pad](#Pad.md).}}


{{glossend}}

## F


{{gloss}}


{{term|1=Face}}


{{defn|defn=Un objet de construction topologique en 2 dimensions. Par exemple, un cube a 6 faces. une face peut être courbe, comme c'est le cas pour une sphère, qui, dans FreeCAD, n'a qu'une face. Le [noyau de modélisation géométrique](#Geometric_modeling_kernel.md) définit une face comme : la partie d'une surface limité par un ensemble fermé de [polylignes](#Wire.md). Voir [https://dev.opencascade.org/doc/overview/html/occt__tutorial.html#OCCT_TUTORIAL_SUB2_3 Profile: Defining the Topology].}}


{{term|Facet}}


{{defn|defn=Facette, souvant utilisé pour décrire les faces planes d'un [maillage](#Mesh.md).}}


{{term|FC}}


{{defn|defn=Abréviation de FreeCAD.}}


{{term|FCStd}}


{{defn|defn=Extension des fichiers de FreeCAD. Extension de fichier *.fcstd, *.FCStd (*.FCStd1 *.FCStd2 ..., sont des fichiers de sauvegardes)}}


{{term|1=Feature}}


{{defn|defn=Une étape dans l'évolution d'une pièce 3D dans le flux de travaux de l'[atelier](#Workbench.md) [PartDesign](PartDesign_Workbench/fr.md). Les exemples sont [Pad](#Pad.md), [Pocket](#Pocket.md), [Groove](#Groove.md), [Fillet](#Fillet.md), etc. Lorsque nous créons un modèle dans l'[atelier](#Workbench.md) [PartDesign](PartDesign_Workbench/fr.md), chaque fonction prend la forme de la dernière et ajoute ou supprime quelque chose. Par conséquent, une fonction "Pocket" n'est pas seulement le creux de la poche en lui même mais la totalité de la forme y compris la poche.}}


{{term|FEM|content=[FEM](FEM_Workbench/fr.md)}}


{{defn|defn=[https://fr.wikipedia.org/wiki/M%C3%A9thode_des_%C3%A9l%C3%A9ments_finis Méthode des Eléments Finis]. L'[atelier FEM](FEM_Workbench/fr.md) est utilisé pour résoudre des problèmes d'ingénierie et de physique associés aux pièces, aux assemblages et aux structures.}}


{{term|Fillet}}


{{defn|defn=Congé. C'est un arrondi de l'arête ou une coupe ajoutée sur l'arête pour que l'apparence finale de l'arête soit adoucie. Voir [Part Congé](Part_Fillet/fr.md) and [PartDesign Congé](PartDesign_Fillet/fr.md).}}


{{term|Fork}}


{{defn|defn=Voir Forked Model.}}


{{term|Forked Model}}


{{defn|defn=Une méthode de modélisation, habituellement accidentelle et incorrecte qui crée deux ou plusieurs versions d'un modèle à partir d'un élément précédent. (Ne doit pas être confondue avec des opérations volontaires réseau, clone, modèle polaire, etc.)}}


{{term|Frenet}}


{{defn|defn=Lors du balayage d'un profil sur une trajectoire en 3D, le paramètre Frenet commande l'orientation du profile qui se déplace le long du trajet. Si Frenet est vrai, les profils sont orientés en utilisant le cadre de Frenet (tangent, double perpendiculaire, perpendiculaire) du trajet. Si Frenet est faux la rotation du profil n'est pas limitée. [http://fr.wikipedia.org/wiki/Rep%C3%A8re_de_Frenet Repère de Frenet]}}


{{term|Freetype|content=[http://www.freetype.org FreeType]}}


{{defn|defn=Une librairie libre utilisée pour extraire les informations de la définition de la police de caractères.}}


{{term|Frustum}}


{{defn|defn=La partie d'un solide, [http://fr.wikipedia.org/wiki/Tronc_(géométrie) Tronc], qui se trouve entre deux plans parallèles le coupant. Utilisé en infographie pour décrire la région tridimensionnelle visible à l'écran, le [http://en.wikipedia.org/wiki/Viewing_frustum "viewing frustum"]}}

. {{term|Fully Constrained}} {{defn|defn=Entièrement contraint. Dans [Sketcher](#Sketcher.md), quand une [esquisse](#Sketch.md) n'a plus aucun [degré de liberté](#Degrees_Of_Freedom.md), elle est qualifiée comme "entièrement contrainte" par les [contraintes](#Constraint.md) qui lui sont appliquées.}} {{term|Fuse}} {{defn|defn=Terme couramment utilisé dans FreeCAD pour se référer à une [union booléenne](#Boolean_Operation.md) d'objets.}} {{glossend}}

## G


{{gloss}}


{{term|GDB ou gdb}}


{{defn|defn=[https://www.gnu.org/software/gdb/ '''G'''NU Project '''D'''e'''B'''ugger], un programme de débogage utilisé sous Unix et les systèmes similaires dans le but d'obtenir une trace d'appel ([backtrace](#Backtrace.md)) représentant l'état du processeur au moment d'un plantage. "gdb" (sans les guillemets) est aussi la première partie de la commande utilisée pour lancer le programme GDB lui même. Il y a un exemple d'utilisation de GDB avec FreeCAD dans [http://forum.freecadweb.org/viewtopic.php?t=7052#p56918 ce post sur le forum]}}


{{term|Geometric modeling kernel}}


{{defn|defn=Aussi appelé CAD kernel. Un ensemble de bibliothèques logicielles complexes responsables de la création de formes en 3D. Toutes les opérations sur les objets (extrusion, opérations booléennes, chanfrein, arrondi) s'appuient sur le kernel (noyau) de modélisation géométrique.}}


{{term|Git}}


{{defn|defn=[http://fr.wikipedia.org/wiki/Gestion_de_version_d%C3%A9centralis%C3%A9e#Gestion_de_versions_d.C3.A9centralis.C3.A9e Système de gestion de versions] utilisé par FreeCAD pour héberger et gérer le code source.}}


{{term|[Group](Std_Group/fr.md)}}


{{defn|defn=Utilisé pour organiser les éléments dans la [Vue en arborescence](Tree_view/fr.md)}}


{{term|GUI}}


{{defn|defn='''G'''raphical '''U'''ser '''I'''nterface. Permet aux utilisateurs d'interagir avec FreeCAD par l'intermédiaire d'icônes et de la souris.}}


{{glossend}}

## H


{{gloss}}


{{term|Half_Space|content=[https://fr.wikipedia.org/wiki/Demi-espace Half Space]}}


{{defn|defn=Quand un plan divise complètement un espace euclidien à trois dimensions, on obtient deux demi-espaces.}}


{{glossend}}

## I


{{gloss}}


{{term|IGES}}


{{defn|defn=Est un format de fichier utilisé pour l'échange de données. Les extensions de fichiers sont *.iges, *.igs. Voir aussi [STEP](#STEP.md).}}


{{term|Intersection|content=[https://fr.wikipedia.org/wiki/Intersection_(math%C3%A9matiques) Intersection]}}


{{defn|defn=La partie de deux ou plusieurs entités géométriques qui leur est commune. Par exemple, l'intersection de deux lignes est un point.}}


{{glossend}}

## J


{{gloss}}


{{term|JT}}


{{defn|defn=Un format de données 3D propriétaire développé par Siemens PLM Software. FreeCAD n'a pour le moment pas de support pour les JT en ce moment.}}


{{glossend}}

## K


{{gloss}}


{{term|Kernel}}


{{defn|defn=Voir [Noyau de modélisation géométrique](#Geometric_modeling_kernel.md).}}


{{term|KML}}


{{defn|defn=Keyhole Markup Language - est un fichier de données de définition géospatiale en 3D basé sur le format XML utilisé par Google Earth. FreeCAD n'a pas pour le moment de support pour le format KML.}}


{{glossend}}

## L


{{gloss}}


{{term|Label}}


{{defn|no=1|defn=Une propriété d'objet définie par l'utilisateur. Utilisé pour rendre la [vue en arborescence](Tree_view/fr.md) des modèles plus lisible.}}


{{defn|no=2|defn=Un texte descriptif ajouté à un dessin. (voir [Draft Etiquette](Draft_Label/fr.md)).}}


{{defn|defn=Ne pas confondre avec [Name](#Name.md).}}


{{term|Line}}


{{defn|defn =Le plus souvent, utilisé comme synonyme de [line segment](#Line_Segment.md). Dans Sketcher, parfois utilisé avec la signification exacte d’un chemin rectiligne infini.}}


{{term|Line Segment}}


{{defn|defn=Une trajectoire rectiligne entre deux [points](#Point.md).}}


{{term|Lock}}


{{defn|defn=[Contrainte fixe](Sketcher_ConstrainLock/fr.md)}}


{{term|Loft|content=[http://en.wikipedia.org/wiki/Loft_%283D%29 Loft]}}


{{defn|defn=Une forme topologique créée en reliant des profils consécutifs avec une surface. Identique au processus utilisé pour faire des avions ou des bateaux recouverts de tissu. FreeCAD utilise également cette fonction pour créer de telles formes.}}


{{glossend}}

## M


{{gloss}}


{{term|Macro}}


{{defn|defn=Une séquence d'instructions FreeCAD enregistrée, souvent écrits par les utilisateurs.}}


{{term|Manifold}}


{{defn|defn=Dit d'une [forme](#Shape.md) qui constitue un volume parfaitement fermé. Familièrement, on pourrait décrire cette forme comme étant "étanche". Pour générer un solide, une coque ([shell](#Shell.md)) doit être "manifold".}}


{{term|Mantis}}


{{defn|defn=[Bug tracking system](#Tracker.md) utilisé pour le projet FreeCAD.}}


{{term|Mesh}}


{{defn|defn=Type d'objet qui peut être importé ou exporté par FreeCAD. Voir [https://fr.wikipedia.org/wiki/Mesh_(objet) Maillage]}}


{{term|Model}}


{{defn|defn=Aussi appelé modèle 3D. Représentation informatique d'une [pièce](#Part.md) à trois dimensions ou d'un [assemblage](#Assembly.md).}}


{{term|MultiTransform|content=[MultiTransform](PartDesign_MultiTransform/fr.md)}}


{{defn|defn=Transformation multiple. Une [fonction](#Feature.md) de l'[atelier](#Workbench.md) [PartDesign](PartDesign_Workbench/fr.md) qui applique une série de transformations chaînées (motifs linéaires et circulaires, en miroir) aux entités sélectionnées.}}


{{glossend}}

## N


{{gloss}}


{{term|Name}}


{{defn|defn=Identifiant unique d'un objet dans un document FreeCAD. Une fois l'objet créé par le programme, un nom lui est attribué. Ce nom ne peut pas être changé, contrairement à[Label](#Label.md).}}


{{term|Non-manifold}}


{{defn|defn=La topologie non-manifold, également appelée épaisseur nulle, correspond à deux corps solides distincts connectés par un sommet ou une arête théorique. Il s'agit d'un type de forme non pris en charge (pas toujours détecté par FreeCAD) qui doit être évité car il peut entraîner des problèmes lors de nouvelles étapes et de l'exportation.}}


{{term|Null Shape}}


{{defn|defn=Une propriété d'une [forme](#Shape.md) qui n'a pas été initialisée par un programme ou une macro. Habituellement, c'est une condition déclenchant une erreur.}}


{{glossend}}

## O


{{gloss}}


{{term|OCC}}


{{defn|defn=Acronyme pour [Open CASCADE](#Open_CASCADE.md). Avant d'être passé en "open source", le nom était CAS.CADE (abréviation de "Computer Aided Software for Computer Aided Design and Engineering").}}


{{term|OCE}}


{{defn|defn='''O'''pen CASCADE '''C'''ommunity '''E'''dition. Cette édition fournit des correctifs, améliorations et expérimentations apportées par les utilisateurs sur la bibliothèque officielle d'[Open CASCADE](#Open_CASCADE.md). FreeCAD fonctionne avec soit OCC, soit OCE.}}


{{term|OCCT}}


{{defn|defn=Open CASCADE Technology. See [OCC](#OCC.md).}}


{{term|Open CASCADE|content=[http://www.opencascade.org Open CASCADE]}}


{{defn|defn=Le [geometric modeling kernel](#Geometric_modeling_kernel.md) est une librairie logicielle sous-jacente de FreeCAD. Aussi appelé [OCC](#OCC.md) or [OCCT](#OCCT.md) (pour Open CASCADE Technology). Voir aussi [OCE](#OCE.md).}}


{{term|OpenSCAD}}


{{defn|defn=Nom d'un logiciel de CAO avec lequel on construit les objets uniquement avec des scripts. C'est aussi un atelier de FreeCAD qui fournit une interface pour l'import/export de modèles *.scad et *.csg. Cet atelier fournit aussi quelques outils associés.}}


{{defn|no=1|defn=Nom d'un programme de CAO basé uniquement sur un script.}}


{{defn|no=2|defn=Un atelier dans FreeCAD. L'[atelier](#Workbench.md) [OpenSCAD](OpenSCAD_Workbench/fr.md)  fournit une interface pour l'importation/exportation des modèles * .scad et * .csg ainsi que des outils utiles.}}


{{term|Origin}}


{{defn|defn=Le centre du système de coordonnées. Tout se passe à partir de ce centre dans les directions positives ou négatives. Comme notre vision de l'univers avec comme "origine" la Terre.}}


{{term|Orthographic}}


{{defn|defn=[https://fr.wikipedia.org/wiki/Projection_orthogonale Projection orthogonale]. Une méthode de représentation d'un objet, à l'écran ou sur plans papier. Voir aussi [http://en.wikipedia.org/wiki/Multiview_orthographic_projection Multiview orthographic projection].}}


{{glossend}}

## P


{{gloss}}


{{term|Pad}}


{{defn|defn=Extension d'une [esquisse](#Sketch.md) dans une direction perpendiculaire au plan de l'Esquisse. Voir aussi [Extrude](#Extrude.md).}}


{{term|Part}}


{{defn|no=1|defn=[Atelier](#Workbench.md) de FreeCAD principalement utilisé pour un flux de travail de type [https://fr.wikipedia.org/wiki/Géométrie_de_construction_de_solides Construction  Géométrique de Solide]. Voir [Atelier Part](Part_Workbench/fr.md).}}


{{defn|no=2|defn=Un module Python de FreeCAD, s'interfaçant directement avec [OCC](#OCC.md). Voir [Part Script](Part_scripting/fr.md).}}


{{defn|no=3|defn=Un conteneur qui regroupe n'importe quel type d'objet FreeCAD et possède un [placement](#Placement.md). Voir [Std Part](Std_Part/fr.md).}}


{{defn|no=4|defn=Un solide unicorps. Le composant de niveau le plus bas dans un assemblage.}}


{{term|PartDesignNext}}


{{defn|defn=Surnom utilisé sur les forums pour faire une différence entre l'[atelier](#Workbench.md) [PartDesign](PartDesign_Workbench/fr.md) de la version FreeCAD 0.17 de celui des versions v0.16 et antérieures, ceci en raison de la grande quantité de changements introduits dans l'atelier PartDesign de la version 0.17.}}


{{term|PD}}


{{defn|defn=Abréviation de [PartDesign](PartDesign_Workbench/fr.md), un [atelier](#Workbench.md) de FreeCAD.}}


{{term|PDN}}


{{defn|defn=Abréviation de [PartDesignNext](#PartDesignNext.md).}}


{{term|Perspective}}


{{defn|defn=[http://fr.wikipedia.org/wiki/Perspective_axonométrique Perspective axonométrique]}}


{{term|Pivy|content=[http://pypi.python.org/pypi/Pivy Pivy]}}


{{defn|defn=Une bibliothèque logicielle qui permet d'utiliser Python Coin.}}


{{term|Placement}}


{{defn|defn=Ensemble des propriétés d'un objet définissant ses coordonnées et son orientation dans l'espace. Voir [Placement](Placement/fr.md).}}


{{term|Planar}}


{{defn|defn=Dit d'une géométrie dont tous les éléments constitutifs font partie du même plan.}}


{{term|Plane}}


{{defn|no=1|defn=Une surface plate, à deux dimensions et qui s'étend à l'infini.}}


{{defn|no=2|defn=Une [primitive](#Primitive.md) à deux dimensions créé dans l'[atelier](#Workbench.md) [Part](Part_Workbench/fr.md).}}


{{term|Plot}}


{{defn|no=1|defn=Synonyme désuet de dessin technique réalisé par un traceur à stylo. Voir [https://fr.wikipedia.org/wiki/Traceur_(informatique) Plotter]}}


{{defn|no=2|defn=Abréviation de plot plan. Voir [https://fr.wikipedia.org/wiki/Document_d%27urbanisme Plan de site]}}


{{defn|no=3|defn=Représentation graphique de données. Voir [https://fr.wikipedia.org/wiki/Repr%C3%A9sentation_graphique Plot (graphiques)]}}


{{term|1=Pocket}}


{{defn|defn=Une [fonction](#Feature.md), appelée poche en mécanique, qui enlève de la matière d'un solide en se servant des contours d'une ([esquisse](#Sketch.md)).}}


{{term|1=Point}}


{{defn|defn=Un élément utilisé pour faire référence à un endroit unique dans l'espace de travail 3D. Un "point" n'a pas de dimension. Il a une dimension à l'écran, généralement représenté par un "point" que nous pouvons voir à son emplacement. Voir aussi [Vertex](#Vertex.md).}}


{{term|Polygon mesh}}


{{defn|defn=Voir [http://fr.wikipedia.org/wiki/Mesh_%28objet%29 Mesh (objet)]}}


{{term|Polyline}}


{{defn|defn=Une série de segments de droite ou d'arc connectés entre eux.}}


{{term|POV-Ray}}


{{defn|defn=[http://fr.wikipedia.org/wiki/POV-Ray POV-Ray] Moteur de rendu par lancer de rayons.}}


{{term|PPA}}


{{defn|defn=Acronyme de '''P'''ersonal '''P'''ackage '''A'''rchive. c'est un type d'entrepôt de logiciels, spécifique à la distribution Linux Ubuntu . Le projet FreeCAD propose sa dernière version stable ainsi que des versions de développement au travers de deux entrepots PPA. Lorsqu'on utilise un PPA, les mises à jour du logiciel sont gérées par le système de mise à jour du système d'exploitation.}}


{{term|Primitive}}


{{defn|defn=Forme de base utilisée dans la construction d'un objet. Certaines primitives 2D sont : point, ligne, polygone, cercle, ellipse, spirale, hélice. Les primitives 3D sont : cube, cylindre, cône, tore, sphère, ellipsoïde, prisme.}}


{{term|PySide|content=[https://wiki.qt.io/PySide PySide]}}


{{defn|defn=Librairie libre et gratuite qui permet d'utiliser Python avec QT.}}


{{term|Python|content=[http://www.python.org Python]}}


{{defn|defn=Python est un des langages de programmation utilisés pour le développement de FreeCAD ainsi que par les utilisateurs programmeurs de [macros](#Macro.md) ou de petits scripts.}}


{{glossend}}

## Q


{{gloss}}


{{term|Qt|content=[https://www.qt.io/developers/ Qt]}}


{{defn|defn=QT est une application gratuite multi-plateforme pour la création d'interfaces utilisateur.}}


{{glossend}}

## R


{{gloss}}


{{term|Raytracing}}


{{defn|defn=[http://fr.wikipedia.org/wiki/Lancer_de_rayon Lancer de rayon]}}


{{term|Revolve}}


{{defn|defn=Outil disponible dans l'[atelier](#Workbench.md) [Part](Part_Workbench/fr.md). Voir [Part Révolution](Part_Revolve/fr.md).}}


{{term|Robot}}


{{defn|defn=[http://fr.wikipedia.org/wiki/Robotique_industrielle Robotique industrielle]}}


{{term|Rotate}}


{{defn|defn=Action consistant à faire pivoter un objet autour d'un axe pour changer son orientation dans l'espace.}}


{{glossend}}

## S


{{gloss}}


{{term|Section}}


{{defn|defn=[https://fr.wikipedia.org/wiki/Dessin_technique#Repr%C3%A9sentations_codifi%C3%A9es Vues en coupe]}}


{{term|Self Intersection}}


{{defn|defn=Une auto-intersection arrive quand par exemple une polyligne ou une courbe se croise elle même (ex.'8','&'). Cela perturbe les algorithmes du noyau géométrique et produit généralement une condition d'erreur.}}


{{term|Shape}}


{{defn|defn=Forme. Terme générique utilisé dans FreeCAD pour décrire la plupart des éléments à l'exception des [maillages](#Mesh.md).}}


{{term|Shell}}


{{defn|defn=Coque. Forme faite de une ou plusieurs [faces](#Face.md) contiguës. Une coque fermée [manifold](#Manifold.md) peut être convertie en un [solide](#Solid.md).}}


{{term|Sketch}}


{{defn|defn=Esquisse. Une représentation 2D d'un objet contraint et fixé sur un plan ou une [face](#Face.md). Dans FreeCAD une esquisse est toujours un objet en 2 dimensions, quelque part dans l'espace 3D.}}


{{term|Sketcher|content=[Sketcher](Sketcher_Workbench/fr.md)}}


{{defn|L'[atelier](#Workbench.md) utilisé pour créer des formes géométriques 2D utilisant des [éléments](#Element.md) et des [contraintes](#Constraint.md).}}


{{term|Sketcher Solver}}


{{defn|defn=Solveur de Sketcher, mécanisme interne de FreeCAD qui calcule les interdépendances et les effets de l'ajout, la suppression et la modification de la géométrie et des contraintes associées dans chaque esquisse. Le solveur calcule également l'agencement de toute la géométrie dans chaque esquisse de sorte qu'elle peut être affichée correctement.}}


{{term|Smooth Line}}


{{defn|defn=Dans un dessin, une ligne indiquant un changement entre des surfaces tangentes, comme dans la transition d'une surface plane avec un congé. Voir aussi "bord tangent". Voir [http://www.freecadweb.org/wiki/index.php?title=Drawing_View/fr#Modifier_une_vue_existante Drawing View - Modifier une vue existante]}}


{{term|Solid}}


{{defn|defn=Solide. Partie de l'espace 3D délimitée par des ([coques](#Shell.md)). Un solide a un volume et possède d'autre propriétés propres aux objets dont la masse.}}


{{term|Solver}}


{{defn|defn=Voir [Sketcher Solver](#Sketcher_Solver/fr.md).}}


{{term|Stable}}


{{defn|defn=Un surnom pour la dernière version générale du logiciel FreeCAD. C'est typiquement la version disponible à partir de sources autres que le projet FreeCAD. Comparer avec [Instable](#Unstable.md).}}


{{term|STL}}


{{defn|Format de description de la surface d'objet 3D en [maillage](#Mesh.md) de triangles ''Standard Tessellation Language''. L'extension du fichier est *.stl}}


{{term|STEP}}


{{defn|defn=Norme ISO (ISO 10303) pour l'échange de données 3D et d'informations sur la fabrication de produits. Il remplace [IGES](#IGES.md). Les extensions des fichiers sont *.step, *.stp.}}


{{term|SVG|content=[SVG](SVG/fr.md)}}


{{defn|[https://fr.wikipedia.org/wiki/Scalable_Vector_Graphics '''S'''calable '''V'''ector '''G'''raphics]. Est un format de fichier de graphisme vectoriel.}}


{{term|Sweep}}


{{defn|defn=Une forme 3D générée à partir d'au moins une section et d'une trajectoire. Le terme est généralement utilisé pour décrire à la fois l'outil et la forme générée. Voir [http://en.wikipedia.org/wiki/Solid_modeling#Sweeping Solid Modeling - Sweeping].}}


{{glossend}}

## T


{{gloss}}


{{term|Task panel}}


{{defn|defn=Un [https://fr.wikipedia.org/wiki/Composant_d%27interface_graphique panneau de commande] dans FreeCAD qui affiche un contenu spécifique à la tâche en cours. Il peut afficher les outils disponibles dans l'[atelier](#Workbench.md) actif ou demander des valeurs et des options pendant qu'une [commande](#Command.md) est active.}}


{{term|Tasks tab}}


{{defn|defn=Voir [Task panel](#Task_panel.md).}}


{{term|Tessellation}}


{{defn|defn=La tessellation (ou pavage) d'une surface est la partition de cette surface utilisant une ou plusieurs formes géométriques appelées tuiles, ces tuiles ne doivent pas se chevaucher est doivent être jointives. Dans FreeCAD, la représentation des formes géométriques dans la vue 3D utilise la tesselation. Cette tessellation est relative aux dimensions de la forme et peut être modifiée dans les préferences afin d'obtenir une vue plus douce des surfaces arrondies. Cela peut générer des temps de calculs plus long pour l'affichage. Voir [Réglage des préférences](Preferences_Editor/fr.md).}}


{{term|Thickness}}


{{defn|no=1|defn=L'épaisseur d'une forme.}}


{{defn|no=2|defn=Outil de l'[atelier](#Workbench.md) [Part](Part_Workbench/fr.md) utilisé pour évider un solide et laisser une épaisseur uniformément définie.}}


{{term|Toggle}}


{{defn|defn=Un paramètre qui prend une valeur parmi deux, par exemple "vrai" ou "faux" ou encore "activé" ou "désactivé".}}


{{term|Topological Naming}}


{{defn|defn=Nommage Topologique. Le procédé selon lequel une arrête ou une face reçoit un nom définitif lors de sa création. Dans son fonctionnement interne, FreeCAD identifie les arêtes et les faces d'un solide en les numérotant; par exemple : Edge1, Edge2, Face1, Face2, etc. Le problème est que la méthode d'attibution de ces identifiants est peu robuste et il s'en suit qu'ils peuvent changer si une manipulation sur l'objet modifie le nombre d'arêtes ou de faces. Par exemple, si le modèle est lié à une Face2, il pourra plus tard se retrouver par erreur lié à une autre face qui serait devenue la nouvelle Face2. Ceci provoque des résultats qui ne sont pas souhaités. Dans FreeCAD version 0.20 le nommage topologique n'est pas encore implémenté, donc si un objet est modifié de telle sorte que son nombre d'arrête ou de face change, le nom de ces arêtes et ces faces peut changer aussi de façon inattendue.}}


{{term|Torus}}


{{defn|defn=Tore : une forme primitive.}}


{{term|Tracker}}


{{defn|defn=Abréviation de bug tracker, application logicielle en ligne utilisée pour assurer le suivi des bogues signalés ou des demandes de fonctionnalités. Voir aussi [Mantis](#Mantis.md).}}


{{term|Tree view|content=[Tree view](Tree_view/fr.md)}}


{{defn|defn=La vue en arborescence est un composant de l'[interface](Interface/fr.md) de FreeCAD. Elle peut être affichée comme un élément séparé de la [GUI](#GUI.md) ou comme une partie de la [vue combinée](Combo_view/fr.md). Elle contient une représentation de la structure du document.}}


{{glossend}}

## U


{{gloss}}


{{term|Union}}


{{defn|defn=Un outil de l'[atelier](#Workbench.md) [Part](Part_Workbench/fr.md) qui réalise une [opération booléenne](#Boolean_Operation.md) sur les formes sélectionnées.}}


{{term|1=Unstable}}


{{defn|defn=Un surnom pour signaler qu'une version du logiciel FreeCAD est très récente et toujours à l'état de mise au point. Cette version contiendra de nombreux changements récemment mis en place par les développeurs. Il en général susceptible de produire des résultats erronés, et les essais ne sont pas terminés}}


{{term|Upgrade|content=[Upgrade](Draft_Upgrade/fr.md)}}


{{defn|defn=Un outil de l'[atelier](#Workbench.md) [Draft](Draft_Workbench/fr.md).}}


{{glossend}}

## V


{{gloss}}


{{term|Vector}}


{{defn|defn=Une grandeur dotée d'une direction. Souvant représenté graphiquement comme une flêche à 2 ou 3 dimensions. Par exemple, "cinquante pas vers le Nord", "9.8 m/s^2 vers le bas", et "(3,5,6) unités respectivement dans les directions x, y, z" sont tous des vecteurs. Dans FreeCAD, ils sont le plus souvent écrits comme des paires (x, y) ou des triplets (x, y, z). Ce sont des objets ordonnés.}}


{{term|Vertex}}


{{defn|defn=Un [point](#Point.md) tout seul dans l'espace, ou le sommet d'une [forme](#Shape.md) où se rencontrent ses [arêtes](#Edge.md). La technologie Open Cascade le définit comme, une forme ([shape](#Shape.md)) à zéro dimensions qui, en géométrie, correspond à un point. Voir [https://dev.opencascade.org/doc/overview/html/occt__tutorial.html#OCCT_TUTORIAL_SUB2_3 OCCT Profile: Defining the topology]}}


{{term|Vertices}}


{{defn|defn=Pluriel de [Vertex](#Vertex.md)}}


{{term|Viewprovider}}


{{defn|defn=Interface générale pour tous les éléments visuels de FreeCAD. ViewProvider génère et gère de manière globale la visualisation et la présentation des objets [App layer](#App.md) de FreeCAD pour l'utilisateur. Cette classe et ses descendants doivent être implémentés pour tout type d'objet afin de pouvoir les afficher dans la [vue 3D](#3DView.md) et la [vue en arborescence](#TreeView.md).}}


{{glossend}}

## W


{{gloss}}


{{term|WB}}


{{defn|defn=Raccourci pour [workbench](#Workbenches.md) (atelier).}}


{{term|term=Wire}}


{{defn|no=1|defn=Polyligne: succession d'[arêtes](#Edge.md) connectées par des [vertex](#Vertex.md) ou Points. Le terme est utilisé en ce sens principalement par [https://dev.opencascade.org/doc/overview/html/occt__tutorial.html#OCCT_TUTORIAL_SUB2_3 Open Cascade Technology]. On l'utilise donc aussi dans FreeCAD.}}


{{defn|no=2|defn=Une commande de l'[atelier](#Workbench.md) [Draft](Draft_Workbench/fr.md) qui crée une polyligne paramétrique.}}


{{term|term=Workbench}}


{{defn|defn=Aussi appellé module, chaque atelier regroupe un ensemble d'outils dédiés à une tâche spécifique.}}


{{glossend}}

## X


{{gloss}}


{{term|X}}


{{defn|defn=Fait communément référence à l'[axe](#Axis.md) X en 2D ou 3D.}}


{{glossend}}

## Y


{{gloss}}


{{term|Y}}


{{defn|defn=Fait communément référence à l'[axe](#Axis.md) Y en 2D ou 3D.}}


{{glossend}}

## Z


{{gloss}}


{{term|Z}}


{{defn|defn=Fait communément référence à l'[axe](#Axis.md) Z en 2D ou 3D.}}


{{glossend}}



---
⏵ [documentation index](../README.md) > [Wiki](Category_Wiki.md) > [Glossary](Category_Glossary.md) > Glossary/fr
