# TechDraw Roadmap/fr
 <img alt="" src=images/preferences-techdraw.svg  style="width:64px;"> 

L\'atelier [Techdraw](TechDraw_Workbench/fr.md) a été officiellement introduit dans FreeCAD en version 0.17. Il est relativement nouveau et n\'a pas eu les années de développement qui ont profité à d\'autres établis. Néanmoins, TechDraw remplit désormais son objectif de conception initial et peut désormais \"produire des dessins techniques de base basés sur le modèle 3D\".

Voici une feuille de route approximative des domaines à traiter dans le futur (sans ordre particulier).

### Activité Courante 

-   corrections de bugs en préparation de la sortie de la v0.19
-   problèmes d\'utilisation en préparation de la sortie de la v0.19

### À venir 

-   TBD

### Changements Récents 

-   voir ci-dessous

## Modifications pour v0.19 

Voir aussi <https://forum.freecadweb.org/viewtopic.php?f=10&t=34586&hilit=release+notes#p290433>

### Options d\'affichage 

La possibilité de créer une vue à partir d\'une fenêtre 3D ou à partir d\'une géométrie 2D existante.
\'\'\'- une version expérimentale de la création d\'une vue à partir de la fenêtre 3D (Insert Active View) a été implémentée. Cela fonctionne, mais nécessite des développements supplémentaires.

### Conformité aux normes 

TechDraw n\'est pas complètement conforme aux normes. La possibilité de sélectionner une norme de dessin et de faire respecter les différentes particularités est indispensable.
\'\'\'- grâce à \@tpavlicek, les dimensions sont formatées selon une norme et un style sélectionnés.

### GD&T, ControlFrames, Symboles 

Cette zone de TD est faible et doit être mise à niveau.
\'\'\'- grâce à \@fjullien, \@reox et autres, la fonction Ballon a été améliorée pour fournir des fonctionnalités de base dans ce domaine.

### Outils Drawing 

Cela inclut la possibilité d\'ajouter des rappels, des légendes et des surlignages détaillés aux vues. Il s\'agit d\'une condition préalable à de nombreuses améliorations, en particulier dans la zone d\'annotation de dessin, comme les cadres de contrôle des fonctions et les reflets de référence pour les vues de détail.
**- des lignes de repère, une annotation de texte riche, des symboles de soudure, des sommets et des arêtes cosmétiques et des traits d\'axe ont été ajoutés.
**- les lignes individuelles peuvent désormais être masquées, colorées ou stylisées.

### Géométrie 2D 

Un certain nombre de fonctions de géométrie 2D ont récemment été ajoutées au module Pièce. Cela doit être examiné en vue de remplacer le code de géométrie 2D personnalisé dans TechDraw par du code standard de Part.
\'\'\'- ces fonctions 2D sont utilisées dans les nouvelles dimensions conformes aux normes.

### Dimensions \"non-Vertex\" 

Il existe un besoin de dimensions qui ne reposent pas sur des sommets/arêtes spécifiques, mais sur des extrema de la figure - par exemple, la largeur/hauteur globale. Également la possibilité de créer des cotes basées uniquement sur le modèle 3D même s\'il n\'y a pas de géométrie projetée correspondante.
\'\'\'- Les cotes d\'extension permettent de créer une cote qui couvre l\'étendue gauche/droite ou supérieure/inférieure d\'une collection d\'arêtes ou de faces.

## Futures

### Modèles de navigation 

TechDraw ne prend pas en charge les différents modèles de navigation utilisés dans le reste de FreeCAD (CAO, Blender, etc.).

### HLR vs Face Occlusion 

TechDraw PartViews utilise les algorithmes OCC Hidden Line Removal pour projeter la forme. HLR nécessite beaucoup de calcul, et certaines (beaucoup? La plupart?) des vues ne nécessitent pas l\'affichage de lignes cachées. Une nouvelle méthode de génération de vues est requise. Cela peut nécessiter d\'obtenir l\'image directement à partir de l\'écran 3D.

### coexistence Draft/Arch 

Il existe des incohérences entre la façon dont les modules Draft / Arch et TechDraw représentent des formes. Cela limite la pertinence de TechDraw pour les utilisateurs Draft / Arch. Un inconvénient notable est que TechDraw est incapable d\'appliquer des dimensions aux images Svg qu\'il reçoit de Draft / Arch.

### Modèles

Créer un modèle avec des champs de texte modifiables nécessite une expertise considérable de [SVG](SVG/fr.md) et d\'un éditeur SVG comme Inkscape. Rendre le processus de création de modèles plus simple sera une priorité du cycle de développement de la v0.18.

### Corrections de bogues / demandes de fonctionnalités 

Voir le traqueur de bogues pour des informations à jour.


{{TechDraw Tools navi

}}  

[Category:User Documentation](Category:User_Documentation.md) [Category:TechDraw](Category:TechDraw.md)
