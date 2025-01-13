---
 GuiCommand:
   Name: Reinforcement StirrupRebar
   Name/pl: Zbrojenie: Strzemiona
   MenuLocation: 3D / BIM , Narzędzia zbrojenia , Strzemiona
   Workbenches: Reinforcement_Workbench/pl, BIM_Workbench/pl
   Version: 0.17
   SeeAlso: 
---

# Reinforcement StirrupRebar/pl



## Opis

Narzędzie **Strzemiona zbrojeniowe** pozwala użytkownikowi na utworzenie zestaw strzemion wzmacniających wewnątrz obiektu [konstrukcyjnego](Arch_Structure/pl.md).

To polecenie jest częścią [zewnętrznego środowiska pracy](External_workbenches/pl.md) [Zbrojenie](Reinforcement_Workbench/pl.md), które można zainstalować za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md).

<img alt="" src=images/Arch_Rebar_Stirrup_example.png  style="width:400px;"> 
*Jeden zestaw strzemion wzmacniających wewnątrz obiektu  [konstrukcji](Arch_Structure/pl.md).*



## Użycie

1.  Wybierz dowolną ścianę wcześniej utworzonego obiektu **<img src="images/Arch_Structure.svg" width=16px> [konstrukcji](Arch_Structure/pl.md)**.

2.  Następnie wybierz **<img src="images/Reinforcement_StirrupRebar.svg" width=16px> Strzemiona** z narzędzi zbrojenia.

3.  Po lewej stronie ekranu pojawi się [Panel zadań](Task_panel/pl.md), jak pokazano poniżej.

4.  Wybierz żądaną orientację.

5.  Wypełnij dane wejściowe, takie jak \"Lewa otulina\", \"Prawa otulina\", \"Górna otulina\", \"Dolna otulina\", \"Przednia otulina\", \"Kąt wygięcia\", \"Współczynnik wygięcia\", \"Zaokrąglenie\" i \"Średnica\" pręta zbrojeniowego.

6.  Wybierz tryb dystrybucji \"Ilość\" lub \"Rozstaw\".
    -   Jeśli wybrano \"Rozstaw\", użytkownik może również wybrać [rozstaw niestandardowy](Reinforcement_Custom_Spacing/pl.md).

7.  
    **Wybierz zaznaczoną ścianę**służy do weryfikacji lub zmiany powierzchni dla rozmieszczenia prętów zbrojeniowych.

8.  Kliknij **OK** lub **Zastosuj**, aby wygenerować pręty zbrojeniowe.

9.  Kliknij przycisk **Anuluj**, aby opuścić panel zadań.

<img alt="" src=images/StirrupDialog.png  style="width:250px;"> 
*Panel zadań dla narzędzia.*



## Właściwości

-    **Otulina przednia**: Odległość między prętem zbrojeniowym a wybraną powierzchnią.

-    **Otulina prawa**: Odległość między prawym końcem pręta zbrojeniowego a prawą ścianą konstrukcji.

-    **Otulina lewa**: Odległość między prawym końcem pręta zbrojeniowego a prawą ścianą konstrukcji: Odległość między lewym końcem pręta zbrojeniowego a lewą ścianą konstrukcji.

-    **Otulina dolna**: Odległość między prętami zbrojeniowymi a dolną ścianą konstrukcji.

-    **Otulina górna**: Odległość między prętami zbrojeniowymi od górnej powierzchni konstrukcji.

-    **Kąt wygięcia**: Kąt wygięcia określa kąt na końcach strzemion.

-    **Współczynnik wygięcia**: Współczynnik wygięcia określa długość końca strzemienia.

-    **Ilość**: Ilość prętów zbrojeniowych.

-    **Rozstaw**: Odległość między osiami każdego pręta.



## Tworzenie skryptów 


**Zobacz również:**

[Skrypty Architektury](Arch_API/pl.md), [Skrypty Zbrojenia](Reinforcement_API/pl.md) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Strzemiona** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji: 
```python
Rebar = makeStirrup(l_cover, r_cover, t_cover, b_cover, f_cover,
                    bentAngle, bentFactor, diameter, rounding, amount_spacing_check, amount_spacing_value,
                    structure=None, facename=None)
```

-   Tworzy obiekt `Rebar` z podanego `structure`, który jest [Arch Structure](Arch_Structure.md) i `facename`, który jest ścianą tej konstrukcji.
    -   Jeśli nie podano `structure` ani `facename`, jako dane wejściowe zostanie przyjęta ściana wybrana przez użytkownika.

-    `l_cover`, `r_cover`, `t_cover`, `b_cover` i `f_cover` są wewnętrznymi odległościami przesunięcia dla elementów zbrojenia względem powierzchni konstrukcji. Są to odpowiednio lewy, prawy, górny, dolny i przedni offset.

-    `diameter`to średnica prętów zbrojeniowych wewnątrz konstrukcji.

-    `rounding`to parametr określający promień gięcia prętów zbrojeniowych podczas tworzenia pętli.

-    `bentLength`i `bentAngle` definiują długość i kąt końcówki pętli zbrojenia.

-    `amount_spacing_check`jeśli ma wartość `True` utworzy tyle pętli zbrojenia ile podano w `amount_spacing_value`; jeśli ma wartość `False` utworzy pętle zbrojenia oddzielone wartością liczbową `amount_spacing_value`.

-    `amount_spacing_value`określa liczbę pętli zbrojenia lub wartość odstępu między nimi, w zależności od parametru `amount_spacing_check`.



### Przykład


```python
import Draft, Arch, Stirrup

# It doesn't work if the structure is not based on a face
# Structure = Arch.makeStructure(length=1000, width=400, height=400)

Rect = Draft.makeRectangle(400, 400)
Structure = Arch.makeStructure(Rect, height=1600)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = Stirrup.makeStirrup(20, 20, 20, 20, 20,
                            115, 4, 8, 2, True, 10, Structure, "Face6")
```



### Edycja zbrojenia 

Właściwości pręta zbrojeniowego można zmienić za pomocą poniższej funkcji:


```python
editStirrup(Rebar, l_cover, r_cover, t_cover, b_cover, f_cover,
            bentAngle, bentFactor, diameter, rounding, amount_spacing_check, amount_spacing_value,
            structure=None, facename=None)
```

-    `Rebar`jest wcześniej utworzonym obiektem `StraightRebar`.

-   Pozostałe parametry są takie same jak wymagane przez funkcję `makeStirrup()`.

-    `structure`i `facename` mogą zostać pominięte, aby pręt zbrojeniowy pozostał w oryginalnej strukturze.


```python
import Stirrup

Stirrup.editStirrup(Rebar, 20, 20, 20, 20, 50,
                    100, 4, 14, 8, True, 8)
```




{{BIM_Tools_navi}}



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement StirrupRebar/pl
