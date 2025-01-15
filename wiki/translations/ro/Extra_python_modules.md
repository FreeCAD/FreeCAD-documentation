# Extra python modules/ro
<div class="mw-translate-fuzzy">


{{docnav/ro
|[Locație](Localisation/ro.md)
|[Documentația sursă](Source_documentation/ro.md)
}}


</div>




## Overview


<div class="mw-translate-fuzzy">

Această pagină afișează câteva module suplimentare de tip python sau alte piese de software care pot fi descărcate gratuit de pe internet și pot adăuga funcționalitate pentru FreeCAD instalat.


</div>

## PySide


<div class="mw-translate-fuzzy">

## PySide (previously PyQt4) 

-   homepage (PySide): [<http://qt-project.org/wiki/PySide>](http://qt-project.org/wiki/PySide)
-   license: LGPL
-   opțional, dar necesare sunt câteva module: Draft, Arch, Ship, Plot, OpenSCAD, Spreadsheet


</div>


<div class="mw-translate-fuzzy">

PySide (anterior numit PyQt) este solicitat de mai multe module ale FreeCAD pentru a accesa interfața Qt a FreeCAD. Acesta este deja inclus în versiunea Windows a FreeCAD și, de obicei, este instalat automat de FreeCAD pe Linux, când se instalează din depozitele oficiale. Dacă aceste module (Draft, Arch etc.) sunt activate după ce FreeCAD este instalat, înseamnă că PySide (anterior PyQt) este deja acolo și nu mai trebuie să mai faceți nimic.


</div>

**Notă:** FreeCAD sa mutat progresiv de la PyQt după versiunea 0.13, în favoarea[PySide](http://qt-project.org/wiki/PySide), care face exact același lucru, dar are o licență (LGPL) mai compatibilă cu FreeCAD.



### Instalarea

#### Linux


<div class="mw-translate-fuzzy">

#### Linux 

Cea mai simplă modalitate de a instala PySide este prin managerul de pachete al distribuției. Pe sistemele Debian / Ubuntu, numele pachetului este în general \"python-PySide\", în timp ce în sistemele bazate pe RPM se numește \"pyside\". Dependentele necesare (Qt și SIP) vor fi luate în considerare automat.


</div>

#### Windows


<div class="mw-translate-fuzzy">

#### Windows 

Programul poate fi descărcat de la <http://qt-project.org/wiki/Category:LanguageBindings>::PySide::Downloads. Va trebui să instalați bibliotecile Qt și SIP înainte de a instala PySide (pentru a fi documentate).


</div>

#### MacOS


<div class="mw-translate-fuzzy">

#### MacOSX

PyQt on Mac can be installed via homebrew or port. See [Compile on MacOS/ro#Install_Dependencies](Compile_on_MacOS/ro#Install_Dependencies.md) for more information.


</div>

### Usage


<div class="mw-translate-fuzzy">

### Utilizare

Odată ce este instalat, puteți verifica dacă totul funcționează prin tastarea în consolă Python FreeCAD:


</div>


```python
import PySide
```

To access the FreeCAD interface, type :


```python
from PySide import QtCore,QtGui
FreeCADWindow = FreeCADGui.getMainWindow()
```

Acum puteți începe să explorați interfața cu comanda dir (). Puteți adăuga elemente noi, cum ar fi un widget personalizat, cu comenzi cum ar fi:


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

### Additional documentation 

-   [Qt official documentation site](https://doc.qt.io/qt.html#qtforpython)

## Pivy


<div class="mw-translate-fuzzy">

## Pivy 

-   homepage: [<https://bitbucket.org/Coin3D/coin/wiki/Home>](https://bitbucket.org/Coin3D/coin/wiki/Home)
-   license: BSD
-   optional, but needed by several modules of FreeCAD: Draft, Arch


</div>


<div class="mw-translate-fuzzy">

Pivy is a needed by several modules to access the 3D view of FreeCAD. On windows, Pivy is already bundled inside the FreeCAD installer, and on Linux it is usually automatically installed when you install FreeCAD from an official repository. On MacOSX, unfortunately, you will need to compile pivy yourself.


</div>



### Instalare

#### Prerequisites


<div class="mw-translate-fuzzy">

#### Cerințe preliminare 

Cred că înainte de a compila Pivy, veți dori să instalați Coin și SoQt.


</div>

Am găsit că pentru construirea pe Mac a fost suficient pentru a instala [Coin3 binary package](http://www.coin3d.org/lib/plonesoftwarecenter_view). Încercarea de a instala coin de la MacPorts a fost problematică: a încercat să adauge o mulțime de pachete X Windows și în cele din urmă s-a prăbușit cu o eroare de script.

For Fedora I found an RPM with Coin3.

SoQt compiled from [source](http://www.coin3d.org/lib/soqt/releases/1.5.0) fine on Mac and Linux.

#### Debian & Ubuntu 


<div class="mw-translate-fuzzy">

#### Debian & Ubuntu 

Începând cu Debian Squeeze și Ubuntu Lucid, pivy va fi disponibil direct din depozitele oficiale, economisind astfel o mulțime de bătăi de cap. Între timp, puteți să descărcați unul dintre pachetele pe care le-am făcut (pentru debian și karmic ubuntu) disponibile în paginile [Download](Download.md) sau să le compilați singur.


</div>

Cea mai bună modalitate de a compila pivy cu ușurință este să luați pachetul sursă debian pentru pivy și să faceți un pachet cu debuild. Este același cod sursă de pe site-ul oficial pivy, dar oamenii de la debian au făcut mai multe adăugări de fixare a bug-urilor. De asemenea, compilează bine karmicul ubuntu: <http://packages.debian.org/squeeze/python-pivy> descărcați fișierul .orig.gz și .diff.gz, apoi dezarhivați ambele, apoi aplicați .diff la sursă: mergeți la directorul sursă de pivy dezarhivate și aplicați patch-ul .diff:


```python
patch -p1 < ../pivy_0.5.0~svn765-2.diff
```

then


```python
debuild
```

to have pivy properly built into an official installable package. Then, just install the package with gdebi.

#### Other Linux distributions 


<div class="mw-translate-fuzzy">

#### Alte distribuții linux 

First get the latest sources from the [project\'s repository](http://pivy.coin3d.org/mercurial/):


</div>

Information to be added.

As of March 2012, the latest version is Pivy-0.5.

Apoi aveți nevoie de un instrument numit SWIG pentru a genera codul C++ pentru legăturile Python. Pivy-0.5 raportează că a fost testată numai cu SWIG 1.3.31, 1.3.33, 1.3.35 și 1.3.40. Deci, puteți descărca o sursă tarball pentru una dintre aceste versiuni vechi de la [<http://www.swig.org>](http://www.swig.org). Then unpack it and from a command line do (as root):


```python
./configure
make
make install (or checkinstall if you use it)
```

Ia doar câteva secunde compilarea.


<div class="mw-translate-fuzzy">

Alternativ, puteți încerca construirea cu un SWIG mai recent. Începând cu luna martie 2012, o versiune tipică pentru depozit este 2.0.4. Pivy are o problemă minoră de compilare cu SWIG 2.0.4 pe Mac OS (vezi mai jos), dar pare să construiască bine pe Fedora Core 15.


</div>

După aceea, mergeți la sursele de pivy și sunați


```python
python setup.py build
```

which creates the source files. Note that build can produce thousands of warnings, but hopefully there will be no errors.

Acest lucru este probabil depășit, însă este posibil să întâmpinați o eroare de compilator în care un \"const char \*\" nu poate fi convertit într-un \'char \*\'. Pentru a repara că trebuie doar să scrieți un \"const\" înainte în liniile corespunzătoare. Există șase linii de rezolvat.

După asta, instalați by issuing (ca root):


```python
python setup.py install (or checkinstall python setup.py install)
```

Et voila, pivy este instalat.

#### MacOS 


<div class="mw-translate-fuzzy">

#### Mac OS 

Este posibil ca aceste instrucțiuni să nu fie complete. Ceva aproape de acest lucru a funcționat pentru OS 10.7 în martie 2012. Eu folosesc MacPorts pentru depozite, dar ar trebui să funcționeze și alte opțiuni.


</div>

În ceea ce privește linux, obțineți cea mai recentă sursă:


```python
hg clone http://hg.sim.no/Pivy/default Pivy
```

Dacă nu aveți hg, îl puteți obține de la MacPorts:


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


<div class="mw-translate-fuzzy">

Începând cu luna martie 2012, MacPorts SWIG este la versiunea 2.0.4. După cum s-a menționat mai sus pentru linux, este posibil să fie mai bine să descărcați o versiune mai veche. SWIG 2.0.4 pare să aibă un bug care oprește clădirea Pivy. Vedeți primul mesaj din acest rezumat:<https://sourceforge.net/mailarchive/message.php?msg_id=28114815>


</div>

Acest lucru poate fi corectat prin editarea celor două locații sursă pentru a adăuga dereferențe: \*arg4, \*arg5 in place of arg4, arg5. Now Pivy should build:


```python
python setup.py build
sudo python setup.py install
```

#### Windows 


<div class="mw-translate-fuzzy">

#### Windows 

Presupunând că utilizați Visual Studio 2005 sau o versiune ulterioară, ar trebui să deschideți un prompt de comandă cu \"Visual Studio 2005 Command prompt\" din meniul Instrumente. Dacă interpretul Python nu este încă în calea sistemului, faceți acest lucru


</div>


```python
set PATH=path_to_python_3.x;%PATH%
```

Pentru a obține o pivă de lucru, ar trebui să obțineți cele mai recente surse din depozitul proiectului:

Information to be added.

Apoi aveți nevoie de un instrument numit SWIG pentru a genera codul C++ pentru legăturile Python. Se recomandă utilizarea versiunii 1.3.25 a SWIG, nu cea mai recentă versiune, deoarece în acest moment pivy va funcționa corect numai cu 1.3.25. Descărcați binarele pentru 1.3.25 de la [<http://www.swig.org>](http://www.swig.org). Apoi despachetați-l și din linia de comandă adăugați-l pe calea sistemului


```python
set PATH=path_to_swig_1.3.25;%PATH%
```

și setați COINDIR pe calea potrivită


```python
set COINDIR=path_to_coin
```

Pe Windows, fișierul config pivy se așteaptă ca SoWin în loc de SoQt ca implicit. Nu am găsit o modalitate evidentă de a construi cu SoQt, așa că am modificat fișierul setup.py direct. În linia 200, scoateți doar partea \"sowin\": (\'gui.\_sowin\', \'sowin-config\', \'pivy.gui.\') (Nu scoateți paranteza de închidere).

After that go to the pivy sources and call


```python
python setup.py build
```

care creează fișierele sursă. S-ar putea să întâlniți o eroare de compilator că nu au putut fi găsite mai multe fișiere antet. În acest caz, ajustați variabila INCLUDE


```python
set INCLUDE=%INCLUDE%;path_to_coin_include_dir
```

și dacă antetele SoQt nu se află în același loc ca și antetele de Coin


```python
set INCLUDE=%INCLUDE%;path_to_soqt_include_dir
```

și în final anteturile Qt


```python
set INCLUDE=%INCLUDE%;path_to_pyside\include\Qt
```


<div class="mw-translate-fuzzy">

Dacă utilizați Express Edition din Visual Studio, puteți obține o excepție python keyerror. În acest caz, trebuie să modificați câteva lucruri în msvccompiler.py localizate în instalarea dvs. python.


</div>

Mergeți la linia 122 și înlocuiți linia de cod


```python
vsbase = r"Software\Microsoft\VisualStudio\%0.1f" % version
```

cu


```python
vsbase = r"Software\Microsoft\VCExpress\%0.1f" % version
```


<div class="mw-translate-fuzzy">

Apoi încercați din nou. Dacă primiți o a doua eroare cum ar fi


</div>


```python
error: Python was built with Visual Studio 2003;...
```

trebui să înlocuiți și linia 128


```python
self.set_macro("FrameworkSDKDir", net, "sdkinstallrootv1.1")
```

cu


```python
self.set_macro("FrameworkSDKDir", net, "sdkinstallrootv2.0")
```

Reîncercați încă o dată. Dacă apare din nou o eroare cum ar fi


```python
error: Python was built with Visual Studio version 8.0, and extensions need to be built with the same version of the compiler, but it isn't installed.
```

then you should check the environment variables DISTUTILS_USE_SDK and MSSDK with


```python
echo %DISTUTILS_USE_SDK%
echo %MSSDK%
```

If not yet set then just set it e.g. to 1


```python
set DISTUTILS_USE_SDK=1
set MSSDK=1
```


<div class="mw-translate-fuzzy">

Acum, puteți întâlni o eroare de compilator în care un \'const char \*\' nu poate fi convertit într-un \'char \*\'. Pentru a repara că trebuie doar să scrieți un \"const\" înainte în liniile corespunzătoare. Există șase linii de rezolvat. Dupa ce copiați directorul generat pivy într-un loc in care interpretul python din FreeCAD îl poate gasi.


</div>

### Usage 


<div class="mw-translate-fuzzy">

### Utilizare 

Pentru a verifica dacă Pivy este instalat corect:


</div>


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


<div class="mw-translate-fuzzy">

### Documentație suplimentară 

Din păcate, documentația despre pivu este încă aproape inexistentă pe net. Dar s-ar putea să găsiți documentația Coin utilă, deoarece pivy pur și simplu traduce funcții de coin, noduri și metode în Python, totul păstrează același nume și proprietăți, ținând cont de diferența de sintaxă dintre C și python:


</div>


<div class="mw-translate-fuzzy">

-   <https://bitbucket.org/Coin3D/coin/wiki/Documentation> - Coin3D API Reference
-   <http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/index.html> - The Inventor Mentor - The \"bible\" of Inventor scene description language.


</div>

You can also look at the Draft.py file in the FreeCAD Mod/Draft folder, since it makes big use of pivy.

## pyCollada


<div class="mw-translate-fuzzy">

## pyCollada 

-   homepage: <http://pycollada.github.com>
-   license: BSD
-   optional, needed to enable import and export of Collada (.DAE) files


</div>


<div class="mw-translate-fuzzy">

pyCollada is a python library that allow programs to read and write [Collada (\*.DAE)](http://en.wikipedia.org/wiki/COLLADA) files. When pyCollada is installed on your system, FreeCAD will be able to handle importing and exporting in the Collada file format.


</div>

### Installation

#### Linux 


```python
sudo apt-get install python3-collada
```


<div class="mw-translate-fuzzy">

You can check if pycollada was correctly installed by issuing in a python console:


</div>


```python
import collada
```

If it returns nothing (no error message), then all is OK

#### Linux AppImages and Snaps 

Paste this code in the [Python console](Python_console.md):


```python
import addonmanager_utilities as utils
import subprocess
import os

if hasattr(utils, "get_python_exe"):
    # For v0.21:
    python_exe = utils.get_python_exe()
else:
    # For v0.22/v1.0:
    from freecad.utils import get_python_exe

python_exe = get_python_exe()
vendor_path = utils.get_pip_target_directory()
if not os.path.exists(vendor_path):
    os.makedirs(vendor_path)

subprocess.run(
    [
        python_exe,
        "-m",
        "pip",
        "install",
        "--disable-pip-version-check",
        "--target",
        vendor_path,
        "pycollada",
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    timeout=120,
    check=True,
)
```

#### Windows 

Pe Windows, de la 0.15 pycollada este inclus atât în versiunea FreeCAD, cât și în versiunea dezvoltatorului, deci nu sunt necesare pași suplimentari.




<div class="mw-translate-fuzzy">

#### Mac OS 


</div>

Dacă utilizați buildul Homebrew al FreeCAD, puteți instala pycollada în sistemul dvs. Python folosind pip.

If you need to install pip:


```python
$ sudo easy_install pip
```

Install pycollada:


```python
$ sudo pip install pycollada
```

Dacă utilizați o versiune binară a FreeCAD, puteți spune pip-ului să instaleze pycollada în pachetele de site-uri din cadrul FreeCAD.app:


```python
$ pip install --target="/Applications/FreeCAD.app/Contents/lib/python3.x/site-packages" pycollada
```

sau după descărcarea codului pycollada


```python
$ export PYTHONPATH=/Applications/FreeCAD\ 0.16.6706.app/Contents/lib/python3.x/site-packages:$PYTHONPATH
$ python setup.py install --prefix=/Applications/FreeCAD\ 0.2x.yyyy.app/Contents
```

## IfcOpenShell

-   homepage: <http://www.ifcopenshell.org>
-   license: LGPL
-   optional, needed to extend import abilities of IFC files


<div class="mw-translate-fuzzy">

IFCOpenShell este o bibliotecă în curs de dezvoltare, care permite importul fișierelor [Classes Fundation Classes (\* .IFC)](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) pentru import (și, în curând, export). IFC este o extensie a formatului STEP și devine standard în fluxurile de lucru [BIM](http://en.wikipedia.org/wiki/Building_information_modeling). Când sistemul ifcopenshell este instalat corect pe sistem, FreeCAD [Arch Workbench/ro](Arch_Workbench/ro.md) îl va detecta și îl va folosi pentru a importa fișiere IFC în locul importatorului său rudimentar integrat. Deoarece ifcopenshell se bazează pe OpenCasCade, precum FreeCAD, calitatea importului este foarte mare, producând o geometrie solidă de înaltă calitate.


</div>

### Installation 

#### Linux 

Installation instructions can be found [here](https://docs.ifcopenshell.org/ifcopenshell-python/installation.html).


<div class="mw-translate-fuzzy">

You can check that ifcopenshell was correctly installed by issuing in a python console:


</div>


```python
import ifcopenshell
```

If it returns nothing (no error message), then all is OK

#### Windows and macOS 

IfcOpenShell is included in both the FreeCAD release and developer builds so no additional steps are necessary.

### Links


<div class="mw-translate-fuzzy">

### Links 

Tutorial [Import/Export IFC - compiling IfcOpenShell](Import/Export_IFC_-_compiling_IfcOpenShell.md)


</div>

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


{{docnav/ro
|[Locație](Localisation/ro.md)
|[Documentația sursă](Source_documentation/ro.md)
}}


</div>



---
⏵ [documentation index](../README.md) > [Python Code](Category_Python%20Code.md) > [Developer Documentation](Category_Developer%20Documentation.md) > Extra python modules/ro
