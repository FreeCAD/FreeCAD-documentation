# Defeaturing Workbench/fr

 <img alt="Icône de l\'atelier Defeaturing" src=images/Defeaturing_workbench_icon.svg  style="width:128px;">

## Introduction


{{TOCright}}

L\'<img alt="" src=images/Defeaturing_workbench_icon.svg  style="width:24px;"> [Atelier Defeaturing](Defeaturing_Workbench/fr.md) est un atelier complémentaire destiné à l\'édition de modèles STEP, en supprimant des fonctionnalités sélectionnées sur le modèle. C\'est un [atelier externe](External_workbenches/fr.md) et ne fait pas partie de l\'installation standard de FreeCAD.

## Fonctionnalités

-   Comprend un ensemble d\'outils pour éditer une forme ou un modèle STEP, en supprimant le(s) trou(s), face(s), en simplifiant le modèle, en modifiant la tolérance, en appliquant des opérations booléennes floues, etc.
-   Il existe également des outils pour créer des formes plus solides, à partir de bord(s), de face(s) ou de coque(s).
-   Il est également possible d\'utiliser la modélisation directe du modèle, lorsque l\'historique des opérations n\'est pas disponible. (C\'est le cas pour les modèles 3D STEP).
-   Utile dans des situations pour supprimer rapidement les détails propriétaires du modèle avant de le partager. Voir [Defeaturing](Defeaturing/fr.md)

Remarque: davantage d\'outils avancés de Defeaturing pourront être utilisés si [OCC7.3](OpenCASCADE/fr.md) est disponible.

## Installation

### Installation automatique (recommandé) 

Utilisation de FreeCAD <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) disponible dans v0.17 + via **Outils → Gestionnaire d'Addon**. Recherchez l\'icône <img alt="" src=images/Defeaturing_workbench_icon.svg  style="width:24px;"> Defeaturing workbench. Le Gestionnaire d\'Addon complémentaires informe également l\'utilisateur lorsqu\'une nouvelle version de cet Addon complémentaire est disponible.

### Manuellement

Voir [Comment installer un atelier supplémentaire](How_to_install_additional_workbenches/fr.md)

### Versions supportées 

-   FreeCAD v0.15 4671
-   FreeCAD v0.16 \>= 6712
-   FreeCAD v0.17 \>= 13522
-   FreeCAD v0.18+

## Références

-   Auteur : Github : [\@easyw](https://github.com/easyw) \| FreeCAD Forums: [1](https://forum.freecadweb.org/viewtopic.php?f=9&t=29506)
-   Code source sur Github : <https://github.com/easyw/Defeaturing_WB>
-   Fil du forum <https://forum.freecadweb.org/viewtopic.php?t=29506>

## Outils

![Boîte de dialogue Defeaturing](images/Defeaturing_WB.png )

<img alt="" src=images/Defeaturing_Tools.svg  style="width:32px;"> Les outils de Defeaturing sont situés dans un cache séparé.

-   <img alt="" src=images/DefeatWB_Tools_rmv_hole.png  style="width:32px;"> [Remove Holes](DefeatWB_Tools_rmv_hole.png.md) : enlève un trou d\'une face
-   <img alt="" src=images/DefeatWB_Tools_rmv_listed_Faces.png  style="width:32px;"> [Remove listed Faces](DefeatWB_Tools_rmv_listed_Faces.md) : enlève les faces d\'une liste.
-   <img alt="" src=images/DefeatWB_Tools_add_Faces_listed_Edges.png  style="width:32px;"> [Add Faces from \'in List\' Edges](DefeatWB_Tools_add_Faces_listed_Edges.md) : ajoute des faces dans une liste de fil.
-   <img alt="" src=images/DefeatWB_Tools_select_Faces_Param_Defeat.png  style="width:32px;"> [Select Faces to be Parametric defeatured](DefeatWB_Tools_select_Faces_Param_Defeat.md) : sélection de faces pour être défaite paramétriquement.
-   <img alt="" src=images/DefeatWB_Tools_create_copy_listed_edges.png  style="width:32px;"> [Create a copy of the \'in List\' Edges ](DefeatWB_Tools_create_copy_listed_edges.md) : Crée une copie d\'une liste de fils.

-   <img alt="" src=images/DefeatWB_Tools_copy_Faces_listed_faces.png  style="width:32px;"> [copy Faces from \'in List\' Faces ](DefeatWB_Tools_copy_Faces_listed_faces.md) : copie des faces à partir d\'une liste de faces.
-   <img alt="" src=images/DefeatWB_Tools_offset_face.png  style="width:32px;"> [ offset face](DefeatWB_Tools_offset_face.md) : déplace une face.
-   <img alt="" src=images/DefeatWB_Tools_offset_edge.png  style="width:32px;"> [offset edge](DefeatWB_Tools_offset_edge.md) : déplace un fil.

-   <img alt="" src=images/DefeatWB_Tools_make_solid_listed_faces.png  style="width:32px;"> [Make Solid from in List Faces](DefeatWB_Tools_make_solid_listed_faces.md) : crée un solide avec une liste de faces.
-   <img alt="" src=images/DefeatWB_Tools_make_solid_faces_selected_objects.png  style="width:32px;"> [Make Solid from the Faces of the selected Objects](DefeatWB_Tools_make_solid_faces_selected_objects.md) : crée un solide avec des faces des objets sélectionnés.
-   <img alt="" src=images/DefeatWB_Tools_select_one_object_2_make_solid_step_proc.png  style="width:32px;"> [Make Solid from in List Faces](DefeatWB_Tools_select_one_object_2_make_solid_step_proc.md) : sélectionnez un objet solide pour tenter de créer un objet STEP destiné à être importé/exporté.
-   <img alt="" src=images/DefeatWB_Tools_Connect.png  style="width:32px;"> [Connect](DefeatWB_Tools_Connect.md) : connexion.
-   <img alt="" src=images/DefeatWB_Tools_clean_face_rmv_holes.png  style="width:32px;"> [clean Face(s) removing holes and merging Outwire](DefeatWB_Tools_clean_face_rmv_holes.md) : nettoie une face(s) efface les trous et fusionne les fils.

-   <img alt="" src=images/DefeatWB_Tools_show_listed_edges.png  style="width:32px;"> [show \'in List' Edge(s)](DefeatWB_Tools_show_listed_edges.md) : affiche une liste de fil(s).
-   <img alt="" src=images/DefeatWB_Tools_show_listed_faces.png  style="width:32px;"> [show \'in List' Face(s)](DefeatWB_Tools_show_listed_faces.md) : affiche une liste de face(s).
-   <img alt="" src=images/DefeatWB_Tools_refine.png  style="width:32px;"> [refine](DefeatWB_Tools_refine.md) : affine.
-   <img alt="" src=images/DefeatWB_Tools_simple_copy.png  style="width:32px;"> [simple copy](DefeatWB_Tools_simple_copy.md) : simple copie
-   <img alt="" src=images/DefeatWB_Tools_parametric_refine.png  style="width:32px;"> [parametric Refine](DefeatWB_Tools_parametric_refine.md) : affinage paramétrique.

-   <img alt="" src=images/DefeatWB_Tools_geometry_check.png  style="width:32px;"> [geometry check](DefeatWB_Tools_geometry_check.md) : valide la géométrie.
-   <img alt="" src=images/DefeatWB_Tools_get_Tolerance_value.png  style="width:32px;"> [get Tolerance value](DefeatWB_Tools_get_Tolerance_value.md) : cherche une valeur de tolérance.
-   <img alt="" src=images/DefeatWB_Tools_set_Tolerance_value.png  style="width:32px;"> [set Tolerance value](DefeatWB_Tools_set_Tolerance_value.md) : donner une valeur de tolérance.

-   <img alt="" src=images/DefeatWB_Tools_make_edges_selected_vertexes.png  style="width:32px;"> [make Edge from selected Vertexes](DefeatWB_Tools_make_edges_selected_vertexes.md) : crée une ligne avec les vertex sélectionnés.
-   <img alt="" src=images/DefeatWB_Tools_reset_placement.png  style="width:32px;"> [reset Placement](DefeatWB_Tools_reset_placement.md): réinitialise le placement
-   <img alt="" src=images/DefeatWB_Tools_show_hide_typeId_shape.png  style="width:32px;"> [show/hide TypeId of the Shape](DefeatWB_Tools_show_hide_typeId_shape.md) : affiche/cache les type Id du profil.
-   <img alt="" src=images/DefeatWB_Tools_help.png  style="width:32px;"> [help](DefeatWB_Tools_help.md): aide

-   <img alt="" src=images/DefeatWB_Tools_Fuzzy_Cut.png  style="width:32px;"> [Fuzzy Cut](DefeatWB_Tools_Fuzzy_Cut.md): Coupe approximative
-   <img alt="" src=images/DefeatWB_Tools_Fuzzy_Union.png  style="width:32px;"> [Fuzzy Union](DefeatWB_Tools_Fuzzy_Union.md): Union approximative
-   <img alt="" src=images/DefeatWB_Tools_Fuzzy_Common.png  style="width:32px;"> [Fuzzy Common](DefeatWB_Tools_Fuzzy_Common.md): Intersection approximative

## Tutoriels vidéo 

### Déconstruction

Fonction enlèvement utilisant le nouvel outil OCC7.3

[480px\|left\|thumb \|link=<https://raw.githubusercontent.com/easyw/FreeCAD-tutorials/master/testing-files/removing-holes.mp4%7CAtelier> Defeaturing - Les fonctions suppression (trous)](Image:Defeaturing-WB-@Work_v3.png.md)

[480px\|left\|thumb \|link=<https://youtu.be/yrTtWFakAyE> \|alt=Defeaturing-WB-\@Work\|YouTube: outils Defeaturing - Simplification du modèle](Image:Defeaturing-WB-@Work_v1.png.md)

[480px\|left\|thumb \|link=<https://youtu.be/vgQwGI6Fk6Q%7CYouTube>: Outils Defeaturing - Sélection de plusieurs faces pour être défaites](Image:Defeaturing-WB-@Work_v2.png.md)

[480px\|left\|thumb \|link=<https://raw.githubusercontent.com/easyw/FreeCAD-tutorials/master/testing-files/removing-fillet-chamfer.mp4%7CAtelier> Defeaturing - Supprimer chanfrein filet](Image:Defeaturing-WB-@Work_v4.png.md)

[480px\|left\|thumb \|link=<https://peertube.mastodon.host/videos/watch/c6bc5abd-2eb7-48c7-af67-c4d8e6783872%7CAtelier> Defeaturing - Vue d\'ensemble des fonctions (en langue allemande)](Image:Defeaturing-WB-@Work_v5.png.md)

[480px\|left\|thumb \|link=<https://raw.githubusercontent.com/easyw/FreeCAD-tutorials/master/testing-files/parametric-defeaturing.mp4%7CAtelier> Defeaturing - Déconstruction paramétrique](Image:Defeaturing-WB-@Work_v6.png.md) 

### Réparation

-   Coudre une forme
-   Supprimer ou simplifier les faces
-   Retirer les trous ou les poches
-   Lire ou modifier la tolérance
-   Faire des opérations booléennes approximatives

## Ateliers externes 

Les ateliers FreeCAD sont faciles à programmer en [ Python](Python/fr.md), de ce fait, beaucoup de personnes développent des ateliers supplémentaires en dehors des développeurs principaux de FreeCAD.

La page des [ateliers externes](External_workbenches/fr.md) contient des informations et des tutoriels sur certains d'entre eux et le projet [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) vise à les rassembler et à les rendre facilement installables depuis FreeCAD.

De nouveaux ateliers sont en développement, restez à l\'écoute !


 

[Category:Addons](Category:Addons.md) [Category:External Workbenches](Category:External_Workbenches.md)
