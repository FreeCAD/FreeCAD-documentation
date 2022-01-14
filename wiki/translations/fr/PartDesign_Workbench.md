# <img alt="Icône de l\'Atelier PartDesign" src=images/Workbench_PartDesign.svg  style="width:64px;"> PartDesign Workbench/fr


{{TOCright}}

## Introduction

L\'[atelier PartDesign](PartDesign_Workbench/fr.md) <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> fournit des outils avancés pour la modélisation de pièces complexes et solides. Il est principalement axé sur la création de pièces mécaniques pouvant être fabriquées et assemblées dans un produit fini. Néanmoins, les solides créés peuvent en général être utilisés à d\'autres fins, tels que la [conception architecturale](Arch_Workbench/fr.md), l\'[analyse par éléments finis](FEM_Workbench/fr.md) ou l\'[usinage et l\'impression 3D](Path_Workbench/fr.md).

L\'atelier PartDesign est étroitement lié à l\'[atelier Sketcher (Esquisse)](Sketcher_Workbench/fr.md). L\'utilisateur crée normalement une esquisse, puis utilise l\'outil [PartDesign Protrusion](PartDesign_Pad/fr.md) pour l\'extruder et créer un solide de base, ensuite ce solide peut être à nouveau modifié.

Alors que l\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [atelier Part](Part_Workbench/fr.md) est basé sur la méthodologie de [géométrie de construction de solides](constructive_solid_geometry/fr.md) (CSG en anglais: \"Constructive Solid Geometry\") pour la construction de formes, l\'atelier PartDesign utilise une méthodologie paramétrique d\'édition de fonctions, ce qui signifie qu\'un solide de base est transformé de manière séquentielle en lui ajoutant des fonctions jusqu\'à l\'obtention de la forme finale. Voir la page [édition de fonctions](feature_editing/fr.md) pour une explication plus complète de ce processus, puis voir [Créer une pièce simple avec PartDesign](Creating_a_simple_part_with_PartDesign/fr.md) pour commencer à créer des solides.

Une discussion plus détaillée de l\'atelier Part par rapport à l\'atelier Part Design peut être trouvée ici: [Part et Part Design](Part_and_PartDesign/fr.md).

Les corps créés avec PartDesign sont souvent soumis à un [problème de dénomination topologique](Topological_naming_problem/fr.md) qui entraîne le changement de nom des fonctionnalités internes lors de la modification des opérations paramétriques. Ce problème peut être minimisé en suivant les meilleures pratiques décrites dans la page d\'[édition de fonctions](feature_editing/fr.md) et en tirant parti des objets de référence pour la prise en charge des esquisses et des fonctionnalités.

<img alt="" src=images/PartDesign_Example.png  style="width:500px;">

## Outils

Les outils Part Design sont situés dans le menu **Part Design** qui apparaît lorsque l\'atelier Part Design est chargé.

### Outils structure 

Ces outils ne font en fait pas partie de l\'atelier PartDesign. Ils appartiennent au système [Std Base](Std_Base/fr.md). Ils ont été développés en v0.17 avec l\'intention qu\'ils seraient utiles pour organiser un modèle et créer des assemblages ; en tant que tels, ils sont très utiles lorsque vous travaillez avec des corps créés avec cet atelier.

-   <img alt="" src=images/Std_Part.svg  style="width:32px;"> [Pièce](Std_Part/fr.md): ajoute un conteneur Pièce dans le document actif et le rend actif.

-   <img alt="" src=images/Std_Group.svg  style="width:32px;"> [Groupe](Std_Group/fr.md): ajoute un Groupe dans l\'arborescence du document actif, qui permet d\'organiser les objets dans la [vue arborescence](Tree_view/fr.md).

### Outils d\'assistance Part Design 

-   <img alt="" src=images/PartDesign_Body.svg  style="width:32px;"> [Corps](PartDesign_Body/fr.md) : crée un objet [Body](Body/fr.md) dans le document actif et le rend actif.

-   ![\|32px](images/Sketcher_NewSketch.svg ) [Esquisse](PartDesign_NewSketch/fr.md) : crée une nouvelle esquisse sur un plan ou une face sélectionnée. Si rien n\'est sélectionné, l\'utilisateur est invité à sélectionner un plan dans le panneau Tâches. L\'interface bascule ensuite vers l\'[atelier Sketcher](Sketcher_Workbench/fr.md) en mode d\'édition d\'esquisse.

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Modifier l\'esquisse](Sketcher_EditSketch/fr.md) : édite l\'esquisse sélectionnée.

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [Appliquer une esquisse sur une face](Sketcher_MapSketch/fr.md) : applique une esquisse sur une face ou un plan sélectionné du corps actif.

### Outils de modélisation Part Design 

#### Outils de référence 

-   <img alt="" src=images/PartDesign_Point.svg  style="width:32px;"> [Point de référence](PartDesign_Point/fr.md) : crée un point de référence dans le corps actif.

-   <img alt="" src=images/PartDesign_Line.svg  style="width:32px;"> [Ligne de référence](PartDesign_Line/fr.md) : crée une ligne de référence (droite) dans le corps actif.

-   <img alt="" src=images/PartDesign_Plane.svg  style="width:32px;"> [Plan de référence](PartDesign_Plane/fr.md) : crée un plan de référence dans le corps actif.

-   <img alt="" src=images/PartDesign_CoordinateSystem.svg  style="width:32px;"> [Système de coordonnées local](PartDesign_CoordinateSystem/fr.md) : crée un système de coordonnées local attaché à la géométrie de référence dans le corps actif.

-   <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:32px;"> [Forme liée](PartDesign_ShapeBinder/fr.md) : crée une forme liée dans le corps actif.

-   <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:32px;"> [Sous forme liée](PartDesign_SubShapeBinder/fr.md): crée une forme liée à un sous-élément comme le bord ou la face d\'un autre corps tout en conservant la position relative de cet élément. {{Version/fr|0.19}}

-   <img alt="" src=images/PartDesign_Clone.svg  style="width:32px;"> [Clone](PartDesign_Clone/fr.md) : crée un clone dans le corps actif.

#### Outils additifs 

Ces outils permettent de créer des fonctions de base ou d\'ajouter de la matière à un corps solide existant.

-   <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [Protrusion](PartDesign_Pad/fr.md) : extrude un objet solide à partir de l\'esquisse sélectionnée.

-   <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Révolution](PartDesign_Revolution/fr.md) : crée un solide par révolution d\'une esquisse autour d\'un axe. L\'esquisse doit former un profil fermé.

-   <img alt="" src=images/PartDesign_AdditiveLoft.svg  style="width:32px;"> [Lissage additif](PartDesign_AdditiveLoft/fr.md) : crée un solide en réalisant une transition entre au moins deux esquisses.

-   <img alt="" src=images/PartDesign_AdditivePipe.svg  style="width:32px;"> [Balayage additif](PartDesign_AdditivePipe/fr.md) : crée un solide en balayant une ou plusieurs esquisse(s) le long d\'un chemin ouvert ou fermé.

-   <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width:32px;"> [Hélice additive](PartDesign_AdditiveHelix/fr.md): crée un solide en balayant une esquisse le long d\'une hélice. {{Version/fr|0.19}}

-   <img alt="" src=images/PartDesign_CompPrimitiveAdditive.png  style="width:48px;"> [Créer une primitive additive](PartDesign_CompPrimitiveAdditive/fr.md) : ajoute une primitive additive dans le corps actif.

:\*<img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:32px;"> [Cube additif](PartDesign_AdditiveBox/fr.md) : crée un cube additif.

:\*<img alt="" src=images/PartDesign_AdditiveCone.svg  style="width:32px;"> [Cône additif](PartDesign_AdditiveCone/fr.md) : crée un cône additif.

:\*<img alt="" src=images/PartDesign_AdditiveCylinder.svg  style="width:32px;"> [Cylindre additif](PartDesign_AdditiveCylinder/fr.md) : crée un cylindre additif.

:\*<img alt="" src=images/PartDesign_AdditiveEllipsoid.svg  style="width:32px;"> [Ellipsoïde additif](PartDesign_AdditiveEllipsoid/fr.md) : crée un ellipsoïde additif.

:\*<img alt="" src=images/PartDesign_AdditivePrism.svg  style="width:32px;"> [Prisme additif](PartDesign_AdditivePrism/fr.md) : crée un prisme additif.

:\*<img alt="" src=images/PartDesign_AdditiveSphere.svg  style="width:32px;"> [Sphère additive](PartDesign_AdditiveSphere/fr.md) : crée une sphère additive.

:\*<img alt="" src=images/PartDesign_AdditiveTorus.svg  style="width:32px;"> [Tore additif](PartDesign_AdditiveTorus/fr.md) : crée un tore additif.

:\*<img alt="" src=images/PartDesign_AdditiveWedge.svg  style="width:32px;"> [Pyramide tronquée additive](PartDesign_AdditiveWedge/fr.md) : crée une pyramide tronquée additive.

#### Outils soustractifs 

Ces outils permettent d\'enlever de la matière à un corps solide existant.

-   <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [Cavité](PartDesign_Pocket/fr.md) : crée une cavité à partir de l\'esquisse sélectionnée.

-   <img alt="" src=images/PartDesign_Hole.svg  style="width:32px;"> [Perçage](PartDesign_Hole/fr.md) : crée une fonction perçage à partir de l\'esquisse sélectionnée. L\'esquisse doit contenir un ou plusieurs cercles.

-   <img alt="" src=images/PartDesign_Groove.svg  style="width:32px;"> [Rainure](PartDesign_Groove/fr.md): crée une rainure par révolution d\'une esquisse sur un axe.

-   <img alt="" src=images/PartDesign_SubtractiveLoft.svg  style="width:32px;"> [Lissage soustractif](PartDesign_SubtractiveLoft/fr.md) : crée un solide en réalisant une transition entre au moins deux esquisses puis la soustrait du corps actif.

-   <img alt="" src=images/PartDesign_SubtractivePipe.svg  style="width:32px;"> [Balayage soustractif](PartDesign_SubtractivePipe/fr.md) : crée un solide en balayant une ou plusieurs esquisse(s) le long d\'un chemin ouvert ou fermé puis le soustrait du corps actif.

-   <img alt="" src=images/PartDesign_SubtractiveHelix.svg  style="width:32px;"> [Hélice soustractive](PartDesign_SubtractiveHelix/fr.md): crée une forme solide en balayant une esquisse le long d\'une hélice et en la soustrayant du corps actif. {{Version/fr|0.19}}

-   <img alt="" src=images/PartDesign_CompPrimitiveSubtractive.png  style="width:48px;"> [Créer une primitive soustractive](PartDesign_CompPrimitiveSubtractive/fr.md) : soustrait une primitive du corps actif.

:\*<img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width:32px;"> [Cube soustractif](PartDesign_SubtractiveBox/fr.md) : crée un cube soustractif.

:\*<img alt="" src=images/PartDesign_SubtractiveCone.svg  style="width:32px;"> [Cône soustractif](PartDesign_SubtractiveCone/fr.md) : crée un cône soustractif.

:\*<img alt="" src=images/PartDesign_SubtractiveCylinder.svg  style="width:32px;"> [Cylindre soustractif](PartDesign_SubtractiveCylinder/fr.md) : crée un cylindre soustractif.

:\*<img alt="" src=images/PartDesign_SubtractiveEllipsoid.svg  style="width:32px;"> [Ellipsoïde soustractif](PartDesign_SubtractiveEllipsoid/fr.md) : crée un ellipsoïde soustractif.

:\*<img alt="" src=images/PartDesign_SubtractivePrism.svg  style="width:32px;"> [Prisme soustractif](PartDesign_SubtractivePrism/fr.md) : crée un prisme soustractif.

:\*<img alt="" src=images/PartDesign_SubtractiveSphere.svg  style="width:32px;"> [Sphère soustractive](PartDesign_SubtractiveSphere/fr.md) : crée une sphère soustractive.

:\*<img alt="" src=images/PartDesign_SubtractiveTorus.svg  style="width:32px;"> [Tore soustractif](PartDesign_SubtractiveTorus/fr.md) : crée un tore soustractif.

:\*<img alt="" src=images/PartDesign_SubtractiveWedge.svg  style="width:32px;"> ‎[Pyramide tronquée soustractive](PartDesign_SubtractiveWedge/fr.md) : crée une pyramide tronquée soustractive.

#### Outils de transformation 

Ces outils permettent d\'appliquer une transformation au moyen de fonctions existantes. Elles vous permettront de choisir quelles fonctions utiliser.

-   <img alt="" src=images/PartDesign_Mirrored.svg  style="width:32px;"> [Symétrie](PartDesign_Mirrored/fr.md) : crée une fonction de symétrie par rapport à un plan ou une face.

-   <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [Répétition linéaire](PartDesign_LinearPattern/fr.md) : crée une fonction de répétition linéaire basée sur une ou plusieurs fonctions.

-   <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> [Répétition circulaire](PartDesign_PolarPattern/fr.md) : Crée une fonction de répétition circulaire à partir d\'une ou plusieurs fonctions.

-   <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:32px;"> [Transformation multiple](PartDesign_MultiTransform/fr.md) : crée une combinaison de n\'importe quelle des autres transformations.

#### Outils d\'habillage 

Ces outils appliquent un traitement aux arêtes ou faces sélectionnées.

-   <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [Congé](PartDesign_Fillet/fr.md) : applique un arrondi/congé sur les arêtes sélectionnées du corps actif.

-   <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [Chanfrein](PartDesign_Chamfer/fr.md) : applique un chanfrein sur les arêtes sélectionnées du corps actif.

-   <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [Dépouille](PartDesign_Draft/fr.md) : applique un angle de dépouille aux faces sélectionnées du corps actif.

-   <img alt="" src=images/PartDesign_Thickness.svg  style="width:32px;"> [Épaisseur](PartDesign_Thickness/fr.md) : évide le corps actif et le transforme en un objet creux à paroi épaisse en creusant la (ou les) face(s) sélectionnée(s).

#### Booléen

-   <img alt="" src=images/PartDesign_Boolean.svg  style="width:32px;"> [Opération Booléenne](PartDesign_Boolean/fr.md) : importe un ou plusieurs corps ou clones PartDesign dans le corps actif et applique une opération Booléenne.

#### Extras

Des fonctionnalités supplémentaires se trouvent dans le menu Part Design :

-   <img alt="" src=images/PartDesign_Migrate.svg  style="width:32px;"> [Migrer](PartDesign_Migrate/fr.md) : migre des fichiers créés dans des versions antérieures de FreeCAD. Si le fichier ne contient que des fonctions PartDesign, la migration devrait réussir. Si le fichier contient des objets mixtes Part/Part Design/Draft, la conversion échouera presque certainement.

-   <img alt="" src=images/PartDesign_Sprocket.svg  style="width:32px;"> [Pignon](PartDesign_Sprocket/fr.md): crée un profil de pignon qui peut être extrudé. {{Version/fr|0.19}}

-   <img alt="" src=images/PartDesign_InternalExternalGear.svg  style="width:32px;"> [Engrenage en développante](PartDesign_InvoluteGear/fr.md) : crée un profil d\'engrenage en développante qui peut être extrudé.

-   <img alt="" src=images/WizardShaft.svg  style="width:32px;"> [ Assistant de conception d\'arbre](PartDesign_WizardShaft/fr.md) : génère un arbre à partir d\'un tableau de valeurs et permet d\'analyser les forces et les moments. L\'arbre est construit à partir de la révolution d\'une esquisse qui peut être modifiée.

### Éléments du menu contextuel 

-   <img alt="" src=images/PartDesign_MoveTip.svg  style="width:32px;"> [Désigner comme fonction résultante](PartDesign_MoveTip/fr.md): redéfinit la fonction résultante qui est la fonction exposée à l\'extérieur du Corps.

-   <img alt="" src=images/PartDesign_MoveFeature.svg  style="width:32px;"> [Déplacer vers un autre corps](PartDesign_MoveFeature/fr.md): déplace l\'esquisse, la géométrie de référence ou la fonction sélectionnée vers un autre Corps.

-   <img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width:32px;"> [Déplacer après un autre objet](PartDesign_MoveFeatureInTree/fr.md): permet de réorganiser l\'arborescence du corps en déplaçant l\'esquisse, la géométrie de référence ou l\'entité sélectionnée vers une autre position dans la liste des entités.

#### Éléments partagés avec l\'atelier Part 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Std Apparence](Std_SetAppearance/fr.md): détermine l\'apparence de la pièce entière (transparence des couleurs etc\...).

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Part Définir les couleurs](Part_FaceColors/fr.md): attribue des couleurs aux faces des pièces.

## Préférences

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Préférences\...](PartDesign_Preferences/fr.md): préférences disponibles pour les outils PartDesign.
-   [Réglage fin](Fine-tuning/fr.md): quelques paramètres supplémentaires pour affiner le comportement de PartDesign.

## Tutoriels

-   [Comment utiliser FreeCAD](http://help-freecad-jpg87.fr/00fr/index.php), un site web décrivant le flux de travail de la conception mécanique.
-   [Créer une pièce simple avec PartDesign](Creating_a_simple_part_with_PartDesign/fr.md)
-   [Tutoriel d\'introduction PartDesign](Basic_Part_Design_Tutorial/fr.md)
-   [Conception Support de Roulement Tutoriel I](PartDesign_Bearingholder_Tutorial_I/fr.md) (nécessite une mise à jour)
-   [Tutoriel de Conception de Support de Roulement II](PartDesign_Bearingholder_Tutorial_II/fr.md) (nécessite une mise à jour)





 {{PartDesign Tools navi}}

[<img src="images/Property.png" style="width:16px"> Workbenches](Category_Workbenches.md)

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > PartDesign Workbench/fr
