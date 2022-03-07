# <img alt="Icône de l\'Atelier Part" src=images/Workbench_Part.svg  style="width:64px;"> Part Module/fr


{{TOCright}}

## Introduction

Les capacités de modélisations de solides de FreeCAD sont basées sur le noyau [OpenCASCADE Technology](OpenCASCADE/fr.md) (OCCT), un système de CAO de niveau professionnel qui offre une création et une manipulation avancées de la géométrie 3D. L\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md) est une couche située au-dessus des bibliothèques OCCT qui permet à l\'utilisateur d\'accéder aux primitives et fonctions géométriques OCCT. Toutes les fonctions de dessin 2D et 3D de chaque atelier (<img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/fr.md), <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher](Sketcher_Workbench/fr.md), <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/fr.md), etc.), sont basées sur ces fonctions exposées par l\'atelier Part. Par conséquent, L\'atelier Part est considéré comme le composant central des capacités de modélisation de FreeCAD.

Une discussion plus détaillée de l\'atelier Part par rapport à l\'atelier Part Design peut être trouvée ici: [Part et Part Design](Part_and_PartDesign/fr.md).

Les objets créés avec l\'atelier Part sont relativement simples. ils sont destinés à être utilisés avec des opérations booléennes (unions et coupes) afin de créer des formes plus complexes. **Ce paradigme de modélisation est connu sous le nom de \[CSG\] [Géométrie Solide Constructive](constructive_solid_geometry/fr.md) et constitue la méthodologie traditionnelle utilisée dans les premiers systèmes de CAO**. D\'autre part, l\'[atelier PartDesign](PartDesign_Workbench/fr.md) fournit un flux de travail plus moderne pour la construction de formes: il utilise des croquis définis de manière paramétrique, qui sont extrudés pour former un corps solide de base, qui est ensuite modifié par des transformations paramétriques ([édition de fonctions](feature_editing/fr.md)), jusqu\'à l\'obtention de l\'objet final.

Les objets Part sont plus complexes que les objets maillés créés avec [l\'atelier Mesh](Mesh_Workbench/fr.md), les objets Part sont plus complexes et permettent donc des opérations plus avancées telles que les opérations booléennes cohérentes, l\'historique des modifications et le comportement paramétrique.

<img alt="" src=images/Part_Workbench_relationships.svg  style="width:600px;">



*L'atelier Part est la couche de base qui expose les fonctions de dessin OCCT à tous les ateliers de FreeCAD.*

## Les outils 

Les outils de l\'atelier Part sont situés dans les menus **Pièce** ou **Mesure**.

### Primitives

Ce sont des outils pour créer des objets primitifs.

-   <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Cube](Part_Box/fr.md): Dessine un cube.

-   <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cylindre](Part_Cylinder/fr.md): Dessine un cylindre.

-   <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Sphère](Part_Sphere/fr.md): Dessine une sphère.

-   <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cône](Part_Cone/fr.md): Dessine un cône.

-   <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Tore](Part_Torus/fr.md) : Dessine un tore.

-   <img alt="" src=images/Part_Tube.svg  style="width:32px;"> [Tube](Part_Tube/fr.md) : Dessine un tube {{Version/fr|0.19}}.

-   <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [Créer des primitives\...](Part_Primitives/fr.md) : Outil pour créer l\'une des primitives suivantes :
    -   <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Plan](Part_Plane/fr.md) : Crée un plan.
    -   <img alt="" src=images/Tree_Part_Box_Parametric.svg  style="width:32px;"> [Cube](Part_Box/fr.md) : Crée une boîte. Cet objet peut également être créé avec l\'outil <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Cube](Part_Box/fr.md).
    -   <img alt="" src=images/Tree_Part_Cylinder_Parametric.svg  style="width:32px;"> [Cylindre](Part_Cylinder/fr.md) : Crée un cylindre. Cet objet peut également être créé avec la <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Cylindre](Part_Cylinder/fr.md).
    -   <img alt="" src=images/Tree_Part_Cone_Parametric.svg  style="width:32px;"> [Cône](Part_Cone/fr.md) : Crée un cône. Cet objet peut également être créé avec la <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cône](Part_Cone/fr.md).
    -   <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:32px;"> [Sphère](Part_Sphere/fr.md) : Crée une sphère. Cet objet peut également être créé avec la <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> L\'outil [Sphère](Part_Sphere/fr.md).
    -   <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Ellipsoïde](Part_Ellipsoid/fr.md) : Crée un ellipsoïde.
    -   <img alt="" src=images/Tree_Part_Torus_Parametric.svg  style="width:32px;"> [Tore](Part_Torus/fr.md) : Crée un tore. Cet objet peut aussi être créé avec la <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Tore](Outil_Part_Torus/fr.md).
    -   <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Prisme](Part_Prism/fr.md) : Crée un prisme.
    -   <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Pyramide tronquée](Part_Wedge/fr.md) : Crée une pyramide tronquée.
    -   <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Hélice](Part_Helix/fr.md) : Crée une hélice.
    -   <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Spirale](Part_Spiral/fr.md) : Crée une spirale.
    -   <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Cercle](Part_Circle/fr.md) : Crée un arc de cercle.
    -   <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Ellipse](Part_Ellipse/fr.md) : Crée un arc elliptique.
    -   <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Point](Part_Point/fr.md) : Crée un point.
    -   <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Ligne](Part_Line/fr.md) : Crée une ligne.
    -   <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Polygone régulier](Part_RegularPolygon/fr.md) : Crée un polygone régulier.

-   <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Générateur de formes](Part_Builder/fr.md) : Crée des formes à partir de diverses primitives.

### Création et modification 

Il s\'agit d\'outils permettant de créer de nouveaux objets et de modifier des objets existants.

-   <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> [Extrusion](Part_Extrude/fr.md): Extrude les faces planes d\'un objet

-   <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> [Révolution](Part_Revolve/fr.md): Crée un solide en faisant tourner un autre objet (pas un solide) autour d\'un axe.

-   <img alt="" src=images/Part_Mirror.svg  style="width:32px;"> [Miroir](Part_Mirror/fr.md): Reflète l\'objet sélectionné sur un plan de miroir.

-   <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> [Congé](Part_Fillet/fr.md): Congés (arrondi) d\'arêtes d\'un objet.

-   <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> [Chanfrein](Part_Chamfer/fr.md): Chanfreine les bords d\'un objet.

-   <img alt="" src=images/Part_MakeFace.svg  style="width:32px;"> [Face à partir de fils](Part_MakeFace/fr.md): Génère une face à partir d\'un ensemble de fils (contours). {{Version/fr|0.19}}

-   <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> [Surface réglée](Part_RuledSurface/fr.md): Crée une surface réglée.

-   <img alt="" src=images/Part_Loft.svg  style="width:32px;"> [Lissage](Part_Loft/fr.md): Crée une forme lissée d\'un profil à un autre.

-   <img alt="" src=images/Part_Sweep.svg  style="width:32px;"> [Balayage](Part_Sweep/fr.md): Crée une forme en balayant un ou plusieurs profils le long d\'un chemin.

-   <img alt="" src=images/Part_Section.svg  style="width:32px;"> [Section](Part_Section/fr.md): Crée une section par intersection d\'un objet avec un plan de coupe.

-   <img alt="" src=images/Part_CrossSections.svg  style="width:32px;"> [Coupes](Part_CrossSections/fr.md) : Crée une ou plusieurs coupes transversales à travers une forme sélectionnée.

-   <img alt="" src=images/Part_CompOffsetTools.png  style="width:48px;"> [Outils de décalage](Part_CompOffsetTools/fr.md):
    -   <img alt="" src=images/Part_Offset.svg  style="width:32px;"> [Décalage 3D](Part_Offset/fr.md): Construit une forme parallèle à une certaine distance de l\'original.
    -   <img alt="" src=images/Part_Offset2D.svg  style="width:32px;"> [Décalage 2D](Part_Offset2D/fr.md): Construit un fil parallèle à une certaine distance de l\'original ou agrandit/réduit une face plane.

-   <img alt="" src=images/Part_Thickness.svg  style="width:32px;"> [Evidement](Part_Thickness/fr.md): Creuse un solide pour en faire comme une coque.

-   <img alt="" src=images/Part_ProjectionOnSurface.svg  style="width:32px;"> [Projection sur une surface](Part_ProjectionOnSurface/fr.md): Projette un logo, un texte ou une face, un fil ou une arête sur une surface. {{Version/fr|0.19}}

-   <img alt="" src=images/Part_EditAttachment.svg  style="width:32px;"> [Ancrage](Part_EditAttachment/fr.md): Rattache un objet à un autre objet.

### Booléen

Ces outils effectuent des opérations booléennes.

-   <img alt="" src=images/Part_CompCompoundTools.png  style="width:48px;"> [Outils pour Composés](Part_CompCompoundTools/fr.md) :
    -   <img alt="" src=images/Part_Compound.svg  style="width:32px;"> [Créer un composé](Part_Compound/fr.md) : Crée un composé à partir des objets sélectionnés.
    -   <img alt="" src=images/_Part_ExplodeCompound.png  style="width:32px;"> [Éclater le composé](Part_ExplodeCompound/fr.md) : Sépare les composés de formes.
    -   <img alt="" src=images/Part_Compound‏‎Filter.svg  style="width:32px;"> [Filtre composé](Part_Compound‏‎Filter/fr.md) : Extrait les pièces individuelles des composés.

-   <img alt="" src=images/Part_Booleans.svg  style="width:32px;"> [Opération booléenne](Part_Boolean/fr.md) : Effectue des opérations booléennes sur des objets.

-   <img alt="" src=images/Part_Cut.svg  style="width:32px;"> [Soustraction](Part_Cut/fr.md) : Soustrait un objet d\'un autre.

-   <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Union](Part_Fuse/fr.md) : Union de deux objets.

-   <img alt="" src=images/Part_Common.svg  style="width:32px;"> [Intersection](Part_Common/fr.md) : Extrait la partie commune (intersection) de deux objets.

-   <img alt="" src=images/Part_CompJoinFeatures.png  style="width:48px;"> [Joindre des objets à parois](Part_CompJoinFeatures/fr.md) :
    -   <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> [Connecter](Part_JoinConnect/fr.md) : Relie les intérieurs d\'objets fermés.
    -   <img alt="" src=images/Part_JoinEmbed.svg  style="width:32px;"> [Intégrer](Part_JoinEmbed/fr.md) : Intègre un objet à un autre objet.
    -   <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> [Découpe](Part_JoinCutout/fr.md) : Crée une découpe dans un objet en fonction d\'un autre objet.

-   <img alt="" src=images/Part_CompSplittingTools.png  style="width:48px;"> [Outils de division de formes](Part_CompSplittingTools/fr.md):
    -   <img alt="" src=images/Part_BooleanFragments.svg  style="width:32px;"> [Fragments booléens](Part_BooleanFragments/fr.md): Crée toutes les pièces pouvant être obtenues par des opérations booléennes entre objets
    -   <img alt="" src=images/Part_SliceApart.png  style="width:32px;"> [Trancher une pièce](Part_SliceApart/fr.md): Coupe et divise un objet par intersection avec d\'autres objets.
    -   <img alt="" src=images/Part_Slice.svg  style="width:32px;"> [Scinder](Part_Slice/fr.md): Divise un objet en morceaux par intersection avec un autre objet.
    -   <img alt="" src=images/Part_XOR.svg  style="width:32px;"> [OU exclusif](Part_XOR/fr.md): Supprime l\'espace partagé (commun) par un nombre pair d\'objets (version symétrique de [Soustraction booléenne](Part_Cut/fr.md)).

### Mesure

<img alt="" src=images/Std_Measure_Menu.png  style="width:64px;"> [Mesure](Part_Measure_Menu/fr.md): Outils pour les mesures linéaires et angulaires.

-   <img alt="" src=images/Part_Measure_Linear.svg  style="width:32px;"> [Mesure linéaire](Part_Measure_Linear/fr.md): Crée une mesure linéaire.

-   <img alt="" src=images/Part_Measure_Angular.svg  style="width:32px;"> [Mesure angulaire](Part_Measure_Angular/fr.md): Crée une mesure angulaire.

-   <img alt="" src=images/Part_Measure_Refresh.svg  style="width:32px;"> [Rafraîchir les mesures](Part_Measure_Refresh/fr.md): Met à jour les mesures.

-   <img alt="" src=images/Part_Measure_Clear_All.svg  style="width:32px;"> [Effacer toute mesure](Part_Measure_Clear_All/fr.md): Efface toutes les mesures.

-   <img alt="" src=images/Part_Measure_Toggle_All.svg  style="width:32px;"> [Basculer tout](Part_Measure_Toggle_All/fr.md): Affiche ou masque toutes les mesures.

-   <img alt="" src=images/Part_Measure_Toggle_3d.svg  style="width:32px;"> [Basculer 3D](Part_Measure_Toggle_3d/fr.md): Affiche ou masque les mesures 3D.

-   <img alt="" src=images/Part_Measure_Toggle_Delta.svg  style="width:32px;"> [Basculer Delta](Part_Measure_Toggle_Delta/fr.md): Affiche ou masque les mesures delta.

### Autres outils 

-   <img alt="" src=images/Part_Import.svg  style="width:32px;"> [Importation](Part_Import/fr.md) : Importe depuis des fichiers \*.IGES, \*.STEP ou \*.BREP.

-   <img alt="" src=images/Part_Export.svg  style="width:32px;"> [Exportation](Part_Export/fr.md) : Exporte vers des fichiers \*.IGES, \*.STEP ou \*.BREP.

-   <img alt="" src=images/Part_BoxSelection.svg  style="width:32px;"> [Sélection par zone](Part_BoxSelection/fr.md) : Sélectionne les faces dans une zone rectangulaire.

-   <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:32px;"> [Forme à partir du maillage](Part_ShapeFromMesh/fr.md) : Crée un objet de forme à partir d\'un objet de maillage.

-   <img alt="" src=images/Part_PointsFromMesh.svg  style="width:32px;"> [Points à partir de maillage](Part_PointsFromMesh/fr.md) : Crée un objet de forme constitué de points du maillage. {{Version/fr|0.19}}

-   <img alt="" src=images/Part_MakeSolid.svg  style="width:32px;"> [Convertir en solide](Part_MakeSolid/fr.md) : Convertit un objet forme en objet solide.

-   <img alt="" src=images/Part_ReverseShapes.svg  style="width:32px;"> [Inverser les formes](Part_ReverseShapes/fr.md) : Inverse les normales de toutes les faces de l\'objet sélectionné.

-   Créer une copie :
    -   <img alt="" src=images/Part_SimpleCopy‎.svg  style="width:32px;"> [Créer une copie simple](Part_SimpleCopy/fr.md) : Crée une copie simple de l\'objet sélectionné.
    -   <img alt="" src=images/Part_TransformedCopy.svg  style="width:32px;"> [Créer une copie transformée](Part_TransformedCopy/fr.md) : Crée une copie transformée de l\'objet sélectionné. {{Version/fr|0.19}}
    -   <img alt="" src=images/Part_ElementCopy.svg  style="width:32px;"> [Créer une copie d\'élément de la forme](Part_ElementCopy/fr.md) : Crée une copie d\'un élément (sommet, arête, face) de l\'objet sélectionné. {{Version/fr|0.19}}
    -   <img alt="" src=images/Part_RefineShape.svg  style="width:32px;"> [Affiner la forme](Part_RefineShape/fr.md) : Nettoie les faces en supprimant les lignes inutiles.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Vérifier la géométrie](Part_CheckGeometry/fr.md): Vérifie la géométrie des objets sélectionnés pour en détecter les erreurs.

-   <img alt="" src=images/Part_Defeaturing.svg  style="width:32px;"> [Défaire une fonctionnalité](Part_Defeaturing/fr.md): Supprime les fonctionnalités d\'un objet.

### Éléments du menu contextuel 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Apparence](Std_SetAppearance/fr.md): Détermine l\'apparence d\'un objet entier (couleur, transparence, etc.).

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Définir les couleurs](Part_FaceColors/fr.md): Attribue des couleurs aux faces des pièces.

## Préférences

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [PartDesign Préférences](PartDesign_Preferences/fr.md): Préférences disponibles pour les outils de Part (l\'atelier Part utilise également les préférences PartDesign).
-   <img alt="" src=images/Preferences-import-export.svg  style="width:32px;"> [Préférences d\'Import Export](Import_Export_Preferences/fr.md): Préférences disponibles pour l\'importation et l\'exportation vers différents formats de fichier.
-   [Réglage fin](Fine-tuning/fr.md): Quelques paramètres supplémentaires pour affiner le comportement de la partie.

## Script

Voir [Part Ecrire un script](Part_scripting/fr.md)

## Tutoriels

-   [Importer depuis STL ou OBJ](Import_from_STL_or_OBJ/fr.md) : Comment importer les fichiers STL/OBJ dans FreeCAD
-   [Exportation de fichier STL ou OBJ](Export_to_STL_or_OBJ/fr.md) : Comment exporter les fichiers STL/OBJ avec FreeCAD
-   [Tutoriel balle Whiffle](Whiffle_Ball_tutorial/fr.md) : Comment utiliser l\'atelier Part



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Part](Part_Workbench.md) > Part Module/fr
