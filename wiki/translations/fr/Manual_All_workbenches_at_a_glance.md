# Manual:All workbenches at a glance/fr
{{Manual:TOC/fr}}

L\'une des plus grandes difficultés pour les nouveaux utilisateurs de FreeCAD est de savoir dans quel atelier trouver un outil spécifique. Le tableau ci-dessous vous donnera un aperçu des ateliers les plus importants et leurs outils. Reportez-vous à chaque page [atelier](Workbenches/fr.md) dans la documentation FreeCAD pour une liste complète d\'informations.

Quatre ateliers sont également conçus pour travailler par paires, et l\'un d\'entre eux est entièrement inclus dans l\'autre : Arch contient tous les outils Draft, et PartDesign tous les outils Sketcher. Cependant, pour plus de clarté, ils sont séparés ci-dessous.

### Atelier Part (Pièces) 

L'atelier Part fournit des outils de base pour travailler avec des pièces solides : primitives, telles que cubes et sphères, des opérations géométriques simples et des opérations Booléennes. Êtant le principal point d\'ancrage avec [OpenCasCade](https://fr.wikipedia.org/wiki/Open_CASCADE_Technology), l'atelier Part fournit la base du système de géométrie de FreeCAD, et presque tous les autres ateliers produisent une géométrie partielle.

  Outil                                                                                                                       Description                                                                                          Outil                                                                                                                              Description
  --------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------
  <img alt="" src=images/Part_Box.svg  style="width:32px;"> _                                                 Dessine un cône en spécifiant ses dimensions
  <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> _                                         Dessine une sphère en spécifiant ses dimensions
  <img alt="" src=images/Part_Torus.svg  style="width:32px;"> _               Outil pour créer différentes primitives géométriques paramétriques
  <img alt="" src=images/Part_Builder.svg  style="width:32px;"> _                                                Fusionne (additionne) deux objets
  <img alt="" src=images/Part_Common.svg  style="width:32px;"> _                                            Soustrait un objet à un autre
  <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> _                Intègre un objet creux dans un autre objet creux
  <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> _                                   Extrude les faces planes d\'un objet
  <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> _                                  Crée un objet par révolution d\'un autre objet autour d\'un axe
  <img alt="" src=images/Part_Section.svg  style="width:32px;"> _   Crée une coupe par l\'intersection d\'un objet avec plusieurs plans de coupe
  <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> _                                       Crée la symétrie de l\'objet sélectionné par rapport à un plan donné
  <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> _                                         Balayage d\'un ou plusieurs profils le long d\'un chemin (ligne fermée ou non)
  <img alt="" src=images/Part_Loft.svg  style="width:32px;"> _                                       Crée une copie décalée de l\'objet sélectionné
  <img alt="" src=images/Part_Thickness.svg  style="width:32px;"> [Epaisseur](Part_Thickness/fr.md)                      Affecte une épaisseur aux faces d\'une forme                                                                                                                                                                                            

### Atelier Draft (Planche à dessin) 

L'atelier Planche à dessin (Draft) fournit des outils pour effectuer des tâches de dessin de base en 2D : lignes, cercles, etc. et une série d\'outils génériques utiles tels que le déplacement, la rotation ou le changement d\'échelle. Il fournit également plusieurs aides au dessin, telles que la grille et l\'accrochage. Il s\'agit principalement de dessiner les lignes directrices pour des objets Arch, mais sert également de «couteau suisse» de FreeCAD.

  Outil                                                                                                                           Description                                                                                         Outil                                                                                                                        Description
  ------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------
  <img alt="" src=images/Draft_Line.svg  style="width:32px;"> _                                   Trace une ligne composée de plusieurs segments de droites
  <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> _                                            Trace un segment d\'arc à partir du centre, rayon, angle de départ et angle d\'arrivée
  <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;">_                           Dessine un polygone régulier à partir du centre et du rayon du cercle circonscrit
  <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> _                                       Dessine une note en texte multiligne
  <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> _                            Dessine une courbe B-Spline à partir d\'une série de points
  <img alt="" src=images/Draft_Point.svg  style="width:32px;"> _   Insère une forme composée, qui représente une chaîne de texte
  <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> _                Dessine une courbe de Bezier à partir d\'une série de points
  <img alt="" src=images/Draft_Move.svg  style="width:32px;"> _                               Déplace l\'objet (ou les objets) par rotation autour d\'un point
  <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> _                               Découpe ou prolonge un objet
  <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> _                   Renvoie ou sépare des objets en objets de niveau inférieur
  <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> _          Génère une projection 2D à partir d\'un objet 3D
  <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> _         Crée un réseau rectangulaire de l\'objet sélectionné
  <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Clone](Draft_Clone/fr.md)                                       Crée un clone lié (dépendant) de l'objet sélectionné                                                                                                                                                                             
  <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Symétrie](Draft_Mirror/fr.md)                                 Copie d\'objets par symétrie par rapport à une droite                                                                                                                                                                            

### Atelier Sketcher (Esquisses) 

L'atelier Sketcher contient des outils pour créer et modifier des objets 2D complexes, appelés des esquisses. La géométrie à l\'intérieur de ces esquisses peut être positionnée avec précision et reliée par l\'utilisation de contraintes. Elles sont principalement destinées à être les éléments constitutifs de la géométrie PartDesign, mais sont utiles partout dans FreeCAD.

  Outil                                                                                                                                                              Description                                                                                                                                           Outil                                                                                                                                                              Description
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:32px;"> _                                                            dessine un segment de droite entre 2 points.
  <img alt="" src=images/Sketcher_Arc.svg  style="width:32px;"> _                        dessine un arc de cercle sur deux points et un troisième point pour la circonférence.
  <img alt="" src=images/Sketcher_Circle.svg  style="width:32px;"> _            dessine un cercle à partir de trois points.
  <img alt="" src=images/Sketcher_CreateEllipse.svg  style="width:32px;"> _     dessine une ellipse à partir du grand diametre (2 points) et d\'un point sur le petit rayon.
  <img alt="" src=images/Sketcher_CreateArcOfEllipse.png  style="width:32px;"> _                                  dessine une ligne composée de plusieurs segments connectés entre eux.
  <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> _                                   dessine un triangle équilatéral inscrit dans un cercle.
  <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> _                                  dessine un pentagone régulier inscrit dans un cercle.
  <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> _                                  dessine un heptagone régulier inscrit dans un cercle.
  <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width:32px;"> _                                                dessine une lumière oblongue en entrant le centre du demi-cercle, le point pour le rayon et le point final du deuxième demi-cercle.
  <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> _                                                      ajuste une ligne, un cercle ou un arc par rapport à l\'emplacement du clic.
  <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> _   bascule un élément vers/depuis le mode construction. Les éléments de construction (en bleu) sont ignorés lors d\'une opération de géométrie 3D et sont seulement visibles quand l'esquisse qui les contient est en mode édition.
  <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> _                  crée une contrainte d'appartenance (point-sur-objet) entre un sommet et un autre objet (ligne, arc, cercle, axe \...).
  <img alt="" src=images/Constraint_Vertical.svg  style="width:32px;"> _                                crée une contrainte d\'horizontalité sur la ou les lignes ou segments de polylignes sélectionnés.
  <img alt="" src=images/Constraint_Parallel.png  style="width:32px;"> _                  crée une contrainte de perpendicularité entre deux entités sélectionnées (droite/droite ou droite/extrémité d'arc).
  <img alt="" src=images/Constraint_Tangent.png  style="width:32px;"> _                                      crée une contrainte d\'égalité entre au moins deux éléments sélectionnés. Contraindra la longueur pour des lignes et le rayon pour des cercles et des arcs.
  <img alt="" src=images/Constraint_Symmetric.png  style="width:32px;"> _                                          crée une contrainte fixe sur le sommet sélectionné en ajoutant des dimensions horizontale et verticale relatives à l\'origine (les dimensions peuvent être éditées par la suite).
  <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:32px;"> _             fixe la distance verticale entre deux sommets ou extrémités de ligne. Si un seul élément est sélectionné, la distance sera relative à l\'origine.
  <img alt="" src=images/Constraint_Length.png  style="width:32px;"> _                                                 crée une contrainte radiale sur un arc ou un cercle sélectionné en ajoutant un rayon (cette dimension pourra être éditée par la suite).
  <img alt="" src=images/Constraint_InternalAngle.png  style="width:32px;"> _                                 contraint deux lignes à respecter une loi de réfraction simulant la trajectoire de la lumière à travers une interface.
  <img alt="" src=images/Constraint_InternalAlignment.png  style="width:32px;"> _                                    applique une esquisse sur une face ou un solide sélectionné.
  <img alt="" src=images/Sketcher_MergeSketch.svg  style="width:32px;"> _                                  crée une esquisse symétrique selon l\'axe X, l\'axe Y ou l\'origine.

### Atelier Part Design (Conception de pièces) 

L\'atelier Part Design (conception de pièces) contient des outils avancés pour créer des pièces solides. Il contient également tous les outils du sketcher. Comme il ne peut produire que des formes solides (la règle numéro 1 de Part Design), c\'est l\'atelier principal à utiliser lors de la conception de pièces (parts) à fabriquer ou imprimer en 3D, car vous obtiendrez toujours un objet imprimable.

  Outil                                                                                                                                                   Description                                                                                      Outil                                                                                                                                                        Description
  ------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> _                                                  Crée une poche (ou cavité) dans un solide existant, à partir de l'esquisse sélectionnée.
  <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> _                                        Enlève de la matière d\'un solide existant par révolution de l'esquisse sélectionnée autour d\'un axe (gorge ou rainure circulaire \...).
  <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> _                                           Applique un chanfrein sur une/plusieurs arêtes sélectionnées d\'un objet.
  <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> _                                         Copie une fonction par symétrie par rapport à un plan ou une face (plane).
  <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> _                   Crée une répétition polaire d'une fonction.
  <img alt="" src=images/PartDesign_Scaled.png  style="width:32px;"> _        Crée une transformation multiple d'une fonction.
  <img alt="" src=images/PartDesign_WizardShaft.svg  style="width:32px;"> _   Permet de créer différents types d'engrenages.

### Atelier Arch (Architecture) 

L\'atelier Architecture (ou « Arch » pour faire court) fournit à FreeCAD les outils pour travailler avec les projets [BIM](https://en.wikipedia.org/wiki/Building_information_modeling) (Génie civil et architecture). Il dispose également de tous les outils de l\'atelier Draft. La principale utilisation de l\'atelier Arch est de créer des objets BIM ou de donner des attributs BIM à des objets créés avec d\'autres ateliers, de façon à pouvoir les exporter au format [IFC](https://en.wikipedia.org/wiki/Industry_Foundation_Classes).

  Outil                                                                                                     Description                                                                Outil                                                                                                                 Description
  --------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------
  <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> _       Crée un élément structurel à partir de zéro ou à partir d\'un objet sélectionné.
  <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> _                                Crée un étage incluant les objets sélectionnés.
  <img alt="" src=images/Arch_Building.svg  style="width:32px;"> _                                    Crée un site incluant les objets sélectionnés.
  <img alt="" src=images/Arch_Window.svg  style="width:32px;"> _   Ajoute un plan de coupe au document.
  <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> _                                 Crée un toit en pente à partir d\'une face sélectionnée.
  <img alt="" src=images/Arch_Space.png  style="width:32px;"> _                         Crée un objet escalier dans le document.
  <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> _                             Crée une ossature à partir d\'un objet 2D plan et d\'un profil.
  <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> _           Attribue un matériau à l\'objet sélectionné.
  <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> _                       Coupe un objet selon un plan défini.
  <img alt="" src=images/Arch_Add.svg  style="width:32px;"> _                           Retirer ou effacer un objet d\'un composant.
  <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Infos](Arch_Survey/fr.md)                 Active ou quitte le mode Informations.                                                                                                                                                           

### Atelier Drawing (Mise en plan) 


**Le développement de [atelier Drawing](Drawing_Workbench/fr.md) s'est arrêté dans FreeCAD 0.16, et le nouveau [atelier TechDraw](TechDraw_Workbench/fr.md) visant à le remplacer a été introduit en v0.17. Le plan de travail de dessin peut être supprimé dans les versions ultérieures. Utilisez plutôt l'atelier TechDraw.**

L\'atelier Drawing (mise en plan) vous permet de coucher sur papier votre projet 3D, en réalisant des projections 2D de votre modèle 3D et en insérant ces projections dans une feuille (page) de mise en plan. Celle-ci pourra avoir une bordure, un titre et un logo, et cette page pourra ensuite être imprimée et/ou exportée vers des applications 2D au format SVG ou DXF, ou vers un fichier PDF.

  Outil                                                                                                                                       Description                                                                                  Outil                                                                                                                        Description
  ------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------
  <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> _                       Insère une vue de l\'objet sélectionné dans la feuille active.
  <img alt="" src=images/Drawing_Annotation.png  style="width:32px;"> _                                  Ajoute un groupe de clips dans la feuille de dessin courante.
  <img alt="" src=images/Drawing_Openbrowser.png  style="width:32px;"> _   Crée automatiquement des vues orthogonales d\'un objet sur la feuille de dessin.
  <img alt="" src=images/Drawing_Symbol.png  style="width:32px;"> _                      Insère une vue de détail de l\'objet sélectionné dans la feuille de dessin en cours.
  <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Sauvegarder](Drawing_Save/fr.md)                                          Exporte la feuille de dessin dans un fichier au format SVG.                                                                                                                                                               

### Autres ateliers de travail intégrés 

Bien que ce qui précède résume les outils les plus importants de FreeCAD, beaucoup d\'autres ateliers sont disponibles, parmi lesquels :

-   L'[atelier Mesh (maillage)](Mesh_Workbench/fr.md) permet de travailler avec des maillages polygonaux ([polygon meshes](https://en.wikipedia.org/wiki/Polygon_mesh)). Bien que les maillages ne soient pas le type préféré de géométrie à utiliser dans FreeCAD, en raison de leur manque de précision et de support pour les courbes, les mailles ont encore beaucoup d\'usages et sont entièrement prises en charge dans FreeCAD. L'atelier Maillage offre également un certain nombre d\'outils Part-vers-Mesh et Mesh-vers-Part.
-   L'[atelier Raytracing (rendu réaliste)](Raytracing_Workbench/fr.md) offre des outils pour l\'interface avec des programmes externes tels que povray ou luxrender. Depuis FreeCAD, cet espace de travail vous permet de produire des rendus de haute qualité à partir de vos modèles.
-   L'atelier [Spreadsheet (feuille de calcul)](Spreadsheet_Workbench/fr.md) permet la création et la manipulation de données de tableur, qui peuvent être extraites des modèles FreeCAD. Les cellules de feuille de calcul peuvent également être référencées dans de nombreux domaines de FreeCAD, ce qui permet de les utiliser comme structures de données de base.
-   L'atelier [FEM](FEM_Workbench/fr.md) traite de l\'analyse par éléments finis ([Finite Elements Analysis](https://en.wikipedia.org/wiki/Finite_element_method)) et permet d\'effectuer des calculs de résistance pré et post-traitement et d\'afficher les résultats graphiquement.

### Ateliers externes 

Un certain nombre d\'autres ateliers très utiles produits par les membres de la communauté FreeCAD existent également. Bien qu\'ils ne soient pas inclus dans une installation standard de FreeCAD, ils sont faciles à installer en tant que plug-ins. Ils sont tous référencés dans le dépôt [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons). Parmi les plus développés se trouvent les suivants :

-   L'atelier [Drawing Dimensioning (dimensionnement de dessin)](https://github.com/hamish2014/FreeCAD_drawing_dimensioning) offre de nombreux nouveaux outils pour travailler directement sur les feuilles de dessin et vous permet d\'ajouter des dimensions, des annotations et d\'autres symboles techniques avec un grand contrôle sur leur aspect.**L\'addon Drawing Dimensioning n\'est plus géré.**
-   L'atelier [Fasteners (Fixations)](https://github.com/shaise/FreeCAD_FastenersWB) offre une large gamme d\'éléments de fixation prêts à insérer comme des vis, des boulons, des tiges, des rondelles et des écrous. De nombreuses options et paramètres sont disponibles.
-   L\'atelier [A2plus](https://github.com/kbwbe/A2plus) offre une série d\'outils pour réaliser et travailler avec des [assemblages](https://en.wikipedia.org/wiki/Assembly_modelling).

**Lire plus d\'informations**

-   [Liste complète des ateliers](Workbenches/fr.md)
-   [Atelier Part](Part_Workbench/fr.md)
-   [Atelier Draft](Draft_Workbench/fr.md)
-   [Atelier Part Design](PartDesign_Workbench/fr.md)
-   [Atelier Arch](Arch_Workbench/fr.md)
-   [Atelier TechDraw](TechDraw_Workbench/fr.md)
-   [Atelier FEM](FEM_Workbench/fr.md)
-   [Le dépôt des greffons pour FreeCAD](https://github.com/FreeCAD/FreeCAD-addons)

---
[documentation index](../README.md) > Manual:All workbenches at a glance/fr
