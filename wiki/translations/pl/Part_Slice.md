---
 GuiCommand:
   Name: Part Slice
   Name/pl: Część: Rozbij na kształty złożenia
   MenuLocation: Część , Rozdziel , Rozbij na kształty złożenia
   Workbenches: Part_Workbench/pl
   Version: 0.17
   SeeAlso: Part_BooleanFragments/pl, Part_XOR/pl, Part_CompJoinFeatures/pl, Part_Boolean/pl
---

# Part Slice/pl



## Opis

Narzędzie <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Rozbij na kształty złożenia](Part_Slice/pl.md) znane również jako **Pokrój na składniki** służy do dzielenia kształtów przez przecięcie z innymi kształtami. Na przykład dla prostopadłościanu i płaszczyzny zostanie utworzone złożenie dwóch brył.

![600px](images/Part_Slice_Demo.png)



* Powyżej: elementy zostały później ręcznie rozsunięte, aby uwidocznić cięcie.*

Istnieją dwa polecenia do przecinania kształtu: <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Rozbij](Part_SliceApart/pl.md) i <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Rozbij na kształty złożenia](Part_Slice.md). Oba tworzą parametryczną cechę *Rozbicia*, która umieszcza pokrojone kawałki w złożeniu. Jednakże <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Rozbij](Part_SliceApart/pl.md) rozbija powstałe złożenie na oddzielne obiekty. \"Rozbij na kształty złożenia\" jest w pełni parametryczne i nie powoduje żadnych problemów, gdy zmienia się liczba części. Natomiast \"Rozbij\" nie aktualizuje liczby obiektów wraz ze zmianą liczby części.

Kształt wyjściowy zajmuje tę samą przestrzeń co oryginał. Jest on jednak dzielony tam, gdzie przecina się z innymi kształtami. Podzielone części są umieszczane w bryle złożonej *(lub bryle zespolonej)*, więc obiekt wydaje się pozostawać w jednym kawałku. Musisz rozbić złożenie, aby uzyskać poszczególne elementy. Jeśli chcesz uzyskać dostęp do poszczególnych części w sposób parametryczny, możesz użyć do tego celu <img alt="" src=images/Part_CompoundFilter.svg  style="width:24px;"> [Filtr złożeń](Part_CompoundFilter/pl.md). Dla szybkiego dostępu nieparametrycznego użyj narzędzia <img alt="" src=images/Draft_Downgrade.svg  style="width:24px;"> [Rozbij kształt](Draft_Downgrade/pl.md).

Narzędzie ma trzy tryby pracy: \"Standardowy\", \"Podziel\" i \"BryłaZłożona\". Nie ma żadnego formularza wyboru, są one predefiniowane, ale można uzyskać do nich dostęp po wykonaniu operacji na poziomie wynikowych segmentów.

**Standard** i **Podziel** różnią się działaniem narzędzia na linach, powłokach i bryłach. W przypadku opcji \"Podziel\" są one rozdzielane. W przypadku opcji \"Standard\" są one utrzymywane razem *(otrzymują dodatkowe segmenty)*.

Struktura łączenia w trybach \"Standard\" i \"Podziel\" jest zgodna ze strukturą łączenia krojonego kształtu.

W trybie \"BryłaZłożona\" bryły są łączone w bryłę złożoną *(lub złożenie brył złożonych, jeśli powstałe bryły tworzą więcej niż jedną wyspę połączeń)*. Złożone bryły to zestaw brył połączonych ścianami. Są one powiązane z bryłami tak, jak linie są powiązane z krawędziami, a powłoki są powiązane ze ścianami. Nazwa pochodzi więc od wyrażenia \"bryła złożona\".

Ogólne działanie narzędzia jest bardzo podobne do <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [Fragmentacja funkcją logiczną](Part_BooleanFragments/pl.md), z wyjątkiem tego, że tylko fragmenty z pierwszego kształtu znajdują się w wyniku.



## Użycie

1.  Wybierz najpierw obiekt, który ma zostać pocięty, a następnie kilka obiektów, którymi ma zostać pocięty.
    Kolejność wyboru jest ważna. Złożenia z samoprzecięciami nie są dozwolone *(samoprzecięcia czasami mogą być uwzględnione poprzez przepuszczenie złożenia przez <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [Part Boolean Fragments](Part_BooleanFragments/pl.md))*.
2.  Wywołaj polecenie *Rozbij na kształty złożenia* na kilka sposobów:
    -   Naciśnij przycisk <img alt="" src=images/Part_Slice.svg  style="width:24px;"> **Rozbij na kształty złożenia** na pasku narzędzi.
    -   Użyj polecenia **Część → Rozdziel → Rozbij na kształty złożenia ** w menu części.




1.  Uwagaː Obiekty do cięcia muszą całkowicie oddzielać obiekt do przecięcia. W ten sposób prostopadłościan nie może zostać przecięty przez polilinię, ale na przykład przez płaszczyznę pochodzącą z wyciągniętej polilinii.

Tworzony jest obiekt parametryczny Rozbicia. Oryginalne obiekty są ukrywane, a wynik połączenia jest wyświetlany w oknie [widoku 3D](3D_view/pl.md).

## Struktura drzewa cechy Rozbij 

Polecenie *Rozbij na kształty złożenia* tworzy coś więcej niż tylko wycięty obiekt. W poniższym przykładzie prostopadłościan jest przecinany przez ścianę.

Tworzony jest wycinek, a każdy jego element jest łączony w Złożenie.

![](images/Part_SliceTree.png )



## Właściwości


{{TitleProperty|Rozkrój}}

-    **Baza**: Obiekt do pokrojenia.

-    **Narzędzia**: Lista obiektów do cięcia. *(od wersji FreeCAD v0.17.8053 właściwość ta nie jest wyświetlana w edytorze właściwości i można uzyskać do niej dostęp tylko za pośrednictwem środowiska Python)*.

-    **Tryb**: \"Standardowy\", \"Podziel\" i \"BryłaZłożona\". \"Podziel\" jest wartością domyślną. Standard i Podziel różnią się działaniem narzędzia na kształtach typu zbiorczego: jeśli zostanie wybrana opcja podziel, kształty te zostaną rozdzielone. W przeciwnym razie będą one trzymane razem *(otrzymają dodatkowe segmenty)*.

-    **Tolerancja**: wartość **Rozmyj**. Jest to dodatkowa tolerancja stosowana podczas wyszukiwania przecięć, oprócz tolerancji przechowywanych w kształtach wejściowych.

̈Uwagaː Właściwości są dostępne na etapie wewnętrznego obiektu wycinka, a nie na poziomie wyniku.



## Przykład



### Tworzenie układanki 

1.  Przełącz się na środowisko pracy <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Szkicownik](Sketcher_Workbench/pl.md)
    -   Utwórz nowy szkic.
    -   Narysuj prostokąt, który wyznaczy ogólny kształt układanki.
    -   Zamknij szkic.
        ![320px](images/slice_example_step1.png)
2.  Przełącz się do środowiska pracy <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md).
    -   Zaznacz szkic i wybierz z menu opcję **Część → <img src="images/Part_MakeFace.svg" width=24px> [Utwórz ścianę z polilinii](Part_MakeFace/pl.md)**.
        ![320px](images/slice_example_step2.png)
3.  Przełącz się z powrotem do <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Szkicownika](Sketcher_Workbench/pl.md)
    -   Utwórz kolejny szkic na tej samej płaszczyźnie.
    -   Używając narzędzia polilinia, narysuj linie, które podzielą układankę na części.
        ![320px](images/slice_example_step3.png).
4.  Przełącz się z powrotem do środowiska pracy <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md).
    -   Zaznacz szkic przedstawiający podział i zastosuj narzędzie <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [Fragmentacja funkcją logiczną](Part_BooleanFragments/pl.md). Spowoduje to wstawienie wierzchołków tam, gdzie przecinają się linie szkicu rozdzielającego. Ich obecność jest niezbędna, aby wykonać następny krok.
        ![320px](images/slice_example_step4.png)
5.  Zaznacz prostokątną ścianę i fragmenty Fragmentów logicznych szkicu rozdzielającego i zastosuj narzędzie <img alt="" src=images/Part_Slice.svg  style="width:24px;"> Rozbij na kształty złożenia.
    ![320px](images/slice_example_step5.png)
6.  Użyj narzędzia <img alt="" src=images/Part_ExplodeCompound.svg  style="width:24px;"> [Rozbij kształt złożony](Part_ExplodeCompound/pl.md) na ścianie pokrojonej w wycinki, aby ponownie rozbić złożenie utworzone przez Part Slice na pojedyncze kawałki.

**Uwaga:** Kroki 5 i 6 można wykonać jednym kliknięciem przy użyciu narzędzia <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Rozkrój](Part_SliceApart/pl.md).



## Uwagi

-   Narzędzie zostało wprowadzone w wersji FreeCAD v0.17.8053. FreeCAD musi być skompilowany z OCC **6.9.0** lub nowszym. W przeciwnym razie narzędzie jest niedostępne.
-   Właściwości są dostępne na wewnętrznym obiekcie wycinka, a nie na poziomie wyniku.
-   Obiekty do cięcia muszą całkowicie oddzielać obiekt do cięcia. Prostopadłościan nie może więc zostać pokrojony przez polilinię, ale na przykład przez płaszczyznę pochodzącą z wyciągniętej polilinii.
-   Obiekt krojony musi przejść kontrolę *BOP*. Zobacz stronę <img alt="" src=images/Part_CheckGeometry.svg  style="width:24px;"> [Sprawdź geometrię](Part_CheckGeometry/pl.md).



## Tworzenie skryptów 

Narzędzie **Odsunięcie 2D** może być używane w [makrodefinicjach](macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji: 
```pythonBOPTools.SplitFeatures.makeSlice(name)```

-   Tworzy pusty cechę Rozbij. Właściwości \"Baza\" i \"Narzędzia\" muszą zostać przypisane jawnie.
-   Zwraca nowo utworzony obiekt.

Obiekt Rozbij może być również stosowany do zwykłych kształtów, bez konieczności posiadania obiektu dokumentu: 
```pythonBOPTools.SplitAPI.slice(base_shape, tool_shapes, mode, tolerance = 0.0)``` Może to być przydatne do tworzenia niestandardowych funkcji skryptowych Python.

Przykład: {{code|code=
import BOPTools.SplitFeatures
j = BOPTools.SplitFeatures.makeSlice(name= 'Slice')
j.Base = FreeCADGui.Selection.getSelection()[0]
j.Tools = FreeCADGui.Selection.getSelection()[1:]
}}

Samo narzędzie jest zaimplementowane w środowisku Python, patrz **/Mod/Part/BOPTools/SplitFeatures.py** *([GitHub link](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/BOPTools/SplitFeatures.py))* w miejscu, w którym zainstalowany jest FreeCAD.



## Poradniki

-   [: FreeCad 0.18 środowisko pracy Część z użyciem narzędzi Rozbij na kształty złożenia i Rozbij](https://www.youtube.com/watch?v=tzHkQaHgrfQ) *(język angielski)*, autor: Ha Gei

-   [: FreeCAD, funkcje Rozbij na kształty złożenia oraz Rozbij, oraz inne sztuczki](https://www.youtube.com/watch?v=JJAL5JmqqKQ) *(język niemiecki)*, autor: Ha Gei



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Slice/pl
