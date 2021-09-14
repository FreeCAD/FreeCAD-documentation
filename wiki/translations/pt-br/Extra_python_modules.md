# Extra python modules/pt-br




<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Overview

This page lists several additional python modules or other pieces of software that can be downloaded freely from the internet, and add functionality to your FreeCAD installation.

## PySide (previously PyQt4) 

-   homepage (PySide): [<http://qt-project.org/wiki/PySide>](http://qt-project.org/wiki/PySide)
-   license: LGPL
-   optional, but needed by several modules: Draft, Arch, Ship, Plot, OpenSCAD, Spreadsheet

PySide (previously PyQt) is required by several modules of FreeCAD to access FreeCAD\'s Qt interface. It is already bundled in the windows verison of FreeCAD, and is usually installed automatically by FreeCAD on Linux, when installing from official repositories. If those modules (Draft, Arch, etc) are enabled after FreeCAD is installed, it means PySide (previously PyQt) is already there, and you don\'t need to do anything more.

**Note:** FreeCAD progressively moved away from PyQt after version 0.13, in favour of [PySide](http://qt-project.org/wiki/PySide), which does exactly the same job but has a license (LGPL) more compatible with FreeCAD.

### Installation

#### Linux

The simplest way to install PySide is through your distribution\'s package manager. On Debian/Ubuntu systems, the package name is generally *python-PySide*, while on RPM-based systems it is named *pyside*. The necessary dependencies (Qt and SIP) will be taken care of automatically.

#### Windows

The program can be downloaded from <http://qt-project.org/wiki/Category:LanguageBindings>::PySide::Downloads . You\'ll need to install the Qt and SIP libraries before installing PySide (to be documented).

#### MacOSX

PyQt on Mac can be installed via homebrew or port. See [Install dependencies](Compile_on_MacOS#Install_Dependencies.md) for more information.

### Usage

Once it is installed, you can check that everything is working by typing in FreeCAD python console:


```python
import PySide
```

To access the FreeCAD interface, type :


```python
from PySide import QtCore,QtGui
FreeCADWindow = FreeCADGui.getMainWindow()
```

Now you can start to explore the interface with the dir() command. You can add new elements, like a custom widget, with commands like :


```python
FreeCADWindow.addDockWidget(QtCore.Qt.RghtDockWidgetArea,my_custom_widget)
```

Working with Unicode :


```python
text = text.encode('utf-8')
```

Working with QFileDialog and OpenFileName :


```python
path = FreeCAD.ConfigGet("AppHomePath")
#path = FreeCAD.ConfigGet("UserAppData")
OpenName, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Read a txt file", path, "*.txt")
```

Working with QFileDialog and SaveFileName :


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

To access the FreeCAD interface, type : You can add new elements, like a custom widget, with commands like :


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

Working with Unicode :


```python
try:
    text = unicode(text, 'ISO-8859-1').encode('UTF-8')  # PyQt4
except Exception:
    text = text.encode('utf-8')                         # PySide
```

Working with QFileDialog and OpenFileName :


```python
OpenName = ""
try:
    OpenName = QFileDialog.getOpenFileName(None,QString.fromLocal8Bit("Lire un fichier FCInfo ou txt"),path,"*.FCInfo *.txt") # PyQt4
except Exception:
    OpenName, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Lire un fichier FCInfo ou txt", path, "*.FCInfo *.txt")#PySide
```

Working with QFileDialog and SaveFileName :


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
self.doubleSpinBox.setProperty("value", 10.0)  # PyQt4
```

replace with :


```python
self.doubleSpinBox.setValue(10.0)  # PySide
```

Working with setToolTip


```python
self.doubleSpinBox.setToolTip(_translate("MainWindow", "Coordinate placement Axis Y", None))  # PyQt4
```

replace with :


```python
self.doubleSpinBox.setToolTip(_fromUtf8("Coordinate placement Axis Y"))  # PySide 
```

or :


```python
self.doubleSpinBox.setToolTip(u"Coordinate placement Axis Y.")# PySide
```

### Additional documentation 

Some pyQt4 tutorials (including how to build interfaces with Qt Designer to use with python):

-   <http://pyqt.sourceforge.net/Docs/PyQt4/classes.html> - the PyQt4 API Reference on sourceforge
-   <http://www.rkblog.rk.edu.pl/w/p/introduction-pyqt4/> - a simple introduction
-   <http://www.zetcode.com/tutorials/pyqt4/> - very complete in-depth tutorial

## Pivy

-   homepage: [<https://bitbucket.org/Coin3D/coin/wiki/Home>](https://bitbucket.org/Coin3D/coin/wiki/Home)
-   license: BSD
-   optional, but needed by several modules of FreeCAD: Draft, Arch

Pivy is a needed by several modules to access the 3D view of FreeCAD. On windows, Pivy is already bundled inside the FreeCAD installer, and on Linux it is usually automatically installed when you install FreeCAD from an official repository. On MacOSX, unfortunately, you will need to compile pivy yourself.

### Installation 

#### Prerequisites

I believe before compiling Pivy you will want to have Coin and SoQt installed.

I found for building on Mac it was sufficient to install the [Coin3 binary package](http://www.coin3d.org/lib/plonesoftwarecenter_view). Attempting to install coin from MacPorts was problematic: tried to add a lot of X Windows packages and ultimately crashed with a script error.

For Fedora I found an RPM with Coin3.

SoQt compiled from [source](http://www.coin3d.org/lib/soqt/releases/1.5.0) fine on Mac and Linux.

#### Debian & Ubuntu 

Starting with Debian Squeeze and Ubuntu Lucid, pivy will be available directly from the official repositories, saving us a lot of hassle. In the meantime, you can either download one of the packages we made (for debian and ubuntu karmic) availables on the [Download](Download.md) pages, or compile it yourself.

The best way to compile pivy easily is to grab the debian source package for pivy and make a package with debuild. It is the same source code from the official pivy site, but the debian people made several bug-fixing additions. It also compiles fine on ubuntu karmic: <http://packages.debian.org/squeeze/python-pivy> download the .orig.gz and the .diff.gz file, then unzip both, then apply the .diff to the source: go to the unzipped pivy source folder, and apply the .diff patch:


```python
patch -p1 < ../pivy_0.5.0~svn765-2.diff
```

then


```python
debuild
```

to have pivy properly built into an official installable package. Then, just install the package with gdebi.

#### Other linux distributions 

First get the latest sources from the [project\'s repository](http://pivy.coin3d.org/mercurial/):


```python
hg clone http://hg.sim.no/Pivy/default Pivy 
```

As of March 2012, the latest version is Pivy-0.5.

Then you need a tool called SWIG to generate the C++ code for the Python bindings. Pivy-0.5 reports that it has only been tested with SWIG 1.3.31, 1.3.33, 1.3.35, and 1.3.40. So you can download a source tarball for one of these old versions from [<http://www.swig.org>](http://www.swig.org). Then unpack it and from a command line do (as root):


```python
./configure
make
make install (or checkinstall if you use it)
```

It takes just a few seconds to build.

Alternatively, you can try building with a more recent SWIG. As of March 2012, a typical repository version is 2.0.4. Pivy has a minor compile problem with SWIG 2.0.4 on Mac OS (see below) but seems to build fine on Fedora Core 15.

After that go to the pivy sources and call


```python
python setup.py build 
```

which creates the source files. Note that build can produce thousands of warnings, but hopefully there will be no errors.

This is probably obsolete, but you may run into a compiler error where a \'const char\*\' cannot be converted in a \'char\*\'. To fix that you just need to write a \'const\' before in the appropriate lines. There are six lines to fix.

After that, install by issuing (as root):


```python
python setup.py install (or checkinstall python setup.py install)
```

That\'s it, pivy is installed.

#### Mac OS 

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

As of March 2012, MacPorts SWIG is version 2.0.4. As noted above for linux, you might be better off downloading an older version. SWIG 2.0.4 seems to have a bug that stops Pivy building. See first message in this digest: <https://sourceforge.net/mailarchive/message.php?msg_id=28114815>

This can be corrected by editing the 2 source locations to add dereferences: \*arg4, \*arg5 in place of arg4, arg5. Now Pivy should build:


```python
python setup.py build
sudo python setup.py install
```

#### Windows 

Assuming you are using Visual Studio 2005 or later you should open a command prompt with \'Visual Studio 2005 Command prompt\' from the Tools menu. If the Python interpreter is not yet in the system path do


```python
set PATH=path_to_python_2.5;%PATH%
```

To get pivy working you should get the latest sources from the project\'s repository:


```python
svn co https://svn.coin3d.org/repos/Pivy/trunk Pivy 
```

Then you need a tool called SWIG to generate the C++ code for the Python bindings. It is recommended to use version 1.3.25 of SWIG, not the latest version, because at the moment pivy will only function correctly with 1.3.25. Download the binaries for 1.3.25 from [<http://www.swig.org>](http://www.swig.org). Then unpack it and from the command line add it to the system path


```python
set PATH=path_to_swig_1.3.25;%PATH%
```

and set COINDIR to the appropriate path


```python
set COINDIR=path_to_coin
```

On Windows the pivy config file expects SoWin instead of SoQt as default. I didn\'t find an obvious way to build with SoQt, so I modified the file setup.py directly. In line 200 just remove the part \'sowin\' : (\'gui.\_sowin\', \'sowin-config\', \'pivy.gui.\') (do not remove the closing parenthesis).

After that go to the pivy sources and call


```python
python setup.py build 
```

which creates the source files. You may run into a compiler error several header files couldn\'t be found. In this case adjust the INCLUDE variable


```python
set INCLUDE=%INCLUDE%;path_to_coin_include_dir
```

and if the SoQt headers are not in the same place as the Coin headers also


```python
set INCLUDE=%INCLUDE%;path_to_soqt_include_dir
```

and finally the Qt headers


```python
set INCLUDE=%INCLUDE%;path_to_qt4\include\Qt
```

If you are using the Express Edition of Visual Studio you may get a python keyerror exception. In this case you have to modify a few things in msvccompiler.py located in your python installation.

Go to line 122 and replace the line


```python
vsbase = r"Software\Microsoft\VisualStudio\%0.1f" % version
```

with


```python
vsbase = r"Software\Microsoft\VCExpress\%0.1f" % version
```

Then retry again. If you get a second error like


```python
error: Python was built with Visual Studio 2003;...
```

you must also replace line 128


```python
self.set_macro("FrameworkSDKDir", net, "sdkinstallrootv1.1")
```

with


```python
self.set_macro("FrameworkSDKDir", net, "sdkinstallrootv2.0")
```

Retry once again. If you get again an error like


```python
error: Python was built with Visual Studio version 8.0, and extensions need to be built with the same version of the compiler, but it isn't installed.
```

then you should check the environment variables DISTUTILS\_USE\_SDK and MSSDK with


```python
echo %DISTUTILS_USE_SDK%
echo %MSSDK%
```

If not yet set then just set it e.g. to 1


```python
set DISTUTILS_USE_SDK=1
set MSSDK=1
```

Now, you may run into a compiler error where a \'const char\*\' cannot be converted in a \'char\*\'. To fix that you just need to write a \'const\' before in the appropriate lines. There are six lines to fix. After that copy the generated pivy directory to a place where the python interpreter in FreeCAD can find it.

### Usage 

To check if Pivy is correctly installed:


```python
import pivy
```

To have Pivy access the FreeCAD scenegraph do the following:


```python
from pivy import coin
App.newDocument() # Open a document and a view 
view = Gui.ActiveDocument.ActiveView 
FCSceneGraph = view.getSceneGraph() # returns a pivy Python object that holds a SoSeparator, the main "container" of the Coin scenegraph
FCSceneGraph.addChild(coin.SoCube()) # add a box to scene 
```

You can now explore the FCSceneGraph with the dir() command.

### Additonal Documentation 

Unfortunately documentation about pivy is still almost nonexistant on the net. But you might find Coin documentation useful, since pivy simply translate Coin functions, nodes and methods in python, everything keeps the same name and properties, keeping in mind the difference of syntax between C and python:

-   <https://bitbucket.org/Coin3D/coin/wiki/Documentation> - Coin3D API Reference
-   <http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/index.html> - The Inventor Mentor - The \"bible\" of Inventor scene description language.

You can also look at the Draft.py file in the FreeCAD Mod/Draft folder, since it makes big use of pivy.

## pyCollada

-   homepage: <http://pycollada.github.com>
-   license: BSD
-   optional, needed to enable import and export of Collada (.DAE) files

pyCollada is a python library that allow programs to read and write [Collada (\*.DAE)](http://en.wikipedia.org/wiki/COLLADA) files. When pyCollada is installed on your system, FreeCAD will be able to handle importing and exporting in the Collada file format.

### Installation 

Pycollada is usually not yet available in linux distributions repositories, but since it is made only of python files, it doesn\'t require compilation, and is easy to install. You have 2 ways, or directly from the official pycollada git repository, or with the easy\_install tool.

#### Linux 

In either case, you\'ll need the following packages already installed on your system:


```python
python-lxml 
python-numpy
python-dateutil
```

##### From the git repository 


```python
git clone git://github.com/pycollada/pycollada.git pycollada
cd pycollada
sudo python setup.py install
```

##### With easy\_install 

Assuming you have a complete python installation already, the easy\_install utility should be present already:


```python
easy_install pycollada
```

You can check if pycollada was correctly installed by issuing in a python console:


```python
import collada
```

If it returns nothing (no error message), then all is OK

#### Windows 

On Windows since 0.15 pycollada is included in both the FreeCAD release and developer builds so no additional steps are necessary.

#### Mac OS 

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

Since ifcopenshell is made primarily for Blender, it uses python3 by default. To use it inside FreeCAD, you need to compile it against the same version of python that is used by FreeCAD. So you might need to force the python version with additional cmake parameters (adjust the python version to yours):


```python
cmake -DOCC_INCLUDE_DIR=/usr/include/oce -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 -DPYTHON_LIBRARY=/usr/lib/python2.7.so ../ifcopenshell/cmake
```

Then:


```python
make
sudo make install
```

You can check that ifcopenshell was correctly installed by issuing in a python console:


```python
import ifcopenshell
```

If it returns nothing (no error message), then all is OK

#### Windows 

**Note**: Official FreeCAD installers obtained from the FreeCAD website/github page now contain ifcopenshell already.

*Copied from the IfcOpenShell README file*

Users are advised to use the Visual Studio .sln file in the win/ folder. For Windows users a prebuilt Open CASCADE version is available from the <http://opencascade.org> website. Download and install this version and provide the paths to the Open CASCADE header and library files to MS Visual Studio C++.

For building the IfcPython wrapper, SWIG needs to be installed. Please download the latest swigwin version from <http://www.swig.org/download.html> . After extracting the .zip file, please add the extracted folder to the PATH environment variable. Python needs to be installed, please provide the include and library paths to Visual Studio.

### Links

Tutorial [Import/Export IFC - compiling IfcOpenShell](Import/Export_IFC_-_compiling_IfcOpenShell.md)

## ODA Converter (previously Teigha Converter) 

-   homepage: <https://www.opendesign.com/guestfiles/oda_file_converter>
-   license: freeware
-   optional, used to enable import and export of DWG files

The ODA Converter is a small freely available utility that allows to convert between several versions of DWG and DXF files. FreeCAD can use it to offer DWG import and export, by converting DWG files to the DXF format under the hood,then using its standard DXF importer to import the file contents. The restrictions of the [DXF importer](Draft_DXF.md) apply.

### Installation 

On all platforms, only by installing the appropriate package from <https://www.opendesign.com/guestfiles/oda_file_converter> . After installation, if the utility is not found automatically by FreeCAD, you might need to set the path to the converter executable manually, open Edit → Preferences → Import-Export → DWG and fill \"Path to Teigha File Converter\" appropriately.

## LazyLoader

LazyLoader is a python module that allows deferred loading, while still importing at the top of the script. This is useful if you are importing another module that is slow, and it is used several times throughout the script. Using LazyLoader can improve workbench startup times, but the module will still need to be loaded on first use.

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





</div>


 

[Category:Python Code](Category:Python_Code.md) [Category:Developer Documentation](Category:Developer_Documentation.md)
