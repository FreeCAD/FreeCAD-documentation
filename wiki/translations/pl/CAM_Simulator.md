---
 GuiCommand:
   Name: CAM Simulator
   Name/pl: CAM: Symulator
   MenuLocation: CAM , Symulator CAM
   Workbenches: CAM_Workbench/pl
   Shortcut: **P** **M**
   SeeAlso: CAM_Inspect/pl
---

# CAM Simulator/pl



## Opis

Narzędzie **Symulator CAM** umożliwia symulację procesu obróbki poprzez przemieszczanie modeli 3D narzędzi po ścieżkach G-Code, odejmując materiał obrabiany tam gdzie narzędzie go przecina, zapewniając wizualizację zadania obróbki. Umożliwia to wykrywanie i eliminowanie błędów przed uruchomieniem zadania obróbki na maszynie.

![](images/Path-Simulation.gif )



## Użycie

1.  Jest kilka sposobów na uruchomienie tego polecenia:
    -   Wciśnij przycisk **<img src="images/CAM_Simulator.svg" width=16px> '''Symulator CAM'''**.
    -   Wybierz opcję z menu **CAM → <img src="images/CAM_Simulator.svg" width=16px> Symulator CAM**.
    -   Użyj skrótu klawiszowego: **P** a następnie **M**.
2.  Odznacz wszelkie **Operacje**, które nie mają być symulowane
3.  Dostosuj ustawienia **Prędkość** i **Dokładność**.
4.  Wybierz **Zadanie** do zasymulowania z listy rozwijanej.
5.  Użyj paska narzędzi **Symulator CAM** aby wywołać różne polecenia:
    -   Wciśnij przycisk <img alt="" src=images/CAM_BPlay.svg  style="width:24px;"> *(Aktywuj / wznów symulację)* aby uruchomić lub wznowić animację operacji.
    -   Wciśnij przycisk <img alt="" src=images/CAM_BFastForward.svg  style="width:24px;"> *(Uruchom całą symulację bez animacji)* aby znacznie zwiększyć prędkość *(żeby szybko obejrzeć skomplikowane ścieżki)*.
    -   Wciśnij przycisk <img alt="" src=images/CAM_BPause.svg  style="width:24px;"> *(Wstrzymaj symulację)* aby zatrzymać animację do rozwiązania problemów
    -   Wciśnij przycisk <img alt="" src=images/CAM_BStep.svg  style="width:24px;"> *(Symulacja pojedynczym krokiem)* aby spowolnić animację, co ułatwia rozwiązywanie problemów i przyglądanie się konkretnym cięciom i/lub ruchom.
    -   Wciśnij przycisk <img alt="" src=images/CAM_BStop.svg  style="width:24px;"> *(Zatrzymaj aktywną symulację)* aby zatrzymać animację.
6.  Wciśnięcie przycisku **Anuluj** usunie materiał obrabiany utworzony dla symulacji. Wciśnięcie **OK** spowoduje jego zachowanie w Twoim zadaniu obróbki.



## Właściwości

-    **Prędkość**: Prędkość odtwarzania symulacji, w liniach G-code na sekundę.

-    **Dokładność**: Dokładność symulacji wyrażona jako procent wskazujący rozbieżność symulacji od zadania obróbki. W przypadku interaktywnych symulacji, redukcja dokładności do 0.3 działa znacznie szybciej.

-    **Zadanie**: Zadanie obróbki używane jako podstawa symulacji

-    **Lista operacji**: Lista operacji wybranych do uwzględnienia w symulacji.





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Simulator/pl
