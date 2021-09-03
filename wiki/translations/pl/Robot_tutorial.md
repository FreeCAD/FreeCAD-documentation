 {{TutorialInfo/pl
|Topic= Środowisko pracy Robot
|Level= początkujący
|Time= dowolny
|Author=r-frank
|FCVersion=0.16.6703
|Files=nie dołączono
}}

## Wprowadzenie

W tym poradniku przedstawiono, jak korzystać z <img alt="" src=images/_Workbench_Robot.svg  style="width:24px;"> [Środowiska pracy Robot](Robot_Workbench/pl.md) do symulacji konfiguracji jednostki robota.

![](images/Robot_Tutorial_RobotSimulation.gif ) *Efekt końcowy tego poradnika.*

## Przed rozpoczęciem 

Ten poradnik jest napisany dla FreeCAD w wersji 0.16.6703 lub wyższej. Więc jeśli nie masz programu FreeCAD na swoim komputerze przejdź do strony [pobierania](Download.md) i wykonaj instalację.

Niniejszy poradnik jest skierowany do wykorzystania [Robotów przemysłowych](http://en.wikipedia.org/wiki/Industrial_robot) a nie robotów ruchomych lub usługowyych *(zobacz stronę Wikipedii [współczesne roboty](http://en.wikipedia.org/wiki/Robot#Modern_robots))*.

## Przygotowanie sceny 

1.  Włącz Środowisko pracy <img alt="" src=images/Workbench_Robot.svg  style="width:24px;"> [Robot](Robot_Workbench/pl.md).
2.  Utwórz nowy dokument wybierając z menu głównego **Plik** → **Nowy**.
3.  Wstaw robota Kuka IR500 do sceny wybierając z menu głównego **Robot** → **Wstaw roboty** → **Kuka IR500**.
4.  Przełącz się na widok aksonometryczny klikając na przycisk <img alt="" src=images/View-axometric.svg  style="width:24px;">.
5.  Przybliż, aby dopasować widok klikając na <img alt="" src=images/Std_ViewFitAll.svg  style="width:24px;"> przycisk [Dopasuj rozmiar do okna](Std_ViewFitAll.md).
6.  Zapisz swój dokument\...

## Ustalenie trajektorii ruchów 

1.  Włącz Środowisko pracy <img alt="" src=images/Workbench_Robot.svg  style="width:24px;"> [Robot](Robot_Workbench/pl.md).
2.  Aktywuj zakładkę model w [widoku drzewa](tree_view/pl.md) klikając na nią.
3.  Utwórz nową trajektorię klikając na przycisk <img alt="" src=images/Robot_CreateTrajectory.svg  style="width:24px;"> [Utwórz nową pustą trajektorię](Robot_CreateTrajectory.md).
4.  Wybierz robota w [widoku drzewa](tree_view/pl.md).
5.  Ustaw pozycję wyjściową dla robota klikając na przycisk <img alt="" src=images/Robot_SetHomePos.svg  style="width:24px;"> [Ustaw pozycję startową](Robot_SetHomePos.md).
6.  przełącz widok na [panel zadań](Task_Panel.md) w [widoku połączonym](Combo_view/pl.md).
7.  Za pomocą suwaków zmień pozycję robota.
8.  Gdy robot i obiekt trajektorii są wybrane w [widoku drzewa](tree_view/pl.md) kliknięcie na przycisk <img alt="" src=images/Robot_InsertWaypoint.svg  style="width:24px;"> [Ustaw lokację narzędzia na trajektorię](Robot_InsertWaypoint.md) wstawi punkt trasy w trajektorii.
9.  Każdy punkt trasy jest oznaczony żółtym krzyżykiem, punkty trasy są połączone pomarańczową linią.
10. Zdefiniuj co najmniej trzy różne punkty orientacyjne i wstaw je do toru ruchu.

## Symulacja ruchów robota 

1.  Wybierz robota i zaprojektowaną trajektorię na [widoku drzewa](tree_view/pl.md).
2.  Wybierz symulację, klikając na przycisk <img alt="" src=images/Robot_Simulate.svg  style="width:24px;"> [Symulacja robota](Robot_Simulate.md).
3.  Kliknij na przycisk Odtwarzaj ** &#9654;**.
4.  Oglądaj efekty.


{{Tutorials navi

}} {{Robot Tools navi}} 
