# Extra python modules/sv
{{TOCright}}

## Overview

This page lists several additional Python modules or other pieces of software that can be downloaded freely from the internet, and add functionality to your FreeCAD installation.

## PySide (previously PyQt) 

-   homepage (PySide): [<http://qt-project.org/wiki/PySide>](http://qt-project.org/wiki/PySide)
-   license: LGPL
-   optional, but needed by several modules: Draft, Arch, Ship, Plot, OpenSCAD, Spreadsheet

PySide (previously PyQt) is required by several modules of FreeCAD to access FreeCAD\'s Qt interface. It is already bundled in the windows verison of FreeCAD, and is usually installed automatically by FreeCAD on Linux, when installing from official repositories. If those modules (Draft, Arch, etc) are enabled after FreeCAD is installed, it means PySide (previously PyQt) is already there, and you don\'t need to do anything more.

**Notera**: av följande moduler, så är Pivy nu helt integrerad i alla FreeCAD installationspaket, och PyQt4 är också integrerat i Windows installationspaket.

### Installation

#### Linux

The simplest way to install PySide is through your distribution\'s package manager. On Debian/Ubuntu systems, the package name is generally *python-PySide*, while on RPM-based systems it is named *pyside*. The necessary dependencies (Qt and SIP) will be taken care of automatically.

#### Windows

The program can be downloaded from <http://qt-project.org/wiki/Category:LanguageBindings>::PySide::Downloads . You\'ll need to install the Qt and SIP libraries before installing PySide (to be documented).

#### MacOS

PySide on Mac can be installed via homebrew or port. See [Install dependencies](Compile_on_MacOS#Install_Dependencies.md) for more information.

### Usage

Once it is installed, you can check that everything is working by typing in FreeCAD Python console:


```python
import PySide
```

To access the FreeCAD interface, type:


```python
from PySide import QtCore,QtGui
FreeCADWindow = FreeCADGui.getMainWindow()
```

Now you can start to explore the interface with the dir() command. You can add new elements, like a custom widget, with commands like:


```python
FreeCADWindow.addDockWidget(QtCore.Qt.RghtDockWidgetArea,my_custom_widget)
```

Working with Unicode:


```python
text = text.encode('utf-8')
```

Working with QFileDialog and OpenFileName:


```python
path = FreeCAD.ConfigGet("AppHomePath")
#path = FreeCAD.ConfigGet("UserAppData")
OpenName, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Read a txt file", path, "*.txt")
```

Working with QFileDialog and SaveFileName:


```python
path = FreeCAD.ConfigGet("AppHomePath")
#path = FreeCAD.ConfigGet("UserAppData")
SaveName, Filter = PySide.QtGui.QFileDialog.getSaveFileName(None, "Save a file txt", path, "*.txt")
```

### Example of transition from PyQt4 and PySide 

PS: these examples of errors were found in the transition from PyQt4 to PySide and these corrections were made, other solutions are certainly available with the examples above


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

To access the FreeCAD interface, type: You can add new elements, like a custom widget, with commands like:


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

Working with Unicode:


```python
try:
    text = unicode(text, 'ISO-8859-1').encode('UTF-8')  # PyQt4
except Exception:
    text = text.encode('utf-8')                         # PySide
```

Working with QFileDialog and OpenFileName:


```python
OpenName = ""
try:
    OpenName = QFileDialog.getOpenFileName(None,QString.fromLocal8Bit("Lire un fichier FCInfo ou txt"),path,"*.FCInfo *.txt") # PyQt4
except Exception:
    OpenName, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Lire un fichier FCInfo ou txt", path, "*.FCInfo *.txt")#PySide
```

Working with QFileDialog and SaveFileName:


```python
SaveName = ""
try:
    SaveName = QFileDialog.getSaveFileName(None,QString.fromLocal8Bit("Sauver un fichier FCInfo"),path,"*.FCInfo") # PyQt4
except Exception:
    SaveName, Filter = PySide.QtGui.QFileDialog.getSaveFileName(None, "Sauver un fichier FCInfo", path, "*.FCInfo")# PySide
```

The MessageBox:


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

Working with setProperty (PyQt4) and setValue (PySide)


```python
self.doubleSpinBox.setProperty("value", 10.0) # PyQt4
```

replace with:


```python
self.doubleSpinBox.setValue(10.0) # PySide
```

Working with setToolTip


```python
self.doubleSpinBox.setToolTip(_translate("MainWindow", "Coordinate placement Axis Y", None)) # PyQt4
```

replace with:


```python
self.doubleSpinBox.setToolTip(_fromUtf8("Coordinate placement Axis Y")) # PySide
```

or:


```python
self.doubleSpinBox.setToolTip(u"Coordinate placement Axis Y.")# PySide
```

### Additional documentation 

-   [Qt official documentation site](https://doc.qt.io/qt.html#qtforpython)

## Pivy

-   homepage: [<https://bitbucket.org/Coin3D/coin/wiki/Home>](https://bitbucket.org/Coin3D/coin/wiki/Home)
-   license: BSD
-   optional, but needed by several modules of FreeCAD: Draft, Arch

Pivy is a needed by several modules to access the 3D view of FreeCAD. On windows, Pivy is already bundled inside the FreeCAD installer, and on Linux it is usually automatically installed when you install FreeCAD from an official repository. On macOS, unfortunately, you will need to compile pivy yourself.

### Installation 

#### Prerequisites

I believe before compiling Pivy you will want to have Coin and SoQt installed.

I found for building on Mac it was sufficient to install the [Coin3 binary package](http://www.coin3d.org/lib/plonesoftwarecenter_view). Attempting to install coin from MacPorts was problematic: tried to add a lot of X Windows packages and ultimately crashed with a script error.

For Fedora I found an RPM with Coin3.

SoQt compiled from [source](http://www.coin3d.org/lib/soqt/releases/1.5.0) fine on Mac and Linux.

#### Debian & Ubuntu 


<div class="mw-translate-fuzzy">

#### Debian & Ubuntu 

Med början i Debian Squeeze och Ubuntu Lucid, så kommer pivy att finnas tillgängligt direkt från de officiella förråden, vilket sparar mycket krångel. Innan dess, så kan du antingen ladda ned ett av de paket som vi har gjort (för debian och ubuntu karmic) tillgängliga på [Nedladdningssidorna](Download/sv.md), eller så kan du kompilera det själv.


</div>


<div class="mw-translate-fuzzy">

Det bästa sättet att kompilera pivy smidigt är att hämta debians källkodspaket för pivy och göra ett paket med debuild. Det är samma källkod som på den officiella pivysajten, men debianfolket har gjort flera bugg-fixningstillägg. Det kompilerar också bra på ubuntu karmic: <http://packages.debian.org/squeeze/python-pivy> (ladda ned .orig.gz och .diff.gz file, packa upp båda, tillämpa sedan .diff på källkoden: gå till den uppackade pivy källkodsmappen, och tillämpa .diff patchen:


</div>


```python
patch -p1 < ../pivy_0.5.0~svn765-2.diff
```

sedan


```python
debuild
```

för att få pivy korrekt byggt till ett officiellt installerbart paket. Sedan så är det bara att installera paketet med gdebi.

#### Other linux distributions 

First get the latest sources from the [project\'s repository](http://pivy.coin3d.org/mercurial/):


```python
hg clone http://hg.sim.no/Pivy/default Pivy
```

As of March 2012, the latest version is Pivy-0.5.

Sedan behöver du ett verktyg som kallas för SWIG för att generera C++ koden för Pythonbindningarna. Det rekommenderas att version 1.3.25 av SWIG används, inte den senaste versionen, därför att pivy för tillfället endast fungerar korrekt med 1.3.25. Ladda ned 1.3.25 source tarball från [<http://www.swig.org>](http://www.swig.org). Packa sedan upp den, och gör som root följande i en konsol:


```python
./configure
make
make install (or checkinstall if you use it)
```

Det tar bara några sekunder att bygga.

Alternatively, you can try building with a more recent SWIG. As of March 2012, a typical repository version is 2.0.4. Pivy has a minor compile problem with SWIG 2.0.4 on macOS (see below) but seems to build fine on Fedora Core 15.

Efter det, gå till pivy källkoden och anropa


```python
python setup.py build
```

which creates the source files. Note that build can produce thousands of warnings, but hopefully there will be no errors.

viltet skapar källkodsfilerna. Du kan få kompileringsfel där en \'const char\*\' inte kan konverteras till en \'char\*\'. För att fixa det så behöver du bara skriva en \'const\' innan raderna som orsakade felet.

Det finns sex rader att fixa. Efter det, installera genom att skriva (som root):


```python
python setup.py install (or checkinstall python setup.py install)
```

Klart! Pivy är installerat.

#### MacOS 

These instructions may not be complete. Something close to this worked for OS 10.7 as of March 2012. I use MacPorts for repositories, but other options should also work.

As for linux, get the latest source:


```python
hg clone http://hg.sim.no/Pivy/default Pivy
```

If you don\'t have hg, you can get it from MacPorts:


```python
port install mercurial
```

Then, as above you need SWIG. It should be a matter of:


```python
port install swig
```

I found I needed also:


```python
port install swig-python
```

As of March 2012, MacPorts SWIG is version 2.0.4. As noted above for linux, you might be better off downloading an older version. SWIG 2.0.4 seems to have a bug that stops Pivy building. See first message in this [digest](https://sourceforge.net/mailarchive/message.php?msg_id=28114815)

This can be corrected by editing the 2 source locations to add dereferences: \*arg4, \*arg5 in place of arg4, arg5. Now Pivy should build:


```python
python setup.py build
sudo python setup.py install
```

#### Windows 


<div class="mw-translate-fuzzy">

#### Windows 

När du använder Visual Studio 2005 eller senare så ska du öppna en kommandoprompt med \'Visual Studio 2005 Command prompt\' från Tools menyn. Om du ännu inte har Pythontolken i systemsökvägen, gör


</div>


```python
set PATH=path_to_python_2.5;%PATH%
```

För att få pivy att fungera så ska du hämta den senaste källkoden från projektets förråd:


```python
svn co https://svn.coin3d.org/repos/Pivy/trunk Pivy
```

Sedan behöver du ett verktyg som kallas för SWIG för att generera C++ koden för Python bindningarna. Det rekommenderas att version 1.3.25 av SWIG används, inte den senaste versionen, därför att pivy för tillfället endast fungerar korrekt med 1.3.25. Ladda ned binärkoden för 1.3.25 från [<http://www.swig.org>](http://www.swig.org). Packa sedan upp den och lägg till den i systemsökvägen från kommandoraden


```python
set PATH=path_to_swig_1.3.25;%PATH%
```

och ställ in COINDIR till den riktiga sökvägen


```python
set COINDIR=path_to_coin
```

På Windows så förväntar sig pivys konfigurationsfil SoWin istället för SoQt som standard. Jag har inte hittat en självklart sätt att bygga med SoQt, så Jag modifierade filen setup.py direkt.

Ta på rad 200 bort delen \'sowin\' : (\'gui.\_sowin\', \'sowin-config\', \'pivy.gui.\') (ta inte bort den stängande parentesen).

Efter det, gå till pivy källkoden och anropa


```python
python setup.py build
```

vilket skapar källkodsfilerna. Du kan få kompileringsfel för att flera headerfiler inte kunde hittas. I detta fall så får du justera INCLUDE variabeln


```python
set INCLUDE=%INCLUDE%;path_to_coin_include_dir
```

och om SoQt headers int är på samma plats som Coin headers så får du också justera


```python
set INCLUDE=%INCLUDE%;path_to_soqt_include_dir
```

och slutligen Qt headers


```python
set INCLUDE=%INCLUDE%;path_to_qt4\include\Qt
```


<div class="mw-translate-fuzzy">

Om du använder Expressutgåvan av Visual Studio så kan du få ett python keyerror undantag.

I detta fall så måste du ändra en del saker i msvccompiler.py som finns i din python installation.


</div>

Gå till rad 122 och byt ut raden


```python
vsbase = r"Software\Microsoft\VisualStudio\%0.1f" % version
```

mot


```python
vsbase = r"Software\Microsoft\VCExpress\%0.1f" % version
```


<div class="mw-translate-fuzzy">

Försök sedan igen.

Om du får ett andra fel som


</div>


```python
error: Python was built with Visual Studio 2003;...
```

Så måste du även byta ut rad 128


```python
self.set_macro("FrameworkSDKDir", net, "sdkinstallrootv1.1")
```

mot


```python
self.set_macro("FrameworkSDKDir", net, "sdkinstallrootv2.0")
```

Försök igen. Om du åter får ett fel som


```python
error: Python was built with Visual Studio version 8.0, and extensions need to be built with the same version of the compiler, but it isn't installed.
```

så ska du kontrollera miljövariablerna DISTUTILS_USE_SDK och MSSDK med


```python
echo %DISTUTILS_USE_SDK%
echo %MSSDK%
```

Om de inte är inställda än, ställ in dem till 1


```python
set DISTUTILS_USE_SDK=1
set MSSDK=1
```


<div class="mw-translate-fuzzy">

Nu kan du få kompileringsfel där en \'const char\*\' inte kan konverteras till en \'char\*\'. För att fixa det så behöver du bara skriva en \'const\' innan raderna som orsakade felet. Det finns sex rader att fixa.

Kopiera sedan den genererade pivykatalogen till en plats där pythontolken i FreeCAD kan hitta den.


</div>

### Usage 

To check if Pivy is correctly installed:


```python
import pivy
```

För att Pivy ska komma åt FreeCAD scengrafen, gör följande:


```python
from pivy import coin
App.newDocument() # Open a document and a view
view = Gui.ActiveDocument.ActiveView
FCSceneGraph = view.getSceneGraph() # returns a pivy Python object that holds a SoSeparator, the main "container" of the Coin scenegraph
FCSceneGraph.addChild(coin.SoCube()) # add a box to scene
```

Nu kan du utforska FCSceneGraph med dir() kommandot.

### Additonal Documentation 


<div class="mw-translate-fuzzy">

### Dokumentation

Olyckligtvis så existerar det knappast ännu någon dokumentation om pivy på nätet. Men Coin dokumentationen kan vara användbar, eftersom pivy helt enkelt översätter Coin funktioner, noder och metoder i python, allt behåller samma namn och egenskaper, bara man tänker på syntaxskillnaden mellan C och python:


</div>

-   <https://bitbucket.org/Coin3D/coin/wiki/Documentation> - Coin3D API Reference
-   <http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/index.html> - The Inventor Mentor - The \"bible\" of Inventor scene description language.

Du kan också titta på Draft.py filen i FreeCAD Mod/Draft mappen, eftersom den använder pivy mycket.

## pyCollada

-   homepage: <http://pycollada.github.com>
-   license: BSD
-   optional, needed to enable import and export of Collada (.DAE) files

pyCollada is a Python library that allow programs to read and write [Collada (\*.DAE)](http://en.wikipedia.org/wiki/COLLADA) files. When pyCollada is installed on your system, FreeCAD will be able to handle importing and exporting in the Collada file format.

### Installation 

#### Linux 


```python
sudo apt-get install python3-collada
```

You can check if pycollada was correctly installed by issuing in a Python console:


```python
import collada
```

If it returns nothing (no error message), then all is OK

#### Windows 

On Windows since 0.15 pycollada is included in both the FreeCAD release and developer builds so no additional steps are necessary.

#### MacOS 

If you are using the Homebrew build of FreeCAD you can install pycollada into your system Python using pip.

If you need to install pip:


```python
$ sudo easy_install pip
```

Install pycollada:


```python
$ sudo pip install pycollada
```

If you are using a binary version of FreeCAD, you can tell pip to install pycollada into the site-packages inside FreeCAD.app:


```python
$ pip install --target="/Applications/FreeCAD.app/Contents/lib/python2.7/site-packages" pycollada
```

or after downloading the pycollada code


```python
$ export PYTHONPATH=/Applications/FreeCAD\ 0.16.6706.app/Contents/lib/python2.7/site-packages:$PYTHONPATH
$ python setup.py install --prefix=/Applications/FreeCAD\ 0.16.6706.app/Contents
```

## IfcOpenShell

-   homepage: <http://www.ifcopenshell.org>
-   license: LGPL
-   optional, needed to extend import abilities of IFC files

IFCOpenShell is a library currently in development, that allows to import (and soon export) [Industry foundation Classes (\*.IFC)](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) files. IFC is an extension to the STEP format, and is becoming the standard in [BIM](http://en.wikipedia.org/wiki/Building_information_modeling) workflows. When ifcopenshell is correctly installed on your system, the FreeCAD [Arch Workbench](Arch_Workbench.md) will detect it and use it to import IFC files, instead of its built-in rudimentary importer. Since ifcopenshell is based on OpenCasCade, like FreeCAD, the quality of the import is very high, producing high-quality solid geometry.

### Installation 

Since ifcopenshell is pretty new, you\'ll likely need to compile it yourself.

#### Linux 

You will need a couple of development packages installed on your system in order to compile ifcopenshell:


```python
liboce-*-dev
python-dev
swig
```

but since FreeCAD requires all of them too, if you can compile FreeCAD, you won\'t need any extra dependency to compile IfcOpenShell.

Grab the latest source code from here:


```python
git clone https://github.com/IfcOpenShell/IfcOpenShell.git
```

The build process is very easy:


```python
mkdir ifcopenshell-build
cd ifcopenshell-build
cmake ../IfcOpenShell/cmake
```

or, if you are using oce instead of opencascade:


```python
cmake -DOCC_INCLUDE_DIR=/usr/include/oce ../ifcopenshell/cmake
```

Since ifcopenshell is made primarily for Blender, it uses Python3 by default. To use it inside FreeCAD, you need to compile it against the same version of Python that is used by FreeCAD. So you might need to force the Python version with additional cmake parameters (adjust the Python version to yours):


```python
cmake -DOCC_INCLUDE_DIR=/usr/include/oce -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 -DPYTHON_LIBRARY=/usr/lib/python2.7.so ../ifcopenshell/cmake
```

Then:


```python
make
sudo make install
```

You can check that ifcopenshell was correctly installed by issuing in a Python console:


```python
import ifcopenshell
```

If it returns nothing (no error message), then all is OK

#### Windows 

**Note**: Official FreeCAD installers obtained from the FreeCAD website/github page now contain ifcopenshell already.

*Copied from the IfcOpenShell README file*

Users are advised to use the Visual Studio .sln file in the win/ folder. For Windows users a prebuilt Open CASCADE version is available from the [opencascade website](http://opencascade.org). Download and install this version and provide the paths to the Open CASCADE header and library files to MS Visual Studio C++.

For building the IfcPython wrapper, SWIG needs to be installed. Please download the latest swigwin version from [swig website](https://www.swig.org/download.html). After extracting the .zip file, please add the extracted folder to the PATH environment variable. Python needs to be installed, please provide the include and library paths to Visual Studio.

### Links

Tutorial [Import/Export IFC - compiling IfcOpenShell](Import/Export_IFC_-_compiling_IfcOpenShell.md)

### Installation 

On all platforms, only by installing the appropriate package from [ODA DWG-DXF Converter](https://www.opendesign.com/guestfiles/oda_file_converter). After installation, if the utility is not found automatically by FreeCAD, you might need to set the path to the converter executable manually, open Edit → Preferences → Import-Export → DWG and fill \"Path to Teigha File Converter\" appropriately.

## LazyLoader

LazyLoader is a Python module that allows deferred loading, while still importing at the top of the script. This is useful if you are importing another module that is slow, and it is used several times throughout the script. Using LazyLoader can improve workbench startup times, but the module will still need to be loaded on first use.

### Installation 

LazyLoader is included with FreeCAD v0.19

### Usage 

You will need to import LazyLoader, then change the import of whatever module you want to be deferred.


```python
from lazy_loader.lazy_loader import LazyLoader
Part = LazyLoader('Part', globals(), 'Part')
```

The variable Part is how the module is named in your script. You can replicate \"import Part as P\" by changing the variable.


```python
P = LazyLoader('Part', globals(), 'Part')
```

You can also import a module from a package. 
```python
utils = LazyLoader('PathScripts', globals(), 'PathScripts.PathUtils')
``` You can\'t import individual functions, just entire modules.

### Links 

-   Original source: <https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/util/lazy_loader.py>
-   Further explanation: <https://wil.yegelwel.com/lazily-importing-python-modules/>
-   Code within the FreeCAD source code: <https://github.com/FreeCAD/FreeCAD/tree/master/src/3rdParty/lazy_loader>
-   Forum discussion: <https://forum.freecadweb.org/viewtopic.php?f=10&t=45298>


<div class="mw-translate-fuzzy">


{{docnav/sv|Localisation/sv|Source documentation/sv}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Python Code](Category_Python Code.md) > [Developer Documentation](Category_Developer Documentation.md) > Extra python modules/sv
