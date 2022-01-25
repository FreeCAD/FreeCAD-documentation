---
- GuiCommand:/pl
   Name:Sketcher ToggleConstruction
   Name/pl:Szkicownik: Przełącz geometrię konstrukcji
   MenuLocation:Sketch → Elementy geometryczne szkicownika → Przełącz geometrię konstrukcji
   Workbenches:[Szkicownik](Sketcher_Workbench/pl.md)
   SeeAlso:[Przełącz wiązanie kontrolujące](Sketcher_ToggleDrivingConstraint/pl.md)
---

# Sketcher ToggleConstruction/pl

## Opis

To narzędzie przełącza geometrię do / z trybu konstrukcyjnego. Może być użyte na dowolnym typie geometrii: linii, łuku czy okręgu.

Geometria konstrukcyjna jest ważnym narzędziem szkicownika. Gdy szkic jest używany do operacji 3D, geometria konstrukcyjna jest ignorowana.

Podczas **[<img src=images/Sketcher_EditSketch.svg style="width:16px"> [Edycji szkicu](Sketcher_EditSketch.md)**, geometria konstrukcyjna jest ukazana jako niebieska i nie zmieni koloru na zielony nawet gdy szkic zostanie w pełni związany. Kiedy **[<img src=images/Sketcher_LeaveSketch.svg style="width:16px"> [Opuścisz szkic](Sketcher_LeaveSketch.md)**, geometria konstrukcyjna zostanie ukryta w [widoku 3D](3D_view/pl.md).

Linie konstrukcyjne mogą zostać użyte jako oś obrotu przez funkcję **[<img src=images/PartDesign_Revolution.svg style="width:16px"> [Projekt Części: Wyciągnij przez obrót](PartDesign_Revolution/pl.md)**.

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:480px;">

## Użycie

Istnieją dwa sposoby użycia tego narzędzia:

1.  Nie mając niczego zaznaczonego w oknie [widoku 3D](3D_view/pl.md):
    -   Wywołaj tryb konstrukcji, klikając na przycisk **[<img src=images/Sketcher_ToggleConstruction.svg style="width:24px"> [Przełącz geometrię konstrukcyjną](Sketcher_ToggleConstruction/pl.md)** lub używając opcji **Szkic → Elementy geometryczne szkicownika → [<img src=images/Sketcher_ToggleConstruction.svg style="width:24px"> Przełącz geometrię konstrukcyjną** w menu Szkicownika.
    -   Spowoduje to zmianę koloru tworzenia nowych elementów geometrycznych na niebieski.
    -   Nowo utworzone elementy geometryczne będą teraz tworzone w trybie konstrukcyjnym.
2.  Z jednym lub kilkoma elementami geometrycznymi zaznaczonymi w oknie [widoku 3D](3D_view/pl.md)
    -   Wywołaj narzędzie Sketcher ToggleConstruction klikając na przycisk **[<img src=images/Sketcher_ToggleConstruction.svg style="width:16px"> [Przełącz geometrię konstrukcyjną](Sketcher_ToggleConstruction/pl.md)** lub wybierając je z menu.
    -   Zaznaczone elementy zostaną teraz przełączone w tryb konstrukcji.
    -   Następnie nowo utworzone elementy będą znowu normalną geometrią.

## Przykład

Użyj trybu Konstrukcyjnego na kilku elementach szkicu,

<img alt="" src=images/Sketcher_ConstructionMode_fr_01.png  style="width:450px;">

i kiedy **[<img src=images/Sketcher_LeaveSketch.svg style="width:16px"> [opuścisz tryb edycji szkicu](Sketcher_LeaveSketch/pl.md)**, geometria, która była zamieniona w konstrukcyjną stanie się niewidoczna w oknie [widoku 3D](3D_view/pl.md) *(ale wciąż będzie obecna w trybie edycji szkicu)*.

<img alt="" src=images/Sketcher_ConstructionMode_fr_02.png  style="width:450px;">

## Uwagi

-   Narzędzie **[<img src=images/Sketcher_CreatePoint.svg style="width:16px"> [Utwórz punkt](Sketcher_CreatePoint/pl.md)** zawsze będzie tworzyć punkty w trybie konstrukcji niezależnie od stanu przełącznika na pasku narzędzi, wybierz żądane punkty w oknie [widoku 3D](3D_view/pl.md) po utworzeniu i kliknij w przycisk **[<img src=images/Sketcher_ToggleConstruction.svg style="width:24px"> [Przełącz tryb konstrukcji](Sketcher_ToggleConstruction.md)**, aby przekształcić je w normalną geometrię. {{Version/pl|0.19}}





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleConstruction/pl
