---
 GuiCommand:
   Name: Part Fuse
   Name/pl: Część: Połączenie
   MenuLocation: Część , Operacje logiczne , Połączenie
   Workbenches: Part_Workbench/pl
   SeeAlso: Part_Cut/pl, Part_Common/pl, Part_Boolean/pl
---

# Part Fuse/pl



## Opis

Narzędzie **![](images/)_'''Połączenie'''**_łączy_*(jednoczy)*_wybrane_obiekty_środowiska_Części_w_jeden. Ta operacja jest w pełni parametryczna i komponenty mogą być modyfikowane, a wynik ponownie obliczany.

**Uwaga:** To polecenie jest zautomatyzowaną formą narzędzia <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Operacja logiczna](Part_Boolean/pl.md).



## Użycie

1.  Wybierz dwa lub więcej kształtów
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **![](images/) Połączenie** na pasku narzędzi **Operacje logiczne**
    -   Użyj pozycji z menu **Część → Operacje logiczne → Połączenie**.



### Obsługiwane dane wejściowe 

Obiekty wejściowe muszą być kształtami [OpenCascade](OpenCASCADE/pl.md). Przykłady: obiekty wykonane z użyciem Środowisk pracy Part, Part Design, Sketcher. Nie mogą to być siatki *(chyba że zostały zamienione na kształty)* - dla siatek, w programie Mesh Design istnieją specyficzne narzędzia do przeprowadzania operacji logicznych.

-   Bryła + Bryła: wynikiem jest bryła, która zajmuje całą objętość zawartą w elementach wejściowych.

-   Powłoka + Powłoka, Powłoka + Ściana, Ściana + Ściana: wynikiem jest powłoka. Tam gdzie ściany się przecinają, są one dzielone. Powłoki mogą być typu non-manifold. Po scaleniu, ściany mogą być połączone przez zastosowanie [Udoskonalenia kształtu](Part_RefineShape/pl.md).

-   Polilinia + Polilinia, Krawędź + Polilinia, Krawędź + Krawędź: wynikiem jest polilinia. Krawędzie są dzielone tam, gdzie się przecinają.

Obsługiwane są związki; zakłada się jednak, że kształty upakowane w związku nie dotykają się ani nie przecinają. Jeśli tak jest w rzeczywistości, funkcja Scalanie prawdopodobnie zawiedzie lub da nieprawidłowy wynik.



## Opcje

Elementy mogą być dodawane i usuwane ze scalenia, poprzez przeciąganie ich myszą do lub z elementu scalenia w widoku drzewa. Aby przeciągnąć obiekty scalenia musisz je upuścić na węzeł dokumentu *(nazwa pliku)* swojego modelu. Ręczna ponowna kalkulacja *(naciśnij klawisz **F5** lub kliknij na przycisk <img alt="" src=images/Std_Refresh.svg  style="width:24px;"> [Przelicz aktywny dokument](Std_Refresh/pl.md))* jest konieczna, aby zobaczyć wyniki.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Fuse/pl
