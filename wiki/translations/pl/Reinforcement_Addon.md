# Reinforcement Addon/pl
## Wprowadzenie

Dodatek [Zbrojenie](Reinforcement_Addon/pl.md) rozszerza środowisko pracy [Architektura](Arch_Workbench/pl.md), zapewniając nowe interfejsy i ustawienia wstępne do tworzenia popularnych typów prętów zbrojeniowych do użytku z [konstrukcjami](Arch_Structure/pl.md).

Narzędzia można zainstalować za pomocą [Menedżera dodatków](Std_AddonMgr/pl.md) poprzez menu **Przybory → Menadżer dodatków → Zbrojenie**. FreeCAD musi zostać ponownie uruchomiony, aby nowe narzędzia pojawiły się w menu **<img src="images/Arch_Rebar.svg" width=16px>. [Narzędzia zbrojenia](Arch_Rebar/pl.md)** środowiska Architektura.

Dodatek ten został opracowany podczas [Google Summer of Code](Google_Summer_of_Code.md) 2017 i jest hostowany w repozytorium [FreeCAD-Reinforcement](https://github.com/amrit3701/FreeCAD-Reinforcement) Github, które jest oddzielone od głównego repozytorium FreeCAD.



### Elementy

Środowisko pracy Architektura udostępnia tylko jedno narzędzie do zbrojenia:

-   <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> [Pręt zbrojeniowy](Arch_Rebar/pl.md): tworzy niestandardowy pręt zbrojeniowy w wybranej [konstrukcji](Arch_Structure/pl.md) przy użyciu [Szkicownika](Sketcher_Workbench/pl.md).

Dodatek zbrojenia dostarcza dodatkowe typy prętów zbrojeniowych:

-   <img alt="" src=images/Arch_Rebar_Straight.svg  style="width:32px;"> [Pręty zbrojeniowe proste](Arch_Rebar_Straight/pl.md): tworzy prosty pręt zbrojeniowy.
-   <img alt="" src=images/Arch_Rebar_UShape.svg  style="width:32px;"> [Pręty zbrojeniowe typu U](Arch_Rebar_UShape/pl.md): tworzy pręt zbrojeniowy w kształcie litery U.
-   <img alt="" src=images/Arch_Rebar_LShape.svg  style="width:32px;"> [Pręty zbrojeniowe typu L](Arch_Rebar_LShape/pl.md): tworzy pręt zbrojeniowy w kształcie litery L.
-   <img alt="" src=images/Arch_Rebar_BentShape.svg  style="width:32px;"> [Pręty zbrojeniowe odgięte](Arch_Rebar_BentShape/pl.md): tworzy wygięty pręt zbrojeniowy.
-   <img alt="" src=images/Arch_Rebar_Stirrup.svg  style="width:32px;"> [Strzemiona](Arch_Rebar_Stirrup/pl.md): tworzy pętlę pręta zbrojeniowego.
-   <img alt="" src=images/Arch_Rebar_Helical.svg  style="width:32px;"> [Pręty zbrojeniowe spiralne](Arch_Rebar_Helical/pl.md): tworzy pręt zbrojeniowy w kształcie spirali.

Nowe narzędzia z graficznym interfejsem do wprowadzania wartości

-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Pręty zbrojeniowe, zbrojenie okrągłych słupów](Arch_Rebar_Circular_ColumnReinforcement/pl.md)
-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Pręty zbrojeniowe, zbrojenie słupów](Arch_Rebar_ColumnReinforcement/pl.md)
-   <img alt="" src=images/Arch_Rebar_ColumnReinforcement.svg  style="width:32px;"> [Pręty zbrojeniowe, zbrojenie słupa dwa ściągi sześć prętów zbrojeniowych](Arch_Rebar_ColumnReinforcement_TwoTiesSixRebars/pl.md)
-   <img alt="" src=images/Arch_Rebar_BeamReinforcement.svg  style="width:32px;"> [Pręty zbrojeniowe, zbrojenie belek](Arch_Rebar_BeamReinforcement/pl.md)



## Zewnętrzne środowiska pracy 

Środowiska pracy FreeCAD są łatwe do zaprogramowania w środowisku [Python](Python/pl.md). Dlatego też, wiele osób opracowuje dodatkowe \"przestrzenie robocze\" wykraczające poza główny obszar rozwoju programu FreeCAD.

Strona [Zewnętrzne środowiska pracy](External_workbenches/pl.md) zawiera informacje i poradniki na temat niektórych z nich, a projekt [Dodatki FreeCAD](https://github.com/FreeCAD/FreeCAD-addons) ma na celu zebranie ich i uczynienie łatwymi do zainstalowania z poziomu programu FreeCAD.

Nowe środowiska pracy są w czasie tworzenia, bądź cierpliwy!



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Category_Arch.md) > Reinforcement Addon/pl
