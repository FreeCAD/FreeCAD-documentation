---
 GuiCommand:
   Name: Part ExplodeCompound
   Name/pl: Część: Rozbij kształt złożony
   MenuLocation: Część , Złożenie , Rozbij kształt złożony
   Workbenches: Part_Workbench/pl
   Version: 0.18
   SeeAlso: Part_Compound/pl, Draft_Downgrade/pl
---

# Part ExplodeCompound/pl



## Opis

Narzędzie <img alt="" src=images/Part_ExplodeCompound.svg  style="width:24px;"> **Rozbij kształt złożony** dzieli zespół kształtów, tak aby każdy zawarty kształt (podrzzędny) był dostępny jako oddzielny obiekt w drzewie modelu. Kształty potomne są automatycznie umieszczane w [Grupie](Std_Group/pl.md), jeśli jest ich więcej niż jeden.

Jest to funkcja półparametryczna: kształty obiektów podrzędnych będą aktualizowane wraz ze zmianą zespołu źródłowego, ale jeśli liczba obiektów podrzędnych w zespole ulegnie zmianie, w rozbiciu będzie brakować niektórych kształtów lub nadmiarowe obiekty będą w stanie błędu.

Rozmieszczenie wyodrębnionych kształtów jest zgodne z rozmieszczeniem oryginałów oraz właściwością *Umiejscowienie* każdego elementu podrzędnego.

Narzędzie rozbija również kształty niezłożone na ich składniki niższego poziomu: Złożenia na bryły, bryły na powłoki, powłoki na ściany, ściany na polilinie, polilinie na krawędzie, krawędzie na wierzchołki.



## Użycie

1.  Wybierz jeden kształt złożony.
2.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/Part_ExplodeCompound.svg" width=16px> [Rozbij kształt złożony](Part_ExplodeCompound/pl.md)**.
    -   Wybierz opcję **Część → Złożenie → Rozbij kształt złożony** z menu.



## Zastosowanie

-   Poprawianie pozycji kształtów utworzonych przez <img alt="" src=images/Draft_OrthoArray.svg  style="width:16px;"> [Szyk ortogonalny](Draft_OrthoArray/pl.md).
-   Uzyskanie podzielonych kawałków z wyniku operacji <img alt="" src=images/Part_Slice.svg  style="width:16px;"> [Krojenia](Part_Slice/pl.md) i <img alt="" src=images/Part_Cut.svg  style="width:16px;"> [Wycięcia](Part_Cut/pl.md).
-   Uzyskiwanie indywidualnych konturów z wielokonturowych szkiców i ścian.
-   Uzyskiwanie samej bryły z bryły w złożeniu, do użytku w środowisku pracy <img alt="" src=images/Workbench_FEM.svg  style="width:16px;"> [MES](FEM_Workbench/pl.md).



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ExplodeCompound/pl
