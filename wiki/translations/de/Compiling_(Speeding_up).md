# Compiling (Speeding up)/de
{{TOCright}}



## Übersicht

FreeCAD ist eine große Anwendung, deren vollständige Kompilierung aus dem Quellcode zwischen 10 Minuten und einer Stunde dauern kann. Dies hängt in erster Linie von der CPU ab, die du hast, und von der Anzahl der Kerne, die im Kompilierungsprozess verwendet werden. Hier sind einige Tipps, um diesen Prozess zu verkürzen und die Erstellungszeiten zu verkürzen.

## CCache


<div class="mw-translate-fuzzy">

## CCache 

Installiere `ccache` zur Bau Zwischenspeicherung.


</div>

[Ccache](https://ccache.dev/) speeds up recompilation by caching previous compilations and detecting when the same compilation is done again. Ccache is free software, released under GPLv3 or later.

On most systems ccache will be automatically detected and enabled, you can use the `FREECAD_USE_CCACHE` `cmake` option to control this behavior.

## Disable modules 


<div class="mw-translate-fuzzy">

## Module deaktivieren 

Wenn `cmake` zur Konfiguration der Bauten verwendet werden, kannst du die Kompilierung bestimmter Arbeitsbereiche deaktivieren, die du im Moment möglicherweise nicht benötigst. Dies ist nützlich, wenn du nur einige wenige Arbeitsbereiche testen musst.


</div>

Zum Beispiel, um den Bau der FEM- und Polygonnetz Arbeitsbereiche zu vermeiden:


```python
cmake -DBUILD_FEM=OFF -DBUILD_MESH=OFF ../freecad-source
```

Verwende `cmake-gui`, `cmake-curses-gui`, oder `cmake-qt-gui`, um alle möglichen Variablen anzuzeigen, die in der Konfiguration bearbeitet werden können; über diese Schnittstellen kannst du verschiedene Arbeitsbereiche leicht ein- oder ausschalten.

## Number of jobs in parallel 


<div class="mw-translate-fuzzy">

## Anzahl der parallelen Aufträge 

Nach der Konfiguration mit `cmake` startet das Programm `make` den eigentlichen C++-Compiler, um an den Quelltextdateien zu arbeiten. Du kannst die Kompilierung beschleunigen, indem du an verschiedenen Dateien gleichzeitig arbeitest. Dies wird mit der Option `-j` von `make` erreicht, die die Anzahl der gleichzeitig ausgeführten \"Jobs\" oder Kompilierungsbefehle angibt. Diese Option ist eine Ganzzahl.


</div>

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


<div class="mw-translate-fuzzy">

## distcc 

Das Programm `distcc` kann verwendet werden, um eine verteilte Kompilierung von C- und C++-Code über mehrere Maschinen in einem Netzwerk durchzuführen.


</div>

[Distcc](https://www.distcc.org/) should always generate the same results as a local compilation. It is free, simple to install and use, and often two or more times faster than compiling locally.

FreeCAD dev \'etrombly\' has published a short explanation on [how to install distcc to compile FreeCAD on a network of computers using Docker](https://forum.freecadweb.org/viewtopic.php?f=4&t=50810&p=459142#p458614).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compiling (Speeding up)/de
