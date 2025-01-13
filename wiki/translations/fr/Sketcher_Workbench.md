# <img alt="Icône de l\'atelier Sketcher" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/fr




## Introduction

Avec l\'<img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [atelier Sketcher](Sketcher_Workbench/fr.md), il est possible de créer des esquisses en 2D destinées à être utilisées dans d\'autres ateliers. Les esquisses 2D sont le point de départ de nombreux modèles de CAO. Elles définissent généralement les profils et les trajectoires des opérations permettant de créer des formes en 3D. Un modèle peut dépendre de plusieurs esquisses pour sa forme finale.

Avec les opérations booléennes définies dans l\'<img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [atelier Part](Part_Workbench/fr.md), l\'atelier Sketcher, ou \"Sketcher\" en abrégé, constitue la base de la méthode de construction de solides [conception 3D solide](Constructive_solid_geometry/fr.md) (CSG en anglais). Avec l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [atelier PartDesign](PartDesign_Workbench/fr.md), elle constitue également la base de la méthodologie des [fonctions](Feature_editing/fr.md) pour la création de solides. Mais de nombreux autres ateliers utilisent également des esquisses.

L\'atelier Sketcher comporte des [contraintes](#Contraintes.md), permettant aux formes 2D de suivre des définitions géométriques précises en termes de longueur, d\'angles et de relations (horizontalité, verticalité, perpendicularité, etc.). Un solveur de contraintes calcule l\'étendue contrainte de la géométrie 2D et permet une exploration interactive des degrés de liberté de l\'esquisse.

Sketcher n\'est pas destiné à produire des plans en 2D. Une fois que les esquisses sont utilisées pour générer un élément solide, elles sont automatiquement masquées et les contraintes ne sont visibles qu\'en mode d\'édition d\'esquisse. Si vous avez uniquement besoin de produire des vues 2D pour l\'impression et que vous ne souhaitez pas créer de modèles 3D, consultez l\'[atelier Draft](Draft_Workbench/fr.md).

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*Une esquisse pleinement contrainte.‎*



## Contraintes

Les contraintes sont utilisées pour limiter les degrés de liberté d\'un objet. Par exemple, une ligne sans contrainte a 4 degrés de liberté (abréviation française \"DDL\" et anglaise \"DoF\") : elle peut être déplacée horizontalement ou verticalement, étirée, subir une rotation.

L\'application d\'une contrainte horizontale ou verticale, ou une contrainte d\'angle (par rapport à une autre ligne ou à l\'un des axes), limite la capacité de rotation, la laissant ainsi avec 3 degrés de liberté.
Le verrouillage d\'un de ses points par rapport à l\'origine va encore supprimer 2 degrés de liberté.
Et, l\'application d\'une contrainte de dimension va supprimer le dernier degré de liberté. La ligne est alors considérée comme **entièrement contrainte**.

Les objets peuvent être contraints les uns par rapport aux autres. Deux lignes peuvent être reliées par l\'un de leurs points grâce à la contrainte de coïncidence des points. Un angle peut être défini entre elles ou elles peuvent être perpendiculaires. Une ligne peut être tangente à un arc ou à un cercle, etc. Une esquisse complexe comportant plusieurs objets peut avoir un certain nombre de solutions différentes, et le fait de la rendre **entièrement contrainte** peut signifier qu\'une seule de ces possibles solutions a été atteinte sur la base des contraintes appliquées.

Il existe deux types de contraintes : géométriques et dimensionnelles. Elles sont détaillées dans la section [Les outils](#Les_outils.md) ci-dessous.



### Modifier les contraintes 

Lorsqu\'une [contrainte pilotante de dimension](Sketcher_ToggleDrivingConstraint/fr.md) est créée, et si la [préférence](Sketcher_Preferences/fr#Affichage.md) **Demander la valeur après la création d'une contrainte de dimension** est sélectionnée (par défaut), une boîte de dialogue s\'ouvre pour modifier sa valeur.

![](images/Sketcher_Edit_Constraint.png )

Vous pouvez saisir une valeur numérique ou une [expression](Expressions/fr.md), et il est possible de nommer la contrainte pour faciliter son utilisation dans d\'autres expressions. Vous pouvez également cocher la case **Référence** pour faire basculer la contrainte en [mode référence](Sketcher_ToggleDrivingConstraint/fr.md).

Pour modifier la valeur d\'une contrainte existante de dimension, procédez comme suit :

-   Double-cliquez sur la valeur de la contrainte dans la [vue 3D](3D_view/fr.md).
-   Double-cliquez sur la contrainte dans la [fenêtre de dialogue](Sketcher_Dialog/fr.md).
-   Cliquez avec le bouton droit de la souris sur la contrainte dans la fenêtre de dialogue de l\'esquisse et sélectionnez l\'option **Changer la valeur** du menu contextuel.



### Repositionner les contraintes 

Les contraintes de dimension peuvent être repositionnées dans la vue 3D en les faisant glisser. Maintenez le bouton gauche de la souris enfoncé sur la valeur de la contrainte et déplacez la souris. Les symboles des contraintes géométriques sont positionnés automatiquement et ne peuvent pas être déplacés.



## Esquisses de profil 

Pour créer une esquisse qui peut être utilisée comme profil pour générer des solides, certaines règles doivent être respectées :

-   L\'esquisse ne doit contenir que des contours fermés. Les espaces entre les extrémités, aussi petits soient-ils, ne sont pas autorisés.
-   Les contours peuvent être imbriqués pour créer des vides, mais ils ne doivent pas s\'auto-intersecter ou croiser d\'autres contours.
-   Les contours ne peuvent pas partager d\'arêtes avec d\'autres contours. Les arêtes en double doivent être évitées.
-   Les connexions en T, c\'est-à-dire plus de deux arêtes partageant un point commun ou un point touchant une arête, ne sont pas autorisées.

Ces règles ne s\'appliquent pas à la géométrie de construction (couleur bleue par défaut), qui n\'est pas affichée en dehors du mode édition, ou si l\'esquisse est utilisée à d\'autres fins. D\'autres restrictions peuvent s\'appliquer en fonction de l\'atelier et de l\'outil qui utilisera l\'esquisse de profil.



## Aides au dessin 

L\'atelier Sketcher dispose de plusieurs aides au dessin et d\'autres fonctions qui peuvent aider à créer des géométries et à appliquer des contraintes.



### Modes continus 

Il existe deux modes continus : **Création de géométrie en mode continu** et **Création de contraintes en mode continu**. Si ces modes sont cochés (par défaut) dans les [préférences](Sketcher_Preferences/fr#Affichage.md), les outils associés redémarreront après avoir été arrêtés. Pour quitter un outil en mode continu, appuyez sur **Échap** ou sur le bouton droit de la souris. Cette opération doit être répétée si un outil géométrique continu a déjà été saisi. Vous pouvez également quitter un outil continu en démarrant un autre outil de création de géométrie ou de contrainte. Notez qu\'en appuyant sur **Échap**, si aucun outil n\'est actif, vous quitterez le mode d\'édition d\'esquisse. Décochez la [préférence](Sketcher_Preferences/fr#Général.md) **Échap permet de quitter l\'esquisse en édition** si vous appuyez souvent par inadvertance sur **Échap** trop de fois.



### Contraintes automatiques 

Dans les esquisses pour lesquelles la case **Contraintes automatiques** est cochée (par défaut), plusieurs contraintes sont appliquées automatiquement. L\'icône d\'une contrainte automatique proposée s\'affiche à côté du curseur lorsqu\'elle est placée correctement. Un clic gauche permet alors d\'appliquer cette contrainte. Il s\'agit d\'un paramètre par esquisse qui peut être modifié dans la [fenêtre de dialogue](Sketcher_Dialog/fr#Contraintes.md) ou en modifiant la [propriété](Property_editor/fr.md) **Autoconstraints** de l\'esquisse.

Les contraintes suivantes sont appliquées automatiquement :

-   [Coincidence](Sketcher_ConstrainCoincident/fr.md)

-   [Point sur objet](Sketcher_ConstrainPointOnObject/fr.md)

-   [Horizontale](Sketcher_ConstrainHorizontal/fr.md)

-   [Verticale](Sketcher_ConstrainVertical/fr.md)

-   [Tangence](Sketcher_ConstrainTangent/fr.md)

-    {{Version/fr|0.22}}: [Symétrie](Sketcher_ConstrainSymmetric/fr.md) (point milieu de la ligne)



### Aimantation


{{Version/fr|0.21}}

Il est possible d\'[aimanter](Sketcher_Snap/fr.md) aux lignes de la grille et aux intersections de la grille, aux arêtes de géométrie et aux points médians des segments et des arcs, ainsi que sur certains angles. Veuillez noter que l\'aimantation ne produit pas de contraintes en soi. Par exemple, ce n\'est que si [Contraintes automatiques](#Contraintes_automatiques.md) est activé que l\'aimantation à une arête produira une [contrainte Point sur objet](Sketcher_ConstrainPointOnObject/fr.md). Mais le simple fait de choisir un point sur l\'arête aurait le même résultat.



### Paramètres d\'affichage 


{{Version/fr|1.0}}

Selon l\'option sélectionnée dans les [préférences](Sketcher_Preferences/fr#Général.md), seuls les paramètres d\'affichage de dimension ou les paramètres d\'affichage de dimension et de position peuvent être activés. Les paramètres de position permettent de saisir des coordonnées exactes, par exemple le centre d\'un cercle ou le point de départ d\'une ligne. Les paramètres de dimension permettent de saisir des dimensions exactes, par exemple le rayon d\'un cercle ou la longueur et l\'angle d\'une ligne. Les paramètres d\'affichage ne sont pas disponibles pour tous les outils.

![](images/Sketcher_On_view_parameters_positional.png ) 
*Détermination du point central d'un cercle avec les paramètres de position activés*

![](images/Sketcher_On_view_parameters_dimensional.png ) 
*Détermination du rayon d'un cercle avec les paramètres de dimension activés*

Si des valeurs sont saisies et confirmées en appuyant sur **Entrée** ou **Tabulation**, les contraintes correspondantes sont ajoutées automatiquement. Si deux paramètres sont affichés en même temps, par exemple les coordonnées X et Y d\'un point, il est possible de saisir une valeur et de choisir un point pour définir l\'autre. En fonction de l\'objet, des contraintes supplémentaires peuvent être nécessaires pour le contraindre complètement. Les contraintes résultant des paramètres d\'affichage sont prioritaires sur celles qui peuvent résulter des [contraintes automatiques](Sketcher_Dialog/fr#Contraintes.md).

<img alt="" src=images/Sketcher_ArcExample3.png  style="width:300px;"> 
*Arc créé en saisissant tous les paramètres d'affichage avec les contraintes créées automatiquement qui en résultent*



### Affichage des coordonnées 

Si la [préférence](Sketcher_Preferences/fr#Affichage.md) **Afficher les coordonnées à côté du curseur lors de l\'édition** est cochée (par défaut), les paramètres de l\'outil géométrique en cours (coordonnées, rayon ou longueur et angle) sont affichés à côté du curseur. Cette option est désactivée lorsque les paramètres d\'affichage sont affichés.



## Méthodes de sélection 

Lorsqu\'une esquisse est en mode édition, les méthodes de sélection suivantes peuvent être utilisées :



### Sélection des éléments dans la vue 3D 

Comme partout ailleurs dans FreeCAD, un élément peut être sélectionné dans la [vue 3D](3D_view/fr.md) avec un simple clic gauche de la souris. Mais il n\'est pas nécessaire de maintenir la touche **Ctrl** pour sélectionner plusieurs éléments. Il est toutefois possible de maintenir cette touche enfoncée, ce qui présente l\'avantage de pouvoir faire un mauvais clic sans perdre la sélection. Les arêtes, les points et les contraintes peuvent être sélectionnés de cette manière.



### Sélection par une boîte dans la vue 3D 

La sélection par boîte dans la vue 3D fonctionne sans utiliser [Std Sélection par boîte](Std_BoxSelection/fr.md) ou [Std Sélection d\'éléments par boîte](Std_BoxElementSelection/fr.md) :

1.  Assurez-vous qu\'aucun outil n\'est actif.
2.  Faites l\'une des choses suivantes :
    -   Cliquez dans une zone vide et faites glisser un rectangle de gauche à droite pour sélectionner les éléments qui se trouvent entièrement à l\'intérieur du rectangle.
    -   Cliquez dans une zone vide et faites glisser un rectangle de droite à gauche pour sélectionner également les éléments qui touchent ou traversent le rectangle.

Vous pouvez sélectionner des arêtes et des points par boîte mais les contraintes ne peuvent pas être sélectionnées par une boîte.



### Sélection de la géométrie connectée dans la vue 3D 


{{Version/fr|1.0}}

Un double-clic sur une arête dans la vue 3D sélectionnera toutes les arêtes directement et indirectement connectées à cette arête via ses extrémités. Il n\'est pas nécessaire que les arêtes soient reliées par des [contraintes de coïncidence](Sketcher_ConstrainCoincident/fr.md), il suffit que les extrémités aient les mêmes coordonnées.



### Fenêtre de dialogue de Sketcher 

Les arêtes et les points peuvent également être sélectionnés à partir de la section Éléments de la [fenêtre de dialogue de Sketcher](Sketcher_Dialog/fr.md) et les contraintes à partir de la section Contraintes de cette même fenêtre de dialogue.



## Copier, couper et coller 


{{Version/fr|1.0}}

Les raccourcis clavier standard, **Ctrl**+**C**, **Ctrl**+**X** et **Ctrl**+**V**, peuvent être utilisés pour copier, couper et coller une géométrie sélectionnée, y compris les contraintes associées. Mais ces outils sont également disponibles dans le menu **Esquisse → Outils d'esquisse**. Ils peuvent être utilisés au sein d\'une même esquisse, mais aussi entre différentes esquisses ou instances distinctes de FreeCAD. Comme les données sont copiées dans le presse-papiers sous forme de code Python, elles peuvent également être utilisées d\'autres manières (par exemple, partagées sur le forum).



## Les outils 

Les outils de l\'atelier Sketcher se trouvent dans le menu Esquisse et/ou dans plusieurs barres d\'outils. {{Version/fr|0.21}} : la majorité des barres d\'outils de Sketcher ne s\'affichent que lorsqu\'une esquisse est en mode édition. La seule exception est la [barre d\'outils de Sketcher](#Barre_d'outils_de_Sketcher.md) est la seule à s\'afficher si aucune esquisse n\'est en mode édition.

Certains outils sont également disponibles dans le menu contextuel de le [vue 3D](3D_view/fr.md) lorsqu\'une esquisse est en mode édition, ou dans les menus contextuels de la [boîte de dialogue](Sketcher_Dialog/fr.md).


{{Version/fr|0.21}}

: si une esquisse est en mode édition, la barre d\'outils Structure est cachée car aucun de ses outils ne peut être utilisé.



### Généralités



#### Barre d\'outils de Sketcher 

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Créer une esquisse](Sketcher_NewSketch/fr.md) : crée une nouvelle esquisse et ouvre la [fenêtre de dialogue](Sketcher_Dialog/fr.md) pour la modifier.

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Modifier une esquisse](Sketcher_EditSketch/fr.md) : ouvre la fenêtre de dialogue pour modifier une esquisse existante.

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [Ancrer une esquisse](Sketcher_MapSketch/fr.md) : ancre une esquisse à la géométrie sélectionnée.

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:32px;"> [Réorienter une esquisse](Sketcher_ReorientSketch/fr.md) : place une esquisse sur l\'un des plans principaux avec un décalage en option. Cela peut également être utilisé pour détacher une esquisse.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Valider une esquisse](Sketcher_ValidateSketch/fr.md) : peut analyser et réparer une esquisse qui n\'est plus modifiable ou qui présente des contraintes non valides, ou ajouter des contraintes coïncidentes manquantes.

-   <img alt="" src=images/Sketcher_MergeSketches.svg  style="width:32px;"> [Fusionner des esquisses](Sketcher_MergeSketches/fr.md) : fusionne deux ou plusieurs esquisses.

-   <img alt="" src=images/Sketcher_MirrorSketch.svg  style="width:32px;"> [Esquisse miroir](Sketcher_MirrorSketch/fr.md) : met en miroir les esquisses par rapport à leur axe X, axe Y ou à leur origine.



#### Barre d\'outils du mode édition de Sketcher 

-   <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:32px;"> [Quitter l\'esquisse](Sketcher_LeaveSketch/fr.md) : quitte le mode d\'édition de l\'esquisse et ferme la [fenêtre de dialogue de Sketcher](Sketcher_Dialog/fr.md).

-   <img alt="" src=images/Sketcher_ViewSketch.svg  style="width:32px;"> [Vue de l\'esquisse](Sketcher_ViewSketch/fr.md) : aligne la [vue 3D](3D_view/fr.md) avec le plan de l\'esquisse.

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width:32px;"> [Vue de section](Sketcher_ViewSection/fr.md) : permet d\'activer/désactiver un plan de coupe temporaire qui masque tous les objets et parties d\'objets devant le plan d\'esquisse.



#### Barre d\'outils des outils d\'édition de Sketcher 

-   <img alt="" src=images/Sketcher_Grid.svg  style="width:32px;"> [Grille](Sketcher_Grid/fr.md) : active/désactive la grille dans l\'esquisse en cours d\'édition. Les paramètres peuvent être modifiés dans le menu correspondant. {{Version/fr|0.21}}

-   <img alt="" src=images/Sketcher_Snap.svg  style="width:32px;"> [Aimantation](Sketcher_Snap/fr.md) : active/désactive l\'aimantation dans toutes les esquisses. Les paramètres peuvent être modifiés dans le menu correspondant. {{Version/fr|0.21}}

-   <img alt="" src=images/Sketcher_RenderingOrder.svg  style="width:32px;"> [Ordre de rendu](Sketcher_RenderingOrder/fr.md) : l\'ordre de rendu de toutes les esquisses peut être modifié dans le menu correspondant. {{Version/fr|0.21}}



#### Autres

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [Arrêt de l\'opération](Sketcher_StopOperation/fr.md) : arrête tout outil de création de géométrie ou de contrainte en cours d\'exécution.



### Géométries d\'esquisse 

Ces outils permettent de créer des objets.

-   <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:32px;"> [Point](Sketcher_CreatePoint/fr.md) : crée un point.

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:32px;"> [Polyligne](Sketcher_CreatePolyline/fr.md) : crée une série de segments de lignes et d\'arcs reliés par leurs extrémités. L\'outil dispose de plusieurs modes.

-   <img alt="" src=images/Sketcher_CreateLine.svg  style="width:32px;"> [Ligne](Sketcher_CreateLine/fr.md) : crée une ligne. {{Version/fr|1.0}} : l\'outil a trois modes.

-   <img alt="" src=images/Sketcher_CreateArc.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Créer un arc :

  - <img alt="" src=images/Sketcher_CreateArc.svg  style="width:32px;"> [Arc](Sketcher_CreateArc/fr.md) : crée un arc par son centre et ses extrémités. {{Version/fr|1.0}} : ou par ses extrémités et un point de l\'arc.

  - <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:32px;"> [Arc par 3 points](Sketcher_Create3PointArc/fr.md) : crée un arc par ses extrémités et un point de l\'arc. {{Version/fr|1.0}} : il s\'agit du même outil que [Arc](Sketcher_CreateArc/fr.md) mais avec un mode initial différent.

  - <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [Arc d\'ellipse](Sketcher_CreateArcOfEllipse/fr.md) : crée un arc d\'ellipse.

  -<img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [Arc d\'hyperbole](Sketcher_CreateArcOfHyperbola/fr.md) : crée un arc d\'hyperbole.

  -<img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [Arc de parabole](Sketcher_CreateArcOfParabola/fr.md) : crée un arc de parabole.

-   <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Créer un cercle/une ellipse :

  - <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:32px;"> [Cercle](Sketcher_CreateCircle/fr.md) : crée un cercle par son centre et un point de la circonférence. {{Version/fr|1.0}} : ou par trois points de la circonférence.

  - <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:32px;"> [Cercle par 3 points](Sketcher_Create3PointCircle/fr.md) : crée un cercle à partir de trois points de la circonférence. {{Version/fr|1.0}} : il s\'agit du même outil que [Cercle](Sketcher_CreateCircle/fr.md) mais avec un mode initial différent.

  - <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [Ellipse par son centre](Sketcher_CreateEllipseByCenter/fr.md) : crée une ellipse par son centre, une des extrémités de l\'un de ses axes et un point de l\'ellipse. {{Version/fr|1.0}} : ou par les deux extrémités d\'un de ses axes et un point de l\'ellipse.

  - <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [Ellipse par 3 points](Sketcher_CreateEllipseBy3Points/fr.md) : crée une ellipse à partir des extrémités de l\'un de ses axes et d\'un point de l\'ellipse. {{Version/fr|1.0}} : Il s\'agit du même outil que [Ellipse](Sketcher_CreateEllipseByCenter/fr.md) mais avec un mode initial différent.

-   <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Créer un rectangle :

  - <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [Rectangle](Sketcher_CreateRectangle/fr.md) : crée un rectangle. {{Version/fr|1.0}} : l\'outil dispose de quatre modes. Les coins arrondis et la création d\'une copie décalée sont des fonctions optionnelles.

  - <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [Rectangle centré](Sketcher_CreateRectangle_Center/fr.md) : crée un rectangle centré. {{Version/fr|1.0}} : il s\'agit du même outil que [Rectangle](Sketcher_CreateRectangle/fr.md) mais avec un mode initial différent.

  - <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [Rectangle arrondi](Sketcher_CreateOblong/fr.md) : crée un rectangle arrondi. Idem.

-   <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Créer un polygone régulier :

  - <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width:32px;"> [Triangle équilatéral](Sketcher_CreateTriangle/fr.md) : crée un triangle équilatéral. {{Version/fr|1.0}} : il s\'agit du même outil que [Polygone régulier](Sketcher_CreateRegularPolygon/fr.md) mais le nombre de côtés est prédéfini à une valeur spécifique.

  - <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> [Carré](Sketcher_CreateSquare/fr.md) : crée un carré. Idem.

  - <img alt="" src=images/Sketcher_CreatePentagon.svg  style="width:32px;"> [Pentagone](Sketcher_CreatePentagon/fr.md) : crée un pentagone. Idem.

  - <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [Hexagone](Sketcher_CreateHexagon/fr.md) : crée un hexagone. Idem.

  - <img alt="" src=images/Sketcher_CreateHeptagon.svg  style="width:32px;"> [Heptagone](Sketcher_CreateHeptagon/fr.md) : crée un heptagone. Idem.

  - <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width:32px;"> [Octogone](Sketcher_CreateOctagon/fr.md) : crée un octogone. Idem.

  - <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [Polygone régulier](Sketcher_CompCreateRegularPolygon/fr.md) : crée un polygone régulier. Le nombre de côtés peut être spécifié.

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Créer un contour oblong :

  - <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [Contour oblong](Sketcher_CreateSlot/fr.md) : crée un contour oblong.

  - <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:32px;"> [Rainure en arc](Sketcher_CreateArcSlot/fr.md) : crée une rainure en arc. {{Version/fr|1.0}}

-   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Créer une B-spline :

  - <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [B-spline simple](Sketcher_CreateBSpline/fr.md) : crée une B-spline par des points de contrôle. {{Version/fr|1.0}} : ou par des points de nœuds.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width:32px;"> [B-spline périodique](Sketcher_CreatePeriodicBSpline/fr.md) : crée une B-spline périodique (fermée) par des points de contrôle. {{Version/fr|1.0}} : c\'est le même outil que [B-spline des points de contrôle](Sketcher_CreateBSpline/fr.md) mais avec un mode initial différent.

  - <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:32px;"> [B-spline par des nœuds](Sketcher_CreateBSplineByInterpolation/fr.md) : crée une B-spline par des nœuds. Idem.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSplineByInterpolation.svg  style="width:32px;"> [B-spline périodique par des nœuds](Sketcher_CreatePeriodicBSplineByInterpolation/fr.md) : crée une B-spline périodique (fermée) par des nœuds. Idem.

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:32px;"> [Géométrie de construction](Sketcher_ToggleConstruction/fr.md) : permet de faire basculer les outils de création de géométrie en mode construction ou de faire basculer la géométrie sélectionnée en mode construction.



### Contraintes d\'esquisse 

Il s\'agit d\'outils permettant de créer des [contraintes](#Contraintes.md). Certaines contraintes nécessitent l\'utilisation de [contraintes d\'assistance](Sketcher_helper_constraint/fr.md).

-   <img alt="" src=images/Sketcher_Dimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Contraintes de dimension :

  - <img alt="" src=images/Sketcher_Dimension.svg  style="width:32px;"> [Dimension](Sketcher_Dimension/fr.md) : il s\'agit de l\'outil de contrainte contextuelle de l\'atelier Sketcher. En fonction de la sélection en cours, il propose des contraintes appropriées de dimension mais aussi des contraintes géométriques. {{Version/fr|1.0}}

  - <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:32px;"> [Distance horizontale](Sketcher_ConstrainDistanceX/fr.md) : fixe la distance horizontale entre deux points ou les extrémités d\'une ligne. Si un seul point est présélectionné, la distance est relative à l\'origine de l\'esquisse.

  - <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:32px;"> [Distance verticale](Sketcher_ConstrainDistanceY/fr.md) : fixe la distance verticale entre deux points ou les extrémités d\'une ligne. Si un seul point est présélectionné, la distance est relative à l\'origine de l\'esquisse.

  - <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:32px;"> [Distance](Sketcher_ConstrainDistance/fr.md) : fixe la longueur d\'une ligne, la distance entre deux points, la distance perpendiculaire entre un point et une ligne. {{Version/fr|0.21}}, la distance entre les arêtes de deux cercles ou arcs, ou entre l\'arête d\'un cercle ou d\'un arc et une ligne. {{Version/fr|1.0}}, la longueur d\'un arc.

  - <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [Rayon automatique](Sketcher_ConstrainRadiam/fr.md) : fixe le rayon des arcs et des cercles des poids des B-splines ainsi que le diamètre des cercles.

  - <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [Rayon ou poids](Sketcher_ConstrainRadius/fr.md) : fixe le rayon des cercles, des arcs et des cercles des poids des B-splines.

  - <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [Diamètre](Sketcher_ConstrainDiameter/fr.md) : fixe le diamètre des cercles et des arcs.

  - <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [Angle](Sketcher_ConstrainAngle/fr.md) : fixe l\'angle entre deux arêtes, l\'angle d\'une ligne avec l\'axe horizontal de l\'esquisse ou l\'angle d\'ouverture d\'un arc de cercle.

  - <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:32px;"> [Fixe](Sketcher_ConstrainLock/fr.md) : Applique les contraintes de [Distance horizontale](Sketcher_ConstrainDistanceX/fr.md) et [Distance verticale](Sketcher_ConstrainDistanceY/fr.md) aux points. Si un seul point est sélectionné, les contraintes font référence à l\'origine de l\'esquisse. Si deux points ou plus sont sélectionnés, les contraintes font référence au dernier point de la sélection.

-   <img alt="" src=images/Sketcher_ConstrainCoincidentUnified.svg  style="width:32px;"> [Coïncidence (unifiée)](Sketcher_ConstrainCoincidentUnified/fr.md) : crée une contrainte de coïncidence entre des points, fixe des points sur des arêtes ou des axes, ou crée une contrainte concentrique. Il combine les outils de [coïncidence](Sketcher_ConstrainCoincident/fr.md) et [point sur objet](Sketcher_ConstrainPointOnObject.md). {{Version/fr|1.0}}

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:32px;"> [Coïncidence](Sketcher_ConstrainCoincident/fr.md) : crée une contrainte de coïncidence entre des points ou une contrainte concentrique.

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:32px;"> [Point sur objet](Sketcher_ConstrainPointOnObject/fr.md) : fixe des points sur des arêtes ou des axes.

-   <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Contrainte horizontale/verticale :

  - <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:32px;"> [Horizontal/vertical](Sketcher_ConstrainHorVer/fr.md) : contraint les lignes ou les paires de points à être horizontales ou verticales, selon ce qui est le plus proche de l\'alignement actuel. L\'outil combine les outils de [contrainte horizontale](Sketcher_ConstrainHorizontal/fr.md) et [contrainte verticale](Sketcher_ConstrainVertical/fr.md). {{Version/fr|1.0}}

  - <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:32px;"> [Horizontal](Sketcher_ConstrainHorizontal/fr.md) : contraint les lignes ou les paires de points à être horizontales.

  - <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:32px;"> [Vertical](Sketcher_ConstrainVertical/fr.md) : contraint les lignes ou les paires de points à être verticales.

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:32px;"> [Parallèle](Sketcher_ConstrainParallel/fr.md) : contraint les lignes à être parallèles.

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:32px;"> [Perpendiculaire](Sketcher_ConstrainPerpendicular/fr.md) : contraint deux lignes à être perpendiculaires, ou deux arêtes, ou une arête et un axe, à être perpendiculaires à leur intersection. La contrainte peut également relier deux arêtes, les obligeant à être perpendiculaires au niveau de la jonction.

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:32px;"> [Tangente](Sketcher_ConstrainTangent/fr.md) : contraint deux arêtes, ou une arête et un axe, à être tangentes. La contrainte peut également relier deux arêtes, les obligeant à être tangentes au niveau de la jonction. Si deux lignes sont sélectionnées, elles deviennent colinéaires.

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:32px;"> [Égalité](Sketcher_ConstrainEqual/fr.md) : contraint les arêtes à avoir la même longueur (lignes) ou la même courbure (autres arêtes sauf B-splines).

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:32px;"> [Symétrie](Sketcher_ConstrainSymmetric/fr.md) : contraint deux points à être symétriques par rapport à une ligne ou un axe, ou par rapport à un troisième point.

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:32px;"> [Blocage](Sketcher_ConstrainBlock/fr.md) : bloque les arêtes en place avec une seule contrainte. Il est principalement destiné aux B-splines.

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:32px;"> [Contrainte de réfraction](Sketcher_ConstrainSnellsLaw/fr.md) : contraint deux lignes à suivre la loi de réfraction de la lumière lorsqu\'elle pénètre à travers une interface.

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Activer/désactiver les contraintes pilotantes/pilotées :

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:32px;"> [Contraintes pilotantes](Sketcher_ToggleDrivingConstraint/fr.md) : active/désactive les outils de création de contraintes de dimension entre le mode pilotant et le mode piloté, ou fait basculer les contraintes de dimension sélectionnées entre ces modes.

-   <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [Activer les contraintes](Sketcher_ToggleActiveConstraint/fr.md) : active ou désactive les contraintes sélectionnées.



### Outils d\'esquisse 

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Créer un congé/chanfrein :

  - <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> [Congé](Sketcher_CreateFillet/fr.md) : crée un congé entre deux arêtes non parallèles. {{Version/fr|1.0}} : l\'outil peut également créer un chanfrein.

  - <img alt="" src=images/Sketcher_CreateChamfer.svg  style="width:32px;"> [Chanfrein](Sketcher_CreateChamfer/fr.md) : crée un chanfrein entre deux arêtes non parallèles. Il s\'agit du même outil que [Congé](Sketcher_CreateFillet/fr.md) mais avec un mode initial différent. {{Version/fr|1.0}}

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Ajuster une arête :

  - <img alt="" src=images/Sketcher_Trimming.svg  style="width:32px;"> [Ajuster](Sketcher_Trimming/fr.md) : ajuste une arête aux intersections les plus proches avec d\'autres arêtes.

  - <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [Diviser](Sketcher_Split/fr.md) : divise une arête tout en transférant la plupart des contraintes.

  - <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [Prolonger](Sketcher_Extend/fr.md) : prolonge ou raccourcit une ligne ou un arc jusqu\'à un emplacement arbitraire, ou jusqu\'à une arête ou un point cible.

-   <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [Géométrie externe](Sketcher_External/fr.md) : projette sur le plan de l\'esquisse des arêtes et/ou des sommets appartenant à des objets situés en dehors de l\'esquisse. {{VersionMinus/fr|1.0}}

-   <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Géométrie externe :

  - <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"> [Projection](Sketcher_Projection/fr.md) : crée les arêtes de projection de la géométrie externe. {{Version/fr|1.1}}

  - <img alt="" src=images/Sketcher_Intersection.svg  style="width:32px;"> [Intersection](Sketcher_Intersection/fr.md) : crée les arêtes d\'intersection de la géométrie externe avec le plan de l\'esquisse. {{Version/fr|1.1}}

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [Copie carbone](Sketcher_CarbonCopy/fr.md) : copie toutes les géométries et contraintes d\'une autre esquisse dans l\'esquisse active.

-   <img alt="" src=images/Sketcher_SelectOrigin.svg  style="width:32px;"> [Selectionner l\'origine](Sketcher_SelectOrigin/fr.md) : sélectionne l\'origine de l\'esquisse.

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg  style="width:32px;"> [Axe horizontal](Sketcher_SelectHorizontalAxis/fr.md) : sélectionne l\'axe horizontal de l\'esquisse.

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg  style="width:32px;"> [Axe vertical](Sketcher_SelectVerticalAxis/fr.md) : sélectionne l\'axe vertical de l\'esquisse.

-   <img alt="" src=images/Sketcher_Translate.svg  style="width:32px;"> [Déplacer/dupliquer](Sketcher_Translate/fr.md) : déplace ou permet de créer des copies des éléments sélectionnés. {{Version/fr|1.0}}

-   <img alt="" src=images/Sketcher_Rotate.svg  style="width:32px;"> [Pivoter/dupliquer](Sketcher_Rotate/fr.md) : fait pivoter ou permet de créer des copies pivotées des éléments sélectionnés. {{Version/fr|1.0}}

-   <img alt="" src=images/Sketcher_Scale.svg  style="width:32px;"> [Mise à l\'échelle](Sketcher_Scale/fr.md): met à l\'échelle ou permet de créer des copies mises à l\'échelle des éléments sélectionnés. {{Version/fr|1.0}}

-   <img alt="" src=images/Sketcher_Offset.svg  style="width:32px;"> [Décaler une géométrie](Sketcher_Offset/fr.md) : crée des arêtes équidistantes autour d\'arêtes sélectionnés. {{Version/fr|1.0}}

-   <img alt="" src=images/Sketcher_Symmetry.svg  style="width:32px;"> [Symétriser](Sketcher_Symmetry/fr.md) : crée des copies de manière symétrique des éléments sélectionnés.

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [Supprimer l\'alignement des axes](Sketcher_RemoveAxesAlignment/fr.md) : supprime l\'alignement des axes des arêtes sélectionnées en remplaçant les contraintes [horizontales](Sketcher_ConstrainHorizontal/fr.md) et [verticales](Sketcher_ConstrainVertical/fr.md) par des contraintes [parallèles](Sketcher_ConstrainParallel/fr.md) et [perpendiculaires](Sketcher_ConstrainPerpendicular/fr.md).

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width:32px;"> [Supprimer tous les éléments de géométrie](Sketcher_DeleteAllGeometry/fr.md) : supprime toute la géométrie et toutes les contraintes de l\'esquisse.

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width:32px;"> [Supprimer toutes les contraintes](Sketcher_DeleteAllConstraints/fr.md) : supprime toutes les contraintes de l\'esquisse.

-   <img alt="" src=images/Edit-copy.svg  style="width:32px;"> Copier dans Sketcher : voir [Copier, couper et coller](#Copier,_couper_et_coller.md).

-   <img alt="" src=images/Edit-copy.svg  style="width:32px;"> Couper dans Sketcher : voir [Copier, couper et coller](#Copier,_couper_et_coller.md).

-   <img alt="" src=images/Edit-copy.svg  style="width:32px;"> Coller dans Sketcher : voir [Copier, couper et coller](#Copier,_couper_et_coller.md).



### Outils d\'esquisse des B-splines 

-   <img alt="" src=images/Sketcher_BSplineConvertToNURBS.svg  style="width:32px;"> [Convertir une géométrie en B-splines](Sketcher_BSplineConvertToNURBS/fr.md) : convertit les arêtes en B-splines.

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Augmenter le degré](Sketcher_BSplineIncreaseDegree/fr.md) : augmente le degré (l\'ordre) des B-splines.

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Diminuer le degré](Sketcher_BSplineDecreaseDegree/fr.md) : diminue le degré (l\'ordre) des B-splines.

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Augmenter la multiplicité des nœuds](Sketcher_BSplineIncreaseKnotMultiplicity/fr.md) : augmente la multiplicité d\'un nœud d\'une B-spline.

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Diminuer la multiplicité des nœuds](Sketcher_BSplineDecreaseKnotMultiplicity/fr.md) : diminue la multiplicité d\'un nœud d\'une B-spline.

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Insérer un nœud](Sketcher_BSplineInsertKnot/fr.md) : insère un nœud dans une B-spline ou augmente la multiplicité d\'un nœud existant.

-   <img alt="" src=images/Sketcher_JoinCurves.svg  style="width:32px;"> [Joindre des courbes](Sketcher_JoinCurves/fr.md) : crée une B-spline en joignant deux B-splines existantes ou d\'autres arêtes. {{Version/fr|0.21}}



### Affichage

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [Degrés de liberté non contraints](Sketcher_SelectElementsWithDoFs/fr.md) : sélectionne les éléments non entièrement contraints dans l\'esquisse.

-   <img alt="" src=images/Sketcher_SelectConstraints.svg  style="width:32px;"> [Contraintes associées](Sketcher_SelectConstraints/fr.md) : sélectionne les contraintes associées aux éléments de l\'esquisse.

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg  style="width:32px;"> [Éléments associés aux contraintes](Sketcher_SelectElementsAssociatedWithConstraints/fr.md) : sélectionne les éléments de l\'esquisse associés aux contraintes.

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width:32px;"> [Contraintes redondantes](Sketcher_SelectRedundantConstraints/fr.md) : sélectionne les contraintes redondantes dans l\'esquisse.

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width:32px;"> [Contraintes conflictuelles](Sketcher_SelectConflictingConstraints/fr.md) : sélectionne les contraintes conflictuelles de l\'esquisse.

-   <img alt="" src=images/Sketcher_ArcOverlay.svg  style="width:32px;"> [Cercle auxiliaire pour les arcs](Sketcher_ArcOverlay/fr.md) : affiche ou masque les aides circulaires (cercles virtuels sous-jacents) pour les arcs dans toutes les esquisses. {{Version/fr|1.0}}

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Afficher/masquer les informations d\'une B-spline :

-   <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [Degré de la B-spline](Sketcher_BSplineDegree/fr.md) : affiche ou masque le degré des B-splines dans toutes les esquisses.

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [Polygone de contrôle](Sketcher_BSplinePolygon/fr.md) : affiche ou masque le polygone de contrôle des B-splines dans toutes les esquisses.

-   <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [Peigne de courbure](Sketcher_BSplineComb/fr.md) : affiche ou masque le peigne de courbure des B-splines dans toutes les esquisses.

-   <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [Multiplicité des nœuds](Sketcher_BSplineKnotMultiplicity/fr.md) : affiche ou masque la multiplicité des nœuds des B-splines dans toutes les esquisses.

-   <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [Poids des points de contrôle](Sketcher_BSplinePoleWeight/fr.md) : affiche ou masque le poids des points de contrôle des B-splines dans toutes les esquisses.

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:32px;"> [Géométrie interne d\'alignement](Sketcher_RestoreInternalAlignmentGeometry/fr.md) : supprime la géométrie interne des éléments ou recrée la géométrie interne manquante.

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width:32px;"> [Espace virtuel](Sketcher_SwitchVirtualSpace/fr.md) : masque/démasque les contraintes ou active/désactive l\'espace virtuel visible.



### Outils obsolète 

-   <img alt="" src=images/Sketcher_Clone.svg  style="width:32px;"> [Cloner](Sketcher_Clone/fr.md) : clone un élément. Non disponible dans {{VersionPlus/fr|1.0}}.

-   <img alt="" src=images/Sketcher_CloseShape.svg  style="width:32px;"> [Fermer la forme](Sketcher_CloseShape/fr.md) : ferme une forme en appliquant des contraintes coïncidentes aux points d\'arrivée. Non disponible dans la ({{VersionPlus/fr|0.21}}).

-   <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:32px;"> [Congé avec contrainte](Sketcher_CreatePointFillet/fr.md) : crée un congé entre deux lignes non parallèles tout en préservant leur point d\'angle. Non disponible dans {{VersionPlus/fr|1.0}}.

-   <img alt="" src=images/Sketcher_ConnectLines.svg  style="width:32px;"> [Connecter les côtés](Sketcher_ConnectLines/fr.md) : connecte les éléments en appliquant des contraintes de coïncidence aux points d\'arrivée. Non disponible dans la ({{VersionPlus/fr|0.21}}).

-   <img alt="" src=images/Sketcher_Copy.svg  style="width:32px;"> [Copier](Sketcher_Copy/fr.md) : copie un élément. Non disponible dans {{VersionPlus/fr|1.0}}.

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Déplacer](Sketcher_Move/fr.md) : déplace la géométrie sélectionnée en prenant comme référence le dernier point sélectionné. Non disponible dans {{VersionPlus/fr|1.0}}.

-   <img alt="" src=images/Sketcher_RectangularArray.svg  style="width:32px;"> [Répétition linéaire](Sketcher_RectangularArray/fr.md) : crée une répétition à partir d\'éléments sélectionnés. Non disponible dans {{VersionPlus/fr|1.0}}.



## Préférences

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Préférences\...](Sketcher_Preferences/fr.md) : préférences pour l\'atelier Sketcher.



## Bonnes pratiques 

Chaque utilisateur de CAO développe sa propre méthode de travail au fil du temps, mais il existe quelques principes généraux utiles à suivre.

-   Une série d\'esquisses simples est plus facile à gérer qu\'une seule esquisse complexe. Par exemple, une première esquisse peut être créée pour l\'élément 3D de base (un tampon ou une rotation), tandis qu\'une deuxième peut contenir des trous ou des découpes (poches). Certains détails peuvent être laissés de côté, pour être réalisés ultérieurement en tant qu\'éléments 3D. Vous pouvez choisir d\'éviter les congés dans votre esquisse s\'il y en a trop, et les ajouter en tant qu\'élément 3D.
-   Créez toujours un profil fermé, sinon votre esquisse ne produira pas un solide, mais plutôt un ensemble de faces ouvertes. Si vous ne souhaitez pas que certains objets soient inclus dans la création du solide, transformez-les en éléments de construction avec l\'outil Mode de construction.
-   Utilisez la fonction de contraintes automatiques pour limiter le nombre de contraintes que vous devrez ajouter manuellement.
-   En règle générale, appliquez d\'abord les contraintes géométriques, puis les contraintes dimensionnelles, et verrouillez votre esquisse en dernier. Mais n\'oubliez pas : les règles sont faites pour être transgressées. Si vous avez du mal à manipuler votre esquisse, il peut être utile de contraindre quelques objets avant de compléter votre profil.
-   Si possible, centrez votre esquisse par rapport à l\'origine (0,0) avec la contrainte de verrouillage. Si votre esquisse n\'est pas symétrique, localisez l\'un de ses points par rapport à l\'origine ou choisissez de jolis chiffres ronds pour les distances de verrouillage.
-   Si vous avez la possibilité de choisir entre la contrainte de longueur et les contraintes de distance horizontale ou verticale, préférez ces dernières. Les contraintes de distance horizontale et verticale sont moins coûteuses en termes de calcul.
-   En général, les meilleures contraintes à utiliser sont : Contraintes horizontales et verticales ; Contraintes de longueur horizontales et verticales ; Tangence point à point. Si possible, limitez l\'utilisation de ces contraintes : la contrainte générale de longueur ; la tangence bord à bord ; la contrainte de fixation du point sur une ligne ; la contrainte de symétrie.
-   En cas de doute sur la validité d\'une esquisse une fois qu\'elle est terminée (les caractéristiques deviennent vertes), fermez la fenêtre de dialogue de Sketcher et utilisez <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:24px;"> [Valider une esquisse](Sketcher_ValidateSketch/fr.md).



## Tutoriels

-   [Sketcher Lecture](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) par chrisb. Il s\'agit d\'un document PDF de plus de 80 pages qui sert de manuel détaillé pour Sketcher. Il explique les bases de l\'utilisation de Sketcher et entre dans les détails de la création de formes géométriques et de chacune des contraintes.
-   [Sketcher : Tutoriel d\'introduction](Basic_Sketcher_Tutorial/fr.md) pour débutants
-   [Sketcher : Micro-tutoriel - Les pratiques de contraintes](Sketcher_Micro_Tutorial_-_Constraint_Practices/fr.md)
-   [Sketcher : Requis pour une esquisse](Sketcher_requirement_for_a_sketch/fr.md) : exigences minimales pour une esquisse et défintion d\'une esquisse.



## Script

La page [Sketcher : Écrire des scripts](Sketcher_scripting/fr.md) contient des exemples sur la façon de créer des contraintes à partir de scripts Python.



## Exemples

Pour avoir une idée de ce qui peut être réalisé avec les outils de Sketcher, jetez un coup d\'œil aux [Sketcher Exemples](Sketcher_Examples/fr.md) :

<img alt="" src=images/Sketcher_ExampleHinge-01.gif  style="width:80px;"> <img alt="" src=images/Sketcher_ExampleHinge-15.png  style="width:90px;">





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Sketcher Workbench/fr
