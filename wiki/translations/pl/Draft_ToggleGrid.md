---
 GuiCommand:
   Name: Draft ToggleGrid
   Name/pl: Rysunek Roboczy: Przełącz widoczność siatki
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Shortcut: **G** **R**
   SeeAlso: Draft_Snap_Grid/pl, Draft_SelectPlane/pl
---

# Draft ToggleGrid/pl



## Opis

Polecenie <img alt="" src=images/Draft_ToggleGrid.svg  style="width:24px;"> **Przełącz widoczność siatki** włącza lub wyłącza widoczność siatki.


{{Version/pl|0.22}}

: Każdy [widok 3D](3D_view/pl.md) ma swoją własną siatkę, która może być zawsze widoczna, widoczna tylko podczas komend lub niewidoczna. Początkowa widoczność siatki w nowych widokach zależy od [usyawień](#Ustawienia.md).



## Użycie

1.  Polecenie może być używane, gdy aktywne jest inne polecenie.
2.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_ToggleGrid.svg" width=16px> '''Przełącz widoczność siatki'''** na pasku narzędzi Draft snap.
    -   Naciśnij przycisk **<img src="images/Draft_ToggleGrid.svg" width=16px> Przełącz widoczność siatki** w [Widżecie przyciągania](Draft_snap_widget/pl.md).
    -   Użyj skrótu klawiaturowego: **G**, a następnie **R**. Tego skrótu nie można użyć, jeśli aktywne jest inne polecenie.
3.  Widoczność siatki należącej do bieżącego okna widoku 3D uległa zmianie:
    -   Jeśli żadne inne polecenie nie jest aktywne:
        -   Jeśli siatka była niewidoczna, teraz jest zawsze widoczna.
        -   Jeśli siatka była widoczna, teraz nie jest już zawsze widoczna, ale widoczność siatki podczas poleceń pozostaje niezmieniona.
    -   Jeśli aktywne jest inne polecenie:
        -   Jeśli siatka była niewidoczna, teraz jest widoczna tylko podczas wykonywania poleceń.
        -   Jeśli siatka była widoczna, teraz nie jest już widoczna podczas poleceń i nie jest już zawsze widoczna.



## Ustawienia

Zobacz także strony: [Edytor ustawień](Preferences_Editor/pl.md) oraz [Rysunek Roboczy: Ustawienia](Draft_Preferences/pl.md).

-   \* Dostępne są różne ustawienia siatki: **Edycja → Preferencje → Rysunek Roboczy → Siatka i przyciąganie → Siatka**.
-   Aby utrzymać siatkę podczas przełączania na inne środowiska pracy, zobacz [Dostrajanie](Fine-tuning/pl#środowisko_pracy_Rysunek_Roboczy.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ToggleGrid/pl
