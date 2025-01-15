---
 GuiCommand:
   Name: Reinforcement SlabRebars
   Name/pl: BIM: Zbrojenie płyty
   MenuLocation: 3D / BIM , Narzędzia zbrojenia , Zbrojenie płyty
   Workbenches: Reinforcement_Workbench/pl, BIM_Workbench/pl
   SeeAlso: 
---

# Reinforcement SlabRebars/pl



## Opis

Narzędzie **Zbrojenie płyty** pozwala użytkownikowi na tworzenie prętów zbrojeniowych wewnątrz obiektu [konstrukcji](Arch_Structure/pl.md) płyty.

To polecenie jest częścią [zewnętrznego środowiska pracy](External_workbenches/pl.md) [Zbrojenie](Reinforcement_Workbench/pl.md), które można zainstalować za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md) poprzez menu **Przybory → Menadżera dodatków → Zbrojenie**.

<img alt="" src=images/Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:600px;"> 
*Przykład zbrojenia wewnątrz [konstrukcji](Arch_Structure/pl.md) płyty.*

<img alt="" src=images/Right_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:600px;"> 
*Widok z prawej strony podanego przykładu zbrojenia płyty.*

<img alt="" src=images/Front_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:600px;"> 
*Widok z przodu podanego przykładu zbrojenia płyty.*



## Użycie

1\. Wybierz dowolną ścianę wcześniej utworzonego obiektu **<img src="images/Arch_Structure.svg" width=16px> [konstrukcji](Arch_Structure/pl.md)** płyty, jak pokazano na poniższym obrazku.

:   <img alt="" src=images/Selected_face_for_Slab_Arch_Structure.png  style="width:400px;">

:   
    
*Wybrana ściana dla konstrukcji płyty.*
    

2\. Następnie wybierz **<img src="images/Reinforcement_SlabRebars.svg" width=16px> '''Zbrojenie płyty'''** z narzędzi prętów zbrojeniowych.

3\. Na ekranie pojawi się okno dialogowe, jak pokazano poniżej.

:   <img alt="" src=images/Slab_Reinforcement_input_dialog_box.png  style="width:600px;">

:   
    
*Okno dialogowe dla zbrojenia płyty.*
    

4\. Wybierz żądany typ otuliny siatki zbrojeniowej *(górna lub dolna)*.

5\. Wybierz żądany typ prętów oraz inne dane wejściowe dla prętów w kierunku równoległym do wybranej ściany w siatce zbrojenia płyty, jak pokazano na poniższym rysunku.

:   <img alt="" src=images/Bent_Shape_rebars_in_parallel_with_distribution_rebars_inputs_for_Slab_Reinforcement.png  style="width:600px;">

:   
    
*Okno dialogowe dla zbrojenia płyty, zbrojenie w kierunku równoległym do wybranej ściany.*
    

6\. Teraz kliknij **Dalej** lub wybierz zbrojenie poprzeczne w widoku listy.

7\. Teraz wybierz żądane dane wejściowe dla prętów w kierunku poprzecznym wybranej powierzchni, jak pokazano na poniższym obrazku.

:   <img alt="" src=images/Bent_Shape_rebars_in_cross_direction_with_distribution_rebars.png  style="width:600px;">

:   
    
*Okno dialogowe zbrojenia płyty prętami zbrojeniowymi w kierunku poprzecznym wybranej ściany.*
    

11\. Kliknij **OK** lub **Zastosuj** lub **Zakończ**, aby wygenerować zbrojenie płyty.

9\. Kliknij **Anuluj**, aby zamknąć okno dialogowe.



## Właściwości

**Właściwości prętów zbrojeniowych w kierunku równoległym do wybranej ściany:**.

-    **Otulina siatki wzdłuż**: Reprezentuje wyrównanie siatki zbrojeniowej wzdłuż górnej lub dolnej powierzchni konstrukcji. Może mieć dwie wartości \"Top\" i \"Bottom\".

-    **Typ pręta**: Typ prętów zbrojeniowych dla równoległych prętów zbrojeniowych do zbrojenia płyt. Może mieć cztery wartości \"StraightRebar\", \"LShapeRebar\", \"UShapeRebar\", \"BentShapeRebar\".

-    **Otulina przednia**: Odległość między równoległym prętem zbrojeniowym a wybraną powierzchnią czołową.

-    **Otulina lewa**: Odległość między lewym końcem równoległego pręta zbrojeniowego a lewą ścianą konstrukcji.

-    **Otulina prawa**: Odległość między prawym końcem równoległego pręta zbrojeniowego a prawą ścianą konstrukcji.

-    **Otulina dolna**: Odległość między równoległymi prętami zbrojeniowymi od dolnej ściany konstrukcji.

-    **Otulina górna**: Odległość między równoległymi prętami zbrojeniowymi od górnej powierzchni konstrukcji.

-    **Otulina tylna**: Tylna otulina dla zbrojenia płyty równoległymi prętami zbrojeniowymi.

-    **Długość kotwy**: Reprezentuje długość ramienia równoległego pręta zbrojeniowego o wygiętym kształcie, gdy typ równoległego pręta zbrojeniowego to BentShapeRebar.

-    **Kąt wygięcia**: Reprezentuje kąt równoległego pręta zbrojeniowego o wygiętym kształcie, gdy typ równoległego pręta zbrojeniowego to BentShapeRebar.

-    **Zaokrąglenie**: Wartość zaokrąglenia stosowana do narożników prętów, wyrażona w krotności średnicy równoległych prętów zbrojeniowych.

-    **Średnica**: Średnica równoległych prętów zbrojeniowych.

-    **Ilość**: Zawiera liczbę równoległych prętów zbrojeniowych.

-    **Rozstaw**: Zawiera odstępy między równoległymi prętami zbrojeniowymi.

**Właściwości prętów zbrojeniowych rozdzielczych dla prętów zbrojeniowych giętych w kierunku równoległym do wybranej powierzchni:**

-    **Ilość**: Zawiera liczbę prętów zbrojeniowych dystrybucyjnych dla prętów zbrojeniowych o kształcie giętym w kierunku równoległym.

-    **Rozstaw**: Zawiera odstępy między prętami zbrojeniowymi rozdzielczymi dla prętów zbrojeniowych odgiętych w kierunku równoległym.

**Właściwości prętów zbrojeniowych w kierunku poprzecznym do wybranej ściany:**

-    **Typ pręta**: Typ pręta zbrojeniowego dla poprzecznych prętów zbrojeniowych do zbrojenia płyt. Parametr może mieć cztery wartości: \"Pręt prosty\", \"Pręt w kształcie L\", \"Pręt w kształcie U\", \"Odgięty pręt zbrojeniowy\".

-    **Otulina przednia**: Odległość między poprzecznym prętem zbrojeniowym a wybraną powierzchnią czołową.

-    **Otulina lewa**: Odległość między lewym końcem poprzecznego pręta zbrojeniowego a lewą ścianą konstrukcji.

-    **Otulina prawa**: Odległość między prawym końcem poprzecznego pręta zbrojeniowego a prawą ścianą konstrukcji.

-    **Otulina dolna**: Odległość między poprzecznymi prętami zbrojeniowymi od dolnej powierzchni konstrukcji.

-    **Otulina górna**: Odległość między poprzecznymi prętami zbrojeniowymi od górnej powierzchni konstrukcji.

-    **Otulina tylna**: Tylna osłona zbrojenia poprzecznego płyty.

-    **Długość kotwy**: Reprezentuje długość ramienia pręta zbrojeniowego poprzecznego o wygiętym kształcie, gdy typ pręta zbrojeniowego poprzecznego to pręt zbrojeniowy odgięty.

-    **Kąt wygięcia**: Reprezentuje kąt wygięcia pręta zbrojeniowego, gdy typ pręta zbrojeniowego to pręt zbrojeniowy odgięty.

-    **Zaokrąglenie**: Wartość zaokrąglenia stosowana do narożników prętów, wyrażona w krotności średnicy prętów zbrojeniowych.

-    **Średnica**: Średnica poprzecznych prętów zbrojeniowych

-    **Amount**: Zawiera liczbę poprzecznych prętów zbrojeniowych.

-    **Spacing**: Zawiera odstępy między poprzecznymi prętami zbrojeniowymi.

**Właściwości prętów zbrojeniowych rozdzielczych dla prętów zbrojeniowych giętych w kierunku poprzecznym do wybranej powierzchni:**

-    **Ilość**: Zawiera liczbę prętów zbrojeniowych dystrybucyjnych dla prętów zbrojeniowych o kształcie giętym w kierunku poprzecznym.

-    **Rozstaw**: Zawiera odstępy między prętami zbrojeniowymi rozdzielczymi dla prętów zbrojeniowych odgiętych w kierunku poprzecznym.



## Tworzenie skryptów 


**Zobacz również:**

[Skrypty Architektury](Arch_API/pl.md), [Skrypty Zbrojenia](Reinforcement_API/pl.md) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Zbrojenie płyty** może być używane z konsoli środowiska [Python](Python/pl.md) za pomocą następującej funkcji:



### Tworzenie zbrojenia płyty 


```python
from SlabReinforcement.SlabReinforcement import makeSlabReinforcement
SlabReinforcementGroup = makeSlabReinforcement(
    parallel_rebar_type,
    parallel_front_cover,
    parallel_rear_cover,
    parallel_left_cover,
    parallel_right_cover,
    parallel_top_cover,
    parallel_bottom_cover,
    parallel_diameter,
    parallel_amount_spacing_check,
    parallel_amount_spacing_value,
    cross_rebar_type,
    cross_front_cover,
    cross_rear_cover,
    cross_left_cover,
    cross_right_cover,
    cross_top_cover,
    cross_bottom_cover,
    cross_diameter,
    cross_amount_spacing_check,
    cross_amount_spacing_value,
    cross_rounding = 2,
    cross_bent_bar_length = 50,
    cross_bent_bar_angle = 135,
    cross_l_shape_hook_orintation = "Alternate",
    cross_distribution_rebars_check = False,
    cross_distribution_rebars_diameter = 8,
    cross_distribution_rebars_amount_spacing_check = True,
    cross_distribution_rebars_amount_spacing_value = 2,
    parallel_rounding = 2,
    parallel_bent_bar_length = 50,
    parallel_bent_bar_angle = 135,
    parallel_l_shape_hook_orintation = "Alternate",
    parallel_distribution_rebars_check = False,
    parallel_distribution_rebars_diameter = 8,
    parallel_distribution_rebars_amount_spacing_check = True,
    parallel_distribution_rebars_amount_spacing_value = 2,
    mesh_cover_along = "Bottom",
    structure = None,
    facename = None,
)
```

-   Tworzy obiekt `SlabReinforcementGroup` z podanej `struktury`, która jest płytą [konstrukcyjną architektury](Arch_Structure/pl.md) i `nazwy ściany`, która jest ścianą tej konstrukcji.
    -   Jeśli nie podano ani jako parametr `struktury` ani `nazwy ściany`, program przyjmie jako dane wejściowe ścianę wybraną przez użytkownika.

**Właściwości prętów zbrojeniowych w kierunku równoległym do wybranej ściany:**.

-    **parallel_rebar_type**: Typ pręta zbrojeniowego dla równoległych prętów zbrojeniowych do zbrojenia płyt. Może mieć cztery wartości \"Pręt prosty\", \"Pręt w kształcie L\", \"Pręt w kształcie U\", \"Pręt wygięty\".

-    **parallel_front_cover**: Odległość między równoległym prętem zbrojeniowym a wybraną powierzchnią.

-    **parallel_rear_cover**: Tylna otulina dla zbrojenia płyty równoległymi prętami zbrojeniowymi.

-    **parallel_left_cover**: Odległość między lewym końcem równoległego pręta zbrojeniowego a lewą ścianą konstrukcji.

-    **parallel_right_cover**: Odległość między prawym końcem równoległego pręta zbrojeniowego a prawą ścianą konstrukcji.

-    **parallel_top_cover**: Odległość między równoległymi prętami zbrojeniowymi od górnej powierzchni konstrukcji.

-    **parallel_bottom_cover**: Odległość między równoległymi prętami zbrojeniowymi od dolnej powierzchni konstrukcji.

-    **parallel_diameter**: Średnica równoległych prętów zbrojeniowych.

-    **parallel_amount_spacing_check**: Jeśli jest ustawiona na True, wartość parallel_amount_spacing_value jest używana jako liczba prętów zbrojeniowych, w przeciwnym razie wartość parallel_amount_spacing_value jest używana jako odstęp w równoległych prętach zbrojeniowych.

-    **parallel_amount_spacing_value**: Zawiera liczbę prętów zbrojeniowych lub odstęp między równoległymi prętami zbrojeniowymi w oparciu o wartość amount_spacing_check.

-    **parallel_bent_bar_length**: Reprezentuje długość ramienia równoległego pręta zbrojeniowego o wygiętym kształcie, gdy parallel_rebar_type to BentShapeRebar

-    **parallel_bent_bar_angle**: Reprezentuje kąt dla równoległego pręta zbrojeniowego o wygiętym kształcie, gdy parallel_rebar_type to BentShapeRebar.

-    **parallel_l_shape_hook_orintation**: Reprezentuje orintację haka równoległego pręta zbrojeniowego w kształcie litery L, jeśli parallel_rebar_type to LShapeRebar. Może mieć trzy wartości \"Lewy\", \"Prawy\", \"Alternatywny\".

-    **parallel_distribution_rebars_check**: Jeśli ma wartość {{True/pl}}, dodaje pręty rozdzielcze dla prętów równoległych. Wartość domyślna to {{False/pl}}.

-    **parallel_distribution_rebars_diameter**: Średnica prętów rozdzielczych dla prętów równoległych.

-    **parallel_distribution_rebars_amount_spacing_check**: Jeśli wartość jest ustawiona na {{True/pl}}, wówczas wartość parallel_distribution_rebars_amount_spacing_value jest używana jako liczba prętów zbrojeniowych, w przeciwnym razie wartość parallel_distribution_rebars_amount_spacing_value jest używana jako odstęp w parallel_distribution_rebars. Wartość domyślna to {{True/pl}}.

-    **parallel_distribution_rebars_amount_spacing_value**: Zawiera liczbę lub odstęp między prętami zbrojeniowymi dla jednej strony równoległych prętów zbrojeniowych o wygiętym kształcie w oparciu o wartość parallel_distribution_rebars_check. Wartość domyślna to 2.

**Właściwości prętów zbrojeniowych w kierunku poprzecznym do wybranej ściany:**

-    **cross_rebar_type**: Typ pręta zbrojeniowego dla poprzecznych prętów zbrojeniowych do zbrojenia płyt. Może mieć cztery wartości \"Pręt prosty\", \"Pręt w kształcie L\", \"Pręt w kształcie U\", \"Pręt wygięty\".

-    **cross_front_cover**: Odległość między poprzecznym prętem zbrojeniowym a cross_face *(powierzchnia prostopadła do wybranej powierzchni)*.

-    **cross_rear_cover**: Tylna otulina dla zbrojenia poprzecznego prętów zbrojeniowych płyty.

-    **cross_left_cover**: Odległość między lewym końcem poprzecznego pręta zbrojeniowego a lewą ścianą konstrukcji.

-    **cross_right_cover**: Odległość między prawym końcem pręta zbrojeniowego a prawą powierzchnią konstrukcji względem cross_face.

-    **cross_top_cover**: Odległość między poprzecznymi prętami zbrojeniowymi od górnej powierzchni konstrukcji.

-    **cross_bottom_cover**: Odległość między poprzecznymi prętami zbrojeniowymi od dolnej powierzchni konstrukcji.

-    **cross_diameter**: Średnica poprzecznych prętów zbrojeniowych.

-    **cross_amount_spacing_check**: Jeśli wartość jest ustawiona na True, wówczas parametr cross_amount_spacing_value jest używany jako liczba prętów zbrojeniowych, w przeciwnym razie wartość parametru cross_amount_spacing_value jest używana jako odstęp między prętami zbrojeniowymi.

-    **cross_amount_spacing_value**: Zawiera liczbę prętów zbrojeniowych lub odstęp między prętami zbrojeniowymi w oparciu o wartość cross_amount_spacing_check.

-    **cross_rounding**: Wartość zaokrąglenia, która ma być zastosowana do narożników prętów, wyrażona w wielokrotności cross_diameter.

-    **cross_bent_bar_length**: Reprezentuje długość ramienia poprzecznego pręta zbrojeniowego o wygiętym kształcie, gdy cross_rebar_type to BentShapeRebar

-    **cross_bent_bar_angle**: Reprezentuje kąt dla wygiętego kształtu poprzecznego pręta zbrojeniowego, gdy cross_rebar_type to BentShapeRebar.

-    **cross_l_shape_hook_orintation**: Reprezentuje orintację haka poprzecznego pręta zbrojeniowego w kształcie L, jeśli cross_rebar_type to LShapeRebar. Może mieć trzy wartości \"Lewy\", \"Prawy\", \"Alternatywnie\".

-    **cross_distribution_rebars_check**: Jeśli ma wartość {{True/pl}}, dodaje pręty rozkładu dla prętów wygiętych krzyżowo. Domyślnie {{False/pl}}.

-    **cross_distribution_rebars_diameter**: Średnica prętów zbrojeniowych dla prętów zbrojeniowych wygiętych krzyżowo.

-    **cross_distribution_rebars_amount_spacing_check**: Jeśli jest ustawiona na {{True/pl}}, wartość cross_distribution_rebars_amount_spacing_value jest używana jako liczba prętów zbrojeniowych, w przeciwnym razie wartość cross_distribution_rebars_amount_spacing_value jest używana jako odstęp w cross_distribution_rebars. Wartość domyślna to {{True/pl}}.

-    **cross_distribution_rebars_amount_spacing_value**: Zawiera liczbę lub odstęp między prętami zbrojeniowymi dla jednej strony prętów zbrojeniowych o kształcie wygiętym krzyżowo w oparciu o wartość cross_distribution_rebars_check. Wartość domyślna to 2.

**Wspólne właściwości prętów równoległych i krzyżowych:**

-    `mesh_cover_along`: Może mieć dwie wartości \" Góra\", \"Dół\". Reprezentuje wyrównanie siatki zbrojeniowej wzdłuż górnej lub dolnej powierzchni konstrukcji.

-    `structure`: Obiekt konstrukcji Architektury. Domyślnie przyjmuje wartość Brak.

-    `facename`: wybrana ściana konstrukcji. Domyślnie przyjmuje wartość Brak.



### Edycja zbrojenia płyty 

Właściwości zbrojenia płyty można zmienić za pomocą następującej funkcji:


```python
from SlabReinforcement.SlabReinforcement import editSlabReinforcement
slabReinforcementGroup = editSlabReinforcement(
    slabReinforcementGroup,
    parallel_rebar_type,
    parallel_front_cover,
    parallel_rear_cover,
    parallel_left_cover,
    parallel_right_cover,
    parallel_top_cover,
    parallel_bottom_cover,
    parallel_diameter,
    parallel_amount_spacing_check,
    parallel_amount_spacing_value,
    cross_rebar_type,
    cross_front_cover,
    cross_rear_cover,
    cross_left_cover,
    cross_right_cover,
    cross_top_cover,
    cross_bottom_cover,
    cross_diameter,
    cross_amount_spacing_check,
    cross_amount_spacing_value,
    cross_rounding = 2,
    cross_bent_bar_length = 50,
    cross_bent_bar_angle = 135,
    cross_l_shape_hook_orintation = "Alternate",
    cross_distribution_rebars_check = False,
    cross_distribution_rebars_diameter = 8,
    cross_distribution_rebars_amount_spacing_check = True,
    cross_distribution_rebars_amount_spacing_value = 2,
    parallel_rounding = 2,
    parallel_bent_bar_length = 50,
    parallel_bent_bar_angle = 135,
    parallel_l_shape_hook_orintation = "Alternate",
    parallel_distribution_rebars_check = False,
    parallel_distribution_rebars_diameter = 8,
    parallel_distribution_rebars_amount_spacing_check = True,
    parallel_distribution_rebars_amount_spacing_value = 2,
    mesh_cover_along: str = "Bottom",
    structure = None,
    facename = None,
)
```

-    `footngReinforcementGroup`to wcześniej utworzony obiekt grupy `Slab Reinforcement`.

-   Pozostałe parametry są takie same, jak wymagane przez funkcję `makeSlabReinforcement()`.



### Przykłady zbrojenia płyt 

-   [Przykład płyty o rozpiętości w dwóch kierunkach](Example_Slab_Spanning_in_Two_Directions/pl.md)

<img alt="" src=images/Isometric_view_of_Bent_Shape_rebars_in_parallel_and_cross_direction_with_distribution_rebars.png  style="width:800px;">

-   [Przykład płyty o rozpiętości w jednym kierunku](Example_Slab_Spanning_in_One_Direction/pl.md)

<img alt="" src=images/Slab_spanning_in_one_Direction.png  style="width:800px;">

-   [Przykład płyty z siatką prostych prętów zbrojeniowych](Example_Slab_Having_Mesh_Of_Straight_Rebars/pl.md)

<img alt="" src=images/Slab_having_straight_rebars_in_both_direction.png  style="width:800px;">

-   [Przykładowa płyta z prętami zbrojeniowymi w kształcie U, Siatka zbrojeniowa](Example_Slab_Having_UShape_Rebars_Reinforcement_Mesh/pl.md)

<img alt="" src=images/U-shape_rebars_isometric_view.png  style="width:800px;">

-   [Przykładowa płyta z prętami zbrojeniowymi w kształcie litery L, Siatka zbrojeniowa](Example_Slab_Having_LShape_Rebars_Reinforcement_Mesh/pl.md)

<img alt="" src=images/L-Shape_Rebars_isometric_view.png  style="width:800px;">



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement SlabRebars/pl
