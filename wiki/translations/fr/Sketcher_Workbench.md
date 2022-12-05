# <img alt="Icône de l\'atelier Sketcher" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/fr


{{TOCright}}

## Introduction

L\'<img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [atelier Sketcher](Sketcher_Workbench/fr.md) de FreeCAD permet de créer des géométries 2D nommées **esquisses**, destinées à être utilisées dans les ateliers <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/fr.md), <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch](Arch_Workbench/fr.md) et d\'autres ateliers. Généralement, une géométrie 2D est le point de départ de la plupart des modèles de CAO ; une esquisse 2D peut être « extrudée » pour créer une forme 3D. D\'autres esquisses peuvent être utilisées pour créer des fonctions comme des cavités, des arêtes ou encore des extrusions qui s\'ajoutent aux formes 3D précédemment construites. Avec des opérations Booléennes sur des solides définies dans l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md), l\'atelier Sketcher constitue le cœur de la [conception 3D solide](constructive_solid_geometry.md). De plus, avec les opérations de l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [atelier PartDesign](PartDesign_Workbench.md), Sketcher constitue également la base de la méthodologie de modification des [fonctions de création de solides](feature_editing/fr.md).

L\'atelier Sketcher comporte des \"contraintes\", permettant aux formes 2D de suivre des définitions géométriques précises en termes de longueur, d\'angles et de relations (horizontalité, verticalité, perpendicularité, etc.). Un solveur de contraintes calcule l\'étendue contrainte de la géométrie 2D et permet une exploration interactive des degrés de liberté de l\'esquisse.

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*Une esquisse pleinement contrainte.‎*

## Les principes de l\'esquisse contrainte 

Pour décrire comment fonctionne l\'atelier Sketcher, il est utile de le comparer avec la méthode « traditionnelle » du dessin.

#### Dessin traditionnel 

La méthode traditionnelle de la DAO hérite de la technique de la [planche à dessin](https://fr.wikipedia.org/wiki/Planche_%C3%A0_dessin). Des [vues orthogonales](https://en.wikipedia.org/wiki/Multiview_orthographic_projection) sont dessinées manuellement afin de produire des dessins techniques (aussi appelés plans). Les éléments sont dessinées précisément à leur taille réelle (ou à l\'échelle). Si vous voulez dessiner une ligne horizontale de 100mm de longueur débutant aux coordonnées (0,0), il faut activer l\'outil ligne, cliquer à l\'écran ou saisir au clavier les coordonnées du premier point, puis faire une second clic ou saisir les coordonnées du second point, soit (0,100). Ou encore, vous pouvez dessiner la ligne sans vous soucier de sa position, pour la déplacer ensuite. Lorsque vous avez terminé votre dessin, vous ajoutez les cotes.

#### L\'esquisse contrainte 

Le **Sketcher** s\'éloigne de cette logique. Les objets n\'ont pas à être dessinés aux dimensions exactes que vous planifiez, puisqu\'ils seront définis ultérieurement par des contraintes. Ils peuvent être dessinés librement, et tant qu\'ils ne sont pas contraints, ils peuvent être manipulés et modifiés. Ces objets en quelque sorte flottent et peuvent être déplacés, étirés, pivotés, redimensionnés, etc. Ceci permet une très grande souplesse au processus de conception.

#### Que sont les contraintes ? 

Les contraintes sont utilisées pour limiter les degrés de liberté d\'un objet. Par exemple, une ligne sans contrainte a 4 degrés de liberté (abréviation française \"DDL\" et anglaise \"DOF\") : elle peut être déplacée horizontalement ou verticalement, étirée, subir une rotation.

L\'application d\'une contrainte horizontale ou verticale, ou une contrainte d\'angle (par rapport à une autre ligne ou à l\'un des axes), limite la capacité de rotation, la laissant ainsi avec 3 degrés de liberté.
Le verrouillage d\'un de ses points par rapport à l\'origine va encore supprimer 2 degrés de liberté.
Et, l\'application d\'une contrainte de dimension va supprimer le dernier degré de liberté. La ligne est alors considérée comme entièrement contrainte.

De nombreux objets peuvent être contraints entre eux. Deux lignes peuvent être reliées par un de leurs points avec une contrainte de coïncidence de point. Les angles peuvent être définis entre eux, ou ils peuvent être définis perpendiculairement. Une ligne peut être tangente à un cercle ou un arc et ainsi de suite. Un dessin complexe avec plusieurs objets aura un nombre de solutions différentes, et le rendre **entièrement contraint** signifie qu\'une seule des solutions possibles a été réalisée sur la base des contraintes appliquées.

Il existe deux types de contraintes : géométriques et dimensionnelles. Elles sont détaillées dans la section [\'Les outils\'](#Les_outils.md) ci-dessous.

#### Sketcher n\'est pas bon pour 

Sketcher n\'est pas destiné à la réalisation de plans 2D. Une fois que l\'esquisse a été utilisée pour générer un solide, elle est automatiquement cachée. Les contraintes sont uniquement visibles en mode édition.

Si vous n\'avez besoin que de produire des vues 2D pour l\'impression et que vous ne souhaitez pas créer de modèles 3D, consultez l\'[atelier Draft](Draft_Workbench/fr.md). Contrairement aux éléments Sketcher, les objets Draft n\'utilisent pas de contraintes ; ce sont des formes simples définies au moment de la création. Draft et Sketcher peuvent tous deux être utilisés pour le dessin de géométrie 2D et la création de solides 3D, bien que leur utilisation privilégiée soit différente ; le Sketcher est normalement utilisé avec les ateliers [Part](Part_Workbench/fr.md) et [PartDesign](PartDesign_Workbench/fr.md) pour créer des solides ; Draft est normalement utilisé pour des dessins plans simples sur une grille, comme lors du dessin d\'un plan d\'architecture ; dans ces situations, Draft est principalement utilisé avec l\'[atelier Arch](Arch_Workbench/fr.md). L\'outil [Draft vers Esquisse](Draft_Draft2Sketch/fr.md) convertit un objet Draft en un objet Esquisse, et vice versa ; de nombreux outils qui nécessitent un élément 2D en entrée fonctionnent avec les deux types d\'objets car une conversion interne est effectuée automatiquement.

## Processus d\'esquisse 

Une esquisse est toujours bidimensionnelle (2D). Pour créer un solide, une esquisse 2D d\'une seule zone fermée est créée, puis extrudée ou reçoit une révolution pour ajouter la 3ème dimension, créant un solide 3D à partir de l\'esquisse 2D.

Si une esquisse possède des segments qui se croisent, ou un point non directement positionné sur un segment, ou encore des écarts entre des points terminaux ou des segments adjacents, l\'extrusion ou la pièce de révolution ne créera pas un solide. Parfois, une esquisse contenant des lignes se croisant fonctionnera pour une opération simple telle qu\'une Protrusion, mais les opérations ultérieures telles que le motif linéaire échoueront. Il est préférable d\'éviter de traverser des lignes. Cette règle ne s\'applique pas aux Géométries de Construction (en bleu).

A l\'intérieur d\'une aire fermée, nous pouvons avoir des aires indépendantes. Celles-ci deviendront des vides lorsque le solide 3D sera généré.

Une fois que l'esquisse est entièrement contrainte, les fonctions d'esquisse deviennent vertes. La géométrie de construction restera bleue. Elle est généralement \"finie\" à ce stade et convient à la création d\'un solide 3D. Cependant, une fois que la boîte de dialogue Esquisse est fermée, il peut s\'avérer utile d\'aller à l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md) et de lancer **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Part Vérifier la géométrie](Part_CheckGeometry/fr.md)** pour vous assurer qu\'aucune fonctionnalité de l\'esquisse ne risque de causer des problèmes ultérieurs.

## Les outils 

Les outils de l\'atelier Sketcher sont tous situés dans le menu Sketch qui s\'affiche lorsque vous chargez l\'atelier Sketcher.

### Généralités

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Créer une esquisse](Sketcher_NewSketch/fr.md) : crée une nouvelle esquisse sur un plan ou une face sélectionnée. Si rien n\'est sélectionné, un dialogue pop up invitera l\'utilisateur à sélectionner un plan.

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Éditer l\'esquisse](Sketcher_EditSketch/fr.md) : édite l\'esquisse sélectionnée. Cela ouvrira la [Sketcher Boite de dialogue](Sketcher_Dialog/fr.md).

-   <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:32px;"> [Quitter l\'esquisse](Sketcher_LeaveSketch/fr.md) : quitte le mode d\'édition de l\'esquisse actuelle.

-   <img alt="" src=images/Sketcher_ViewSketch.svg  style="width:32px;"> [Vue de l\'esquisse](Sketcher_ViewSketch/fr.md) : définit l\'affichage de l\'objet perpendiculairement au plan de l\'esquisse.

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width:32px;"> [Vue sectionnée](Sketcher_ViewSection/fr.md) : crée un plan de coupe qui masque temporairement toute matière devant le plan d'esquisse.

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [Esquisse sur une face](Sketcher_MapSketch/fr.md) : applique une esquisse sur une face ou un solide sélectionné.

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:32px;"> [Réorienter l\'esquisse](Sketcher_ReorientSketch/fr.md): permet d\'attacher l\'esquisse à l\'un des plans principaux.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Valider l\'esquisse\...](Sketcher_ValidateSketch/fr.md) : vérifier la tolérance des différents points et les faire correspondre entre eux.

-   <img alt="" src=images/Sketcher_MergeSketches.svg  style="width:32px;"> [Fusionner les esquisses](Sketcher_MergeSketches/fr.md) : fusionner deux ou plusieurs esquisses.

-   <img alt="" src=images/Sketcher_MirrorSketch.svg  style="width:32px;"> [Esquisse miroir](Sketcher_MirrorSketch/fr.md) : crée une esquisse miroir selon l\'axe X, l\'axe Y ou l\'origine.

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Arrêt de l\'opération](Sketcher_StopOperation/fr.md) : en mode édition, arrêter l\'opération en cours, qu\'il s\'agisse de dessiner, de définir des contraintes, etc.

### Géométries d\'esquisse 

Ces outils permettent de créer des objets.

-   <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:32px;"> [Point](Sketcher_CreatePoint/fr.md) : dessine un point.

-   <img alt="" src=images/Sketcher_CreateLine.svg  style="width:32px;"> [Ligne](Sketcher_CreateLine/fr.md) : dessine une ligne entre 2 points. Les lignes sont considérées comme infinies par certaines contraintes.

-   <img alt="" src=images/Sketcher_CompCreateArc.png  style="width:48px;"> [Arcs](Sketcher_CompCreateArc/fr.md) : menu d\'icône dans la barre d\'outils Géométries d\'esquisse qui contient les commandes suivantes :

  - <img alt="" src=images/Sketcher_CreateArc.svg  style="width:32px;"> [Arc](Sketcher_CreateArc/fr.md) : dessine un segment d\'arc à partir du centre, rayon, angle de départ et angle d\'arrivée.

  - <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:32px;"> [Arc par 3 points](Sketcher_Create3PointArc/fr.md) : dessine un arc de cercle entre deux points d\'extrémité et un troisième point pour la circonférence.

-   <img alt="" src=images/Sketcher_CompCreateCircle.png  style="width:48px;"> [Cercles](Sketcher_CompCreateCircle/fr.md) : menu d\'icône dans la barre d\'outils Géométries d\'esquisse qui contient les commandes suivantes :

  - <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:32px;"> [Cercle](Sketcher_CreateCircle/fr.md) : dessine un cercle à partir de son centre et du rayon.

  - <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:32px;"> [Cercle par 3 points](Sketcher_Create3PointCircle/fr.md) : dessine un cercle à partir de trois points sur la circonférence.

-   <img alt="" src=images/Sketcher_CompCreateConic.png  style="width:48px;"> [Coniques](Sketcher_CompCreateConic/fr.md) : Sketcher fournit les sections coniques suivantes. Contrairement aux B-splines, elles peuvent être utilisées avec toutes sortes de contraintes telles que [Contrainte tangente](Sketcher_ConstrainTangent/fr.md), des [Contrainte point sur objet](Sketcher_ConstrainPointOnObject/fr.md) ou [Contrainte perpendiculaire](Sketcher_ConstrainPerpendicular/fr.md).

  - <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [Ellipse par son centre](Sketcher_CreateEllipseByCenter/fr.md) : dessine une ellipse à partir du centre, d\'un point sur le grand rayon et d\'un point sur le petit rayon.

  - <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [Ellipse par 3 points](Sketcher_CreateEllipseBy3Points/fr.md) : dessine une ellipse à partir du grand diametre (2 points) et d\'un point sur le petit rayon.

  - <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [Arc d\'ellipse](Sketcher_CreateArcOfEllipse/fr.md) : dessine une ellipse à partir du centre, d\'un point sur le grand rayon, avec un point de départ et un point d\'arrivée.

  -<img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [Arc d\'hyperbole](Sketcher_CreateArcOfHyperbola/fr.md) : dessine un arc d\'hyperbole.

  -<img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [Arc de parabole](Sketcher_CreateArcOfParabola/fr.md) : dessine un arc de parabole.

-   <img alt="" src=images/Sketcher_CompCreateBSpline.png  style="width:48px;"> [B-splines](Sketcher_CompCreateBSpline/fr.md) : menu d\'icône dans la barre d\'outils Géométries d\'esquisse qui contient les commandes suivantes :

  - <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [B-spline simple](Sketcher_CreateBSpline/fr.md) : dessine une courbe B-spline par ses points de contrôle.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width:32px;"> [B-spline périodique](Sketcher_CreatePeriodicBSpline/fr.md) : dessine une courbe B-spline périodique (fermée) par ses points de contrôle.

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:32px;"> [Polyligne](Sketcher_CreatePolyline/fr.md) : dessine une ligne composée de plusieurs segments connectés entre eux. Appuyer sur la touche **M** pendant que la commande est active bascule entre plusieurs modes de polylignes.

-   <img alt="" src=images/Sketcher_CompCreateRectangles.png  style="width:48px;"> [Rectangles](Sketcher_CompCreateRectangles/fr.md) : menu d\'icônes dans la barre d\'outils de Sketcher qui contient les commandes suivantes : {{Version/fr|0.20}}

  - <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [Rectangle](Sketcher_CreateRectangle/fr.md) : dessine un rectangle à partir de 2 points opposés.

  - <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Rectangle centré](Sketcher_CreateRectangle_Center/fr.md) : dessine un rectangle à partir d\'un point central et d\'un point du bord. {{Version/fr|0.20}}

  - <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Rectangle arrondi](Sketcher_CreateOblong/fr.md) : dessine un rectangle arrondi à partir de 2 points opposés. {{Version/fr|0.20}}

-   <img alt="" src=images/Sketcher_CompCreateRegularPolygon.png  style="width:48px;"> [Polygones réguliers](Sketcher_CompCreateRegularPolygon/fr.md) : menu d\'icônes dans la barre d\'outils Géométries d\'esquisse qui contient les commandes suivantes :

  - <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width:32px;"> [Triangle](Sketcher_CreateTriangle/fr.md) : dessine un triangle équilatéral inscrit dans un cercle.

  - <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> [Carré](Sketcher_CreateSquare/fr.md) : dessine un carré inscrit dans un cercle.

  - <img alt="" src=images/Sketcher_CreatePentagon.svg  style="width:32px;"> [Pentagone](Sketcher_CreatePentagon/fr.md) : dessine un pentagone régulier inscrit dans un cercle.

  - <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [Hexagone](Sketcher_CreateHexagon/fr.md) : dessine un hexagone régulier inscrit dans un cercle.

  - <img alt="" src=images/Sketcher_CreateHeptagon.svg  style="width:32px;"> [Heptagone](Sketcher_CreateHeptagon/fr.md) : dessine un heptagone régulier inscrit dans un cercle.

  - <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width:32px;"> [Octogone](Sketcher_CreateOctagon/fr.md) : dessine un octogone régulier inscrit dans un cercle.

  - <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [Polygone régulier](Sketcher_CompCreateRegularPolygon/fr.md) : dessine un polygone régulier en sélectionnant le nombre de côtés et en choisissant deux points: le centre et un coin.

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Contour oblong](Sketcher_CreateSlot/fr.md) : dessine un contour oblong (ex : clavette de type A) en entrant le centre du demi-cercle, le centre d\'un rayon et le point final du deuxième demi-cercle.

-   <img alt="" src=images/Sketcher_CompCreateFillets.png  style="width:48px;"> [Congés](Sketcher_CompCreateFillets/fr.md) : menu d\'icônes dans la barre d\'outils des contraintes de Sketcher qui contient les commandes suivantes :

  - <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> [Congé](Sketcher_CreateFillet/fr.md) : crée un congé entre deux lignes non parallèles.

  - <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:32px;"> [Congé avec contrainte](Sketcher_CreatePointFillet/fr.md) : crée un congé entre deux lignes non parallèles tout en préservant leur intersection (virtuelle).

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:32px;"> [Ajuster](Sketcher_Trimming/fr.md) : ajuste une ligne, un cercle ou un arc par rapport à l\'emplacement du clic.

-   <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Prolonger](Sketcher_Extend/fr.md) : prolonge une ligne ou un arc jusqu\'à une limite définie par un arc, une ellipse, un arc d\'ellipse ou un point dans l\'espace.

-   <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Diviser](Sketcher_Split/fr.md) : divise une ligne ou un arc en deux, convertit un cercle en arc de cercle en gardant la plupart des contraintes. {{Version/fr|0.20}}

-   <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [Géométrie externe](Sketcher_External/fr.md) : crée une arête liée à une géométrie externe.

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [Copie carbone](Sketcher_CarbonCopy/fr.md): copie la géométrie contenue dans une autre esquisse.

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:32px;"> [Basculer en géométrie de construction](Sketcher_ToggleConstruction/fr.md) : bascule les éléments vers/depuis le mode Construction. Les géométries de construction sont représentées en bleu, et ne sont pas prises en compte en dehors du mode d\'édition de l\'esquisse.

### Contraintes d\'esquisse 

Les contraintes sont utilisées pour définir des règles entre les éléments d\'esquisse et pour verrouiller l\'esquisse le long des axes vertical et horizontal. Certaines contraintes requièrent l\'utilisation de [contraintes d\'assistance](Sketcher_helper_constraint/fr.md).

#### Contraintes géométriques 

Ces contraintes ne sont pas associées à des données numériques.

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:32px;"> [Coïncidence](Sketcher_ConstrainCoincident/fr.md) : affecte un point à (coïncider avec) un ou plusieurs autres points. Elle agit comme une contrainte concentrique si deux ou plusieurs cercles, arcs, ellipses ou arcs d\'ellipses sont sélectionnés.

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:32px;"> [Point sur objet](Sketcher_ConstrainPointOnObject/fr.md) : fixe un point sur un autre objet tel qu\'une ligne, un arc ou un axe.

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:32px;"> [Vertical](Sketcher_ConstrainVertical/fr.md) : crée une contrainte de verticalité sur les lignes ou segments de polylignes sélectionnés. Il est possible de sélectionner plus d\'un objet avant d\'appliquer cette contrainte.

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:32px;"> [Horizontal](Sketcher_ConstrainHorizontal/fr.md) : crée une contrainte d\'horizontalité sur les lignes ou segments de polylignes sélectionnés. Il est possible de sélectionner plus d\'un objet avant d\'appliquer cette contrainte.

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:32px;"> [Parallèle](Sketcher_ConstrainParallel/fr.md) : contraint deux ou plusieurs lignes parallèles les unes aux autres.

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:32px;"> [Perpendiculaire](Sketcher_ConstrainPerpendicular/fr.md) : contraint deux lignes perpendiculaires l\'une à l\'autre, ou contraint une ligne perpendiculaire à l\'extrémité d\'un arc.

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:32px;"> [Tangente](Sketcher_ConstrainTangent/fr.md) : crée une contrainte de tangence entre deux éléments sélectionnés, ou de colinéarité entre deux lignes. Un segment de ligne ne doit pas nécessairement se trouver directement sur un arc ou un cercle pour être contraint de manière tangente à cet arc ou ce cercle.

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:32px;"> [Égalité](Sketcher_ConstrainEqual/fr.md) : contraint deux entités sélectionnées à être égales l\'une à l\'autre. Si elle est utilisée sur des cercles ou des arcs, leurs rayons seront égaux.

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:32px;"> [Symétrie](Sketcher_ConstrainSymmetric/fr.md) : contraint deux points symétriquement autour d\'une ligne, ou contraint les deux premiers points sélectionnés symétriquement autour d\'un troisième point sélectionné.

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:32px;"> [Contrainte de blocage](Sketcher_ConstrainBlock/fr.md) : empêche une arête de se déplacer, c\'est-à-dire qu\'il empêche ses sommets de changer leur position en cours. Particulièrement utile de fixer la position des B-Splines. Voir la [discussion «Block Constraint» (en) sur le forum](https://forum.freecadweb.org/viewtopic.php?f=9&t=26572).

#### Contraintes dimensionnelles 

Ces contraintes sont associées à des données numériques, pour lesquelles vous pouvez utiliser des [expressions](Expressions/fr.md). Les données peuvent être tirées d\'un [tableur](Spreadsheet_Workbench/fr.md).

-   <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:32px;"> [Fixe](Sketcher_ConstrainLock/fr.md) : contraint l\'élément sélectionné en définissant des distances verticales et horizontales par rapport à l\'origine, verrouillant ainsi l\'emplacement de cet élément. Ces contraintes dimensionnelles peuvent être éditées par la suite.

-   <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:32px;"> [Distance horizontale](Sketcher_ConstrainDistanceX/fr.md) : fixe la distance horizontale entre deux points ou extrémités de ligne. Si un seul élément est sélectionné, la distance sera relative à l\'origine.

-   <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:32px;"> [Distance verticale](Sketcher_ConstrainDistanceY/fr.md) : fixe la distance verticale entre deux points ou extrémités de ligne. Si un seul élément est sélectionné, la distance sera relative à l\'origine.

-   <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:32px;"> [Dimensionnelle](Sketcher_ConstrainDistance/fr.md) : fixe la longueur d\'une ligne sélectionnée, ou la distance entre une ligne et un point. La distance sera perpendiculaire à la ligne.

-   <img alt="" src=images/Sketcher_CompConstrainRadDia.png  style="width:48px;"> [Arc ou cercle](Sketcher_CompConstrainRadDia/fr.md) : menu d\'icônes dans la barre d\'outils des contraintes de Sketcher qui contient les commandes suivantes :

  - <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [Rayon](Sketcher_ConstrainRadius/fr.md) : définit le rayon d\'un arc ou d\'un cercle sélectionné en contraignant le rayon.

  - <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Diamètre](Sketcher_ConstrainDiameter/fr.md) : définit le diamètre d\'un arc ou d\'un cercle sélectionné en contraignant le diamètre.

  - <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Rayon automatique](Sketcher_ConstrainRadiam/fr.md) : définit automatiquement le rayon/diamètre d\'un arc ou d\'un cercle sélectionné (poids pour un pôle B-spline, diamètre pour un cercle complet, rayon pour un arc) {{Version/fr|0.20}}.

  - <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Angle](Sketcher_ConstrainAngle/fr.md) : crée une contrainte d\'angle interne entre deux lignes sélectionnées.

#### Contraintes spéciales 

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:32px;"> [Contrainte de réfraction](Sketcher_ConstrainSnellsLaw/fr.md) : contraint deux lignes à respecter une loi de réfraction simulant la trajectoire de la lumière à travers une interface.

-   <img alt="" src=images/Sketcher_ConstrainInternalAlignment.svg  style="width:32px;"> [Alignement interne](Sketcher_ConstrainInternalAlignment/fr.md) : aligne les éléments selectionnés à la forme sélectionnée (par exemple, contraint une ligne à devenir le grand axe d\'une ellipse).

#### Outils de contrainte 

Les outils suivants peuvent être utilisés pour modifier l\'effet des contraintes:

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:32px;"> [Basculement de contrainte](Sketcher_ToggleDrivingConstraint/fr.md) : bascule la barre d\'outils ou les contraintes sélectionnées vers/depuis le mode de référence.

-   <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Activation des contraintes](Sketcher_ToggleActiveConstraint/fr.md) : active ou désactive une contrainte déjà placée. {{Version/fr|0.19}}

### Outils d\'esquisse 

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [Sélecteur des degrés de liberté non contraints](Sketcher_SelectElementsWithDoFs/fr.md) : surligne en vert les éléments de l\'esquisse contenant des degrés de liberté, c\'est-à-dire non complètement contraints.

-   <img alt="" src=images/Sketcher_CloseShape.svg  style="width:32px;"> [Fermer la forme](Sketcher_CloseShape/fr.md) : ferme une forme en appliquant des contraintes coïncidentes aux points d\'arrivée. Cet outil est obsolète, il ne sera pas disponible dans les prochaines versions ({{VersionPlus/fr|1.0}}).

-   <img alt="" src=images/Sketcher_ConnectLines.svg  style="width:32px;"> [Connecter les côtés](Sketcher_ConnectLines/fr.md) : connecte les éléments de l\'esquisse en appliquant des contraintes de coïncidence aux points d\'arrivée. Cet outil est obsolète, il ne sera pas disponible dans les prochaines versions ({{VersionPlus/fr|1.0}}).

-   <img alt="" src=images/Sketcher_SelectConstraints.svg  style="width:32px;"> [Sélecteur de contraintes associées](Sketcher_SelectConstraints/fr.md) : sélectionne les contraintes d\'un élément de l\'esquisse.

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg  style="width:32px;"> [Sélecteur des éléments associés aux contraintes](Sketcher_SelectElementsAssociatedWithConstraints/fr.md) : sélectionne les éléments associés aux contraintes.

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width:32px;"> [Sélection contraintes redondantes](Sketcher_SelectRedundantConstraints/fr.md) : sélectionne les contraintes redondantes de l\'esquisse.

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width:32px;"> [Sélection des contraintes conflictuelles](Sketcher_SelectConflictingConstraints/fr.md) : sélectionne les contraintes conflictuelles de l\'esquisse.

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:32px;"> [Basculer la géométrie interne](Sketcher_RestoreInternalAlignmentGeometry/fr.md) : recrée/supprime la géométrie interne de l\'élément sélectionné (ellipse, arc d\'ellipse/hyperbole/parabole, courbe B-spline).

-   <img alt="" src=images/Sketcher_SelectOrigin.svg  style="width:32px;"> [Sélectionner l\'origine](Sketcher_SelectOrigin/fr.md) : sélectionne l\'origine de l\'esquisse.

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg  style="width:32px;"> [Sélectionner l\'axe vertical](Sketcher_SelectVerticalAxis/fr.md) : sélectionne l\'axe vertical de l\'esquisse.

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg  style="width:32px;"> [Sélectionner l\'axe horizontal](Sketcher_SelectHorizontalAxis/fr.md) : sélectionne l\'axe horizontal de l\'esquisse.

-   <img alt="" src=images/Sketcher_Symmetry.svg  style="width:32px;"> [Symétrie](Sketcher_Symmetry/fr.md) : crée une copie symétrique par rapport à une ligne donnée.

-   <img alt="" src=images/Sketcher_Clone.svg  style="width:32px;"> [Clone](Sketcher_Clone/fr.md) : clone un élément de l\'esquisse.

-   <img alt="" src=images/Sketcher_Copy.svg  style="width:32px;"> [Copie](Sketcher_Copy/fr.md) : copie un élément de l\'esquisse.

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Déplacer](Sketcher_Move/fr.md) : déplace la géométrie sélectionnée en prenant comme référence le dernier point sélectionné.

-   <img alt="" src=images/Sketcher_RectangularArray.svg  style="width:32px;"> [Réseau rectangulaire](Sketcher_RectangularArray/fr.md) : crée une réseau à partir des éléments sélectionnés.

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Supprimer l\'alignement des axes](Sketcher_RemoveAxesAlignment/fr.md) : supprime l\'alignement des axes tout en essayant de préserver la relation de contrainte de la sélection. {{Version/fr|0.20}}.

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width:32px;"> [Supprimer tous les éléments de géométrie](Sketcher_DeleteAllGeometry/fr.md) : supprime toute la géométrie de l\'esquisse.

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width:32px;"> [Supprimer toutes les contraintes](Sketcher_DeleteAllConstraints/fr.md) : supprime toutes les contraintes de l\'esquisse.

### Outils d\'esquisse B-spline 

-   <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [Montrer/Cacher le degré de la B-spline](Sketcher_BSplineDegree/fr.md)

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [Montrer/Cacher le polygone de contrôle de la B-spline](Sketcher_BSplinePolygon/fr.md)

-   <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [Montrer/Cacher le peigne de courbure de la B-spline](Sketcher_BSplineComb/fr.md)

-   <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [Montrer/Cacher la multiplicité des nœuds de la B-spline](Sketcher_BSplineKnotMultiplicity/fr.md)

-   <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [Poids des points de contrôle B-spline](Sketcher_BSplinePoleWeight/fr.md), {{Version/fr|0.19}}

-   <img alt="" src=images/Sketcher_BSplineApproximate.svg  style="width:32px;"> [Convertir une géométrie en B-spline](Sketcher_BSplineApproximate/fr.md)

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Augmenter le degré de la B-spline](Sketcher_BSplineIncreaseDegree/fr.md)

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Diminuer le degré de la B-spline](Sketcher_BSplineDecreaseDegree/fr.md), {{Version/fr|0.19}}

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Augmenter la multiplicité des nœuds de la B-spline](Sketcher_BSplineIncreaseKnotMultiplicity/fr.md)

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Diminuer la multiplicité des nœuds de la B-spline](Sketcher_BSplineDecreaseKnotMultiplicity/fr.md)

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Insérer un nœud](Sketcher_BSplineInsertKnot/fr.md), {{Version/fr|0.20}}

### Espace virtuel de l\'esquisse 

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width:32px;"> [Basculer l\'espace virtuel](Sketcher_SwitchVirtualSpace/fr.md) :permet de masquer toutes les contraintes d\'une esquisse et de les rendre à nouveau visibles.

## Préférences

-   <img alt="" src=images/Std_DlgParameter.svg  style="width:32px;"> [Préférences\...](Sketcher_Preferences/fr.md) : préférences disponibles pour l\'atelier **Sketcher**.

## Bonnes pratiques 

Chaque utilisateur de DAO développe sa propre philosophie au cours de son travail, mais il y a quelques principes généraux utiles à suivre.

-   Une série d\'esquisses simples est plus facile à gérer qu\'une seule esquisse complexe. Par exemple, une première esquisse peut être créée pour l\'élément 3D de base (un tampon ou une rotation), tandis qu\'une deuxième peut contenir des trous ou des découpes (poches). Certains détails peuvent être laissés de côté, pour être réalisés ultérieurement en tant qu\'éléments 3D. Vous pouvez choisir d\'éviter les congés dans votre esquisse s\'il y en a trop, et les ajouter en tant qu\'élément 3D.
-   Créez toujours un profil fermé, sinon votre esquisse ne produira pas un solide, mais plutôt un ensemble de faces ouvertes. Si vous ne souhaitez pas que certains objets soient inclus dans la création du solide, transformez-les en éléments de construction avec l\'outil Mode de construction.
-   Utilisez la fonction de contraintes automatiques pour limiter le nombre de contraintes que vous devrez ajouter manuellement.
-   En règle générale, appliquez d\'abord les contraintes géométriques, puis les contraintes dimensionnelles, et verrouillez votre esquisse en dernier. Mais n\'oubliez pas : les règles sont faites pour être transgressées. Si vous avez du mal à manipuler votre esquisse, il peut être utile de contraindre quelques objets avant de compléter votre profil.
-   Si possible, centrez votre esquisse par rapport à l\'origine (0,0) avec la contrainte de verrouillage. Si votre esquisse n\'est pas symétrique, localisez l\'un de ses points par rapport à l\'origine ou choisissez de jolis chiffres ronds pour les distances de verrouillage.
-   Si vous avez la possibilité de choisir entre la contrainte de longueur et les contraintes de distance horizontale ou verticale, préférez ces dernières. Les contraintes de distance horizontale et verticale sont moins coûteuses en termes de calcul.
-   En général, les meilleures contraintes à utiliser sont : Contraintes horizontales et verticales ; Contraintes de longueur horizontales et verticales ; Tangence point à point. Si possible, limitez l\'utilisation de ces contraintes : la contrainte générale de longueur ; la tangence bord à bord ; la contrainte de fixation du point sur une ligne ; la contrainte de symétrie.
-   Si vous avez des doutes sur la validité d\'une esquisse une fois qu\'elle est terminée (les caractéristiques deviennent vertes), fermez la boîte de dialogue Sketcher, passez à l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md) et exécutez **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Part Vérifier la géométrie](Part_CheckGeometry/fr.md)**.

## Tutoriels

-   [Sketcher tutorial](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) par chrisb. Il s'agit d'un document PDF de 70 pages qui sert de manuel détaillé à l'atelier esquisse. Il explique les bases de l\'utilisation du Sketcher et aborde de nombreux détails concernant la création de formes géométriques et chacune des contraintes.
-   [Sketcher : Tutoriel d\'introduction](Basic_Sketcher_Tutorial/fr.md) pour débutants
-   [Sketcher : Micro-tutoriel - Les pratiques de contraintes](Sketcher_Micro_Tutorial_-_Constraint_Practices/fr.md)
-   [Sketcher : Requis pour une esquisse](Sketcher_requirement_for_a_sketch/fr.md) Exigence minimale pour un croquis et détermination complète d\'un croquis.

## Script

La page [Sketcher : Ecrire des scripts](Sketcher_scripting/fr.md) contient des exemples sur la façon de créer des contraintes à partir de scripts Python.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Sketcher Workbench/fr
