---
- GuiCommand:
   Name: Part SliceApart
   Name/pl: Część: Rozetnij
   MenuLocation: Część - Rozdziel - Rozetnij
   Workbenches: [Część](Part_Workbench/pl.md)
   Version: 0.18
   SeeAlso: [Krojenie](Part_Slice/pl.md), [Rozbij kształt złożony](Part_ExplodeCompound/pl.md)
---

# Part SliceApart/pl



## Opis

Jest to narzędzie do dzielenia kształtów przez przecięcie innym kształtem. Na przykład dla prostopadłościanu i płaszczyzny tworzone są dwie bryły.
![600px](images/Part_Slice_Demo.png)



* Powyżej: elementy zostały później ręcznie rozsunięte, aby uwidocznić cięcie.*

Narzędzie **Rozetnij** jest tym samym, co <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Rozbij na kształty złożenia](Part_Slice/pl.md), po którym następuje działanie funkcji jak w narzędziu <img alt="" src=images/Part_ExplodeCompound.svg  style="width:24px;"> [Rozbij na kształty złożenia](Part_ExplodeCompound/pl.md). Podczas gdy \"Rozbij na kształty złożenia\" jest w pełni parametryczne i nie powoduje żadnych problemów, gdy zmienia się liczba elementów, \"Rozetnij\" nie aktualizuje liczby obiektów, gdy zostanie zmieniona liczba elementów w operacji. Oba tworzą parametryczną cechę *Rozbicia*, która umieszcza pocięte kawałki w złożeniu, ale funkcja \"Rozbij\" rozbija wynikowe złożenie na osobne obiekty.

Kształt wyjściowy zajmuje tę samą przestrzeń co oryginał. Jest on jednak dzielony w miejscach przecięcia z innymi kształtami. Podzielone elementy są odrębnymi elementami.

Więcej informacji można znaleźć na stronie [Rozbij na kształty złożenia](Part_Slice/pl.md).

## Struktura drzewa cechy Rozetnij 

Polecenie Rozbij tworzy coś więcej niż tylko wycięty obiekt. W poniższym przykładzie prostopadłościan jest przecinany przez ścianę.

Zostaje utworzony fragment, a dla każdej jego części tworzony jest [Filtr złożenia](Part_CompoundFilter/pl.md), dzięki czemu ten sam fragment występuje wielokrotnie pod każdym Filtrem złożenia. Wszystkie te Filtry złożeń są połączone w jeden obiekt Złożenia.

![](images/Part_SliceApartTree.png )



## Przykład

-   Tworzenie puzzli: patrz przykład zastosowania funkcji [Rozbij na kształty złożenia](Part_Slice/pl.md), kroki od 1 do 6.



## Tworzenie skryptów 

Narzędzie Rozetnij może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:

`BOPTools.SplitFeatures.makeSlice(name)`

Ustaw tryb na *podziel*, aby uzyskać podział na części.

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



## Uwagi

Narzędzie zostało wprowadzone w wersji FreeCAD v0.18.15506. FreeCAD musi być skompilowany z OCC **6.9.0** lub nowszym. W przeciwnym razie narzędzie jest niedostępne.



## Poradniki Wideo 

-   <https://www.youtube.com/watch?v=tzHkQaHgrfQ> : FreeCad 0.18 środowisko pracy Część z użyciem narzędzi Rozbij na kształty złożenia i Rozetnij *(język angielski)*, autor: Ha Gei

-   <https://www.youtube.com/watch?v=JJAL5JmqqKQ> : FreeCAD, funkcje Rozbij na kształty złożenia oraz Rozetnij, oraz inne sztuczki *(język niemiecki)*, autor: Ha Gei



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part SliceApart/pl
