# Robot Workbench/pl
**Środowisko pracy FreeCAD Robot nie jest utrzymywane. Jeśli masz doświadczenie w tym temacie i jesteś zainteresowany jego utrzymaniem, poinformuj o swoich zamiarach w sekcji dla deweloperów na forum [https://forum.freecadweb.org/index.php FreeCAD].

Powodem, dla którego ten warsztat jest nadal w głównym kodzie źródłowym jest to, że jest on zaprogramowany w C++. Jeśli mógłby być zaprogramowany w Pythonie, to można by utworzyć [zewnętrzne środowisko](external_workbenches.md) i mógłby być przeniesiony do osobnego repozytorium.
**

## Wprowadzenie

<img alt="Ikonka Środowiska pracy Robot" src=images/Workbench_Robot.svg  style="width:128px;">

<img alt="" src=images/Workbench_Robot.svg  style="width:24px;"> [Środowisko pracy Robot](Robot_Workbench.md) jest narzędziem do symulacji standardowego [6-osiowego robota przemysłowego](Robot_6-Axis.md), na przykład [Kuka](http://kuka.com/).

Możesz wykonywać następujące zadania:

-   Ustawić środowisko symulacyjne z robotem i elementami roboczymi.
-   Stworzyć i wypełnić trajektorie ruchu.
-   Rozłożyć cechy elementów CAD na trajektorię.
-   Symulować ruch robota i osiąganie odległości.
-   Wyeksportować trajektorię do pliku programu robota.

Na wstępie wypróbuj [Samouczek robota](Robot_tutorial.md), i zobacz interfejs programowania w pliku [RobotExample.py](https://github.com/FreeCAD/FreeCAD_sf_master/blob/master/src/Mod/Robot/RobotExample.py).


{{TOCright}}

<img alt="" src=images/Robot_Workbench_example.jpg  style="width:500px;">

## Narzędzia

Tutaj znajdują się główne polecenia, których można użyć do stworzenia konfiguracji dla robota.

### Roboty

Narzędzia do tworzenia i zarządzania robotami 6-osiowymi.

-   <img alt="" src=images/Robot_CreateRobot.svg  style="width:30px;"> [Wstaw robota](Robot_CreateRobot/pl.md): Umieść nowego robota na scenie.
-   <img alt="" src=images/Robot_Simulate.svg  style="width:30px;"> [Uruchom symulacje trajektorii](Robot_Simulate/pl.md): Otwiera okno dialogowe symulacji i pozwala na rozpoczęcie symulacji.
-   <img alt="" src=images/Robot_Export.svg  style="width:30px;"> [Eksport trajektorii](Robot_Export/pl.md): Eksport pliku programu robota.
-   <img alt="" src=images/Robot_SetHomePos.svg  style="width:30px;"> [Ustaw pozycję startową](Robot_SetHomePos/pl.md): Ustawianie pozycji startowej robota.
-   <img alt="" src=images/Robot_RestoreHomePos.svg  style="width:30px;"> [Przejdź do pozycji startowej](Robot_RestoreHomePos/pl.md): Ustaw robota w pozycji startowej.

### Tor ruchu 

Narzędzia do tworzenia i manipulowania trajektoriami. Istnieją dwa podstawowe rodzaje, parametryczne i nie parametryczne.

#### Trajektorie nie parametryczne 

-   <img alt="" src=images/Robot_CreateTrajectory.svg  style="width:30px;"> [Utwórz trajektorię](Robot_CreateTrajectory/pl.md): Wstawia nowy pusty obiekt trajektorii do sceny.
-   <img alt="" src=images/Robot_SetDefaultOrientation.svg  style="width:30px;"> [Ustaw domyślną orientację](Robot_SetDefaultOrientation/pl.md): Punkty orientacyjne są tworzone jako domyślne.
-   <img alt="" src=images/Robot_SetDefaultValues.svg  style="width:30px;"> [Ustaw wartości domyślne](Robot_SetDefaultValues/pl.md): Ustaw wartości domyślne dla sposobu tworzenia punktów trasy.
-   <img alt="" src=images/Robot_InsertWaypoint.svg  style="width:30px;"> [Wstaw pozycje narzędzia \...](Robot_InsertWaypoint/pl.md): Wstaw punkt trasy z bieżącej pozycji robota do trajektorii.
-   <img alt="" src=images/Robot_InsertWaypointPre.svg  style="width:30px;"> [Wstaw wstępnie wybrany punkt trasy](Robot_InsertWaypointPre/pl.md): Wstaw w trajektorię punkt orientacyjny z aktualnej pozycji kursora myszki.

#### Trajektorie parametryczne 

-   <img alt="" src=images/Robot_Edge2Trac.svg  style="width:30px;"> [Generuj trasę z krawędzi](Robot_Edge2Trac/pl.md): Wstaw nowy obiekt, którego krawędzie zostaną rozłożone na trajektorię.
-   <img alt="" src=images/Robot_TrajectoryDressUp.svg  style="width:30px;"> [Ukształtuj trajektorię](Robot_TrajectoryDressUp/pl.md): Pozwala nadpisać jedną lub więcej właściwości trajektorii.
-   <img alt="" src=images/Robot_TrajectoryCompound.svg  style="width:30px;"> [Grupuj i połącz trajektorie](Robot_TrajectoryCompound/pl.md): Stworzy układ złożony z kilku pojedynczych trajektorii.

## Tworzenie skryptów 

Aby uzyskać opis funkcji używanych do modelowania przemieszczeń robota, zobacz [Przykład API dla robota](Robot_API_example/pl.md).

## Poradniki

-   [Robot 6-Axis](Robot_6-Axis/pl.md)
-   [VRML przygotowanie symulacji robota](VRML_Preparation_for_Robot_Simulation/pl.md)





{{Robot Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Robot](Category_Robot.md) > Robot Workbench/pl
