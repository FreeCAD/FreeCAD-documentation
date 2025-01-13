---
 GuiCommand:
   Name: CAM Custom
   Name/pl: CAM: Użytkownika
   MenuLocation: CAM , Polecenia dodatkowe , Użytkownika
   Workbenches: CAM_Workbench/pl
---

# CAM Custom/pl



## Opis

Narzędzie <img alt="" src=images/CAM_Custom.svg  style="width:24px;"> [Użytkownika](CAM_Custom/pl.md) wstawia obiekt ścieżki, który jest zbudowany z ręcznie utworzonego kodu G-code użytkownika.

Ponieważ polecenie Użytkownika nie zapewnia połączenia z kontrolerem narzędzi, jeśli narzędzie jest używane przez kod G-code użytkownika, jego indeks musi być zapisany razem z kodem M-code uruchomienia wrzeciona aby zostało przekazane do postprocesora. To zapewnia, że zmiany narzędzia i uruchomienie będą prawidłowo wygenerowane.

Przykładowo, aby przekazać do postprocesora, że narzędzie używane w operacji opartej na kodzie G-code użytkownika ma indeks narzędzia 6 i prędkość wrzeciona 10,000, wstaw następujący kod na początku kodu G-code operacji użytkownika:

(T6: 4mm Endmill)

M6 T6

M3 S10000

Zauważ, że prędkości posuwu będą poprawnie generowane przez postprocesor tylko jeśli prędkości posuwu kodu G-code użytkownika są zapisane w jednostkach na sekundę.



## Użycie

1.  Wciśnij przycisk **<img src="images/CAM_Custom.svg" width=16px> [Użytkownika](CAM_Custom/pl.md)
**
2.  Wprowadź własny kod G-code we właściwości **G Code** nowo utworzonego obiektu. Zobacz stronę [Skrypty środowiska CAM](CAM_scripting/pl.md) aby sprawdzić wspierane polecenia G-code.



## Właściwości

-    **G Code**: Polecenia G-code użytkownika, na których ma być zbudowana ścieżka.





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Custom/pl
