---
- GuiCommand:/pl
   Name:Part Fuse
   Name/pl:Część: Scalenie
   MenuLocation:Część → Operacje logiczne → Suma
   Workbenches:[Część](Part_Workbench/pl.md)
   SeeAlso:[Wytnij](Part_Cut/pl.md), [Część wspólna](Part_Common/pl.md), [Operacje logiczne](Part_Boolean/pl.md)
---

# Part Fuse/pl

## Opis

Narzędzie **![](images/)_[Scalenie](Part_Fuse/pl.md)** łączy *(jednoczy)* wybrane obiekty środowiska Części w jeden. Ta operacja jest w pełni parametryczna i komponenty mogą być modyfikowane, a wynik ponownie obliczany.

**Uwaga:** To polecenie jest zautomatyzowaną formą <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [Operacji na bryłach](Part_Boolean/pl.md).

## Użycie

1.  Wybierz dwa lub więcej kształtów
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **![](images/) Utwórz sumę kilku kształtów** na pasku narzędzi **Narzędzia środowiska Część**
    -   Użyj pozycji z menu **Część → Funkcje logiczne → Suma**.

### Obsługiwane dane wejściowe 

Obiekty wejściowe muszą być kształtami [OpenCascade](OpenCASCADE/pl.md). Przykłady: obiekty wykonane z użyciem Środowisk pracy Part, Part Design, Sketcher. Nie mogą to być siatki *(chyba że zostały zamienione na kształty)* - dla siatek, w programie Mesh Design istnieją specyficzne narzędzia do przeprowadzania operacji logicznych.

-   Bryła + Bryła: wynikiem jest bryła, która zajmuje całą objętość zawartą w elementach wejściowych.

-   Powłoka + Powłoka, Powłoka + Ściana, Ściana + Ściana: wynikiem jest powłoka. Tam gdzie ściany się przecinają, są one dzielone. Powłoki mogą być typu non-manifold. Po scaleniu, ściany mogą być połączone przez zastosowanie [Udoskonalenia kształtu](Part_RefineShape/pl.md).

-   Polilinia + Polilinia, Krawędź + Polilinia, Krawędź + Krawędź: wynikiem jest polilinia. Krawędzie są dzielone tam, gdzie się przecinają.

Obsługiwane są związki; zakłada się jednak, że kształty upakowane w związku nie dotykają się ani nie przecinają. Jeśli tak jest w rzeczywistości, funkcja Scalanie prawdopodobnie zawiedzie lub da nieprawidłowy wynik.

## Opcje

Elementy mogą być dodawane i usuwane ze scalenia, poprzez przeciąganie ich myszą do lub z elementu scalenia w widoku drzewa. Aby przeciągnąć obiekty scalenia musisz je upuścić na węzeł dokumentu *(nazwa pliku)* swojego modelu. Ręczna ponowna kalkulacja *(naciśnij klawisz **F5** lub kliknij na przycisk <img alt="" src=images/Std_Refresh.svg  style="width:24px;"> [Przelicz aktywny dokument](Std_Refresh/pl.md))* jest konieczna, aby zobaczyć wyniki.

Po zakończeniu tej operacji może być konieczne wyczyszczenie kształtu za pomocą narzędzia <img alt="" src=images/Part_RefineShape.svg  style="width:24px;">. [Udoskonal kształt](Part_RefineShape/pl.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Fuse/pl
