# Extra python modules/es
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Vista general 

En esta página se enumeran varios módulos adicionales de python u otras piezas de software que pueden descargarse libremente de Internet, y que añaden funcionalidad a su instalación de FreeCAD.

## PySide (anteriormente PyQt4) 

-   página web (PySide): [<http://qt-project.org/wiki/PySide>](http://qt-project.org/wiki/PySide)
-   licencia: LGPL
-   opcional, pero necesario para varios módulos: Borrador, Arco, Barco, Gráfica, OpenSCAD, Hoja de cálculo

PySide (antes PyQt) es requerido por varios módulos de FreeCAD para acceder a la interfaz Qt de FreeCAD. Ya está incluido en la versión de Windows de FreeCAD, y suele ser instalado automáticamente por FreeCAD en Linux, cuando se instala desde los repositorios oficiales. Si esos módulos (Draft, Arch, etc.) se activan después de que se instale FreeCAD, significa que PySide (antes PyQt) ya está ahí, y no es necesario hacer nada más.

**Nota:** FreeCAD se alejó progresivamente de PyQt después de la versión 0.13, a favor de [PySide](http://qt-project.org/wiki/PySide), que hace exactamente el mismo trabajo pero tiene una licencia (LGPL) más compatible con FreeCAD.

### Instalación

#### Linux

La vía más simple para instalar PySide es a través del administrador de paquetes de su distribución. En los sistemas Debian/Ubuntu, el nombre del paquete es generalmente *python-PySide*, mientras que en los sistemas basados en RPM se llama *pyside*. Las dependencias necesarias (Qt y SIP) serán atendidas automáticamente.

#### Windows

El programa puede ser descargado de <http://qt-project.org/wiki/Category:LanguageBindings>::PySide::Downloads . Necesitarás instalar las librerías Qt y SIP antes de instalar PySide (para ser documentado).

#### MacOSX

PyQt en Mac puede ser instalado vía homebrew o puerto. Ver [Instalar dependencias](Compile_on_MacOS/es#Install_Dependencies.md) para más información.

### Uso

Una vez instalado, puede comprobar que todo funciona escribiendo en la consola python de FreeCAD:


```python
import PySide
```

Para acceder a la interfaz de FreeCAD, escriba :


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

### Documentación

Más tutoriales de pyQt4 (incluyendo cómo construir interfaces con Qt Designer para utilizar con Python):

<http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/classes.html> - la referencia oficial del API de PyQt4

<http://www.rkblog.rk.edu.pl/w/p/introduction-pyqt4/> - una simple introducción

<http://www.zetcode.com/tutorials/pyqt4/> - un tutorial en profundidad muy completo

## Pivy

-   homepage: [<https://bitbucket.org/Coin3D/coin/wiki/Home>](https://bitbucket.org/Coin3D/coin/wiki/Home)
-   license: BSD
-   optional, but needed by several modules of FreeCAD: Draft, Arch

Pivy is a needed by several modules to access the 3D view of FreeCAD. On windows, Pivy is already bundled inside the FreeCAD installer, and on Linux it is usually automatically installed when you install FreeCAD from an official repository. On MacOSX, unfortunately, you will need to compile pivy yourself.

### Instalación 

#### Requisitos previos 

Creo que antes de compilar Pivy querrás tener Coin y SoQt instalados.

Para construirlo en Mac es suficiente instalar el [paquete binario de Coin3](http://www.coin3d.org/lib/plonesoftwarecenter_view). Intentar instalar Coin desde MacPorts es problemático: añadir un montón de paquetes de X Windows y finalmente se cuelga con un error de script.

Para Fedora encontré un RPM con Coin3.

SoQt compilado desde [código fuente](http://www.coin3d.org/lib/soqt/releases/1.5.0) funciona bien en Mac y Linux.

#### Debian & Ubuntu 

Empezando con Debian Squeeze y Ubuntu Lucid, pivy está disponible directamente desde los repositorios oficiales, ahorrándonos un montón de dificultades. Mientras tanto, puedes descargar uno de los paquetes que hemos creado (para Debian y Ubuntu karmic) disponibles en la página de [Descargas](Download/es.md), o compilarlo tu mismo.

El mejor modo de compilar pivy siomplemente es aprovechar el paquete de código fuente de Debian para pivy y crear un paquete con debuild. Es el mismo código fuente desde la web oficial de pivy, pero la gente de Debian han creado varios parches adicionales. También se compila bien en Ubuntu karmic: <http://packages.debian.org/squeeze/python-pivy>, descarga los archivos .orig.gz y .diff.gz, luego descomprimelos, y aplica .diff al código fuente: ve a las carpetas del código fuente descomprimido de pivy, y aplica el parche .diff:


```python
patch -p1 < ../pivy_0.5.0~svn765-2.diff
```

luego


```python
debuild
```

para tener pivy correctamente construido en un paquete oficial de instalación. A continuación, simplemente instala el paquete con gdebi.

#### Otras distribuciones Linux 

Primero consigue la última versión del código fuente de [los repositorios del proyecto](http://pivy.coin3d.org/mercurial/):


```python
hg clone http://hg.sim.no/Pivy/default Pivy 
```

En marzo de 2012, la última versión es Pivy-0.5

Luego necesitas una herramienta llamada SWIG para generar el código C++ para la vinculación de Python. Pivy-0.5 informa que sólo ha sido comprobado con SWIG 1.3.31, 1.3.33, 1.3.35, y 1.3.40. Así que puedes descargar el código fuente en un tarball para una de dichas versiones anteriores desde [<http://www.swig.org>](http://www.swig.org). Luego descomprimelo y desde la línea de comandos haz lo siguiente (como root):


```python
./configure
make
make install (or checkinstall if you use it)
```

Esto tardará unos segundos en construirse.

Como alternativa, puedes tratar de construir con un SWIG más reciente. En marzo de 2012, una versión típica del repositorio es la 2.0.4. Pivy tiene un problema menor de compilación con SWIG 2.0.4 en Mac OS (mira más abajo) pero parece construirse bien en Fedora Core 15.

Después de eso ve al archivo que va a los recursos de pivy y ejecuta


```python
python setup.py build 
```

lo que creará los archivos fuente. Ten en cuenta que la construcción puede producir miles de advertencias, pero afortunadamente no hay errores.

Es posible que esto esté obsoleto, pero puedes llegar a un error de compilación donde una constante de tipo caracter (char) no puede ser convertida en una \'char\*\'. Para solucionarlo sólo necesitas escribir una constante antes de las líneas apropiadas. Hay 6 líneas que corregir.

Después de eso, instalar por publicación (como root):


```python
python setup.py install (or checkinstall python setup.py install)
```

Eso es todo, pivy está instalado.

#### Mac OS 

Estas instrucciones puede que no estén completas. Algo parecido funciona para OS 10.7 en marzo de 2012. He utilizado MacPorts para los repositorios, pero también deberían funcionar otras opciones.

Para Linux, consigue la última vcersión del código fuente:


```python
hg clone http://hg.sim.no/Pivy/default Pivy 
```

Si no tienes hg, puedes conseguirlo desde MacPorts:


```python
port install mercurial
```

Luego, como se indica arriba, necesitas SWIG. Debería ser cuestión de hacer:


```python
port install swig
```

He encontrado que también necesitaba:


```python
port install swig-python
```

En marzo de 2012, la versión de SWIG en MacPorts es la 2.0.4. Como se ha indicado arriba para Linux, podría ser mejor que descargaras una versión más antigua. SWIG 2.0.4 parece tener un error que detiene la construcción de Pivy. Mira el primer mensaje en este enlace: <https://sourceforge.net/mailarchive/message.php?msg_id=28114815>

Esto se puede corregir editando las dos ubicaciones de código fuente para añadir: \*arg4, \*arg5 en lugar de arg4, arg5. Ahora Pivy debería construirse:


```python
python setup.py build
sudo python setup.py install
```

#### Windows 

Asumiendo que utilizas Visual Studio 2005 o superior deberías abrir una ventana de comandos con \'Visual Studio 2005 Command prompt\' desde el menú Herramientas. Si el interprete aún no está en el sistema, haz


```python
set PATH=path_to_python_2.5;%PATH%
```

Para tener pivy funcionando deberías conseguir las últimas fuentes desde los repositorios del proyect:


```python
svn co https://svn.coin3d.org/repos/Pivy/trunk Pivy 
```

Luego necesitas una herramienta denominada SWIG para generar el ódigo C++ para la vinculación con Python. Es recomendable utilizar la versión 1.3.25 de SWIG, no la última versión, porque de momento pivy sólo funciona correctamente con con la versión with 1.3.25. Descarga los binarios para 1.3.25 desde [<http://www.swig.org>](http://www.swig.org). Luego descomprimelo y desde la línea de comandos añádelo al sistema path


```python
set PATH=path_to_swig_1.3.25;%PATH%
```

y establece COINDIR a la ruta aproviada


```python
set COINDIR=path_to_coin
```

En Windows el archivo de configuración de pivyespera SoWin en lugar de SoQt por defecto. No he encontrado una manera obvia para construirlo con SoQt, así que he modificado el arhivo setup.py directamente. En la línea 200 simplemente elimina la parte \'sowin\' : (\'gui.\_sowin\', \'sowin-config\', \'pivy.gui.\') (no elimines los paréntesis de cierre).

Después de esto ve a las fuentes de pivy y ejecuta


```python
python setup.py build 
```

lo cual crea los archivos de fuente. Puedes llegar a un error de compilación de \'Varios archivos de cabecera no se han encontrado\'. En este caso ajusta la variable INCLUDE


```python
set INCLUDE=%INCLUDE%;path_to_coin_include_dir
```

y si las cabeceras de SoQt no están en el mismo sitio que las cabeceras de Coin también


```python
set INCLUDE=%INCLUDE%;path_to_soqt_include_dir
```

y finalmente las cabeceras de Qt


```python
set INCLUDE=%INCLUDE%;path_to_qt4\include\Qt
```

Si estas utilizando la versión Express Edition de Visual Studio puedes tener una excepción de error de clave de Python. En este caso tendrás que modificar unas cuantas cosas en msvccompiler.py situado en la instalación de Python.

Ve a la línea 122 y reemplaza la línea


```python
vsbase = r"Software\Microsoft\VisualStudio\%0.1f" % version
```

con


```python
vsbase = r"Software\Microsoft\VCExpress\%0.1f" % version
```

Luego prueba de nuevo. Si te da un segundo error como


```python
error: Python was built with Visual Studio 2003;...
```

debes reemplazar también la línea 128


```python
self.set_macro("FrameworkSDKDir", net, "sdkinstallrootv1.1")
```

con


```python
self.set_macro("FrameworkSDKDir", net, "sdkinstallrootv2.0")
```

Intenta de nuevo. Si tienes un nuevo error como


```python
error: Python was built with Visual Studio version 8.0, and extensions need to be built with the same version of the compiler, but it isn't installed.
```

entonces deberías comprobar las variables de entorno DISTUTILS\_USE\_SDK y MSSDK con


```python
echo %DISTUTILS_USE_SDK%
echo %MSSDK%
```

If not yet set then just set it e.g. to 1


```python
set DISTUTILS_USE_SDK=1
set MSSDK=1
```

Ahora, debes encontrar un error de compilación donde una constante de tipo char no se puede convertir en char. Para solucionarlo necesitas escribir una constante antes de las líneas apropiadas. Hay 6 líneas que corregir. Después copia el directorio de pivy generado a un lugar donde el interprete de Python de FreeCAD lo pueda encontrar.

### Utilización

To check if Pivy is correctly installed:


```python
import pivy
```

Para tener Pivy acceso a la escena gráfica de FreeCAD haz lo siguiente:


```python
from pivy import coin
App.newDocument() # Open a document and a view 
view = Gui.ActiveDocument.ActiveView 
FCSceneGraph = view.getSceneGraph() # returns a pivy Python object that holds a SoSeparator, the main "container" of the Coin scenegraph
FCSceneGraph.addChild(coin.SoCube()) # add a box to scene 
```

Ahora puedes explorar FCSceneGraph con el comando dir().


<div class="mw-translate-fuzzy">

### Documentación 

Desafortunadamente la documentación sobre pivy es casi inexistente en la redt. Pero podrías encontrar la documentación de Coin útil, ya que pivy simplemente traduce las funciones de Coin, los nodos y métodos en Python, todo mantiene el mismo nombre y propiedades, teniendo en cuenta la diferencia de sintaxis entre C y Python:


</div>

-   <http://doc.coin3d.org/Coin/classes.html> - Referencia del API de Coin3D

-   <http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/index.html> - The Inventor Mentor - La \"biblia\" del lenguaje de descripción de escena de Inventor.

También puedes echar un vistazo al archivo Draft.py en el directorio de FreeCAD Mod/Draft, ya que hace un uso importante de pivy.

## pyCollada

-   homepage: <http://pycollada.github.com>
-   license: BSD
-   optional, needed to enable import and export of Collada (.DAE) files

[pyCollada](http://pycollada.github.com) es una biblioteca de Python que permite a los programas leer y escribir [archivos de Collada (\*.DAE)](http://en.wikipedia.org/wiki/COLLADA). Cuando pyCollada está instalado en tu sistema, FreeCAD ({{version/es|0.13}}) lo detectará y añadirá opciones de importación y exportación para manejar la apertura y guardado en el formato de archivos de Collada.

### Instalación 

Pycollada no está normalmente disponible en los repositorios de las distribuciones de Linux, pero ya que está creado únicamente por archivos de Python, no es necesaria su compilación, y es sencillo de instalar. Tienes dos métodos, o directamente desde el repositorio ofician en Git de pycollada, o con la herramienta easy\_install.

#### Linux 

En ambos casos, necesitaras tener los siguientes paquetes ya instalados en tu sistema:


```python
python-lxml 
python-numpy
python-dateutil
```

##### Desde el repositorio de Git 


```python
git clone git://github.com/pycollada/pycollada.git pycollada
cd pycollada
sudo python setup.py install
```

##### Con easy\_install 

Asumiendo que ya tienes una instalación completa de Python, la utilidad easy\_install ya debería estar presente:


```python
easy_install pycollada
```

Puedes comprobar si pycollada fue instalada correctamente emitiendo en una consola de python:


```python
import collada
```

Si no devuelve nada (no hay mensaje de error), entonces todo está bien.

#### Windows 

En Windows desde 0.15 pycollada está incluida tanto en la versión de FreeCAD como en las construcciones de los desarrolladores, por lo que no son necesarios pasos adicionales.

#### Mac OS 

Si estás usando la versión Homebrew de FreeCAD puedes instalar pycollada en tu sistema Python usando pip.

Si necesitas instalar pip:


```python
$ sudo easy_install pip
```

Instalar pycollada:


```python
$ sudo pip install pycollada
```

Si está usando una versión binaria de FreeCAD, puede decirle a pip que instale pycollada en los paquetes del sitio dentro de FreeCAD.app:


```python
$ pip install --target="/Applications/FreeCAD.app/Contents/lib/python2.7/site-packages" pycollada
```

o después de descargar el código de la pycollada


```python
$ export PYTHONPATH=/Applications/FreeCAD\ 0.16.6706.app/Contents/lib/python2.7/site-packages:$PYTHONPATH
$ python setup.py install --prefix=/Applications/FreeCAD\ 0.16.6706.app/Contents
```

## IfcOpenShell

-   página web: <http://www.ifcopenshell.org>
-   licencia: LGPL
-   opcional, necesario para ampliar las capacidades de importación de los archivos IFC

IFCOpenShell is a library currently in development, that allows to import (and soon export) _ will detect it and use it to import IFC files, instead of its built-in rudimentary importer. Since ifcopenshell is based on OpenCasCade, like FreeCAD, the quality of the import is very high, producing high-quality solid geometry.

### Instalación 

Ya que ifcopenshell es bastante nuevo, es probable que tengas que compilarlo tú mismo.

#### Linux 

Necesitará un par de paquetes de desarrollo instalados en su sistema para compilar ifcopenshell:


```python
liboce-*-dev
python-dev
swig
```

pero como FreeCAD requiere todos ellos también, si puedes compilar FreeCAD, no necesitarás ninguna dependencia extra para compilar IfcOpenShell.

Coge el último código fuente de aquí:


```python
git clone https://github.com/IfcOpenShell/IfcOpenShell.git
```

El proceso de construcción es muy fácil:


```python
mkdir ifcopenshell-build
cd ifcopenshell-build
cmake ../IfcOpenShell/cmake
```

o, si estás usando oce en lugar de opencascade:


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

### Enlaces

Tutorial [Importación/Exportación IFC - compilación de IfcOpenShell](Import/Export_IFC_-_compiling_IfcOpenShell/es.md)

### Instalación 

En todas las plataformas, sólo instalando el paquete apropiado de <https://www.opendesign.com/guestfiles/oda_file_converter> . Después de la instalación, si la utilidad no es encontrada automáticamente por FreeCAD, puede que sea necesario establecer la ruta del ejecutable del convertidor manualmente, abrir Editar → Preferencias → Importación-Exportación → DWG y llenar \"Camino al convertidor de archivos de Teigha\" apropiadamente.

## LazyLoader

LazyLoader is a python module that allows deferred loading, while still importing at the top of the script. This is useful if you are importing another module that is slow, and it is used several times throughout the script. Using LazyLoader can improve workbench startup times, but the module will still need to be loaded on first use.

### Instalación 

LazyLoader está incluido en FreeCAD v0.19

### Uso 

Necesitarás importar LazyLoader, y luego cambiar la importación de cualquier módulo que quieras que sea aplazado.


```python
from lazy_loader.lazy_loader import LazyLoader
Part = LazyLoader('Part', globals(), 'Part')
```

La variable Part es como se nombra el módulo en su guión. Puedes replicar \"importar Part como P\" cambiando la variable.


```python
P = LazyLoader('Part', globals(), 'Part')
```

You can also import a module from a package. 
```python
utils = LazyLoader('PathScripts', globals(), 'PathScripts.PathUtils')
``` You can\'t import individual functions, just entire modules.

### Enlaces 

-   Fuente original: <https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/util/lazy_loader.py>
-   Explicación más detallada: <https://wil.yegelwel.com/lazily-importing-python-modules/>
-   Código dentro del código fuente de FreeCAD: <https://github.com/FreeCAD/FreeCAD/tree/master/src/3rdParty/lazy_loader>
-   Discusión en el foro: <https://forum.freecadweb.org/viewtopic.php?f=10&t=45298>


<div class="mw-translate-fuzzy">





</div>


 

_ _

---
[documentation index](../README.md) > [Python Code](Category_Python Code.md) > Extra python modules/es
