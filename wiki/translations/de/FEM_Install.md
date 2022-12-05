# FEM Install/de
{{TOCright}}

## Einführung

Um die Finite Element Analyse (FEA) innerhalb des **<img src="images/Workbench_FEM.svg" width=24px> [FEM Arbeitsbereichs](FEM_Workbench/de.md)** durchführen zu können, verwendet FreeCAD zwei externe Programme: eines wird für die Generierung des [FEM Netz](FEM_Mesh/de.md) verwendet, das andere für die numerische Lösung der eigentlichen Analyse. Du kannst testen, ob dein FreeCAD Installation für die FEA bereit ist, indem du das [FEM CalculiX Kragarm 3D](FEM_CalculiX_Cantilever_3D/de.md) Beispiel ausführen, das in jeder Installation von FreeCAD seit v0.17 enthalten ist.

<img alt="" src=images/FEM_Workbench_workflow.svg  style="width:600px;"> 
* Arbeitsablauf des FEM Arbeitsbereichs; der Arbeitsbereich ruft zwei externe Programme auf, um die Vernetzung eines festen Objekts und die eigentliche Lösung des Finite Element Problems durchzuführen.*

### FEM Löser 

Der Standard Löser zur Durchführung von Finite Elemente Berechnungen ist [CalculiX](FEM_CalculiX/de.md), ein einfacher Löser zur Analyse von Strukturen. FreeCAD schreibt eine CalculiX Eingabedatei, startet den Löser und liest die Ausgabe, die dann visuell im Ansichtsfenster dargestellt werden kann; das bedeutet, dass das CalculiX Binärdatei eigenständig und unabhängig von FreeCAD ist. In Anbetracht der Tatsache, dass es viele Programme gibt, die ein Netz generieren können, **ist es empfehlenswert, den Löser zu installieren und sicherzustellen, dass er zuerst funktioniert**.

Wenn der Löser korrekt installiert ist, kannst du den einzelnen Befehl `ccx` im Terminal ausführen, um eine einfache Antwort zu erhalten:


{{SystemInput|User@PC:~$ ccx}}


```python
Usage: CalculiX.exe -i jobname
```

Wenn der Löser installiert ist, stelle sicher, dass der FEM Arbeitsbereich in der Lage ist, die Binärdatei zu finden; gehe zu **Bearbeiten → Einstellungen → FEM → CalculiX → In bekannten Binärverzeichnissen suchen**. Wenn du den Löser selbst kompiliert hast, deaktiviere die Option, und gib den korrekten Pfad zur Binärdatei an. Für andere Löser, die mit FreeCAD verwendet werden können, siehe [FEM Löser](FEM_Solver/de.md).

### FEM Netz Generator 

Um ein [FEM Polygonnetz](FEM_Mesh/de.md) zu erstellen, verwendet FreeCAD [Gmsh](http://gmsh.info/) als Standard Netzerzeuger. Abhängig vom Betriebssystem und der FreeCAD-Installation, ist Gmsh in den FreeCAD-Installationsdateien vorhanden oder auch nicht. Wenn es nicht mitgeliefert wird, kann es unabhängig von FreeCAD installiert werden und anschließend das Menü **Edit → Preferences → FEM → Gmsh** verwendet werden, um den Pfad zu *gmsh.exe* einzugeben.

Wenn das Programm korrekt installiert ist, kannst du den Befehl `gmsh` im Terminal ausführen, um die grafische Oberfläche des Programms zu starten. Diese Oberfläche wird von FreeCAD nicht verwendet, zeigt aber an, dass das Programm installiert ist.


{{SystemInput|User@PC:~$ gmsh -info}}


```python
Version          : 3.0.6
License          : GNU General Public License
Build OS         : Linux64
Build date       : 20171107
Build host       : lgw01-amd64-034
Build options    : 64Bit Ann Bamg Bfgs Blas(Generic) Blossom C++11 Cgns Chaco DIntegration Dlopen Fltk Gmm Jpeg Kbipack Lapack(Generic) LinuxJoystick MPI MathEx Med Mesh Mmg3d Mpeg NativeFileChooser Netgen ONELAB ONELABMetamodel OpenCASCADE OpenGL OptHom Parser Plugins Png Post Python Solver TetGen/BR Tetgen Voro3D Zlib
FLTK version     : 1.3.4
OCC version      : 6.9.1
MED version      : 3.0.6
Packaged by      : buildd
Web site         : http://gmsh.info
Mailing list     : gmsh@onelab.info
```

Wenn der Netzerzeuger installiert ist, stelle sicher, dass der FEM Arbeitsbereich in der Lage ist, die Binärdatei zu finden; gehe zu **Bearbeiten → Einstellungen → FEM → Gmsh → In bekannten Binärverzeichnissen suchen**. Wenn du den Löser selbst kompiliert hast, deaktiviere die Option, und gib den korrekten Pfad zur Binärdatei an. Siehe [FEM Polygonetz](FEM_Mesh/de.md) für verschiedene Möglichkeiten, ein gültiges Netz für die Analyse zu erhalten.

### Netgen


**Hinweis: Der Netgen Netzerzeuger wurde im März 2017 deaktiviert, als FreeCAD auf die Verwendung von OCCT 7.1 umgestellt wurde. Bitte bearbeiten Sie diese Information, wenn Netgen mit der stabilen Version von FreeCAD wieder nutzbar ist.**

In früheren Versionen von FreeCAD war [Netgen](https://sourceforge.net/projects/netgen-mesher/) der Standard Netzerzeuger. Damit es mit dem FEM Arbeitsbereich funktioniert, musste FreeCAD zur Kompilierzeit mit den Netgen Bibliotheken gelinkt werden. Als FreeCAD von OCE 0.17 auf OCCT 7.1 überging, konnte Netgen 4.9.13 nicht mehr gegen diese Version von OCCT gelinkt werden, so dass beschlossen wurde, die Netgen Unterstützung im [FEM Arbeitsbereich](FEM_Workbench/de.md) zu beenden. (die Schaltfläche [Netgen](FEM_MeshNetgenFromShape/de.md) wurde entfernt). Nichtsdestotrotz berichteten einige Anwender kurz darauf von Erfolgen beim Patchen von Netgen 5.3.1, so dass es mit OCCT 7.x und FreeCAD funktionierte.

Als historische Referenz siehe die Beiträge:

-   [(Ubuntu Daily PPA) Transitioning to OCCT7, VTK7\...](https://forum.freecadweb.org/viewtopic.php?f=4&t=17501)
-   [Ubuntu Daily Builds PPA verwendet jetzt OCC 7.1.0](https://forum.freecadweb.org/viewtopic.php?t=21246)
-   [patching Netgen 5.3.1](https://forum.freecadweb.org/viewtopic.php?f=4&t=17501&start=200#p165769) um mit OCCT 7.1 zu arbeiten
-   [Probleme mit gmsh in FEM wb (netgen nostalgy)](https://forum.freecadweb.org/viewtopic.php?t=28368)

Obwohl Netgen nicht aus dem [FEM Arbeitsbereich](FEM_Workbench/de.md) heraus verfügbar ist, kann es dennoch allein verwendet werden, um Netze zu erzeugen, die dann importiert werden können.

Wenn das Programm korrekt installiert ist, kannst du den Befehl `netgen` im Terminal ausführen, um die grafische Oberfläche des Programms zu starten.


{{SystemInput|User@PC:~$ netgen -V}}


```python
NETGEN-6.2-dev
Developed by Joachim Schoeberl at
2010-xxxx Vienna University of Technology
2006-2010 RWTH Aachen University
1996-2006 Johannes Kepler University Linz
Including OpenCascade geometry kernel
Run parallel Netgen with 'mpirun -np xy netgen'
NETGENDIR = .
Tcl header version = 8.6.8
Tcl runtime version = 8.6.8 
using internal Tcl-script
optfile ./ng.opt does not exist - using default values
togl-version : 2
OCC module loaded
```

## Installation unter Windows 

Die auf der [Herunterladen](Download/de.md) Seite verfügbaren FreeCAD Pakete enthalten bereits Netgen und CalculiX, so dass keine zusätzliche Software installiert werden muss. Einige Verweise, wo eine bessere ausführbare Calculix Datei als die in FreeCAD enthalten bekommen kann, können hier unter [alternative ccx ausführbare Dateien](https://forum.freecadweb.org/viewtopic.php?f=18&t=58792&start=10#p506164) gefunden werden.


<div class="mw-collapsible mw-collapsed toccolours">

## Installation unter Linux 

Linux Distributionen haben unterschiedliche Möglichkeiten, Software zu installieren. Viele Distributionen haben Software Repositorien und Paketmanager; Vor dem kompilieren des Quellcodes, schau in deinem Paketmanager nach `netgen`, `gmsh`, `calculix-ccx` oder `ccx`, und installiere diese nach den Anweisungen deiner eigenen Distribution.


<div class="mw-collapsible-content">

### Ubuntu PPA 

Die [freecad-stable](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-stable) und [freecad-daily](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) persönlichen Paketarchive (PPA) bieten eine aktuellere Version von FreeCAD als in den offiziellen Ubuntu Repositorien verfügbar ist. Diese PPAs enthalten auch die aktuellsten Pakete `netgen`, `gmsh` und `calculix-ccx`. Siehe [Installieren unter Linux](Installing_on_Linux/de.md) für weitere Informationen zum Einrichten der Repositorien.

Wenn ein PPA bereits zu deinem System hinzugefügt wurde, installiere die Pakete wie folgt


```python
sudo apt-get install netgen
sudo apt-get install gmsh
sudo apt-get install calculix-ccx
```

Das [freecad-community](https://launchpad.net/~freecad-community/+archive/ubuntu/ppa) PPA stellt auch die Pakete `netgen`, `gmsh` und `calculix-ccx` zum Testen bereit. Wenn sie stabil genug sind, können sie zu den täglichen oder stabilen Repositorien hinzugefügt werden. Die Binärdateien für ccx 2.14 funktionieren unter Debian Stretch, aber nicht unter Debian Buster aufgrund von Abhängigkeitsproblemen.


**Hinweis:**

Der Beitrag [Ubuntu Repositorium](http://forum.freecadweb.org/viewtopic.php?f=18&t=10393) behandelt die Erstellung der Ubuntu PPA Pakete. Zu der Zeit, als er geschrieben wurde, war CalculiX nicht in den Debian Repositorien enthalten, daher gab es mehrere persönliche Pakete in Launchpad. Es sollte nur ein Paket installiert werden.

### Arch Linux 

Hol dir das CalculiX Paket aus dem [AUR Repositorium](https://aur.archlinux.org/packages/calculix/).

### Debian

-   Debian 9 Buster: die Pakete im [Repositorium](https://packages.debian.org/buster/calculix-ccx) sind veraltet, aber du kannst die Pakete aus dem Ubuntu PPA (`freecad-community`) verwenden. Siehe [Gmsh 4 Paket im Community Extras PPA zum Testen verfügbar](https://forum.freecadweb.org/viewtopic.php?f=18&t=31360&start=10#p279925) (Forenbeitrag).
-   Debian 8 Stretch: die Pakete im [repository](https://packages.debian.org/stretch/calculix-ccx) sind veraltet, aber du kannst die Pakete aus dem Ubuntu PPA (`freecad-community`) verwenden. Siehe [Gmsh 4 Paket verfügbar zum Testen im Community Extras PPA](https://forum.freecadweb.org/viewtopic.php?f=18&t=31360&p=279925#p260872) (Forumsbeitrag).
-   Debian 7 Jessie: Installiere die Pakete von Debian 8 Stretch mit `dpkg`. Siehe [Debian Quellpaket für Calculix](http://forum.freecadweb.org/viewtopic.php?f=4&t=5975&p=110597#p110597) (Forenbeitrag).

### openSUSE

-   [openSUSE:Science Math](https://en.opensuse.org/openSUSE:Science_Math#Mesh_Generation_and_Related_Tools)
-   [netgen Automatischer 3D-Tetraedernetz-Generator](https://software.opensuse.org/package/netgen)
-   [gmsh Ein Generator für dreidimensionale Finite Elemente Netze](https://software.opensuse.org/package/gmsh)
-   [ccx Ein quelloffenes Finite Elemente Paket](https://software.opensuse.org/package/ccx)

Zusätzliche Pakete werden typischerweise mit YAST (Abk. Yet another Setup Tool)(deutsch: Noch ein anderes Einrichtungswerkzeug), dem Einrichtungs- und Konfigurationswerkzeug für das Linux Betriebssystem, oder in jedem Terminal/Konsole (root Rechte erforderlich) mit:

:   
    
```python
    zypper install netgen
    zypper install gmsh
    zypper install ccx
    
```
    

### CalculiX Binärdatei 

Die CalculiX Autoren stellen ein vorkompiliertes Linux Binärdatei des Lösers zur Verfügung; es kann von der [Autoren Webseite](http://www.dhondt.de/) heruntergeladen werden. Da jedoch verschiedene Linux Distributionen unterschiedliche Bibliothekspfade haben, wird diese Binärdatei höchstwahrscheinlich nicht funktionieren, ohne einige Anpassungen vorzunehmen.

Um das Binärdatei mit Fedora 21 zu verwenden, siehe den Beitrag [FEM unter Linux fedora 21 zum Laufen bringen](http://forum.freecadweb.org/viewtopic.php?f=18&t=10140). Für neuere Fedora Versionen solltest du CalculiX selbst kompilieren.

Wenn du diese Binärdatei verwendest, überprüfe, dass die Binärdatei ausführbar ist, dass sie sich im ausführbaren `$PATH` deines Systems befindet und dass du die erforderliche Version der Bibliotheken (`libgfortran`, `liblapack`, `libblas`, usw.) hast, gegen die sie kompiliert wurde. Dies wird im Forumsbeitrag [FEM WB](http://forum.freecadweb.org/viewtopic.php?f=3&t=11830&start=20#p95741) erwähnt.

Verwende den Befehl `ldd`, um die Bibliotheken anzuzeigen, die von der Binärdatei gelinkt werden. Installiere alle fehlenden Abhängigkeiten.


{{SystemInput|User@PC:~$ ldd /usr/bin/ccx}}


```python
linux-vdso.so.1 (0x00007fffbabdc000)
 libspooles.so.2.2 => /usr/lib/x86_64-linux-gnu/libspooles.so.2.2 (0x00007fe9bd042000)
 libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fe9bce23000)
 libarpack.so.2 => /usr/lib/x86_64-linux-gnu/libarpack.so.2 (0x00007fe9bcbd9000)
 liblapack.so.3 => /usr/lib/x86_64-linux-gnu/liblapack.so.3 (0x00007fe9bc353000)
 libgfortran.so.4 => /usr/lib/x86_64-linux-gnu/libgfortran.so.4 (0x00007fe9bbf74000)
 libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fe9bbbd6000)
 libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fe9bb7e5000)
 libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007fe9bb5cd000)
 libmpi.so.20 => /usr/lib/x86_64-linux-gnu/libmpi.so.20 (0x00007fe9bb2db000)
 /lib64/ld-linux-x86-64.so.2 (0x00007fe9bdaa9000)
 libblas.so.3 => /usr/lib/x86_64-linux-gnu/libblas.so.3 (0x00007fe9bb080000)
 libopenblas.so.0 => /usr/lib/x86_64-linux-gnu/libopenblas.so.0 (0x00007fe9b8dda000)
 libquadmath.so.0 => /usr/lib/x86_64-linux-gnu/libquadmath.so.0 (0x00007fe9b8b9a000)
 libopen-rte.so.20 => /usr/lib/x86_64-linux-gnu/libopen-rte.so.20 (0x00007fe9b8912000)
 libopen-pal.so.20 => /usr/lib/x86_64-linux-gnu/libopen-pal.so.20 (0x00007fe9b8660000)
 librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007fe9b8458000)
 libhwloc.so.5 => /usr/lib/x86_64-linux-gnu/libhwloc.so.5 (0x00007fe9b821b000)
 libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fe9b8017000)
 libutil.so.1 => /lib/x86_64-linux-gnu/libutil.so.1 (0x00007fe9b7e14000)
 libnuma.so.1 => /usr/lib/x86_64-linux-gnu/libnuma.so.1 (0x00007fe9b7c09000)
 libltdl.so.7 => /usr/lib/x86_64-linux-gnu/libltdl.so.7 (0x00007fe9b79ff000)
```

### CalculiX kompilieren 

Da CalculiX eine eigenständige Anwendung ist, kannst du entweder eine für deine Distribution gepackte Binärdatei installieren oder sie selbst kompilieren. Jede CalculiX Version ab 2.7.x sollte mit FreeCAD funktionieren, und da der Code in den letzten Jahren nicht viel geändert wurde, können auch niedrigere Versionen als 2.7.x funktionieren.

Das Kompilieren von CalculiX ist eine Aufgabe für erfahrene Anwender und erfordert die Bearbeitung der Makefiles und Build Optionen auf verschiedenen Plattformen. Siehe die folgenden Informationen:

-   Debian: [Debian-Quellpaket für Calculix](http://forum.freecadweb.org/viewtopic.php?f=4&t=5975&start=10), [Gmsh 4 Paket verfügbar zum Testen im Community Extras PPA](https://forum.freecadweb.org/viewtopic.php?f=18&t=31360&start=10#p260506), [Kompilieren CalculiX ccx unter fedora, ubuntu und debian](https://forum.freecadweb.org/viewtopic.php?f=18&t=34024).
-   Fedora 27, 28, 29: [Kompilieren CalculiX ccx unter fedora, ubuntu und debian](https://forum.freecadweb.org/viewtopic.php?f=18&t=34024).
-   Es gibt eine CMake Version des Quellpakets in einem [github repository](https://github.com/ricortiz/CalculiX-cmake), aber in den FreeCAD Foren hat niemand berichtet, ob dieses Paket funktioniert.

### Netgen kompilieren 

Netgen wurde ursprünglich von FreeCAD verknüpft, als FreeCAD OCE, die Gemeinschaftsabspaltung von OpenCascade (OCCT), verwendete. Da OCE in der Entwicklung hinter OCCT zurückblieb, wechselte FreeCAD zurück zu OCCT. Dadurch wurde die Verknüpfung von Netgen unterbrochen, das nur gegen OCCT 6.9 oder OCE 0.18 und darunter verknüpft werden konnte. Da die OCCT 7.x Versionen die Kernfunktionalität von FreeCAD verbesserten, wurde beschlossen, die Netgen Unterstützung zugunsten von Gmsh aufzugeben.

Seitdem ist es gelungen, neuere Versionen von Netgen auszubessern und mit OCCT 7.x zu verbinden. Dennoch ist die Einbindung von Netgen in FreeCAD immer noch problematisch.


</div>


</div>

## Installation unter MacOSX 


**Diese Informationen könnten veraltet sein. Wenn du ein OSX Benutzer bist, teste und bereinige bitte diesen Abschnitt**

Die OSX [Entwicklungspakete](https://github.com/FreeCAD/FreeCAD/releases) von FreeCAD enthalten möglicherweise Netgen, aber nicht CalculiX.

Siehe diesen Forumsbeitrag [FEM on Mac OSX](https://forum.freecadweb.org/viewtopic.php?f=18&t=10979&p=198652#p198642) für Informationen zur Installation von CalculiX, und einen [aktualisierter Beitrag](https://forum.freecadweb.org/viewtopic.php?f=18&t=10979&start=90#p273746) für neuere Informationen.

CalculiX:

-   [CalculiX mit brew installieren](https://forum.freecadweb.org/viewtopic.php?f=18&t=10979&start=90#p508724)

Die folgenden Beiträge sind möglicherweise veraltet:

-   [FEM auf Mac OSX, Beitrag 1](http://forum.freecadweb.org/viewtopic.php?f=18&t=10979)
-   [MacPorts Benutzer: CalculiX port Test Anfrage](http://forum.freecadweb.org/viewtopic.php?f=8&t=14497)

## Weitere Informationen 

Der [FEM Arbeitsbereich](FEM_Workbench/de.md) befindet sich in ständiger Entwicklung. Die aktuellsten Informationen findest du im [FreeCAD Forum](http://www.forum.freecadweb.org/).

Wenn du Probleme bei der Installation von Netgen, Gmsh oder CalculiX oder einem anderen externen Werkzeug hast, suche bitte zuerst im Forum:

-   [netgen site:forum.freecadweb.org](https://www.google.ch/search?q=sys.append.path+site%3Aforum.freecadweb.org#q=netgen+site:forum.freecadweb.org)
-   [gmsh site:forum.freecadweb.org](https://www.google.ch/search?q=sys.append.path+site%3Aforum.freecadweb.org#q=gmsh+site:forum.freecadweb.org)
-   [calculix site:forum.freecadweb.org](https://www.google.ch/search?q=sys.append.path+site%3Aforum.freecadweb.org#q=calculix+site:forum.freecadweb.org)


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM Install/de
