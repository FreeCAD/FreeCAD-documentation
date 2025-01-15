---
 GuiCommand:
   Name: Arch Panel
   Name/pl: Architektura: Panel
   MenuLocation: 3D / BIM , Narzędzia panelu , Panel
   Workbenches: BIM_Workbench/pl
   Shortcut: **P** **A**
   Version: 0.15
   SeeAlso: Arch_Panel_Cut/pl, Arch_Panel_Sheet/pl
---

# Arch Panel/pl



## Opis

Narzędzie **Panel** umożliwia tworzenie wszelkiego rodzaju elementów panelopodobnych, typowych dla konstrukcji panelowych, takich jak projekt [WikiHouse](https://www.wikihouse.cc/), ale także dla wszelkiego rodzaju obiektów opartych na płaskim profilu.

<img alt="" src=images/Arch_Panel_example.jpg  style="width:700px;">

*Powyższy obraz przedstawia serię obiektów panelowych, utworzonych po prostu z zaimportowanych konturów 2D z pliku DXF. Można je następnie obracać i łączyć w celu tworzenia struktur.*

Od wersji {{VersionPlus/pl|0.17}} narzędzie Panel może być również używany do tworzenia profili falistych lub trapezowych:

<img alt="" src=images/Arch_panel_wave.jpg  style="width:700px;">



## Użycie

1.  Wybierz kształt 2D *(rysunek roboczy obiektu, ścianę lub szkic)* - opcjonalnie.
2.  Naciśnij przycisk **<img src="images/Arch_Panel.svg" width=16px> '''Panel'''** lub naciśnij **P**, a następnie **A**.
3.  Dostosuj żądane właściwości.



### Ograniczenia

-   Obecnie nie ma automatycznego systemu do tworzenia arkuszy cięcia 2D z obiektów panelowych, ale taka funkcja jest w planach i zostanie dodana w przyszłości.



## Opcje

-   Panele mają wspólne właściwości i zachowania ze wszystkimi [komponentami](Arch_Component/pl.md) środowiska Architektura.
-   Grubość panelu można dostosować po jego utworzeniu.
-   Naciśnij **Esc** lub przycisk **Anuluj**, aby przerwać bieżące polecenie.
-   Dwukrotne kliknięcie panelu w widoku drzewa po jego utworzeniu umożliwia przejście do trybu edycji i uzyskanie dostępu do opcji dodawania i odejmowania.
-   Możliwe jest automatyczne tworzenie paneli składających się z więcej niż jednego arkusza materiału, poprzez ustawienie właściwości Arkusze.
-   Panele mogą wykorzystywać <img alt="" src=images/Arch_MultiMaterial.svg  style="width:24px;"> [materiał złożony](Arch_MultiMaterial/pl.md). Podczas korzystania z materiału złożonego, panel stanie się wielowarstwowy, używając grubości określonych przez materiał złożony. Każda warstwa o grubości równej zero będzie miała grubość zdefiniowaną automatycznie przez pozostałą przestrzeń zdefiniowaną przez wartość Grubość panelu, po odjęciu innych warstw.



## Właściwości

-    **Długość**: Długość panelu

-    **Szerokość**: Szerokość panelu

-    **Grubość**: Grubość panelu

-    **Obszar**: Obszar panelu (automatycznie)

-    **Arkusze**: Liczba arkuszy materiału, z którego wykonany jest panel

-    **Długość fali**: Długość fali dla paneli falistych

-    **Wysokość fali**: Wysokość fali dla paneli falistych

-    **Typ fali**: Typ fali dla paneli falistych, zakrzywiona, trapezowa lub kolczasta.

-    **Kierunek fali**: Kierunek fali dla paneli falistych.

-    **Fala denna**: Określa czy dolna fala panelu jest płaska czy nie.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Panel** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
Panel = makePanel(baseobj=None, length=0, width=0, thickness=0, placement=None, name="Panel")
```

-   Tworzy obiekt `Panel` z podanego `baseobj`, który jest profilem zamkniętym i podanego wyciągnięcia `thickness`.
    -   Jeśli nie podano `baseobj`, można podać wartości liczbowe dla `length`, `width` i `thickness`, aby utworzyć panel blokowy.
-   Jeśli podano `placement`, zostanie on użyty.

Przykład:


```python
import FreeCAD, Draft, Arch

Rect = Draft.makeRectangle(1000, 400)
Panel = Arch.makePanel(Rect, thickness=36)
```



## Poradniki

-   [Poradnik przenoszenia Wikihouse](Wikihouse_porting_tutorial/pl.md)



---
⏵ [documentation index](../README.md) > Arch Panel/pl
