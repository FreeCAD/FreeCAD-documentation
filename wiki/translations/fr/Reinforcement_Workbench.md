# <img alt="Icône de l\'atelier Reinforcement" src=images/Reinforcement_Workbench.svg  style="width   *64px;"> Reinforcement Workbench/fr


{{TOCright}}

## Introduction

L\'[Atelier Reinforcement](Reinforcement_Workbench/fr.md) est un [Atelier externe](External_workbenches/fr.md) qui fournit des outils pour la génération et le détail des armatures. Cet atelier fournit une interface et des préréglages pour la création de types d\'armatures courants ainsi que des outils pour générer la nomenclature des armatures, la liste de coupe des formes d\'armatures, la nomenclature de pliage des barres et le dessin et la cote des armatures.

Image   *Arch_Rebar_Straight_example.png\|[Armature droite](Arch_Rebar_Straight/fr.md) Image   *Arch_Rebar_UShape_example.png\|[Armature en U](Arch_Rebar_UShape/fr.md) Image   *Arch_Rebar_LShape_example.png\|[Armature en L](Arch_Rebar_LShape/fr.md) Image   *Arch_Rebar_BentShape_example.png\|[Armature cintrée](Arch_Rebar_BentShape/fr.md) Image   *Arch_Rebar_Stirrup_example.png\|[Armature en étrier](Arch_Rebar_Stirrup/fr.md) Image   *Arch_Rebar_Helical_example.png\|[Armature hélicoïdale](Arch_Rebar_Helical/fr.md) Image   *Arch_Rebar_Circular_ColumnReinforcement_example.png\|[Armature circulaire](Arch_Rebar_Circular_ColumnReinforcement/fr.md) Image   *Arch_Rebar_ColumnReinforcement_example.png\|[Armature en colonne](Arch_Rebar_ColumnReinforcement/fr.md) Image   *Arch_Rebar_ColumnReinforcement_TwoTies_example.png\|[Armature 2 cadres 6 barres](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/fr.md) Image   *Arch_Rebar_BeamReinforcement_example.png\|[Poutre](Arch_Rebar_BeamReinforcement/fr.md) Image   *Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png\|[Renforts de dalle](Arch_Rebar_Slab_Reinforcement/fr.md) Image   *Isometric_view_of_Columns_footing.png\|[Renforts de semelle](Arch_Rebar_Footing_Reinforcement/fr.md) Image   *Arch_Rebar_BOM_example.png\|[Nomenclature armature](Arch_Rebar_BOM/fr.md) Image   *Reinforcement_Bar_Shape_Cut_List_example.svg\|[Nomenclature de façonnage des armatures](Reinforcement_Bar_Shape_Cut_List/fr.md) Image   *Reinforcement_Bar_Bending_Schedule_example.svg\|[Tableau des armatures](Reinforcement_Bar_Bending_Schedule/fr.md) Image   *Arch_Rebar_Drawing_Dimensioning_example.svg\|[Dimensions et dessins d\'armatures](Arch_Rebar_Drawing_Dimensioning/fr.md)

## Installation

L\'atelier Reinforcement n\'est pas fourni avec le package FreeCAD par défaut mais peut être facilement installé via le <img alt="" src=images/AddonManager.svg  style="width   *24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md). Pour l\'installer, **Outils → [Gestionnaire d'Addon](Std_AddonMgr/fr.md)**. Le code de l\'atelier Reinforcement est [hébergé et développé sur github](https   *//github.com/amrit3701/FreeCAD-Reinforcement) et peut également être installé manuellement en le copiant dans le répertoire **MOD** de FreeCAD.

## Outils

### Créer des armatures 

-   <img alt="" src=images/Arch_Rebar_Straight.png  style="width   *32px;"> [Armature droite](Arch_Rebar_Straight/fr.md)    * Crée une barre de ferraillage droite dans un élément de structure sélectionné.

-   <img alt="" src=images/Arch_Rebar_UShape.png  style="width   *32px;"> [Armature en U](Arch_Rebar_UShape/fr.md)    * Crée une barre de ferraillage de forme U dans un élément de structure sélectionné.

-   <img alt="" src=images/Arch_Rebar_LShape.png  style="width   *32px;"> [Armature en L](Arch_Rebar_LShape/fr.md)    * Crée une barre de ferraillage de forme L dans un élément de structure sélectionné.

-   <img alt="" src=images/Arch_Rebar_BentShape.png  style="width   *32px;"> [Armature cintrée](Arch_Rebar_BentShape/fr.md)    * Crée une barre de renforcement de forme cintrée dans un élément de structure sélectionné.

-   <img alt="" src=images/Arch_Rebar_Stirrup.png  style="width   *32px;"> [Armature en étrier](Arch_Rebar_Stirrup/fr.md)    * Crée une barre de renforcement d\'étrier dans un élément de structure sélectionné.

-   <img alt="" src=images/Arch_Rebar_Helical.png  style="width   *32px;"> [Armature hélicoïdale](Arch_Rebar_Helical/fr.md)    * Crée une barre de ferraillage hélicoïdale dans un élément de structure sélectionné.

-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width   *32px;"> [Armature circulaire](Arch_Rebar_Circular_ColumnReinforcement/fr.md)    * Crée des armatures dans un élément structurel circulaire de type poteau.

-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width   *32px;"> [Armature en colonne](Arch_Rebar_ColumnReinforcement/fr.md)    * Crée des armatures dans un élément structurel rectangulaire de type poteau.

-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width   *32px;"> [Armature 2 cadres 6 barres](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/fr.md)    * Crée des barres d\'armature dans un élément structurel de type poteau.

-   <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width   *32px;"> [Poutre](Arch_Rebar_BeamReinforcement/fr.md)    * Crée des barres d\'armature dans un élément structurel de type poutre.

-   <img alt="" src=images/Arch_Rebar_Slab_Reinforcement.svg  style="width   *32px;"> [Renfort de dalle](Arch_Rebar_Slab_Reinforcement/fr.md)    * Crée des barres d\'armature dans un élément structurel de dalle sélectionné.

-   <img alt="" src=images/Arch_Rebar_Footing_Reinforcement.svg  style="width   *32px;"> [Renforts de semelle](Arch_Rebar_Footing_Reinforcement/fr.md)   * Crée des barres d\'armature à l\'intérieur d\'un objet Arch Structure Semelle.

-   <img alt="" src=images/Arch_Rebar.svg  style="width   *32px;"> [Armature personnalisée](Arch_Rebar/fr.md)    * Crée une barre de ferraillage personnalisée dans un élément de structure sélectionné à l\'aide d\'une esquisse.

### Informations sur les armatures 

-   <img alt="" src=images/Arch_Rebar_BOM.svg  style="width   *32px;"> [Nomenclature armature](Arch_Rebar_BOM/fr.md)    * Crée la nomenclature des armatures.

-   <img alt="" src=images/Reinforcement_Bar_Shape_Cut_List.svg  style="width   *32px;"> [Nomenclature de façonnage des armatures](Reinforcement_Bar_Shape_Cut_List/fr.md)    * Crée la nomenclature de façonnage des armatures.

-   <img alt="" src=images/Reinforcement_Bar_Bending_Schedule.svg  style="width   *32px;"> [Tableau des armatures](Reinforcement_Bar_Bending_Schedule/fr.md)    * Crée la liste des armatures, types, longueurs, masse.

-   <img alt="" src=images/Arch_Rebar_Drawing_Dimensioning.svg  style="width   *32px;"> [Dimensions et dessins d\'armatures](Arch_Rebar_Drawing_Dimensioning/fr.md)    * Crée dessins et dimensions des armatures.
    -   <img alt="" src=images/Arch_Rebar_Drawing.svg  style="width   *32px;"> [Dessins des armatures](Arch_Rebar_Drawing_Dimensioning/fr#Dessins_des_armatures.md)    * Crée les dessins des armatures.
    -   <img alt="" src=images/Arch_Rebar_Dimensioning.svg  style="width   *32px;"> [Reinforcement Dimensioning](Arch_Rebar_Drawing_Dimensioning#Reinforcement_Dimensioning.md)    * Crée les dimensions des armatures dans les [Dessins des armatures](Arch_Rebar_Drawing_Dimensioning/fr#Dessins_des_armatures.md).




[Category   *Addons](Category_Addons.md) [Category   *External Workbenches](Category_External_Workbenches.md) [Category   *Reinforcement](Category_Reinforcement.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement Workbench/fr
