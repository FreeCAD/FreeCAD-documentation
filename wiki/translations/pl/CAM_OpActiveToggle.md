---
 GuiCommand:
   Name: CAM OpActiveToggle
   Name/pl: CAM: Przecz aktywne stadium operacji
   MenuLocation: CAM , Przełącz aktywne stadium operacji
   Workbenches: CAM_Workbench/pl
   Shortcut: **P** **X **
---

# CAM OpActiveToggle/pl



## Opis

Narzędzie <img alt="" src=images/CAM_OpActiveToggle.svg  style="width:24px;"> [Przełącz aktywne stadium operacji](CAM_OpActiveToggle/pl.md) w <img alt="" src=images/Workbench_CAM.svg  style="width:24px;"> [środowisku pracy CAM](CAM_Workbench/pl.md) jest używane do przełączania aktywnego stanu istniejącej operacji ścieżki.

To narzędzie może być używane tylko wtedy, gdy <img alt="" src=images/CAM_Job.svg  style="width:24px;"> [zadanie](CAM_Job/pl.md) ma co najmniej jedną operację ścieżki.



## Użycie

1.  Zaznacz operację w grupie **Operations** należącej do zadania obróbki. Dezaktywowaną operację można rozpoznać po jej wyszarzonej etykiecie i ikonie.
2.  Istnieje kilka sposobów wywołania tej komendy:
    -   Wciśnij przycisk **<img src="images/CAM_OpActiveToggle.svg" width=16px> [Przełącz aktywne stadium operacji](CAM_OpActiveToggle/pl.md)**.
    -   Wybierz opcję **CAM → <img src="images/CAM_OpActiveToggle.svg" width=16px> Przełącz aktywne stadium operacji** z menu.
    -   Użyj skrótu klawiszowego: **P** a następnie **X**.
3.  Rezultat zależy od wybranej operacji:
    -   Jeśli wybrałeś aktywną operację, to polecenie ją dezaktywuje:
        -   Ikona operacji jest zastępowana ikoną tego narzędzia: <img alt="" src=images/CAM_OpActiveToggle.svg  style="width:16px;">.
        -   Ikona i etykieta operacji zostają wyszarzone.
        -   Ścieżki generowane z operacji znikają z [widoku 3D](3D_view/pl.md).
        -   Podczas używania komendy <img alt="" src=images/CAM_Inspect.svg  style="width:16px;"> [Sprawdź ścieżkę narzędzia](CAM_Inspect/pl.md) lub <img alt="" src=images/CAM_Post.svg  style="width:16px;"> [Przetwarzanie końcowe](Path_Post/pl.md), G-code operacji nie jest zapewniany.
    -   Jeśli wybrałeś dezaktywowaną operację, to polecenie ją aktywuje:
        -   Ikona operacji jest zastępowaną tą należącą do operacji.
        -   Ikona i etykieta operacji nie są już wyszarzone.
        -   Ścieżki wygenerowane przez operację są przeliczane i wyświetlane w [widoku 3D](3D_view/pl.md).
        -   Podczas używania komendy <img alt="" src=images/CAM_Inspect.svg  style="width:16px;"> [Sprawdź ścieżkę narzędzia](CAM_Inspect/pl.md) lub <img alt="" src=images/CAM_Post.svg  style="width:16px;"> [Przetwarzanie końcowe](CAM_Post/pl.md), G-code operacji jest zapewniany.



## Opcje

Pusto



## Właściwości

Pusto



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Przykład:


```python
#Umieść tu kod przykładu.
```





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM OpActiveToggle/pl
