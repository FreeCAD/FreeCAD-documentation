---
 GuiCommand:
   Name: Sketcher CreatePoint
   Name/pl: Szkicownik: Utwórz punkt
   MenuLocation: Szkic , Elementy geometryczne szkicownika , Utwórz punkt
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **Y**
---

# Sketcher CreatePoint/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:24px;"> **Punkt** tworzy punkt w bieżącym szkicu.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

Pos-OVP = Pozycyjne [Parametry wyświetlane w widoku](Sketcher_Preferences/pl#Ogólne.md). {{Version/pl|1.0}}

1.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_CreatePoint.svg" width=16px> '''Utwórz punkt'''**.
    -   Wybierz z menu opcję **Szkic → Elementy geometryczne szkicownika → <img src="images/Sketcher_CreatePoint.svg" width=16px> Utwórz punkt**.
    -   Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **<img src="images/Sketcher_CreatePoint.svg" width=16px> Utwórz punkt** z menu kontekstowego.
    -   Użyj skrótu klawiaturowego: **G**, a następnie **Y**.
2.  Kursor zmieni się krzyżyk z ikoną narzędzia.
3.  Wybierz punkt. Lub za pomocą Pos-OVP: wprowadź jego współrzędne X i / lub Y.
4.  Punkt zostanie utworzony i dodane zostaną odpowiednie wiązania oparte na Pos-OVP.
5.  Jeśli narzędzie działa w [trybie kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md):
    1.  Opcjonalnie kontynuuj tworzenie punktów.
    2.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



## Uwagi

-    {{VersionMinus/pl|0.21}}: Punkty są zawsze tworzone jako geometria konstrukcyjna. Opcjonalnie zmień je na normalną geometrię za pomocą narzędzia [Przełącz tryb konstrukcji](Sketcher_ToggleConstruction/pl.md), aby były widoczne poza trybem edycji szkicu.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePoint/pl
