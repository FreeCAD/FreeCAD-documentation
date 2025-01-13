---
 TutorialInfo:l
   Topic: Przykład płyty o rozpiętości w jednym kierunku
   Level: Średnio zaawansowany
   Time: dowolny
   Author: Shiv Charan
   FCVersion: 0.20
   Files: nie dołączono
---

# Example Slab Spanning in One Direction/pl







## Opis

Narzędzie <img alt="" src=images/Reinforcement_SlabRebars.svg  style="width:24px;"> [Zbrojenie płyt](Reinforcement_SlabRebars/pl.md) pozwala użytkownikowi na tworzenie prętów zbrojeniowych wewnątrz obiektu [konstrukcji](Arch_Structure/pl.md) płyty.

To narzędzie jest częścią [zewnętrznego środowiska pracy](External_workbenches/pl.md) [Zbrojenie](Reinforcement_Workbench/pl.md), które można zainstalować za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md).

W tym przykładzie utworzymy zbrojenie płyty dla płyty rozpiętej w jednym kierunku, jak pokazano na poniższym rysunku.

<img alt="" src=images/Slab_spanning_in_one_Direction.png  style="width:800px;"> 
*Przykład zbrojenia płyty o rozpiętości w jednym kierunku w [konstrukcji](Arch_Structure/pl.md) płyty.*

<img alt="" src=images/Right_view_of_Slab_spanning_in_one_direction.png  style="width:800px;"> 
*Widok z prawej strony podanego przykładu zbrojenia płyty.*

<img alt="" src=images/Front_view_of_slab_spanning_in_one_direction.png  style="width:800px;"> 
*Widok z przodu podanego przykładu zbrojenia płyty.*



## Użycie

1\. Wybierz dowolną ścianę wcześniej utworzonego obiektu **<img src="images/Arch_Structure.svg" width=16px> [konstrukcji](Arch_Structure/pl.md)** płyty, jak pokazano na poniższym obrazku.

:   <img alt="" src=images/Selected_face_for_Slab_Arch_Structure.png  style="width:400px;">

:   
    
*Wybrana ściana dla konstrukcji płyty.*
    

2\. Następnie wybierz **<img src="images/Reinforcement_SlabRebars.svg" width=16px> '''Zbrojenie płyty'''** z narzędzi prętów zbrojeniowych.

3\. Na ekranie pojawi się okno dialogowe, jak pokazano poniżej.

:   ![](images/Slab_Reinforcement_input_dialog_box.png )

:   
    
*Okno dialogowe dla zbrojenia płyty.*
    

4\. Wybierz żądany typ pokrycia siatki zbrojeniowej *(Góra lub Dół)* W przykładzie wybrano Dół.

5\. Wybierz typ pręta zbrojeniowego Pręt prosty i inne dane wejściowe dla prętów zbrojeniowych w kierunku równoległym do wybranej powierzchni, jak pokazano na poniższym rysunku.

:   ![](images/Straight_Rebars_in_parallel_for_Slab_Spanning_in_One_Direction.png )

:   
    
*Okno dialogowe dla zbrojenia płyty, zbrojenie w kierunku równoległym do wybranej ściany.*
    

6\. Teraz kliknij przycisk **Dalej** lub wybierz Pręty zbrojeniowe w widoku listy.

7\. Teraz wybierz typ pręta zbrojeniowego Pręt zbrojeniowy odgięty i inne żądane dane jako dane wejściowe dla prętów zbrojeniowych w kierunku poprzecznym wybranej powierzchni, jak pokazano na poniższym obrazku.

:   ![](images/Bent_Shape_rebars_in_cross_direction_with_distribution_rebars.png )

:   
    
*Okno dialogowe zbrojenia płyty prętami zbrojeniowymi w kierunku poprzecznym wybranej ściany.*
    

8\. Kliknij **OK** lub **Zastosuj** lub **Zakończ**, aby wygenerować zbrojenie płyty.

9\. Kliknij **Anuluj**, aby zamknąć okno dialogowe.



## Właściwości używane dla płyt o rozpiętości w jednym kierunku 

**Właściwości prętów zbrojeniowych w kierunku równoległym do wybranej ściany:**.

-    **Pokrycie siatki wzdłuż**: Reprezentuje wyrównanie siatki zbrojeniowej wzdłuż górnej lub dolnej powierzchni konstrukcji. Może mieć dwie wartości \"Góra\" i \"Dół\".

-    **Typ pręta**: Typ prętów zbrojeniowych dla równoległych prętów zbrojeniowych do zbrojenia płyt. Może mieć cztery wartości \"Pręty zbrojeniowe proste\", \"Pręty zbrojeniowe typu L\", \"Pręty zbrojeniowe typu U\", \"Pręty zbrojeniowe odgięte\".

-    **Otulina przednia**: Odległość między równoległym prętem zbrojeniowym, a wybraną powierzchnią czołową.

-    **Otulina lewa**: Odległość między lewym końcem równoległego pręta zbrojeniowego, a lewą ścianą konstrukcji.

-    **Otulina prawa**: Odległość między prawym końcem równoległego pręta zbrojeniowego, a prawą ścianą konstrukcji.

-    **Otulina dolna**: Odległość między równoległymi prętami zbrojeniowymi od dolnej ściany konstrukcji.

-    **Otulina górna**: Odległość między równoległymi prętami zbrojeniowymi od górnej powierzchni konstrukcji.

-    **Otulina tylna**: Tylna osłona dla zbrojenia płyty równoległymi prętami zbrojeniowymi.

-    **Średnica**: Średnica równoległych prętów zbrojeniowych.

-    **Ilość**: Zawiera liczbę równoległych prętów zbrojeniowych.

-    **Odstęp**: Zawiera odstępy między równoległymi prętami zbrojeniowymi.

**Właściwości prętów zbrojeniowych w kierunku poprzecznym do wybranej ściany:**

-    **Typ pręta**: Typ prętów zbrojeniowych dla równoległych prętów zbrojeniowych do zbrojenia płyt. Może mieć cztery wartości \"Pręty zbrojeniowe proste\", \"Pręty zbrojeniowe typu L\", \"Pręty zbrojeniowe typu U\", \"Pręty zbrojeniowe odgięte\".

-    **Otulina przednia**: Odległość między równoległym prętem zbrojeniowym, a wybraną powierzchnią czołową.

-    **Otulina lewa**: Odległość między lewym końcem równoległego pręta zbrojeniowego, a lewą ścianą konstrukcji.

-    **Otulina prawa**: Odległość między prawym końcem równoległego pręta zbrojeniowego, a prawą ścianą konstrukcji.

-    **Otulina dolna**: Odległość między równoległymi prętami zbrojeniowymi od dolnej ściany konstrukcji.

-    **Otulina górna**: Odległość między równoległymi prętami zbrojeniowymi od górnej powierzchni konstrukcji.

-    **Otulina tylna**: Tylna osłona dla zbrojenia płyty równoległymi prętami zbrojeniowymi.

-    **Długość kotwy**: Reprezentuje długość ramienia poprzecznego pręta zbrojeniowego o wygiętym kształcie, gdy typ poprzecznego pręta zbrojeniowego to Pręt zbrojeniowy odgięty.

-    **Kąt wygięcia**: Reprezentuje kąt dla wygiętego kształtu poprzecznego pręta zbrojeniowego, gdy typ poprzecznego pręta zbrojeniowego to Pręt zbrojeniowy odgięty.

-    **Zaokrąglenie**: Wartość zaokrąglenia, która ma być zastosowana do końców prętów, wyrażona w krotności średnicy poprzecznych prętów zbrojeniowych.

-    **Średnica**: Średnica równoległych prętów zbrojeniowych.

-    **Ilość**: Zawiera liczbę równoległych prętów zbrojeniowych.

-    **Odstęp**: Zawiera odstępy między równoległymi prętami zbrojeniowymi.

**Właściwości prętów zbrojeniowych rozdzielczych dla prętów zbrojeniowych giętych w kierunku poprzecznym do wybranej powierzchni:**

-    **Ilość**: Zawiera liczbę prętów zbrojeniowych dystrybucyjnych dla prętów zbrojeniowych o kształcie giętym w kierunku poprzecznym.

-    **Rozstaw**: Zawiera odstępy między prętami zbrojeniowymi rozdzielczymi dla prętów zbrojeniowych odgiętych w kierunku poprzecznym.



## Tworzenie skryptów 


**Zobacz również:**

[Skrypty Architektury](Arch_API/pl.md), [Skrypty Zbrojenia](Reinforcement_API/pl.md) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Zbrojenie płyt** może być używane z konsoli środowiska [Python](Python/pl.md) za pomocą następującej funkcji:



### Tworzenie zbrojenia płyty o rozpiętości w jednym kierunku 

Aby utworzyć zbrojenie płyty obejmujące jeden kierunek, jak pokazano na powyższych rysunkach, można użyć funkcji `makeSlabReinforcement` w następujący sposób:


```python
from SlabReinforcement.SlabReinforcement import makeSlabReinforcement
SlabReinforcementGroup = makeSlabReinforcement(
    parallel_rebar_type="StraightRebar",
    parallel_front_cover=20,
    parallel_rear_cover=20,
    parallel_left_cover=10,
    parallel_right_cover=10,
    parallel_top_cover=30,
    parallel_bottom_cover=20,
    parallel_diameter=8,
    parallel_amount_spacing_check=False,
    parallel_amount_spacing_value=50,
    cross_rebar_type="BentShapeRebar",
    cross_front_cover=20,
    cross_rear_cover=20,
    cross_left_cover=10,
    cross_right_cover=10,
    cross_top_cover=29,
    cross_bottom_cover=20,
    cross_diameter=8,
    cross_amount_spacing_check=True,
    cross_amount_spacing_value=10,
    cross_rounding=2,
    cross_bent_bar_length=150,
    cross_bent_bar_angle=135,
    cross_distribution_rebars_check = True,
    cross_distribution_rebars_diameter = 8,
    cross_distribution_rebars_amount_spacing_check = True,
    cross_distribution_rebars_amount_spacing_value = 4,
    mesh_cover_along = "Bottom",
    structure=App.getDocument("slab").getObject("Beam"),
    facename='Face4',
)
```

-   Tworzy obiekt `SlabReinforcementGroup` dla rozpiętości płyty z prostym zbrojeniem prętami zbrojeniowymi z podanego obiektu `structure`, który jest [konstrukcją](Arch_Structure/pl.md), oraz `facename`, który jest ścianą tej konstrukcji.
    -   Jeśli nie podano `structure` ani `facename`, jako dane wejściowe zostanie przyjęta ściana wybrana przez użytkownika.

**Właściwości używane dla płyty rozpiętej w jednym kierunku na potrzeby skryptów.**

**Właściwości prętów zbrojeniowych w kierunku równoległym do wybranej ściany:**.

-    **parallel_rebar_type**: Typ pręta zbrojeniowego dla równoległych prętów zbrojeniowych do zbrojenia płyt. Może mieć cztery wartości \"Pręty zbrojeniowe proste\", \"Pręty zbrojeniowe typu L\", \"Pręty zbrojeniowe typu U\", \"Pręty zbrojeniowe odgięte\".

-    **parallel_front_cover**: Odległość między równoległym prętem zbrojeniowym a wybraną powierzchnią.

-    **parallel_rear_cover**: Tylna otulina dla zbrojenia płyty równoległymi prętami zbrojeniowymi.

-    **parallel_left_cover**: Odległość między lewym końcem równoległego pręta zbrojeniowego a lewą ścianą konstrukcji.

-    **parallel_right_cover**: Odległość między prawym końcem równoległego pręta zbrojeniowego a prawą ścianą konstrukcji.

-    **parallel_top_cover**: Odległość między równoległymi prętami zbrojeniowymi od górnej powierzchni konstrukcji.

-    **parallel_bottom_cover**: Odległość między równoległymi prętami zbrojeniowymi od dolnej powierzchni konstrukcji.

-    **parallel_diameter**: Średnica równoległych prętów zbrojeniowych.

-    **parallel_amount_spacing_check**: Jeśli jest ustawiona na {{True/pl}}, wartość parallel_amount_spacing_value jest używana jako liczba prętów zbrojeniowych, w przeciwnym razie wartość parallel_amount_spacing_value jest używana jako odstęp w równoległych prętach zbrojeniowych.

-    **parallel_amount_spacing_value**: Zawiera liczbę prętów zbrojeniowych lub odstęp między równoległymi prętami zbrojeniowymi w oparciu o wartość amount_spacing_check.

**Właściwości prętów zbrojeniowych w kierunku poprzecznym do wybranej ściany:**

-    **cross_rebar_type**: Typ pręta zbrojeniowego dla poprzecznych prętów zbrojeniowych do zbrojenia płyt. Może mieć cztery wartości \"Pręty zbrojeniowe proste\", \"Pręty zbrojeniowe typu L\", \"Pręty zbrojeniowe typu U\", \"Pręty zbrojeniowe odgięte\".

-    **cross_front_cover**: Odległość między poprzecznym prętem zbrojeniowym a cross_face *(powierzchnia prostopadła do wybranej powierzchni)*.

-    **cross_rear_cover**: Tylna otulina dla zbrojenia poprzecznego prętów zbrojeniowych płyty.

-    **cross_left_cover**: Odległość między lewym końcem poprzecznego pręta zbrojeniowego a lewą ścianą konstrukcji.

-    **cross_right_cover**: Odległość między prawym końcem pręta zbrojeniowego a prawą powierzchnią konstrukcji względem cross_face.

-    **cross_top_cover**: Odległość między poprzecznymi prętami zbrojeniowymi od górnej powierzchni konstrukcji.

-    **cross_bottom_cover**: Odległość między poprzecznymi prętami zbrojeniowymi od dolnej powierzchni konstrukcji.

-    **cross_diameter**: Średnica poprzecznych prętów zbrojeniowych.

-    **cross_amount_spacing_check**: Jeśli jest ustawiona na {{True/pl}}, wartość cross_amount_spacing_value jest używana jako liczba prętów zbrojeniowych, w przeciwnym razie wartość cross_amount_spacing_value jest używana jako odstęp w prętach zbrojeniowych.

-    **cross_amount_spacing_value**: Zawiera liczbę prętów zbrojeniowych lub odstęp między prętami zbrojeniowymi w oparciu o wartość cross_amount_spacing_check.

-    **cross_rounding**: Wartość zaokrąglenia, która ma być zastosowana do narożników prętów, wyrażona w krotności cross_diameter.

-    **cross_bent_bar_length**: Reprezentuje długość ramienia wygiętego pręta zbrojeniowego, gdy cross_rebar_type to Przęt zbrojeniowy odgięty.

-    **cross_bent_bar_angle**: Reprezentuje kąt dla wygiętego pręta zbrojeniowego, gdy cross_rebar_type to Pręt zbrojeniowy odgięty.

-    **cross_distribution_rebars_check**:

Jeśli opcja ma wartość {{True/pl}}, dodaje pręty rozdzielcze dla prętów wygiętych krzyżowo. Domyślna wartość to {{False/pl}}.

-    **cross_distribution_rebars_diameter**: Średnica prętów zbrojeniowych dla prętów zbrojeniowych wygiętych krzyżowo.

-    **cross_distribution_rebars_amount_spacing_check**: Jeśli wartość jest ustawiona na {{True/pl}}, wówczas wartość cross_distribution_rebars_amount_spacing_value jest używana jako liczba prętów zbrojeniowych, w przeciwnym razie wartość cross_distribution_rebars_amount_spacing_value jest używana jako odstęp w cross_distribution_rebars. Wartość domyślna to {{True/pl}}.

-    **cross_distribution_rebars_amount_spacing_value**: Zawiera liczbę lub odstęp między prętami zbrojeniowymi dla jednej strony prętów zbrojeniowych o kształcie wygiętym krzyżowo w oparciu o wartość cross_distribution_rebars_check. Wartość domyślna to 2.

**Wspólne właściwości prętów równoległych i krzyżowych:**

-    `mesh_cover_along`: Może mieć dwie wartości \" Góra\", \"Dół\". Reprezentuje wyrównanie siatki zbrojeniowej wzdłuż górnej lub dolnej powierzchni konstrukcji.

-    `structure`: Obiekt konstrukcji Architektury. Domyślnie przyjmuje wartość Brak.

-    `facename`: wybrana ściana konstrukcji. Domyślnie przyjmuje wartość Brak.



### Edycja zbrojenia płyty o rozpiętości w jednym kierunku 

Właściwości zbrojenia płyty dla płyty rozpiętej w jednym kierunku można zmienić za pomocą funkcji `editSlabReinforcement` w następujący sposób:


```python
from SlabReinforcement.SlabReinforcement import editSlabReinforcement
SlabReinforcementGroup = editSlabReinforcement(
    SlabReinforcementGroup,
    parallel_rebar_type="StraightRebar",
    parallel_front_cover=20,
    parallel_rear_cover=20,
    parallel_left_cover=10,
    parallel_right_cover=10,
    parallel_top_cover=30,
    parallel_bottom_cover=20,
    parallel_diameter=8,
    parallel_amount_spacing_check=True,
    parallel_amount_spacing_value=10,
    cross_rebar_type="BentShapeRebar",
    cross_front_cover=20,
    cross_rear_cover=20,
    cross_left_cover=10,
    cross_right_cover=10,
    cross_top_cover=20,
    cross_bottom_cover=20,
    cross_diameter=8,
    cross_amount_spacing_check=True,
    cross_amount_spacing_value=15,
    cross_rounding=2,
    cross_bent_bar_length=150,
    cross_bent_bar_angle=135,
    cross_distribution_rebars_check = True,
    cross_distribution_rebars_diameter = 8,
    cross_distribution_rebars_amount_spacing_check = True,
    cross_distribution_rebars_amount_spacing_value = 4,
    mesh_cover_along = "Bottom",
    structure=App.getDocument("slab").getObject("Beam"),
    facename='Face4',
)
```

-    `slabReinforcementGroup`jest wcześniej utworzonym obiektem grupy `Slab Reinforcement`.

-   Pozostałe parametry są takie same jak wymagane przez funkcję `makeSingleTieFourRebars()`.

możesz zmienić dowolną właściwość, aby edytować zbrojenie płyty.



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Example Slab Spanning in One Direction/pl
