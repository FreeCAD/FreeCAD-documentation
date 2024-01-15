---
 GuiCommand:
   Name: Draft AddConstruction
   Name/pl: Rysunek Roboczy: Dodaj do grupy konstrukcyjnej
   MenuLocation: Narzędzia , Dodaj do grupy konstrukcyjnej
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Version: 0.17
   SeeAlso: Draft_ToggleConstructionMode/pl, Draft_AddToGroup/pl
---

# Draft AddConstruction/pl



## Opis

Polecenie <img alt="" src=images/Draft_AddConstruction.svg  style="width:24px;"> **Dodaj do grupy konstrukcyjnej** przenosi obiekty do [grupy konstrukcyjnej](Draft_ToggleConstructionMode/pl.md). Stosuje również [kolor geometrii konstrukcji](Draft_ToggleConstructionMode/pl#Ustawienia.md) względem obiektów.



## Użycie

1.  Wybierz jeden lub więcej obiektów.
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_AddConstruction.svg" width=16px> '''Dodaj do grupy konstrukcyjnej'''**.
    -   Wybierz opcję z menu **Narzędzia → <img src="images/Draft_AddConstruction.svg" width=16px> Dodaj do grupy konstrukcyjnej**.
3.  Jeśli nie istnieje, najpierw tworzona jest grupa konstrukcyjna.
4.  Obiekty są przenoszone do grupy konstrukcyjnej i zmieniane są ich właściwości kolorystyczne.



## Uwagi

-   Obiekty mogą być również przenoszone do grupy konstrukcyjnej poprzez przeciągnięcie i upuszczenie ich na grupę w oknie [Widoku drzewa](Tree_view/pl.md) lub poprzez użycie polecenia [Dodaj do grupy](Draft_AddToGroup/pl.md). Ale w obu przypadkach [kolor geometrii konstrukcji](Draft_ToggleConstructionMode/pl#Ustawienia.md) nie jest stosowany.
-   Więcej informacji na temat organizacji modelu można znaleźć na stronach [Struktura dokumentu](Document_structure/pl.md) i [Poradnik dla środowiska pracy Architektura](Arch_tutorial/pl#Porządkowanie_modelu.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft AddConstruction/pl
