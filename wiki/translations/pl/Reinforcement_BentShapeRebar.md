---
 GuiCommand:
   Name: Reinforcement BentShapeRebar
   Name/pl: Zbrojenie: Pręty zbrojeniowe wygięte
   MenuLocation: 3D / BIM , Narzędzia zbrojenia , Pręty zbrojeniowe wygięte
   Workbenches: Reinforcement_Workbench/pl, BIM_Workbench/pl
   Version: 0.17
   SeeAlso: 
---

# Reinforcement BentShapeRebar/pl



## Opis

Narzędzie **Pręty zbrojeniowe odgięte** pozwala użytkownikowi na utworzenie zestawu prętów zbrojeniowych odgiętych, wewnątrz obiektu [konstrukcji](Arch_Structure/pl.md).

To polecenie jest częścią [zewnętrznego środowiska pracy](External_workbenches/pl.md) [Zbrojenie](Reinforcement_Workbench/pl.md), które można zainstalować za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md) poprzez menu **Przybory → Menadżera dodatków → Zbrojenie**.

<img alt="" src=images/Arch_Rebar_BentShape_example.png  style="width:400px;"> 
*Dwa zestawy odgiętych prętów zbrojeniowych wewnątrz [konstrukcji](Arch_Structure/pl.md)*



## Użycie

1.  Wybierz dowolną ścianę wcześniej utworzonego obiektu **<img src="images/Arch_Structure.svg" width=16px> [konstrukcji](Arch_Structure/pl.md)** obiektu.

2.  Następnie wybierz **<img src="images/Reinforcement_BentShapeRebar.svg" width=16px> '''Pręty zbrojeniowe odgięte'''** z narzędzi prętów zbrojeniowych.

3.  Po lewej stronie ekranu pojawi się [panel zadań](Task_panel/pl.md), jak pokazano poniżej.

4.  Wybierz żądaną orientację.

5.  Wypełnij dane wejściowe, takie jak \"Lewa otulina\", \"Prawa otulina\", \"Górna otulina\", \"Dolna otulina\", \"Przednia otulina\", \"Kąt wygięcia\", \"Współczynnik wygięcia\", \"Zaokrąglenie\" i \"Średnica\" pręta zbrojeniowego.

6.  Wybierz tryb dystrybucji \"Ilość\" lub \"Rozstaw\".
    -   Jeśli wybrano \"Rozstaw\", użytkownik może również wybrać [Rozstaw niestandardowy](Reinforcement_Custom_Spacing/pl.md).

7.  
    **Wybierz zaznaczoną ścianę**służy do weryfikacji lub zmiany powierzchni dla rozmieszczenia prętów zbrojeniowych.

8.  Kliknij **OK** lub **Zastosuj**, aby wygenerować pręty zbrojeniowe.

9.  Kliknij przycisk **Anuluj**, aby opuścić panel zadań.

<img alt="" src=images/BentShapeDialog.png  style="width:250px;"> 
*Panel zadań dla narzędzia.*



## Właściwości

Otulina\* **Orientacja**: Decyduje o orientacji pręta zbrojeniowego *(jak dół, góra, prawo i lewo)*.

-    **Otulina przednia**: Odległość między prętem zbrojeniowym a wybraną powierzchnią czołową.

-    **Otulina prawa**: Odległość między prawym końcem pręta zbrojeniowego a prawą ścianą konstrukcji.

-    **Otulina lewa**: Odległość między prawym końcem pręta zbrojeniowego a prawą ścianą konstrukcji: \* **Zaokrąglenie**: Odległość między lewym końcem pręta zbrojeniowego a lewą ścianą konstrukcji.

-    **Otulina dolna**: Odległość między prętami zbrojeniowymi a dolną ścianą konstrukcji.

-    **Otulina górna**: Odległość między prętami zbrojeniowymi od górnej powierzchni konstrukcji.

-    **Zaokrąglenie**: Wartość zaokrąglenia stosowana do narożników prętów, wyrażona jako wielokrotność średnicy.

-    **Ilość**: Ilość prętów zbrojeniowych.

-    **Rozstaw**: Odległość między osiami każdego pręta.



## Tworzenie skryptów 


**Zobacz również:**

[Skrypty Architektury](Arch_API/pl.md), [Skrypty Zbrojenia](Reinforcement_API/pl.md) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Pręty zbrojeniowe odgięte** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji: 
```python
Rebar = makeBentShapeRebar(f_cover, b_cover, l_cover, r_cover,
                           diameter, t_cover, bentLength, bentAngle, rounding, amount_spacing_check, amount_spacing_value, orientation="Bottom",
                           structure=None, facename=None)
```

-   Tworzy obiekt `Rebar` z podanego `structure`, który jest [konstrukcją architektury](Arch_Structure/pl.md) i `facename`, który jest ścianą tej konstrukcji.
    -   Jeśli nie podano `structure` ani `facename`, jako dane wejściowe zostanie przyjęta ściana wybrana przez użytkownika.

-    `f_cover`, `b_cover`, `l_cover`, `r_cover` i `t_cover` są wewnętrznymi odległościami przesunięcia dla elementów zbrojenia względem powierzchni konstrukcji. Są to odpowiednio przednie, dolne, lewe, prawe i górne przesunięcia.

-    `diameter`to średnica prętów zbrojeniowych wewnątrz konstrukcji.

-    `rounding`to parametr określający promień gięcia środkowych prętów zbrojenia.

-    `bentLength`i `bentAngle` definiują długość końcówki prętów zbrojeniowych i kąt zgięcia od prętów środkowych.

-    `amount_spacing_check`jeśli ma wartość `True` utworzy tyle prętów zbrojeniowych ile podano w `amount_spacing_value`; jeśli ma wartość `False` utworzy pręty zbrojeniowe oddzielone wartością liczbową `amount_spacing_value`.

-    `amount_spacing_value`określa liczbę prętów zbrojenia lub wartość odstępu między nimi, w zależności od `amount_spacing_check`.

-    `orientation`określa orientację pręta zbrojeniowego; może to być `"Dół"`, `"Góra"`, `"Lewa"` lub `"Prawa"`.



### Przykład


```python
import FreeCAD, Arch, BentShapeRebar

Structure = Arch.makeStructure(length=1000, width=1000, height=100)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = BentShapeRebar.makeBentShapeRebar(50, 20, 20, 20,
                                          8, 40, 100, 135, 2, True, 4, "Bottom", Structure, "Face4")
Rebar.ViewObject.ShapeColor = (0.9, 0.0, 0.0)

Rebar2 = BentShapeRebar.makeBentShapeRebar(50, 40, 20, 20,
                                           8, 20, 100, 135, 2, True, 4, "Bottom", Structure, "Face6")
Rebar2.ViewObject.ShapeColor = (0.0, 0.0, 0.9) 
```



### Edycja zbrojenia 

Właściwości pręta zbrojeniowego można zmienić za pomocą poniższej funkcji:


```python
editBentShapeRebar(Rebar, f_cover, b_cover, l_cover, r_cover,
                   diameter, t_cover, bentLength, bentAngle, rounding, amount_spacing_check, amount_spacing_value, orientation,
                   structure=None, facename=None)
```

-    `Rebar`jest wcześniej utworzonym obiektem `BentShapeRebar`.

-   Pozostałe parametry są takie same jak wymagane przez funkcję `makeUShapeRebar()`.

-    `structure`i `facename` mogą zostać pominięte, aby pręt zbrojeniowy pozostał w oryginalnej konstrukcji.


```python
import BentShapeRebar

BentShapeRebar.editBentShapeRebar(Rebar, 50, 20, 20, 20,
                                  12, 20, 100, 155, 2, True, 6, "Top")

BentShapeRebar.editBentShapeRebar(Rebar2, 50, 35, 20, 20,
                                  12, 35, 100, 155, 2, True, 6, "Top")
```



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement BentShapeRebar/pl
