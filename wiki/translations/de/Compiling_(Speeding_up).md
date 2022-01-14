# Compiling (Speeding up)/de
{{TOCright}}

## Übersicht

FreeCAD ist eine große Anwendung, deren vollständige Kompilierung aus dem Quellcode zwischen 10 Minuten und einer Stunde dauern kann. Dies hängt in erster Linie von der CPU ab, die du hast, und von der Anzahl der Kerne, die im Kompilierungsprozess verwendet werden. Hier sind einige Tipps, um diesen Prozess zu verkürzen und die Erstellungszeiten zu verkürzen.

## CCache

Installiere `ccache` zur Bau Zwischenspeicherung.

## Module deaktivieren 

Wenn `cmake` zur Konfiguration der Bauten verwendet werden, kannst du die Kompilierung bestimmter Arbeitsbereiche deaktivieren, die du im Moment möglicherweise nicht benötigst. Dies ist nützlich, wenn du nur einige wenige Arbeitsbereiche testen musst.

Zum Beispiel, um den Bau der FEM- und Polygonnetz Arbeitsbereiche zu vermeiden:


```python
cmake -DBUILD_FEM=OFF -DBUILD_MESH=OFF ../freecad-source
```

Verwende `cmake-gui`, `cmake-curses-gui`, oder `cmake-qt-gui`, um alle möglichen Variablen anzuzeigen, die in der Konfiguration bearbeitet werden können; über diese Schnittstellen kannst du verschiedene Arbeitsbereiche leicht ein- oder ausschalten.

## Anzahl der parallelen Aufträge 

Nach der Konfiguration mit `cmake` startet das Programm `make` den eigentlichen C++-Compiler, um an den Quelltextdateien zu arbeiten. Du kannst die Kompilierung beschleunigen, indem du an verschiedenen Dateien gleichzeitig arbeitest. Dies wird mit der Option `-j` von `make` erreicht, die die Anzahl der gleichzeitig ausgeführten \"Jobs\" oder Kompilierungsbefehle angibt. Diese Option ist eine Ganzzahl.

Führe vier Kompilierungsbefehle parallel aus:


```python
make -j4
```

Kompiliere so viele Dateien parallel wie die Anzahl der CPU-Kerne in Deinem System. Dies ist nützlich, wenn Du viele Kerne hast und diese alle zum Kompilieren der Software verwenden möchtest.


{{code|code=
make -j$(nproc)
}}

Kompiliere so viele Dateien parallel wie die Anzahl der CPU-Kerne in Deinem System, minus zwei. Verwende dies, damit Dein System immer noch auf eine andere Aufgabe reagiert, z.B. zwei Kerne, die es Dir ermöglichen, einen Browser zu verwenden, während der Rest der Kerne die Software im Hintergrund kompiliert.


{{code|code=
make -j$(nproc --ignore=2)
}}

## distcc

Das Programm `distcc` kann verwendet werden, um eine verteilte Kompilierung von C- und C++-Code über mehrere Maschinen in einem Netzwerk durchzuführen.







[<img src="images/Property.png" style="width:16px"> Developer\_Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Developer](Category_Developer.md)

---
[documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > Compiling (Speeding up)/de
