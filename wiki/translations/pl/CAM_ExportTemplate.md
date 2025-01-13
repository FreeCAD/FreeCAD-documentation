---
 GuiCommand:
   Name: CAM ExportTemplate
   Name/pl: CAM: Eksportuj szablon
   MenuLocation: CAM , Eksportuj szablon
   Workbenches: CAM_Workbench/pl
   SeeAlso: CAM_SetupSheet/pl
---

# CAM ExportTemplate/pl



## Opis

Narzędzie <img alt="" src=images/CAM_ExportTemplate.svg  style="width:24px;"> [Eksportuj szablon](CAM_ExportTemplate/pl.md) zapewnia wygodny mechanizm do zapisania powszechnie używanych definicji zadań z poziomu istniejącego zadania. Ułatwia to przygotowanie konfiguracji przyszłych zadań, które są w dużej mierze podobne, pozwalając na import szablonów zadań, podczas tworzenia zadania.

Opcja **Edycja → Preferencje ... → CAM → Ustawienia dla zadania → Ustawienia domyślne → Szablon** ustawia domyślny szablon.



## Użycie

1.  Wybierz opcję **CAM → <img src="images/CAM_ExportTemplate.svg" width=16px> Eksportuj szablon** z menu.
2.  Zaznacz elementy do uwzględnienia z okna konfiguracyjnego polecenia **Eksportuj szablon**.
3.  Szablon musi być zapisany w katalogu makr lub katalogu środowiska CAM, zgodnie z ustawieniami w [Preferencjach środowiska CAM](CAM_Preferences/pl.md).
4.  Nazwa szablonu musi być zgodna ze wzorem **job_<nazwa szablonu>.json**. W polu zaznaczenia przedrostek **job_** i rozszerzenie są pomijane.
5.  Wciśnij przycisk **OK** i zapisz szablon.



## Opcje

## Post Processing 

-   Zaznaczenia postprocessora
-   Argumenty postprocessora
-   Nazwa pliku wyjściowego



## Półprodukt

-   Zakres: rozmiar półproduktu
-   Umiejscowienie: lokalizacja półproduktu



## Arkusz konfiguracji 

-   Wysokości operacji
-   Głębokości operacji
-   Prędkość posuwu szybkiego narzędzia



## Kontrolery narzędzi 

-   Wybrane kontrolery narzędzi





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM ExportTemplate/pl
