---
 GuiCommand:
   Name: Sketcher CreatePointFillet
   Name/pl: Utwórz zaokrąglenie z zachowaniem narożników
   MenuLocation: Szkic , Elementy geometryczne szkicownika , Utwórz zaokrąglenie z zachowaniem narożników
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **F** **P**
   Version: 0.19
   SeeAlso: Sketcher_CreateFillet
---

# Sketcher CreatePointFillet/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:24px;"> **Utwórz zaokrąglenie z zachowaniem wiązań** tworzy zaokrąglenie między dwiema nierównoległymi krawędziami. Jeśli zaokrąglane są dwie proste krawędzie połączone [wiązaniem zbieżności](Sketcher_ConstrainCoincident/pl.md) zostaną zaokrąglone, powiązany punkt wspólny zostanie zachowany poprzez dodanie [obiektu punktu](Sketcher_CreatePoint/pl.md), który ma wiązanie [punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md) z obiema krawędziami. Wiązania połączone ze wspólnym punktem są przenoszone do nowego obiektu punktu. Poza tym narzędzie to jest identyczne z narzędziem [Utwórz zaokrąglenie](Sketcher_CreateFillet/pl.md). Więcej informacji można znaleźć tutaj.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

1.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_CreatePointFillet.svg" width=16px> '''Utwórz zaokrąglenie z zachowaniem wiązań'''**.
    -   Wybierz z menu **Szkic → Elementy geometryczne szkicownika → <img src="images/Sketcher_CreatePointFillet.svg" width=16px> Utwórz zaokrąglenie z zachowaniem narożnika**.
    -   Kliknij prawym przyciskiem myszy na [widoku 3D](3D_view/pl.md) i wybierz **<img src="images/Sketcher_CreatePointFillet.svg" width=16px> Utwórz zaokrąglenie z zachowaniem wiązań** z menu podręcznego.
    -   Użyj skrótu klawiaturowego: **G**, następnie **F**, a potem **P**.
2.  Dalsze kroki można znaleźć na stronie [Utwórz zaokrąglenie](Sketcher_CreateFillet#Użycie.md).



## Uwagi

Zapoznaj się z informacjami na stronie [Utwórz zaokrąglenie](Sketcher_CreateFillet/pl#Uwagi.md).





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePointFillet/pl
