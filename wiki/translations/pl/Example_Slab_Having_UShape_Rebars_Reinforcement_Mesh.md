---
 TutorialInfo:l
   Topic: Przykładowa płyta z siatką prętów zbrojeniowych w kształcie litery U
   Level: Średnio zaawansowany
   Time: dowolny
   Author: Shiv Charan
   FCVersion: 0.20
   Files: nie dołączono
---

# Example Slab Having UShape Rebars Reinforcement Mesh/pl







## Opis

Narzędzie <img alt="" src=images/Reinforcement_SlabRebars.svg  style="width:24px;"> [Zbrojenie płyt](Reinforcement_SlabRebars/pl.md) pozwala użytkownikowi na tworzenie prętów zbrojeniowych wewnątrz obiektu [konstrukcji](Arch_Structure/pl.md) płyty.

To narzędzie jest częścią [zewnętrznego środowiska pracy](External_workbenches/pl.md) [Zbrojenie](Reinforcement_Workbench/pl.md), które można zainstalować za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md).

W tym przykładzie utworzymy zbrojenie płyty z prętami zbrojeniowymi w kształcie litery U dla obu kierunków, jak pokazano na poniższym rysunku.

<img alt="" src=images/U-shape_rebars_isometric_view.png  style="width:800px;"> 
*Przykład zbrojenia płyty prętami zbrojeniowymi w kształcie litery U w [konstrukcji](Arch_Structure/pl.md) płyty.*



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

5\. Wybierz typ pręta zbrojeniowego w kształcie U i inne dane wejściowe dla prętów zbrojeniowych w kierunku równoległym do wybranej powierzchni, jak pokazano na poniższym rysunku.

:   ![](images/U-shape_parallel_rebars_inputs.png )

:   
    
*Okno dialogowe dla zbrojenia płyty, zbrojenie w kierunku równoległym do wybranej ściany.*
    

6\. Teraz kliknij przycisk **Dalej** lub wybierz Pręty zbrojeniowe w widoku listy.

7\. Teraz wybierz typ pręta zbrojeniowego w kształcie U i inne żądane dane jako dane wejściowe dla prętów zbrojeniowych w kierunku poprzecznym wybranej powierzchni, jak pokazano na poniższym rysunku.

:   ![](images/U-Shape_rebars_in_cross_direction_inputs.png )

:   
    
*Okno dialogowe zbrojenia płyty prętami zbrojeniowymi w kierunku poprzecznym wybranej ściany.*
    

11\. Kliknij **OK** lub **Zastosuj** lub **Zakończ**, aby wygenerować zbrojenie płyty.

9\. Kliknij **Anuluj**, aby zamknąć okno dialogowe.



## Właściwości stosowane do zbrojenia płyt prętami zbrojeniowymi w kształcie U 

**Właściwości prętów zbrojeniowych w kierunku równoległym do wybranej ściany:**.

-   {{ PropertyData\|Pokrycie siatki wzdłuż}}: Reprezentuje wyrównanie siatki zbrojeniowej wzdłuż górnej lub dolnej powierzchni konstrukcji. Może mieć dwie wartości \"Góra\" i \"Dół\".
-   {{ PropertyData\|Typ pręta}}: Typ prętów zbrojeniowych dla równoległych prętów zbrojeniowych do zbrojenia płyt. Może mieć cztery wartości \"Pręty zbrojeniowe proste\", \"Pręty zbrojeniowe typu L\", \"Pręty zbrojeniowe typu U\", \"Pręty zbrojeniowe odgięte\".
-   {{ PropertyData\|Otulina przednia}}: Odległość między równoległym prętem zbrojeniowym a wybraną powierzchnią czołową.
-   {{ PropertyData\|Otulina lewa}}: Odległość między lewym końcem równoległego pręta zbrojeniowego a lewą ścianą konstrukcji.
-   {{ PropertyData\|Otulina prawa}}: Odległość między prawym końcem równoległego pręta zbrojeniowego a prawą ścianą konstrukcji.
-   {{ PropertyData\|Otulina dolna}}: Odległość między równoległymi prętami zbrojeniowymi od dolnej powierzchni konstrukcji.
-   {{ PropertyData\|Otulina górna}}: Odległość między równoległymi prętami zbrojeniowymi od górnej powierzchni konstrukcji.
-   {{ PropertyData\|Otulina tylna}}: Tylna osłona dla zbrojenia płyty równoległymi prętami zbrojeniowymi.
-   {{ PropertyData\|Średnica}}: Średnica równoległych prętów zbrojeniowych.
-   {{ PropertyData\|Zaokrąglenie}}: Wartość zaokrąglenia, która zostanie zastosowana do narożników prętów, wyrażona w krotności średnicy równoległych prętów zbrojeniowych.
-   {{ PropertyData\|Ilość}}: Zawiera liczbę równoległych prętów zbrojeniowych.
-   {{ PropertyData\|Odstęp}}: Zawiera odstępy między równoległymi prętami zbrojeniowymi.

**Właściwości prętów zbrojeniowych w kierunku poprzecznym do wybranej ściany:**

-   {{ PropertyData\|Typ pręta}}: Typ prętów zbrojeniowych dla równoległych prętów zbrojeniowych do zbrojenia płyt. Może mieć cztery wartości \"Pręty zbrojeniowe proste\", \"Pręty zbrojeniowe typu L\", \"Pręty zbrojeniowe typu U\", \"Pręty zbrojeniowe odgięte\".
-   {{ PropertyData\|Otulina przednia}}: Odległość między równoległym prętem zbrojeniowym a wybraną powierzchnią czołową.
-   {{ PropertyData\|Otulina lewa}}: Odległość między lewym końcem równoległego pręta zbrojeniowego a lewą ścianą konstrukcji.
-   {{ PropertyData\|Otulina prawa}}: Odległość między prawym końcem równoległego pręta zbrojeniowego a prawą ścianą konstrukcji.
-   {{ PropertyData\|Otulina dolna}}: Odległość między równoległymi prętami zbrojeniowymi od dolnej powierzchni konstrukcji.
-   {{ PropertyData\|Otulina górna}}: Odległość między równoległymi prętami zbrojeniowymi od górnej powierzchni konstrukcji.
-   {{ PropertyData\|Otulina tylna}}: Tylna osłona dla zbrojenia płyty równoległymi prętami zbrojeniowymi.
-   {{ PropertyData\|Średnica}}: Średnica równoległych prętów zbrojeniowych.
-   {{ PropertyData\|Zaokrąglenie}}: Wartość zaokrąglenia, która zostanie zastosowana do narożników prętów, wyrażona w krotności średnicy równoległych prętów zbrojeniowych.
-   {{ PropertyData\|Ilość}}: Zawiera liczbę równoległych prętów zbrojeniowych.
-   {{ PropertyData\|Odstęp}}: Zawiera odstępy między równoległymi prętami zbrojeniowymi.



## Tworzenie skryptów 


**Zobacz również:**

[Skrypty Architektury](Arch_API/pl.md), [Skrypty Zbrojenia](Reinforcement_API/pl.md) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Zbrojenie płyt** może być używane z konsoli środowiska [Python](Python/pl.md) za pomocą następującej funkcji:



### Tworzenie zbrojenia płyty prętami zbrojeniowymi w kształcie litery U 

Aby utworzyć zbrojenie płyty w kształcie litery U, jak pokazano na powyższych rysunkach, można użyć funkcji `makeSlabReinforcement` w następujący sposób:


```python
from SlabReinforcement.SlabReinforcement import makeSlabReinforcement
SlabReinforcementGroup = makeSlabReinforcement(
    parallel_rebar_type="UShapeRebar",
    parallel_front_cover=20,
    parallel_rear_cover=20,
    parallel_left_cover=10,
    parallel_right_cover=10,
    parallel_top_cover=30,
    parallel_bottom_cover=20,
    parallel_rounding=2,
    parallel_diameter=8,
    parallel_amount_spacing_check=True,
    parallel_amount_spacing_value=12,
    cross_rebar_type="UShapeRebar",
    cross_front_cover=20,
    cross_rear_cover=20,
    cross_left_cover=10,
    cross_right_cover=10,
    cross_top_cover=20,
    cross_bottom_cover=20,
    cross_rounding=2,
    cross_diameter=8,
    cross_amount_spacing_check=True,
    cross_amount_spacing_value=12,
    mesh_cover_along = "Bottom",
    structure=App.getDocument("slab").getObject("Beam"),
    facename='Face4',
)
```

-   Tworzy obiekt `SlabReinforcementGroup` dla zbrojenia płyty z prętami zbrojeniowymi w kształcie litery U dla podanego obiektu `structure`, który jest [konstrukcją](Arch_Structure/pl.md) płyty i obiektrm `facename`, który jest powierzchnią tej konstrukcji.
    -   Jeśli nie podano `structure` ani `facename`, jako dane wejściowe przyjmowana jest ściana wybrana przez użytkownika.

**Właściwości stosowane do zbrojenia płyt z prętami zbrojeniowymi w kształcie litery U do zbrojenia za pomocą skryptów**

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

-    **parallel_rounding**: Wartość zaokrąglenia, która zostanie zastosowana do narożników prętów, wyrażona w wielokrotności parallel_diameter.

**Właściwości prętów zbrojeniowych w kierunku poprzecznym do wybranej ściany:**

-    **cross_rebar_type**: Typ pręta zbrojeniowego dla poprzecznych prętów zbrojeniowych do zbrojenia płyt. Może mieć cztery wartości \"Pręty zbrojeniowe proste\", \"Pręty zbrojeniowe typu L\", \"Pręty zbrojeniowe typu U\", \"Pręty zbrojeniowe odgięte\".

-    **cross_front_cover**: Odległość między poprzecznym prętem zbrojeniowym a cross_face (powierzchnia prostopadła do wybranej powierzchni).

-    **cross_rear_cover**: Tylna otulina dla zbrojenia poprzecznego prętów zbrojeniowych płyty.

-    **cross_left_cover**: Odległość między lewym końcem poprzecznego pręta zbrojeniowego a lewą ścianą konstrukcji.

-    **cross_right_cover**: Odległość między prawym końcem pręta zbrojeniowego a prawą powierzchnią konstrukcji względem cross_face.

-    **cross_top_cover**: Odległość między poprzecznymi prętami zbrojeniowymi od górnej powierzchni konstrukcji.

-    **cross_bottom_cover**: Odległość między poprzecznymi prętami zbrojeniowymi od dolnej powierzchni konstrukcji.

-    **cross_diameter**: Średnica poprzecznych prętów zbrojeniowych.

-    **cross_amount_spacing_check**: Jeśli jest ustawiona na {{True/pl}}, wartość cross_amount_spacing_value jest używana jako liczba prętów zbrojeniowych, w przeciwnym razie wartość cross_amount_spacing_value jest używana jako odstęp w prętach zbrojeniowych.

-    **cross_amount_spacing_value**: Zawiera liczbę prętów zbrojeniowych lub odstęp między prętami zbrojeniowymi w oparciu o wartość cross_amount_spacing_check.

-    **cross_rounding**: Wartość zaokrąglenia, która ma być zastosowana do narożników prętów, wyrażona w krotności cross_diameter.

**Wspólne właściwości prętów równoległych i krzyżowych:**

-    `mesh_cover_along`: Może mieć dwie wartości \" Góra\", \"Dół\". Reprezentuje wyrównanie siatki zbrojeniowej wzdłuż górnej lub dolnej powierzchni konstrukcji.

-    `structure`: Obiekt konstrukcji Architektury. Domyślnie przyjmuje wartość Brak.

-    `facename`: wybrana ściana konstrukcji. Domyślnie przyjmuje wartość Brak.



### Edycja zbrojenia płyty z prętami zbrojeniowymi w kształcie litery U 

Właściwości zbrojenia płyty z prętami zbrojeniowymi w kształcie litery u można zmienić za pomocą funkcji `editSlabReinforcement` w następujący sposób:


```python
from SlabReinforcement.SlabReinforcement import editSlabReinforcement
SlabReinforcementGroup = editSlabReinforcement(
    SlabReinforcementGroup,
    parallel_rebar_type="UShapeRebar",
    parallel_front_cover=20,
    parallel_rear_cover=20,
    parallel_left_cover=10,
    parallel_right_cover=10,
    parallel_top_cover=30,
    parallel_bottom_cover=20,
    parallel_rounding=2,
    parallel_diameter=8,
    parallel_amount_spacing_check=True,
    parallel_amount_spacing_value=15,
    cross_rebar_type="UShapeRebar",
    cross_front_cover=20,
    cross_rear_cover=20,
    cross_left_cover=10,
    cross_right_cover=10,
    cross_top_cover=20,
    cross_bottom_cover=20,
    cross_rounding=2,
    cross_diameter=8,
    cross_amount_spacing_check=True,
    cross_amount_spacing_value=15,
    mesh_cover_along = "Bottom",
    structure=App.getDocument("slab").getObject("Beam"),
    facename='Face4',
)
```

-    `slabReinforcementGroup`jest wcześniej utworzonym obiektem grupy `Slab Reinforcement`.

-   Pozostałe parametry są takie same jak wymagane przez funkcję `makeSingleTieFourRebars()`.

możesz zmienić dowolną właściwość, aby edytować zbrojenie płyty.



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Example Slab Having UShape Rebars Reinforcement Mesh/pl
