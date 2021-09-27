# PartDesign project/fr
**
Ce plan de développement est probablement obsolète. Pour plus d'informations, voir [Plan de développement](Development_roadmap/fr.md).<br>
Si vous n'êtes pas impliqué dans le développement discuté ici :<br>
!!! S'IL VOUS PLAÎT, NE MODIFIEZ PAS ET NE TRADUISEZ PAS !!!
**


{{TOCright}}

Voici le plan du projet pour **PartDesign** dans le cadre de la feuille de route de développement ([feuille de route](Development_roadmap/fr.md)).

## But et principes 

Il s\'agit d\'un projet de développement logiciel, visant à mettre en oeuvre les capacités de Part Design. La mise en oeuvre de certaines fonctions des caractéristiques de base dans les modules de CAO de FreeCAD, **Part, PartDesign et Assembly**.

Les étapes de développement sont planifiées et structurées puis écrites dans un journal qui constitue un historique de modifications : [Issue Tracker](http://apps.sourceforge.net/mantisbt/free-cad/my_view_page.php)

## Résultat

L\'objectif du projet, est de permettre à FreeCAD de produire un dessin comme ci dessous.

<img alt="" src=images/Gripper.jpg  style="width:300px;">

Ce résultat est obtenu en utilisant **Sketcher** (Esquisse) et **PartDesign** (Dessin de pièces), pour dessiner des pièces spéciales utiliser **Part**, pour charger un pièce standard tels que **STEP** (par exemple, le palier linéaire). Puis, tout assembler **Assembly** et combiner les contraintes.

Le montage d\'entités (Méthodologie d\'édition d\'opérations) est une réalisation importante, il offre aux utilisateurs une approche intuitive pour accomplir et modifier les opérations. Ceci est très important pour tous les modules et environnements futurs et les compiler dans une interface utilisateur (GUI) la plus cohérente possible !

<img alt="" src=images/TaskPanel.jpg  style="width:400px;">

![](images/CAD_Modeling.gif‎ )

### Sketcher

**Sketcher** est une \"planche\" de dessin avec un solveur de contraintes géométriques, entièrement paramétrable, pour plus de détails, voir la page **[projet Sketcher](Sketcher_project/fr.md)**.

### PartDesign

#### Fonction Corps (Body) 

Une modélisation peut avoir beaucoup d\'étapes pour arriver à sa forme finale, alors un historique est nécessaire. Le résultat final obtenu de la modélisation est le **corps** et constitue un groupe avec l\'historique des opérations.

#### Fonction **Pad feature** 

L\'outil **Pad feature** a pour fonctionnalité d\'extruder une esquisse (ou tout **Object Part2D**) dans sa direction normale. Garantit toujours la création d\'un solide ou échoue.

#### Fonction **Pocket feature** 

L\'outil **Pocket feature** crée une cavité dans un solide de base, de la forme de l'esquisse, avec une profondeur définie, ou débouchant. Garantit aussi toujours la création d\'un solide.

#### Fonction d\'alésage 

Une très bonne définition des paramètres d\'alésage à partir de la spécification NaroCad:

  ----------------------------------------------------------------------- ------------------------------------------------------------------------- -----------------------------------------------------------------------
  <img alt="" src=images/Counterbore_settings.png  style="width:300px;">   <img alt="" src=images/Counterbore_settings2.png  style="width:300px;">   <img alt="" src=images/Countersink_settings.png  style="width:300px;">
  ----------------------------------------------------------------------- ------------------------------------------------------------------------- -----------------------------------------------------------------------

  : **NaroCAD Bore definitions**

#### Modèle

Répliquer un des modèles ci-dessus

##### **Modèle rectangulaire** 

Répliquer une des caractéristiques ci-dessus, le long d\'un modèle x, y

##### **Modèle circulaire** 

Répliquer une des caractéristiques ci-dessus, le long d\'un modèle en coordonnées polaires

##### **Modèle en script** 

Répliquer une des caractéristiques ci-dessus, selon une règle générale fourni sous la forme d\'un script.

## Des idées 

### Ce que font les autres 

-   [SolidWorks examples](http://www.youtube.com/watch?v=cVXQmDStHus)

### Implémentation de modèles 

**Pattern feature class** peut être mis en oeuvre avec un modèle de tableaux et, servir de classe de base pour les fonctions, modèles rectangulaires, circulaires et scriptés.

Ces classes dérivées, n\'auront qu\'à remplir le tableau de répétitions de la classe de base.

Chaque ligne de la table de répétitions de la **Pattern class** de base doit tenir au moins une matrice de transformation, de la caractéristique originale qui doit être répliquée.

En outre, nous pourrions avoir comme option, des règles de transformation comme, par exemple, la manipulation de certaines valeurs de paramètres de la fonction pour être reproduite, (par exemple, afin de créer un motif de perçage avec des rayons différents).

## Organisation

### Hiérarchie des modèles d\'objets 

Cette [UML](http://fr.wikipedia.org/wiki/Unified_Modeling_Language) graphique montre la hiérarchie d\'objets et de ses relations.
Le **jaune** est une classe de base abstraite, le **bleu** et le **gris**, sont ceux qui sont prévu.

<img alt="" src=images/PartDesign_ModlingObjectsHirachy.png  style="width:1000px;">

## Tutoriels

[PartDesign Bearingholder Tutorial I](PartDesign_Bearingholder_Tutorial_I/fr.md)

[PartDesign Bearingholder Tutorial II](PartDesign_Bearingholder_Tutorial_II/fr.md)

## Actions suivantes 

Les actions suivantes sont définies dans **[Mantis roadmap entry for PartDesign](http://www.freecadweb.org/tracker/roadmap_page.php)**

### Corps

Vu la nature paramétrique/associative de la **PartDesign**, nous avons enfin un **corps** (ensemble), qui regroupe, et, organise un historique de la construction. Il contient le résultat final comme une forme, et, a regroupé comme une hiérarchie (parents enfants) les caractéristiques de **PartDesign**. Il définit également l\'entête de l\'historique de la modélisation. Il est aussi liée au [Projet Assemblage](Assembly_project/fr.md) qui est le bloc de construction pour les produits et les composants.

### Opérations additionnelles 

Les fonctions **extrusion** (Pad) et **cavités** (Pocket), sont les outils les plus intéressants de PartDesign. Il ya encore beaucoup de travail à faire, surtout pour la visibilité et le contrôle des manipulateurs visuels. Mais, des fonctionnalités supplémentaires sont nécessaires.

#### Modèles

La fonction de reproduction de modèle, à appliquer sur une fonction **extrusion** ou **cavité** selon, un modèle circulaire ou rectangulaire.
Un bel exemple sur [IronCAD](http://www.ironcad.com/index.php/support/learning-center). **Done \[jrheinlaender\]**

#### Forage

Perçage de trou classique avec tous les paramètres pour le filetage, taraudage, fraisage, chambrage \....

#### Balayage

Balaie une esquisse le long d\'une courbe en vue de créer un solide.

#### Revolution

Faire pivoter une esquisse sur un axe et un angle défini.

## Liste des fonctions à faire 

1.  **Pièce de congé/chanfrein**
    1.  Appliquer l\'opération de congé/chanfrein à différents types de sélection (face/paire de faces/corps entier)\*
2.  **Outil Pad**
    1.  Créer le mode \'jusqu\'au suivant\' **FAIT** \[**mrlukeparry**\]
    2.  Créer le mode \'jusqu\'à la surface/face\' \[**mrlukeparry**\]
    3.  Créer une propriété brouillon pour le pad\' *FAIT*\' \[**mrlukeparry**\]
    4.  Si le tampon est sélectionné sur la face, créer automatiquement une esquisse?
    5.  Créer le mode \'midplane\' **FAIT** \[**jrheinlaender**\]
3.  **Outil Pocket**
    1.  Créez les modes \'jusqu\'à la première\', \'jusqu\'à la dernière\', \'à travers tout\', \'jusqu\'à la surface/face\' **FAIT** \[**jrheinlaender**\]
    2.  Si la poche est sélectionnée sur la face, créer automatiquement une esquisse?
4.  **Part Révolution**
    1.  Autoriser l\'utilisation d\'un segment/axe de ligne générique comme référence
    2.  Créer le mode \'midplane\' **FAIT** \[**jrheinlaender**\]
5.  **Fonction de perçage** Créer une présentation ISO des filetages selon la norme ISO 6410--1 dans un filetage partiel
6.  **Pattern Feature** **FAIT** \[**jrheinlaender**\]
7.  **Fonction de balayage**
8.  **Caractéristique du corps**
9.  **Géométrie de référence**
    1.  Plan
10. **Outil miroir** **FAIT** \[**jrheinlaender**\]
11. **Outil de fonction de copie**



_

---
[documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign project/fr
