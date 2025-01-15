---
 GuiCommand:
   Name: Reinforcement ColumnRebars
   Name/pl: Zbrojenie: Zbrojenie kolumn
   MenuLocation: 3D / BIM , Narzędzia zbrojenia , Zbrojenie kolumn
   Workbenches: Reinforcement_Workbench/pl, BIM_Workbench/pl
   Version: 0.19
   SeeAlso: Reinforcement_ColumnRebars/pl, Reinforcement_ColumnRebars_TwoTiesSixRebars/pl
---

# Reinforcement ColumnRebars Circular/pl



## Opis

Narzędzie **Zbrojenie okrągłych słupów** pozwala użytkownikowi na tworzenie prętów zbrojeniowych wewnątrz obiektu [konstrukcji](Arch_Structure/pl.md). Ta strona pokazuje dodatkowy przykład użycia tego narzędzia.

To polecenie jest częścią [zewnętrznego środowiska pracy](External_workbenches/pl.md) [Zbrojenie](Reinforcement_Workbench/pl.md), które można zainstalować za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md) poprzez menu **Przybory → Menadżera dodatków → Zbrojenie**.

Dostępne są trzy przykłady użycia:

-   [Prostokątna kolumna z pojedynczym ściągiem](Reinforcement_ColumnRebars/pl.md)
-   [Zbrojenie słupa dwa ściągi sześć prętów zbrojeniowych](Reinforcement_ColumnRebars_TwoTiesSixRebars/pl.md)
-   [Zbrojenie okrągłych słupów *(zobacz poniżej)*](#Użycie.md)

<img alt="" src=images/Arch_Rebar_Circular_ColumnReinforcement_example.png  style="width:400px;"> 
*Okrągłe wzmocnienie wewnątrz [słupa](Arch_Structure/pl.md)*



## Użycie

1\. Wybierz górną ścianę wcześniej utworzonego obiektu **<img src="images/Arch_Structure.svg" width=16px> [konstrukcji](Arch_Structure/pl.md)** architektury.

2\. Następnie wybierz **<img src="images/Reinforcement_ColumnRebars.svg" width=16px> [Zbrojenie słupów](Reinforcement_ColumnRebars/pl.md)** z narzędzi prętów zbrojeniowych.

3\. Na ekranie pojawi się okno dialogowe, jak pokazano poniżej.

:   <img alt="" src=images/ColumnReinforcementDialog_Ties.png  style="width:700px;">

:   
    
*Okno dialogowe dla narzędzia Zbrojenie okrągłych słupów.*
    

4\. Wciśnij przycisk \"Słup okrągły\" w oknie dialogowym Zbrojenie słupa.

:   <img alt="" src=images/CircularColumnReinforcementDialog.png  style="width:700px;">

:   
    
*Okno dialogowe dla zbrojenia okrągłych słupów*
    

5\. Wprowadź dane dotyczące zbrojenia dla okrągłego słupa.

8\. Kliknij **OK** lub **Zastosuj**, aby wygenerować zbrojenie słupa okrągłego.

7\. Kliknij **Anuluj**, aby zamknąć okno dialogowe.



## Właściwości

**Spiralne pręty zbrojeniowe:**

-    **Otulina boczna**: Odległość między prętem zbrojeniowym a zakrzywioną powierzchnią.

-    **Otulina górna**: Odległość między prętami zbrojeniowymi od górnej ściany konstrukcji.

-    **Otulina dolna**: Odległość między prętami zbrojeniowymi od dolnej powierzchni konstrukcji.

-    **Skok**: Skok spirali to wysokość jednego pełnego obrotu spirali, mierzona równolegle do osi spirali.

-    **Średnica**: Średnica pręta zbrojeniowego.

**Zbrojenie główne:**

-    **Odsunięcie górne**: Odległość między prętami zbrojeniowymi od górnej powierzchni konstrukcji.

-    **Odsunięcie dolne**: Odległość między prętami zbrojeniowymi od dolnej powierzchni konstrukcji.

-    **Średnica**: Średnica głównych prętów zbrojeniowych.

-    **Ilość**: Liczba głównych prętów zbrojeniowych.

-    **Kąt**: Odległość kątowa między strzemionami.



## Tworzenie skryptów 


**Zobacz również:**

[Skrypty Architektury](Arch_API/pl.md), [Skrypty Zbrojenia](Reinforcement_API/pl.md) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Zbrojenie kolumn** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:



### Tworzenie zbrojenia słupa okrągłego 


```python
RebarGroup = CircularColumn.makeReinforcement(
    s_cover,
    helical_rebar_t_offset,
    helical_rebar_b_offset,
    pitch,
    dia_of_helical_rebar,
    main_rebars_t_offset,
    main_rebars_b_offset,
    dia_of_main_rebars,
    number_angle_check,
    number_angle_value,
    structure=None,
    facename=None,
)
```

-   Tworzy obiekt `RebarGroup` z podanej `structure`, która jest [konstrukcją architektury](Arch_Structure/pl.md), oraz `facename`, który jest powierzchnią tej struktury.
    -   Jeśli nie podano `structure` ani `facename`, zostanie użyta wybrana przez użytkownika powierzchnia.

-    `s_cover`, `helical_rebar_t_offset` i `helical_rebar_b_offset` to wewnętrzne odległości dla zbrojenia spiralnego względem powierzchni struktury. Są to odpowiednio odległości boczna, górna i dolna.

-    `pitch`to parametr określający, jak blisko lub daleko od siebie znajdują się poszczególne pętle spiralne.

-    `dia_of_helical_rebar`to średnica zbrojenia spiralnego wewnątrz struktury.

-    `main_rebars_t_offset`i `main_rebars_b_offset` to wewnętrzne odległości dla głównych zbrojeń względem górnej i dolnej powierzchni struktury, odpowiednio.

-    `dia_of_main_rebars`to średnica głównych zbrojeń.

-    `number_angle_check`jeśli jest `True`, utworzy tyle głównych zbrojeń, ile podano w `number_angle_value`; jeśli `False`, utworzy główne zbrojenia pod kątem `number_spacing_value`, określonym w stopniach.

-    `number_angle_value`określa liczbę głównych zbrojeń lub wartość kąta między głównymi zbrojeniami, w zależności od `number_angle_check`.



#### Przykład


```python
import FreeCAD, Draft, Arch
from ColumnReinforcement import CircularColumn

Circle = Draft.makeCircle(radius=250)
Structure = Arch.makeStructure(Circle)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

RebarGroup = CircularColumn.makeReinforcement(
    s_cover=20,
    helical_rebar_t_offset=40,
    helical_rebar_b_offset=40,
    pitch=50,
    dia_of_helical_rebar=8,
    main_rebars_t_offset=20,
    main_rebars_b_offset=20,
    dia_of_main_rebars=16,
    number_angle_check=True,
    number_angle_value=6,
    structure=Structure,
    facename="Face3",
).rebar_group
```



### Edycja okrągłego zbrojenia kolumny 

Właściwości prętów spiralnych i głównych można zmienić za pomocą poniższej funkcji:


```python
rebar_group = editReinforcement(
    rebar_group,
    s_cover,
    helical_rebar_t_offset,
    helical_rebar_b_offset,
    pitch,
    dia_of_helical_rebar,
    main_rebars_t_offset,
    main_rebars_b_offset,
    dia_of_main_rebars,
    number_angle_check,
    number_angle_value,
    structure=None,
    facename=None,
)
```

-    `Rebar`jest wcześniej utworzonym obiektem `ColumnReinforcement`.

-   Pozostałe parametry są takie same jak wymagane przez funkcję `makeSingleTieFourRebars()`.

-    `structure`i `facename` mogą zostać pominięte, aby pręt zbrojeniowy pozostał w oryginalnej konstrukcji.



#### Przykład 


```python
from ColumnReinforcement import CircularColumn

rebar_group = CircularColumn.editReinforcement(
    rebar_group,
    s_cover=30,
    helical_rebar_t_offset=30,
    helical_rebar_b_offset=30,
    pitch=60,
    dia_of_helical_rebar=10,
    main_rebars_t_offset=-30,
    main_rebars_b_offset=-30,
    dia_of_main_rebars=18,
    number_angle_check=False,
    number_angle_value=45,
    structure=Structure,
    facename="Face3",
)
```



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement ColumnRebars Circular/pl
