# BIM Workbench/fr
**Dans la version 1.0, les ateliers BIM, Native-IFC et [Arch](Arch_Workbench/fr.md) ont été fusionnés dans l'atelier BIM.<br>
Cette page a été mise à jour pour cette version.**

<img alt="Icône de l\'atelier externe BIM" src=images/Workbench_BIM.svg  style="width:128px;">




## Introduction

L\'<img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [atelier BIM](BIM_Workbench/fr.md) fournit un flux de travail moderne [BIM](https://fr.wikipedia.org/wiki/Building_information_modeling) dans FreeCAD, avec des objets entièrement paramétriques tels que les murs, les poutres, les toits, les fenêtres, les escaliers, les tuyaux et le mobilier. Il prend en charge les fichiers [Industry Foundation Classes](Arch_IFC/fr.md) (IFC) et la production de plans 2D en combinaison avec l\'<img alt="" src=images/Workbench_TechDraw.svg  style="width:16px;"> [atelier TechDraw](TechDraw_Workbench/fr.md).

L\'atelier BIM importe tous les outils de l\'<img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> [atelier Draft](Draft_Workbench/fr.md) car il utilise ses objets 2D pour créer des objets architecturaux paramétriques 3D. Néanmoins, il peut également utiliser des formes solides créées avec d\'autres ateliers tels que <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/fr.md) et <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/fr.md).

Voir le [guide de migration BIM de FreeCAD](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide) pour un aperçu rapide si vous êtes déjà utilisateur d\'une autre application BIM.

Les développeurs de Draft et BIM collaborent également avec la [communauté OSArch](https://osarch.org) dans le but ultime d\'améliorer la conception des bâtiments en utilisant un logiciel entièrement gratuit.

<img alt="" src=images/BIM_workbench_presentation.png  style="width:800px;">



## Commencer

<img alt="" src=images/BIM_welcome_screen.png  style="width:800px;">

Lorsque vous démarrez l\'atelier BIM pour la première fois, une fenêtre de dialogue de bienvenue s\'affiche, donnant un aperçu rapide du fonctionnement de l\'atelier et permettant à l\'utilisateur de démarrer un [tutoriel ludique](BIM_ingame_tutorial/fr.md). Le dialogue de bienvenue est également disponible dans le menu **aide**. Lorsque vous fermez l\'écran de bienvenue en cliquant sur OK, la [Fenêtre de dialogue configuration BIM](BIM_Setup/fr.md) s\'affiche. Elle permet à l\'utilisateur de définir rapidement certaines des préférences les plus courantes liées à BIM de FreeCAD sans qu\'il soit nécessaire de parcourir les pages complètes des [paramètres de préférences FreeCAD.](Preferences_Editor/fr.md).

L\'outil [Configuration](BIM_Setup/fr.md) vous permet de configurer rapidement un projet BIM en renseignant certaines informations de base sur votre projet. Vous pouvez ensuite, par exemple, utiliser les différents outils de dessin 2D pour dessiner des repères et des lignes de base, Puis utiliser les différents outils de modélisation 3D pour créer automatiquement des objets BIM 3D à partir d\'eux. Une ligne, par exemple, peut devenir un mur simplement en la sélectionnant et en appuyant sur le bouton [Mur](Arch_Wall/fr.md).

Les éléments communs de construction tels que les [murs](Arch_Wall/fr.md) ou les [colonnes](BIM_Column/fr.md) sont facilement créés en appuyant sur le bouton approprié de la barre d\'outils et en cliquant sur des points dans la vue 3D. Une fois créés, ils peuvent être déplacés, pivotés et modifiés. La plupart des éléments de BIM sont créés sur le [plan de travail](Draft_SelectPlane/fr.md) en cours, de sorte qu\'un flux de travail typique consiste à placer d\'abord le plan de travail, puis à créer un élément de BIM. Des éléments plus complexes peuvent être créés en dessinant d\'abord des éléments 2D, puis en utilisant l\'un des outils de BIM pour les convertir en l\'élément souhaité.

Les éléments des projets de construction peuvent être organisés en utilisant des [sites](Arch_Site/fr.md), [bâtiments](Arch_Building/fr.md) et des [niveaux](Arch_BuildingPart/fr.md), pour reproduire ce qui est communément fait dans d\'autres applications BIM. Dans FreeCAD, cependant, de telles structures ne sont pas obligatoires, et vous êtes libre d\'organiser les éléments de votre modèle comme vous l\'entendez, par exemple en utilisant des [groupes](Std_Group/fr.md).

Des dessins 2D peuvent être générés à partir d\'un modèle pour représenter des vues en plan, en coupe ou en élévation. Pour générer un tel dessin, des [plans de coupe](Arch_SectionPlane/fr.md) sont placés dans le modèle pour indiquer l\'endroit où il doit être coupé ou vu. Une fois les plans de coupe en place, deux méthodes sont possibles :

1.  Créer des vues projetées dans le document en utilisant des [vues 2D d\'une forme](Draft_Shape2DView/fr.md) puis ajouter toutes les annotations nécessaires telles que les textes et les dimensions, et enfin mettre le tout sur une page. C\'est la méthode recommandée, car elle offre plus de souplesse.
2.  Créer une vue sur une page directement à partir du plan de coupe. Ensuite, toutes les annotations 2D nécessaires doivent être soit ajoutées au plan de coupe, soit effectuées directement sur la page. Cette méthode est moins souple.

Enfin, les nomenclatures des quantités peuvent être créés à l\'aide de l\'outil [Nomenclature](Arch_Schedule/fr.md).

Si vous êtes habitué à une autre application BIM, consultez notre [Tableau de compatibilité des applications BIM](BIM_application_compatibility_table/fr.md) pour connaître vos marques lors du démarrage avec FreeCAD.

<img alt="" src=images/BIM_tutorial_screenshot.png  style="width:800px;">

Le [BIM Tutoriel](BIM_ingame_tutorial/fr.md) est un moyen facile de se mettre rapidement sur la bonne voie avec l\'atelier BIM.



## Outils

L\'atelier BIM rassemble des outils provenant de plusieurs autres ateliers FreeCAD, principalement [Draft](Draft_Workbench/fr.md) et [Part](Part_Workbench/fr.md), grossièrement réorganisés en catégories logiques.

De plus, si de telles [extensions](External_workbenches/fr.md) sont installées, des outils de [Reinforcement](Reinforcement_Workbench/fr.md) (armatures supplémentaires), [Fasteners](Fasteners_Workbench/fr.md) (boulons et vis), [Flamingo/Dodo](Flamingo_Workbench/fr.md) (outils de structure métallique et de tuyauterie) et [Parts Library](Parts_Library_Workbench/fr.md) sont automatiquement inclus dans l\'atelier BIM.

L\'atelier BIM ajoute également une série d\'éléments dans la **barre d\'état** de FreeCAD et quelques **éléments de menu contextuel**, accessibles en cliquant avec le bouton droit de la souris dans la vue 3D ou dans l\'arborescence.



### Dessin 2D 

Les objets 2D sont couramment utilisés comme aide à la conception ou pour tracer des lignes de base et des profils sur lesquels construire des objets BIM. Ils peuvent également être utilisés pour dessiner des symboles et des annotations dans votre modèle. En plus des esquisses, qui utilisent leur propre système de coordonnées, des objets 2D seront dessinés sur le [plan de travail](Draft_SelectPlane/fr.md) sélectionné.

-   <img alt="" src=images/BIM_Sketch.svg  style="width:32px;"> [Esquisse](BIM_Sketch/fr.md) : crée une nouvelle esquisse et passe en mode édition d\'esquisse. Les esquisses sont des objets 2D avancés avec prise en charge des contraintes.

-   <img alt="" src=images/Draft_Line.svg  style="width:32px;"> [Ligne](Draft_Line/fr.md) : crée une ligne droite.

-   <img alt="" src=images/Draft_Wire.svg  style="width:32px;"> [Polyligne](Draft_Wire/fr.md) : crée une polyligne (appelée aussi filaire), une séquence de plusieurs segments de ligne connectés.

-   <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> [Cercle](Draft_Circle/fr.md) : crée un cercle à partir d\'un centre et d\'un rayon.

  - <img alt="" src=images/Draft_Arc.svg  style="width:32px;"> [Arc](Draft_Arc/fr.md) : crée un arc de cercle à partir d\'un centre, d\'un rayon, d\'un angle de départ et d\'un angle d\'ouverture.

  - <img alt="" src=images/Draft_Arc_3Points.svg  style="width:32px;"> [Arc par 3 points](Draft_Arc_3Points/fr.md) : crée un arc de cercle à partir de trois points qui définissent sa circonférence.

-   <img alt="" src=images/Draft_Fillet.svg  style="width:32px;"> [Congé](Draft_Fillet/fr.md) : crée un congé, un coin arrondi, ou un chanfrein, un bord droit, entre deux [Draft Lignes](Draft_Line/fr.md).

-   <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;"> [Ellipse](Draft_Ellipse/fr.md) : crée une ellipse à partir de deux points définissant un rectangle dans lequel l\'ellipse s\'inscrira.

-   <img alt="" src=images/Draft_Polygon.svg  style="width:32px;"> [Polygone](Draft_Polygon/fr.md) : crée un polygone régulier à partir d\'un centre et d\'un rayon.

-   <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> [Rectangle](Draft_Rectangle/fr.md) : crée un rectangle à partir de deux points.

-   <img alt="" src=images/Draft_BSpline.svg  style="width:32px;"> [B-spline](Draft_BSpline/fr.md) : crée une courbe B-spline à partir de plusieurs points.

  - <img alt="" src=images/Draft_BezCurve.svg  style="width:32px;"> [Courbe de Bézier](Draft_BezCurve/fr.md) : crée une courbe de Bézier à partir de plusieurs points.

  - <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:32px;"> [Courbe de Bézier cubique](Draft_CubicBezCurve/fr.md) : crée une courbe de Bézier du troisième degré.

-   <img alt="" src=images/Draft_Point.svg  style="width:32px;"> [Point](Draft_Point/fr.md) : crée un simple point.

### 3D/BIM

Les objets 3D et BIM sont les éléments du monde réel qui composeront votre projet BIM.

-   <img alt="" src=images/BIM_Project.svg  style="width:32px;"> [Projet](BIM_Project/fr.md) : crée un projet IFC incluant les objets sélectionnés.

-   <img alt="" src=images/Arch_Site.svg  style="width:32px;"> [Site](Arch_Site/fr.md) : crée un site incluant les objets sélectionnés.

-   <img alt="" src=images/Arch_Building.svg  style="width:32px;"> [Bâtiment](Arch_Building/fr.md) : crée un bâtiment incluant les objets sélectionnés.

-   <img alt="" src=images/Arch_Floor.svg  style="width:32px;"> [Niveau](Arch_Floor/fr.md) : crée un niveau incluant les objets sélectionnés.

-   <img alt="" src=images/Arch_Space.svg  style="width:32px;"> [Espace](Arch_Space/fr.md) : crée un objet volume vide.

-   <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> [Mur](Arch_Wall/fr.md) : crée un mur à partir de rien ou en utilisant un objet sélectionné comme base.

-   <img alt="" src=images/Arch_CurtainWall.svg  style="width:32px;"> [Mur-rideau](Arch_CurtainWall/fr.md) : crée un mur-rideau à partir de rien ou en utilisant un objet sélectionné comme base.

-   <img alt="" src=images/BIM_Column.svg  style="width:32px;"> [Colonne](BIM_Column/fr.md) : crée un élément vertical [structurel](Arch_Structure/fr.md) à un point donné, en utilisant éventuellement un objet sélectionné comme profil.

-   <img alt="" src=images/BIM_Beam.svg  style="width:32px;"> [Poutre](BIM_Beam/fr.md) : crée un élément [structurel](Arch_Structure/fr.md) horizontal entre deux points, en utilisant éventuellement un objet sélectionné comme profil.

-   <img alt="" src=images/BIM_Slab.svg  style="width:32px;"> [Dalle](BIM_Slab/fr.md) : crée un élément plat [structural](Arch_Structure/fr.md) en extrudant un objet plat sélectionné.

-   <img alt="" src=images/BIM_Door.svg  style="width:32px;"> [Porte](BIM_Door/fr.md) : crée un objet [Fenêtre](Arch_Window/fr.md) en utilisant les préréglages de porte.

-   <img alt="" src=images/Arch_Window.svg  style="width:32px;"> [Fenêtre](Arch_Window/fr.md) : crée une fenêtre à partir de rien ou en utilisant un objet sélectionné comme base.

-   <img alt="" src=images/Arch_Pipe.svg  style="width:32px;"> [Conduite](Arch_Pipe/fr.md) : crée une conduite.

-   <img alt="" src=images/Arch_PipeConnector.svg  style="width:32px;"> [Raccord](Arch_PipeConnector/fr.md) : crée un angle ou une connexion en T entre 2 ou 3 conduites sélectionnées.

-   <img alt="" src=images/Arch_Stairs.svg  style="width:32px;"> [Escalier](Arch_Stairs/fr.md) : crée un objet escalier.

-   <img alt="" src=images/Arch_Roof.svg  style="width:32px;"> [Toit](Arch_Roof/fr.md) : crée un toit incliné à partir d\'une polyligne sélectionnée.

-   <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Panneau](Arch_Panel/fr.md) : crée un objet panneau à partir d\'un objet 2D sélectionné.

-   <img alt="" src=images/Arch_Frame.svg  style="width:32px;"> [Ossature](Arch_Frame/fr.md) : crée un objet ossature à partir d\'une mise en page sélectionnée.

-   <img alt="" src=images/Arch_Fence.svg  style="width:32px;"> [Clôture](Arch_Fence/fr.md) : crée un objet clôture à partir d\'un poteau et d\'un chemin sélectionnés.

-   <img alt="" src=images/Arch_Truss.svg  style="width:32px;"> [Treillis](Arch_Truss/fr.md) : crée un treillis à partir d\'une ligne sélectionnée ou de zéro.

-   <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> [Équipement](Arch_Equipment/fr.md) : crée un objet d\'équipement ou de mobilier.

-   Outils d\'armatures :

:   Ces outils, à l\'exception du premier, ne sont disponibles que si le [atelier Reinforcement](Reinforcement_Workbench/fr.md) a été installé.

  -<img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Armature personnalisée](Arch_Rebar/fr.md) : crée une armature personnalisée dans un élément de structure sélectionné à l\'aide d\'une esquisse.

  - <img alt="" src=images/Reinforcement_StraightRebar.svg  style="width:32px;"> [Armature droite](Reinforcement_StraightRebar/fr.md) : crée une armature droite dans un élément de structure sélectionné.

  - <img alt="" src=images/Reinforcement_UShapeRebar.svg  style="width:32px;"> [Armature en U](Reinforcement_UShapeRebar/fr.md) : crée une armature en U dans un élément de structure sélectionné.

  - <img alt="" src=images/Reinforcement_LShapeRebar.svg  style="width:32px;"> [Armature en L](Reinforcement_LShapeRebar/fr.md) : crée une armature en L dans un élément de structure sélectionné.

  - <img alt="" src=images/Reinforcement_StirrupRebar.svg  style="width:32px;"> [Armature en étrier](Reinforcement_StirrupRebar/fr.md) : crée une armature étrier dans un élément de structure sélectionné.

  - <img alt="" src=images/Reinforcement_BentShapeRebar.svg  style="width:32px;"> [Armature cintrée](Reinforcement_BentShapeRebar/fr.md) : crée une armature de forme cintrée dans un élément de structure sélectionné.

  - <img alt="" src=images/Reinforcement_HelicalRebar.svg  style="width:32px;"> [Armature hélicoïdale](Reinforcement_HelicalRebar/fr.md) : crée une armature hélicoïdale dans un élément de structure sélectionné.

  - <img alt="" src=images/Reinforcement_ColumnRebars.svg  style="width:32px;"> [Armature pour colonne](Reinforcement_ColumnRebars/fr.md) : crée des armatures dans une colonne sélectionnée.

  - <img alt="" src=images/Reinforcement_BeamRebars.svg  style="width:32px;"> [Poutre](Reinforcement_BeamRebars/fr.md) : crée des armatures dans une poutre sélectionnée.

  - <img alt="" src=images/Reinforcement_SlabRebars.svg  style="width:32px;"> [Renfort de dalle](Reinforcement_SlabRebars/fr.md) : crée des armatures dans une dalle sélectionnée.

  - <img alt="" src=images/Reinforcement_FootingRebars.svg  style="width:32px;"> [Renfort de semelle](Reinforcement_FootingRebars/fr.md): crée des armatures dans une semelle sélectionnée.

-   Outils 3D génériques :

:   Ces outils permettent de créer des objets 3D génériques qui peuvent être transformés ou utilisés dans des composants BIM.

  - <img alt="" src=images/Arch_Profile.svg  style="width:32px;"> [Profilé](Arch_Profile/fr.md) : crée un profilé 2D paramétrique.

  - <img alt="" src=images/BIM_Box.svg  style="width:32px;"> [Boîte](BIM_Box/fr.md) : crée une boîte en spécifiant ses dimensions graphiquement.

  - <img alt="" src=images/Part_Builder.svg  style="width:32px;"> [Générateur de formes\...](Part_Builder/fr.md) : crée des formes plus complexes à partir de diverses primitives.

  - <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> [Surface liée](Draft_Facebinder/fr.md) : crée un objet surface à partir des faces sélectionnées.

  - <img alt="" src=images/BIM_Library.svg  style="width:32px;"> [Bibliothèque d\'objets](BIM_Library/fr.md) : insère un objet d\'équipement ou de mobilier. Nécessite l\'extension [Parts Library](Parts_Library/fr.md).

  - <img alt="" src=images/Arch_Component.svg  style="width:32px;"> [Composant](Arch_Component/fr.md) : crée un composant Arch non-paramétrique.

  - <img alt="" src=images/Arch_Reference.svg  style="width:32px;"> [Référence externe](Arch_Reference/fr.md) : lie les objets d\'un autre fichier FreeCAD dans le document en cours.

### Annotation

Les annotations sont des objets d\'aide visuels pouvant être placés dans votre modèle. Ils peuvent être utilisés pour exporter votre modèle directement vers un format 2D tel que [DXF](Draft_DXF/fr.md), ou être réutilisés lors de la création de vues 2D de votre modèle avec l\'[atelier TechDraw](TechDraw_Workbench/fr.md).

-   <img alt="" src=images/BIM_Text.svg  style="width:32px;"> [Texte](BIM_Text/fr.md) : crée un texte 2D dans un document ou sur une page TechDraw.

-   <img alt="" src=images/Draft_ShapeString.svg  style="width:32px;"> [Forme à partir d\'un texte](Draft_ShapeString/fr.md) : crée une forme composée qui représente une chaîne de texte.

-   <img alt="" src=images/BIM_DimensionAligned.svg  style="width:32px;"> [Dimension alignée](BIM_DimensionAligned/fr.md) : crée une dimension alignée avec deux points ou une arête sélectionnée.

-   <img alt="" src=images/BIM_DimensionHorizontal.svg  style="width:32px;"> [Dimension horizontale](BIM_DimensionHorizontal/fr.md) : crée une dimension horizontale entre deux points ou à partir d\'un arête sélectionnée.

-   <img alt="" src=images/BIM_DimensionVertical.svg  style="width:32px;"> [Dimension verticale](BIM_DimensionVertical/fr.md) : crée une dimension verticale entre deux points ou à partir d\'une arête sélectionnée.

-   <img alt="" src=images/BIM_Leader.svg  style="width:32px;"> [Ligne de référence](BIM_Leader/fr.md) : crée une polyligne à 2 segments avec une flèche à son extrémité, à utiliser comme ligne de référence avec un [texte](BIM_Text/fr.md).

-   <img alt="" src=images/Draft_Label.svg  style="width:32px;"> [Étiquette](Draft_Label/fr.md) : crée un texte de plusieurs lignes avec une ligne de tête à deux segments et une flèche.

-   <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> [Axes](Arch_Axis/fr.md) : ajoute un réseau d\'axes à 1 direction.

-   <img alt="" src=images/Arch_AxisSystem.svg  style="width:32px;"> [Système d\'axes](Arch_AxisSystem/fr.md) : ajoute un système d\'axes composé de plusieurs axes.

-   <img alt="" src=images/Arch_Grid.svg  style="width:32px;"> [Grille](Arch_Grid/fr.md) : ajoute un objet de type grille.

-   <img alt="" src=images/Arch_SectionPlane.svg  style="width:32px;"> [Plan de coupe](Arch_SectionPlane/fr.md) : ajoute un objet plan de coupe.

-   <img alt="" src=images/Draft_Hatch.svg  style="width:32px;"> [Hachures](Draft_Hatch/fr.md) : crée des hachures sur les faces d\'un objet sélectionné.

-   <img alt="" src=images/BIM_TDPage.svg  style="width:32px;"> [Page](BIM_TDPage/fr.md) : crée une [page de TechDraw](TechDraw_PageTemplate/fr.md) à partir d\'un fichier SVG modèle.

-   <img alt="" src=images/BIM_TDView.svg  style="width:32px;"> [Vue](BIM_TDView/fr.md) : crée une vue de/des objet(s) sélectionnés, tel qu\'un [plan de coupe](Arch_SectionPlane/fr.md) ou un groupe contenant les différents éléments d\'une vue 2D.

-   <img alt="" src=images/BIM_Shape2DView.svg  style="width:32px;"> [Projection 2D](BIM_Shape2DView/fr.md) : crée une vue projetée en 2D à partir d\'un objet sélectionné tel qu\'un [plan de coupe](Arch_SectionPlane/fr.md) ou un [niveau](Arch_BuildingPart/fr.md).



### Aimantation

Ce menu contient les outils [Draft Aimantation](Draft_Snap/fr.md) ainsi que les outils suivants :

-   <img alt="" src=images/BIM_SetWPTop.svg  style="width:32px;"> [Plan de travail en haut](BIM_SetWPTop/fr.md) : place le plan de travail sur le plan global XY (sol).

-   <img alt="" src=images/BIM_SetWPFront.svg  style="width:32px;"> [Plan de travail de devant](BIM_SetWPFront/fr.md) : place le plan de travail sur le plan global XZ (avant).

-   <img alt="" src=images/BIM_SetWPSide.svg  style="width:32px;"> [Plan de travail de côté](BIM_SetWPSide/fr.md) : place le plan de travail sur le plan global YZ (coté).



### Modification

-   <img alt="" src=images/Draft_Move.svg  style="width:32px;"> [Déplacer](Draft_Move/fr.md) : déplace ou copie les objets sélectionnés d\'un point à un autre.

-   <img alt="" src=images/BIM_Copy.svg  style="width:32px;"> [Copier](BIM_Copy/fr.md) : copie les objets sélectionnés d\'un point à un autre.

-   <img alt="" src=images/Draft_Rotate.svg  style="width:32px;"> [Pivoter](Draft_Rotate/fr.md) : fait pivoter ou copie les objets sélectionnés autour d\'un point central selon un angle donné.

-   <img alt="" src=images/BIM_Clone.svg  style="width:32px;"> [Cloner](BIM_Clone/fr.md) : clone les objets sélectionnés.

-   <img alt="" src=images/BIM_SimpleCopy.svg  style="width:32px;"> [Copie simple](BIM_SimpleCopy/fr.md) : crée une copie non paramétrique d\'un objet sélectionné. Il s\'agit du même outil que [Part Copie simple](Part_SimpleCopy/fr.md).

-   <img alt="" src=images/BIM_Compound.svg  style="width:32px;"> [Composé](BIM_Compound/fr.md) : crée un composé à partir des objets sélectionnés. Il s\'agit du même outil que [Part Composé](Part_Compound/fr.md).

-   <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> [Décaler](Draft_Offset/fr.md) : décale chaque segment d\'un objet sélectionné sur une distance donnée ou crée une copie décalée de l\'objet sélectionné.

-   <img alt="" src=images/BIM_Offset2D.svg  style="width:32px;"> [Décaler en 2D](BIM_Offset2D/fr.md) : construit une polyligne parallèle à une distance donnée de l\'originale, ou agrandit/réduit une face plane (version paramétrique). Il s\'agit du même outil que [Part Décaler en 2D](Part_Offset2D/fr.md).

-   <img alt="" src=images/Draft_Trimex.svg  style="width:32px;"> [Ajuster ou prolonger](Draft_Trimex/fr.md) : ajuste ou étend un objet sélectionné.

-   <img alt="" src=images/Draft_Join.svg  style="width:32px;"> [Joindre](Draft_Join/fr.md) : joint des [Draft Lignes](Draft_Line/fr.md) et des [Draft Polylignes](Draft_Wire/fr.md) en une seule polyligne.

-   <img alt="" src=images/Draft_Split.svg  style="width:32px;"> [Scinder](Draft_Split/fr.md) : divise une [Draft Ligne](Draft_Line/fr.md) ou une [Draft Polyligne](Draft_Wire/fr.md) à un point ou une arête spécifique.

-   <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> [Échelle](Draft_Scale/fr.md) : met à l\'échelle ou copie les objets sélectionnés autour d\'un point de base.

-   <img alt="" src=images/Draft_Stretch.svg  style="width:32px;"> [Étirer](Draft_Stretch/fr.md) : étire les objets en déplaçant les points sélectionnés.

-   <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> [Draft \<=\> esquisse](Draft_Draft2Sketch/fr.md) : convertit les objets Draft en [Sketcher Esquisses](Sketcher_NewSketch/fr.md) et vice versa.

-   <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> [Agréger](Draft_Upgrade/fr.md) : agrège les objets sélectionnés.

-   <img alt="" src=images/Draft_Downgrade.svg  style="width:32px;"> [Désagréger](Draft_Downgrade/fr.md) : déclasse les objets sélectionnés.

-   <img alt="" src=images/Arch_Add.svg  style="width:32px;"> [Ajouter](Arch_Add/fr.md) : ajoute des objets à un composant.

-   <img alt="" src=images/Arch_Remove.svg  style="width:32px;"> [Supprimer](Arch_Remove/fr.md) : soustrait ou supprime des objets d\'un composant.

-   <img alt="" src=images/Draft_OrthoArray.svg  style="width:32px;"> [Réseau orthogonal](Draft_OrthoArray/fr.md) : crée un réseau orthogonal à partir d\'un objet sélectionné. Cela peut éventuellement créer un réseau de [liens](App_Link/fr.md).

-   <img alt="" src=images/Draft_PathArray.svg  style="width:32px;"> [Réseau selon une courbe](Draft_PathArray/fr.md) : crée un réseau à partir d\'un objet sélectionné en plaçant des copies le long d\'un tracé.

-   <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> [Réseau polaire](Draft_PolarArray/fr.md) : crée un réseau à partir d\'un objet sélectionné en plaçant des copies sur une circonférence. L\'outil peut créer un réseau de [liens](App_Link/fr.md).

-   <img alt="" src=images/Draft_PointArray.svg  style="width:32px;"> [Réseau de points](Draft_PointArray/fr.md) : crée un réseau à partir d\'un objet sélectionné en plaçant des copies aux points d\'un composé de points.

-   <img alt="" src=images/Arch_CutPlane.svg  style="width:32px;"> [Couper suivant un plan](Arch_CutPlane/fr.md) : découpe un objet en fonction d\'un plan.

-   <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Miroir](Draft_Mirror/fr.md) : crée des copies miroir à partir des objets sélectionnés.

-   <img alt="" src=images/BIM_Extrude.svg  style="width:32px;"> [Extrusion](BIM_Extrude/fr.md) : extrude les faces planes d\'un objet. Il s\'agit du même outil que [Part Extrusion](Part_Extrude/fr.md).

-   <img alt="" src=images/BIM_Cut.svg  style="width:32px;"> [Soustraction](BIM_Cut/fr.md) : soustrait un objet d\'un autre. Il s\'agit du même outil que [Part Soustraction](Part_Cut/fr.md).

-   <img alt="" src=images/BIM_Fuse.svg  style="width:32px;"> [Union](BIM_Fuse/fr.md) : fusionne deux objets. Il s\'agit du même outil que [Part Union](Part_Fuse/fr.md).

-   <img alt="" src=images/BIM_Common.svg  style="width:32px;"> [Intersection](BIM_Common/fr.md) : extrait la partie commune de deux objets. Il s\'agit du même outil que [Part Intersection](Part_Common/fr.md).



### Gestion

-   <img alt="" src=images/BIM_Setup.svg  style="width:32px;"> [Configuration des BIM](BIM_Setup/fr.md) : configure certaines des préférences de FreeCAD les plus couramment utilisées pour les BIM.

-   <img alt="" src=images/BIM_Views.svg  style="width:32px;"> [Gérer les vues BIM](BIM_Views/fr.md) : gérer les différentes vues et niveaux de votre projet.

-   <img alt="" src=images/BIM_ProjectManager.svg  style="width:32px;"> [Projet](BIM_ProjectManager/fr.md) : permet de créer des objets de base tels qu\'un [site](Arch_Site/fr.md), un [bâtiment](Arch_Building/fr.md) et des [axes](Arch_Axis/fr.md) en remplissant les informations de base du projet.

-   <img alt="" src=images/BIM_Windows.svg  style="width:32px;"> [Fenêtres et portes](BIM_Windows/fr.md) : gérer les portes et fenêtres de votre projet.

-   <img alt="" src=images/BIM_IfcElements.svg  style="width:32px;"> [Éléments IFC](BIM_IfcElements/fr.md) : gérer la façon dont les différents éléments de votre projet seront exportés en IFC.

-   <img alt="" src=images/BIM_IfcQuantities.svg  style="width:32px;"> [Quantités IFC](BIM_IfcQuantities/fr.md) : gérer la façon dont les quantités de vos objets sont explicitement exportées en IFC.

-   <img alt="" src=images/BIM_IfcProperties.svg  style="width:32px;"> [Propriétés IFC](BIM_IfcProperties/fr.md) : gérer les propriétés IFC attachées à chacun de vos objets.

-   <img alt="" src=images/BIM_Classification.svg  style="width:32px;"> [Classification](BIM_Classification/fr.md) : gérer la façon dont les objets et les matériaux de votre projet sont liés à des systèmes de classification tels que [Uniclass](https://en.wikipedia.org/wiki/Uniclass).

-   <img alt="" src=images/BIM_Layers.svg  style="width:32px;"> [Calques](BIM_Layers/fr.md) : gérer les calques de votre document.

-   <img alt="" src=images/BIM_Material.svg  style="width:32px;"> [Matériau](BIM_Material/fr.md) : gère les [matériaux](Arch_SetMaterial/fr.md) ou les [multi-matériaux](Arch_MultiMaterial/fr.md) des objets sélectionnés.

-   <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> [Nomenclature](Arch_Schedule/fr.md) : crée différents types de nomenclatures.

-   <img alt="" src=images/BIM_Preflight.svg  style="width:32px;"> [Contrôle en amont](BIM_Preflight/fr.md) : effectuer différents contrôles sur votre modèle avant de l\'exporter en IFC.

-   <img alt="" src=images/Draft_AnnotationStyleEditor.svg  style="width:32px;"> [Éditer le style des annotations](Draft_AnnotationStyleEditor/fr.md) : permet de définir des styles qui affectent les propriétés visuelles des objets de type annotation.



### Utilitaires

-   <img alt="" src=images/BIM_TogglePanels.svg  style="width:32px;"> [Bascule des panneaux inférieurs](BIM_TogglePanels/fr.md) : affiche ou masque les fenêtres de sortie (la vue rapport et la console Python).

-   <img alt="" src=images/BIM_Trash.svg  style="width:32px;"> [Corbeille](BIM_Trash/fr.md) : déplace les objets sélectionnés vers la corbeille, créée si nécessaire.

-   <img alt="" src=images/BIM_WPView.svg  style="width:32px;"> [Vue du plan de travail](BIM_WPView/fr.md) : règle la caméra pour qu\'elle soit face au plan de travail en cours.

-   <img alt="" src=images/Draft_SelectGroup.svg  style="width:32px;"> [Sélection groupée](Draft_SelectGroup/fr.md) : sélectionne le contenu des objets de type [Std Groupe](Std_Group/fr.md) ou des objets de type groupe de [Arch](Arch_Workbench/fr.md).

-   <img alt="" src=images/Draft_Slope.svg  style="width:32px;"> [Pente](Draft_Slope/fr.md) : incline les [Draft Lignes](Draft_Line/fr.md) ou les [Draft Polylignes](Draft_Wire.md) sélectionnés en augmentant ou en diminuant, la coordonnée Z de tous les points après le premier.

-   <img alt="" src=images/Draft_WorkingPlaneProxy.svg  style="width:32px;"> [Proxy de plan de travail](Draft_WorkingPlaneProxy/fr.md) : crée un proxy de plan de travail pour sauvegarder le [Draft Plan de travail](Draft_SelectPlane/fr.md).

-   <img alt="" src=images/Draft_AddConstruction.svg  style="width:32px;"> [Ajouter au groupe de construction](Draft_AddConstruction/fr.md) : déplace les objets vers le [Draft mode construction](Draft_ToggleConstructionMode/fr.md).

-   <img alt="" src=images/Arch_SplitMesh.svg  style="width:32px;"> [Diviser un maillage](Arch_SplitMesh/fr.md) : divise un maillage sélectionné en composants séparés.

-   <img alt="" src=images/Arch_MeshToShape.svg  style="width:32px;"> [Maillage vers une forme](Arch_MeshToShape/fr.md) : convertit un maillage en une forme, en unifiant les faces coplanaires.

-   <img alt="" src=images/Arch_SelectNonSolidMeshes.svg  style="width:32px;"> [Sélection de Sélection de maillages non-manifoldz non-manifold](Arch_SelectNonSolidMeshes/fr.md) : sélectionne tous les maillages non-manifold de la sélection courante ou du document.

-   <img alt="" src=images/Arch_RemoveShape.svg  style="width:32px;"> [Supprimer la forme](Arch_RemoveShape/fr.md) : rend l\'objet Arch basé sur une forme cubique entièrement paramétrique.

-   <img alt="" src=images/Arch_CloseHoles.svg  style="width:32px;"> [Fermer les trous](Arch_CloseHoles/fr.md) : ferme les trous dans un objet de forme sélectionné.

-   <img alt="" src=images/Arch_MergeWalls.svg  style="width:32px;"> [Fusionner des murs](Arch_MergeWalls/fr.md) : fusionne des murs.

-   <img alt="" src=images/Arch_Check.svg  style="width:32px;"> [Vérification](Arch_Check/fr.md) : vérifie si les objets sélectionnés sont des solides et ne contiennent pas de défauts.

-   <img alt="" src=images/Arch_ToggleIfcBrepFlag.svg  style="width:32px;"> [Basculer en B-rep IFC](Arch_ToggleIfcBrepFlag/fr.md) : force un objet sélectionné à être exporté en tant que [IfcFacetedBrep](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm).

-   <img alt="" src=images/Arch_ToggleSubs.svg  style="width:32px;"> [Bascule des sous composants](Arch_ToggleSubs/fr.md) : affiche ou cache les sous-composants d\'un objet Arch.

-   <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Prendre des cotes](Arch_Survey/fr.md) : permet de rentrer ou de sortir du mode prise de cotes.

-   <img alt="" src=images/BIM_Diff.svg  style="width:32px;"> [Comparateur d\'IFC](BIM_Diff/fr.md) : affiche une différence visuelle entre deux fichiers IFC.

-   <img alt="" src=images/BIM_IfcExplorer.svg  style="width:32px;"> [Explorateur d\'IFC](BIM_IfcExplorer/fr.md) : ouvre un outil permettant d\'explorer la structure d\'un fichier IFC avant de l\'importer.

-   <img alt="" src=images/Arch_IfcSpreadsheet.svg  style="width:32px;"> [Tableur IFC](Arch_IfcSpreadsheet/fr.md) : cet outil crée une feuille de calcul pour stocker les propriétés IFC d\'un objet.

-   <img alt="" src=images/BIM_ImagePlane.svg  style="width:32px;"> [Plan d\'image](BIM_ImagePlane/fr.md) : insère un plan d\'image dans le document.

-   <img alt="" src=images/BIM_Unclone.svg  style="width:32px;"> [Cloner libre](BIM_Unclone/fr.md) : crée un objet cloné indépendant de l\'objet d\'origine.

-   <img alt="" src=images/BIM_Rewire.svg  style="width:32px;"> [Recréer les polylignes](BIM_Rewire/fr.md) :

-   <img alt="" src=images/BIM_Glue.svg  style="width:32px;"> [Coller](BIM_Glue/fr.md) :

-   <img alt="" src=images/BIM_Reextrude.svg  style="width:32px;"> [Extruder de nouveau](BIM_Reextrude/fr.md) : recrée une extrusion à partir d\'une forme qui a perdu son extrusion paramétrique en sélectionnant une face de base.

-   Outils pour les panneaux :

  - <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> [Panneaux](Arch_Panel/fr.md) : crée un objet panneau à partir d\'un objet 2D sélectionné.

  - <img alt="" src=images/Arch_Panel_Cut.svg  style="width:32px;"> [Découpe de panneaux](Arch_Panel_Cut/fr.md) : crée une vue coupée en 2D à partir d\'un panneau.

  - <img alt="" src=images/Arch_Panel_Sheet.svg  style="width:32px;"> [Feuille de panneau](Arch_Panel_Sheet/fr.md) : crée une feuille de découpe 2D comprenant des découpes de panneaux ou d\'autres objets 2D.

  - <img alt="" src=images/Arch_Nest.svg  style="width:32px;"> [Calepinage](Arch_Nest/fr.md) : permet d\'imbriquer plusieurs objets plats à l\'intérieur d\'une forme conteneur.

-   Outils pour les structures :

-   <img alt="" src=images/Arch_Structure.svg  style="width:32px;"> [Structure](Arch_Structure/fr.md) : crée un élément structurel à partir de rien ou en utilisant un objet sélectionné comme base.

  - <img alt="" src=images/Arch_StructuralSystem.svg  style="width:32px;"> [Système structurel](Arch_StructuralSystem/fr.md) :

  - <img alt="" src=images/Arch_StructuresFromSelection.svg  style="width:32px;"> [Structures multiples](Arch_StructuresFromSelection/fr.md) :

-   <img alt="" src=images/IFC_Diff.svg  style="width:32px;"> [Différence IFC](IFC_Diff/fr.md) :

-   <img alt="" src=images/IFC_Expand.svg  style="width:32px;"> [Développer l\'IFC](IFC_Expand/fr.md) :

-   <img alt="" src=images/IFC_MakeProject.svg  style="width:32px;"> [Projet IFC](IFC_MakeProject/fr.md) :

-   <img alt="" src=images/IFC_UpdateIOS.svg  style="width:32px;"> [Mise à jour de IfcOpenShell](IFC_UpdateIOS/fr.md) :

-   Petit déplacement :

  - [Mode Auto/manuel](BIM_Nudge_Switch.md):

  - [Vers le haut](BIM_Nudge_Up/fr.md) :

  - [Vers le bas](BIM_Nudge_Down/fr.md) :

  - [Vers la gauche](BIM_Nudge_Left/fr.md) :

  - [Vers la droite](BIM_Nudge_Right/fr.md) :

  - [Rotation à gauche](BIM_Nudge_RotateLeft/fr.md) :

  - [Rotation à droite](BIM_Nudge_RotateRight/fr.md) :

  - [Extension](BIM_Nudge_Extend/fr.md) :

  - [Diminution](BIM_Nudge_Shrink/fr.md) :



### Barre d\'état 

La barre d\'état contient quelques boutons qui permettent de changer facilement d\'état :

-   <img alt="" src=images/BIM_TogglePanels.svg  style="width:32px;"> [Bascule des panneaux de bas de page](BIM_TogglePanels/fr.md) : affiche ou masque la [vue rapport](Report_view/fr.md) et la [console Python](Python_console/fr.md).

-   <img alt="" src=images/BIM_ToggleViews.svg  style="width:32px;"> Bascule des vues : affiche ou masque le panneau de [Gérer les vues BIM](BIM_Views/fr.md).

-   <img alt="" src=images/BIM_ToggleBackground.svg  style="width:32px;"> Cycle de l\'arrière-plan : cycles entre les modes dégradé vertical, dégradé radial et arrière-plan de couleur simple. Cela peut être utilisé pour alterner entre un arrière-plan sombre pour la modélisation et un arrière-plan blanc pour le dessin en 2D.

-   <img alt="" src=images/IFC.svg  style="width:32px;"> Vérrouiller IFC : permet de passer [du mode IFC verrouillé au mode IFC déverrouillé](NativeIFC/fr#Modes_verrouillé_et_déverrouillé.md)



### Menu contextuel de la vue en arborescence 

A définir



### Menu contextuel de la vue 3D 

A définir



### Outils obsolètes 

-   <img alt="" src=images/Arch_3Views.svg  style="width:32px;"> [Arch 3 vues depuis un maillage](Arch_3Views/fr.md) : crée des vues de dessus, de face et de côté à partir d\'un [maillage](Mesh_Workbench/fr.md). Non disponible dans {{VersionPlus/fr|1.0}}.

-   <img alt="" src=images/Arch_BuildingPart.svg  style="width:32px;"> [Arch Partie de bâtiment](Arch_BuildingPart/fr.md) : crée une partie de bâtiment incluant les objets sélectionnés. Non disponible dans {{VersionPlus/fr|1.0}}. Utilisez plutôt [Arch Niveau](Arch_Floor/fr.md).

-   <img alt="" src=images/Arch_CloneComponent.svg  style="width:32px;"> [Cloner un composant](Arch_CloneComponent/fr.md) : produit des composants Arch qui sont des clones d\'objets Arch sélectionnés. Non disponible dans {{VersionPlus/fr|1.0}}. Utilisez plutôt [Draft Cloner](Draft_Clone/fr.md).

-   <img alt="" src=images/Arch_CutLine.svg  style="width:32px;"> [Arch Couper selon une ligne](Arch_CutLine/fr.md) : coupe un objet en fonction d\'une ligne. Non disponible dans {{VersionPlus/fr|1.0}}. Utilisez plutôt [Arch Couper selon un plan](Arch_CutPlane/fr.md).

-   <img alt="" src=images/Arch_MultiMaterial.svg  style="width:32px;"> [Arch Multi-matériau](Arch_MultiMaterial/fr.md) : crée un multi-matériau et l\'attribue aux objets sélectionnés, s\'il y en a. Non disponible dans {{VersionPlus/fr|1.0}}. Utilisez plutôt [BIM Matériau](BIM_Material/fr.md).

-   <img alt="" src=images/Arch_Project.svg  style="width:32px;"> [Arch Projet](Arch_Project/fr.md) : crée un projet incluant les objets sélectionnés. Non disponible dans {{VersionPlus/fr|1.0}}. Utilisez plutôt [BIM Projet](BIM_Project/fr.md).

-   <img alt="" src=images/Arch_SetMaterial.svg  style="width:32px;"> [Arch Matériau](Arch_SetMaterial/fr.md) : crée un matériau et l\'attribue aux objets sélectionnés, s\'il y en a. Non disponible dans {{VersionPlus/fr|1.0}}. Utilisez plutôt [BIM Matériau](BIM_Material/fr.md).



## Préférences

-   <img alt="" src=images/Preferences-bim.svg  style="width:32px;"> [Préférences](BIM_Preferences/fr.md) : préférences générales pour l\'atelier BIM.
-   [Réglage fin](Fine-tuning/fr#Atelier_BIM.md) : paramètres supplémentaires pour améliorer le comportement de BIM.



## Travailler avec les IFC 

L\'atelier BIM fonctionne nativement avec les fichiers [Industry Foundation Classes](https://fr.wikipedia.org/wiki/Industry_Foundation_Classes) (IFC). Natif signifie qu\'il n\'y a plus de traduction entre le contenu IFC et FreeCAD : le contenu des IFC est directement rendu dans FreeCAD, et tout changement affecte directement le contenu des IFC. Pour en savoir plus, voir [NativeIFC](NativeIFC/fr.md).

Si vous n\'avez pas l\'intention de travailler avec d\'autres personnes et que vous n\'avez pas besoin d\'IFC, vous pouvez toujours utiliser les outils de l\'atelier BIM et ignorer tout ce qui a trait à l\'IFC. Vous pouvez toujours exporter votre modèle au format IFC.

L\'ancien importateur de [Arch IFC](Arch_IFC/fr.md) est désactivé par défaut dans FreeCAD mais toujours disponible à partir de Python.



## Formats de fichiers 

-   [IFC](Arch_IFC/fr.md) : Industry Foundation Classes
-   [DAE](Arch_DAE/fr.md) : format de maillage de Collada
-   [OBJ](Arch_OBJ/fr.md) : format de maillage OBJ (seulement en exportation)
-   [JSON](Arch_JSON/fr.md) : JavaScript Object Notation format (seulement en exportation)
-   [3DS](Arch_3DS/fr.md) : format 3DS (seulement en importation)
-   [SHP](Arch_SHP/fr.md) : shapefiles GIS (seulement en importation)

## API

L\'atelier Arch peut être utilisé dans des scripts [Python](Python/fr.md) et dans des [macros](Macros/fr.md) grâce aux fonctions [Arch Python API](Arch_API/fr.md).



## Tutoriels et apprentissage 

-   [Migrer de Revit vers FreeCAD](Migrating_to_FreeCAD_from_Revit/fr.md)
-   [Tutoriels sur ce wiki Arch & BIM](Tutorials/fr#Architecture_et_BIM.md)
-   [\"BIM with FreeCAD\" série de vidéos de Yorik](https://www.youtube.com/playlist?list=PLmKdGVtV5Vnt2cj4IZIv9FM39QHaE1ZaU)
-   [\"FreeCAD tutorials\" série de vidéos de Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwkkxVOfVmR8ObpPN5QbL7ye)
-   [\"Quinta Monroy\" série de vidéos de Regis](https://www.youtube.com/playlist?list=PLDd21g-eSHwnAYyutuKhrPY51skaBhrVU)
-   [\"HRCompacta\" chaîne youtube (la plupart du contenu est en portugais)](https://www.youtube.com/@HRCompacta)
-   [\"FreeCADBIM\" chaîne youtube (la plupart du contenu est en portugais)](https://www.youtube.com/@FreeCadBIM)



## Fichiers d\'exemple 

-   FreeCAD propose un exemple BIM à la page Start.
-   D\'autres exemples de fichiers BIM sont disponibles ici : [Exemples BIM](https://github.com/yorikvanhavre/FreeCAD-BIM-examples).
-   Dans FreeCAD, utilisez le menu Aide → Exemples BIM.



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > BIM Workbench/fr
