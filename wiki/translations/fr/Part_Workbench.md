# <img alt="Icône de l\'atelier Part" src=images/Workbench_Part.svg  style="width:64px;"> Part Workbench/fr




## Introduction

L\'<img alt="" src=images/Workbench_Part.svg  style="width:32px;"> **atelier Part** fournit un flux de travail traditionnel de [géométrie de construction de solides](Constructive_solid_geometry/fr.md) (CSG en anglais). Dans ce processus, chaque objet est un solide indépendant. L\'atelier Part peut les créer à partir d\'[esquisses](Sketcher_Workbench/fr.md) paramétriques à l\'aide d\'outils tels que une [extrusion](Part_Extrude/fr.md), une [révolution](Part_Revolve/fr.md), un [lissage](Part_Loft/fr.md), etc. En outre, des solides primitifs de base comme [cube](Part_Box/fr.md), un [cylindre](Part_Cylinder/fr.md), etc. peuvent également être créés. Ces objets peuvent être combinés, par le biais d\'opérations booléennes, pour créer des solides plus complexes.

L\'atelier Part peut également créer des objets qui ne sont pas des solides, tels que des faces, des coques et des objets ne comportant que des arêtes ou des sommets. Il fournit également une variété d\'outils d\'usage général pour la manipulation et la validation de géométries, ainsi que pour la réalisation de copies.

L\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [atelier PartDesign](PartDesign_Workbench/fr.md) utilise un autre flux de travail pour créer des solides. Pour une discussion détaillée sur l\'atelier Part par rapport à l\'atelier PartDesign, voir [Part et PartDesign](Part_and_PartDesign/fr.md).

![](images/Part_Workbench_Example.jpg )



## Les outils 



### Barres d\'outils des solides 

-   <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Cube](Part_Box/fr.md) : dessine un cube.

-   <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cylindre](Part_Cylinder/fr.md) : dessine un cylindre.

-   <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Sphère](Part_Sphere/fr.md) : dessine une sphère.

-   <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cône](Part_Cone/fr.md) : dessine un cône.

-   <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Tore](Part_Torus/fr.md) : dessine un tore.

-   <img alt="" src=images/Part_Tube.svg  style="width:32px;"> [Tube](Part_Tube/fr.md) : crée un tube.

-   <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [Créer des primitives\...](Part_Primitives/fr.md) : outil pour créer l\'une des primitives suivantes :

  - <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Plan](Part_Plane/fr.md) : crée un plan.

  - <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Cube](Part_Box/fr.md) : crée une boîte. Cet objet peut également être créé avec l\'outil [Cube](Part_Box/fr.md).

  - <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cylindre](Part_Cylinder/fr.md) : crée un cylindre. Cet objet peut également être créé avec l\'outil [Cylindre](Part_Cylinder/fr.md).

  - <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cône](Part_Cone/fr.md) : crée un cône. Cet objet peut également être créé avec l\'outil [Cône](Part_Cone/fr.md).

  - <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Sphère](Part_Sphere/fr.md) : crée une sphère. Cet objet peut également être créé avec l\'outil [Sphère](Part_Sphere/fr.md).

  - <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Ellipsoïde](Part_Ellipsoid/fr.md) : crée un ellipsoïde.

  - <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Tore](Part_Torus/fr.md) : crée un tore. Cet objet peut aussi être créé avec l\'outil [Tore](Part_Torus/fr.md).

  - <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Prisme](Part_Prism/fr.md) : crée un prisme.

  - <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Pyramide tronquée](Part_Wedge/fr.md) : crée une pyramide tronquée.

  - <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Hélice](Part_Helix/fr.md) : crée une hélice.

  - <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Spirale](Part_Spiral/fr.md) : crée une spirale.

  - <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Cercle](Part_Circle/fr.md) : crée un arc de cercle.

  - <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Ellipse](Part_Ellipse/fr.md) : crée un arc elliptique.

  - <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Point](Part_Point/fr.md) : crée un point.

  - <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Ligne](Part_Line/fr.md) : crée une ligne.

  - <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Polygone régulier](Part_RegularPolygon/fr.md) : crée un polygone régulier.

-   <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Générateur de formes](Part_Builder/fr.md) : crée des formes à partir de diverses primitives.



### Barres d\'outils des outils de Part 

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Créer une esquisse](Sketcher_NewSketch/fr.md) : crée une nouvelle esquisse et ouvre la [fenêtre de dialogue](Sketcher_Dialog/fr.md) pour la modifier.

-   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Extrusion](Part_Extrude/fr.md) : extrude les faces planes d\'un objet.

-   <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> [Révolution](Part_Revolve/fr.md) : crée un solide en faisant tourner un autre objet (pas un solide) autour d\'un axe.

-   <img alt="" src=images/Part_Mirror.svg  style="width:32px;"> [Objet en miroir](Part_Mirror/fr.md) : reflète l\'objet sélectionné sur un plan de miroir.

-   <img alt="" src=images/Part_Scale.svg  style="width:32px;"> [Échelle](Part_Scale/fr.md) : met à l\'échelle une ou plusieurs formes. {{Version/fr|1.0}}

-   <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Congé](Part_Fillet/fr.md) : congés (arrondi) d\'arêtes d\'un objet.

-   <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> [Chanfrein](Part_Chamfer/fr.md) : chanfreine les bords d\'un objet.

-   <img alt="" src=images/Part_MakeFace.svg  style="width:32px;"> [Face à partir de polylignes](Part_MakeFace/fr.md) : génère une face à partir d\'un ensemble de polylignes (contours).

-   <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> [Surface réglée](Part_RuledSurface/fr.md) : crée une surface réglée.

-   <img alt="" src=images/Part_Loft.svg  style="width:32px;"> [Lissage](Part_Loft/fr.md) : crée une forme lissée d\'un profil à un autre.

-   <img alt="" src=images/Part_Sweep.svg  style="width:32px;"> [Balayage](Part_Sweep/fr.md) : crée une forme en balayant un ou plusieurs profils le long d\'un chemin.

-   <img alt="" src=images/Part_Section.svg  style="width:32px;"> [Section](Part_Section/fr.md) : crée une section par intersection d\'un objet avec un plan de coupe.

-   <img alt="" src=images/Part_CrossSections.svg  style="width:32px;"> [Coupes](Part_CrossSections/fr.md) : crée une ou plusieurs coupes transversales à travers une forme sélectionnée.

-   <img alt="" src=images/Part_Offset.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Décalage:

  - <img alt="" src=images/Part_Offset.svg  style="width:32px;"> [Décaler en 3D](Part_Offset/fr.md) : construit une forme parallèle à une certaine distance de l\'original.

  - <img alt="" src=images/Part_Offset2D.svg  style="width:32px;"> [Décaler en 2D](Part_Offset2D/fr.md) : construit une polyligne parallèle à une certaine distance de l\'originale ou agrandit/réduit une face plane.

-   <img alt="" src=images/Part_Thickness.svg  style="width:32px;"> [Évider](Part_Thickness/fr.md) : creuse un solide pour en faire comme une coque.

-   <img alt="" src=images/Part_ProjectionOnSurface.svg  style="width:32px;"> [Projeter sur une surface](Part_ProjectionOnSurface/fr.md) : projette un logo, un texte ou une face, une polyligne ou une arête sur une surface.

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Couleur par face](Part_ColorPerFace/fr.md) : attribue des couleurs aux faces des pièces.



### Barres d\'outils des booléens 

-   <img alt="" src=images/Part_Compound.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Composé:

  - <img alt="" src=images/Part_Compound.svg  style="width:32px;"> [Créer un composé](Part_Compound/fr.md) : crée un composé à partir des objets sélectionnés.

  - <img alt="" src=images/_Part_ExplodeCompound.png  style="width:32px;"> [Éclater le composé](Part_ExplodeCompound/fr.md) : sépare les composés de formes.

  - <img alt="" src=images/Part_CompoundFilter.svg  style="width:32px;"> [Filtre de composé](Part_CompoundFilter/fr.md) : extrait les pièces composantes de composés.

-   <img alt="" src=images/Part_Booleans.svg  style="width:32px;"> [Opération booléenne](Part_Boolean/fr.md) : effectue des opérations booléennes sur deux objets.

-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Soustraction](Part_Cut/fr.md) : soustrait un objet d\'un autre.

-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Union](Part_Fuse/fr.md) : unit deux ou plus d\'objets.

-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Intersection](Part_Common/fr.md) : extrait la partie commune de deux objets.

-   <img alt="" src=images/Part_JoinConnect.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Joindre:

  - <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> [Connecter](Part_JoinConnect/fr.md) : relie les intérieurs d\'objets fermés.

  - <img alt="" src=images/Part_JoinEmbed.svg  style="width:32px;"> [Intégrer](Part_JoinEmbed/fr.md) : intègre un objet à un autre objet.

  - <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> [Découper](Part_JoinCutout/fr.md) : crée une découpe dans un objet en fonction d\'un autre objet.

-   <img alt="" src=images/Part_BooleanFragments.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Scinder:

  - <img alt="" src=images/Part_BooleanFragments.svg  style="width:32px;"> [Fragments booléens](Part_BooleanFragments/fr.md) : crée toutes les pièces obtenues par des opérations booléennes.

  - <img alt="" src=images/Part_SliceApart.png  style="width:32px;"> [Séparer/exploser](Part_SliceApart/fr.md) : sépare et explose un objet par intersection avec d\'autres objets.

  - <img alt="" src=images/Part_Slice.svg  style="width:32px;"> [Scinder](Part_Slice/fr.md) : scinde un objet en morceaux par intersection avec d\'autres objets.

  - <img alt="" src=images/Part_XOR.svg  style="width:32px;"> [OU exclusif](Part_XOR/fr.md) : supprime l\'espace partagé (commun) par un nombre pair d\'objets.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Vérifier la géométrie](Part_CheckGeometry/fr.md) : vérifie la géométrie des objets sélectionnés pour en détecter les erreurs.

-   <img alt="" src=images/Part_Defeaturing.svg  style="width:32px;"> [Supprimer la fonction](Part_Defeaturing/fr.md) : supprime des fonctions d\'un objet.



### Autres outils 

-   <img alt="" src=images/Part_Import.svg  style="width:32px;"> [Importation](Part_Import/fr.md) : importe des fichiers \*.IGES, \*.STEP ou \*.BREP.

-   <img alt="" src=images/Part_Export.svg  style="width:32px;"> [Exportation](Part_Export/fr.md) : exporte des fichiers \*.IGES, \*.STEP ou \*.BREP.

-   <img alt="" src=images/Part_BoxSelection.svg  style="width:32px;"> [Sélection par boîte](Part_BoxSelection/fr.md) : sélectionne les faces dans une zone rectangulaire.

-   <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:32px;"> [Forme à partir du maillage](Part_ShapeFromMesh/fr.md) : crée des formes à partir d\'objets maillés.

-   <img alt="" src=images/Part_PointsFromMesh.svg  style="width:32px;"> [Points à partir de maillage](Part_PointsFromMesh/fr.md) : crée des objets points à partir d\'objets géométriques.

-   <img alt="" src=images/Part_MakeSolid.svg  style="width:32px;"> [Convertir en solide](Part_MakeSolid/fr.md) : crée des solides à partir d\'objets de forme.

-   <img alt="" src=images/Part_ReverseShape.svg  style="width:32px;"> [Inverser les formes](Part_ReverseShape/fr.md) : crée des copies paramétriques avec des normales de face inversées à partir d\'objets sélectionnés.

-   Copie :

  - <img alt="" src=images/Part_SimpleCopy.svg  style="width:32px;"> [Copie simple](Part_SimpleCopy/fr.md) : crée des copies non paramétriques à partir d\'objets.

  - <img alt="" src=images/Part_TransformedCopy.svg  style="width:32px;"> [Copie transformée](Part_TransformedCopy/fr.md) : crée des copies non paramétriques à partir d\'objets. Elle est destinée aux objets imbriqués dans des conteneurs.

  - <img alt="" src=images/Part_ElementCopy.svg  style="width:32px;"> [Copie d\'élément de la forme](Part_ElementCopy/fr.md) : crée des copies non paramétriques de sous-éléments : sommets, arêtes et faces.

  - <img alt="" src=images/Part_RefineShape.svg  style="width:32px;"> [Affiner la forme](Part_RefineShape/fr.md) : crée des copies paramétriques avec une forme affinée à partir des objets sélectionnés. Cette commande supprime les arêtes inutiles des faces planes et cylindriques.

-   <img alt="" src=images/Part_EditAttachment.svg  style="width:32px;"> [Ancrage](Part_EditAttachment/fr.md) : rattache un objet à un ou plusieurs autres objets.



## Outils obsolètes 



### Mesure

L\'outil <img alt="" src=images/Std_Measure.svg  style="width:32px;"> [Mesurer](Std_Measure/fr.md) remplace les outils listés ci-dessous. {{Version/fr|1.0}}

-   <img alt="" src=images/Part_Measure_Linear.svg  style="width:32px;"> [Mesure linéaire](Part_Measure_Linear/fr.md) : crée une mesure linéaire. Non disponible dans {{VersionPlus/fr|1.0}}.

-   <img alt="" src=images/Part_Measure_Angular.svg  style="width:32px;"> [Mesure angulaire](Part_Measure_Angular/fr.md) : crée une mesure angulaire. Non disponible dans {{VersionPlus/fr|1.0}}.

-   <img alt="" src=images/Part_Measure_Refresh.svg  style="width:32px;"> [Rafraîchir les mesures](Part_Measure_Refresh/fr.md) : met à jour les mesures. Non disponible dans {{VersionPlus/fr|1.0}}.

-   <img alt="" src=images/Part_Measure_Clear_All.svg  style="width:32px;"> [Effacer toute mesure](Part_Measure_Clear_All/fr.md) et [Affichage Supprimer les mesures](View_Measure_Clear_All/fr.md): efface toutes les mesures. Non disponible dans {{VersionPlus/fr|1.0}}.

-   <img alt="" src=images/Part_Measure_Toggle_All.svg  style="width:32px;"> [Tout basculer](Part_Measure_Toggle_All/fr.md) et [Affichage Basculer les mesures](View_Measure_Toggle_All/fr.md) : affiche ou masque toutes les mesures. Non disponible dans {{VersionPlus/fr|1.0}}.

-   <img alt="" src=images/Part_Measure_Toggle_3D.svg  style="width:32px;"> [Mesures dans la 3D](Part_Measure_Toggle_3D/fr.md) : affiche ou masque les mesures dans la 3D. Non disponible dans {{VersionPlus/fr|1.0}}.

-   <img alt="" src=images/Part_Measure_Toggle_Delta.svg  style="width:32px;"> [Mesures selon le repère global](Part_Measure_Toggle_Delta/fr.md) : affiche ou masque les mesures dans le repère global. Non disponible dans {{VersionPlus/fr|1.0}}.



## Préférences

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Préférences](PartDesign_Preferences/fr.md) : préférences de l\'atelier Part.
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Préférences Importer/Exporter](Import_Export_Preferences/fr.md) : préférences pour l\'importation et l\'exportation vers différents formats de fichier.
-   [Réglage fin](Fine-tuning/fr#Atelier_Part/fr.md) : quelques paramètres supplémentaires pour affiner le comportement de la partie.



## Script

Voir [Part Écrire un script](Part_scripting/fr.md)



## Tutoriels

-   [Importer depuis STL ou OBJ](Import_from_STL_or_OBJ/fr.md) : comment importer les fichiers STL/OBJ dans FreeCAD
-   [Exportation de fichier STL ou OBJ](Export_to_STL_or_OBJ/fr.md) : comment exporter les fichiers STL/OBJ avec FreeCAD
-   [Tutoriel balle Whiffle](Whiffle_Ball_tutorial/fr.md) : comment utiliser l\'atelier Part



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Part](Category_Part.md) > Part Workbench/fr
