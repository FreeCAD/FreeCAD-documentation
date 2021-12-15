---
- GuiCommand:/pl
   Name:Sketcher CreatePoint
   Name/pl:Szkicownik: Utwórz punkt
   MenuLocation:Szkic → Elementy geometryczne szkicownika → Utwórz punkt
   Workbenches:[Szkicownik](Sketcher_Workbench/pl.md)
---

# Sketcher CreatePoint/pl

## Opis

Narzędzie Punkt tworzy punkt w bieżącym szkicu, który może być użyty do konstruowania elementów geometrii.

_

## Użycie

-   Kliknij na przycisk **<img src="images/Sketcher_CreatePoint.svg" width=24px> Utwórz punkt**, aby aktywować funkcję.
-   Kliknięcie w szkicu tworzy punkt.
-   Naciśnięcie klawisza **Esc** lub kliknięcie prawym przyciskiem myszy anuluje funkcję.

## Opcje

-   Domyślnie punkty są tworzone jako geometria konstrukcyjna i dlatego nie są widoczne poza trybem edycji szkicu. Użyj narzędzia <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:24px;"> [Przełącz tryb konstrukcji](Sketcher_ToggleConstruction/pl.md), aby przekształcić je w normalną geometrię. {{Version/pl|0.19}}

Tryb przyciągania do siatki może być ustawiony w [Preferencje szkicownika](Sketcher_Preferences/pl.md). Następnie punkt jest przyciągany do siatki, jeśli jego odległość od linii siatki jest mniejsza niż 25%. Tryb przyciągania nie ustala punktu na siatce. Nadal ma on dwa stopnie swobody i można go przesuwać za pomocą myszy lub związać do innych miejsc.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePoint/pl
