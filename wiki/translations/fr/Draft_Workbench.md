# <img alt="Icône de l\'atelier Draft" src=images/Workbench_Draft.svg  style="width:64px;"> Draft Workbench/fr


{{TOCright}}

## Introduction

L\'<img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> **atelier Draft** est principalement axé sur la création et la modification d\'objets 2D dans FreeCAD. Mais il n\'est pas limité au plan XY du système de coordonnées global. Ses objets peuvent avoir n\'importe quelle orientation et position dans l\'espace 3D et certains objets Draft peuvent être soit planaires, soit non planaires.

Les objets Draft peuvent être utilisés pour le dessin général, de manière similaire à ce que l\'on peut faire avec Inkscape ou AutoCAD. Mais ils peuvent également servir de base à la création d\'objets 3D dans d\'autres environnements de travail. Une [Draft Polyligne](Draft_Wire/fr.md) peut définir le tracé d\'un [Arch Mur](Arch_Wall/fr.md), un [Draft Polygone](Draft_Polygon/fr.md) peut être extrudé avec [Part Extrusion](Part_Extrude/fr.md), etc. La plupart des [outils de modification de Draft](#Modification.md) peuvent être appliqués à des objets 2D et 3D créés avec d\'autres ateliers. Vous pouvez, par exemple, [déplacer](Draft_Move/fr.md) une [esquisse](Sketcher_Workbench/fr.md) ou créer un [Draft Réseau orthogonal](Draft_OrthoArray/fr.md) à partir d\'un objet [Part](Part_Workbench/fr.md).

L\'atelier Draft fournit également des outils pour définir un [plan de travail](Draft_SelectPlane/fr.md), une [grille](Draft_Snap_Grid/fr.md) et un [système d\'aimantaion](Draft_Snap/fr.md) pour contrôler précisément la position de la géométrie.

Si votre objectif principal est la production de dessins 2D complexes et de fichiers [DXF](DXF/fr.md) et que vous n\'avez pas besoin de modélisation 3D, FreeCAD n\'est peut-être pas le bon choix pour vous. Vous pouvez envisager d\'utiliser un logiciel dédié au dessin technique, tel que [LibreCAD](https://fr.wikipedia.org/wiki/LibreCAD) ou [QCad](https://fr.wikipedia.org/wiki/QCad).

![](images/Draft_Workbench_Example.png ) 
*L'image montre la [grille](Draft_Snap_Grid/fr.md) alignée avec le plan XY.<br>
A gauche, en blanc, plusieurs objets planaires.<br>
À droite, une [Draft Polyligne](Draft_Wire/fr.md) non planaire utilisé comme objet de chemin d'un [Draft Réseau selon une courbe](Draft_PathArray/fr.md).*



## Planche à dessin 

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Ligne](Draft_Line/fr.md) : crée une ligne droite.

-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Polyligne](Draft_Wire/fr.md) : crée une polyligne, une séquence de plusieurs segments de ligne connectés.

-   <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> [Congé](Draft_Fillet/fr.md) : crée un congé, un coin arrondi, ou un chanfrein, un bord droit, entre deux [Draft Lignes](Draft_Line/fr.md).

-   <img alt="" src=images/Draft_Arc.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Outils Arc :

  - <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Arc](Draft_Arc/fr.md) : crée un arc de cercle à partir d\'un centre, d\'un rayon, d\'un angle de départ et d\'un angle d\'ouverture.

  - <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Arc par 3 points](Draft_Arc_3Points/fr.md) : crée un arc de cercle à partir de trois points qui définissent sa circonférence.

-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Cercle](Draft_Circle/fr.md) : crée un cercle à partir d\'un centre et d\'un rayon.

-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellipse](Draft_Ellipse/fr.md) : crée une ellipse à partir de deux points définissant un rectangle dans lequel l\'ellipse s\'inscrira.

-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rectangle](Draft_Rectangle/fr.md) : crée un rectangle à partir de deux points.

-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Polygone](Draft_Polygon/fr.md) : crée un polygone régulier à partir d\'un centre et d\'un rayon.

-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [B-spline](Draft_BSpline/fr.md) : crée une courbe B-spline à partir de plusieurs points.

-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Outils de Bézier :

  - <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Courbe de Bézier cubique](Draft_CubicBezCurve/fr.md) : crée une courbe de Bézier du troisième degré.

  - <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Courbe de Bézier](Draft_BezCurve/fr.md) : crée une courbe de Bézier à partir de plusieurs points.

-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Point](Draft_Point/fr.md) : crée un simple point.

-   <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Surfaces liées](Draft_Facebinder/fr.md) : crée un objet surface à partir des faces sélectionnées.

-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [Formes à partir de texte](Draft_ShapeString/fr.md) : crée une forme composée qui représente une chaîne de texte.

-   <img alt="" src=images/Draft_Hatch.svg  style="width:32px;"> [Hachure](Draft_Hatch/fr.md) : crée des hachures sur les faces planes d\'un objet sélectionné. {{Version/fr|0.20}}

## Annotation

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Texte](Draft_Text/fr.md) : crée un texte de plusieurs lignes à un point donné.

-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Dimension](Draft_Dimension/fr.md) : crée une dimension linéaire, une dimension radiale ou une dimension angulaire.

-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Étiquette](Draft_Label/fr.md) : crée un texte de plusieurs lignes avec une ligne de tête à deux segments et une flèche.

-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Éditeur de styles d\'annotations](Draft_AnnotationStyleEditor/fr.md) : permet de définir des styles qui affectent les propriétés visuelles des objets de type annotation.

## Modification

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Déplacer](Draft_Move/fr.md) : déplace ou copie les objets sélectionnés d\'un point à un autre.

-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Pivoter](Draft_Rotate/fr.md) : fait pivoter ou copie les objets sélectionnés autour d\'un point central selon un angle donné.

-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Échelle](Draft_Scale/fr.md) : met à l\'échelle ou copie les objets sélectionnés autour d\'un point de base.

-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Miroir](Draft_Mirror/fr.md) : crée des copies miroir à partir des objets sélectionnés.

-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Décalage](Draft_Offset/fr.md) : décale chaque segment d\'un objet sélectionné sur une distance donnée ou crée une copie décalée de l\'objet sélectionné.

-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Ajuster ou prolonger](Draft_Trimex/fr.md) : coupe ou étend un objet sélectionné.

-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Étirer](Draft_Stretch/fr.md) : étire les objets en déplaçant les points sélectionnés.

-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Cloner](Draft_Clone/fr.md) : crée des copies liées, des clones, des objets sélectionnés.

-   <img alt="" src=images/Draft_OrthoArray.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Outils Réseau :

  - <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [Réseau orthogonal](Draft_OrthoArray/fr.md) : crée un réseau orthogonal à partir d\'un objet sélectionné. Cela peut éventuellement créer un réseau de [Link](App_Link/fr.md).

  - <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> [Réseau polaire](Draft_PolarArray/fr.md) : crée un réseau à partir d\'un objet sélectionné en plaçant des copies le long d\'une circonférence. Cela peut éventuellement créer un réseau de [Link](App_Link/fr.md).

  - <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> [Réseau circulaire](Draft_CircularArray/fr.md) : crée un réseau à partir d\'un objet sélectionné en plaçant des copies le long de circonférences concentriques. Cela peut éventuellement créer un réseau de [Link](App_Link/fr.md).

  - <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Réseau selon une courbe](Draft_PathArray/fr.md) : crée un réseau à partir d\'un objet sélectionné en plaçant des copies le long d\'un tracé.

  - <img alt="" src=images/Draft_PathLinkArray.svg  style="width:32px;"> [Réseau lié selon une courbe](Draft_PathLinkArray/fr.md) : idem, mais crée un réseau de [Link](App_Link/fr.md) au lieu d\'un réseau normal.

  - <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Réseau de points](Draft_PointArray/fr.md) : crée un réseau à partir d\'un objet sélectionné en plaçant des copies aux points d\'un composé de points.

  - <img alt="" src=images/Draft_PointLinkArray.svg  style="width:32px;"> [Réseau lié selon des points](Draft_PointLinkArray/fr.md) : idem, mais crée un réseau de [Link](App_Link/fr.md) au lieu d\'un réseau normal.

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Éditer](Draft_Edit/fr.md) : met les objets sélectionnés en mode d\'édition de Draft. Dans ce mode, les propriétés des objets peuvent être modifiées graphiquement.

-   <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:32px;"> [Surligner les sous éléments](Draft_SubelementHighlight/fr.md) : met temporairement en évidence les objets sélectionnés ou les objets de base des objets sélectionnés.

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Joindre](Draft_Join/fr.md) : joint des [Draft Lignes](Draft_Line/fr.md) et des [Draft Polylignes](Draft_Wire/fr.md) en une seule ligne.

-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Scinder](Draft_Split/fr.md) : divise une [Draft Ligne](Draft_Line/fr.md) ou une [Draft Polyligne](Draft_Wire/fr.md) à un point ou un bord spécifié.

-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Agréger](Draft_Upgrade/fr.md) : agrège les objets sélectionnés.

-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Désagréger](Draft_Downgrade/fr.md) : déclasse les objets sélectionnés.

-   <img alt="" src=images/Draft_WireToBSpline.svg  style="width:32px;"> [Polyligne vers B-spline](Draft_WireToBSpline/fr.md) : convertit des [Draft Polylignes](Draft_Wire/fr.md) en [Draft BSplines](Draft_BSpline/fr.md) et vice versa.

-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Draft vers Esquisse](Draft_Draft2Sketch/fr.md): convertit les objets [Draft](Draft_Workbench/fr.md) en [Sketcher Esquisses](Sketcher_NewSketch/fr.md) et vice versa.

-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Pente](Draft_Slope/fr.md) : incline les [Draft Lignes](Draft_Line/fr.md) ou les [Draft Polylignes](Draft_Wire.md) sélectionnés en augmentant ou en diminuant, la coordonnée Z de tous les points après le premier.

-   <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> [Inverser la direction de la cote](Draft_FlipDimension/fr.md) : fait pivoter le texte de la dimension des [Draft Dimensions](Draft_Dimension/fr.md) sélectionnées de 180° autour de la ligne de cote.

-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Vue 2D d\'une forme](Draft_Shape2DView/fr.md) : crée des projections 2D à partir des objets sélectionnés.



## La barre de Draft 

[Draft La barre](Draft_Tray/fr.md) permet de sélectionner le plan de travail, de définir les paramètres de style, de passer en mode construction et de spécifier le calque ou le groupe actif.

![](images/Draft_tray_default.png )

-   ![](images/Draft_tray_button_plane.png ) [Plan de travail](Draft_SelectPlane/fr.md) : sélectionne le plan de travail Draft en cours. Egalement disponible dans le menu : **Draft → Utilitaires → <img src="images/Draft_SelectPlane.svg" width=16px> Sélectionnez un plan**.

-   ![](images/Draft_tray_button_style.png ) [Définir le style](Draft_SetStyle/fr.md) : définit le style par défaut pour les nouveaux objets. Egalement disponible dans le menu : **Draft → Utilitaires → <img src="images/Draft_SetStyle.svg" width=16px> Définir le style**.

-   ![](images/Draft_tray_button_construction.png ) [Basculer en mode construction](Draft_ToggleConstructionMode/fr.md) : active ou désactive le mode de construction de Draft. Egalement disponible dans le menu : **Draft → Utilitaires → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Basculer en mode construction**.

-   ![](images/Draft_tray_button_layer.png ) [Groupement automatique](Draft_AutoGroup/fr.md) : change le [Draft Calque](Draft_Layer/fr.md) actif ou, accessoirement, le [Std Groupe](Std_Group/fr.md) actif ou un objet de type groupe [Arch](Arch_Workbench/fr.md).



## Widget d\'échelle d\'annotation de Draft 

Avec le [Draft Widget d\'échelle d\'annotation](Draft_annotation_scale_widget/fr.md), l\'échelle d\'annotation Draft peut être spécifiée.

![](images/Draft_annotation_scale_widget_button.png )



## Widget d\'aimantation de Draft 

Le [Draft Widget d\'aimantation](Draft_snap_widget/fr.md) peut être utilisé comme alternative à la [Barre d\'outils d\'aimantation de Draft](#Barre_d.27outils_d.27aimantation_de_Draft.md).

![](images/Draft_snap_widget_button.png )



## Barre d\'outils d\'aimantation de Draft 

La barre d\'outils Draft Aimantation permet de sélectionner les options actives d\'aimantation. Les boutons appartenant aux options actives restent enfoncés. Pour des informations générales sur l\'aimantation, voir : [Draft Aimantation](Draft_Snap/fr.md).

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Verrouillage de l\'aimantation](Draft_Snap_Lock/fr.md) : active ou désactive l\'aimantation de manière globale.

-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Aimantation Terminaison](Draft_Snap_Endpoint/fr.md): aimante aux extrémités des segments.

-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Aimantation Milieu](Draft_Snap_Midpoint/fr.md) : aimante au point milieu des segments.

-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Aimantation Centre](Draft_Snap_Center/fr.md) : aimante au point central des faces et des arêtes circulaires et au point {{PropertyData/fr|Placement}} de [Draft Proxy de plan de travail](Draft_WorkingPlaneProxy/fr.md) et [Arch Partie de bâtiment](Arch_BuildingPart/fr.md).

-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Aimantation Angle](Draft_Snap_Angle/fr.md) : aimante aux points cardinaux spéciaux des bords circulaires, aux multiples de 30° et 45°.

-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Aimantation Intersection](Draft_Snap_Intersection/fr.md): aimante à l\'intersection de deux bords.

-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Aimantation Perpendiculaire](Draft_Snap_Perpendicular/fr.md) : aimante aux points perpendiculaires sur les faces ({{Version/fr|1.0}}) et les arêtes.

-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Aimantation Extension](Draft_Snap_Extension/fr.md) : aimante à une ligne imaginaire qui s\'étend au-delà des extrémités des bords droits.

-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Aimantation Parallèle](Draft_Snap_Parallel/fr.md) : aimante à une ligne imaginaire parallèle aux bords droits.

-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Aimantation Spécial](Draft_Snap_Special/fr.md) : aimante à des points spéciaux définis par l\'objet.

-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Aimantation Le plus proche](Draft_Snap_Near/fr.md) : aimante au point le plus proche sur les faces et les bords.

-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Aimantation Orthogonal](Draft_Snap_Ortho/fr.md) : aimante sur des lignes imaginaires qui croisent le point précédent à des multiples de 45°.

-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Aimantation Grille](Draft_Snap_Grid/fr.md) : aimante aux intersections des lignes de la grille.

-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Aimantation Plan de travail](Draft_Snap_WorkingPlane/fr.md) : projette les points d\'aimantation sur le [plan de travail](Draft_SelectPlane/fr.md) en cours.

-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Aimantation Dimensions](Draft_Snap_Dimensions/fr.md) : montre les dimensions X et Y temporaires.

-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Basculer la grille](Draft_ToggleGrid/fr.md) : active ou désactive la grille.



## Outils utilitaires de la barre d\'outils de Draft 

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Calque](Draft_Layer/fr.md) : crée un [Draft Calque](Draft_Layer/fr.md).

-   <img alt="" src=images/Draft_AddNamedGroup.svg  style="width:32px;"> [Nommer un groupe](Draft_AddNamedGroup/fr.md) : crée un [Std Groupe](Std_Group/fr.md) nommé et déplace les objets sélectionnés vers ce groupe. {{Version/fr|0.20}}

-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> [Déplacer vers un groupe](Draft_AddToGroup/fr.md) : déplace les objets vers un [Std Groupe](Std_Group/fr.md). Il peut aussi dégrouper des objets.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Sélection groupée](Draft_SelectGroup/fr.md) : sélectionne le contenu des objets de type [Std Groupe](Std_Group/fr.md) ou des objets de type groupe de [Arch](Arch_Workbench/fr.md).

-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Ajouter au groupe de construction](Draft_AddConstruction/fr.md) : déplace les objets vers le [Draft mode construction](Draft_ToggleConstructionMode/fr.md).

-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Mode d\'affichage](Draft_ToggleDisplayMode/fr.md) : bascule la {{PropertyView/fr|Display Mode}} (mode d\'affichage) des objets sélectionnés entre {{Value|Flat Lines}} et {{Value|Wireframe}}.

-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Proxy de plan de travail](Draft_WorkingPlaneProxy/fr.md) : crée un proxy de plan de travail pour sauvegarder le [Draft Plan de travail](Draft_SelectPlane/fr.md).



## Outils supplémentaires 

Le menu **Draft → Utilitaires** contient plusieurs outils. La plupart d\'entre eux sont également accessibles depuis les barres d\'outils ou [Draft La barre](Draft_Tray/fr.md) et ont déjà été mentionnés ci-dessus. Pour les outils suivants, ce n\'est pas le cas :

-   <img alt="" src=images/Draft_ApplyStyle.svg  style="width:32px;"> [Appliquer le style](Draft_ApplyStyle/fr.md) : applique les paramètres du style en cours aux objets sélectionnés.

-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Réparer](Draft_Heal/fr.md) : répare les objets Draft problématiques trouvés dans de très vieux fichiers.

-   <img alt="" src=images/Draft_ToggleContinueMode.svg  style="width:32px;"> [Basculer en mode continu](Draft_ToggleContinueMode/fr.md) : active ou désactive le mode continu.

-   <img alt="" src=images/Draft_ShowSnapBar.svg  style="width:32px;"> [Barre d\'aimantation](Draft_ShowSnapBar/fr.md) : montre la [Draft Barre d\'aimantation](#Barre_d.27outils_d.27aimantation_de_Draft.md).



## Fonctions additionnelles 

-   [Plan de travail](Draft_SelectPlane/fr.md) : le plan dans la [vue 3D](3D_view/fr.md) où les nouveaux objets Draft sont créés.
-   [Aimantation](Draft_Snap/fr.md) : sélectionne des points géométriques exacts sur, ou définis par, des objets existants ou la grille.
-   [Contrainte](Draft_Constrain/fr.md) : pour chaque point suivant, vous pouvez contraindre le mouvement du curseur dans la direction X, Y ou Z.
-   [Mode de construction](Draft_ToggleConstructionMode/fr.md) : place les nouveaux objets Draft dans un groupe dédié, ce qui facilite leur masquage ou leur suppression.
-   [Motif](Draft_Pattern/fr.md) : les objets Draft ayant une propriété {{PropertyData/fr|Make Face}} peuvent afficher un motif SVG au lieu d\'une couleur unie.



## Menu contextuel de l\'arborescence 

Les options supplémentaires sont disponibles dans le menu contextuel de la [Vue en arborescence](Tree_view/fr.md) :



### Options par défaut 

Pour la plupart des objets Draft, l\'option suivante est disponible :

-   Editer : édite l\'objet. Selon le type d\'objet, on utilise soit [Draft Editer](Draft_Edit/fr.md) soit une solution d\'édition dédiée. {{Version/fr|1.0}}

S\'il y a un document actif, le menu contextuel contient un sous-menu supplémentaire :

-   Utilitaires : un sous-ensemble des outils disponibles dans le menu principal Draft Utilitaires.



### Options des lignes 

Pour une [Draft Ligne](Draft_Line/fr.md) et une [Draft Polyligne](Draft_Wire/fr.md), cette option supplémentaire est disponible :

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> Aplatir : aplatit la polyligne sur le [Draft Plan de travail](Draft_SelectPlane/fr.md) en cours. Cette option ne fonctionne pas correctement pour la {{VersionMinus/fr|0.19}}.



### Options du conteneur du calque 

Pour un [Draft Calque](Draft_Layer/fr.md), les options supplémentaires sont disponibles :

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Fusionner les calques en double](Draft_Layer/fr#Options_du_conteneur_du_calque.md) : fusionne tous les calques ayant le même libellé de base.

-   <img alt="" src=images/Draft_NewLayer.svg  style="width:32px;"> [Ajouter un nouveau calque](Draft_Layer/fr#Options_du_conteneur_du_calque.md) : ajoute un nouveau calque au document en cours.



### Options du calque 

Pour un [Draft Calque](Draft_Layer/fr.md), les options supplémentaires sont disponibles :

-   <img alt="" src=images/button_right.svg  style="width:32px;"> [Activer ce calque](Draft_AutoGroup/fr.md) : active le calque sélectionné.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Sélectionner le contenu du calque](Draft_SelectGroup/fr.md) : sélectionne les objets à l\'intérieur du calque sélectionné.



### Options du proxy du plan de travail 

Pour un [Draft Proxy de plan de travail](Draft_WorkingPlaneProxy/fr.md), les options supplémentaires sont disponibles :

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Écrire la position de la caméra](Draft_WorkingPlaneProxy/fr#Menu_contextuel.md) : met à jour la propriété **View Data** du proxy du plan de travail avec les paramètres en cours de la caméra de la [Vue 3D](3D_view/fr.md).

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Écriture de l\'état des objets](Draft_WorkingPlaneProxy/fr#Menu_contextuel.md) : met à jour la propriété **Visibility Map** du proxy du plan de travail avec l\'état de visibilité en cours des objets dans le document.



## Menu contextuel de la vue 3D 

Les options supplémentaires sont disponibles dans le menu contextuel de la [Vue 3D](3D_view/fr.md) :



### Options par défaut 

S\'il y a un document actif, le menu contextuel contient un sous-menu supplémentaire :

-   Utilitaires : un sous-ensemble des outils disponibles dans le menu principal Draft Utilitaires.



## Outils obsolète 

Ces commandes sont obsolètes mais toujours disponibles :

-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> [Réseau](Draft_Array/fr.md) : crée un réseau orthogonal à partir d\'un objet sélectionné. Le réseau créé peut être transformé en un [réseau polaire](Draft_PolarArray/fr.md) ou un [réseau circulaire](Draft_CircularArray/fr.md) en modifiant sa propriété **Array Type**. {{Obsolete/fr|0.19}}

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> [Dessin](Draft_Drawing/fr.md) : insère des vues des objets sélectionnés dans une page [Drawing](Drawing_Workbench/fr.md). {{Obsolete/fr|0.17}}



## Préférences

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [Draft Préférences](Draft_Preferences/fr.md) : préférences générales pour l\'atelier Draft.

-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Préférences d\'import-export](Import_Export_Preferences/fr.md) : préférences disponibles pour l\'importation et l\'exportation vers différents formats de fichiers.



## Formats de fichiers 

L\'atelier Draft fournit à FreeCAD des importateurs et des exportateurs pour différents formats de fichiers. Ceux-ci sont utilisés par les commandes [Std Importer](Std_Import/fr.md) et [Std Exporter](Std_Export/fr.md).

-   [Autodesk .DXF](Draft_DXF/fr.md) : importe et exporte les fichiers [DXF (Drawing eXchange Format)](http://fr.wikipedia.org/wiki/Drawing_eXchange_Format) créés avec d\'autres applications de CAO 2D. Voir aussi [Importation DXF et FreeCAD](FreeCAD_and_DXF_Import/fr.md).
-   [Autodesk .DWG](Draft_DXF/fr.md) : importe et exporte des fichiers DWG via un convertisseur DWG externe. Voir aussi [Importation FreeCAD et DWG](FreeCAD_and_DWG_Import/fr.md).
-   [Scalable Vector Graphics .SVG](Draft_SVG/fr.md) : importe et exporte les fichiers [Scalable Vector Graphics(SVG)](http://fr.wikipedia.org/wiki/Scalable_Vector_Graphics) créés avec des applications de dessin vectoriel
-   [Open Cad format .OCA](Draft_OCA/fr.md) : importe et exporte des fichiers [OCA/GCAD](http://groups.google.com/group/open_cad_format).
-   [Airfoil Data Format .DAT](Draft_DAT/fr.md) : importe des fichiers DAT décrivant des profils d\'ailes.



## Tests unitaires 

Voir aussi : [Atelier Test](Testing/fr.md).

Pour exécuter les tests unitaires du plan de travail, exécutez ce qui suit à partir du terminal du système d\'exploitation:


```python
freecad -t TestDraft
```



## Script

Voir aussi : [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) et [FreeCAD Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'atelier comprend un module pour créer des échantillons de tous les objets dans un nouveau document.

Utilisez-le pour tester que tous les objets sont produits correctement:


```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```

L\'inspection du code de ce module peut aider à comprendre l\'interface de programmation.



## Tutoriels

-   [Draft Tutoriel](Draft_tutorial/fr.md)
-   [Draft Tutoriel Forme à partir de texte](Draft_ShapeString_tutorial/fr.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Draft](Category_Draft.md) > Draft Workbench/fr
