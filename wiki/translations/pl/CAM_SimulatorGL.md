---
 GuiCommand:
   Name: CAM SimulatorGL
   Name/pl: CAM: Nowy symulator
   MenuLocation: CAM , Nowy symulator
   Workbenches: CAM_Workbench/pl
   Shortcut: **P** **N**
   Version: 1.0
   SeeAlso: CAM_Simulator/pl
---

# CAM SimulatorGL/pl



## Opis

Narzędzie <img alt="" src=images/CAM_SimulatorGL.svg  style="width:24px;"> [Nowy symulator](CAM_SimulatorGL/pl.md) to nowa alternatywa dla [Symulatora](CAM_Simulator/pl.md). Jest oparty o funkcje OpenGL niskiego poziomu. Aby wyeliminować konflikty z oknem 3D programu FreeCAD, nowy symulator działa w osobnym oknie z oddzielnym kontekstem OpenGL. Z założenia jest szybszy i bardziej precyzyjny niż stary symulator.

<img alt="" src=images/CAM_new_simulator.PNG  style="width:600px;">



## Użycie

1.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Naciśnij przycisk **<img src="images/CAM_SimulatorGL.svg" width=16px> [Nowy symulator](CAM_SimulatorGL/pl.md)**.
    -   Wybierz opcję **CAM → <img src="images/CAM_Simulator.svg" width=16px> Nowy symulator** z menu.
    -   Użyj skrótu klawiaturowego: **P** a następnie **N**.
2.  Odznacz wszystkie **Operacje**, które nie mają być symulowane.
3.  Dostosuj ustawienie **Dokładność**.
4.  Wybierz **Zadanie** do symulacji z menu rozwijanego.
5.  Naciśnij przycisk <img alt="" src=images/CAM_BPlay.svg  style="width:24px;"> (Aktywuj / wznów symulację).
    -   Otworzy się oddzielne okno z symulatorem.
    -   Używaj przycisków po lewej stronie: Odtwórz, Pojedynczy krok i Przyspiesz oraz suwaka do kontrolowania animacji.
    -   Używaj przycisków po prawej stronie: Pokaż/ukryj nakładkę modelu bazowego, Obrót modelu, Wyświetlenie ścieżki i Włącz/wyłącz Ambient Occlusion.
    -   Steruj widokiem 3D za pomocą aktualnego sterowania 3D we FreeCAD.



## Właściwości

-    **Dokładność**: Dokładność symulacji wyrażona jako procent wskazujący rozbieżność symulacji od zadania obróbki. W przypadku interaktywnych symulacji, redukcja dokładności do 0.3 działa znacznie szybciej.

-    **Zadanie**: Zadanie obróbki używane jako podstawa symulacji

-    **Lista operacji**: Lista operacji wybranych do uwzględnienia w symulacji.





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM SimulatorGL/pl
