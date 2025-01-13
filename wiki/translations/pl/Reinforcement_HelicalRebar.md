---
 GuiCommand:
   Name: Reinforcement HelicalRebar
   Name/pl: Zbrojenie: Pręty zbrojeniowe spiralne
   MenuLocation: 3D / BIM , Narzędzia zbrojenia , Pręty zbrojeniowe spiralne
   Workbenches: Reinforcement_Workbench/pl, BIM_Workbench/pl
   Version: 0.17
   SeeAlso: 
---

# Reinforcement HelicalRebar/pl



## Opis

Narzędzie **Pręty zbrojeniowe spiralne** pozwala użytkownikowi na utworzenie zestawu spiralnych prętów zbrojeniowych, wewnątrz obiektu [konstrukcji](Arch_Structure/pl.md).

To polecenie jest częścią [zewnętrznego środowiska pracy](External_workbenches/pl.md) [Zbrojenie](Reinforcement_Workbench/pl.md), które można zainstalować za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md) poprzez menu **Przybory → Menadżera dodatków → Zbrojenie**.

:   <img alt="" src=images/Arch_Rebar_Helical_example.png  style="width:80px;">



*Jeden ciągły spiralny pręt zbrojeniowy wewnątrz [konstrukcji](Arch_Structure/pl.md)*



## Użycie

1.  Wybierz dowolną ścianę wcześniej utworzonego obiektu **<img src="images/Arch_Structure.svg" width=16px> [konstrukcji](Arch_Structure/pl.md)**.

2.  Następnie wybierz **<img src="images/Reinforcement_HelicalRebar.svg" width=16px> '''Pręty zbrojeniowe spiralne'''** z narzędzi zbrojenia.

3.  Po lewej stronie ekranu pojawi się [panel zadań](Task_panel/pl.md), jak pokazano poniżej.

4.  Wybierz żądaną orientację.

5.  Wypełnij dane wejściowe, takie jak \"Lewa otulina\", \"Prawa otulina\", \"Górna otulina\", \"Dolna otulina\", \"Przednia otulina\", \"Kąt wygięcia\", \"Współczynnik wygięcia\", \"Zaokrąglenie\" i \"Średnica\" pręta zbrojeniowego.

6.  Wybierz tryb dystrybucji \"Ilość\" lub \"Rozstaw\".
    -   Jeśli wybrano \"Rozstaw\", użytkownik może również wybrać [Rozstaw niestandardowy](Reinforcement_Custom_Spacing/pl.md).

7.  
    **Wybierz zaznaczoną ścianę**służy do weryfikacji lub zmiany powierzchni dla rozmieszczenia prętów zbrojeniowych.

8.  Kliknij **OK** lub **Zastosuj**, aby wygenerować pręty zbrojeniowe.

9.  Kliknij przycisk **Anuluj**, aby opuścić panel zadań.

<img alt="" src=images/HelicalRebarDialog.png  style="width:250px;"> 
*Panel zadań dla narzędzia.*



## Właściwości

-    **Otulina boczna**: Odległość między prętem zbrojeniowym a zakrzywioną powierzchnią.

-    **Otulina górna**: Odległość między prętami zbrojeniowymi od górnej ściany konstrukcji.

-    **Otulina dolna**: Odległość między prętami zbrojeniowymi od dolnej powierzchni konstrukcji.

-    **Skok**: Skok spirali to wysokość jednego pełnego obrotu spirali, mierzona równolegle do osi spirali.

-    **Średnica**: Średnica pręta zbrojeniowego.



## Tworzenie skryptów 


**Zobacz również:**

[Skrypty Architektury](Arch_API/pl.md), [Skrypty Zbrojenia](Reinforcement_API/pl.md) oraz [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Pręty zbrojeniowe spiralne** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:


```python
Rebar = makeHelicalRebar(s_cover, b_cover, diameter, t_cover, pitch, structure=None, facename=None)
```

-   Tworzy obiekt `Rebar` z podanego `structure`, który jest [konstrukcja architektury](Arch_Structure/pl.md) i `facename`, który jest ścianą tej konstrukcji.
    -   Jeśli nie podano `structure` ani `facename`, jako dane wejściowe zostanie przyjęta ściana wybrana przez użytkownika.

-    `s_cover`, `b_cover` i `t_cover` są wewnętrznymi odległościami przesunięcia pręta zbrojeniowego względem powierzchni konstrukcji. Są to odpowiednio przesunięcia boczne, dolne i górne.

-    `diameter`to średnica spirali zbrojenia wewnątrz konstrukcji.

-    `pitch`to parametr określający, jak blisko lub daleko od siebie znajdują się poszczególne pętle spirali.



### Przykład


```python
import FreeCAD, Draft, Arch, HelicalRebar

Circle = Draft.makeCircle(radius=250)
Structure = Arch.makeStructure(Circle)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

Rebar = HelicalRebar.makeHelicalRebar(10, 50, 8, 50, 50, structure, "Face2")
```



### Edycja zbrojenia 

Właściwości pręta zbrojeniowego można zmienić za pomocą poniższej funkcji:


```python
editHelicalRebar(Rebar, s_cover, b_cover, diameter, t_cover, pitch, structure=None, facename=None)
```

-    `Rebar`jest wcześniej utworzonym obiektem `HelicalRebar`.

-   Pozostałe parametry są takie same jak wymagane przez funkcję `makeHelicalRebar()`.

-    `structure`i `facename` mogą zostać pominięte, aby pręt zbrojeniowy pozostał w oryginalnej konstrukcji.


```python
import HelicalRebar

HelicalRebar.editHelicalRebar(Rebar, 20, 100, 20, 20, 100)
```




{{BIM_Tools_navi}}



---
⏵ [documentation index](../README.md) > [External_Command_Reference](Category_External_Command_Reference.md) > [Reinforcement](Category_Reinforcement.md) > Reinforcement HelicalRebar/pl
