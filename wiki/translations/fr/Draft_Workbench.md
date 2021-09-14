# Draft Workbench/fr




 

<img alt="Icône de l\'atelier Draft" src=images/Workbench_Draft.svg  style="width:128px;">


{{TOCright}}

## Introduction

L\'<img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> [atelier Draft](Draft_Workbench/fr.md) vous permet de dessiner des objets 2D simples et propose plusieurs outils pour les modifier par la suite. Il fournit également des outils pour définir un plan de travail, une grille et un système d\'accrochage permettant de contrôler avec précision la position de votre géométrie.

Les objets 2D créés peuvent être utilisés pour le dessin général d\'une manière similaire à celle réalisée avec Inkscape ou Autocad. Ces formes 2D peuvent également être utilisées comme composants de base d\'objets 3D créés avec d\'autres ateliers, par exemple, <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> l\'[atelier Part](Part_Workbench/fr.md) et <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> l\'[atelier Arch](Arch_Workbench/fr.md). La conversion des objets Draft en <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [Esquisses](Sketcher_Workbench/fr.md) est également possible, ce qui signifie que les formes peuvent également être utilisées avec <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> l\'[atelier PartDesign](PartDesign_Workbench/fr.md) pour la création de corps solides.

FreeCAD est avant tout une application de modélisation 3D et ses outils 2D ne sont donc pas aussi avancés que dans d\'autres programmes de dessin. Si votre objectif principal est la production de dessins 2D complexes et de fichiers [DXF](DXF/fr.md), et que vous n\'avez pas besoin de modélisation 3D, vous pouvez envisager un logiciel dédié à la rédaction technique, tel que [LibreCAD](https://fr.wikipedia.org/wiki/LibreCAD), [QCad](https://fr.wikipedia.org/wiki/QCad), [QCad](https://fr.wikipedia.org/wiki/QCad) ou et autres.

<img alt="Draft Workbench Example" src=images/Draft_Workbench_Example.png  style="width:400px;">

## Objets de dessin 

Les outils de création d\'objets.

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Ligne](Draft_Line/fr.md) : Trace un segment de ligne à partir de 2 points
-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Polyligne](Draft_Wire/fr.md) : Trace une ligne composée de plusieurs segments de lignes
-   <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> [Congé](Draft_Fillet/fr.md) : dessine un congé (coin arrondi) ou un chanfrein (ligne droite) entre deux simples [Lignes](Draft_Line/fr.md). {{Version/fr|0.19}}
-   <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Arc](Draft_Arc/fr.md) : Trace un segment d\'arc à partir du centre, rayon, angle de départ et angle d\'arrivée
-   <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Arc 3Points](Draft_Arc_3Points/fr.md) : dessine un segment d\'arc de cercle à partir de trois points situés dans la circonférence. {{Version/fr|0.19}}
-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Cercle](Draft_Circle/fr.md) : Trace un cercle à partir du centre et du rayon
-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellipse](Draft_Ellipse/fr.md) : Dessine une ellipse à partir de deux points opposés (coins)
-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rectangle](Draft_Rectangle/fr.md) : Dessine un rectangle à partir de deux points opposés
-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Polygone](Draft_Polygon/fr.md) : Dessine un polygone régulier à partir du centre et du rayon et nombre de côtés
-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [B-spline](Draft_BSpline/fr.md) : Dessine une courbe B-spline à partir d\'une série de points
-   <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Courbe de Bézier cubique](Draft_CubicBezCurve/fr.md) : dessine une courbe de Bézier du troisième degré en faisant glisser deux points. {{Version/fr|0.19}}
-   <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Courbes de Bezier](Draft_BezCurve/fr.md) : Dessine la courbe de Bézier à partir d\'une série de points
-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Point](Draft_Point/fr.md) : Insère un objet point
-   <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Surfaces liées](Draft_Facebinder/fr.md) : Crée un nouvel objet à partir de faces sélectionnées sur des objets existants.
-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [Formes à partir de texte](Draft_ShapeString/fr.md) : L\'outil Formes à partir de texte insère une forme composée, qui représente une chaîne de texte au point donné

## Annotation d\'objets 

-   <img alt="" src=images/Draft_Text.svg  style="width:32px;"> [Texte](Draft_Text/fr.md) : dessine une annotation de texte sur plusieurs lignes.
-   <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> [Dimension](Draft_Dimension/fr.md) : dessine une annotation de dimension.
-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Étiquette](Draft_Label/fr.md) : place une étiquette avec une flèche pointant vers un élément sélectionné. {{Version/fr|0.17}}
-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Éditeur de style d\'annotation](Draft_AnnotationStyleEditor/fr.md) : ouvre un éditeur pour changer le style d\'annotation de l\'objet. {{Version/fr|0.19}}

## Édition d\'objets 

Ces outils permettent de modifier des objets existants. Ils fonctionnent sur les objets sélectionnés, s\'il n\'y a aucune sélection, vous serez invité à en faire une.

De nombreux outils d\'opération (déplacer, faire pivoter, mettre en tableau, etc.) fonctionnent également sur des objets solides([Part](Part_Workbench/fr.md), [PartDesign](PartDesign_Workbench/fr.md), [Arch](Arch_Workbench/fr.md), etc.).

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Déplacer](Draft_Move/fr.md) : Déplace l\'objet (ou les objets) d\'un emplacement à un autre
-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Rotation](Draft_Rotate/fr.md) : Pivote l\'objet (ou les objets) d\'un angle de départ à un angle d\'arrivée
-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Redimensionner](Draft_Scale/fr.md) : Redimensionne l\'objet (ou les objets) sélectionné(s) à partir d\'un point de base
-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Miroir](Draft_Mirror/fr.md) : Crée un objet miroir des objets sélectionnés
-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Décalage](Draft_Offset/fr.md) : Déplace les segments d\'un objet à une certaine distance
-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Découper/prolonger (Trimex)](Draft_Trimex/fr.md) : Découpe ou prolonge un objet
-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Étirer](Draft_Stretch/fr.md) : Étire les objets sélectionnés {{Version/fr|0.17}}

-   <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Clone](Draft_Clone/fr.md) : clone les objets sélectionnés
-   <img alt="" src=images/Draft_Array.svg  style="width:32px;"> [Réseau](Draft_Array/fr.md): outils réseaux
    -   <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [Réseau orthogonal](Draft_OrthoArray.md) : crée un réseau orthogonal à partir de l\'objet sélectionné. Il peut également créer des copies [App Link](App_Link/fr.md). {{Version/fr|0.19}}
    -   <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> [Réseau polaire](Draft_PolarArray/fr.md) : crée un réseau polaire avec le motif, c\'est-à-dire un balayage un angulaire. Il peut également créer des copies [App Link](App_Link.md). {{Version/fr|0.19}}
    -   <img alt="" src=images/Draft_CircularArray.svg  style="width:32px;"> [Réseau circulaire](Draft_CircularArray/fr.md) : crée un réseau circulaire avec un motif, c\'est-à-dire en partant d\'un centre et en se déplaçant radialement vers l\'extérieur. Il peut également créer des copies [App Link](App_Link/fr.md). {{Version/fr|0.19}}
    -   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Réseau selon une courbe](Draft_PathArray/fr.md) : crée une réseau d\'objets le long d\'un tracé (chemin)
    -   <img alt="" src=images/Draft_PathLinkArray.svg  style="width:32px;"> [Réseau lié selon une courbe](Draft_PathLinkArray/fr.md) : comme <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Réseau selon une courbe](Draft_PathArray/fr.md) mais crée des [App Links](App_Link/fr.md) au lieu de copies régulières. {{Version/fr|0.19}}
    -   <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Matrice de points](Draft_PointArray/fr.md) : crée un tableau d\'objets en plaçant les copies sur certains points. {{Version/fr|0.18}}
    -   <img alt="" src=images/Draft_PointLinkArray.svg  style="width:32px;"> [Réseau lié selon des points](Draft_PointLinkArray/fr.md) : comme <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Matrice de points](Draft_PointArray/fr.md) mais crée des [App Links](App_Link/fr.md) au lieu de copies régulières. {{Version/fr|0.19}}

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> [Éditer](Draft_Edit/fr.md) : Édite un objet sélectionné
-   <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:32px;"> [Surligner les sous éléments](Draft_SubelementHighlight/fr.md) : Active un mode d'édition permettant d'éditer différents objets. {{Version/fr|0.19}}

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Joindre](Draft_Join/fr.md) : relie les lignes en un seul fil. {{Version/fr|0.18}}
-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Scinder](Draft_Split/fr.md) : divise un fil en deux. {{Version/fr|0.18}}
-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Mettre à niveau](Draft_Upgrade/fr.md) : joint des objets en un objet de plus haut niveau
-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Rétrograder](Draft_Downgrade/fr.md) : explose des objets en objets de niveau inférieur

-   <img alt="" src=images/Draft_WireToBSpline.svg  style="width:32px;"> [Filaire vers B-Spline](Draft_WireToBSpline/fr.md) : convertit un filaire (Wire) en une courbe B-Spline et vice versa.
-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Draft vers Esquisse](Draft_Draft2Sketch/fr.md) : convertit un objet Draft en esquisse dans l\'[atelier Sketcher](Sketcher_Workbench/fr.md) et vice versa.
-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Pente](Draft_Slope/fr.md) : modifie la pente d\'élévation de la [Draft Ligne ](Draft_Line/fr.md) ou du [Draft Fil](Draft_Wire/fr.md) sélectionné. {{Version/fr|0.17}}
-   <img alt="" src=images/Draft_FlipDimension.svg  style="width:32px;"> [Inverser la direction de la cote](Draft_FlipDimension/fr.md) : inverse l\'orientation du texte d\'une [Draft Dimension](Draft_Dimension/fr.md).

-   <img alt="" src=images/Draft_Shape2DView.svg  style="width:32px;"> [Vue 2D d\'une forme](Draft_Shape2DView/fr.md) : Génère une projection 2D à partir d\'un objet 3D.

## Barre d\'outils Plan de travail de Draft 

La barre d\'outils Plan de travail de Draft apparaît au démarrage de l\'atelier et permet de sélectionner le plan de travail, ainsi que certaines propriétés visuelles telles que la couleur des lignes, la couleur des formes, la taille du texte, la largeur des lignes et le groupe automatique.

![](images/Draft_tray_default.png )

Its tools are also available in the **Draft → Utilities** menu:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Plan de travail](Draft_SelectPlane/fr.md) : définit un plan de travail à partir d\'une vue standard ou d\'une face sélectionnée.
-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;"> [Basculer le mode de construction](Draft_ToggleConstructionMode/fr.md) : active ou désactive le mode de construction Draft.
-   <img alt="" src=images/Draft_ApplyStyle.svg  style="width:32px;"> [Appliquer le style](Draft_ApplyStyle/fr.md) : applique le style et la couleur actuels aux objets sélectionnés.
-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> [Groupe automatique](Draft_AutoGroup/fr.md) : place automatiquement de nouveaux objets dans un <img alt="" src=images/Std_Group.svg  style="width:32px;"> [Std Group](Std_Group/fr.md), <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Draft Calque](Draft_Layer/fr.md), ou l\'un des objets de type groupe de l\'[atelier Arch](Arch_Workbench/fr.md) comme <img alt="" src=images/Arch_BuildingPart.svg  style="width:32px;"> [Arch Partie de bâtiment](Arch_BuildingPart/fr.md). {{Version/fr|0.17}}

-   <img alt="" src=images/Draft_SetStyle.svg  style="width:32px;"> [Set style](Draft_SetStyle.md): sets the default style for new objects. <small>(v0.19)</small> 

-   <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:32px;"> [Toggle construction mode](Draft_ToggleConstructionMode.md): switches Draft construction mode on or off.

-   <img alt="" src=images/Draft_AutoGroup.svg  style="width:32px;"> [AutoGroup](Draft_AutoGroup.md): changes the active [Draft Layer](Draft_Layer.md) or, optionally, the active [Std Group](Std_Group.md) or group-like [Arch](Arch_Workbench.md) object.

## Draft annotation scale widget 

With the [Draft annotation scale widget](Draft_annotation_scale_widget.md) the Draft annotation scale can be specified. <small>(v0.19)</small> 

![](images/Draft_annotation_scale_widget_button.png )

## Draft snap widget 

The [Draft snap widget](Draft_snap_widget.md) can be used as an alternative for the [Draft Snap toolbar](#Draft_snap_toolbar.md). <small>(v0.19)</small> 

![](images/Draft_snap_widget_button.png )

## Barre d\'outils Accrochage de Draft 

La barre d\'outils [Draft Accrochage](Draft_Snap/fr.md) permet de sélectionner le mode d\'accrochage. Son bouton reste enfoncé lorsqu\'un mode est actif.

-   <img alt="" src=images/Draft_Snap_Lock.svg  style="width:32px;"> [Basculer l\'accrochage](Draft_Snap_Lock/fr.md) : active ou désactive globalement [accrochage aux objets](Draft_Snap/fr.md).
-   <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:32px;"> [Terminaison](Draft_Snap_Endpoint/fr.md) : s\'accroche aux extrémités des segments de ligne, d\'arc et de spline.
-   <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:32px;"> [Milieu](Draft_Snap_Midpoint/fr.md) : s\'accroche au point central des segments de ligne et d\'arc.
-   <img alt="" src=images/Draft_Snap_Center.svg  style="width:32px;"> [Centre](Draft_Snap_Center/fr.md) : s\'accroche au centre des cercles, arcs et des faces, [objets Proxy pour le plan de travail](Draft_WorkingPlaneProxy/fr.md) et [parties de bâtiment](Arch_BuildingPart/fr.md).
-   <img alt="" src=images/Draft_Snap_Angle.svg  style="width:32px;"> [Angle](Draft_Snap_Angle/fr.md) : s\'accroche aux points cardinaux spéciaux des cercles et des arcs, à 45° et 90°.
-   <img alt="" src=images/Draft_Snap_Intersection.svg  style="width:32px;"> [Intersection](Draft_Snap_Intersection/fr.md) : s\'accroche à l\'intersection de deux segments de ligne ou d\'arc. Passez la souris sur les deux objets souhaités pour activer leurs accrochages d\'intersection.
-   <img alt="" src=images/Draft_Snap_Perpendicular.svg  style="width:32px;"> [Perpendiculaire](Draft_Snap_Perpendicular/fr.md) : sur les segments de ligne et d\'arc, s\'accroche perpendiculairement au dernier point.
-   <img alt="" src=images/Draft_Snap_Extension.svg  style="width:32px;"> [Extension](Draft_Snap_Extension/fr.md) : s\'accroche sur une ligne imaginaire qui s\'étend au-delà des extrémités des segments de ligne. Passez la souris sur l\'objet souhaité pour activer son accrochage d\'extension.
-   <img alt="" src=images/Draft_Snap_Parallel.svg  style="width:32px;"> [Parallèle](Draft_Snap_Parallel/fr.md) : s\'accroche sur une ligne imaginaire parallèle à un segment de ligne. Passez la souris sur l\'objet souhaité pour activer son accrochage parallèle.
-   <img alt="" src=images/Draft_Snap_Special.svg  style="width:32px;"> [Spécial](Draft_Snap_Special/fr.md) : s\'accroche sur des points spéciaux définis par l\'objet. {{Version/fr|0.17}}
-   <img alt="" src=images/Draft_Snap_Near.svg  style="width:32px;"> [Le plus proche](Draft_Snap_Near/fr.md) : s\'accroche au point ou au bord le plus proche de l\'objet le plus proche.
-   <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:32px;"> [Orthogonale](Draft_Snap_Ortho/fr.md) : s\'accroche sur des lignes imaginaires qui traversent le dernier point et s\'étendent à 0°, 45° et 90°.
-   <img alt="" src=images/Draft_Snap_Grid.svg  style="width:32px;"> [Grille](Draft_Snap_Grid/fr.md) : s\'accroche aux intersections des lignes de la grille, si la grille est visible.
-   <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:32px;"> [Plan de travail](Draft_Snap_WorkingPlane/fr.md) : place toujours le point d\'accrochage sur le [plan de travail](Draft_SelectPlane/fr.md) actuel, même si vous vous accrochez à un point en dehors de ce plan de travail.
-   <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:32px;"> [Dimensions](Draft_Snap_Dimensions/fr.md) : affiche les dimensions X et Y temporaires lors de l\'accrochage.
-   <img alt="" src=images/Draft_ToggleGrid.svg  style="width:32px;"> [Visibilité de la grille](Draft_ToggleGrid/fr.md) : active ou désactive la visibilité de la grille.

## Outils utilitaires 

-   <img alt="" src=images/_Draft_Layer.svg  style="width:32px;"> [Calque](Draft_Layer/fr.md) : crée un calque dans le document actuel, auquel des objets peuvent être ajoutés pour contrôler la visibilité et la couleur des objets. Il remplace [Groupe visuel](Draft_VisGroup/fr.md). {{Version/fr|0.19}}
-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Défini le proxy du plan de travail](Draft_WorkingPlaneProxy/fr.md) : ajoute un objet proxy au document pour stocker un [Plan de travail](Draft_SelectPlane/fr.md). {{Version/fr|0.17}}
-   <img alt="" src=images/Draft_ToggleDisplayMode.svg  style="width:32px;"> [Bascule le mode d\'affichage](Draft_ToggleDisplayMode/fr.md) : bascule le mode d\'affichage des objets sélectionnés entre « Flat Lines » et « Wireframe » (mode filaire).
-   <img alt="" src=images/Draft_AddToGroup.svg  style="width:32px;"> [Ajouter au groupe](Draft_AddToGroup/fr.md) : ajoute rapidement les objets sélectionnés à un [groupe](Std_Group/fr.md) ou [Draft Groupe visuel](Draft_VisGroup/fr.md) existant.
-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Sélectionner le groupe](Draft_SelectGroup/fr.md) : sélectionne le contenu d\'un [Groupe](Std_Group/fr.md) ou [Draft Groupe visuel](Draft_VisGroup/fr.md) existant sélectionné.
-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Ajouter au groupe de construction](Draft_AddConstruction/fr.md) : ajoute les objets sélectionnés au groupe de construction. {{Version/fr|0.17}}
-   <img alt="" src=images/Draft_Heal.svg  style="width:32px;"> [Réparer](Draft_Heal/fr.md) : corrige les objets problématiques trouvés dans les très vieux fichiers.

## Menu Utilitaires 

Outils supplémentaires, disponibles via le menu **Draft → Utilitaires**, ou via le clic droit de la souris selon les objets sélectionnés.

-   <img alt="" src=images/Draft_ToggleContinueMode.svg  style="width:32px;"> [Inverse le mode continuer](Draft_ToggleContinueMode/fr.md) : active ou désactive le mode continuer le projet
-   <img alt="" src=images/Draft_ShowSnapBar.svg  style="width:32px;"> [Montrer la barre d\'accrochage](Draft_Snap/fr.md) : active ou désactive la barre d\'outils d\'accrochages

## Fonctions additionnelles 

-   [Saisir des coordonnées manuelles](Draft_Coordinates/fr.md) : Permet de saisir des coordonnées manuellement plutôt que de cliquer à l\'écran.
-   [Contraindre](Draft_Constrain/fr.md) : Permet de placer des points horizontalement ou verticalement en relation aux points précédents.
-   [Accrochage](Draft_Snap/fr.md) : Permet de place de nouveau points en des endroits spécifiques sur des objets existants.
-   [Copy Mode](Draft_Copying/fr.md) : Tous les outils de modification peuvent soit modifier les objets sélectionnés, soit en créer une copie modifiée. Appuyer et maintenir **Alt** pendant la modification de l\'objet, par exemple déplacé ou tourné, crée une copie lorsque la clé est relâchée.
-   [Construction Mode](Draft_ToggleConstructionMode/fr.md) : vous permet de créer des géométries séparées du reste en les activant et en les désactivant simplement.
-   [Plan de travail](Draft_SelectPlane/fr.md) : vous permet de sélectionner une surface sur laquelle construire vos formes.

## Tree view context menu 

The following additional options are available in the [Tree view](Tree_view.md) context menu:

### Selection options 

If there is a selection the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Wire options 

For a [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) and [Draft BezCurve](Draft_BezCurve.md) this additional option is available:

-   <img alt="" src=images/Draft_Edit.svg  style="width:32px;"> Flatten this wire: flattens the wire based on its internal geometry. This option currently does not work properly.

### Layer container options 

For a [Draft LayerContainer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> Merge layer duplicates: this option currently does not work.

-   <img alt="" src=images/Draft_NewLayer.svg  style="width:32px;"> [Add new layer](Draft_Layer.md): adds a new layer to the current document.

### Layer options 

For a [Draft Layer](Draft_Layer.md) these additional options are available:

-   <img alt="" src=images/button_right.svg  style="width:32px;"> [Activate this layer](Draft_AutoGroup.md): makes the selected layer the active layer.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Select layer contents](Draft_SelectGroup.md): selects the objects inside the selected layer.

### Working plane proxy options 

For a [Draft WorkingPlaneProxy](Draft_WorkingPlaneProxy.md) these additional options are available:

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write camera position](Draft_WorkingPlaneProxy#Tree_view_context_menu.md): updates the camera settings stored in the working plane proxy.

-   <img alt="" src=images/Draft_SelectPlane.svg  style="width:32px;"> [Write objects state](Draft_WorkingPlaneProxy#Tree_view_context_menu.md): updates the visibility state of objects stored in the working plane proxy.

## 3D view context menu 

The following additional options are available in the [3D view](3D_view.md) context menu:

### No-selection options 

If there is no selection the context menu contains one additional sub-menu:

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Selection options 

If there is a selection the context menu contains two additional sub-menus:

-    **Draft**: tools for [drawing objects](#Drawing_objects.md) and [modifying objects](#Modifying_objects.md).

-    **Utilities**: a subset of the tools available in the main Draft Utilities menu.

### Obsolète

Ces outils ont été supprimés de l\'interface dans la v0.19 car ils n\'avaient plus de raison d\'être.

-   <img alt="" src=images/Draft_VisGroup.svg  style="width:32px;"> [Groupe visuel](Draft_VisGroup/fr.md) : crée un Groupe visuel dans le document actuel. Cela a été remplacé par <img alt="" src=images/Draft_Layer.svg  style="width:32px;"> [Calque](Draft_Layer/fr.md). {{Obsolete/fr|0.19}}
-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> [Terminer la ligne](Draft_FinishLine/fr.md) : Termine le dessin du [Draft Fil](Draft_Wire/fr.md) en cours ou courbe [Draft B-Spline](Draft_BSpline/fr.md), sans refermer. {{Obsolete/fr|0.19}}
-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> [Fermer la ligne](Draft_CloseLine/fr.md) : Termine le dessin du filaire [Draft Fil](Draft_Wire/fr.md) actuel ou courbe [Draft B-Spline](Draft_BSpline/fr.md) et le ferme à la fin de l\'opération. {{Obsolete/fr|0.19}}
-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> [Annuler le dernier segment](Draft_UndoLine/fr.md) : Annule le dernier segment du [Draft Fil](Draft_Wire/fr.md). {{Obsolete/fr|0.19}}

-   <img alt="" src=images/Draft_Drawing.svg  style="width:32px;"> [Drawing](Draft_Drawing.md): writes selected objects to a [Drawing Workbench](Drawing_Workbench.md) page. {{Obsolete|0.17}}

These [3D view](3D_view.md) context menu options are still available when the [Draft Wire](Draft_Wire.md), [Draft BSpline](Draft_BSpline.md), [Draft CubicBezCurve](Draft_CubicBezCurve.md) or [Draft BezCurve](Draft_BezCurve.md) command is active but will be removed in the near future:

-   <img alt="" src=images/Draft_UndoLine.svg  style="width:32px;"> [Undo last segment](Draft_Wire#Options.md): use the {{button|<img src="images/Draft_UndoLine.svg" width=16px> Undo}} button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_FinishLine.svg  style="width:32px;"> [Finish line](Draft_Wire#Options.md): use the **<img src="images/Draft_FinishLine.svg" width=16px> Finish** button in the task panel of the command instead. {{Obsolete|0.20}}

-   <img alt="" src=images/Draft_CloseLine.svg  style="width:32px;"> [Close line](Draft_Wire#Options.md): use the **<img src="images/Draft_CloseLine.svg" width=16px> Close** button in the task panel of the command instead. {{Obsolete|0.20}}

## Préférences

-   <img alt="" src=images/Preferences-draft.svg  style="width:32px;"> [Draft Préférences](Draft_Preferences/fr.md) : Préférences générales pour les plans de travail et les outils Draft.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Préférences d\'Import Export](Import_Export_Preferences/fr.md) : préférences disponibles pour importer et exporter de différents formats de fichier.

## Formats de fichiers 

Ce sont des fonctions pour ouvrir, importer ou exporter d'autres formats de fichiers. L\'ouverture ouvrira un nouveau document avec le contenu du fichier, tandis que l\'importation ajoutera le contenu du fichier au document actuel. Exporter enregistrera les objets sélectionnés dans un fichier. Si rien n\'est sélectionné, tous les objets seront exportés. Sachez que l\'objectif du module de brouillon est de travailler avec des objets 2D. Par conséquent, ces routines d\'importation se concentrent uniquement sur les objets 2D. Bien que les formats DXF et OCA prennent également en charge les définitions d\'objet dans un espace 3D (les objets ne sont pas nécessairement plats), ils ne le seront pas. importer des objets volumétriques tels que des maillages, des surfaces 3D, etc., mais plutôt des lignes, des cercles, des textes ou des formes plates. Les formats de fichier actuellement supportés sont :

-   [Autodesk .DXF](Draft_DXF/fr.md) : Importe et exporte les fichiers [DXF (Drawing eXchange Format)](http://fr.wikipedia.org/wiki/Drawing_eXchange_Format) créés avec d\'autres applications de CAO 2D. Voir aussi [Importation DXF et FreeCAD](FreeCAD_and_DXF_Import/fr.md).
-   [Autodesk .DWG](Draft_DXF/fr.md) : permet d\'importer et d\'exporter des fichiers DWG via l\'importateur DXF lorsque l\'utilitaire [Convertisseur ODA](Extra_python_modules/fr#ODA_Converter_.28pr.C3.A9c.C3.A9demment_Teigha_Converter.29.md) est installé. Voir aussi [ Importation FreeCAD et DWG](FreeCAD_and_DWG_Import/fr.md).
-   [SVG (come géometrie)](Draft_SVG/fr.md) : Importe et exporte les fichiers [Scalable Vector Graphics(SVG)](http://fr.wikipedia.org/wiki/Scalable_Vector_Graphics) créés avec des applications de dessin vectoriel
-   [Open Cad format .OCA](Draft_OCA/fr.md) : Importe et exporte les fichiers OCA/GCAD, un nouveau [format de fichier CAO ouvert](http://groups.google.com/group/open_cad_format) potentiel
-   [Airfoil Data Format .DAT](Draft_DAT/fr.md) : Importe et exporte les fichiers DAT décrivant des [profils de surface portante](http://www.ae.illinois.edu/m-selig/ads/coord_database.html)

### Installation d\'importeurs 

-   [FreeCAD and DWG-Import](FreeCAD_and_DWG_Import/fr.md) : Importe et exporte des fichiers DWG
-   [FreeCAD- und DXF-Import](FreeCAD_and_DXF_Import/fr.md) : Importe et exporte des fichiers DXF

## Tests unitaires 


**Voir aussi :**

[Atelier Test](Testing/fr.md).

Pour exécuter les tests unitaires du plan de travail, exécutez ce qui suit à partir du terminal du système d\'exploitation. 
```python
freecad -t TestDraft
```

## Script

Les outils de Draft peuvent être utilisés dans des [macros](macros/fr.md) et à partir de la console [Python](Python/fr.md) en utilisant le [Draft API](Draft_API/fr.md).

L\'atelier comprend un module pour créer des échantillons de tous les objets dans un nouveau document. {{Version/fr|0.19}}

Utilisez-le pour tester que tous les objets sont produits correctement. 
```python
import drafttests.draft_test_objects as dto
doc = dto.create_test_file()
```

L\'inspection du code de ce module est utile pour comprendre comment utiliser l\'interface de programmation. 
```python
$INSTALLDIR/Mod/Draft/drafttests/draft_test_objects.py
```

Où `$INSTALLDIR` est le répertoire de niveau supérieur où le logiciel a été installé ; par exemple, sous Linux, il peut s\'agir de `/usr/share/freecad`.

<img alt="" src=images/Draft_test_objects.png  style="width:500px;"> 
*Objets test pour l'[atelier Draft](Draft_Workbench/fr.md).*

## Tutoriels

-   [Draft Tutoriel](Draft_tutorial/fr.md)
-   [Draft Tutoriel obsolète](Draft_tutorial_Outdated/fr.md)
-   [Draft Tutoriel Forme à partir de texte](Draft_ShapeString_tutorial/fr.md)





 

[Category:Workbenches](Category:Workbenches.md)
