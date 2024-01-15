# <img alt="L\'icona dell\'ambiente Reinforcement" src=images/Reinforcement_Workbench.svg  style="width:64px;"> Reinforcement Workbench/it






## Introduzione

L\'ambiente [Rinforzi](Reinforcement_Workbench/it.md) è un [ambiente di lavoro esterno](External_workbenches/it.md) che fornisce strumenti per la generazione e la creazione di armature. Questo ambiente fornisce un\'interfaccia e preimpostazioni per la creazione dei tipi comuni di barre d\'armatura, e strumenti per generare distinte base per barre d\'armatura, distinte di taglio per forme d\'armatura, programma di piegatura delle barre e disegno e quotatura delle barre d\'armatura.

Image:Arch_Rebar_Straight_example.png\|[Armatura diritta](Arch_Rebar_Straight/it.md) Image:Arch_Rebar_UShape_example.png\|[Armatura ad U](Arch_Rebar_UShape/it.md) Image:Arch_Rebar_LShape_example.png\|[Armatura a L](Arch_Rebar_LShape/it.md) Image:Arch_Rebar_BentShape_example.png\|[Armatura sagomata](Arch_Rebar_BentShape/it.md) Image:Arch_Rebar_Stirrup_example.png\|[Staffe d\'armatura](Arch_Rebar_Stirrup/it.md) Image:Arch_Rebar_Helical_example.png\|[Armatura elicoidale](Arch_Rebar_Helical/it.md) Image:Arch_Rebar_Circular_ColumnReinforcement_example.png\|[Armatura di colonna circolare](Arch_Rebar_Circular_ColumnReinforcement/it.md) Image:Arch_Rebar_ColumnReinforcement_example.png\|[Armatura di pilastro a tirante singolo](Arch_Rebar_ColumnReinforcement/it.md) Image:Arch_Rebar_ColumnReinforcement_TwoTies_example.png\|[Armatura di pilastro con due staffe e sei barre](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/it.md) Image:Arch_Rebar_BeamReinforcement_example.png\|[Armatura di trave](Arch_Rebar_BeamReinforcement/it.md) Image:Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png\|[Armatura di soletta](Arch_Rebar_Slab_Reinforcement/it.md) Image:Isometric_view_of_Columns_footing.png\|[Armatura di fondamenta](Arch_Rebar_Footing_Reinforcement/it.md) Image:Arch_Rebar_BOM_example.png\|[Distinta base](Arch_Rebar_BOM/it.md) Image:Reinforcement_Bar_Shape_Cut_List_example.svg\|[Lista della sagomatura dei ferri](Reinforcement_Bar_Shape_Cut_List/it.md) Image:Reinforcement_Bar_Bending_Schedule_example.svg\|[Programma di piegatura delle barre d\'armatura](Reinforcement_Bar_Bending_Schedule/it.md) Image:Arch_Rebar_Drawing_Dimensioning_example.svg\|[Dimensionamento del disegno dell\'armatura](Arch_Rebar_Drawing_Dimensioning/it.md)



## Installazione

L\'ambiente Reinforcement non è incluso nel pacchetto predefinito di FreeCAD, ma può essere facilmente installato tramite <img alt="" src=images/AddonManager.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr/it.md). Si installa da **Strumenti → Addon Manager → Reinforcement**. Il codice dell\'Ambiente Reinforcement è [ospitato e sviluppato su github](https://github.com/amrit3701/FreeCAD-Reinforcement) e può anche essere installato manualmente copiandolo nella directory **MOD** di FreeCAD.



## Strumenti



### Generazione di rinforzi 

-   <img alt="" src=images/Arch_Rebar_Straight.png  style="width:32px;"> [Armatura diritta](Arch_Rebar_Straight/it.md): Crea una barra d\'armatura diritta in un elemento strutturale selezionato

-   <img alt="" src=images/Arch_Rebar_UShape.png  style="width:32px;"> [Armatura ad U](Arch_Rebar_UShape/it.md): Crea una barra d\'armatura a U in un elemento strutturale selezionato

-   <img alt="" src=images/Arch_Rebar_LShape.png  style="width:32px;"> [Armatura a forma di L](Arch_Rebar_LShape/it.md): Crea una barra d\'armatura a forma di L in un elemento strutturale selezionato

-   <img alt="" src=images/Arch_Rebar_BentShape.png  style="width:32px;"> [Armatura sagomata](Arch_Rebar_BentShape/it.md): Crea una barra d\'armatura sagomata in un elemento strutturale selezionato

-   <img alt="" src=images/Arch_Rebar_Stirrup.png  style="width:32px;"> [Stirrup Rebar](Arch_Rebar_Stirrup/it.md): Crea una staffa d\'armatura in un elemento strutturale selezionato

-   <img alt="" src=images/Arch_Rebar_Helical.png  style="width:32px;"> [Armatura elicoidale](Arch_Rebar_Helical/it.md): Crea una barra d\'armatura elicoidale in un elemento strutturale selezionato

-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Armatura di colonna circolare](Arch_Rebar_Circular_ColumnReinforcement/it.md): Crea barre d\'armatura per un pilastro circolare in un elemento strutturale selezionato

-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Armatura di pilastro](Arch_Rebar_ColumnReinforcement/it.md): Crea barre d\'armatura per un pilastro rettangolare in un elemento strutturale selezionato

-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Armatura di pilastro con due staffe e sei barre](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/it.md): Crea barre d\'armatura in un elemento strutturale selezionato

-   <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width:32px;"> [Armatura di trave](Arch_Rebar_BeamReinforcement/it.md): Crea barre d\'armatura di una trave in un elemento strutturale selezionato

-   <img alt="" src=images/Arch_Rebar_Slab_Reinforcement.svg  style="width:32px;"> [Armatura di soletta](Arch_Rebar_Slab_Reinforcement/it.md): Crea barre d\'armatura di una soletta in un elemento strutturale selezionato

-   <img alt="" src=images/Arch_Rebar_Footing_Reinforcement.svg  style="width:32px;"> [Armatura di fondamenta](Arch_Rebar_Footing_Reinforcement/it.md): Crea barre d\'armatura di fondamenta in un elemento strutturale selezionato

-   <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Armatura](Arch_Rebar/it.md): Crea un\'armatura personalizzata in un elementro strutturale selezionato utilizzando uno schizzo



### Dettagli dei rinforzi 

-   <img alt="" src=images/Arch_Rebar_BOM.svg  style="width:32px;"> [Distinta dei ferri](Arch_Rebar_BOM/it.md): Crea la distinta delle barre d\'armatura.

-   <img alt="" src=images/Reinforcement_Bar_Shape_Cut_List.svg  style="width:32px;"> [Sagomatura dei ferri](Reinforcement_Bar_Shape_Cut_List/it.md): Crea una distinta dela sagomatura delle barre d\'armatura.

-   <img alt="" src=images/Reinforcement_Bar_Bending_Schedule.svg  style="width:32px;"> [Distinta e sagomatura dei ferri](Reinforcement_Bar_Bending_Schedule.md): Crea una distinta dei ferri e il disegno della sagomatura delle barre d\'armatura.

-   <img alt="" src=images/Arch_Rebar_Drawing_Dimensioning.svg  style="width:32px;"> [Disegna e quota un\'armatura](Arch_Rebar_Drawing_Dimensioning/it.md): Crea il disegno e il dimensionamento delle barre d\'armatura.
    -   <img alt="" src=images/Arch_Rebar_Drawing.svg  style="width:32px;"> [Disegna un\'armatura](Arch_Rebar_Drawing_Dimensioning/it#Disegna_un'armatura.md): Crea il disegno delle barre d\'armatura
    -   <img alt="" src=images/Arch_Rebar_Dimensioning.svg  style="width:32px;"> [Quota un\'armatura](Arch_Rebar_Drawing_Dimensioning/it#Quota_un'armatura.md): Crea il dimensionamento delle barre d\'armatura in [Disegna un\'armatura](Arch_Rebar_Drawing_Dimensioning/it#Disegna_un'armatura.md)



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement Workbench/it
