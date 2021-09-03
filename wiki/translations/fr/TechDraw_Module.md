




<img alt="Icône de l\'atelier TechDraw" src=images/Workbench_TechDraw.svg  style="width:128px;">

## Introduction

L\'atelier <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw](TechDraw_Module/fr.md) est utilisé pour produire des dessins techniques de base à partir de modèles 3D créés avec un autre atelier, tels que [Part](Part_Workbench/fr.md), [PartDesign](PartDesign_Workbench/fr.md) ou [Arch](Arch_Module/fr.md), ou importés à partir d\'autres applications. Chaque dessin est une page pouvant contenir diverses vues d\'objets pouvant être dessinés, telles que Part::Features, PartDesign::Bodies, App::Part groups et des groupes Object Document. Les dessins résultants peuvent être utilisés pour des éléments tels que la documentation, les instructions de fabrication, les contrats, les permis, etc.

Des dimensions, des sections, des zones hachurées, des annotations et des symboles [SVG](SVG/fr.md) peuvent être ajoutés à la page, qui peuvent ensuite être exportés vers différents formats tels que [DXF](DXF/fr.md), [SVG](SVG/fr.md) et [PDF](PDF/fr.md).

TechDraw a été officiellement inclus dans FreeCAD à partir de la version 0.17; il est destiné à remplacer l\'atelier [Drawing](Drawing_Module/fr.md) non pris en charge. Les deux ateliers sont toujours fournis dans la v0.17, mais l\'atelier Drawing pourrait être supprimé dans les versions ultérieures. Pour suivre les plans et les développements de TechDraw, visitez la [Feuille de route TechDraw](TechDraw_Roadmap/fr.md).

FreeCAD est principalement une application de modélisation 3D et ne dispose donc pas de nombreux outils de dessin 2D, qui sont pour la plupart inclus dans les ateliers [Draft](Draft_Workbench/fr.md) et [Sketcher](Sketcher_Workbench/fr.md). Si votre objectif principal est la production de dessins 2D complexes et de fichiers [DXF](DXF/fr.md), et que vous n\'avez pas besoin de modélisation 3D, vous pouvez envisager un logiciel dédié à la rédaction technique, tel que [LibreCAD](https://fr.wikipedia.org/wiki/LibreCAD), [QCad](https://fr.wikipedia.org/wiki/QCad), TurboCad et autres.


{{TOCright}}

<img alt="" src=images/TechDraw_Workbench_Example.png  style="width:600px;">

## Pages

Ce sont les outils pour créer des objets Pages.

-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width:32px;"> [Page par défaut](TechDraw_PageDefault/fr.md) : ajoute une nouvelle page en utilisant le [modèle](TechDraw_Templates/fr.md) par défaut.

-   <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:32px;"> [Page selon un modèle](TechDraw_PageTemplate/fr.md) : ajoute une nouvelle page en utilisant un [modèle](TechDraw_Templates/fr.md) sélectionné.

-   <img alt="" src=images/TechDraw_RedrawPage.svg  style="width:32px;"> [Rafraîchir](TechDraw_RedrawPage/fr.md) : force la mise à jour de la page. {{Version/fr|0.19}}

## Vues

Ce sont les outils pour créer des objets Vues.

-   <img alt="" src=images/TechDraw_View.svg  style="width:32px;"> [Nouvelle vue](TechDraw_View/fr.md) : ajoute une vue en projection 2D d\'un objet.

-   <img alt="" src=images/TechDraw_ActiveView.svg  style="width:32px;"> [Vue active](TechDraw_ActiveView/fr.md) : insère une vue de la vue 3D active. {{Version/fr|0.19}}

-   <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:32px;"> [Insérer un groupe de projections](TechDraw_ProjectionGroup/fr.md) : invoque une boîte de dialogue pour créer plusieurs vues d\'un objet à partir de plusieurs directions.

-   <img alt="" src=images/TechDraw_SectionView.svg  style="width:32px;"> [Nouvelle vue en coupe](TechDraw_SectionView/fr.md) : ajoute une vue en coupe à partir d\'une vue existante.

-   <img alt="" src=images/TechDraw_DetailView.svg  style="width:32px;"> [Nouvelle vue de détail](TechDraw_DetailView/fr.md) : ajoute une vue de détail d\'une partie d\'une vue existante.

-   <img alt="" src=images/TechDraw_DraftView.svg  style="width:32px;"> [Nouvelle vue d\'un objet Draft](TechDraw_DraftView/fr.md) : ajoute une vue d\'un objet [Draft](Draft_Workbench/fr.md).

-   <img alt="" src=images/TechDraw_ArchView.svg  style="width:32px;"> [Nouvelle vue d\'un objet Arch](TechDraw_ArchView/fr.md): ajoute une vue d\'un objet [Arch Plan de section](Arch_SectionPlane/fr.md) de l\'[Atelier Arch](Arch_Module/fr.md).

-   <img alt="" src=images/TechDraw_SpreadsheetView.svg  style="width:32px;"> [Vue d\'un tableur](TechDraw_SpreadsheetView/fr.md): insère une vue d\'une feuille de calcul de l\'[atelier Spreadsheet](Spreadsheet_Workbench/fr.md).

## Rognages

Ce sont des outils pour créer et gérer des objets de Rognages (vues découpées).

-   <img alt="" src=images/TechDraw_ClipGroup.svg  style="width:32px;"> [Fenêtre de rognage](TechDraw_ClipGroup/fr.md): insère une fenêtre de rognage sur une page.

-   <img alt="" src=images/TechDraw_ClipGroupAdd.svg  style="width:32px;"> [Ajout vue à une fenêtre de rognage](TechDraw_ClipGroupAdd/fr.md): ajoute une vue existante à une fenêtre de rognage.

-   <img alt="" src=images/TechDraw_ClipGroupRemove.svg  style="width:32px;"> [Suppression vue à une fenêtre de rognage](TechDraw_ClipGroupRemove/fr.md): supprime une vue à une fenêtre de rognage.

## Cotations

Ce sont les outils pour créer et travailler avec des objets Dimension.

Les cotes linéaires peuvent être basées sur deux points, sur une ligne ou sur deux lignes.

-   <img alt="" src=images/TechDraw_Dimension_Length.svg  style="width:32px;"> [Nouvelle longueur](TechDraw_Dimension_Length/fr.md) : ajoute une cote de longueur.

-   <img alt="" src=images/TechDraw_Dimension_Horizontal.svg  style="width:32px;"> [Nouvelle cote horizontale](TechDraw_Dimension_Horizontal/fr.md) : ajoute une cote de longueur horizontale.

-   <img alt="" src=images/TechDraw_Dimension_Vertical.svg  style="width:32px;"> [Nouvelle cote verticale](TechDraw_Dimension_Vertical/fr.md) : ajoute une cote de longueur verticale.

-   <img alt="" src=images/TechDraw_Dimension_Radius.svg  style="width:32px;"> [Nouvelle cote radiale](TechDraw_Dimension_Radius/fr.md) : ajoute une cote de rayon à un cercle ou un arc de cercle.

-   <img alt="" src=images/TechDraw_Dimension_Diameter.svg  style="width:32px;"> [Nouvelle cote diamétrale](TechDraw_Dimension_Diameter/fr.md) : ajoute une cote de diamètre à un cercle ou à un arc de cercle.

-   <img alt="" src=images/TechDraw_Dimension_Angle.svg  style="width:32px;"> [Nouvelle cote angulaire](TechDraw_Dimension_Angle/fr.md) : ajoute une cote angulaire entre deux arêtes droites.

-   <img alt="" src=images/TechDraw_Dimension_Angle3Pt.svg  style="width:32px;"> [Nouvelle cote angulaire par 3Pts](TechDraw_Dimension_Angle3Pt/fr.md) : ajoute une cote d\'angle à partir de trois sommets.

-   <img alt="" src=images/TechDraw_Dimension_Horizontal_Extent.svg  style="width:32px;"> [Extension dimension horizontale](TechDraw_Dimension_Horizontal_Extent/fr.md) : ajoute une dimension d\'extension horizontale.{{Version/fr|0.19}}

-   <img alt="" src=images/TechDraw_Dimension_Vertical_Extent.svg  style="width:32px;"> [Extension dimension verticale](TechDraw_Dimension_Vertical_Extent/fr.md) : ajoute une dimension d\'extension verticale. {{Version/fr|0.19}}

-   <img alt="" src=images/TechDraw_Dimension_Link.svg  style="width:32px;"> [Nouveau lien](TechDraw_Dimension_Link/fr.md) : lie une cote existante à la géométrie 3D.

-   <img alt="" src=images/TechDraw_Balloon.svg  style="width:32px;"> [Nouvelle bulle](TechDraw_Balloon/fr.md) : ajout de notes \"bulles\" dans la page. {{Version/fr|0.19}}

-   <img alt="" src=images/Techdraw-landmarkdistance.svg  style="width:32px;"> [Dimension de repère](TechDraw_Dimension_Landmark/fr.md) : ajoute une cote linéaire. {{Version/fr|0.19}}

## Import/Export

Ce sont les outils pour exporter les pages vers d\'autre applications.

-   <img alt="" src=images/TechDraw_ExportPageSVG.svg  style="width:32px;"> [Sauvegarder au format SVG](TechDraw_ExportPageSVG/fr.md) : enregistre la page en cours sous forme de fichier [SVG](SVG/fr.md).

-   <img alt="" src=images/TechDraw_ExportPageDXF.svg  style="width:32px;"> [Sauvegarder au format DXF](TechDraw_ExportPageDXF/fr.md) : enregistre la page en cours sous forme de fichier [DXF](DXF/fr.md).

## Décorations

Ce sont les outils pour décorer l\'apparence des pages et des vues.

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [Hachures par motif](TechDraw_Hatch/fr.md) : hachure une face en utilisant un fichier image.

-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [Applique un motif de hachure](TechDraw_GeometricHatch/fr.md) : applique un motif de hachure à une face en utilisant une spécification Autodesk PAT.

-   <img alt="" src=images/TechDraw_Symbol.svg  style="width:32px;"> [Symbole SVG](TechDraw_Symbol/fr.md) : insère un symbole [SVG](SVG/fr.md) dans une page.

-   <img alt="" src=images/TechDraw_Image.svg  style="width:32px;"> [Nouvelle image Bitmap](TechDraw_Image/fr.md) : insère une image PNG ou JPG [bitmap](bitmap/fr.md) dans une page.

-   <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:32px;"> [Affichage des cadres](TechDraw_ToggleFrame/fr.md) : bascule l\'affichage des cadres et des étiquettes entourant une vue.

## Annotation

Les outils d\'annotation permettent de \"marquer\" un dessin avec des informations supplémentaires.

-   <img alt="" src=images/TechDraw_Annotation.svg  style="width:32px;"> [Insérer une annotation](TechDraw_Annotation/fr.md) : ajoute un bloc de texte pour servir d\'annotation.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_LeaderLine.svg  style="width:24px;"> [Ajout d\'une ligne de rappel](TechDraw_LeaderLine/fr.md) : ajoute une ligne d\'annotation à une vue. {{Version/fr|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width:24px;"> [Annotation texte enrichi](TechDraw_RichTextAnnotation/fr.md) : ajoute un bloc d'annotation en texte enrichi à une [Ligne de référence](TechDraw_LeaderLine/fr.md) ou à une vue. {{Version/fr|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width:24px;"> [Ajout point cosmétique](TechDraw_CosmeticVertex/fr.md) : ajoute un sommet qui ne fait pas partie de la géométrie principale. {{Version/fr|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Midpoints.svg  style="width:24px;"> [Points médians](TechDraw_Midpoints/fr.md) : ajoute des points cosmétiques aux points médians d\'une ou de plusieurs arêtes sélectionnées. {{Version/fr|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_Quadrants.svg  style="width:24px;"> [Quadrant](TechDraw_Quadrants/fr.md) : ajoute des points cosmétiques tous les quarts de points d\'un ou de plusieurs bords sélectionnés (circulaires). {{Version/fr|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:24px;"> [Ligne centrale à une face](TechDraw_FaceCenterLine/fr.md) : ajoute une ligne centrale aux face(s) sélectionnée(s). {{Version/fr|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_2LineCenterLine.svg  style="width:24px;"> [Ligne centrale entre 2 lignes](TechDraw_2LineCenterLine/fr.md) : ajoute une ligne centrale entre 2 arêtes. {{Version/fr|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_2PointCenterLine.svg  style="width:24px;"> [Ligne centrale entre 2 points](TechDraw_2PointCenterLine/fr.md) : ajoute une ligne centrale entre 2 points. {{Version/fr|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw-line2points.svg  style="width:24px;"> [Ligne cosmétique](TechDraw_2PointCosmeticLine/fr.md): ajoute une ligne cosmétique reliant 2 sommets. {{Version/fr|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:24px;"> [Gomme](TechDraw_CosmeticEraser/fr.md) : supprime les objets cosmétiques d\'une page. {{Version/fr|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:24px;"> [Apparence des lignes](TechDraw_DecorateLine/fr.md) : modifie l\'apparence des lignes. {{Version/fr|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ShowAll.svg  style="width:24px;"> [Montrer tout](TechDraw_ShowAll/fr.md) : affiche/masque les bords invisibles dans une vue. {{Version/fr|0.19}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width:24px;"> [Symbole de soudure](TechDraw_WeldSymbol/fr.md) : ajoute des spécifications de soudage à une Ligne de référence existante. {{Version/fr|0.19}}


</div>

## Extension Package {#extension_package}

The Extension Package includes many useful tools to improve your TechDraw drawings.


**Some of these tools have yet to be released.**

-   <img alt="" src=images/TechDraw_ToolCircleCenterLines.svg  style="width:32px;"> [CircleCenterLines](TechDraw_Extension_CircleCenterLines.md): adds center lines to circles. <small>(v0.20)</small> 
-   <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width:32px;"> [ThreadHoleSide](TechDraw_Extension_ThreadHoleSide.md): adds a symbolic thread at a side seen hole. <small>(v0.20)</small> 
-   <img alt="" src=images/TechDraw_ExtensionThreadHoleBottom.svg  style="width:32px;"> [ThreadHoleBottom](TechDraw_Extension_ThreadHoleBottom.md): adds a symbolic thread at a bottom seen hole. <small>(v0.20)</small> 
-   <img alt="" src=images/TechDraw_ExtensionThreadBoltSide.svg  style="width:32px;"> [ThreadBoltSide](TechDraw_Extension_ThreadBoltSide.md): adds a symbolic thread at a side seen bolt. <small>(v0.20)</small> 
-   <img alt="" src=images/TechDraw_ExtensionThreadBoltBottom.svg  style="width:32px;"> [ThreadBoltBottom](TechDraw_Extension_ThreadBoltBottom.md): adds a symbolic thread at a bottom seen bolt. <small>(v0.20)</small> 

## Fonctions additionnelles {#fonctions_additionnelles}

-   [Groupes de lignes](TechDraw_LineGroup/fr.md) : pour contrôler l\'apparence de divers types de lignes.
-   [Modèles](TechDraw_Templates/fr.md) : modèles par défaut définis pour les pages de dessin.
-   [Hachures](TechDraw_Hatching/fr.md) : explication des différentes techniques de hachurage.
-   [Dimensionnement géométrique et tolérancement.](TechDraw_Geometric_dimensioning_and_tolerancing/fr.md): explication sur la façon de réaliser le dimensionnement géométrique et le tolérancement.

## Préférences

-   <img alt="" src=images/Preferences-techdraw.svg  style="width:32px;"> [Préférences](TechDraw_Preferences/fr.md) : préférences pour les valeurs par défaut de la page de dessin, telles que l\'angle de projection, les couleurs, la taille du texte et les styles de trait.

## Script

Les outils TechDraw peuvent être utilisés dans des [macros](macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide de deux API :

-   [TechDraw API](TechDraw_API/fr.md)
-   [TechDrawGui API](TechDrawGui_API/fr.md)

## Limitations

-   Les dessins TechDraw et son API Python ne sont pas interchangeables avec l\'[atelier Drawing](Drawing_Workbench/fr.md) et son API. Il est possible de convertir des pages de dessin en pages TechDraw en utilisant un script Python (`moveViews.py`).
-   Il est possible d\'avoir à la fois des Pages TechDraw et Drawing dans le même document FreeCAD, chaque page étant complètement indépendante l'une de l'autre.
-   Il existe des différences mineures dans la spécification des textes modifiables dans les modèles [SVG](SVG/fr.md) par rapport au module Dessin. Dans TechDraw, la mise à l\'échelle du document SVG affecte la position des champs de texte modifiables. Voir la discussion du forum [échelle des modèles TechDraw](https://forum.freecadweb.org/viewtopic.php?f=3&t=24981&p=196271#p196271) pour plus de détails.
-   Les filetages ne sont pas implémentés. Une solution possible est d\'utiliser une [Dimension de diamètre](TechDraw_Dimension_Diameter/fr.md) et de mettre un texte approprié dans la propriété \"Format Spec\", par exemple \"M4x15\".
-   Ne coupez pas, ne copiez pas et ne collez pas d\'objets TechDraw dans l\'arborescence, car cela ne fonctionne généralement pas bien.

## Tutoriels

-   [Tutoriel TechDraw de base](Basic_TechDraw_Tutorial/fr.md): introduction à la création de dessins avec l\'atelier TechDraw.
-   [Comment créer un modèle](TechDraw_TemplateHowTo/fr.md): instructions pour créer un nouveau modèle de page dans Inkscape à utiliser avec l\'atelier TechDraw.
-   [Mesure des angles sur les axes des trous](Measurement_Of_Angles_On_Holes/fr.md): instructions pour ajouter des lignes centrales et des représentations angulaires ultérieures sur les trous.
-   [Comment](TechDraw_HowTo_Page.md): instructions pour différents paramètres tels que les marques centrales etc\...

Tutoriels video par sliptonic

-   Atelier TechDraw [Part 1 (Basics)](https://www.youtube.com/watch?v=7LbOmSGW9F0), [Part 2 (Dimensions)](https://www.youtube.com/watch?v=z3w84RfvqaE), [Part 3 (Multivues)](https://www.youtube.com/watch?v=uNjXg-m38aI)
-   Atelier TechDraw [Part 4 (Sections et Details)](https://www.youtube.com/watch?v=3zSdeFV6I5o), [Part 5 (Création de feuilles de dessin)](https://www.youtube.com/watch?v=kcmdJ7xa7gg)





{{TechDraw Tools navi

}} 

[Category:Workbenches{{\#translation:}}](Category:Workbenches.md)
