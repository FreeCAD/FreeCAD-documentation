# Extra python modules/de
{{TOCright}}

## Überblick

Diese Seite listet verschiedene zusätzliche Python Module oder andere Softwarestücke auf, die kostenlos aus dem Internet heruntergeladen werden können und die deiner FreeCAD Installation Funktionalität hinzufügen.

## PySide (vorher PyQt4) 

-   Homepage (PySide): (http://qt-project.org/wiki/PySide <http://qt-project.org/wiki/PySide> <http://qt-project.org/wiki/PySide>)
-   Lizenz: LGPL
-   optional, wird aber von mehreren Modulen benötigt: Entwurf, Bogen, Schiff, Druck, OpenSCAD, Kalkulationsblatt

PySide (früher PyQt) wird von mehreren Modulen von FreeCAD benötigt, um auf die Qt-Schnittstelle von FreeCAD zuzugreifen. Es ist bereits in der Windows-Version von FreeCAD enthalten und wird in der Regel automatisch von FreeCAD unter Linux installiert, wenn es aus offiziellen Repositories installiert wird. Wenn diese Module (Draft, Arch, etc.) nach der Installation von FreeCAD aktiviert werden, bedeutet das, dass PySide (früher PyQt) bereits vorhanden ist und nichts mehr getan werden muss.

**Hinweis:** FreeCAD hat sich nach und nach von PyQt ab Version 0.13 zu Gunsten von [PySide](http://qt-project.org/wiki/PySide) entfernt, das genau den gleichen Job macht, aber eine (LGPL) Lizenz hat, die besser mit FreeCAD kompatibel ist.

## Installation

#### Linux

Der einfachste Weg, PySide zu installieren, ist über den Paketmanager Ihrer Distribution. Auf Debian/Ubuntu-Systemen lautet der Paketname im Allgemeinen *python-PySide*, während er auf RPM-basierten Systemen *pyside* genannt wird. Die notwendigen Abhängigkeiten (Qt und SIP) werden automatisch erledigt.

#### Windows

Das Programm kann unter <http://qt-project.org/wiki/Category:LanguageBindings>::PySide::Downloads heruntergeladen werden. Du must die Qt- und SIP-Bibliotheken installieren, bevor Du PySide installieren kannst (zu dokumentieren).

#### MacOSX

PyQt auf Mac kann über Homebrew oder Port installiert werden. Weitere Informationen findet man unter [Install dependencies](Compile_on_MacOS#Install_Dependencies.md).

### Verwendung

Sobald es installiert ist, kann überprüft werden, ob alles funktioniert, indem in die FreeCAD Python-Konsole eingegeben wird:


```python
import PySide
```

Um auf die FreeCAD-Schnittstelle zuzugreifen, gib ein :


```python
from PySide import QtCore,QtGui
FreeCADWindow = FreeCADGui.getMainWindow()
```

Nun kann mit dem Befehl dir() begonnen werden, die Oberfläche zu erkunden. Neue Elemente können ergänzt werden, wie ein benutzerdefiniertes Widget, mit Befehlen wie :


```python
FreeCADWindow.addDockWidget(QtCore.Qt.RghtDockWidgetArea,my_custom_widget)
```

Arbeiten mit Unicode :


```python
text = text.encode('utf-8')
```

Arbeiten mit QFileDialog und OpenFileName :


```python
path = FreeCAD.ConfigGet("AppHomePath")
#path = FreeCAD.ConfigGet("UserAppData")
OpenName, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Read a txt file", path, "*.txt")
```

Arbeiten mit QFileDialog und SaveFileName :


```python
path = FreeCAD.ConfigGet("AppHomePath")
#path = FreeCAD.ConfigGet("UserAppData")
SaveName, Filter = PySide.QtGui.QFileDialog.getSaveFileName(None, "Save a file txt", path, "*.txt")
```

### Beispiel für den Übergang von PyQt4 und PySide 

PS: diese Beispiele von Fehlern wurden beim Übergang von PyQt4 zu PySide gefunden und diese Korrekturen wurden vorgenommen, andere Lösungen sind sicherlich mit den obigen Beispielen verfügbar


```python
try:
    import PyQt4                                        # PyQt4
    from PyQt4 import QtGui ,QtCore                     # PyQt4
    from PyQt4.QtGui import QComboBox                   # PyQt4
    from PyQt4.QtGui import QMessageBox                 # PyQt4
    from PyQt4.QtGui import QTableWidget, QApplication  # PyQt4
    from PyQt4.QtGui import *                           # PyQt4
    from PyQt4.QtCore import *                          # PyQt4
except Exception:
    import PySide                                       # PySide
    from PySide import QtGui ,QtCore                    # PySide
    from PySide.QtGui import QComboBox                  # PySide
    from PySide.QtGui import QMessageBox                # PySide
    from PySide.QtGui import QTableWidget, QApplication # PySide
    from PySide.QtGui import *                          # PySide
    from PySide.QtCore import *                         # PySide
```

Um auf die FreeCAD Oberfläche zuzugreifen, gib ein : Du kannst neue Elemente hinzufügen, wie ein benutzerdefiniertes Widget, mit Befehlen wie :


```python
myNewFreeCADWidget = QtGui.QDockWidget()          # create a new dockwidget
myNewFreeCADWidget.ui = Ui_MainWindow()           # myWidget_Ui()             # load the Ui script
myNewFreeCADWidget.ui.setupUi(myNewFreeCADWidget) # setup the ui
try:
    app = QtGui.qApp                              # PyQt4 # the active qt window, = the freecad window since we are inside it
    FCmw = app.activeWindow()                     # PyQt4 # the active qt window, = the freecad window since we are inside it
    FCmw.addDockWidget(QtCore.Qt.RightDockWidgetArea,myNewFreeCADWidget) # add the widget to the main window
except Exception:
    FCmw = FreeCADGui.getMainWindow()             # PySide # the active qt window, = the freecad window since we are inside it 
    FCmw.addDockWidget(QtCore.Qt.RightDockWidgetArea,myNewFreeCADWidget) # add the widget to the main window
```

Arbeiten mit Unicode :


```python
try:
    text = unicode(text, 'ISO-8859-1').encode('UTF-8')  # PyQt4
except Exception:
    text = text.encode('utf-8')                         # PySide
```

Arbeiten mit QFileDialog und OpenFileName :


```python
OpenName = ""
try:
    OpenName = QFileDialog.getOpenFileName(None,QString.fromLocal8Bit("Lire un fichier FCInfo ou txt"),path,"*.FCInfo *.txt") # PyQt4
except Exception:
    OpenName, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Lire un fichier FCInfo ou txt", path, "*.FCInfo *.txt")#PySide
```

Arbeiten mit QFileDialog und SaveFileName :


```python
SaveName = ""
try:
    SaveName = QFileDialog.getSaveFileName(None,QString.fromLocal8Bit("Sauver un fichier FCInfo"),path,"*.FCInfo") # PyQt4
except Exception:
    SaveName, Filter = PySide.QtGui.QFileDialog.getSaveFileName(None, "Sauver un fichier FCInfo", path, "*.FCInfo")# PySide
```

Die MitteilungsBox:


```python
def errorDialog(msg):
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Critical,u"Error Message",msg )
    try:
        diag.setWindowFlags(PyQt4.QtCore.Qt.WindowStaysOnTopHint) # PyQt4 # this function sets the window before
    except Exception:    
        diag.setWindowFlags(PySide.QtCore.Qt.WindowStaysOnTopHint)# PySide # this function sets the window before
#    diag.setWindowModality(QtCore.Qt.ApplicationModal)       # function has been disabled to promote "WindowStaysOnTopHint"
    diag.exec_()
```

Arbeiten mit setProperty (PyQt4) und setValue (PySide)


```python
self.doubleSpinBox.setProperty("value", 10.0)  # PyQt4
```

ersetzen durch :


```python
self.doubleSpinBox.setValue(10.0)  # PySide
```

Arbeiten mit setToolTip


```python
self.doubleSpinBox.setToolTip(_translate("MainWindow", "Coordinate placement Axis Y", None))  # PyQt4
```

ersetzen durch :


```python
self.doubleSpinBox.setToolTip(_fromUtf8("Coordinate placement Axis Y"))  # PySide 
```

oder:


```python
self.doubleSpinBox.setToolTip(u"Coordinate placement Axis Y.")# PySide
```

### Zusätzliche Dokumentation 

Einige pyQt4-Tutorien (einschließlich der Erstellung von Schnittstellen mit Qt Designer zur Verwendung mit Python):

-   <http://pyqt.sourceforge.net/Docs/PyQt4/classes.html> - die PyQt4 API Referenz auf sourceforge
-   <http://www.rkblog.rk.edu.pl/w/p/introduction-pyqt4/> - eine einfache Einführung
-   <http://www.zetcode.com/tutorials/pyqt4/> - sehr komplettes, ausführliches Tutorial

## Pivy

-   Startseite: [<https://bitbucket.org/Coin3D/coin/wiki/Home>](https://bitbucket.org/Coin3D/coin/wiki/Home)
-   Lizenz: BSD
-   optional, aber von verschiedenen Modulen von FreeCAD benötigt: Entwurf, Bogen

Pivy wird von mehreren Modulen benötigt, um die 3D Ansicht von FreeCAD zu erreichen. Unter Windows ist Pivy bereits im FreeCAD Installationsprogramm enthalten, unter Linux wird es normalerweise automatisch installiert, wenn Du FreeCAD aus einem offiziellen Repository installierst. Unter MacOSX musst Du Pivy leider selbst kompilieren.

### Installation 

#### Voraussetzungen

Ich glaube, bevor Du Pivy kompilierst, solltest Du Coin und SoQt installiert haben.

Ich fand, dass es zum Bauen auf Mac ausreicht, das [Coin3-Binärpaket](http://www.coin3d.org/lib/plonesoftwarecenter_view) zu installieren. Der Versuch, Coin von MacPorts aus zu installieren, war problematisch: versuchte, eine Menge X Windowspakete hinzuzufügen und stürzte schließlich mit einem Skriptfehler ab.

Für Fedora habe ich eine RPM mit Coin3 gefunden.

SoQt kompiliert von [source](http://www.coin3d.org/lib/soqt/releases/1.5.0) gut auf Mac und Linux.

##### Debian & Ubuntu 

Beginnend mit Debian Squeeze und Ubuntu Lucid, wird pivy direkt aus den offiziellen Repositorien verfügbar sein, was uns eine Menge Ärger erspart. In der Zwischenzeit kannst Du entweder eines der Pakete, die wir (für debian und ubuntu karmic) auf den [Download](Download.md) Seiten zur Verfügung gestellt haben, herunterladen oder selbst kompilieren.

Der beste Weg, pivy einfach zu kompilieren, ist, das Debian-Quellpaket für pivy zu holen und ein Paket mit debuild zu erstellen. Es ist derselbe Quellcode von der offiziellen Pivy Seite, aber die Debian Leute haben einige fehlerbereinigende Ergänzungen vorgenommen. Es lässt sich auch gut mit ubuntu karmic kompilieren: <http://packages.debian.org/squeeze/python-pivy> lade die .orig.gz und die .diff.gz Datei herunter, entpacke dann beide und wende dann den . diff auf den Quellcode an: gehe in den entpackten pivy Quellcode-Ordner und wende den .diff Patch an:


```python
patch -p1 < ../pivy_0.5.0~svn765-2.diff
```

dann


```python
debuild
```

um pivy ordnungsgemäß in ein offizielles installierbares Paket eingebaut zu haben. Dann installiere das Paket einfach mit gdebi.

#### Andere Linux Distributionen 

Hole Dir zuerst die neuesten Quellen aus dem [Projekt Repositorium](http://pivy.coin3d.org/mercurial/):


```python
hg clone http://hg.sim.no/Pivy/default Pivy 
```

Ab März 2012 ist die neueste Version Pivy-0.5.

Dann brauchst Du ein Werkzeug namens SWIG, um den C++ Code für die Python Bindungen zu generieren. Pivy-0.5 berichtet, dass es nur mit SWIG 1.3.31, 1.3.33, 1.3.35 und 1.3.40 getestet wurde. Du kannst also eine Quell Tar-Datei für eine dieser alten Versionen von [<http://www.swig.org>](http://www.swig.org) herunterladen. Dann entpacke sie und mache sie von der Kommandozeile aus (als root):


```python
./configure
make
make install (or checkinstall if you use it)
```

Der Bau dauert nur wenige Sekunden.

Alternativ kannst Du versuchen, mit einer neueren SWIG zu bauen. Ab März 2012 ist eine typische Repositorien Version 2.0.4. Pivy hat ein kleines Kompilierproblem mit SWIG 2.0.4 unter Mac OS (siehe unten), scheint aber auf Fedora Core 15 gut zu bauen.

Danach gehst du zu den pivy Quellen und rufst


```python
python setup.py build 
```

die die Quelldateien erstellt. Beachte, dass der Bau tausende von Warnungen erzeugen kann, aber hoffentlich keine Fehler auftreten werden.

Dies ist wahrscheinlich veraltet, aber du köntest auf einen Compiler Fehler stoßen, bei dem ein \'const char\*\' nicht in ein \'char\*\' umgewandelt werden kann. Um das zu beheben, musst du nur eine \'const\' vorher in die entsprechenden Zeilen schreiben. Es sind sechs Zeilen zu korrigieren.

Danach installieren durch ausgeben (als root):


```python
python setup.py install (or checkinstall python setup.py install)
```

Das war\'s, pivy ist installiert.

##### Mac OS 

== Diese Anleitungen könnten möglicherweise nicht vollständig sein. Etwas in dieser Art funktionierte für OS 10.7 ab März 2012. Ich verwende MacPorts für Repositorien, aber andere Optionen sollten auch funktionieren.

Wie für Linux, hole dir die neueste Quelle:


```python
hg clone http://hg.sim.no/Pivy/default Pivy 
```

Wenn du kein hg hast, kannst du es von MacPorts holen:


```python
port install mercurial
```

Dann brauchst du wie oben SWIG. Es sollte eine Sache sein von:


```python
port install swig
```

Ich fand, ich brauche auch:


```python
port install swig-python
```

Seit März 2012 ist die MacPorts SWIG Version 2.0.4. Wie oben für Linux angemerkt, ist es vielleicht besser, eine ältere Version herunterzuladen. SWIG 2.0.4 scheint einen Fehler zu haben, der das Bauen von Pivy verhindert. Siehe erste Meldung in diesem Auszug: <https://sourceforge.net/mailarchive/message.php?msg_id=28114815>

Dies kann korrigiert werden, indem man die 2 Quellorte bearbeitet, um Dereferenzierungen hinzuzufügen: \*arg4, \*arg5 an Stelle von arg4, arg5. Jetzt sollte Pivy bauen:


```python
python setup.py build
sudo python setup.py install
```

##### Windows 

== Angenommen, du verwendest Visual Studio 2005 oder höher, solltest du eine Eingabeaufforderung mit \'Visual Studio 2005 Command prompt\' aus dem Werkzeugmenü öffnen. Wenn der Python Interpreter noch nicht im Systempfad liegt, mache


```python
set PATH=path_to_python_2.5;%PATH%
```

Um mit pivy arbeiten zu können, solltest du dir die neuesten Quellen aus dem Repositorium des Projekts besorgen:


```python
svn co https://svn.coin3d.org/repos/Pivy/trunk Pivy 
```

Dann brauchst Du ein Werkzeug namens SWIG, um den C++ Code für die Python Bindungen zu erzeugen. Es wird empfohlen, die Version 1.3.25 von SWIG zu verwenden, nicht die neueste Version, da Pivy im Moment nur mit 1.3.25 korrekt funktioniert. Lade die Binärdateien für 1.3.25 von [<http://www.swig.org>](http://www.swig.org) herunter. Entpacke sie dann und füge sie von der Kommandozeile aus dem Systempfad hinzu


```python
set PATH=path_to_swig_1.3.25;%PATH%
```

und setze COINDIR auf den entsprechenden Pfad


```python
set COINDIR=path_to_coin
```

Unter Windows erwartet die Pivy Konfigurationsdatei standardmäßig SoWin anstelle von SoQt. Ich habe keinen naheliegenden Weg gefunden, um mit SoQt zu bauen, also habe ich die Datei setup.py direkt modifiziert. In Zeile 200 einfach den Teil \'sowin\' : (\'gui.\_sowin\', \'sowin-config\', \'pivy.gui.\') entfernen (die schließende Klammer nicht entfernen).

Danach gehe zu den pivy Quellen und rufe


```python
python setup.py build 
```

was die Quelldateien erstellt. Es kann sein, dass du einen Kompilierer Fehler bekommst, weil mehrere Kopfdateien nicht gefunden wurden. In diesem Fall passe die INCLUDE Variable an


```python
set INCLUDE=%INCLUDE%;path_to_coin_include_dir
```

und wenn die SoQt Kopfzeilen nicht an der gleichen Stelle wie die Coin Kopfzeilen sind auch


```python
set INCLUDE=%INCLUDE%;path_to_soqt_include_dir
```

und schließlich die Qt Kopfzeilen


```python
set INCLUDE=%INCLUDE%;path_to_qt4\include\Qt
```

Wenn du die Express Edition von Visual Studio verwendest, erhälst du möglicherweise eine Python keyerror Ausnahme. In diesem Fall musst Du ein paar Dinge in der msvccompiler.py, die sich in deiner Pythoninstallation befindet, ändern.

Gehe zur Zeile 122 und ersetze die Zeile


```python
vsbase = r"Software\Microsoft\VisualStudio\%0.1f" % version
```

mit


```python
vsbase = r"Software\Microsoft\VCExpress\%0.1f" % version
```

Dann versuche es noch einmal. Wenn du einen zweiten Fehler wie


```python
error: Python was built with Visual Studio 2003;...
```

Du must auch Zeile 128 ersetzen


```python
self.set_macro("FrameworkSDKDir", net, "sdkinstallrootv1.1")
```

mit


```python
self.set_macro("FrameworkSDKDir", net, "sdkinstallrootv2.0")
```

Versuche es noch einmal. Wenn du wieder einen Fehler wie


```python
error: Python was built with Visual Studio version 8.0, and extensions need to be built with the same version of the compiler, but it isn't installed.
```

dann solltest du die Umgebungsvariablen DISTUTILS_USE_SDK und MSSDK prüfen mit


```python
echo %DISTUTILS_USE_SDK%
echo %MSSDK%
```

Wenn noch nicht gesetzt, dann setze ihn einfach z.B. auf 1


```python
set DISTUTILS_USE_SDK=1
set MSSDK=1
```

Nun kann es zu einem Compilerfehler kommen, bei dem ein \'const char\*\' nicht in ein \'char\*\' umgewandelt werden kann. Um das zu beheben, musst du nur vorher eine \'const\' in die entsprechenden Zeilen schreiben. Es sind sechs Zeilen zu korrigieren. Danach kopiere das generierte Pivy Verzeichnis an einen Ort, wo der Python Interpreter in FreeCAD es finden kann.

### Verwendung 

Um zu überprüfen, ob Pivy korrekt installiert ist:


```python
import pivy
```

Um pivy Zugriff auf den FreeCAD Szenengraphen zu haben, gehe wie folgt vor:


```python
from pivy import coin
App.newDocument() # Open a document and a view 
view = Gui.ActiveDocument.ActiveView 
FCSceneGraph = view.getSceneGraph() # returns a pivy Python object that holds a SoSeparator, the main "container" of the Coin scenegraph
FCSceneGraph.addChild(coin.SoCube()) # add a box to scene 
```

Du kannst nun den FCSceneGraph mit dem dir() Befehl untersuchen.

### Zusätzliche Dokumentation 

Leider ist die Dokumentation über pivy immer noch fast nicht im Netz vorhanden. Aber du könntest die Coin Dokumentation nützlich finden, da pivy einfach Coin Funktionen, Knoten und Methoden in Python übersetzt, alles behält den gleichen Namen und die gleichen Eigenschaften, wobei der Unterschied in der Syntax zwischen C und Python berücksichtigt wird:

-   <https://bitbucket.org/Coin3D/coin/wiki/Documentation> - Coin3D API Referenz
-   <http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/index.html> - Der Inventor Mentor - Die \"Bibel\" der Inventor Szenenbeschreibungssprache.

Du kannst dir auch die Datei Draft.py im FreeCAD Mod/Draft Ordner ansehen, da sie starken Gebrauch von pivy macht.

## pyCollada

-   Startseite: <http://pycollada.github.com>
-   Lizenz: BSD
-   optional, notwendig um den Import und Export von Collada (.DAE) Dateien zu ermöglichen

pyCollada ist eine Python Bibliothek, die es Programmen ermöglicht, Dateien [Collada (\*.DAE)](http://en.wikipedia.org/wiki/COLLADA) zu lesen und zu schreiben. Wenn pyCollada auf Ihrem System installiert ist, ist FreeCAD in der Lage, den Import und Export im Collada Dateiformat zu handhaben.

### Installation 

Pycollada ist normalerweise noch nicht in den Repositorien der Linux Distributionen verfügbar, aber da es nur aus Python Dateien besteht, muss es nicht kompiliert werden und ist einfach zu installieren. Es gibt 2 Wege, oder direkt aus dem offiziellen pycollada git Repositorium, oder mit dem easy_install Werkzeug.

#### Linux 

In jedem Fall benötigst Du die folgenden Pakete bereits installiert auf Deinem System:


```python
python-lxml 
python-numpy
python-dateutil
```

##### Aus dem Git Repositorium 


```python
git clone git://github.com/pycollada/pycollada.git pycollada
cd pycollada
sudo python setup.py install
```

======= Mit easy_install ======= Angenommen, du hast bereits eine komplette Python Installation, sollte das easy_install Hilfsprogramm bereits vorhanden sein:


```python
easy_install pycollada
```

Du kannst überprüfen, ob pycollada korrekt installiert wurde, indem du in einer Python Konsole eingibst:


```python
import collada
```

Wenn es nichts zurückgibt (keine Fehlermeldung), dann ist alles OK

#### Windows 

Wenn es nichts zurückgibt (keine Fehlermeldung), dann ist alles OK. Unter Windows, da 0.15 pycollada sowohl in der FreeCAD Version als auch in den Entwickler Builds enthalten ist, so dass keine zusätzlichen Schritte notwendig sind.

#### Mac OS 

Wenn du den Homebrew Build von FreeCAD verwendest, kannst du pycollada mit pip in dein System Python installieren.

Wenn du pip installieren musst:


```python
$ sudo easy_install pip
```

Installiere pycollada:


```python
$ sudo pip install pycollada
```

Wenn du eine binäre Version von FreeCAD verwendest, kannst du pip anweisen, pycollada in die Site Pakete innerhalb von FreeCAD.app zu installieren:


```python
$ pip install --target="/Applications/FreeCAD.app/Contents/lib/python2.7/site-packages" pycollada
```

oder nach dem Herunterladen des pycollada Codes


```python
$ export PYTHONPATH=/Applications/FreeCAD\ 0.16.6706.app/Contents/lib/python2.7/site-packages:$PYTHONPATH
$ python setup.py install --prefix=/Applications/FreeCAD\ 0.16.6706.app/Contents
```

## IfcOpenShell

-   Startseite: <http://www.ifcopenshell.org>
-   Lizenz. \* LGPL
-   optional, notwendig zur Erweiterung der Importfähigkeit von IFC-Dateien

IFCOpenShell ist eine derzeit in Entwicklung befindliche Bibliothek, die es erlaubt, Dateien [Industry Foundation Classes (\*.IFC)](https://de.wikipedia.org/wiki/Industry_Foundation_Classes) zu importieren (und bald auch zu exportieren). IFC ist eine Erweiterung des STEP-Formats und wird zum Standard in \[hhttps://de.wikipedia.org/wiki/Building_Information_Modeling BIM\]-Arbeitsabläufen. Wenn ifcopenshell korrekt auf Ihrem System installiert ist, wird das FreeCAD [Arch-Arbeitsgebiet](Arch_Workbench/de.md) es erkennen und zum Importieren von IFC-Dateien verwenden, anstelle des eingebauten rudimentären Importeurs. Da ifcopenshell wie FreeCAD auf OpenCasCade basiert, ist die Qualität des Imports sehr hoch und erzeugt hochwertige Volumenkörpergeometrie.

### Installation 

Da ifcopenshell ziemlich neu ist, wirst du es wahrscheinlich selbst kompilieren müssen.

##### Linux 

== Du brauchst ein paar auf deinem System installierte Entwicklungspakete, um ifcopenshell zu kompilieren:


```python
liboce-*-dev
python-dev
swig
```

aber da FreeCAD auch alle benötigt, benötigst Du, wenn Du FreeCAD kompilieren kannst, keine zusätzlichen Abhängigkeiten, um IfcOpenShell zu kompilieren.

Hole dir den neuesten Quellcode von hier:


```python
git clone https://github.com/IfcOpenShell/IfcOpenShell.git
```

Der Bauprozess ist sehr einfach:


```python
mkdir ifcopenshell-build
cd ifcopenshell-build
cmake ../IfcOpenShell/cmake
```

oder, wenn du oce statt opencascade benutzt:


```python
cmake -DOCC_INCLUDE_DIR=/usr/include/oce ../ifcopenshell/cmake 
```

Da ifcopenshell hauptsächlich für Blender gemacht ist, verwendet es standardmäßig python3. Um es innerhalb von FreeCAD zu verwenden, musst du es gegen die gleiche Version von Python kompilieren, die auch von FreeCAD verwendet wird. Daher musst du möglicherweise die Python Version mit zusätzlichen cmake Parametern erzwingen (passe die Python Version an Deine an):


```python
cmake -DOCC_INCLUDE_DIR=/usr/include/oce -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 -DPYTHON_LIBRARY=/usr/lib/python2.7.so ../ifcopenshell/cmake
```

Dann:


```python
make
sudo make install
```

Du kannst überprüfen, ob ifcopenshell korrekt installiert wurde, indem du in einer Python Konsole eingibst:


```python
import ifcopenshell
```

Wenn es nichts zurückgibt (keine Fehlermeldung), dann ist alles OK

#### Windows 

**Hinweis**: Offizielle FreeCAD Installationsprogramme, die von der FreeCAD Webseite/Github Seite bezogen wurden, enthalten jetzt bereits ifcopenshell.

*Kopiert von der IfcOpenShell README Datei*

Anwendern wird empfohlen, die Visual Studio .sln Datei im Ordner win/ zu verwenden. Für Windows Anwender ist eine vorkompilierte Open CASCADE Version auf der Website <http://opencascade.org> verfügbar. Lade diese Version herunter, installiere sie und stelle die Pfade zu den Open CASCADE Header- und Bibliotheksdateien für MS Visual Studio C++ zur Verfügung.

Um den IfcPython wrapper zu erstellen, muss SWIG installiert werden. Bitte lade die aktuelle swigwin Version von <http://www.swig.org/download.html> herunter. Nach dem Entpacken der .zip Datei füge bitte den entpackten Ordner in die Umgebungsvariable PATH ein. Python muss installiert sein, bitte gib die Include- und Bibliotheks Pfade zu Visual Studio an.

### Verweise

Tutorium [Import/Export IFC - compiling IfcOpenShell](Import/Export_IFC_-_compiling_IfcOpenShell.md)

### Installation 

Auf allen Plattformen, nur durch Installation des entsprechenden Pakets von <https://www.opendesign.com/guestfiles/oda_file_converter>. Nach der Installation, wenn das Dienstprogramm nicht automatisch von FreeCAD gefunden wird, musst Du möglicherweise den Pfad zur ausführbaren Konverterdatei manuell einstellen, öffne Bearbeiten → Einstellungen → Import-Export → DWG und fülle \"Pfad zum Teigha File Converter\" entsprechend.

## TrägerLader (LazyLoader) 

TrägerLader (LazyLoader) ist ein Python Modul, das ein zeitversetztes Laden ermöglicht, während der Import immer noch am Anfang des Skripts erfolgt. Dies ist nützlich, wenn du ein anderes Modul importierst, das langsam ist und im gesamten Skript mehrmals verwendet wird. Die Verwendung von LazyLoader kann die Startzeiten des Arbeitsbereichs verbessern, aber das Modul muss bei der ersten Verwendung immer noch geladen werden.

### Installation 

LazyLoader ist in FreeCAD v0.19 enthalten

### Verwendung 

Du musst LazyLoader importieren und dann den Import des Moduls, das zurückgestellt werden soll, ändern.


```python
from lazy_loader.lazy_loader import LazyLoader
Part = LazyLoader('Part', globals(), 'Part')
```

Die Variable Part gibt an, wie das Modul in deinem Skript benannt ist. Du kannst \"Part als P importieren\" wiederholen, indem du die Variable änderst.


```python
P = LazyLoader('Part', globals(), 'Part')
```

You can also import a module from a package. 
```python
utils = LazyLoader('PathScripts', globals(), 'PathScripts.PathUtils')
``` Du kannst keine Einzelfunktionen importieren, sondern nur ganze Module.

### Verknüpfungen

-   Originalquelle: <https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/util/lazy_loader.py>
-   Weitere Erklärung: <https://wil.yegelwel.com/lazily-importing-python-modules/>
-   Code innerhalb des FreeCAD Quellcodes: <https://github.com/FreeCAD/FreeCAD/tree/master/src/3rdParty/lazy_loader>
-   Forumsdiskussion: <https://forum.freecadweb.org/viewtopic.php?f=10&t=45298>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Python Code](Category_Python Code.md) > [Developer Documentation](Category_Developer Documentation.md) > Extra python modules/de
