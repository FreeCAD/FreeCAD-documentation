# Release notes 0.20/fr
**Cette page suit les nouvelles fonctionnalités à mesure qu'elles sont ajoutées à la version de développement de FreeCAD, qui est actuellement la 0.20. Lorsque les fonctionnalités de la 0.20 seront figées, supprimez ces messages et n'ajoutez plus d'autres fonctionnalités à cette page. FreeCAD 0.20 devrait sortir en 202x.**


**!!! Toutes les images de cette page doivent utiliser le suffixe {{FileName|_relnotes_0.20** !!!}}


{{Message|
Des fonctionnalités sont-elles manquantes? Mentionnez-les dans les [https://forum.freecadweb.org/viewtopic.php?f&#61;10&t&#61;56135 Notes de publication pour v0.20] du fil du forum.

Consultez l'[aide FreeCAD](Help_FreeCAD/fr.md) pour savoir comment contribuer à FreeCAD.
}}


{{TOCright}}

**FreeCAD 0.20** a été publié le **DD mois 202x**, récupérez-le sur la page de [Téléchargement](Download/fr.md). Ceci est un résumé des changements les plus intéressants. La liste complète des modifications est disponible dans le [journal des modifications MantisBT bugtracker FC 0.20](https://www.freecadweb.org/tracker/changelog_page.php?version_id=78).

Les notes de versions plus anciennes de FreeCAD sont disponibles dans la [Liste des fonctionnalités](Feature_list/fr#Notes_de_versions.md).

## Points forts 

## Généralités

### Python 3 et Qt5 

### Quelques problèmes 

### Développement

Pour [compiler FreeCAD sous Windows](Compile_on_Windows/fr.md), il existe différents Libpacks (bibliothèques pré-emballées) disponibles :

-   Libpack pour Windows avec Qt xx, OCC yy et Python zz

La plus basse version de Python supportée est la 3.6.9 selon <https://forum.freecadweb.org/viewtopic.php?f=10&t=62701>.

Systèmes d\'exploitation pris en charge :

-   Windows 7, 8 et 10
-   Linux Ubuntu Bionic Beaver (18.04) et Focal Fossa (20.04)
-   MacOS version minimale 10.12 Sierra

Autres nouvelles du développement :

### Documentation

### Limitations connues 

## Interface utilisateur 

+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ![](images/Navi_Cube_relnotes_0.20.gif ) | Le cube de navigation a été retravaillé pour activer ces nouvelles fonctionnalités :                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                | -   Il y a maintenant des faces d\'arêtes pour voir la scène à des angles de 45 °.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                | -   La nouvelle option de préférences [Tourner au plus près](Preferences_Editor/fr#Navigation.md) permet de visualiser la scène à l\'incrément le plus proche. Lorsqu\'elle est désactivée, en cliquant sur une face du cube, vous vous retrouverez toujours à la même position, quel que soit l\'état du cube dans lequel vous vous trouviez lorsque vous avez cliqué sur la face. Voir l\'animation à gauche pour comprendre ce que cela signifie. Essayez la même séquence de clics que dans l\'animation sans l\'option *Rotate to nearest* pour voir la différence. |
|                                                                | -   En cliquant sur le point en haut à droite du cube, vous pouvez voir rapidement la vue arrière de la scène actuelle.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                | -   La taille du cube peut être ajustée par l\'option de préférences [Taille du cube](Preferences_Editor/fr#Navigation.md).                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                | [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=52118), [Pull request \#4502](https://github.com/FreeCAD/FreeCAD/pull/4502).                                                                                                                                                                                                                                                                                                                                                                                                                              |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

  -------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](images/Improved_tooltips_relnotes_0.20.gif )   Des infobulles affichent désormais le nom de la commande dans le titre, ce qui permet aux nouveaux utilisateurs de rechercher plus facilement de l\'aide. À la fin de l\'infobulle, le nom de la commande \"interne\" est ajouté entre parenthèses : *(Std\_WhatsThis)*. C\'est également le nom de la page qui documente la commande dans le Wiki. [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=34&t=58747), [Pull request \#4978](https://github.com/FreeCAD/FreeCAD/pull/4978).
  -------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](images/Std_UserEditMode_relnotes_0.20.gif )   La nouvelle commande [Std Mode d\'édition](Std_UserEditMode/fr.md) permet à l\'utilisateur de choisir le mode d\'édition qui sera utilisé lorsqu\'il double-cliquera sur un objet dans la [Vue en arborescence](Tree_view/fr.md). Cliquez sur l\'image à gauche pour voir une animation de la sélection. Si le mode d\'édition sélectionné n\'est pas applicable, le mode d\'édition par défaut de l\'objet est utilisé à la place. [Pull request \#5110](https://github.com/FreeCAD/FreeCAD/pull/5110).
  ------------------------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

+------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ![](images/Dependencies-selection_relnotes_0.20.png ) | Le menu contextuel de la [Vue en arborescence](Tree_view/fr.md) contient une nouvelle entrée **Ajouter des objets dépendants à la sélection**. |
|                                                                                          | [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=13566), [Pull request \#4133](https://github.com/FreeCAD/FreeCAD/pull/4133).                              |
|                                                                                          |                                                                                                                                                                                  |
|                                                                                          | Dans l\'image, l\'objet *Hole001* a été sélectionné par l\'utilisateur, puis                                                                                                     |
|                                                                                          | ses dépendances ont été ajoutées à la sélection via le menu contextuel.                                                                                                          |
+------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### Autres améliorations de l\'interface utilisateur 

-   Deux nouveaux modes de navigation à la souris ont été ajoutés. L\'un basé sur **[OpenSCAD](Mouse_navigation/fr#Mode_OpenSCAD.md)**, l\'autre sur **[TinkerCAD](Mouse_navigation/fr#Mode_TinkerCAD.md)**. [Discussion du forum OpenSCAD](https://forum.freecadweb.org/viewtopic.php?f=8&t=60975), [Discussion du forum TinkerCAD](https://forum.freecadweb.org/viewtopic.php?p=544639#p544376), [commit 1](https://github.com/FreeCAD/FreeCAD/commit/a1c9ab658c), [commit 2](https://github.com/FreeCAD/FreeCAD/commit/ef100d55e9d50), [commit 3](https://github.com/FreeCAD/FreeCAD/commit/549e5b5650).
-   Il est maintenant possible de faire un panoramique de la vue du [Graphique de dépendance](Std_DependencyGraph/fr.md) avec la souris. [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=34791), [pull request \#4638](https://github.com/FreeCAD/FreeCAD/pull/4638).
-   Correction d\'un problème où l\'utilisation d\'un stylet de tablette (par exemple, une tablette Wacom) était lente au point d\'être complètement inutilisable. [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=45046), [Pull request \#4687](https://github.com/FreeCAD/FreeCAD/pull/4687).
-   Le système de coordonnées dans la vue 3D peut être redimensionné dans les préférences dans la section [Affichage → Vue 3D](Preferences_Editor/fr#Vue_3D.md). [Pull request \#5182](https://github.com/FreeCAD/FreeCAD/pull/5182)
-   Un nouveau paramètre dans [Préférences → Général](Preferences_Editor/fr#G.C3.A9n.C3.A9ral.md) permet de substituer le séparateur décimal du pavé numérique par le séparateur de la locale appropriée s\'ils sont différents. [Pull request \#3256](https://github.com/FreeCAD/FreeCAD/pull/3256) [Pull request \#5150](https://github.com/FreeCAD/FreeCAD/pull/5150) [Pull request 5203](https://github.com/FreeCAD/FreeCAD/pull/5203)

## App::Link et assemblage 

## Core System, App, Base et espaces de noms de la Gui 

  ------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/Object_selection_relnotes_0.20.png  style="width:384px;">   Lorsque vous utilisez **Edition → Copier** ou **Edition → Dupliquer la sélection** pour un objet avec des dépendances, il existe un nouveau bouton **Utiliser les sélections d'origine** dans le dialogue de sélection d\'objet. Cliquez sur ce bouton pour copier/dupliquer uniquement les objets que vous avez sélectionnés à l\'origine avant d\'ouvrir le dialogue, en ignorant les dépendances et en ne tenant pas compte des actions que vous avez pu effectuer pendant que le dialogue était ouvert, comme cocher ou décocher certaines cases. L\'effet est le même que si vous aviez décoché toutes les cases à côté des objets que vous n\'aviez pas sélectionnés à l\'origine et appuyé sur OK. Remarque : il convient d\'être particulièrement prudent lorsque vous copiez/dupliquez des pages TechDraw. Il est recommandé de copier/dupliquer également tous les enfants de la page (modèles, vues, dimensions, etc.). Sinon, les modifications apportées à l\'une des pages auront également un impact sur l\'autre page. Par exemple, la suppression de l\'une des vues d\'une page entraîne sa suppression de l\'autre page. Par exemple, la suppression d\'une des vues d\'une page la supprime également de l\'autre page. La suppression d\'une des pages supprime également tout le contenu de l\'autre page si des copies du contenu ne sont pas également effectuées.
  ------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Un nouveau type de module complémentaire appelé [Preference Pack](Preference_Packs/fr.md) a été ajouté, permettant de distribuer et d\'appliquer un sous-ensemble d\'un fichier de préférences utilisateur (user.cfg). [Discussion sur le forum](https://forum.freecadweb.org/viewtopic.php?f=17&t=62477), [Pull request \#4787](https://github.com/FreeCAD/FreeCAD/pull/4787)

## Gestionnaire d\'Addon 

## Atelier Arch 

## Atelier Draft 

-   Une case à cocher **Global** a été ajoutée au panneau des tâches de nombreuses commandes de dessin. Le fait de la cocher permet de saisir des coordonnées dans le système de coordonnées global même si le [plan de travail](Draft_SelectPlane/fr.md) n\'est pas aligné avec le plan XY global.

-   La commande <img alt="" src=images/Draft_Hatch.svg  style="width:24px;"> [Draft Hachure](Draft_Hatch/fr.md) a été introduite. Elle crée des hachures sur les faces d\'un objet sélectionné à l\'aide de motifs provenant de fichiers PAT d\'AutoCAD.

-   La commande <img alt="" src=images/Draft_AddNamedGroup.svg  style="width:24px;"> [Draft Nommer un groupe](Draft_AddNamedGroup/fr.md) a été introduite. La commande<img alt="" src=images/Draft_AddToGroup.svg  style="width:24px;"> [Draft Déplacer vers un groupe](Draft_AddToGroup/fr.md) a été étendue avec la même fonctionnalité.

-   Le travail sur la commande <img alt="" src=images/Draft_SetStyle.svg  style="width:24px;"> [Draft Définir le style](Draft_SetStyle/fr.md), toujours en cours dans FreeCAD version 0.19, a été terminé.

-   Une option d\'édition par double-clic a été ajoutée pour <img alt="" src=images/Draft_Text.svg  style="width:24px;"> [Draft Texte](Draft_Text/fr.md). Elle ouvre le même panneau de tâches d\'édition que celui utilisé lors de la création d\'un texte.

-   Pour <img alt="" src=images/Draft_Dimension.svg  style="width:24px;"> [Draft Dimensions](Draft_Dimension/fr.md), la {{Value|arch}} **Unit Override** pour les dimensions architecturales impériales a été introduite.

-   Les objets <img alt="" src=images/Draft_Shape2DView.svg  style="width:24px;"> [Draft Vue 2D d\'une forme](Draft_Shape2DView/fr.md) ont maintenant une propriété **Auto Update**. La définition de cette propriété à {{False}} peut s\'avérer utile si un document contient de nombreux objets *Draft Vue 2D d\'une forme* ou s\'ils sont complexes.

-   Il est maintenant possible d\'inverser une [Draft Polyligne](Draft_Wire/fr.md) via le menu contextuel <img alt="" src=images/Draft_Edit.svg  style="width:24px;"> [Draft Éditer](Draft_Edit/fr.md). [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=23&t=58643&start=20), [Pull request \#4811](https://github.com/FreeCAD/FreeCAD/pull/4811).

### Autres améliorations de Draft 

-   Correction de [Draft Aimantation Grille](Draft_Snap_Grid/fr.md) lorsque le curseur se trouve sur une face. [Discussion du forum](https://forum.freecad.org/viewtopic.php?f=23&t=62274). [Git commit](https://github.com/FreeCAD/FreeCAD/commit/1761eb8ce).

-   Les nouveaux [Draft Textes](Draft_Text/fr.md) sont désormais alignés sur le [plan de travail](Draft_SelectPlane/fr.md), [Pull request \#5092](https://github.com/FreeCAD/FreeCAD/pull/5092).

-   La prise en charge de deux convertisseurs DWG a été ajoutée : [LibreDWG](https://www.gnu.org/software/libredwg) et [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg). Voir [Préférences d\'Import Export](Import_Export_Preferences/fr#DWG.md) et [FreeCAD et l\'importation DWG](FreeCAD_and_DWG_Import/fr.md) pour plus d\'informations.

## Atelier FEM 

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/FEM_Gmsh-MeshSizeFromCurvature_relnotes_0.20.png  style="width:384px;">Effet de \"la taille du maillage à partir de la courbure\". À gauche : réglé sur 12, à droite : désactivé                 Il existe une nouvelle propriété pour le mailleur [Gmsh](FEM_MeshGmshFromShape/fr.md). Le nombre d\'éléments de maillage par $2\pi$ fois le rayon de la courbure peut être spécifié. La valeur par défaut est 12 et pour obtenir un maillage plus fin aux petits coins ou trous, cette valeur peut être augmentée pour de meilleurs résultats. Cette fonctionnalité nécessite Gmsh 4.8 ou plus récent. [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=56401), [Pull request \#4596](https://github.com/FreeCAD/FreeCAD/pull/4596)
  <img alt="" src=images/FEM_Gmsh-RecombinationAlgorithm_relnotes_0.20.png  style="width:384px;">Effet de l\'algorithme de recombinaison. À gauche : en utilisant *Simple*, à droite : en utilisant *Simple full-quad*   FreeCAD permet maintenant de sélectionner un algorithme ainsi que la recombinaison de maillage 3D pour le mailleur [Gmsh](FEM_MeshGmshFromShape/fr.md). Pour plus de détails sur la recombinaison des éléments de maillage, [FEM Maillage MEF à partir d\'une forme avec Gmsh](FEM_MeshGmshFromShape/fr#Recombinaison_d.27.C3.A9l.C3.A9ments.md). [Pull request \#4706](https://github.com/FreeCAD/FreeCAD/pull/4706)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Autres améliorations de FEM 

-   Un nouveau solveur a été ajouté : **Solve → [<img src=images/FEM_SolverMystran.svg style="width:16px"> [Solveur Mystran](FEM_SolverMystran/fr.md)**. De nombreux commits.
-   Une nouvelle contrainte a été ajoutée : **Model → Contraintes géométriques → [<img src=images/FEM_ConstraintSpring.svg style="width:16px"> [Contrainte ressort](FEM_ConstraintSpring/fr.md)**. [Pull request \#4982](https://github.com/FreeCAD/FreeCAD/pull/4982)
-   L\'ordre des éléments des maillages [Gmsh](FEM_MeshGmshFromShape/fr.md) peut être modifié via la boîte de dialogue de maillage. [Pull request \#4660](https://github.com/FreeCAD/FreeCAD/pull/4660)
-   Les cartes de matériaux peuvent désormais contenir des valeurs de conductivité électrique. [Pull request \#4647](https://github.com/FreeCAD/FreeCAD/pull/4647)
-   Cartes de matériaux ajoutées pour l\'azote et l\'argon. [Pull request \#4649](https://github.com/FreeCAD/FreeCAD/pull/4649)
-   Ajout de la prise en charge des algorithmes de maillage \"HXT\" (3D) et \"Packing Parallelograms\" (2D) de [Gmsh](FEM_MeshGmshFromShape/fr.md). [Pull request \#4654](https://github.com/FreeCAD/FreeCAD/pull/4654)
-   Permettre de définir pour la propriété *Optimisation d\'ordre élevé* de [Gmsh](FEM_MeshGmshFromShape/fr#Propriétés.md) un certain algorithme.[Pull request \#4705](https://github.com/FreeCAD/FreeCAD/pull/4705)
-   Les matériaux solides non linéaires à durcissement simple peuvent désormais avoir un nombre arbitraire de limites d\'élasticité. [Pull request \#5024](https://github.com/FreeCAD/FreeCAD/pull/5024)

## Importation

## Prise en main des matériaux 

## Atelier Mesh 

### Amélioration du support des éléments NASTRAN GRID 

L\'outil d\'importation de Mesh supporte maintenant l\'élément \"GRID\*\" de haute précision. L\'élément \"GRID\" de précision standard a également été amélioré et supporte maintenant les entrées numériques délimitées par des espaces ainsi que les entrées à largeur de champ fixe, conformément à la documentation du format NASTRAN95.

### Autres améliorations de Mesh 

Correction des faux négatifs lors des tests d\'auto-intersection lorsque les facettes sont coplanaires : [Pull request \#5002](https://github.com/FreeCAD/FreeCAD/pull/5002).

## Atelier OpenSCAD 

L\'interopérabilité avec OpenSCAD a été améliorée, en ajoutant le support de plusieurs opérations manquantes dans les versions précédentes (extrusion linéaire avec rotations, extrusions rotatives). Plusieurs opérations ont été modifiées pour fournir des équivalents d\'objets FreeCAD améliorés, en particulier pour les extrusions torsadées. La génération de surfaces à partir de données discrètes a été modifiée pour donner des résultats plus proches de ceux d\'OpenSCAD, plutôt que des surfaces cannelées.

**Ajouter un élément OpenSCAD** - a maintenant des options supplémentaires

Load - charger un fichier scad
Save - sauvegarder un fichier scad
Refresh - mise à jour de la vue FreeCAD
Clear - effacer la saisie de texte

Il y a également une zone de texte pour le retour des erreurs d\'OpenSCAD.

## Atelier Part 

### Autres améliorations de Part 

-   La boîte de dialogue pour éditer des [Cylindres](Part_Cylinder/fr.md) permet maintenant de spécifier un angle par rapport à la normale du plan d\'attache choisi. De cette façon, on peut créer des cylindres obliques. [Pull request \#4708](https://github.com/FreeCAD/FreeCAD/pull/4708)

## Atelier PartDesign 

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/PD_Pocket-direction_relnotes_0.20.gif  style="width:384px;">Cavité selon différentes directions.Cliquez sur l\'image pour afficher l\'animation.                                                               Il est maintenant possible de spécifier la direction pour l\'extrusion de la cavité. [Pull request \#5164](https://github.com/FreeCAD/FreeCAD/pull/5164)
  <img alt="" src=images/PD_Pad-Length-along-reference_relnotes_0.20.gif  style="width:384px;">Extrusion le long d\'une arête du modèle.Cliquez sur l\'image pour afficher l\'animation.                                      Il y a une nouvelle option pour extruder le long de la direction d\'un bord dans le modèle 3D. [Pull request \#4685](https://github.com/FreeCAD/FreeCAD/pull/4685)
  <img alt="" src=images/PD_Pad-Length-alog-direction_relnotes_0.20.gif  style="width:384px;">Effet de la nouvelle option \"Longueur le long de la normale de l\'esquisse\".Cliquez sur l\'image pour afficher l\'animation.   Nouvelle option pour extruder d\'une certaine longueur le long de la direction. La longueur est mesurée le long de la normale de l\'esquisse ou le long de la direction personnalisée. [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=17&t=50466), [Pull request \#3893](https://github.com/FreeCAD/FreeCAD/pull/3893)
  <img alt="" src=images/PartDesign_Cylinder_direction_relnotes_0.20.png  style="width:384px;">                                                                                                                                                               La boîte de dialogue pour éditer un [Cylindre](PartDesign_AdditiveCylinder/fr.md) (additif et soustractif) permet maintenant de spécifier un angle par rapport à la normale du plan d\'attache choisi. De cette façon, on peut créer des cylindres obliques. [Pull request \#4708](https://github.com/FreeCAD/FreeCAD/pull/4708)
  <img alt="" src=images/PartDesign_Chamfer_Face_Selection_relnotes_0.20.png  style="width:384px;">                                                                                                                                                       Lorsque la distance et l\'angle sont spécifiés dans l\'outil [Chanfrein](PartDesign_Chamfer/fr.md) et que des faces sont sélectionnées, la distance sera appliquée le long des faces sélectionnées. De même, si deux distances sont spécifiées, la taille à 1 sera appliquée le long de la face sélectionnée. Ce comportement peut être remplacé par l\'autre face en utilisant le bouton de changement de direction. [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=19&t=62084), [Pull request \#5039](https://github.com/FreeCAD/FreeCAD/pull/5039).
  <img alt="" src=images/PartDesign_Loft_Vertex_relnotes_0.20.png  style="width:384px;">.                                                                                                                                                                        Il est désormais possible de créer un [Lissage additif](PartDesign_AdditiveLoft/fr.md), [Lissage soustractif](PartDesign_SubtractiveLoft/fr.md), [Balayage additif](PartDesign_AdditivePipe/fr.md) ou [Balayage soustractif](PartDesign_SubtractivePipe/fr.md) vers ou depuis un [Vertex](Glossary/fr#V.md) d\'une esquisse ou d\'un corps. Cela permet par exemple de créer des pyramides. [Pull request \#5170](https://github.com/FreeCAD/FreeCAD/pull/5170) (pour les lissages), [Pull request \#5193](https://github.com/FreeCAD/FreeCAD/pull/5193) (pour les balayages)
  <img alt="" src=images/PartDesign_Helix_Growth_relnotes_0.20.png  style="width:384px;">.                                                                                                                                                                      La fonction [Hélice](PartDesign_AdditiveHelix/fr.md) a le nouveau mode **Hauteur-Tours-Croissance** pour créer des spirales plates. [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=19&t=56378) [Pull request \#4590](https://github.com/FreeCAD/FreeCAD/pull/4590)
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Autres améliorations de PartDesign 

-   Avec la fonction [Hélice](PartDesign_AdditiveHelix/fr.md), on peut désormais utiliser la normale de l\'esquisse comme axe. [Pull request \#5199](https://github.com/FreeCAD/FreeCAD/pull/5199)
-   La fonction [Pignon](PartDesign_Sprocket/fr.md) permet désormais de créer également des pignons normalisés ISO. [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=22&t=44525#p478369) [Pull request \#4478](https://github.com/FreeCAD/FreeCAD/pull/4478)
-   Les fonctions [Lissage](PartDesign_AdditiveLoft/fr.md) et [Balayage](PartDesign_AdditivePipe/fr.md) permettent désormais d\'utiliser les faces du corps pour les sections. [Pull request \#5155](https://github.com/FreeCAD/FreeCAD/pull/5155)
-   Il est désormais possible de sélectionner plusieurs faces avant d\'ouvrir la boîte de dialogue de [Protrusion](PartDesign_Pad/fr.md) ou [Cavité](PartDesign_Pocket/fr.md). Dans ce cas, la première face sélectionnée sera utilisée pour déterminer la direction par défaut de la ptrotrusion/cavité. [commit d34a5616](https://github.com/FreeCAD/FreeCAD/commit/d34a5616a2b38c96ad05f9a0763ba7504dfb814d)

## Atelier Path 

## Atelier Render 

## Atelier Sketcher 

  --------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/SketcherSplitExample2_relnotes_0.20.png )                                                  Nouvelle fonction ![](images/Sketcher_Split.svg  style="width:24px;"> [Diviser une arête](Sketcher_Split/fr.md) pour diviser les lignes ou les arcs existants. [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=9&t=55412) [Pull request \#4420](https://github.com/FreeCAD/FreeCAD/pull/4420)
  <img alt="" src=images/SketcherCreateRoundedRectangleExample_relnotes_0.20.png )                  Nouvel outil ![](images/Sketcher_CreateOblong.svg  style="width:24px;"> [Rectangle arrondi](Sketcher_CreateOblong/fr.md) pour créer des rectangles aux coins arrondis. [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=17&t=59210) [Main Pull request \#4835](https://github.com/FreeCAD/FreeCAD/pull/4835)
  <img alt="" src=images/SketcherCreateCenteredRectangleExample_relnotes_0.20.png  style="width:384px;">   Nouvel outil <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:24px;"> [Rectangle centré](Sketcher_CreateRectangle_Center/fr.md) pour définir des rectangles via un point central. [Main commit](https://github.com/FreeCAD/FreeCAD/commit/8b4acf11c2caf53cc1cb8dccd8bb6de8516f4492)
  <img alt="" src=images/Radiam_anim_relnotes_0.20.gif )                                                                      Nouvelle fonction ![](images/Sketcher_ConstrainRadiam.svg  style="width:24px;"> [Contrainte automatique rayon/diamètre](Sketcher_ConstrainRadiam/fr.md) permet d\'assigner automatiquement un poids sur le pôle B-spline, un diamètre sur un cercle complet ou un rayon sur un arc. Support de la multi-sélection comme outils de diamètre/rayon. [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=57584&start=20#p509485) [Main Pull request \#4855](https://github.com/FreeCAD/FreeCAD/pull/4855)
  <img alt="" src=images/SketcherRemoveAxesAlignmentResult_relnotes_0.20.png )                          Nouvel outil de contrainte ![](images/Sketcher_RemoveAxesAlignment.svg  style="width:24px;"> [Supprimer l\'alignement des axes](Sketcher_RemoveAxesAlignment/fr.md) pour supprimer l\'alignement des axes tout en essayant de préserver la relation de contrainte de la sélection. [Main commit](https://github.com/FreeCAD/FreeCAD/commit/3c593a33cedc3e6a42928d9087f8a160852cc685)
  \| ![](images/SketcherSnapSlot_relnotes_0.20.gif )                                                     [Sketcher Rainure](Sketcher_CreateSlot/fr.md) peut être contraint horizontalement ou verticalement soit en l\'aimantant manuellement avec la touche **Ctrl**, soit en utilisant l\'option *Auto contraintes* de Sketcher. [Pull request \#5200](https://github.com/FreeCAD/FreeCAD/pull/5200)
  --------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Autres améliorations de Sketcher 

-   Prise en charge de l\'Ajustement remanié. [Pull Request](https://github.com/FreeCAD/FreeCAD/pull/4330) [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=10&t=54441) \<\-- Besoin de copies d\'écran
-   Le comportement de l\'outil <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:24px;"> [Rainure](Sketcher_CreateSlot/fr.md) a changé. Les rainures peuvent maintenant être créées en définissant le centre des deux demi-cercles. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/4843) [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=17&t=59243&p=508658#p508658)
-   L\'automatisation de la visibilité permet d\'ouvrir Sketcher dans une [Vue en section](Sketcher_ViewSection/fr.md) lors de l\'entrée en mode édition. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/4742) [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=57056)
-   L\'automatisation de la visibilité permet de forcer la caméra en [Mode orthographique](Std_OrthographicCamera/fr.md) lorsqu\'on rentre dans le mode édition. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/4778) [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=22&t=44747).
-   Option permettant d\'afficher le nom de la contrainte dimensionnelle et d\'utiliser un format personnalisé pour celui-ci. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/4966) [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?t=61153)
-   Lors de l\'esquisse d\'un [arc à 3 points](Sketcher_Create3PointArc/fr.md) avec Autoconstraint activé, une [contrainte tangente](Sketcher_ConstrainTangent/fr.md) est proposée pour les 3 points lors du survol d\'une ligne/courbe. [Pull request](https://github.com/FreeCAD/FreeCAD/pull/4945) [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=3&t=60596&p=520217#p520209).
-   Les contraintes de rayon/diamètre sont affichées en utilisant une rotation angulaire pour faciliter la visualisation. L\'angle et le caractère aléatoire optionnel sont réglables par l\'utilisateur grâce aux paramètres documentés dans le [Réglage fin](Fine-tuning/fr.md). [Pull request](https://github.com/FreeCAD/FreeCAD/pull/4934) [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=22&t=60370)
-   Il est maintenant possible de fixer l\'angle de la direction lors de l\'utilisation de l\'outil [Réseau rectangulaire](Sketcher_RectangularArray/fr.md). [commit](https://github.com/FreeCAD/FreeCAD/commit/c9eaa2393d33) [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?p=535691#p535691)
-   Il est maintenant possible de fixer l\'angle de la direction lors de l\'utilisation des outils [Clone](Sketcher_Clone/fr.md), [Copier](Sketcher_Copy/fr.md) et [Déplacer](Sketcher_Move/fr.md). [commit](https://github.com/FreeCAD/FreeCAD/commit/6e4a09f569cf) [Discussion du forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=62799)

## Atelier Spreadsheet 

  -------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/Spreadsheet-Preferences-Spreadsheet_relnotes_0.20.png )   L\'atelier a maintenant des ![](images/Std_DlgPreferences.svg  style="width:24px;"> [Préférences](Spreadsheet_Preferences/fr.md). Elles sont utilisées par les commandes <img alt="" src=images/Spreadsheet_Import.svg  style="width:16px;"> [Spreadsheet Importer](Spreadsheet_Import/fr.md) et <img alt="" src=images/Spreadsheet_Export.svg  style="width:16px;"> [Spreadsheet Exporter](Spreadsheet_Export/fr.md). [Pull request \#5073](https://github.com/FreeCAD/FreeCAD/pull/5073)
  -------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   Il est maintenant possible de sélectionner dans le menu contextuel des lignes/colonnes, à quelles positions les nouvelles lignes/colonnes seront insérées. [Pull request \#4704](https://github.com/FreeCAD/FreeCAD/pull/4704).

### Autres améliorations de Spreadsheet 

-   Importation XLSX (utilisée par [Std Importer](Std_Import/fr.md)) : Ajout du support des fonctions Partie entière par défaut (floor) et Partie entière supérieure (ceil). [Pull request \#5015](https://github.com/FreeCAD/FreeCAD/pull/5015).
-   Liaison de cellules : demande à un ensemble de cellules d\'afficher le contenu d\'un autre ensemble de cellules. Fait partie de [Pull request \#2862](https://github.com/FreeCAD/FreeCAD/pull/2862).
-   Amélioration de la navigation en utilisant les touches Tab et Entrée.
-   Amélioration de l\'interface pour couper et coller des blocs de cellules.

## Atelier Start 

## Atelier Surface 

## Atelier TechDraw 

+-------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <img alt="" src=images/TechDraw_ExtensionExample_relnotes_0.20.png  style="width:400px;"> | Plusieurs nouveaux outils, appelés [Extensions](TechDraw_Workbench/fr#Extensions.md), sont désormais disponibles. Ils offrent de nouvelles fonctionnalités cosmétiques pour améliorer les dessins : |
|                                                                                                             |                                                                                                                                                                                                             |
|                                                                                                             | -   <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width:24px;"> [TechDraw Lignes de centre cercles et arcs](TechDraw_ExtensionCircleCenterLines/fr.md)   |
|                                                                                                             | -   <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width:24px;"> [TechDraw Symbole filetage perçage](TechDraw_ExtensionThreadHoleSide/fr.md)                    |
|                                                                                                             | -   <img alt="" src=images/TechDraw_ExtensionThreadBoltSide.svg  style="width:24px;"> [TechDraw Symbole filetage boulon](TechDraw_ExtensionThreadBoltSide/fr.md)                     |
|                                                                                                             | -   <img alt="" src=images/TechDraw_ExtensionThreadHoleBottom.svg  style="width:24px;"> [TechDraw Symbole dessous perçage](TechDraw_ExtensionThreadHoleBottom/fr.md)               |
|                                                                                                             | -   <img alt="" src=images/TechDraw_ExtensionThreadBoltBottom.svg  style="width:24px;"> [TechDraw Symbole dessous boulon](TechDraw_ExtensionThreadBoltBottom/fr.md)                |
+-------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### Autres améliorations de TechDraw 

## Web

## Ateliers externes 


**Remarque :**

ce sont les nouveaux ateliers créés dans ce cycle de développement ou les anciens ateliers qui ont reçu des mises à jour. Voir les [Ateliers externes](External_workbenches/fr.md) pour plus d\'ateliers pouvant être installés et couvrant une grande variété de sujets. Si vous souhaitez voir votre atelier ajouté, rejoignez le [forum](https://forum.freecadweb.org/index.php) et présentez votre code.

### Outils d\'impression 3D 

### A2plus

### Assembly3

### Assembly4

### ArchTextures

### BOLTSFC

### Atelier CurvedShapes 

### Dodo (anciennement Flamingo) 

### Fasteners

### FCGear

L\'[atelier FCGear](FCGear_Workbench/fr.md) a reçu quelques améliorations:

-   Pour les engrenages à développante, le diamètre extérieur (ou pointe) et le diamètre de la racine sont exposés en tant que propriétés ([détails](https://github.com/looooo/freecad.gears/pull/69)).
-   Les objets engrenages sont maintenant [attachables](Part_EditAttachment/fr.md). ([détails](https://github.com/looooo/freecad.gears/pull/72))
-   Les objets engrenages peuvent désormais être utilisés comme des fonctions additives dans les corps de PartDesign ([détails](https://github.com/looooo/freecad.gears/pull/74)).
-   La création d\'objets engrenages apparaît désormais dans la pile d\'annulation ([détails](https://github.com/looooo/freecad.gears/pull/83))

### Atelier MeshRemodel 

### Atelier MOOC 

### NodeEditor (PyFlow) 

### Trails, PyTrails, Turns, pivy\_trackers et Geomatics 

[<img src="images/Property.png" style="width:16px"> News](Category_News.md) [<img src="images/Property.png" style="width:16px"> Documentation](Category_Documentation.md) [<img src="images/Property.png" style="width:16px"> Releases](Category_Releases.md)

---
[documentation index](../README.md) > [News](Category_News.md) > Release notes 0.20/fr
