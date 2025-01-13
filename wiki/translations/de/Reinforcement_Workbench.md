# <img alt="Symbol des Arbeitsbereichs Reinforcement" src=images/Reinforcement_Workbench.svg  style="width:64px;"> Reinforcement Workbench/de






## Einleitung

Der Arbeitsbereich [Reinforcement](Reinforcement_Workbench/de.md) ist ein [externer Arbeitsbereich](External_workbenches/de.md), der Werkzeuge für die Erstellung und Detaillierung von Armierungen (Bewehrungen) bereit stellt. Dieser Arbeitsbereich beinhaltet eine Benutzerschnittstelle und Voreinstellungen zum Erstellen üblicher Armierungen. Er enthält auch Werkzeuge zum Erstellen von Bewehrungsstücklisten, Zuschnittlisten für Bewehrungen, Biegeplänen für Bewehrungen und zum Zeichnen sowie Bemaßen von Bewehrungen.

Image:Arch_Rebar_Straight_example.png\|[Geradlinige Bewehrung](Reinforcement_StraightRebar/de.md) Image:Arch_Rebar_UShape_example.png\|[U-förmige Bewehrung](Reinforcement_UShapeRebar/de.md) Image:Arch_Rebar_LShape_example.png\|[L-förmige Bewehrung](Reinforcement_LShapeRebar/de.md) Image:Arch_Rebar_Stirrup_example.png\|[Bewehrungsbügel](Reinforcement_StirrupReba/de.md) Image:Arch_Rebar_BentShape_example.png\|[Abgesetzte Bewehrung](Reinforcement_BentShapeRebar/de.md) Image:Arch_Rebar_Helical_example.png\|[Wendelbewehrung](Reinforcement_HelicalRebar/de.md) Image:Arch_Rebar_ColumnReinforcement_example.png\|[Rechteckige Einzelbügel-Stützenarmierung](Reinforcement_ColumnRebars/de.md) (Bewehrungskorb) Image:Arch_Rebar_ColumnReinforcement_TwoTies_example.png\|[Rechteckige Zwei-Bügel-Stützenarmierung mit sechs Bewehrungsstäben](Reinforcement_ColumnRebars_TwoTiesSixRebars/de.md) (Bewehrungskorb) Image:Arch_Rebar_Circular_ColumnReinforcement_example.png\|[Ringförmige Stützenarmierung](Reinforcement_ColumnRebars_Circular/de.md) (Bewehrungskorb) Image:Arch_Rebar_BeamReinforcement_example.png\|[Balkenarmierung](Reinforcement_BeamRebars/de.md) Image:Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png\|[Plattenarmierung](Reinforcement_SlabRebars/de.md) Image:Isometric_view_of_Columns_footing.png\|[Fundamentarmierung](Reinforcement_FootingRebars/de.md) Image:Arch_Rebar_BOM_example.png\|[Stückliste](Reinforcement_BillOfMaterial/de.md) Image:Reinforcement_Bar_Shape_Cut_List_example.svg\|[Bewehrungszuschnittliste](Reinforcement_BarShapeCutList/de.md) Image:Reinforcement_Bar_Bending_Schedule_example.svg\|[Bewehrungsbiegeplan](Reinforcement_BarBendingSchedule/de.md) Image:Arch_Rebar_Drawing_Dimensioning_example.svg\|[Bewehrungszeichnung](Reinforcement_DrawingDimensioning/de.md)



## Installieren

Der Arbeitsbereich Reinforcement ist standardmäßig nicht im FreeCAD-Paket enthalten, kann aber einfach mit dem <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr/de.md) installiert werden: **Werkzeuge → Addon-Manager → Reinforcement**. Der Code des Arbeitsbereichs Reinforcement wird auf [github](https://github.com/amrit3701/FreeCAD-Reinforcement) bereitgestellt und weiterentwickelt; er kann auch manuell installiert werden, indem er in FreeCADs Verzeichnis **MOD** kopiert wird.



## Werkzeuge



### Armierung erstellen 

-   <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Bewehrung](Arch_Rebar/de.md): Erstellt unter Verwendung einer Skizze ein individuell angepasstes Bewehrungselement in einem ausgewählten Strukturelement.

-   <img alt="" src=images/Reinforcement_StraightRebar.svg  style="width:32px;"> [Gerade Bewehrung](Reinforcement_StraightRebar/de.md): Erstellt einen geraden Bewehrungsstab in einem ausgewählten Strukturelement.

-   <img alt="" src=images/Reinforcement_UShapeRebar.svg  style="width:32px;"> [U-förmige Bewehrung](Reinforcement_UShapeRebar/de.md): Erstellt einen U-förmigen Bewehrungsstab in einem ausgewählten Strukturelement.

-   <img alt="" src=images/Reinforcement_LShapeRebar.svg  style="width:32px;"> [L-förmige Bewehrung](Reinforcement_LShapeRebar/de.md): Erstellt einen L-förmigen Bewehrungsstab in einem ausgewählten Strukturelement

-   <img alt="" src=images/Reinforcement_StirrupRebar.svg  style="width:32px;"> [Bewehrungsbügel](Reinforcement_StirrupRebar/de.md): Erstellt einen Bewehrungsbügel in einem ausgewählten Strukturelement.

-   <img alt="" src=images/Reinforcement_BentShapeRebar.svg  style="width:32px;"> [Abgesetzte Bewehrung](Reinforcement_BentShapeRebar/de.md): Erstellt einen Bewehrungsstab mit Absatz in einem ausgewählten Strukturelement.

-   <img alt="" src=images/Reinforcement_HelicalRebar.svg  style="width:32px;"> [Wendelbewehrung](Reinforcement_HelicalRebar/de.md): Erstellt eine Wendelbewehrung in einem ausgewählten Strukturelement.

-   <img alt="" src=images/Reinforcement_ColumnRebars.svg  style="width:32px;"> [Stützenbewehrung](Reinforcement_ColumnRebars/de.md): Erstellt Armierungen (Bewehrungsstäbe und Bewehrungsbügel) in einer ausgewählten Stütze.

-   <img alt="" src=images/Reinforcement_BeamRebars.svg  style="width:32px;"> [Balkenbewehrung](Reinforcement_BeamRebars/de.md): Erstellt Armierungen (Bewehrungsstäbe und Bewehrungsbügel) in einem ausgewählten Balken.

-   <img alt="" src=images/Reinforcement_SlabRebars.svg  style="width:32px;"> [Plattenbewehrung](Reinforcement_SlabRebars/de.md): Erstellt Bewehrungsstäbe in einer ausgewählten Platte.

-   <img alt="" src=images/Arch_Rebar_Footing_Reinforcement.svg  style="width:32px;"> [Fundamentbewehrung](Arch_Rebar_Footing_Reinforcement/de.md): Erstellt Armierungen (Bewehrungsstäbe und Bewehrungsbügel) in einem ausgewählten Fundament.



### Armierung detaillieren 

-   <img alt="" src=images/Reinforcement_BillOfMaterial.svg  style="width:32px;"> [Armierung Stückliste](Reinforcement_BillOfMaterial/de.md): Erstellt eine Stückliste der Bewehrungselemente.

-   <img alt="" src=images/Reinforcement_BarShapeCutList.svg  style="width:32px;"> [Armierung Zuschnittliste](Reinforcement_BarShapeCutList/de.md): Erstellt eine Form- und Zuschnittliste der Bewehrungselemente.

-   <img alt="" src=images/Reinforcement_BarBendingSchedule.svg  style="width:32px;"> [Armierung Biegeplan](Reinforcement_BarBendingSchedule/de.md): Erstellt einen Biegeplan der Bewehrungselemente.

-   <img alt="" src=images/Reinforcement_DrawingDimensioning.svg  style="width:32px;"> [Armierung ZeichnungBemaßen](Reinforcement_DrawingDimensioning/de.md): Erstellt Zeichnungen mit Bemaßung von den Bewehrungselementen.



---
⏵ [documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement Workbench/de
