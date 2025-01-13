# <img alt="Icône de l\'Atelier PartDesign" src=images/Workbench_PartDesign.svg  style="width:64px;"> PartDesign Workbench/fr




## Introduction

L\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> **atelier PartDesign** fournit des outils pour la modélisation de composants solides. Il est principalement axé sur la création de composants mécaniques qui peuvent être fabriqués et assemblés en un produit fini. Néanmoins, les solides créés peuvent en général être utilisés à d\'autres fins, tels que la [modélisation BIM](BIM_Workbench/fr.md), l\'[analyse par éléments finis](FEM_Workbench/fr.md) ou l\'[usinage et l\'impression 3D](CAM_Workbench/fr.md).

L\'atelier PartDesign utilise une méthodologie basée sur les fonctions. Un composant est représenté par le conteneur d\'un objet Corps (Body en anglais). Le corps définit un système de coordonnées local et contient les fonctions cumulatives qui définissent le composant. La plupart des fonctions sont basées sur des esquisses paramétriques et sont soit additives, soit soustractives. Par exemple, l\'outil [Protrusion](PartDesign_Pad/fr.md) ajoute l\'esquisse extrudée au solide en cours de développement, tandis que l\'outil [Cavité](PartDesign_Pocket/fr.md) soustrait l\'esquisse extrudée. Chaque fonction est cumulative et s\'appuie sur le résultat des fonctions précédentes. Il est également possible d\'utiliser des primitives ([Cylindre](PartDesign_AdditiveCylinder/fr.md), [Sphère](PartDesign_AdditiveSphere/fr.md), etc.) ainsi que des solides créés en dehors du corps comme des fonctions.

Voir la page [Édition de fonctions](Feature_editing/fr.md) pour une explication plus complète de ce processus, puis voir [PartDesign Tutoriel pour créer une pièce simple](Creating_a_simple_part_with_PartDesign.md) pour commencer à créer des solides.

L\'<img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [atelier Part](Part_Workbench/fr.md) fournit une méthodologie alternative à la [géométrie de construction de solides](Constructive_solid_geometry/fr.md) (CSG en anglais) pour la construction de formes. Pour une discussion détaillée sur l\'atelier Part par rapport à l\'atelier PartDesign, voir [Part et PartDesign](Part_and_PartDesign/fr.md).

![](images/PartDesign_Workbench_Example.jpg )



## Outils

Les outils de PartDesign se situent dans le menu **PartDesign** qui apparaît lorsque l\'atelier PartDesign est chargé.



### Outils d\'assistance de PartDesign 

-   <img alt="" src=images/PartDesign_Body.svg  style="width:32px;"> [Corps](PartDesign_Body/fr.md) : crée un objet [Body](Body/fr.md) dans le document actif et le rend actif.

-   <img alt="" src=images/PartDesign_NewSketch.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Créer une esquisse :

  - ![\|32px](images/PartDesign_NewSketch.svg ) [Esquisse](PartDesign_NewSketch/fr.md) : crée une nouvelle esquisse sur un plan ou une face sélectionnée. Si rien n\'est sélectionné, l\'utilisateur est invité à sélectionner un plan dans le panneau Tâches. L\'interface bascule ensuite vers l\'[atelier Sketcher](Sketcher_Workbench/fr.md) en mode d\'édition d\'esquisse.

  - <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [Ancrer une esquisse](Sketcher_MapSketch/fr.md) : ancre une esquisse à la géométrie sélectionnée dans le corps actif.

  - <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Modifier une esquisse](Sketcher_EditSketch/fr.md) : ouvre l\'esquisse sélectionnée pour la modifier.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Valider une esquisse](Sketcher_ValidateSketch/fr.md) : vérifie la tolérance de différents points et les ajuste.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Vérifier la géométrie](Part_CheckGeometry/fr.md) : vérifie la géométrie des objets sélectionnés pour en détecter les erreurs.

-   <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:32px;"> [Forme liée](PartDesign_ShapeBinder/fr.md) : crée une forme liée référençant la géométrie d\'un seul objet parent.

-   <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:32px;"> [Sous forme liée](PartDesign_SubShapeBinder/fr.md) : crée une forme liée référençant la géométrie d\'un ou plusieurs objets parents.

-   <img alt="" src=images/PartDesign_Clone.svg  style="width:32px;"> [Clone](PartDesign_Clone/fr.md) : crée un clone dans le corps actif.

-   <img alt="" src=images/PartDesign_Plane.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Créer une référence (

  -<img alt="" src=images/PartDesign_Plane.svg  style="width:32px;"> [Plan de référence](PartDesign_Plane/fr.md) : crée un plan de référence dans le corps actif. ({{VersionMinus/fr|1.0}})

  -<img alt="" src=images/PartDesign_Line.svg  style="width:32px;"> [Ligne de référence](PartDesign_Line/fr.md) : crée une ligne de référence dans le corps actif. ({{VersionMinus/fr|1.0}})

  -<img alt="" src=images/PartDesign_Point.svg  style="width:32px;"> [Point de référence](PartDesign_Point/fr.md) : crée un point de référence dans le corps actif. ({{VersionMinus/fr|1.0}})

  -<img alt="" src=images/PartDesign_CoordinateSystem.svg  style="width:32px;"> [Système de coordonnées local](PartDesign_CoordinateSystem/fr.md) : crée un système de coordonnées local attaché à la géométrie de référence dans le corps actif. ({{VersionMinus/fr|1.0}})

:   
    {{Version/fr|1.1}}: ces outils ont été remplacés par de nouveaux [outils de référence](Std_Base/fr#Part_Datums.md).



### Outils de modélisation de PartDesign 



#### Outils additifs 

Ces outils permettent de créer des fonctions de base ou d\'ajouter de la matière à un corps solide existant.

-   <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [Protrusion](PartDesign_Pad/fr.md) : extrude un objet solide à partir de l\'esquisse sélectionnée.

-   <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Révolution](PartDesign_Revolution/fr.md) : crée un solide par révolution d\'une esquisse autour d\'un axe. L\'esquisse doit former un profil fermé.

-   <img alt="" src=images/PartDesign_AdditiveLoft.svg  style="width:32px;"> [Lissage additif](PartDesign_AdditiveLoft/fr.md) : crée un solide en réalisant une transition entre au moins deux esquisses.

-   <img alt="" src=images/PartDesign_AdditivePipe.svg  style="width:32px;"> [Balayage additif](PartDesign_AdditivePipe/fr.md) : crée un solide en balayant une ou plusieurs esquisse(s) le long d\'un chemin ouvert ou fermé.

-   <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width:32px;"> [Hélice additive](PartDesign_AdditiveHelix/fr.md) : crée un solide en balayant une esquisse le long d\'une hélice.

-   <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Créer une primitive additive :

  -<img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:32px;"> [Cube additif](PartDesign_AdditiveBox/fr.md) : crée un cube additif.

  -<img alt="" src=images/PartDesign_AdditiveCylinder.svg  style="width:32px;"> [Cylindre additif](PartDesign_AdditiveCylinder/fr.md) : crée un cylindre additif.

  -<img alt="" src=images/PartDesign_AdditiveSphere.svg  style="width:32px;"> [Sphère additive](PartDesign_AdditiveSphere/fr.md) : crée une sphère additive.

  -<img alt="" src=images/PartDesign_AdditiveCone.svg  style="width:32px;"> [Cône additif](PartDesign_AdditiveCone/fr.md) : crée un cône additif.

  -<img alt="" src=images/PartDesign_AdditiveEllipsoid.svg  style="width:32px;"> [Ellipsoïde additif](PartDesign_AdditiveEllipsoid/fr.md) : crée un ellipsoïde additif.

  -<img alt="" src=images/PartDesign_AdditiveTorus.svg  style="width:32px;"> [Tore additif](PartDesign_AdditiveTorus/fr.md) : crée un tore additif.

  -<img alt="" src=images/PartDesign_AdditivePrism.svg  style="width:32px;"> [Prisme additif](PartDesign_AdditivePrism/fr.md) : crée un prisme additif.

  -<img alt="" src=images/PartDesign_AdditiveWedge.svg  style="width:32px;"> [Pyramide tronquée additive](PartDesign_AdditiveWedge/fr.md) : crée une pyramide tronquée additive.



#### Outils soustractifs 

Ces outils permettent d\'enlever de la matière à un corps solide existant.

-   <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [Cavité](PartDesign_Pocket/fr.md) : crée une cavité à partir de l\'esquisse sélectionnée.

-   <img alt="" src=images/PartDesign_Hole.svg  style="width:32px;"> [Perçage](PartDesign_Hole/fr.md) : crée une fonction perçage à partir de l\'esquisse sélectionnée. L\'esquisse doit contenir un ou plusieurs cercles.

-   <img alt="" src=images/PartDesign_Groove.svg  style="width:32px;"> [Rainure](PartDesign_Groove/fr.md) : crée une rainure par révolution d\'une esquisse sur un axe.

-   <img alt="" src=images/PartDesign_SubtractiveLoft.svg  style="width:32px;"> [Lissage soustractif](PartDesign_SubtractiveLoft/fr.md) : crée un solide en réalisant une transition entre au moins deux esquisses puis la soustrait du corps actif.

-   <img alt="" src=images/PartDesign_SubtractivePipe.svg  style="width:32px;"> [Balayage soustractif](PartDesign_SubtractivePipe/fr.md) : crée un solide en balayant une ou plusieurs esquisse(s) le long d\'un chemin ouvert ou fermé puis le soustrait du corps actif.

-   <img alt="" src=images/PartDesign_SubtractiveHelix.svg  style="width:32px;"> [Hélice soustractive](PartDesign_SubtractiveHelix/fr.md) : crée une forme solide en balayant une esquisse le long d\'une hélice et en la soustrayant du corps actif.

-   <img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Créer une primitive soustractive :

  -<img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width:32px;"> [Cube soustractif](PartDesign_SubtractiveBox/fr.md) : crée un cube soustractif.

  -<img alt="" src=images/PartDesign_SubtractiveCylinder.svg  style="width:32px;"> [Cylindre soustractif](PartDesign_SubtractiveCylinder/fr.md) : crée un cylindre soustractif.

  -<img alt="" src=images/PartDesign_SubtractiveSphere.svg  style="width:32px;"> [Sphère soustractive](PartDesign_SubtractiveSphere/fr.md) : crée une sphère soustractive.

  -<img alt="" src=images/PartDesign_SubtractiveCone.svg  style="width:32px;"> [Cône soustractif](PartDesign_SubtractiveCone/fr.md) : crée un cône soustractif.

  -<img alt="" src=images/PartDesign_SubtractiveEllipsoid.svg  style="width:32px;"> [Ellipsoïde soustractif](PartDesign_SubtractiveEllipsoid/fr.md) : crée un ellipsoïde soustractif.

  -<img alt="" src=images/PartDesign_SubtractiveTorus.svg  style="width:32px;"> [Tore soustractif](PartDesign_SubtractiveTorus/fr.md) : crée un tore soustractif.

  -<img alt="" src=images/PartDesign_SubtractivePrism.svg  style="width:32px;"> [Prisme soustractif](PartDesign_SubtractivePrism/fr.md) : crée un prisme soustractif.

  -<img alt="" src=images/PartDesign_SubtractiveWedge.svg  style="width:32px;"> ‎[Pyramide tronquée soustractive](PartDesign_SubtractiveWedge/fr.md) : crée une pyramide tronquée soustractive.



#### Booléen

-   <img alt="" src=images/PartDesign_Boolean.svg  style="width:32px;"> [Opération booléenne](PartDesign_Boolean/fr.md) : importe un ou plusieurs corps ou PartDesign clones dans le corps actif et applique une opération booléenne.



### Outils de finition 

Ces outils appliquent un traitement aux arêtes ou faces.

-   <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [Congé](PartDesign_Fillet/fr.md) : applique un arrondi/congé sur les arêtes sélectionnées du corps actif.

-   <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [Chanfrein](PartDesign_Chamfer/fr.md) : applique un chanfrein sur les arêtes sélectionnées du corps actif.

-   <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [Dépouille](PartDesign_Draft/fr.md) : applique un angle de dépouille aux faces sélectionnées du corps actif.

-   <img alt="" src=images/PartDesign_Thickness.svg  style="width:32px;"> [Évidement](PartDesign_Thickness/fr.md) : crée une évidement épais à partir du corps actif et ouvre la face sélectionnée.



### Outils de transformation 

Il s\'agit d\'outils permettant de transformer des fonctions existantes.

-   <img alt="" src=images/PartDesign_Mirrored.svg  style="width:32px;"> [Symétrie](PartDesign_Mirrored/fr.md) : symmétrise une ou plusieurs fonctions.

-   <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [Répétition linéaire](PartDesign_LinearPattern/fr.md) : crée une fonction de répétition linéaire d\'une ou plusieurs fonctions.

-   <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> [Répétition circulaire](PartDesign_PolarPattern/fr.md) : crée une fonction de répétition circulaire à partir d\'une ou plusieurs fonctions.

-   <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:32px;"> [Transformation multiple](PartDesign_MultiTransform/fr.md) : crée une combinaison de n\'importe quelle des autres transformations ci-dessus, ainsi que la transformation [Mise à l\'échelle](PartDesign_Scaled/fr.md).
    -   <img alt="" src=images/PartDesign_Scaled.svg  style="width:32px;"> [Mise à l\'échelle](PartDesign_Scaled/fr.md) : met à l\'échelle un ou plusieurs éléments. Ceci n\'est pas disponible en tant qu\'outil de transformation séparé.



#### Extras

Des fonctions supplémentaires se trouvent dans le menu PartDesign :

-   <img alt="" src=images/PartDesign_Sprocket.svg  style="width:32px;"> [Pignon](PartDesign_Sprocket/fr.md) : crée un profil de pignon qui peut être extrudé.

-   <img alt="" src=images/PartDesign_InvoluteGear.svg  style="width:32px;"> [Engrenage à développante](PartDesign_InvoluteGear/fr.md) : crée un profil d\'engrenage à développante qui peut être extrudé.

-   <img alt="" src=images/WizardShaft.svg  style="width:32px;"> [Conception d\'arbre](PartDesign_WizardShaft/fr.md) : génère un arbre à partir d\'un tableau de valeurs et permet d\'analyser les forces et les moments. L\'arbre est construit à partir de la révolution d\'une esquisse qui peut être modifiée.



### Éléments du menu contextuel 

-   [Désactiver](PartDesign_Suppressed/fr.md) : case à cocher pour désactiver une fonction particulière sans la supprimer. {{Version/fr|1.0}}

-   <img alt="" src=images/PartDesign_MoveTip.svg  style="width:32px;"> [Désigner comme fonction résultante](PartDesign_MoveTip/fr.md) : redéfinit la fonction résultante qui est la fonction exposée à l\'extérieur du Corps.

-   <img alt="" src=images/PartDesign_MoveFeature.svg  style="width:32px;"> [Déplacer vers un autre corps](PartDesign_MoveFeature/fr.md) : déplace l\'esquisse, la géométrie de référence ou la fonction sélectionnée vers un autre Corps.

-   <img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width:32px;"> [Déplacer après un autre objet](PartDesign_MoveFeatureInTree/fr.md) : permet de réorganiser l\'arborescence du corps en déplaçant l\'esquisse, la géométrie de référence ou l\'entité sélectionnée vers une autre position dans la liste des entités.



#### Éléments partagés avec l\'atelier Part 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Std Apparence](Std_SetAppearance/fr.md) : détermine l\'apparence de la pièce entière (transparence des couleurs etc\...).

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Couleur par face](Part_ColorPerFace/fr.md) : attribue des couleurs aux faces des pièces.



## Outils obsolètes 

-   <img alt="" src=images/PartDesign_Migrate.svg  style="width:32px;"> [Migrer](PartDesign_Migrate/fr.md) : migre les fichiers des versions de FreeCAD inférieures à 0.17 vers la version 0.17. Cet outil n\'est pas disponible dans la {{VersionPlus/fr|1.0}}.



## Préférences

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Préférences\...](PartDesign_Preferences/fr.md) : préférences disponibles pour les outils PartDesign.
-   [Réglage fin](Fine-tuning/fr.md) : quelques paramètres supplémentaires pour affiner le comportement de PartDesign.



## Tutoriels

-   [Comment utiliser FreeCAD](http://help-freecad-jpg87.fr/00fr/index.php), un site web décrivant le flux de travail de la conception mécanique.
-   [PartDesign Tutoriel pour créer une pièce simple](Creating_a_simple_part_with_PartDesign/fr.md)
-   [PartDesign Tutoriel d\'introduction V0.19](Basic_Part_Design_Tutorial_019/fr.md)
-   [PartDesign Tutoriel pour la conception d\'un support de roulement (I)](PartDesign_Bearingholder_Tutorial_I/fr.md) (nécessite une mise à jour)
-   [PartDesign Tutoriel pour la conception d\'un support de roulement (II)](PartDesign_Bearingholder_Tutorial_II/fr.md) (nécessite une mise à jour)



## Exemples

Pour avoir une idée de ce qui peut être réalisé avec les outils de PartDesign, jetez un coup d\'œil aux [PartDesign Exemples](PartDesign_Examples/fr.md) :

<img alt="" src=images/PartDesign_ExampleSphere-02.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleTorus-01.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExamplePad-09.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSweep-02.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSweep-05.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSpring-04.png  style="width:80px;">





 {{PartDesign_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > PartDesign Workbench/fr
