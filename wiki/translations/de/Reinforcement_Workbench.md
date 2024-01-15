# <img alt="Symbol des Arbeitsbereichs Reinforcement" src=images/Reinforcement_Workbench.svg  style="width:64px;"> Reinforcement Workbench/de






## Einleitung

Der Arbeitsbereich [Reinforcement](Reinforcement_Workbench/de.md) ist ein [externer Arbeitsbereich](External_workbenches/de.md), der Werkzeuge für die Erstellung und Detaillierung von Armierungen (Bewehrungen) bereit stellt. Dieser Arbeitsbereich beinhaltet eine Benutzerschnittstelle und Voreinstellungen zum Erstellen üblicher Armierungen. Er enthält auch Werkzeuge zum Erstellen von Bewehrungsstücklisten, Zuschnittlisten für Bewehrungen, Biegeplänen für Bewehrungen und zum Zeichnen sowie Bemaßen von Bewehrungen.

Image:Arch_Rebar_Straight_example.png\|[Geradlinige Bewehrung](Arch_Rebar_Straight/de.md) Image:Arch_Rebar_UShape_example.png\|[U-förmige Bewehrung](Arch_Rebar_UShape/de.md) Image:Arch_Rebar_LShape_example.png\|[L-förmige Bewehrung](Arch_Rebar_LShape/de.md) Image:Arch_Rebar_BentShape_example.png\|[Abgesetzte Bewehrung](Arch_Rebar_BentShape/de.md) Image:Arch_Rebar_Stirrup_example.png\|[Bewehrungsbügel](Arch_Rebar_Stirrup/de.md) Image:Arch_Rebar_Helical_example.png\|[Wendelbewehrung](Arch_Rebar_Helical/de.md) Image:Arch_Rebar_Circular_ColumnReinforcement_example.png\|[Ringförmige Stützenarmierung](Arch_Rebar_Circular_ColumnReinforcement/de.md) (Bewehrungskorb) Image:Arch_Rebar_ColumnReinforcement_example.png\|[Rechteckige Einzelbügel-Stützenarmierung](Arch_Rebar_ColumnReinforcement/de.md) (Bewehrungskorb) Image:Arch_Rebar_ColumnReinforcement_TwoTies_example.png\|[Rechteckige Zwei-Bügel-Stützenarmierung mit sechs Bewehrungsstäben](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/de.md) (Bewehrungskorb) Image:Arch_Rebar_BeamReinforcement_example.png\|[Balkenarmierung](Arch_Rebar_BeamReinforcement/de.md) Image:Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png\|[Plattenarmierung](Arch_Rebar_Slab_Reinforcement/de.md) Image:Isometric_view_of_Columns_footing.png\|[Fundamentarmierung](Arch_Rebar_Footing_Reinforcement/de.md) Image:Arch_Rebar_BOM_example.png\|[Stückliste](Arch_Rebar_BOM/de.md) Image:Reinforcement_Bar_Shape_Cut_List_example.svg\|[Bewehrungszuschnittliste](Reinforcement_Bar_Shape_Cut_List/de.md) Image:Reinforcement_Bar_Bending_Schedule_example.svg\|[Bewehrungsbiegeplan](Reinforcement_Bar_Bending_Schedule/de.md) Image:Arch_Rebar_Drawing_Dimensioning_example.svg\|[Bewehrungszeichnung](Arch_Rebar_Drawing_Dimensioning/de.md)



## Installieren

Der Arbeitsbereich Reinforcement ist standardmäßig nicht im FreeCAD-Paket enthalten, kann aber einfach mit dem <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr/de.md) installiert werden: **Werkzeuge → Addon-Manager → Reinforcement**. Der Code des Arbeitsbereichs Reinforcement wird auf [github](https://github.com/amrit3701/FreeCAD-Reinforcement) bereitgestellt und weiterentwickelt; er kann auch manuell installiert werden, indem er in FreeCADs Verzeichnis **MOD** kopiert wird.



## Werkzeuge



### Armierung erstellen 

-   <img alt="" src=images/Arch_Rebar_Straight.png  style="width:32px;"> [Geradlinige Bewehrung](Arch_Rebar_Straight/de.md): Erstellt einen geraden Bewehrungsstab in einem gewählten Strukturelement.

-   <img alt="" src=images/Arch_Rebar_UShape.png  style="width:32px;"> [U-förmige Bewehrung](Arch_Rebar_UShape/de.md): Erstellt einen U-förmigen Bewehrungsstab in einem gewählten Strukturelement.

-   <img alt="" src=images/Arch_Rebar_LShape.png  style="width:32px;"> [L-förmige Bewehrung](Arch_Rebar_LShape/de.md): Erstellt einen L-förmigen Bewehrungsstab in einem gewählten Strukturelement

-   <img alt="" src=images/Arch_Rebar_BentShape.svg  style="width:32px;"> [Abgesetzte Bewehrung](Arch_Rebar_BentShape/de.md): Erstellt einen Bewehrungsstab mit Absatz in einem ausgewählten Strukturelement.

-   <img alt="" src=images/Arch_Rebar_Stirrup.svg  style="width:32px;"> [Bewehrungsbügel](Arch_Rebar_Stirrup/de.md): Erstellt einen Bewehrungsbügel in einem ausgewählten Strukturelement.

-   <img alt="" src=images/Arch_Rebar_Helical.svg  style="width:32px;"> [Wendelbewehrung](Arch_Rebar_Helical/de.md): Erstellt eine Wendelbewehrung in einem ausgewählten Strukturelement.

-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Runde Stützenbewehrung](Arch_Rebar_Circular_ColumnReinforcement/de.md): Erstellt Armierungen (Bewehrungsstäbe und Wendelbewehrung) in einem ausgewählten zylindrischen Strukturelement Stütze.

-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Stützenbewehrung](Arch_Rebar_ColumnReinforcement/de.md): Erstellt Armierungen (Bewehrungsstäbe und Bewehrungsbügel) in einem ausgewählten rechteckigen Strukturelement Stütze.

-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Rechteckige Zwei-Bügel-Stützenarmierung mit sechs Bewehrungsstäben](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/de.md): Erstellt Armierungen (Bewehrungsstäbe und Bewehrungsbügel) in einem ausgewählten rechteckigen Strukturelement Stütze.

-   <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width:32px;"> [Balkenbewehrung](Arch_Rebar_BeamReinforcement/de.md): Erstellt Armierungen (Bewehrungsstäbe und Bewehrungsbügel) in einem ausgewählten Strukturelement Balken.

-   <img alt="" src=images/Arch_Rebar_Slab_Reinforcement.svg  style="width:32px;"> [Plattenbewehrung](Arch_Rebar_Slab_Reinforcement/de.md): Erstellt Bewehrungsstäbe in einem ausgewählten Strukturelement Platte.

-   <img alt="" src=images/Arch_Rebar_Footing_Reinforcement.svg  style="width:32px;"> [Fundamentbewehrung](Arch_Rebar_Footing_Reinforcement/de.md): Erstellt Bewehrungsstäbe in einem ausgewählten Strukturelement Fundament.

-   <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Bewehrung](Arch_Rebar/de.md): Erstellt unter Verwendung einer Skizze ein individuell angepasstes Bewehrungselement in einem ausgewählten Strukturelement.

### Reinforcement Detailing 

-   <img alt="" src=images/Arch_Rebar_BOM.svg  style="width:32px;"> [Armierung Stückliste](Arch_Rebar_BOM/de.md): Erstellt eine Stückliste der Bewehrungselemente.

-   <img alt="" src=images/Reinforcement_Bar_Shape_Cut_List.svg  style="width:32px;"> [Armierung Zuschnittliste](Reinforcement_Bar_Shape_Cut_List/de.md): Erstellt eine Form- und Zuschnittliste der Bewehrungselemente.

-   <img alt="" src=images/Reinforcement_Bar_Bending_Schedule.svg  style="width:32px;"> [Armierung Biegeplan](Reinforcement_Bar_Bending_Schedule.md): Erstellt einen Biegeplan der Bewehrungselemente.

-   <img alt="" src=images/Arch_Rebar_Drawing_Dimensioning.svg  style="width:32px;"> [Armierung ZeichnungBemaßen](Arch_Rebar_Drawing_Dimensioning/de.md): Erstellt Zeichnungen mit Bemaßung von den Bewehrungselementen.
    -   <img alt="" src=images/Arch_Rebar_Drawing.svg  style="width:32px;"> [Armierung Zeichnung](Arch_Rebar_Drawing_Dimensioning#Reinforcement_Drawing/de.md): Erstellt Zeichnungen von den Bewehrungselementen.
    -   <img alt="" src=images/Arch_Rebar_Dimensioning.svg  style="width:32px;"> [Armierung Bemaßen](Arch_Rebar_Drawing_Dimensioning#Reinforcement_Dimensioning/de.md): Bemaßt die Bewehrungselemente auf einem mit [Armierung Zeichnung](Arch_Rebar_Drawing_Dimensioning#Reinforcement_Drawing/de.md) erstellten Zeichnungsblatt.



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement Workbench/de
