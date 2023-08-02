---
- GuiCommand:
   Name: Draft ToggleConstructionMode
   Name/pl: Rysunek Roboczy: Przełącz tryb konstrukcyjny
   MenuLocation: Kreślenie -> Przybory -> Przełącz tryb konstrukcyjny
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   SeeAlso: Draft_AddConstruction/pl, Draft_AutoGroup/pl
---

# Draft ToggleConstructionMode/pl

## Opis

Polecenie <img alt="" src=images/Draft_ToggleConstructionMode.svg  style="width:24px;"> **Rysunek Roboczy: Przełącz tryb konstrukcyjny** włącza lub wyłącza tryb konstrukcyjny. Jeśli tryb konstrukcji jest włączony, nowe obiekty [Rysunku Roboczego](Draft_Workbench/pl.md), z wyjątkiem [Punktu](Draft_Point/pl.md), są umieszczane w dedykowanej grupie i otrzymują predefiniowany kolor. Ta funkcja jest przeznaczona dla, często tymczasowej, geometrii konstrukcyjnej używanej do tworzenia nowych [punktów przyciągania](Draft_Snap/pl.md) do tworzenia innych obiektów. Gdy geometria konstrukcyjna nie jest już potrzebna, grupa konstrukcyjna może być łatwo [ukryta](Std_HideSelection/pl.md) lub [usunięta](Std_Delete/pl.md).

<img alt="" src=images/Draft_construction_mode_example.jpg  style="width:400px;"> 
*Geometria konstrukcyjna, w kolorze niebieskim, używana do wyznaczania środka i promienia okręgu*

## Użycie

1.  Istnieje kilka sposobów na wywołanie tej komendy:
    -   Naciśnij przycisk **<img src="images/Draft_ToggleConstructionMode.svg" width=16px> [Przełącz tryb konstrukcyjny](Draft_ToggleConstructionMode/pl.md)** na [Tacce narzędziowej](Draft_Tray/pl.md). Ten przycisk jest aktywny, jeśli włączony jest tryb konstrukcji w wersji roboczej.
    -   Wybierz opcję z menu **Przybory → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Przełącz tryb konstrukcji**.
    -   Użyj skrótu klawiaturowego: **C** a następnie **M**.
2.  Przycisk w [Tacce narzędziowej](Draft_Tray/pl.md) zostanie zaktualizowany.

## Uwagi

-   Jeżeli włączony jest tryb konstrukcji Rysunku Roboczego, to aktywna [warstwa](Draft_Layer/pl.md) jest ignorowana.

## Ustawienia

-   Aby zmienić etykietę grupy konstrukcyjnej, użyj opcji: **Edycja → Preferencje → Rysunek Roboczy → Ustawienia ogólne → Geometria konstrukcyjna → Nazwa grupy konstrukcyjnej**.
-   Aby zmienić używany kolor, użyj opcji: **Edycja → Preferencje → Rysunek Roboczy → Ustawienia ogólne → Geometria konstrukcyjna → Kolor geometrii konstrukcji**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ToggleConstructionMode/pl
