# <img alt="Icône de l\'atelier TechDraw" src=images/Workbench_TechDraw.svg  style="width   *64px;"> TechDraw Workbench/fr

## Introduction

L\'atelier <img alt="" src=images/Workbench_TechDraw.svg  style="width   *24px;"> [TechDraw](TechDraw_Workbench/fr.md) est utilisé pour produire des dessins techniques de base à partir de modèles 3D créés avec un autre atelier, tels que [Part](Part_Workbench/fr.md), [PartDesign](PartDesign_Workbench/fr.md) ou [Arch](Arch_Workbench/fr.md), ou importés à partir d\'autres applications. Chaque dessin est une page pouvant contenir diverses vues d\'objets pouvant être dessinés, telles que Part   *   *Features, PartDesign   *   *Bodies, App   *   *Part groups et des groupes Object Document. Les dessins résultants peuvent être utilisés pour des éléments tels que la documentation, les instructions de fabrication, les contrats, les permis, etc.

Des dimensions, des sections, des zones hachurées, des annotations et des symboles [SVG](SVG/fr.md) peuvent être ajoutés à la page, qui peuvent ensuite être exportés vers différents formats tels que [DXF](DXF/fr.md), [SVG](SVG/fr.md) et [PDF](PDF/fr.md).

TechDraw a été officiellement inclus dans FreeCAD à partir de la version 0.17; il est destiné à remplacer l\'atelier [Drawing](Drawing_Workbench/fr.md) non pris en charge. Les deux ateliers sont toujours fournis dans la v0.17, mais l\'atelier Drawing pourrait être supprimé dans les versions ultérieures. Pour suivre les plans et les développements de TechDraw, visitez la [Feuille de route TechDraw](TechDraw_Roadmap.md).

Si votre objectif principal est la production de dessins 2D complexes et de fichiers [DXF](DXF/fr.md) et que vous n\'avez pas besoin de modélisation 3D, FreeCAD n\'est peut-être pas le bon choix pour vous. Vous pouvez envisager d\'utiliser un logiciel dédié au dessin technique, tel que [LibreCAD](https   *//fr.wikipedia.org/wiki/LibreCAD) ou [QCad](https   *//fr.wikipedia.org/wiki/QCad).


{{TOCright}}

<img alt="" src=images/TechDraw_Workbench_Example.png  style="width   *600px;">

## Pages

Ce sont les outils pour créer des objets Pages.

-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width   *32px;"> [Page par défaut](TechDraw_PageDefault/fr.md)    * ajoute une nouvelle page en utilisant le [modèle](TechDraw_Templates/fr.md) par défaut.

-   <img alt="" src=images/TechDraw_PageTemplate.svg  style="width   *32px;"> [Page selon un modèle](TechDraw_PageTemplate/fr.md)    * ajoute une nouvelle page en utilisant un [modèle](TechDraw_Templates/fr.md) sélectionné.

-   <img alt="" src=images/TechDraw_RedrawPage.svg  style="width   *32px;"> [Rafraîchir](TechDraw_RedrawPage/fr.md)    * force la mise à jour de la page. {{Version/fr|0.19}}

## Vues

Ce sont les outils pour créer des objets Vues.

-   <img alt="" src=images/TechDraw_View.svg  style="width   *32px;"> [Vue](TechDraw_View/fr.md)    * ajoute une vue en projection 2D d\'un objet.

-   <img alt="" src=images/TechDraw_ActiveView.svg  style="width   *32px;"> [Vue active](TechDraw_ActiveView/fr.md)    * insère une vue de la vue 3D active. {{Version/fr|0.19}}

-   <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width   *32px;"> [Groupe de projections](TechDraw_ProjectionGroup/fr.md)    * ouvre une boîte de dialogue pour créer plusieurs vues d\'un objet à partir de plusieurs directions.

-   <img alt="" src=images/TechDraw_SectionView.svg  style="width   *32px;"> [Vue en coupe](TechDraw_SectionView/fr.md)    * ajoute une vue en coupe à partir d\'une vue existante.

-   <img alt="" src=images/TechDraw_DetailView.svg  style="width   *32px;"> [Vue détaillée](TechDraw_DetailView/fr.md)    * ajoute une vue détaillée d\'une partie d\'une vue existante.

-   <img alt="" src=images/TechDraw_DraftView.svg  style="width   *32px;"> [Vue d\'un objet Draft](TechDraw_DraftView/fr.md)    * ajoute une vue d\'un objet [Draft](Draft_Workbench/fr.md).

-   <img alt="" src=images/TechDraw_ArchView.svg  style="width   *32px;"> [Vue d\'un objet Arch](TechDraw_ArchView/fr.md)   * ajoute une vue d\'un objet [Arch Plan de section](Arch_SectionPlane/fr.md) de l\'[Atelier Arch](Arch_Workbench/fr.md).

-   <img alt="" src=images/TechDraw_SpreadsheetView.svg  style="width   *32px;"> [Vue d\'un tableur](TechDraw_SpreadsheetView/fr.md)   * insère une vue d\'une feuille de calcul de l\'[atelier Spreadsheet](Spreadsheet_Workbench/fr.md).

-   <img alt="" src=images/TechDraw_MoveView.svg  style="width   *32px;"> [Déplacer une vue](TechDraw_MoveView/fr.md)   * déplace une vue et ses dépendants vers une page différente. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ShareView.svg  style="width   *32px;"> [Copier une vue](TechDraw_ShareView/fr.md)    * Partagez une vue entre plusieurs pages. {{Version/fr|0.20}}

## Rognages

Ce sont des outils pour créer et gérer des objets de Rognages (vues découpées).

-   <img alt="" src=images/TechDraw_ClipGroup.svg  style="width   *32px;"> [Fenêtre de rognage](TechDraw_ClipGroup/fr.md)   * insère une fenêtre de rognage sur une page.

-   <img alt="" src=images/TechDraw_ClipGroupAdd.svg  style="width   *32px;"> [Ajout vue à une fenêtre de rognage](TechDraw_ClipGroupAdd/fr.md)   * ajoute une vue existante à une fenêtre de rognage.

-   <img alt="" src=images/TechDraw_ClipGroupRemove.svg  style="width   *32px;"> [Suppression vue d\'une fenêtre de rognage](TechDraw_ClipGroupRemove/fr.md)   * supprime une vue d\'une fenêtre de rognage.

## Décorations

Ce sont les outils pour décorer l\'apparence des pages et des vues.

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width   *32px;"> [Hachures par motif](TechDraw_Hatch/fr.md)    * hachure une face en utilisant un fichier image.

-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width   *32px;"> [Applique un motif de hachure](TechDraw_GeometricHatch/fr.md)    * applique un motif de hachure à une face en utilisant une spécification Autodesk PAT.

-   <img alt="" src=images/TechDraw_Symbol.svg  style="width   *32px;"> [Symbole SVG](TechDraw_Symbol/fr.md)    * insère un symbole [SVG](SVG/fr.md) dans une page.

-   <img alt="" src=images/TechDraw_Image.svg  style="width   *32px;"> [Image Bitmap](TechDraw_Image/fr.md)    * insère une image PNG ou JPG [bitmap](bitmap/fr.md) dans une page.

-   <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width   *32px;"> [Bascule des cadres](TechDraw_ToggleFrame/fr.md)    * bascule l\'affichage des cadres et des étiquettes entourant une vue.

## Cotes

Ce sont les outils pour créer et travailler avec des objets Cote.

Les cotes linéaires peuvent être basées sur deux points, sur une ligne ou sur deux lignes.

-   <img alt="" src=images/TechDraw_LengthDimension.svg  style="width   *32px;"> [Cote de longueur](TechDraw_LengthDimension/fr.md)    * ajoute une cote de longueur.

-   <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width   *32px;"> [Cote horizontale](TechDraw_HorizontalDimension/fr.md)    * ajoute une cote de longueur horizontale.

-   <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width   *32px;"> [Cote verticale](TechDraw_VerticalDimension/fr.md)    * ajoute une cote de longueur verticale.

-   <img alt="" src=images/TechDraw_RadiusDimension.svg  style="width   *32px;"> [Cote de rayon](TechDraw_RadiusDimension/fr.md)    * ajoute une cote de rayon à un cercle ou un arc de cercle.

-   <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width   *32px;"> [Cote de diamètre](TechDraw_DiameterDimension/fr.md)    * ajoute une cote de diamètre à un cercle ou à un arc de cercle.

-   <img alt="" src=images/TechDraw_AngleDimension.svg  style="width   *32px;"> [Cote angulaire](TechDraw_AngleDimension/fr.md)    * ajoute une cote angulaire entre deux arêtes droites.

-   <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width   *32px;"> [Cote angulaire par 3 points](TechDraw_3PtAngleDimension/fr.md)    * ajoute une cote d\'angle à partir de trois sommets.

-   <img alt="" src=images/TechDraw_HorizontalExtentDimension.svg  style="width   *32px;"> [Extension horizontale](TechDraw_HorizontalExtentDimension/fr.md)    * ajoute une dimension d\'extension horizontale. {{Version/fr|0.19}}

-   <img alt="" src=images/TechDraw_VerticalExtentDimension.svg  style="width   *32px;"> [Extension verticale](TechDraw_VerticalExtentDimension/fr.md)    * ajoute une dimension d\'extension verticale. {{Version/fr|0.19}}

-   <img alt="" src=images/TechDraw_LinkDimension.svg  style="width   *32px;"> [Lier une dimension](TechDraw_LinkDimension/fr.md)    * lie une cote existante à la géométrie 3D.

-   <img alt="" src=images/TechDraw_Balloon.svg  style="width   *32px;"> [Infobulle](TechDraw_Balloon/fr.md)    * ajout \"d\'infobulles\" dans la page. {{Version/fr|0.19}}

-   <img alt="" src=images/TechDraw_LandmarkDimension.svg  style="width   *32px;"> [Dimension de repère](TechDraw_LandmarkDimension/fr.md)    * ajoute une cote linéaire. {{Version/fr|0.19}}

## Annotations

Les outils d\'annotation permettent de \"marquer\" un dessin avec des informations supplémentaires.

-   <img alt="" src=images/TechDraw_Annotation.svg  style="width   *32px;"> [Annotation](TechDraw_Annotation/fr.md)    * ajoute un bloc de texte pour servir d\'annotation.

-   <img alt="" src=images/TechDraw_LeaderLine.svg  style="width   *32px;"> [Ligne de référence](TechDraw_LeaderLine/fr.md)    * ajoute une ligne de référence à une vue. {{Version/fr|0.19}}

-   <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width   *32px;"> [Annotation texte enrichi](TechDraw_RichTextAnnotation/fr.md)    * ajoute un bloc d'annotation en texte enrichi à une ligne de référence ou à une vue. {{Version/fr|0.19}}

-   <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width   *32px;"> [Point cosmétique](TechDraw_CosmeticVertex/fr.md)    * ajoute un sommet qui ne fait pas partie de la géométrie principale. {{Version/fr|0.19}}

-   <img alt="" src=images/TechDraw_Midpoints.svg  style="width   *32px;"> [Points médians](TechDraw_Midpoints/fr.md)    * ajoute des points cosmétiques aux points médians d\'une ou de plusieurs arêtes sélectionnées. {{Version/fr|0.19}}

-   <img alt="" src=images/TechDraw_Quadrants.svg  style="width   *32px;"> [Quadrant](TechDraw_Quadrants/fr.md)    * ajoute des points cosmétiques tous les quarts de points d\'un ou de plusieurs bords sélectionnés (circulaires). {{Version/fr|0.19}}

-   <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width   *32px;"> [Ligne centrale à une face](TechDraw_FaceCenterLine/fr.md)    * ajoute une ligne centrale aux face(s) sélectionnée(s). {{Version/fr|0.19}}

-   <img alt="" src=images/TechDraw_2LineCenterLine.svg  style="width   *32px;"> [Ligne centrale entre 2 lignes](TechDraw_2LineCenterLine/fr.md)    * ajoute une ligne centrale entre 2 arêtes. {{Version/fr|0.19}}

-   <img alt="" src=images/TechDraw_2PointCenterLine.svg  style="width   *32px;"> [Ligne centrale entre 2 points](TechDraw_2PointCenterLine/fr.md)    * ajoute une ligne centrale entre 2 points. {{Version/fr|0.19}}

-   <img alt="" src=images/TechDraw-line2points.svg  style="width   *32px;"> [Ligne cosmétique par 2 points](TechDraw_2PointCosmeticLine/fr.md)   * ajoute une ligne cosmétique reliant 2 points. {{Version/fr|0.19}}

-   <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width   *32px;"> [Gomme](TechDraw_CosmeticEraser/fr.md)    * supprime les objets cosmétiques d\'une page. {{Version/fr|0.19}}

-   <img alt="" src=images/TechDraw_DecorateLine.svg  style="width   *32px;"> [Apparence des lignes](TechDraw_DecorateLine/fr.md)    * modifie l\'apparence des lignes. {{Version/fr|0.19}}

-   <img alt="" src=images/TechDraw_ShowAll.svg  style="width   *32px;"> [Montrer tout](TechDraw_ShowAll/fr.md)    * affiche/masque les bords invisibles dans une vue. {{Version/fr|0.19}}

-   <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width   *32px;"> [Soudure](TechDraw_WeldSymbol/fr.md)    * ajoute des spécifications de soudage à une ligne de référence existante. {{Version/fr|0.19}}

-   <img alt="" src=images/TechDraw_SurfaceFinishSymbol.svg  style="width   *32px;"> [Symbole d\'état de surface](TechDraw_SurfaceFinishSymbol/fr.md)    * ajoute un symbole de finition de surface à une page. {{Version/fr|1.0}}

## Extensions

Ce sont des outils pour améliorer vos dessins TechDraw.

### Caractéristiques et modifications 

-   <img alt="" src=images/TechDraw_ExtensionSelectLineAttributes.svg  style="width   *32px;"> [Sélection des attributs](TechDraw_ExtensionSelectLineAttributes/fr.md)    * sélectionne les attributs (style, largeur et couleur) des nouvelles lignes cosmétiques et des lignes centrales, et spécifie l\'espacement en cascade et la distance delta. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionChangeLineAttributes.svg  style="width   *32px;"> [Modification des attributs](TechDraw_ExtensionChangeLineAttributes/fr.md)    * modifie les attributs (style, largeur et couleur) des lignes cosmétiques et des lignes centrales. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionExtendLine.svg  style="width   *32px;"> [Prolonger](TechDraw_ExtensionExtendLine/fr.md)    * prolonge une ligne cosmétique ou une ligne centrale aux deux extrémités. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionShortenLine.svg  style="width   *32px;"> [Raccourcir](TechDraw_ExtensionShortenLine/fr.md)    * raccourcit une ligne cosmétique ou une ligne centrale aux deux extrémités. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionLockUnlockView.svg  style="width   *32px;"> [Verrouiller/déverrouiller](TechDraw_ExtensionLockUnlockView/fr.md)    * verrouille/déverrouille la position d\'une vue. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionPositionSectionView.svg  style="width   *32px;"> [Position d\'une vue en coupe](TechDraw_ExtensionPositionSectionView/fr.md)    * aligne orthogonalement une vue en coupe avec sa vue source. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionPosHorizChainDimension.svg  style="width   *32px;"> [Aligner horizontalement](TechDraw_ExtensionPosHorizChainDimension/fr.md)    * aligne des cotes horizontales pour créer une chaîne de cotes. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionPosVertChainDimension.svg  style="width   *32px;"> [Aligner verticalement](TechDraw_ExtensionPosVertChainDimension/fr.md)    * aligne des cotes verticales pour créer une chaîne de cotes. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionPosObliqueChainDimension.svg  style="width   *32px;"> [Aligner obliquement](TechDraw_ExtensionPosObliqueChainDimension/fr.md)    * aligne des cotes obliques pour créer une chaîne de cotes. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCascadeHorizDimension.svg  style="width   *32px;"> [Cascade horizontale](TechDraw_ExtensionCascadeHorizDimension/fr.md)   * espace régulièrement des cotes horizontales. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCascadeVertDimension.svg  style="width   *32px;"> [Cascade verticale](TechDraw_ExtensionCascadeVertDimension/fr.md)   * espace régulièrement des cotes verticales. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCascadeObliqueDimension.svg  style="width   *32px;"> [Cascade oblique](TechDraw_ExtensionCascadeObliqueDimension/fr.md)   * espace régulièrement des cotes obliques. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionAreaAnnotation.svg  style="width   *32px;"> [Surface](TechDraw_ExtensionAreaAnnotation/fr.md)    * calcule la surface des faces sélectionnées et insère une annotation de surface. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCustomizeFormat.svg  style="width   *32px;"> [Personnaliser le format d\'infobulle](TechDraw_ExtensionCustomizeFormat/fr.md)    * Personnalise le formatage du texte d\'une infobulle ou du texte d\'une cote. Des [symboles GD&T](https   *//en.wikipedia.org/wiki/Geometric_dimensioning_and_tolerancing) et d\'autres caractères spéciaux peuvent être ajoutés. {{Version/fr|0.20}}

### Lignes centrales, filetage et taraudage 

-   <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width   *32px;"> [Axes de centrage](TechDraw_ExtensionCircleCenterLines/fr.md)    * ajoute des lignes de centre aux cercles et aux arcs. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionHoleCircle.svg  style="width   *32px;"> [Axes de centrage de trous/vis](TechDraw_ExtensionHoleCircle/fr.md)    * dessine les lignes centrales des cercles de trous/vis. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width   *32px;"> [Corps de taraudage](TechDraw_ExtensionThreadHoleSide/fr.md)    * ajoute un symbole pour le taraudage à la vue latérale d\'un trou. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionThreadHoleBottom.svg  style="width   *32px;"> [Taraudage](TechDraw_ExtensionThreadHoleBottom/fr.md)    * ajoute des taraudages symboliques à la vue supérieure ou inférieure des trous. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionThreadBoltSide.svg  style="width   *32px;"> [Corps de filetage](TechDraw_ExtensionThreadBoltSide/fr.md)    * ajoute un symbole pour le filetage à la vue latérale des boulons/vis/tiges. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionThreadBoltBottom.svg  style="width   *32px;"> [Filetage](TechDraw_ExtensionThreadBoltBottom/fr.md)    * ajoute des filetages symboliques à la vue supérieure ou inférieure des boulons/vis/tiges. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionVertexAtIntersection.svg  style="width   *32px;"> [Intersection de lignes](TechDraw_ExtensionVertexAtIntersection/fr.md)    * crée des sommets cosmétiques à l\'intersection des lignes sélectionnées. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle.svg  style="width   *32px;"> [Cercle](TechDraw_ExtensionDrawCosmCircle/fr.md)    * dessine un cercle cosmétique en utilisant deux points. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionDrawCosmArc.svg  style="width   *32px;"> [Arc](TechDraw_ExtensionDrawCosmArc/fr.md)    * ajoute un arc cosmétique dans le sens inverse des aiguilles d\'une montre à partir de trois sommets. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionDrawCosmCircle3Points.svg  style="width   *32px;"> [Cercle par 3 points](TechDraw_ExtensionDrawCosmCircle3Points/fr.md)    * ajoute un cercle cosmétique basé sur trois sommets. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionLineParallel.svg  style="width   *32px;"> [Ligne parallèle](TechDraw_ExtensionLineParallel/fr.md)    * dessine une ligne cosmétique parallèle à une autre ligne passant par un sommet. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionLinePerpendicular.svg  style="width   *32px;"> [Ligne perpendiculaire](TechDraw_ExtensionLinePerpendicular/fr.md)    * dessine une ligne cosmétique perpendiculaire à une autre ligne passant par un sommet. {{Version/fr|0.20}}

### Cotes 

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizChainDimension.svg  style="width   *32px;"> [Cotes horizontales](TechDraw_ExtensionCreateHorizChainDimension/fr.md)    * crée une séquence horizontale de cotes. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCreateVertChainDimension.svg  style="width   *32px;"> [Cotes verticales](TechDraw_ExtensionCreateVertChainDimension/fr.md)    * crée une séquence verticale de cotes. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCreateObliqueChainDimension.svg  style="width   *32px;"> [Cotes obliques](TechDraw_ExtensionCreateObliqueChainDimension/fr.md)    * crée une séquence oblique de cotes. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizCoordDimension.svg  style="width   *32px;"> [Cotes parallèles horizontales](TechDraw_ExtensionCreateHorizCoordDimension/fr.md)    * crée des cotes horizontales uniformément espacées à partir de la même ligne de base.. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCreateVertCoordDimension.svg  style="width   *32px;"> [Cotes parallèles verticales](TechDraw_ExtensionCreateVertCoordDimension/fr.md)    * crée des cotes verticales uniformément espacées à partir de la même ligne de base. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCreateObliqueCoordDimension.svg  style="width   *32px;"> [Cotes parallèles obliques](TechDraw_ExtensionCreateObliqueCoordDimension/fr.md)    * crée des cotes obliques uniformément espacées à partir de la même ligne de base. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCreateHorizChamferDimension.svg  style="width   *32px;"> [Cote horizontale chanfrein](TechDraw_ExtensionCreateHorizChamferDimension/fr.md)    * crée une cote horizontale et une cote d\'angle pour un chanfrein. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCreateVertChamferDimension.svg  style="width   *32px;"> [Cote verticale chanfrein](TechDraw_ExtensionCreateVertChamferDimension/fr.md)   * crée une cote verticale et une cote d\'angle pour un chanfrein. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionCreateLengthArc.svg  style="width   *32px;"> [Longueur d\'arc](TechDraw_ExtensionCreateLengthArc/fr.md)    * crée une dimension de longueur d\'arc. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionInsertDiameter.svg  style="width   *32px;"> [Diamètre](TechDraw_ExtensionInsertDiameter/fr.md)    * insère un symbole \"⌀\" pour un diamètre au début du texte de la cote. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionInsertSquare.svg  style="width   *32px;"> [Section tube](TechDraw_ExtensionInsertSquare/fr.md)    * insère le symbole \"〼\" pour une section de tube carré au début du texte de la cote. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionRemovePrefixChar.svg  style="width   *32px;"> [Supprimer les symboles](TechDraw_ExtensionRemovePrefixChar/fr.md)    * supprime tous les symboles au début du texte de la cote. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionIncreaseDecimal.svg  style="width   *32px;"> [Plus de décimales](TechDraw_ExtensionIncreaseDecimal/fr.md)    * augmente le nombre de décimales du texte de la cote. {{Version/fr|0.20}}

-   <img alt="" src=images/TechDraw_ExtensionDecreaseDecimal.svg  style="width   *32px;"> [Moins de décimales](TechDraw_ExtensionDecreaseDecimal/fr.md)   * diminue le nombre de décimales du texte de la cote. {{Version/fr|0.20}}

## Exportation

Ce sont les outils pour exporter les pages vers d\'autre applications.

-   <img alt="" src=images/TechDraw_ExportPageSVG.svg  style="width   *32px;"> [Sauvegarder au format SVG](TechDraw_ExportPageSVG/fr.md)    * enregistre la page en cours sous forme de fichier [SVG](SVG/fr.md).

-   <img alt="" src=images/TechDraw_ExportPageDXF.svg  style="width   *32px;"> [Sauvegarder au format DXF](TechDraw_ExportPageDXF/fr.md)    * enregistre la page en cours sous forme de fichier [DXF](DXF/fr.md).

## Fonctions supplémentaires 

-   [Groupes de lignes](TechDraw_LineGroup/fr.md)    * pour contrôler l\'apparence de divers types de lignes.
-   [Modèles](TechDraw_Templates/fr.md)    * modèles par défaut définis pour les pages de dessin.
-   [Hachures](TechDraw_Hatching/fr.md)    * explication des différentes techniques de hachurage.
-   [Dimensionnement géométrique et tolérancement.](TechDraw_Geometric_dimensioning_and_tolerancing/fr.md)   * explication sur la façon de réaliser le dimensionnement géométrique et le tolérancement.

## Préférences

-   <img alt="" src=images/Preferences-techdraw.svg  style="width   *32px;"> [Préférences](TechDraw_Preferences/fr.md)    * préférences pour les valeurs par défaut de la page de dessin, telles que l\'angle de projection, les couleurs, la taille du texte et les styles de trait.

## Script

Les outils TechDraw peuvent être utilisés dans des [macros](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide de deux API    *

-   [TechDraw API](TechDraw_API/fr.md)
-   [TechDrawGui API](TechDrawGui_API/fr.md)

## Limitations

-   Les dessins TechDraw et son API Python ne sont pas interchangeables avec l\'[atelier Drawing](Drawing_Workbench/fr.md) et son API. Il est possible de convertir des pages de dessin en pages TechDraw en utilisant un script Python (`moveViews.py`).
-   Il est possible d\'avoir à la fois des Pages TechDraw et Drawing dans le même document FreeCAD, chaque page étant complètement indépendante l'une de l'autre.
-   Il existe des différences mineures dans la spécification des textes modifiables dans les modèles [SVG](SVG/fr.md) par rapport au module Dessin. Dans TechDraw, la mise à l\'échelle du document SVG affecte la position des champs de texte modifiables. Voir la discussion du forum [échelle des modèles TechDraw](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=24981&p=196271#p196271) pour plus de détails.
-   Ne coupez pas, ne copiez pas et ne collez pas d\'objets TechDraw dans la [Vue en arborescence](Tree_view/fr.md) car cela ne fonctionne généralement pas bien.
-   Ne faites pas glisser les objets TechDraw dans la [Vue en arborescence](Tree_view/fr.md) avec la souris.

## Tutoriels

-   [Tutoriel TechDraw de base](Basic_TechDraw_Tutorial/fr.md)    * Introduction à la création de dessins avec l\'atelier TechDraw.
-   [Comment créer un modèle](TechDraw_TemplateHowTo/fr.md)   * instructions pour créer un nouveau modèle de page dans Inkscape à utiliser avec l\'atelier TechDraw.
-   [TechDraw Création de modèles](TechDraw_TemplateGenerator/fr.md)    * Instructions pour créer une macro pour générer un modèle de base.

   *   Quelques lignes de code ajoutées permettent d\'obtenir un outil comme la [Macro TemplateHelper](Macro_TemplateHelper/fr.md).

-   [Mesure des angles sur les axes des trous](Measurement_Of_Angles_On_Holes/fr.md)    * Instructions pour ajouter des lignes de centre et des représentations angulaires ultérieures sur les trous.
-   [Comment](TechDraw_HowTo_Page.md)   * instructions pour différents paramètres tels que les marques centrales etc\...
-   [Tutoriel TechDraw Cercle Imaginaire](TechDraw_Pitch_Circle_Tutorial/fr.md)    * Instructions pour ajouter un cercle imaginaire à une vue.

Tutoriels video par sliptonic

-   Atelier TechDraw [Part 1 (Basics)](https   *//www.youtube.com/watch?v=7LbOmSGW9F0), [Part 2 (Dimensions)](https   *//www.youtube.com/watch?v=z3w84RfvqaE), [Part 3 (Multivues)](https   *//www.youtube.com/watch?v=uNjXg-m38aI)
-   Atelier TechDraw [Part 4 (Sections et Details)](https   *//www.youtube.com/watch?v=3zSdeFV6I5o), [Part 5 (Création de feuilles de dessin)](https   *//www.youtube.com/watch?v=kcmdJ7xa7gg)





{{TechDraw_Tools_navi

}} 

[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > TechDraw Workbench/fr
