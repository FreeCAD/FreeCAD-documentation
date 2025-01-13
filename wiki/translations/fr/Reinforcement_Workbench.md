# <img alt="Icône de l\'atelier Reinforcement" src=images/Reinforcement_Workbench.svg  style="width:64px;"> Reinforcement Workbench/fr




## Introduction

L\'[atelier Reinforcement](Reinforcement_Workbench/fr.md) est un [atelier externe](External_workbenches/fr.md) qui fournit des outils pour la génération et le détail des armatures. Cet atelier fournit une interface et des préréglages pour la création de types d\'armatures courants ainsi que des outils pour générer la nomenclature des armatures, la liste de coupe des formes d\'armatures, la nomenclature de pliage des barres et le dessin et la cote des armatures.

Image:Arch_Rebar_Straight_example.png\|[Armature droite](Reinforcement_StraightRebar/fr.md) Image:Arch_Rebar_UShape_example.png\|[Armature en U](Reinforcement_UShapeRebar/fr.md) Image:Arch_Rebar_LShape_example.png\|[Armature en L](Reinforcement_LShapeRebar/fr.md) Image:Arch_Rebar_Stirrup_example.png\|[Armature en étrier](Reinforcement_StirrupRebar/fr.md) Image:Arch_Rebar_BentShape_example.png\|[Armature cintrée](Reinforcement_BentShapeRebar/fr.md) Image:Arch_Rebar_Helical_example.png\|[Armature hélicoïdale](Reinforcement_HelicalRebar/fr.md) Image:Arch_Rebar_ColumnReinforcement_example.png\|[Armature en colonne](Reinforcement_ColumnRebars/fr.md) Image:Arch_Rebar_ColumnReinforcement_TwoTies_example.png\|[Armature 2 cadres 6 barres](Reinforcement_ColumnRebars_TwoTiesSixRebars/fr.md) Image:Arch_Rebar_Circular_ColumnReinforcement_example.png\|[Armature circulaire](Reinforcement_ColumnRebars_Circular/fr.md) Image:Arch_Rebar_BeamReinforcement_example.png\|[Poutre](Reinforcement_BeamRebars/fr.md) Image:Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png\|[Renforts de dalle](Reinforcement_SlabRebars/fr.md) Image:Isometric_view_of_Columns_footing.png\|[Renforts de semelle](Reinforcement_FootingRebars/fr.md) Image:Arch_Rebar_BOM_example.png\|[Nomenclature armature](Reinforcement_BillOfMaterial/fr.md) Image:Reinforcement_Bar_Shape_Cut_List_example.svg\|[Nomenclature de façonnage des armatures](Reinforcement_BarShapeCutList/fr.md) Image:Reinforcement_Bar_Bending_Schedule_example.svg\|[Plan de cintrage](Reinforcement_BarBendingSchedule/fr.md) Image:Arch_Rebar_Drawing_Dimensioning_example.svg\|[Dimensions et dessins d\'armatures](Reinforcement_DrawingDimensioning/fr.md)



## Installation

L\'atelier Reinforcement n\'est pas fourni avec le package FreeCAD par défaut mais peut être facilement installé via le <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Gestionnaire des extensions](Std_AddonMgr/fr.md). Pour l\'installer, **Outils → [Gestionnaire des extensions](Std_AddonMgr/fr.md)**. Le code de l\'atelier Reinforcement est [hébergé et développé sur github](https://github.com/amrit3701/FreeCAD-Reinforcement) et peut également être installé manuellement en le copiant dans le répertoire **MOD** de FreeCAD.



## Outils



### Créer des armatures 

-   <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Armature personnalisée](Arch_Rebar/fr.md) : crée une barre de ferraillage personnalisée dans un élément de structure sélectionné à l\'aide d\'une esquisse.

-   <img alt="" src=images/Reinforcement_StraightRebar.svg  style="width:32px;"> [Armature droite](Reinforcement_StraightRebar/fr.md) : crée une barre de ferraillage droite dans un élément de structure sélectionné.

-   <img alt="" src=images/Reinforcement_UShapeRebar.svg  style="width:32px;"> [Armature en U](Reinforcement_UShapeRebar/fr.md) : crée une barre de ferraillage de forme U dans un élément de structure sélectionné.

-   <img alt="" src=images/Reinforcement_LShapeRebar.svg  style="width:32px;"> [Armature en L](Reinforcement_LShapeRebar/fr.md) : crée une barre de ferraillage de forme L dans un élément de structure sélectionné.

-   <img alt="" src=images/Reinforcement_StirrupRebar.svg  style="width:32px;"> [Armature en étrier](Reinforcement_StirrupRebar/fr.md) : crée une barre de renforcement d\'étrier dans un élément de structure sélectionné.

-   <img alt="" src=images/Reinforcement_BentShapeRebar.svg  style="width:32px;"> [Armature cintrée](Reinforcement_BentShapeRebar/fr.md) : crée une barre de renforcement de forme cintrée dans un élément de structure sélectionné.

-   <img alt="" src=images/Reinforcement_HelicalRebar.svg  style="width:32px;"> [Armature hélicoïdale](Reinforcement_HelicalRebar/fr.md) : crée une barre de ferraillage hélicoïdale dans un élément de structure sélectionné.

-   <img alt="" src=images/Reinforcement_ColumnRebars.svg  style="width:32px;"> [Armature en colonne](Reinforcement_ColumnRebars/fr.md) : crée des armatures dans une colonne sélectionnée.

-   <img alt="" src=images/Reinforcement_BeamRebars.svg  style="width:32px;"> [Poutre](Reinforcement_BeamRebars/fr.md) : crée des armatures dans une poutre sélectionnée.

-   <img alt="" src=images/Reinforcement_SlabRebars.svg  style="width:32px;"> [Renfort de dalle](Reinforcement_SlabRebars/fr.md) : crée des armatures dans une dalle sélectionnée.

-   <img alt="" src=images/Reinforcement_FootingRebars.svg  style="width:32px;"> [Renfort de semelle](Reinforcement_FootingRebars/fr.md): crée des armatures dans une semelle sélectionnée.



### Informations sur les armatures 

-   <img alt="" src=images/Reinforcement_BillOfMaterial.svg  style="width:32px;"> [Nomenclature armature](Reinforcement_BillOfMaterial/fr.md) : crée la nomenclature des armatures.

-   <img alt="" src=images/Reinforcement_BarShapeCutList.svg  style="width:32px;"> [Nomenclature de façonnage](Reinforcement_BarShapeCutList/fr.md) : crée la nomenclature de façonnage des armatures.

-   <img alt="" src=images/Reinforcement_BarBendingSchedule.svg  style="width:32px;"> [Plan de cintrage](Reinforcement_BarBendingSchedule/fr.md) : crée un plan de cintrage des barres d\'armature.

-   <img alt="" src=images/Reinforcement_DrawingDimensioning.svg  style="width:32px;"> [Dessins et dimensions](Reinforcement_DrawingDimensioning/fr.md) : crée les dessins et dimensions des armatures.



---
⏵ [documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement Workbench/fr
