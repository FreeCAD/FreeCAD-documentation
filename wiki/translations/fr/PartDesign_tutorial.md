---
 TutorialInfo:r
   Topic: Sketcher
   Level: Débutant
   Time: 15 minutes
   Author: http://freecadweb.org/wiki/index.php?title=User:Drei Drei
   FCVersion: 0.16 ou plus
   Files: 
}}

### Introduction

Ce tutoriel a pour but d\'initier le lecteur à utilisation de l\' Atelier PartDesign. Le lecteur verra comment créer des objets 3D basés sur des esquisses, effectuer des opérations de soustraction et comment répliquer des entités spécifiques dans un modèle.

!{width="480"}

### Prérequis

-   FreeCAD version 0.17 ou supérieure
-   Le lecteur a terminé le tutoriel sur les esquisses

### Procédure

#### Créer une forme géométrique 3D 

L\'objectif de l**\'atelier PartDesign** est de permettre à l\'utilisateur de créer des formes géométriques dans un espace 3D, pour répondre à un certain besoin. Ainsi , sont mis à disposition des outils pour faire des esquisses et les convertir en objets 3D.

Il existe deux outils de base pour y parvenir: !{width="32"} protusion et !{width="32"} Révolution. À coté de leur équivalent de substitution {width="32"} Poche et !{width="32"} Rainure) Ils permettent de faire la plupart des actions usuelles utilisées dans cet atelier.

1.  Aller sur l\'atelier PartDesign
2.  L\'esquisse étant sélectionnée dans l\'arborescence, appuyez sur **File:PartDesign_Body.svg   16px PartDesign_Body/fr**{: mediawiki}, choisissez le plan XY par défaut et appuyez sur **OK**. L\'esquisse doit maintenant apparaître à l\'intérieur du corps.
3.  Sélectionner !{width="32"} Protusion
4.  Renseigner une distance de 5mm
5.  Sélectionnez **Ok**

Une autre manière de créer des formes géométriques 3D est avec l\'outil !{width="32"} éevolution .

!{width="480"}

1.  Créez un nouveau corps **File:PartDesign_Body.svg   16px PartDesign_Body/fr**{: mediawiki}, puis une esquisse basée sur l\'image ci-dessus.
2.  L\'esquisse peut être sur n\'importe quel plan, mais doit coïncider avec l\'axe horizontal.
3.  Sélectionner !{width="32"} Révolution
4.  Définissez \"Axe\" sur \"Axe d\'esquisse horizontal\"
5.  Renseigner un angle de 360°

#### Outils d\'enlèvement de matière 

Commencer par créer une esquisse avec la forme à enlever.

1.  Sélectionner la face supérieure du **pad**
2.  Sélectionner !{width="32"} Nouvelle esquisse
3.  Sélectionner !{width="32"} Géométrie externe
4.  Approcher le bord du pad, un arc devrait apparaître en surbrillance
5.  Sélectionner l\'arc. Un arc de couleur différente devrait apparaître dans l\'esquisse
6.  Créer un cercle centré sur le même point que l\'arc, et renseigner un rayon de 5 mm


{{Message| '''External Geometry'''
Lorsqu'un élément 3D a été créé, il est possible de créer des références à l'intérieur d'une esquisse.
# Sélectionner Image:Sketcher_External.svg Sketcher_External/fr.
#Approcher l'élément à référencer, le bord d'un '''Pad''' par exemple.
# Cliquer dessus
# De nouveaux éléments d'une couleur différente doivent apparaître sur l'esquisse à l'emplacement de la fonction à référencer.
---

# PartDesign tutorial/fr

 
<img alt="" src=images/PartDesign_pocket_exercise.png  style="width:480px;">

Après cela, nous allons utiliser l\'outil **cavité**.

1.  Sélectionner l\'esquisse
2.  Sélectionner <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [Poche](PartDesign_Pocket/fr.md)
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
2.  Sélectionner <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:32px;"> [Transformation multiple](PartDesign_MultiTransform/fr.md)

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

<img alt="" src=images/PartDesign_multitransform_exercise.png  style="width:480px;">

Sinon, rééditer l\'opération MultiTransform en double-cliquant dessus dans l\'arborescence.

Vérifier les deux fonctions de motif pour détecter les modifications nécessaires, telles que l\'axe et si la *\'Direction\'* doit être inversée.

C\'est maintenant terminé la routine de base pour le [PartDesign Workbench](PartDesign_Workbench.md).



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign tutorial/fr
