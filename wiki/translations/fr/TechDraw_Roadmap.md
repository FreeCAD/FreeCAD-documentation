# <img alt="" src=images/preferences-techdraw.svg  style="width:64px;">  TechDraw Roadmap/fr

L\'[atelier Techdraw](TechDraw_Workbench/fr.md) a été officiellement introduit dans FreeCAD en version 0.17.

Voici une feuille de route approximative des domaines à traiter dans le futur (sans ordre particulier).

### Activité en cours 

-   A définir

### À venir 

-   A définir

### Changements récents 

-   A définir

## Futures

### Modèles de navigation 

TechDraw ne prend pas en charge les différents modèles de navigation utilisés dans le reste de FreeCAD (CAO, Blender, etc.).

### HLR vs Face Occlusion 

TechDraw PartViews utilise les algorithmes OCC Hidden Line Removal pour projeter la forme. HLR nécessite beaucoup de calcul, et certaines (beaucoup? La plupart?) des vues ne nécessitent pas l\'affichage de lignes cachées. Une nouvelle méthode de génération de vues est requise. Cela peut nécessiter d\'obtenir l\'image directement à partir de l\'écran 3D.

### coexistence Draft/Arch 

Il existe des incohérences entre la façon dont les ateliers Draft/Arch et TechDraw représentent des formes. Cela limite la pertinence de TechDraw pour les utilisateurs de Draft/Arch. Un inconvénient notable est que TechDraw est incapable d\'appliquer des dimensions aux images Svg qu\'il reçoit de Draft/Arch.

### Modèles

Créer un modèle avec des champs de texte modifiables nécessite une expertise considérable de [SVG](SVG/fr.md) et d\'un éditeur SVG comme Inkscape. Rendre le processus de création de modèles plus simple sera une priorité du cycle de développement de la v0.18.

### Corrections de bogues / demandes de fonctionnalités 

Voir le traqueur de bogues pour des informations à jour.


{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Roadmap/fr
