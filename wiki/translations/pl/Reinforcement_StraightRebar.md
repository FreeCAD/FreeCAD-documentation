---
 GuiCommand:
   Name: Reinforcement StraightRebar
   Name/pl: BIM: Zbrojenie stóp fundamentowych
   MenuLocation: 3D / BIM , Narzędzia zbrojenia , Pręty zbrojeniowe proste
   Workbenches: Reinforcement_Workbench/pl, BIM_Workbench/pl
   Version: 0.17
   SeeAlso: 
---

# Reinforcement StraightRebar/pl



## Opis

Narzędzie **Pręty zbrojeniowe proste** pozwala użytkownikowi na utworzenie zestawu prostych prętów zbrojeniowych wewnątrz obiektu [konstrukcyjnego](Arch_Structure/pl.md).

To polecenie jest częścią [zewnętrznego środowiska pracy](External_workbenches/pl.md) [Zbrojenie](Reinforcement_Workbench/pl.md), które można zainstalować za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md) poprzez menu **Przybory → Menadżera dodatków → Zbrojenie**.

<img alt="" src=images/Arch_Rebar_Straight_example.png  style="width:400px;"> 
*Dwa zestawy prostych prętów zbrojeniowych wewnątrz [konstrukcji](Arch_Structure/pl.md)*



## Użycie

1.  Wybierz dowolną ścianę wcześniej utworzonego obiektu **<img src="images/Arch_Structure.svg" width=16px> [konstrukcji](Arch_Structure/pl.md)**.

2.  Następnie wybierz **<img src="images/Reinforcement_StraightRebar.svg" width=16px> '''Pręty zbrojeniowe proste'''** z narzędzi zbrojenia.

3.  Po lewej stronie ekranu pojawi się [Panel zadań](Panel_zadań/pl.md), jak pokazano poniżej.

4.  Wybierz żądaną orientację.

5.  Podaj dane wejściowe, takie jak \"Otulina z przodu\", \"Otulina z prawej strony\", \"Otulina z lewej strony\", \"Otulina dolna\" i \"Średnica\" pręta zbrojeniowego.

6.  Wybierz tryb dystrybucji \"Ilość\" lub \"Rozstaw\".

7.  Jeśli wybrano rozstaw, użytkownik może również wybrać [Rozstaw](Reinforcement_Custom_Spacing/pl.md).

8.  
    **Wybierz zaznaczoną ścianę**służy do weryfikacji lub zmiany ściany dla rozmieszczenia prętów zbrojeniowych.

9.  Kliknij **OK** lub **Zastosuj**, aby wygenerować pręty zbrojeniowe.

10. Kliknij przycisk **Anuluj**, aby opuścić panel zadań.

<img alt="" src=images/StraightRebarDialog.png  style="width:250px;"> 
*Panel zadań dla narzędzia.*



## Właściwości

-    **Orientacja**: Decyduje o orientacji pręta zbrojeniowego *(jak dół, góra, prawo i lewo)*.

-    **Otulina z przodu**: Odległość między prętem zbrojeniowym a wybraną powierzchnią czołową.

-    **Prawa otulina**: Odległość między prawym końcem pręta zbrojeniowego a prawą ścianą konstrukcji.

-    **Lewa otulina**: Odległość między lewym końcem pręta zbrojeniowego a lewą ścianą konstrukcji.

-    **Otulina wzdłuż**: odległość między lewym końcem pręta zbrojeniowego a lewą ścianą konstrukcji: Ta właściwość umożliwia użytkownikowi określenie górnego lub dolnego pokrycia.

-    **Otulina dolna**: Odległość między prętami zbrojeniowymi od dolnej powierzchni konstrukcji.

-    **Otulina górna**: Odległość między prętami zbrojeniowymi od górnej powierzchni konstrukcji.

-    **Ilość**: Ilość prętów zbrojeniowych.

-    **Rozstaw**: Odległość między osiami każdego pręta.



## Tworzenie skryptów 


**Zobacz również:**

[Skrypty Architektury](Arch_API/pl.md), [Skrypty Zbrojenia](Reinforcement_API/pl.md) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Pręty zbrojeniowe proste** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:


```python
Rebar = makeStraightRebar(f_cover, coverAlong, rt_cover, lb_cover,
                          diameter, amount_spacing_check, amount_spacing_value, orientation="Horizontal",
                          structure=None, facename=None)
```

-   Tworzy obiekt `Rebar` z podanego `structure`, który jest [konstrukcją architektury](Arch_Structure/pl.md), i `facename`, który jest ścianą tej konstrukcji.
    -   Jeśli nie podano obiektu `structure` ani `facename`, jako dane wejściowe zostanie przyjęta ściana wybrana przez użytkownika.

-    `f_cover`, `coverAlong`, `rt_cover` i `lb_cover` są wewnętrznymi odległościami przesunięcia dla elementów zbrojenia względem powierzchni konstrukcji.

    -   
        `f_cover`
        
        to przesunięcie otuliny czołowej.

    -   
        `coverAlong`
        
        to krotka `(position, value)` określająca wartość przesunięcia w jednej pozycji *(góra, dół, lewo, prawo)* w zależności od parametru `orientation`.

    -   
        `rt_cover`
        
        jest prawym lub górnym przesunięciem otuliny, w zależności od wartości `coverAlong` i `orientation`.

    -   
        `lb_cover`
        
        jest lewym lub dolnym przesunięciem otuliny, w zależności od wartości `coverAlong` i `orientation`.

-    `diameter`to średnica prętów zbrojeniowych wewnątrz konstrukcji.

-    `amount_spacing_check`, jeśli ma wartość `True`, utworzy tyle prętów zbrojeniowych, ile podano w parametrze `amount_spacing_value`. Jeśli ma wartość `False`, utworzy pręty zbrojeniowe oddzielone wartością liczbową `amount_spacing_value`.

-    `amount_spacing_value`określa liczbę prętów zbrojenia lub wartość odstępu między nimi, w zależności od wartości parametru `amount_spacing_check`.

-    `orientation`określa orientację pręta zbrojeniowego. Może mieć wartość `"Horizontal"` lub `"Vertical"`.

W zależności od orientacji pręta zbrojeniowego, funkcja ta może być wywołana na dwa ogólne sposoby poprzez odpowiednie ustawienie parametru `coverAlong`.



### Pręty zbrojeniowe są poziome 


```python
Rebar = makeStraightRebar(f_cover, ("Top Side", value), right_cover, left_cover, ...)
Rebar = makeStraightRebar(f_cover, ("Bottom Side", value), right_cover, left_cover, ...)
```

-    `coverAlong`jest krotką z `value` przesunięcia `"Top Side"` lub `"Bottom Side"` .

-   W tym przypadku `rt_cover` odnosi się do przesunięcia `right_cover`, a `lb_cover` odnosi się do przesunięcia `left_cover`.



### Pręty zbrojeniowe są pionowe 


```python
Rebar = makeStraightRebar(f_cover, ("Left Side", value), top_cover, bottom_cover, ...)
Rebar = makeStraightRebar(f_cover, ("Right Side", value), top_cover, bottom_cover, ...)
```

-    `coverAlong`jest krotką z `value` przesunięcia `"Left Side"` lub `"Right Side"` `value`.

-   W tym przypadku `rt_cover` odnosi się do przesunięcia `top_cover`, a `lb_cover` odnosi się do przesunięcia `bottom_cover`.



### Przykład poziomy 


```python
import Arch, Draft, StraightRebar

Structure = Arch.makeStructure(length=1000, width=1000, height=400)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = StraightRebar.makeStraightRebar(50, ("Bottom Side", 20), 100, 100,
                                        12, True, 5, "Horizontal", Structure, "Face4")
Rebar.ViewObject.ShapeColor = (0.9, 0.0, 0.0)

Rebar2 = StraightRebar.makeStraightRebar(50, ("Bottom Side", 50), 100, 100,
                                         12, True, 5, "Horizontal", Structure, "Face6")
Rebar2.ViewObject.ShapeColor = (0.0, 0.0, 0.9)
```



### Przykład pionowy 


```python
import Arch, Draft, StraightRebar

Structure2 = Arch.makeStructure(length=1000, width=1000, height=400)
Structure2.ViewObject.Transparency = 80
Draft.move(Structure2, FreeCAD.Vector(1500, 0, 0))
FreeCAD.ActiveDocument.recompute()

Rebar3 = StraightRebar.makeStraightRebar(50, ("Left Side", 20), 100, 100,
                                         12, True, 5, "Vertical", Structure2, "Face4")
Rebar3.ViewObject.ShapeColor = (0.9, 0.5, 0.0)

Rebar4 = StraightRebar.makeStraightRebar(50, ("Left Side", 50), 100, 100,
                                         12, True, 5, "Vertical", Structure2, "Face6")
Rebar4.ViewObject.ShapeColor = (0.0, 0.5, 0.5)
```



### Edycja prętów zbrojeniowych 

Właściwości pręta zbrojeniowego można zmienić za pomocą poniższej funkcji:


```python
editStraightRebar(Rebar, f_cover, coverAlong, rt_cover, lb_cover,
                  diameter, amount_spacing_check, amount_spacing_value, orientation,
                  structure=None, facename=None)
```

-    `Rebar`jest wcześniej utworzonym obiektem `StraightRebar`.

-   Pozostałe parametry są takie same jak wymagane przez funkcję `makeStraightRebar()`.

-    `structure`i `facename` mogą zostać pominięte, aby pręt zbrojeniowy pozostał w oryginalnej strukturze.

Przykład:


```python
import StraightRebar

StraightRebar.editStraightRebar(Rebar, 50, ("Top Side", 20), 100, 100,
                                24, True, 7, "Horizontal")

StraightRebar.editStraightRebar(Rebar2, 50, ("Top Side", 50), 100, 100,
                                24, True, 7, "Horizontal")

StraightRebar.editStraightRebar(Rebar3, 50, ("Right Side", 20), 100, 100,
                                24, True, 7, "Vertical")

StraightRebar.editStraightRebar(Rebar4, 50, ("Right Side", 50), 100, 100,
                                24, True, 7, "Vertical")
```



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > [BIM](Category_BIM.md) > Reinforcement StraightRebar/pl
