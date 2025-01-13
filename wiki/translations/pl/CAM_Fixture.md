---
 GuiCommand:
   Name: CAM Fixture
   Name/pl: CAM: Mocowanie
   MenuLocation: CAM , Polecenia dodatkowe , Uchwyt
   Workbenches: CAM_Workbench/pl
---

# CAM Fixture/pl



## Opis

Narzędzie <img alt="" src=images/CAM_Fixture.svg  style="width:24px;"> [Uchwyt](CAM_Fixture/pl.md) ustawia mocowanie odsuniętego układu współrzędnych roboczych kontrolera CNC obrabiarki.

Docelowe współrzędne odsunięcia współrzędnych roboczych zwykle zawierają: mocowania G53 do G59. Kod G-code to po prostu mocowanie (G53, G54, etc\...). Mocowania odsuniętego układu współrzędnych przedstawiają:

-   G53 → Układ współrzędnych obrabiarki.
-   G54 → Układ współrzędnych brudnopisu.
-   G55 to G59.9 → Mocowania współrzędnych pozwalające na odsunięcia robocze, względne do przełączników naprowadzających zlokalizowanych na obrabiarce CNC jakie mają być użyte.

Mocowanie G59 jest używane do rozszerzenia dostępnych mocowań. Zaimplementowany stopień rozszerzalności zależy od obrabiarki CNC a to polecenie pozwala na G59.1 do G59.9.



## Użycie

1.  Wciśnij przycisk **<img src="images/CAM_Fixture.svg" width=16px> [Uchwyt](CAM_Fixture/pl.md)** lub użyj skrótu klawiszowego **P** a następnie **F**.
2.  Wybierz żądane mocowanie odsunięcia roboczego z listy rozwijanej.



## Właściwości

-    **Fixture**: Ustawia aktualny punkt mocowania

-    **Active**: Definiuje czy to polecenie jest aktywne czy nie podczas wstawiania do złożenia



## Uwagi



## Ograniczenia



## Tworzenie skryptów 





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Fixture/pl
