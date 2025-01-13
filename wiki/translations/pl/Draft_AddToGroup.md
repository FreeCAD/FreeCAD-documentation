---
 GuiCommand:
   Name: Draft AddToGroup
   Name/pl: Rysunek Roboczy: Dodaj do grupy
   MenuLocation: Narzędzia , Dodaj do grupy ...
   Workbenches: Draft_Workbench/pl
   SeeAlso: Std_Group/pl, Draft_AddNamedGroup/pl, Draft_AddConstruction/pl, Draft_AutoGroup/pl
---

# Draft AddToGroup/pl



## Opis

Polecenie <img alt="" src=images/Draft_AddToGroup.svg  style="width:24px;"> **Dodaj do grupy** przenosi obiekty do [Grupy](Std_Group/pl.md) lub obiektu podobnego do grupy [BIM](BIM_Workbench/pl.md). Może ono również rozgrupować obiekty.



## Użycie

1.  Wybierz jeden lub więcej obiektów.
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_AddToGroup.svg" width=16px> '''Przenieś do grupy'''**.
    -   Wybierz opcję **Narzędzia → <img src="images/Draft_AddToGroup.svg" width=16px> Przenieś do grupy ...** z menu lub menu kontekstowego [widoku drzewa](Tree_view/pl.md) bądź [widoku 3D](3D_view/pl.md).
3.  W pobliżu kursora wyświetlane jest menu. Wykonaj jedną z następujących czynności:
    -   Wybierz **Rozgrupuj**, aby przenieść obiekty poza grupę (grupy), w której się znajdują.
    -   Wybierz grupę, do której chcesz przenieść obiekty.
    -   Wybierz **+ Dodaj nową grupę**, aby przenieść obiekty do nowej grupy:
        1.  Otworzy się panel zadań **Dodaj grupę**.
        2.  Wprowadź **Nazwa grupy**.
        3.  Naciśnij przycisk **OK**.



## Uwagi

-   Obiekty mogą być również przenoszone do grupy poprzez przeciągnięcie i upuszczenie ich na grupę w oknie [Widoku drzewa](Tree_view/pl.md).
-   Polecenie to może być użyte do przeniesienia obiektów do [Przełącz tryb konstrukcyjny](Draft_ToggleConstructionMode/pl.md), ale w przeciwieństwie do polecenia [Dodaj do grupy konstrukcyjnej](Draft_AddConstruction/pl.md), nie stosuje ono [koloru geometrii konstrukcyjnej](Draft_ToggleConstructionMode/pl#Ustawienia.md).
-   Więcej informacji na temat organizacji modelu można znaleźć na stronie [Struktura dokumentu](Document_structure/pl.md) oraz [Poradnik dla środowiska pracy Architektura](Arch_tutorial/pl#Porządkowanie_modelu.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft AddToGroup/pl
