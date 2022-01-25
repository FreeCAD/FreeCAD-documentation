# Python 3/de
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

Die Portierung von FreeCAD auf Python 3 ist derzeit im Gange und der Fortschritt wird unter [in diesem Forumsthread](https://forum.freecadweb.org/viewtopic.php?f=10&t=12534) verfolgt. Der Hauptzweig von FreeCAD ist bereits mit python3 nutzbar. Die Tests sind bestanden, aber es gibt immer noch viele kleine Inkompatibilitäten. TESTER GESUCHT!

Dieses Dokument ist ein Platzhalter für die Bauanleitung verschiedener Plattformen und eine Checkliste zur Überwachung der Fortschritte.

## Bau FreeCAD m/ Python 3 

### Ubuntu

Der erste Schritt bei der Erstellung von FreeCAD für Python 3 ist die Sicherstellung, dass Du normal bauen kannst. **Tip**\': Es ist auch hilfreich, ein cmake GUI-Tool wie **cmake-qt-gui** oder **cmake-curses-gui** zu haben.

Die folgenden Anweisungen wurden von einem Beitrag von looo im Python 3 Porting Thread übernommen: Hinweis: Nur getestet mit linux/ubuntu.

Lade den aktuellen Master von FreeCAD herunter.

 git clone [https://github.com/FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD)

Wenn python3 Dein Standard Python ist dann sollte nicht viel zu tun sein. Wenn nicht, dann ist das einfachste zu tun: Setze die python relevanten cmake Variablen mit cmake gui, welche sind:


```python
- PYTHON_EXECUTABLE
- PYTHON_INCLUDE_DIR
- PYTHON_LIBRARY
- PYTHON_BASENAME (=PySideConfigPYTHON_SUFFIX.cmake) -> for me on ubuntu this would be this: .cpython-35m-x86_64-linux-gnu
- PYTHON_SUFFIX (=ShibokenConfigPYTHON_SUFFIX.cmake) -> eg.: .cpython-35m-x86_64-linux-gnu
```

#### Pivy

python3 Builds für freecad sind mit diesem [ppa](https://launchpad.net/~sppedflyer/+archive/ubuntu/mytestppa1) verfügbar


```python
sudo add-apt-repository ppa:sppedflyer/mytestppa1
sudo apt-get update
sudo apt-get install python3-pivy
```

#### PySide

PySide für Python3.5 ist nicht offiziell verfügbar, aber ich denke, ubuntu bietet einen Build.


```python
sudo apt-get install python3-pyside
```

## Test Builds auf Anakonda (linux64) 


```python
wget -c http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
bash Miniconda-latest-Linux-x86_64.sh
```

und folge den Anweisungen

sobald miniconda installiert ist, müssen wir conda konfigurieren, um Zugriff auf die Freecad Builds zu haben:


```python
conda config --add channels conda-forge
conda config --add channels freecad
```

Nun erstellen wir eine neue Umgebung und installieren freecad


```python
conda create --name freecad_py3 python=3.6 freecad
```

dies wird alle notwendigen Pakete herunterladen. Wenn abgeschlossen, aktiviere die Umgebung und starte FreeCAD.


```python
source activate freecad_py3
FreeCAD
```

beim ersten Start von freecad lädt matplotlib einige Module, und deshalb braucht FreeCAD einige Zeit, um zu erscheinen.

### Ersatz Installation 

#### Conda


```python
Install miniconda: http://conda.pydata.org/miniconda.html 
```

Installiere conda-build:


```python
conda install conda_build
```

Füge Kanäle hinzu:


```python
conda config --add channels freecad
conda config --add channels conda-forge
```

Klone den aktuellen Python 3 Port von FreeCAD


```python
git clone https://github.com/looooo/FreeCAD/tree/py3-27
```

Klone die conda Rezepte für FreeCAD


```python
git clone https://github.com/looooo/FreeCAD_Conda
```

\- gehe zu FreeCAD\_Conda/.FreeCAD\_debug

\- Setze die Variablen über dem Skript (den Pfad zu FreeCAD, und wenn Du mit dem Aufruf von cmake bauen willst)


```python
conda build . --python=3.6 --dirty
```

(die schmutzige Flagge ist nicht notwendig, wenn du das erste Mal baust. Wenn sie nicht gesetzt ist, führt conda die ganze Zeit einen vollständigen Build durch. Die Python Option ist nicht notwendig, wenn Du die Miniconda Version python3.6 installiert hast. Aber dann musst Du dieses Flag setzen, um mit python2.7 zu bauen\....)

## Verweise

-   Verfolge die neuesten Entwicklungen bei Pyside:

:\* Fortschrittsberichte: <https://wiki.qt.io/PySide2#Pyside_Development_Progress_Notes>

:\* Git commits: <http://code.qt.io/cgit/pyside/pyside.git/log/>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Administration](Category_Administration.md) > Python 3/de
