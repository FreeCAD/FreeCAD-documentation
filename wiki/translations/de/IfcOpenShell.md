# IfcOpenShell/de
## Beschreibung


{{TOCright}}

[IfcOpenShell](IfcOpenShell/de.md) ist eine Open Source (LGPL 3) Softwarebibliothek , die Entwicklern hilft, mit dem Dateiformat [industry foundation classes](http://www.buildingsmart-tech.org/specifications/ifc-overview) ([IFC](Arch_IFC/de.md)) zu arbeiten. Das IFC Dateiformat kann verwendet werden, um Gebäude und Konstruktionsdaten zu beschreiben. Das Format wird häufig für [Bauwerksdatenmodellierung](https://de.wikipedia.org/wiki/Building_Information_Modeling) (engl.: building information modelling) (BIM) verwendet, z. B. für mechanische Belastungsanalysen und Studien zur thermischen und energetischen Effizienz. IfcOpenShell ist in erster Linie eine Sammlung von C++ Bibliotheken, da es jedoch [Python](Python/de.md) Bindungen besitzt, kann es in Programme wie FreeCAD und Blender integriert werden.

IfcOpenShell verwendet intern [OpenCASCADE](OpenCASCADE/de.md), um die implizite Geometrie in IFC Dateien in explizite Geometrie zu konvertieren, die andere CAD Pakete verstehen können, z. B. STEP, [OBJ](Arch_OBJ/de.md) und [DAE](Arch_DAE/de.md).

Ab v0.19 ist FreeCAD in der Lage, IFC Dateien zu importieren, solange das `ifcopenshell` [Python](Python/de.md) Modul im System verfügbar ist. Ebenso können die [Architektur](Arch_Workbench/de.md) und [BIM Arbeitsbereiche](BIM_Workbench/de.md) ein Gebäudemodell in das IFC Format exportieren, so dass es in anderen Anwendungen verwendet werden kann.

Um zu überprüfen, ob IfcOpenShell in deinem System installiert ist, versuche, sie über die [Python Konsole](Python_console/de.md) zu importieren; die Bibliothek ist korrekt installiert, wenn keine Fehlermeldung zurückgegeben wird.


```python
import ifcopenshell
```

## Installation

IfcOpenShell kann auf verschiedene Arten installiert werden, je nach Betriebssystem und Python Umgebung. In der Vergangenheit war die Installation von IfcOpenShell etwas schwierig, da sie für dein spezifisches System kompiliert werden musste; seit diesem Beitrag (2020) ist es jedoch einfacher, sie zu verwenden, da sie nun zusammen mit FreeCAD in vielen FreeCAD Distributionen enthalten ist. Im Allgemeinen ist es ratsam, eine dieser vorkompilierten Distributionen zu verwenden und es nur selbst zu kompilieren, wenn du ein fortgeschrittener Benutzer bist.

### Pip

The easiest way to install IfcOpenShell is using [pip](https://pypi.org/project/pip/). Once pip is installed on your system, you can [install](https://datatofish.com/install-package-python-using-pip/) IfcOpenShell easily by issuing from a terminal window:


```python
pip install ifcopenshell
```

### Conda

Für Windows und MacOS Systeme enthalten FreeCAD Distributionen, die mit dem Paketmanager [Conda](Conda/de.md) zusammengestellt wurden, in der Regel bereits IfcOpenShell, so dass keine weitere Installation erforderlich ist. Hol dir die entsprechende Distribution von der [Herunterladen](Download/de.md) Seite.

Das [AppImage](AppImage/de.md) für Linux basiert ebenfalls auf [Conda](Conda/de.md) und beinhaltet auch IfcOpenShell.

### Linux

Wenn es verfügbar ist, kannst du IfcOpenShell über den Paketmanager deiner Distribution installieren.


```python
sudo apt install ifcopenshell
```

Beachte jedoch, dass Pakete, die von vielen Linux Repositorien bereitgestellt werden, dazu neigen, alt zu sein, und möglicherweise nicht die neuesten Entwicklungen der Software enthalten. Wenn du sicher sein willst, dass du die neueste Software verwendest, verwende eine [Conda](Conda/de.md) basierte Distribution von FreeCAD, eine vorkompilierte IfcOpenShell Distribution oder kompiliere IfcOpenShell selbst.

### Verwendung eines vorkompilierten IfcOpenShell Pakets 

Es gibt ein spezielles Repositorium des IfcOpenShell Projekts, das regelmäßig die IfcOpenShell Bibliotheken für verschiedene Systeme (Linux, Windows, MacOS), Architekturen (32-bit und 64-bit) und Python Versionen (2.7, 3.x) kompiliert. Um diese vorkompilierten Bibliotheken zu verwenden, musst du die richtige Version auswählen, die zu deinem Betriebssystem, deiner Architektur und den Haupt- und Nebenziffern für das [Python](Python/de.md), das mit FreeCAD verwendet wird, passt. Das bedeutet, dass die ersten beiden Nummern übereinstimmen müssen (Python 3.6 und 3.7 werden als unterschiedliche Versionen angesehen), während die dritte Nummer (micro) keine Rolle spielt (Python 3.6.5 und 3.6.12 werden aus Kompatibilitätsgründen als gleich angesehen).

1.  Begib dich in das Bau Repositorium [IfcOpenBot/IfcOpenShell](https://github.com/IfcOpenBot/IfcOpenShell). Dieses Repositorium ist nicht für die Entwicklung gedacht, es enthält nur eine Kopie des Hauptrepositorys sowie vorkompilierte Pakete.
2.  Zum Zeitpunkt dieses Beitrags (2020) enthält der Hauptzweig des IfcOpenShell Projekts nicht den neuesten Code, daher müssen wir den gewünschten Zweig auswählen, zum Beispiel `v0.6.0`.
3.  Klicke auf die Commit Nummer, wodurch du zur Liste der Commits für den Zweig gelangst, z. B. `IfcOpenBot/IfcOpenShell/commits/v0.6.0`.
4.  Gehe in der Historie zurück, bis du einen Commit findest, der einen Kommentar hat. Dies zeigt den Zeitpunkt an, an dem die vorkompilierten Bibliotheken freigegeben wurden.
5.  Klicke auf den Commit. Du wirst einen Kommentar von IfcOpenBot sehen, der eine Tabelle mit Kombinationen von Betriebssystem, Architektur und Python Version zeigt. Wähle den richtigen Verweis für \"Python\", der zu deiner [Version von FreeCAD](Std_About/de.md) passt. Die Pakete \"Blender\", \"IfcConvert\" und \"IfcGeomServer\" werden für die Verwendung von FreeCAD nicht benötigt.
6.  Das heruntergeladene Paket muss extrahiert werden, und das extrahierte Verzeichnis muss in den Python Suchpfad gelegt werden, um die neuen Module zu finden.


**Hinweis:**

Die folgenden Beispiele gehen von einem Debian/Ubuntu basierten System aus, aber die allgemeine Vorgehensweise sollte auch für andere Betriebssysteme funktionieren.

-   Entpacken des heruntergeladenen Pakets erzeugt einen Ordner `ifcopenshell/`.


```python
unzip ifcopenshell-python-36-v0.6.0-4baec57-linux64.zip
```

-   Der Suchpfad kann durch die Untersuchung der Variable `sys.path` in der [Python Konsole](Python_console/de.md) ermittelt werden.


```python
import sys
print(sys.path)
```

Wenn du die IfcOpenShell Bibliothek nur für deinen Benutzer installierst und keine Auswirkungen auf Systemverzeichnisse haben möchtest, solltest du den extrahierten Ordner `ifcopenshell/` in das Home Verzeichnis deines eigenen Anwenders legen. 
```python
mv -t $HOME/.local/lib/python3.6/site-packages/ ifcopenshell/
```

Wenn du die IfcOpenShell Bibliothek systemweit installieren möchtest, benötigst du normalerweise Superuser Rechte, um in Systemverzeichnisse zu schreiben; dies ist normalerweise ein `site-packages/` Verzeichnis oder ein `dist-packages/` Verzeichnis für Debian/Ubuntu Distributionen. 
```python
sudo mv -t /usr/local/lib/python3.6/dist-packages/ ifcopenshell/
```

Wenn das Verzeichnis korrekt verschoben wurde, teste ob das Modul `ifcopenshell` von der [Python Konsole](Python_console/de.md) aus zugänglich ist. 
```python
>>> import ifcopenshell
>>> print(ifcopenshell.version)
0.6.0b0
>>> print(ifcopenshell.__path__)
['/home/user/.local/lib/python3.6/site-packages/ifcopenshell']
```

Um die installierte Bibliothek zu entfernen, lösche einfach das entsprechende Verzeichnis mit allen darin enthaltenen Modulen. 
```python
rm -rf $HOME/.local/lib/python3.6/site-packages/ifcopenshell/
sudo rm -rf /usr/local/lib/python3.6/dist-packages/ifcopenshell/
```

## Kompilieren

Das Kompilieren von IfcOpenShell wird nur für fortgeschrittene Benutzer empfohlen. Der Prozess ähnelt dem [Kompilieren von FreeCAD unter Linux](Compile_on_Linux/de.md), wenn du dies bereits gemacht hast, verfügst du möglicherweise bereits über die notwendigen Voraussetzungen wie die [OpenCASCADE\'s](OpenCASCADE/de.md) Entwicklungsdateien. Der Prozess verwendet das CMake Konfigurationswerkzeug, um eine benutzerdefinierte `Makefile` für die Verwendung mit dem Make Werkzeug zu erzeugen.

Die allgemeinen Anweisungen sind im [IfcOpenShell-Repository](https://github.com/IfcOpenShell/IfcOpenShell) umrissen und lauten wie folgt:

1.  Hol dir den Quellcode von IfcOpenShell aus seinem Hauptrepository.
2.  Sammle alle Abhängigkeiten für die Kompilierung, einschließlich eines C++ Kompilierers, CMake und Make, sowie die Entwicklungsdateien für Boost, libxml2, [OpenCASCADE](OpenCASCADE/de.md), SWIG, Python und OpenCOLLADA (optional). Die meisten dieser Komponenten sind rein optional, für die Verwendung mit FreeCAD sollten sie jedoch alle installiert sein. OpenCOLLADA ist optional, da es nur [DAE](Arch_DAE/de.md) Unterstützung für das `IfcConvert` Binärformat bietet.
3.  Führe `cmake` aus, um eine `Makefile` zu erzeugen, und starte dann die Kompilierung durch Ausführen von `make`.
4.  Installiere das `ifcopenshell` [Python](Python/de.md) Modul in das entsprechende `site-packages/` Verzeichnis, damit es von FreeCAD gefunden wird.


**Hinweis:**

Die folgenden Beispiele gehen von einem Debian/Ubuntu basierten System aus, aber die allgemeine Vorgehensweise sollte auch für andere Betriebssysteme funktionieren. Zum Beispiel befinden sich unter Debian gemeinsam genutzte Bibliotheken normalerweise in `/usr/lib/x86_64-linux-gnu/`, während dies bei anderen Distributionen `/usr/lib64/` sein kann, so dass die Pfade entsprechend angepasst werden sollten.

### Voraussetzungen

Installiere die grundlegenden Kompilierwerkzeuge. 
```python
sudo apt install git cmake gcc g++ libboost-all-dev
```

Hol dir den Quellcode des Projekts und leg ihn in einem eigenen Verzeichnis ab, auf das du vollen Schreibzugriff hast.

Zum Zeitpunkt dieses Schreibens (2020) enthält der Hauptzweig des IfcOpenShell Projekts nicht den neuesten Code, sodass wir einen bestimmten Zweig klonen müssen. 
```python
git clone https://github.com/IfcOpenShell/IfcOpenShell -b v0.6.0 IfcOpenShell-source
```

### OpenCASCADE

Installiere die Entwicklungsdateien von [OpenCASCADE](OpenCASCADE/de.md). 
```python
sudo apt install libocct*-dev
```

Das erweitert sich auf 
```python
sudo apt install libocct-data-exchange-dev libocct-draw-dev libocct-foundation-dev libocct-modeling-algorithms-dev libocct-modeling-data-dev libocct-ocaf-dev libocct-visualization-dev
```

Du kannst auch die Gemeinschaftsedition (OCE) von OpenCASCADE verwenden, beachte aber bitte, dass diese Version veraltet ist und ab 2020 nicht mehr von FreeCAD empfohlen wird.

### OpenCOLLADA

Installiere die Entwicklungsdateien von OpenCOLLADA. 
```python
sudo apt install opencollada-dev
```

Wenn die Dateien in deiner Distribution zu alt sind, kannst du die Bibliotheken auch selbst kompilieren. Die Vorgehensweise ist im Haupt Repositorium, [KhronosGroup/OpenCOLLADA](https://github.com/KhronosGroup/OpenCOLLADA), beschrieben und ist sehr einfach, da nur die Entwicklungsdateien `libpcre3` und `libxml2` benötigt werden.


```python
sudo apt install libpcre3-dev libxml2-dev
git clone https://github.com/KhronosGroup/OpenCOLLADA OpenCOLLADA-source

mkdir -p OpenCOLLADA-build
cd OpenCOLLADA-build
cmake ../OpenCOLLADA-source

make -j 3
sudo make install
```

### Python Umverpackung 

Für die Verwendung mit FreeCAD benötigst du den [Python](Python/de.md) Umverpacker, der SWIG verwendet, um die richtigen Schnittstellen aus den C++-Klassen zu generieren.


```python
sudo apt-get install python-all-dev swig
```

### CMake Konfiguration 

Es wird empfohlen, die Konfiguration und Kompilierung in einem speziellen Bau Verzeichnis getrennt vom Quellverzeichnis durchzuführen.


```python
mkdir -p IfcOpenShell-build
cd IfcOpenShell-build

cmake ../IfcOpenShell-source/cmake/
```

Beachte, dass sich die Datei `CMakeLists.txt`, die CMake steuert, im Unterverzeichnis `cmake/` im Quellverzeichnis befindet.

Abhängig von deiner Linux Distribution und dem Weg, wie du die Abhängigkeiten installiert hast, musst du eventuell einige CMake Variablen definieren, damit die Bibliotheken richtig gefunden werden.

#### Angabe der OpenCASCADE Bibliotheken 

Wenn du OpenCASCADE manuell kompiliert hast, oder wenn die Bibliotheken nicht in einem Standardverzeichnis liegen, musst du eventuell die richtigen Variablen setzen.


```python
cmake \
    -DOCC_INCLUDE_DIR=/usr/include/opencascade \
    -DOCC_LIBRARY_DIR=/usr/lib/x86_64-linux-gnu \
    ../IfcOpenShell-source/cmake/
```

Standardmäßig erwartet das Bau System die Gemeinschaftsedition (OCE) von OpenCASCADE (`/usr/include/oce/`), beachte aber bitte, dass diese Version veraltet ist und ab 2020 von FreeCAD nicht mehr empfohlen wird. Aus diesem Grund wird die Installation der Entwicklungsdateien der Hauptversion von [OpenCASCADE](OpenCASCADE/de.md) (OCCT) empfohlen.

#### Ohne OpenCOLLADA 

Wenn du keine OpenCOLLADA Unterstützung benötigst ([DAE](Arch_DAE/de.md) Dateien), musst du sie explizit mit der Variable `COLLADA_SUPPORT` abschalten.


```python
cmake \
    ...
    -DCOLLADA_SUPPORT=FALSE \
    ../IfcOpenShell-source/cmake/
```

#### Mit OpenCOLLADA 

Wenn du OpenCOLLADA manuell kompiliert hast oder wenn sich die Bibliotheken nicht in einem Standardverzeichnis befinden, musst du möglicherweise die richtigen Variablen für OpenCOLLADA und für die Bibliothek `libpcre` setzen.


```python
cmake \
    ...
    -DOPENCOLLADA_INCLUDE_DIR=/usr/include/opencollada \
    -DOPENCOLLADA_LIBRARY_DIR=/usr/lib/opencollada \
    -DPCRE_LIBRARY_DIR=/usr/lib/x86_64-linux-gnu \
    ../IfcOpenShell-source/cmake/
```

#### Angeben der libxml2 Bibliotheken 

Wenn die `libxml2` Bibliotheken beim Kompilieren und Verweisen nicht gefunden werden oder wenn sich die Bibliotheken nicht in einem Standardverzeichnis befinden, musst du eventuell die entsprechenden Variablen setzen.


```python
cmake \
    ...
    -DLIBXML2_INCLUDE_DIR=/usr/include/libxml2 \
    -DLIBXML2_LIBRARIES=/usr/lib/x86_64-linux-gnu/libxml2.so \
    ../IfcOpenShell-source/cmake/
```

#### Angeben der Installation im Home Verzeichnis des Anwenders 

Standardmäßig wird das Python Modul `ifcopenshell` in einem Systemverzeichnis `site-packages/` installiert, sodass es Superuser Rechte benötigt. Durch Setzen der Variable `USERSPACE_PYTHON_PREFIX` wird die Installation des Python Moduls in das Heimatverzeichnis des Benutzers vorgenommen.


```python
cmake \
    ...
    -DUSERSPACE_PYTHON_PREFIX=ON \
    ../IfcOpenShell-source/cmake/
```

#### Angabe der Python Version 

Wenn du eine Bindung für eine bestimmte Python Version erzeugen möchtest, setze die Variable `PYTHON_EXECUTABLE` auf die spezifische ausführbare Version. Denke daran, dass diese Version die gleiche Python Version sein muss, gegen die FreeCAD kompiliert wurde. 
```python
cmake \
    ...
    -DPYTHON_EXECUTABLE=/usr/bin/python3.6 \
    ../IfcOpenShell-source/cmake/
```

#### Einzelne Konfigurationszeile 

In einem typischen Debian/Ubuntu System kannst du diese Zeile verwenden, um die Kompilierung zu konfigurieren. Passe sie nach Bedarf an. 
```python
cmake -DOCC_INCLUDE_DIR=/usr/include/opencascade -DOCC_LIBRARY_DIR=/usr/lib/x86_64-linux-gnu -DLIBXML2_INCLUDE_DIR=/usr/include/libxml2 -DLIBXML2_LIBRARIES=/usr/lib/x86_64-linux-gnu/libxml2.so -DUSERSPACE_PYTHON_PREFIX=ON ../IfcOpenShell-source/cmake/
```

Ohne OpenCOLLADA: 
```python
cmake -DOCC_INCLUDE_DIR=/usr/include/opencascade -DOCC_LIBRARY_DIR=/usr/lib/x86_64-linux-gnu -DCOLLADA_SUPPORT=FALSE -DLIBXML2_INCLUDE_DIR=/usr/include/libxml2 -DLIBXML2_LIBRARIES=/usr/lib/x86_64-linux-gnu/libxml2.so -DUSERSPACE_PYTHON_PREFIX=ON ../IfcOpenShell-source/cmake/
```

### Aktuelle Kompilierung 

Wenn es bei der Konfiguration mit CMake keine Fehlermeldungen gab, sollte eine `Makefile` im Bauverzeichnis erstellt worden sein, so dass du mit der Kompilierung der Bibliotheken durch Ausführen von `make` fortfahren kannst. 
```python
make -j N
```


`N`

ist die Anzahl der Prozessoren, die du dem Kompilierungsprozess zuweist; wähle mindestens einen weniger als die Gesamtzahl der CPU Kerne, die du hast.

### Fehlersuche und weitere Optionen 

Alle Konfigurationsoptionen sind in der Datei `CMakeLists.txt` verfügbar, die sich im Verzeichnis `IfcOpenShell-source/cmake/` befindet. Wenn beim Ausführen von CMake oder Make Probleme auftreten, suche hier nach weiteren Optionen, die möglicherweise gesetzt werden müssen.

In allen obigen Anweisungen kann anstelle von `cmake` die grafische Oberfläche `cmake-gui` verwendet werden. Dadurch werden die verfügbaren Optionen in der Konfiguration schnell angezeigt.


```python
cmake-gui ../IfcOpenShell-source/cmake/
```

### Testen der Kompilierung im Bau Verzeichnis 

Wenn der Bau erfolgreich war, solltest du ein Unterverzeichnis `examples/` mit der neu kompilierten ausführbaren Datei `IfcOpenHouse` haben. Führe dieses Dienstprogramm aus dem Bau Verzeichnis aus, um eine Beispiel IFC Datei zu erzeugen. 
```python
example/IfcOpenHouse
```

Die [IFC](Arch_IFC/de.md) Beispieldatei sollte im Bau Verzeichnis erscheinen und kann als Eingabe für die ebenfalls neu kompilierte ausführbare Datei `IfcConvert` verwendet werden. Dieses Hilfsprogramm nimmt als Eingabe eine IFC Datei und erzeugt als Ausgabe ein anderes Format, einschließlich [OBJ](Arch_OBJ/de.md), [DAE](Arch_DAE/de.md), wenn die OpenCOLLADA Unterstützung aktiviert wurde, STEP, IGS, XML, [SVG](Draft_SVG/de.md), oder ein anderes [IFC](Arch_IFC/de.md). 
```python
./IfcConvert IfcOpenHouse.ifc
```

Wenn keine Ausgabedatei angegeben wird, wird standardmäßig eine [OBJ](Arch_OBJ/de.md) Datei und die dazugehörige Materialtabelle (MTL) erstellt.

### Installation der kompilierten Bibliotheken 

Wenn die Kompilierung keine Fehler meldet, kannst du `make install` ausführen, um die Header, kompilierten Bibliotheken und Binärdateien in ihre entsprechenden Installationsverzeichnisse zu kopieren.


```python
sudo make install
```

Standardmäßig ist der `CMAKE_INSTALL_PREFIX` `/usr/local/`, so dass alle kompilierten Dateien unter diesem Verzeichnis abgelegt werden, was normalerweise erhöhte Rechte erfordert. 
```python
/usr/local/bin/IfcConvert
/usr/local/bin/IfcGeomServer
/usr/local/include/ifcparse/*.h
/usr/local/include/ifcgeom/*.h
/usr/local/include/ifcgeom_schema_agnostic/*.h
/usr/local/include/serializers/{*.h,*.cpp}
/usr/local/include/serializers/schema_dependent/{*.h,*.cpp}
/usr/local/lib/libIfcGeom*.a
/usr/local/lib/libIfcParse.a
/usr/local/lib/libSerializers*.a
```

Das `ifcopenshell` Python Modul, das für FreeCAD benötigt wird, ist nicht tatsächlich im Erstellungsverzeichnis vorhanden; dieses Paket wird nur erstellt, wenn `make install` ausgeführt wird. Das resultierende Paket wird in einem `site-packages/` Verzeichnis oder einem `dist-packages/` Verzeichnis für Debian/Ubuntu-Distributionen abgelegt. 
```python
/usr/lib/python3/dist-packages/ifcopenshell/
```

Wenn die Variable `USERSPACE_PYTHON_PREFIX` während des CMake-Konfigurationsschritts gesetzt wurde, wird `ifcopenshell` im Verzeichnis `site-packages/` des Benutzers abgelegt. 
```python
$HOME/.local/lib/python3.6/site-packages/ifcopenshell/
```

### Entfernen der kompilierten Bibliotheken 

Um die installierten Bibliotheken zu entfernen, entferne einfach die entsprechenden Dateien, die installiert wurden, und das Verzeichnis `ifcopenshell/` mit allen Modulen darin. 
```python
sudo rm -rf /usr/local/bin/IfcConvert
sudo rm -rf /usr/local/bin/IfcGeomServer
sudo rm -rf /usr/local/include/ifcparse/
sudo rm -rf /usr/local/include/ifcgeom/
sudo rm -rf /usr/local/include/ifcgeom_schema_agnostic/
sudo rm -rf /usr/local/lib/libIfcGeom*
sudo rm -rf /usr/local/lib/libIfcParse*
sudo rm -rf /usr/local/lib/libSerializers*
```


```python
sudo rm -rf /usr/lib/python3/dist-packages/ifcopenshell/
```

Oder wenn die Variable `USERSPACE_PYTHON_PREFIX` gesetzt wurde. 
```python
sudo rm -rf $HOME/.local/lib/python3.6/site-packages/ifcopenshell/
```

### Manuelle Installation 

Die Kompilierung der gesamten IfcOpenShell Distribution erzeugt Binärdateien wie `IfcConvert` und `IfcGeomServer`, sowie viele statische Bibliotheken (`lib*.a`) im Bau Verzeichnis. Für FreeCAD benötigen wir jedoch nur das `ifcopenshell` Python Modul. Dieses Modul ist keine einzelne Datei, sondern ein \"Paket\", also ein Verzeichnis mit verschiedenen Dateien. Dieses `ifcopenshell` Paket wird aus den Python Wrappern, die innerhalb von `IfcOpenShell-build/ifcwrap/` gebaut wurden, und aus den Python Modulen im ursprünglichen Quellverzeichnis `IfcOpenShell-source/src/ifcopenshell-python/ifcopenshell/` zusammengesetzt.

-   Erzeugt durch den Kompiliervorgang:


```python
../IfcOpenShell-build/ifcwrap/ifcopenshell_wrapper.py
../IfcOpenShell-build/ifcwrap/_ifcopenshell_wrapper.so
```

-   Vorhanden im Quellverzeichnis:


```python
../IfcOpenShell-source/src/ifcopenshell-python/ifcopenshell/
```

Das `ifcopenshell` Modul wird erstellt, indem das ursprüngliche Quellverzeichnis kopiert wird und die beiden Dateien `*ifcopenshell_wrapper*` hinzugefügt werden.


```python
cp -rt . ../IfcOpenShell-source/src/ifcopenshell-python/ifcopenshell/
cp -t ifcopenshell/ ifcwrap/ifcopenshell_wrapper.py ifcwrap/_ifcopenshell_wrapper.so
```

Nun kann dieses Verzeichnis in das benutzerspezifische oder Systemverzeichnis `site-packages/` verschoben werden. (`dist-packages/` für Debian/Ubuntu) verschoben werden, um es für alle Python Anwendungen verfügbar zu machen. 
```python
mv -t $HOME/.local/lib/python3.6/site-packages/ ifcopenshell/
```

-   Vorhanden im Quellverzeichnis:


```python
sudo mv -t /usr/lib/python3/dist-packages/ ifcopenshell/
```

Jetzt sollte das Modul `ifcopenshell` verfügbar sein, um von einer [Python Konsole](Python_console/de.md) importiert zu werden. 
```python
>>> import ifcopenshell
>>> print(ifcopenshell.version)
0.6.0b0
>>> print(ifcopenshell.__path__)
['/home/user/.local/lib/python3.6/site-packages/ifcopenshell']
```

## IFC Betrachter Anwendung 

Die IfcOpenShell Bibliothek enthält tatsächlich einen kleinen grafischen Betrachter für IFC Dateien, der PyQt5 und PythonOCC verwendet.

Um diesen Betrachter von der Python Konsole aus zu starten, muss die Klasse `application` instanziiert und gestartet werden: 
```python
from ifcopenshell.geom.app import application
application().start()
```

Wenn die Bibliothek bereits installiert ist, kann das gesamte Modul auch über das Terminal ausgeführt werden: 
```python
python3 /home/user/.local/lib/python3.6/site-packages/ifcopenshell/geom/app.py
```

Zum Zeitpunkt der Erstellung dieses Artikels (2020) wurde nur die für die [OpenCASCADE](OpenCASCADE/de.md) Gemeinschaftsausgabe (OCE) kompilierte [PythonOCC](PythonOCC/de.md) Version unterstützt.

## IFC Online Betrachter 

Das IfcOpenShell Projekt hat auch \"IFC Pipeline\" entwickelt, ein selbstgehostetes IFC Verarbeitungs- und Visualisierungsprogramm. Es bietet auch eine kleine Webanwendung, die Datei Uploads akzeptiert, die jeder verwenden kann. Das bedeutet, dass du zur Visualisierung von IFC Daten weder IfcOpenShell noch andere Viewer lokal installiert haben musst; Du kannst einfach deine IFC Datei in dieses System laden und das Ergebnis sehen.

-   Online Betrachter: <https://view.ifcopenshell.org/>
-   Repositorium: [AECgeeks/ifc-pipeline](https://github.com/AECgeeks/ifc-pipeline)

## Weitere Informationen 

-   Webseite: [ifcopenshell.org](http://ifcopenshell.org/)
-   Code Repositorium: [IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell)
-   Akademie mit Beispielen und Artikeln: [academy.ifcopenshell.org](http://academy.ifcopenshell.org/)
-   [IfcOpenShell online Betrachter](https://view.ifcopenshell.org/)
-   OSArch Gemeinschaft mit Ressourcen für Open Source Architektur: [wiki.OSArch.org](https://wiki.osarch.org/index.php?title=Main_Page)
-   [Installation von IfcOpenShell](https://forum.freecadweb.org/viewtopic.php?f=39&t=48971); Hauptdiskussion im Forum.
-   [IFC Installation](https://forum.freecadweb.org/viewtopic.php?f=39&t=12368&start=10#p117883); alte Diskussion im Forum.
-   [IfcPlusPlus kompiliert auf Gentoo - Fragen und Alternativen?](https://forum.freecadweb.org/viewtopic.php?f=39&t=33254)
-   [Compiling IfcOpenShell for MacOS](Import/Export_IFC_-_compiling_IfcOpenShell.md); eine ältere Anleitung, die den allgemeinen Prozess beschreibt. Sie wird möglicherweise nicht mehr benötigt, da IfcOpenShell jetzt dank [Conda](Conda/de.md) zusammen mit FreeCAD verteilt wird.
-   Welche Seiten verlinken auf [diese Seite](Special:WhatLinksHere/IfcOpenShell/de.md).


 {{FEM Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [BIM](Category_BIM.md) > [3rd Party](Category_3rd Party.md) > [Arch](Category_Arch.md) > [FEM](Category_FEM.md) > IfcOpenShell/de
