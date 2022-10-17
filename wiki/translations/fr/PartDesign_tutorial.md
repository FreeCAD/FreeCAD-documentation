---
- TutorialInfo   */fr
   Topic   * Sketcher
   Level   * Débutant
   Time   * 15 minutes
   Author   *[http   *//freecadweb.org/wiki/index.php?title=User   *Drei Drei]
   FCVersion   *0.16 or above
   Files   *
}}

### Introduction

Ce tutoriel a pour but d\'initier le lecteur à utilisation de l\' [Atelier PartDesign](PartDesign_Workbench/fr.md). Le lecteur verra comment créer des objets 3D basés sur des esquisses, effectuer des opérations de soustraction et comment répliquer des entités spécifiques dans un modèle.

<img alt="" src=images/Sketcher_tutorial_result.png  style="width   *480px;">

### Prérequis

-   FreeCAD version 0.17 ou supérieure
-   Le lecteur a terminé le [tutoriel sur les esquisses](Basic_Sketcher_Tutorial/fr.md)

### Procédure

#### Créer une forme géométrique 3D 

L\'objectif de l**\'atelier PartDesign** est de permettre à l\'utilisateur de créer des formes géométriques dans un espace 3D, pour répondre à un certain besoin. Ainsi , sont mis à disposition des outils pour faire des esquisses et les convertir en objets 3D.

Il existe deux outils de base pour y parvenir   * <img alt="" src=images/PartDesign_Pad.svg  style="width   *32px;"> [protusion](PartDesign_Pad/fr.md) et <img alt="" src=images/PartDesign_Revolution.svg  style="width   *32px;"> [Révolution](PartDesign_Revolution/fr.md). À coté de leur équivalent de substitution (<img alt="" src=images/PartDesign_Pocket.svg  style="width   *32px;"> [Poche](PartDesign_Pocket/fr.md) et <img alt="" src=images/PartDesign_Groove.svg  style="width   *32px;"> [Rainure](PartDesign_Groove/fr.md)) Ils permettent de faire la plupart des actions usuelles utilisées dans cet atelier.

1.  Aller sur l\'atelier PartDesign
2.  L\'esquisse étant sélectionnée dans l\'[arborescence](tree_view/fr.md), appuyez sur **[PartDesign Body](File   *PartDesign_Body.svg   16px]] [[PartDesign_Body/fr.md)**, choisissez le plan XY par défaut et appuyez sur **OK**. L\'esquisse doit maintenant apparaître à l\'intérieur du corps.
3.  Sélectionner <img alt="" src=images/PartDesign_Pad.svg  style="width   *32px;"> [Protusion](PartDesign_Pad/fr.md)
4.  Renseigner une distance de 5mm
5.  Sélectionnez **Ok**

Une autre manière de créer des formes géométriques 3D est avec l\'outil <img alt="" src=images/PartDesign_Revolution.svg  style="width   *32px;"> [éevolution](PartDesign_Revolution/fr.md) .

<img alt="" src=images/PartDesign_revolution_exercise.png  style="width   *480px;">

1.  Créez un nouveau corps **[PartDesign Body](File   *PartDesign_Body.svg   16px]] [[PartDesign_Body/fr.md)**, puis une esquisse basée sur l\'image ci-dessus.
2.  L\'esquisse peut être sur n\'importe quel plan, mais doit coïncider avec l\'axe horizontal.
3.  Sélectionner <img alt="" src=images/PartDesign_Revolution.svg  style="width   *32px;"> [Révolution](PartDesign_Revolution/fr.md)
4.  Définissez \"Axe\" sur \"Axe d\'esquisse horizontal\"
5.  Renseigner un angle de 360°

#### Outils d\'enlèvement de matière 

Commencer par créer une esquisse avec la forme à enlever.

1.  Sélectionner la face supérieure du **pad**
2.  Sélectionner <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width   *32px;"> [Nouvelle esquisse](Sketcher_NewSketch/fr.md)
3.  Sélectionner <img alt="" src=images/Sketcher_External.svg‎‎  style="width   *32px;"> [Géométrie externe](Sketcher_External/fr.md)
4.  Approcher le bord du pad, un arc devrait apparaître en surbrillance
5.  Sélectionner l\'arc. Un arc de couleur différente devrait apparaître dans l\'esquisse
6.  Créer un cercle centré sur le même point que l\'arc, et renseigner un rayon de 5 mm


{{Message| '''External Geometry'''
Lorsqu'un élément 3D a été créé, il est possible de créer des références à l'intérieur d'une esquisse.
# Sélectionner <img src="images/Sketcher_External.svg" width=32px> [Géométrie externe](Sketcher_External/fr.md).
#Approcher l'élément à référencer, le bord d'un '''Pad''' par exemple.
# Cliquer dessus
# De nouveaux éléments d'une couleur différente doivent apparaître sur l'esquisse à l'emplacement de la fonction à référencer.
---

# PartDesign tutorial/fr

 
<img alt="" src=images/PartDesign_pocket_exercise.png  style="width   *480px;">

Après cela, nous allons utiliser l\'outil **cavité**.

1.  Sélectionner l\'esquisse
2.  Sélectionner <img alt="" src=images/PartDesign_Pocket.svg  style="width   *32px;"> [Poche](PartDesign_Pocket/fr.md)
3.  Régler la distance sur **À travers tout**

#### Caractéristiques du motif 

Rappeler le profil extrudé créé au début du tutoriel.

1.  Sélectionner la face supérieure de l\'objet
2.  Créer un nouveau sketch
3.  Créer une géométrie de référence liée au bras de la face
4.  Créer un cercle contraint au centre de l\'arc de référence
5.  Renseigner le rayon à 3 mm
6.  Faire traverser le sketch à travers la pièce encoure

Au lieu de créer un cercle pour chaque trou dans l\'esquisse, Utiliser le concept de *\'Reprodution du motif\'*. Ces outils fonctionnent en reproduisant une caractéristique de la pièce déjà créée à reproduire dans un arrangement linéaire ou circulaire. Utiliser une combinaison de fonctions de motif *\'Linear\' \'et\'* Polar \'\' pour simuler la pièce finale.

1.  Sélectionner la cavité (Pocket) qui vient juste d\'être crée dans la **Vue en arborescence**
2.  Sélectionner <img alt="" src=images/PartDesign_MultiTransform.svg  style="width   *32px;"> [Transformation multiple](PartDesign_MultiTransform/fr.md)

Dans le Combo View, les Transformations \'\' désirées sont présentées.

Noter que dans le menu *\'MultiTransform parameters\'*, FreeCAD a identifié le Pocket comme *\'Original\'* et une deuxième case demande de *\'Cliquer avec le bouton droit\'* pour introduire les caractéristiques du motif.

1.  Faire un clic droit sur la case
2.  Sélectionner *\'Ajouter un motif linéaire\'*
3.  Régler la *\'Direction\'* sur *\'Vertical Sketch Axis\'*
4.  Définir la longueur à 10 mm
5.  Laisser les occurrences à 2
6.  Cliquer sur OK
7.  Cliquer avec le bouton droit de la souris sur la boîte pour ajouter un *\'Motif Polaire\'*. Notez que la vue 3D a maintenant ajouté le motif linéaire.
8.  Définir les occurrences sur 5
9.  Cliquer deux fois sur OK

Après avoir terminé cette tâche, le résultat suivant apparait.

<img alt="" src=images/PartDesign_multitransform_exercise.png  style="width   *480px;">

Sinon, rééditer l\'opération MultiTransform en double-cliquant dessus dans l\'arborescence.

Vérifier les deux fonctions de motif pour détecter les modifications nécessaires, telles que l\'axe et si la *\'Direction\'* doit être inversée.

C\'est maintenant terminé la routine de base pour le [PartDesign Workbench](PartDesign_Workbench.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign tutorial/fr
