# Extra python modules/fr
{{TOCright}}

## Présentation

Cette page contient plusieurs modules python supplémentaires ou d\'autres bouts de code qui peuvent être téléchargés gratuitement sur Internet, et ajouter des fonctionnalités à votre installation de FreeCAD.

## PySide (précédemment PyQt4) 

-   page officielle (PySide): [<http://qt-project.org/wiki/PySide>](http://qt-project.org/wiki/PySide)
-   licence: LGPL
-   option, plusieurs modules sont nécessaires et d\'autres modules peuvent être ajoutés : Draft, Arch, Ship, Plot, OpenSCAD, Spreadsheet

PySide (auparavant PyQt) est requise par tous les modules de FreeCAD et pour accéder à l\'interface Qt de FreeCAD. Il est déjà livré dans dans les versions FreeCAD, et est généralement installé automatiquement par FreeCAD sur Linux, l\'installation peut se faire à partir des dépôts officiels. Si ces modules (Draft, Arch, etc) sont activés après l\'installation de FreeCAD, cela signifie que PySide (auparavant PyQt) est déjà installé, et vous n\'avez pas besoin de faire quoi que ce soit de plus.

**Remarque :** PyQt4 va devenir progressivement obsolète dans FreeCAD, après la version 0.13, la préférence ira sur [PySide](http://qt-project.org/wiki/PySide), qui fait exactement le même travail, mais dispose d\'une licence (**LGPL**) plus compatible avec FreeCAD.

### Installation

#### Linux

La façon la plus simple d\'installer PySide est de l\'installer par le biais du gestionnaire de paquets de votre distribution. Sur les systèmes Debian / Ubuntu, le nom du package est généralement **python-PySide**, tandis que sur les systèmes basés sur RPM il est nommé **Pyside**. Les dépendances nécessaires (Qt et SIP) seront pris en charge automatiquement.

#### Windows

Le programme peut être téléchargé à partir \[<http://qt-project.org/wiki/<img src="images/Property.png" style="width:16px"> LanguageBindings>::PySide::Downloads PySide Downloads\]. Vous aurez besoin d\'installer les bibliothèques Qt et SIP avant d\'installer PySide (à documenter).

#### MacOSX

PyQt pour Mac doit être installé via homebrew ou port. Pour plus d\'informations voir [Installation des dépendances](Compile_on_MacOS/fr#Installation_des_dépendances.md).

### Utilisation

Une fois installé, vous pouvez vérifier le bon fonctionne de l\'installation, en tapant dans la console **Python** de FreeCAD :


```python
import PySide
```

Pour accéder à l\'interface de FreeCAD, tapez :


```python
from PySide import QtCore,QtGui
FreeCADWindow = FreeCADGui.getMainWindow()
```

Maintenant, vous pouvez commencer l\'exploration de l\'interface avec la commande **dir()**. Vous pouvez ajouter de nouveaux éléments, comme un widget personnalisé, avec des commandes comme :


```python
FreeCADWindow.addDockWidget(QtCore.Qt.RghtDockWidgetArea,my_custom_widget)
```

Travailler avec Unicode :


```python
text = text.encode('utf-8')
```

Travailler avec QFileDialog et OpenFileName :


```python
path = FreeCAD.ConfigGet("AppHomePath")
#path = FreeCAD.ConfigGet("UserAppData")
OpenName, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Read a txt file", path, "*.txt")
```

Travailler avec QFileDialog et SaveFileName :


```python
path = FreeCAD.ConfigGet("AppHomePath")
#path = FreeCAD.ConfigGet("UserAppData")
SaveName, Filter = PySide.QtGui.QFileDialog.getSaveFileName(None, "Save a file txt", path, "*.txt")
```

### Exemple de transition de PyQt4 vers PySide 

PS: ces exemples d\'erreurs ont été trouvées dans la transition de PyQt4 à PySide et ces corrections ont été faites, d\'autres solutions sont certainement disponibles avec les exemples ci-dessus


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

Pour accéder à l\'interface FreeCAD, tapez: Vous pouvez ajouter de nouveaux éléments, comme un widget personnalisé, avec des commandes comme :


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

Travailler avec Unicode :


```python
try:
    text = unicode(text, 'ISO-8859-1').encode('UTF-8')  # PyQt4
except Exception:
    text = text.encode('utf-8')                         # PySide
```

Travailler avec QFileDialog et OpenFileName :


```python
OpenName = ""
try:
    OpenName = QFileDialog.getOpenFileName(None,QString.fromLocal8Bit("Lire un fichier FCInfo ou txt"),path,"*.FCInfo *.txt") # PyQt4
except Exception:
    OpenName, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Lire un fichier FCInfo ou txt", path, "*.FCInfo *.txt")#PySide
```

Travailler avec QFileDialog et SaveFileName :


```python
SaveName = ""
try:
    SaveName = QFileDialog.getSaveFileName(None,QString.fromLocal8Bit("Sauver un fichier FCInfo"),path,"*.FCInfo") # PyQt4
except Exception:
    SaveName, Filter = PySide.QtGui.QFileDialog.getSaveFileName(None, "Sauver un fichier FCInfo", path, "*.FCInfo")# PySide
```

Travailler avec MessageBox:


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

Travailler avec setProperty (PyQt4) et setValue (PySide)


```python
self.doubleSpinBox.setProperty("value", 10.0)  # PyQt4
```

remplacer par :


```python
self.doubleSpinBox.setValue(10.0)  # PySide
```

Travailler avec setToolTip


```python
self.doubleSpinBox.setToolTip(_translate("MainWindow", "Coordinate placement Axis Y", None))  # PyQt4
```

remplacer par :


```python
self.doubleSpinBox.setToolTip(_fromUtf8("Coordinate placement Axis Y"))  # PySide 
```

ou


```python
self.doubleSpinBox.setToolTip(u"Coordinate placement Axis Y.")# PySide
```

### Documentation

Plus de tutoriels sur **PyQt4** (y compris sur la façon de construire des interfaces avec **Qt Designer** pour utiliser avec Python):

-   [API PyQt4](http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/classes.html) - La référence officielle sur l**\'API de PyQt4**

-   [Introduction PyQt4](http://www.rkblog.rk.edu.pl/w/p/introduction-pyqt4/)- une simple introduction.

-   [un tutoriel](http://www.zetcode.com/tutorials/pyqt4/) - vraiment complet.

## Pivy

-   homepage: [<https://bitbucket.org/Coin3D/coin/wiki/Home>](https://bitbucket.org/Coin3D/coin/wiki/Home)
-   license: BSD
-   option, utilisé par tous les modules de FreeCAD: Draft, Arch

Pivy a besoin de plusieurs modules pour accéder à la vue 3D de FreeCAD. Pour les fenêtres, pivy est déjà fourni dans l\'installateur de FreeCAD pour Linux, il est généralement installé automatiquement lorsque vous installez FreeCAD partir d\'un référentiel officiel. Sur MacOSX, malheureusement, vous aurez besoin de compiler Pivy vous même.

### Installation 

#### Prérequis

Je crois, qu\'avant de compiler **[Pivy](http://pivy.coin3d.org/)** vous devez avoir **[Coin](http://www.coin3d.org/)** et **[SoQt](http://www.coin3d.org/lib/soqt/releases/1.5.0)** d\'installés.

J\'ai trouvé que pour la compilation sur **Mac**, il suffisait d\'installer le **[Coin3 binary package](http://www.coin3d.org/lib/plonesoftwarecenter_view)**.
La tentative d\'installation de **Coin** sur **MacPorts** était problématique : j\'ai essayé d\'ajouter un grand nombre de paquets X Windows, et, finalement, tout c\'est terminé avec une erreur de script !

Pour Fedora, j\'ai trouvé un **RPM** avec **Coin3**.

**SoQt**, compilé à partir [des sources](http://www.coin3d.org/lib/soqt/releases/1.5.0) fonctionne très bien sur **Mac et Linux**.

#### Debian & Ubuntu 

Depuis **Debian Squeeze** et **Ubuntu Lucid**, **Pivy** est disponible directement à partir des dépôts officiels, et, nous permet d\'économiser beaucoup de tracas.
En attendant, vous pouvez soit télécharger l\'un des **packages** que nous avons fait (pour Debian et Ubuntu karmic), disponibles sur les pages de [téléchargements](Download/fr.md) , ou, vous pouvez le compiler vous-même.

La meilleure façon de compiler facilement **Pivy**, est de prendre le **debian source package** pour **Pivy**, et, faire un **package** avec **debuild**.
C\'est le même code source que sur le site officiel de **Pivy**, mais, les gens de **Debian** ont ajoutés plusieurs bug-fixing. Il compile également très bien sur : **[Ubuntu Karmic](http://packages.debian.org/squeeze/python-pivy)** \... télécharger **.orig.gz** et **.diff.gz**, décompressez le tout, puis appliquez **.diff** à la source :
allez dans le dossier source de **Pivy** décompressé, et appliquez le patch **.diff** :


```python
patch -p1 < ../pivy_0.5.0~svn765-2.diff
```

alors


```python
debuild
```

pour avoir **Pivy**, correctement compilé, avec un package officiellement installable. Ensuite, il suffit d\'installer le package avec **gdebi**.

#### Autres distributions Linux 

D\'abord, téléchargez les dernières sources du [project\'s repository](http://pivy.coin3d.org/mercurial/) :


```python
hg clone http://hg.sim.no/Pivy/default Pivy 
```

En Mars 2012, la dernière version était la **pivy-0.5**.

Ensuite, vous avez besoin d\'un outil appelé **SWIG** pour générer le code C++ pour les **Python bindings**. **Pivy-0.5** rapports qui a été testé seulement avec **SWIG 1.3.31, 1.3.33, 1.3.35 et 1.3.40**. Ainsi, vous pouvez télécharger une archive source pour l\'une de ces anciennes versions de [SWIG](http://www.swig.org).
Puis, décompressez-le, et, faites en ligne de commande (en tant que root) :


```python
./configure
make
make install (or checkinstall if you use it)
```

Il faut quelques secondes pour la compilation.

Alternativement, vous pouvez essayer avec une compilation plus récent **SWIG**. En Mars 2012, la version référentielle typique était **2.0.4**.
**Pivy** a un problème de compilation avec les versions inférieures **2.0.4** de **SWIG** sur Mac OS ([voir ci-dessous](#Mac_OS.md)), mais semble compiler correctement sur **Fedora Core 15**.

Après cela, allez dans le source **Pivy** et tapez :


```python
python setup.py build 
```

pour créer les fichiers sources. Notez que cette génération de fichiers peut produire des milliers de mises en garde, mais j\'espère qu\'il n\'y aura pas d\'erreurs.

Ceci est probablement obsolète, mais vous risquez de rencontrer une erreur de compilation, ou, un **\"const char\*\"** ne peut pas être converti en un **\"char\*\"**.
Pour corriger cela, il vous suffit d\'écrire une **\"const\"**, dans les lignes appropriées, avant la génération. Il y a six lignes à corriger.

Après cela, installez (en tant que root) :


```python
python setup.py install (or checkinstall python setup.py install)
```

Ça y est, pivy est installé.

#### Mac OS 

Ces instructions peuvent ne pas être complètes. Quelque chose plus ou moins comme cela a fonctionné pour **OS 10.7 de Mars 2012**. J\'utilise **[MacPorts](http://www.macports.org/)** pour les dépôts, mais d\'autres options devraient également fonctionner.

En ce qui concerne linux, téléchargez les dernières sources :


```python
hg clone http://hg.sim.no/Pivy/default Pivy 
```

Si vous n\'avez pas **hg**, vous pouvez l\'obtenir à partir **[MacPorts](http://www.macports.org/)** :


```python
port install mercurial
```

Puis, comme ci-dessus vous avez besoin **[SWIG](http://www.swig.org/)**.
Faites :


```python
port install swig
```

J\'ai trouvé que j\'avais besoin aussi de faire :


```python
port install swig-python
```

En Mars 2012, **MacPorts SWIG** est la version **2.0.4**. Comme il est indiqué ci-dessus pour Linux, il vaudrait mieux télécharger une version plus ancienne. **SWIG 2.0.4** semble avoir un bug qui empêche la compilation de **Pivy**.
Regardez le premier message dans ce : *[digest](https://sourceforge.net/mailarchive/message.php?msg_id=28114815)*

Cela peut être corrigé, en modifiant les 2 emplacements source et déréférencer : **\*arg4, \*arg5** à la place de **arg4, arg5**.
Maintenant nous pouvons compiler **Pivy**:


```python
python setup.py build
sudo python setup.py install
```

#### Windows 

En supposant que vous utilisiez **Visual Studio 2005** ou une version ultérieure, vous devrez ouvrir une invite de commande avec **Visual Studio 2005 Command prompt** dans le menu Outils.
Si l\'interpréteur **Python** n\'est pas encore dans le chemin système (PATH), faites :


```python
set PATH=path_to_python_2.5;%PATH%
```

Pour que **Pivy** soit fonctionnel, vous devriez télécharger les dernières sources à partir du référentiel du projet :


```python
svn co https://svn.coin3d.org/repos/Pivy/trunk Pivy 
```

Ensuite, vous avez besoin d\'un outil appelé [SWIG](http://www.swig.org/) pour générer le code C++ pour les **Python bindings**. Il est recommandé d\'utiliser la version **1.3.25 de SWIG**, pas la dernière version, parceque, **Pivy** ne fonctionne pas correctement avec la version **1.3.25**. Télécharger le binaire pour la version **1.3.25** de **[Swig](http://www.swig.org)**.
Puis décompressez-le et à partir de la ligne de commande, ajoutez le chemin (path) du système


```python
set PATH=path_to_swig_1.3.25;%PATH%
```

et définir le chemin approprié à **COINDIR** :


```python
set COINDIR=path_to_coin
```

Sous Windows, le fichier de configuration **Pivy** attend **SoWin** au lieu de **SoQt** par défaut. Je n\'ai pas trouvé de façon évidente pour compiler avec **SoQt**, alors, j\'ai modifié le fichier **setup.py** directement.
A la ligne 200 il suffit de retirer la partie **sowin** : **(\'gui.\_sowin\', \'sowin-config\', \'pivy.gui.\') (ne pas enlever la parenthèse fermante ! )**.

Après cela, allez dans le source de **pivy** et tapez :


```python
python setup.py build 
```

qui crée les fichiers source. Vous pouvez rencontrer une erreur de compilation, cause, **plusieurs fichiers d\'en-tête n\'ont pas été trouvés**.
Dans ce cas, réglez la variable **INCLUDE** comme ceci :


```python
set INCLUDE=%INCLUDE%;path_to_coin_include_dir
```

et si les en-têtes **soqt**, ne sont pas au même endroit que les en-têtes **Coin**, faites aussi ceci :


```python
set INCLUDE=%INCLUDE%;path_to_soqt_include_dir
```

et finalement, pour les en-têtes **Qt** faites :


```python
set INCLUDE=%INCLUDE%;path_to_qt4\include\Qt
```

Si vous utilisez **Express Edition of Visual Studio**, vous pouvez obtenir une exception **Python keyerror**.
Dans ce cas, vous devez modifier de petites choses dans **msvccompiler.py**, qui se trouve, dans votre installation Python.

Aller à la ligne 122 et remplacez la ligne :


```python
vsbase = r"Software\Microsoft\VisualStudio\%0.1f" % version
```

par


```python
vsbase = r"Software\Microsoft\VCExpress\%0.1f" % version
```

Puis réessayez.
Si vous obtenez une deuxième erreur comme :


```python
error: Python was built with Visual Studio 2003;...
```

vous devez également remplacer la ligne 128 comme ceci :


```python
self.set_macro("FrameworkSDKDir", net, "sdkinstallrootv1.1")
```

par


```python
self.set_macro("FrameworkSDKDir", net, "sdkinstallrootv2.0")
```

Réessayez encore une fois.
Si vous obtenez de nouveau une erreur comme :


```python
error: Python was built with Visual Studio version 8.0, and extensions need to be built with the same version of the compiler, but it isn't installed.
```

alors vous devriez vérifier les variables d\'environnement **DISTUTILS\_USE\_SDK** et **MSSDK** avec :


```python
echo %DISTUTILS_USE_SDK%
echo %MSSDK%
```

Si ce n\'est pas toujours pas arrangé, il suffit de définir à 1 :


```python
set DISTUTILS_USE_SDK=1
set MSSDK=1
```

Maintenant, vous pouvez rencontrer une erreur de compilation, ou un **const char\*** ne peut pas être converti en un **char\***.
Pour corriger cela il vous suffit d\'écrire un **const** avant, dans les lignes appropriées, il y a six lignes à corriger.
Après copiez le répertoire généré par **Pivy** dans un endroit où l\'interpréteur **Python** de FreeCAD peut le trouver.

### Utilisation 

Pour vérifier si pivy est correctement installé :


```python
import pivy
```

Pour avoir accès à Pivy à partir de la scénographique de FreeCAD, procédez comme ceci:


```python
from pivy import coin
App.newDocument() # Open a document and a view 
view = Gui.ActiveDocument.ActiveView 
FCSceneGraph = view.getSceneGraph() # returns a pivy Python object that holds a SoSeparator, the main "container" of the Coin scenegraph
FCSceneGraph.addChild(coin.SoCube()) # add a box to scene 
```

Vous pouvez maintenant explorer la **FCSceneGraph** avec la commande **dir()**.

### Documentation 

Malheureusement, la documentation sur **Pivy** est \"pour le moment\" presque inexistante sur le net. Mais vous pouvez trouver de la documentation très utile sur **Coin**, car **Pivy** a simplement traduit les fonctions, **Coin**, des nœuds et des méthodes en **Python**, les noms sont conservés (mêmes noms) ainsi que les propriétés ne sont différentes que par la syntaxe entre le **C** et **Python** :

-   <https://bitbucket.org/Coin3D/coin/wiki/Documentation> - Coin3D API Reference
-   <http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/index.html> - The Inventor Mentor - La \"bible\" de Inventor langage de description de scène.

Vous pouvez également consulter le fichier **Draft.py** dans le dossier **FreeCAD Mod/Draft**, car **Pivy** est fortement utilisé.

## pyCollada

-   homepage: <http://pycollada.github.com>
-   license: BSD
-   option, est nécessaire pour permettre l\'importation et l\'exportation de fichiers Collada (.DAE)

**[pyCollada](http://pycollada.github.com)** est une bibliothèque **Python** qui permet aux programmes de lire et d\'écrire des fichiers **[Collada (\*.DAE)](http://en.wikipedia.org/wiki/COLLADA)**. Lorsque **pyCollada** est installé sur votre système, FreeCAD (<small>(v0.13)</small> ) le détecte et ajoute les options d\'importation et d\'exportation, qui permettent l\'ouverture et l\'enregistrement de fichiers au format **Collada**.

### Installation 

**Pycollada** n\'est généralement pas encore disponible dans les dépôts des distributions Linux, mais puisqu\'il est fait uniquement en **Python**, il ne nécessite pas de compilation, et est facile à installer.
Vous avez 2 façons de l\'installer, soit directement à partir du **pycollada git repository** officiel, ou avec l\'outil **easy\_install**.

#### Linux 

Dans les deux cas, vous aurez besoin des paquetages suivants, installés d\'avance sur votre système :


```python
python-lxml 
python-numpy
python-dateutil
```

##### Depuis le dépôt git (pycollada git repository) 


```python
git clone git://github.com/pycollada/pycollada.git pycollada
cd pycollada
sudo python setup.py install
```

##### Avec easy\_install (easy\_install) 

En supposant que vous avez déjà installé complètement **Python**, l\'utilitaire **easy\_install** doit être déjà présent :


```python
easy_install pycollada
```

Vous devez vous assurer que **pycollada**, est correctement installé, en utilisant la commande suivante dans la console Python :


```python
import collada
```

Si la commande ne retourne aucun message d\'erreur, alors tout est OK.

#### Windows 

Pycollada est inclus sur Windows depuis la version 0.15 et dans les versions de développement de FreeCAD, donc aucune étape supplémentaire n\'est nécessaire.

#### Mac OS 

Si vous utilisez l\'accumulation des Homebrew FreeCAD vous pouvez installer pycollada dans votre système Python en utilisant pip.

Si vous devez installer pip:


```python
$ sudo easy_install pip
```

Installer pycollada:


```python
$ sudo pip install pycollada
```

Si vous utilisez une version binaire de FreeCAD, vous pouvez dire pip installez pycollada dans le site-packages à l\'intérieur FreeCAD.app:


```python
$ pip install --target="/Applications/FreeCAD.app/Contents/lib/python2.7/site-packages" pycollada
```

ou après avoir téléchargé le code pycollada


```python
$ export PYTHONPATH=/Applications/FreeCAD\ 0.16.6706.app/Contents/lib/python2.7/site-packages:$PYTHONPATH
$ python setup.py install --prefix=/Applications/FreeCAD\ 0.16.6706.app/Contents
```

## IfcOpenShell

-   homepage: <http://www.ifcopenshell.org>
-   license: LGPL
-   option, requis pour étendre les capacités d\'importation de fichiers IFC

IFCOpenShell, est une bibliothèque actuellement en développement, ce qui permet d\'importer (et bientôt d\'exporter) [Industry foundation Classes (\*.Fichiers IFC)](http://fr.wikipedia.org/wiki/Industry_Foundation_Classes). Ceci est une extension pour le format [STEP](http://fr.wikipedia.org/wiki/Standard_pour_l%27%C3%A9change_de_donn%C3%A9es_de_produit) et devient la norme dans les workflows [BIM](http://fr.wikipedia.org/wiki/Building_Information_Modeling). Lorsque **ifcopenshell** est correctement installé sur votre système, l\'**![](images/)_[atelier_Arch](Arch_Workbench/fr.md)** de FreeCAD le détectera et l\'utilisera pour importer des fichiers **IFC**. Étant donné qu**\'ifcopenshell** est basé sur OpenCasCade, comme FreeCAD, la qualité de l\'importation est très élevée, en produisant une géométrie de solides de haute qualité.

### Installation 

Étant donné que **\'ifcopenshell** est assez nouveau, vous devrez probablement le compiler vous-même.

#### Linux 

Vous aurez besoin de deux ou trois paquets de développement, installés sur votre système afin de rassembler les ifcopenshell :


```python
liboce-*-dev
python-dev
swig
```

mais, étant donné que FreeCAD exige tout, vous pouvez compiler FreeCAD, vous n\'aurez aucune dépendance supplémentaire pour compiler IfcOpenShell.

Prenez le dernier code source ici :


```python
git clone https://github.com/IfcOpenShell/IfcOpenShell.git
```

Le processus de création est très simple :


```python
mkdir ifcopenshell-build
cd ifcopenshell-build
cmake ../IfcOpenShell/cmake
```

ou, si vous utilisez **oce** au lieu d**\'opencascade** :


```python
cmake -DOCC_INCLUDE_DIR=/usr/include/oce ../ifcopenshell/cmake 
```

Étant donné que **ifcopenshell** est fait principalement pour [Blender](http://www.blender.org/), il utilise **python3** par défaut. Pour l\'utiliser à l\'intérieur de FreeCAD, vous devez le compiler avec la même version de Python qui est utilisé dans FreeCAD. Vous devrez peut-être forcer les paramètres avec la version de **Python** et **cmake** (réglez la version de Python avec la vôtre) :


```python
cmake -DOCC_INCLUDE_DIR=/usr/include/oce -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 -DPYTHON_LIBRARY=/usr/lib/python2.7.so ../ifcopenshell/cmake
```

Alors :


```python
make
sudo make install
```

Vous pouvez vérifier que **ifcopenshell**, a été correctement installé en tapant dans la console Python :


```python
import ifcopenshell
```

Si la commande ne retourne aucun message d\'erreur, alors tout est OK.

#### Windows 

**Note**: les installateurs officiels FreeCAD obtenus à partir de la page du site Web/github de FreeCAD contiennent déjà ifcopenshell.

\'\' Documentation copiée à partir du fichier README IfcOpenShell\'\'

Les utilisateurs sont priés d\'utiliser le fichier **.sln** de Visual Studio qui se trouve dans **win/folder**.

Pour les utilisateurs de Windows une version pré-construite Open CASCADE est disponible sur le site d\'[OpenCascade](http://opencascade.org). Téléchargez, et, installez cette version dans le chemin d\'accès d\'Open CASCADE, et, des fichiers de la bibliothèque de MS Visual Studio C++.

Pour créer le **IfcPython wrapper**, **SWIG** doit être installé. Téléchargez la dernière version de [swigwin](http://www.swig.org/download.html). Après avoir extrait le fichier **.zip**, veuillez ajouter le dossier à la variable **d\'environnement PATH**. Python doit être installé, veuillez fournir les chemins d\'accès des fichiers include, et, bibliothèque pour Visual Studio.

### Liens

Tutoriel [Import/Export IFC - compiling IfcOpenShell](Import/Export_IFC_-_compiling_IfcOpenShell.md)

### Installation 

S\'installe sur toutes les plateformes, par l\'installation du paquet approprié disponible à <https://www.opendesign.com/guestfiles/oda_file_converter>. Après l\'installation, si l\'utilitaire n\'est pas trouvé automatiquement par FreeCAD, vous devrez configurer manuellement le chemin de l\'exécutable du convertisseur via le menu Édition → Préférences → Importer-Exporter → DWG et renseignez le champs \"Chemin d'accès du convertisseur de fichier Teiga\".

## LazyLoader

LazyLoader est un module python qui permet un chargement différé tout en continuant d\'importer en haut du script. Ceci est utile si vous importez un autre module qui est lent et qu\'il est utilisé plusieurs fois dans le script. L\'utilisation de LazyLoader peut améliorer les temps de démarrage du plan de travail mais le module devra toujours être chargé lors de la première utilisation.

### Installation 

LazyLoader est inclus avec FreeCAD v0.19.

### Utilisation 

Vous devrez importer LazyLoader puis modifier l\'importation du module que vous souhaitez différer.


```python
from lazy_loader.lazy_loader import LazyLoader
Part = LazyLoader('Part', globals(), 'Part')
```

La variable Part est la façon dont le module est nommé dans votre script. Vous pouvez répliquer \"import Part as P\" (importer une pièce en P) en modifiant la variable.


```python
P = LazyLoader('Part', globals(), 'Part')
```

Vous pouvez également importer un module à partir d\'un package. 
```python
utils = LazyLoader('PathScripts', globals(), 'PathScripts.PathUtils')
``` Vous ne pouvez pas importer des fonctions individuelles, seulement des modules entiers.

### Liens 

-   Source d\'origine: <https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/util/lazy_loader.py>
-   Plus d\'explications: <https://wil.yegelwel.com/lazily-importing-python-modules/>
-   Code dans le code source de FreeCAD: <https://github.com/FreeCAD/FreeCAD/tree/master/src/3rdParty/lazy_loader>
-   Discussion du forum: <https://forum.freecadweb.org/viewtopic.php?f=10&t=45298>





 

[<img src="images/Property.png" style="width:16px"> Python Code](Category_Python_Code.md) [<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md)

---
[documentation index](../README.md) > [Python Code](Category_Python Code.md) > Extra python modules/fr
