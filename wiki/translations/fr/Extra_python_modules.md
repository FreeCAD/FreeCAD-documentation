# Extra python modules/fr
## Présentation

Cette page contient plusieurs modules Python supplémentaires ou d\'autres bouts de code qui peuvent être téléchargés gratuitement sur Internet, et ajouter des fonctionnalités à votre installation de FreeCAD.



## PySide

-   [Page officielle PySide](https://contribute.qt-project.org/wiki/PySide)
-   Licence : LGPL
-   Optionnel, plusieurs modules sont nécessaires et d\'autres modules peuvent être ajoutés : Draft, BIM, Ship, Plot, OpenSCAD, Spreadsheet

PySide est requise par tous les modules de FreeCAD et pour accéder à l\'interface Qt de FreeCAD. Il est déjà livré dans dans les versions FreeCAD, et est généralement installé automatiquement par FreeCAD sur Linux, l\'installation peut se faire à partir des dépôts officiels. Si ces modules (Draft, BIM, etc) sont activés après l\'installation de FreeCAD, cela signifie que PySide (auparavant PyQt) est déjà installé, et vous n\'avez pas besoin de faire quoi que ce soit de plus.

**Remarque :** FreeCAD s\'est progressivement éloigné de PyQt après la version 0.13, en faveur de [PySide](http://qt-project.org/wiki/PySide), qui fait exactement le même travail mais a une licence (LGPL) plus compatible avec FreeCAD.



### Installation

#### Linux

La manière la plus simple d\'installer PySide est de passer par le gestionnaire de paquets de votre distribution. Sur les systèmes Debian/Ubuntu, le nom du paquet est généralement *python-PySide*, tandis que sur les systèmes basés sur RPM, il est nommé *pyside*. Les dépendances nécessaires (Qt et SIP) seront prises en charge automatiquement.

#### Windows

Le programme peut être téléchargé à partir \[<http://qt-project.org/wiki/Category:LanguageBindings>::PySide::Downloads PySide Downloads\]. Vous aurez besoin d\'installer les bibliothèques Qt et SIP avant d\'installer PySide (à documenter).

#### MacOS

PySide sur Mac peut être installé via homebrew ou port. Voir [Installation des dépendances](Compile_on_MacOS/fr#Installation_des_dépendances.md).



### Utilisation

Une fois installé, vous pouvez vérifier que tout fonctionne en tapant dans la console Python de FreeCAD :


```python
import PySide
```

Pour accéder à l\'interface de FreeCAD, tapez :


```python
from PySide import QtCore,QtGui
FreeCADWindow = FreeCADGui.getMainWindow()
```

Vous pouvez maintenant commencer à explorer l\'interface avec la commande dir(). Vous pouvez ajouter de nouveaux éléments, comme un widget personnalisé, avec des commandes comme :


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



### Documentation complémentaire 

-   [Site de la documentation officielle de Qt](https://doc.qt.io/qt.html#qtforpython)

## Pivy

-   Page d\'accueil : [<https://www.coin3d.org/>](https://www.coin3d.org/)
-   Licence : BSD
-   Optionnel mais nécessaire pour plusieurs modules de FreeCAD : Draft, BIM

Pivy est un module nécessaire pour accéder à la vue 3D de FreeCAD. Sous Windows, Pivy est déjà inclus dans le programme d\'installation de FreeCAD, et sous Linux, il est généralement installé automatiquement lorsque vous installez FreeCAD à partir d\'un dépôt officiel. Sur macOS, malheureusement, vous devrez compiler Pivy vous-même.

### Installation 



#### Prérequis

Je pense qu\'avant de compiler Pivy, vous devrez installer Coin et SoQt.

J\'ai constaté que pour construire sur Mac, il suffisait d\'installer le [Coin3 binaire](http://www.coin3d.org/lib/plonesoftwarecenter_view). Tenter d\'installer Coin à partir de MacPorts s\'est avéré problématique : j\'ai essayé d\'ajouter un grand nombre de paquets X Windows et j\'ai fini par me planter avec une erreur de script.

Pour Fedora, j\'ai trouvé un RPM avec Coin3.

SoQt compilé à partir de la [source](http://www.coin3d.org/lib/soqt/releases/1.5.0) fonctionne bien sur Mac et Linux.

#### Debian & Ubuntu 

À partir de Debian Squeeze et Ubuntu Lucid, pivy sera disponible directement depuis les dépôts officiels, ce qui nous évitera bien des tracas. En attendant, vous pouvez soit télécharger l\'un des paquets que nous avons mis à disposition (pour Debian et Ubuntu Karmic) sur les pages de [téléchargements](Download/fr.md), soit le compiler vous-même.

La meilleure façon de compiler pivy facilement est de récupérer le paquet source debian pour pivy et de faire un paquet avec debuild. Il s\'agit du même code source que celui du site officiel de pivy, mais les gens de debian ont fait plusieurs ajouts pour corriger des bogues. Il se compile également très bien sur ubuntu karmic : <http://packages.debian.org/squeeze/python-pivy> téléchargez le fichier .orig.gz et le fichier .diff.gz, puis décompressez les deux, et appliquez le .diff au source : allez dans le dossier source décompressé de pivy, et appliquez le patch .diff :


```python
patch -p1 < ../pivy_0.5.0~svn765-2.diff
```

alors


```python
debuild
```

pour que pivy soit correctement intégré dans un paquetage installable officiel. Ensuite, il suffit d\'installer le paquet avec gdebi.



#### Autres distributions Linux 

D\'abord, téléchargez les dernières sources du [dépôt du projet](https://github.com/coin3d/pivy) :

Informations à ajouter.

En Mars 2012, la dernière version était pivy-0.5.

Ensuite, vous avez besoin d\'un outil appelé SWIG pour générer le code C++ pour les liaisons Python. Pivy-0.5 indique qu\'il n\'a été testé qu\'avec SWIG 1.3.31, 1.3.33, 1.3.35, et 1.3.40. Vous pouvez donc télécharger une archive des sources pour l\'une de ces anciennes versions à partir de [<http://www.swig.org>](http://www.swig.org). Ensuite, décompressez-la et, à partir d\'une ligne de commande, faites (en tant que root) :


```python
./configure
make
make install (or checkinstall if you use it)
```

Il faut quelques secondes pour la compilation.

Vous pouvez également essayer de compiler avec un SWIG plus récent. Depuis mars 2012, une version standard du dépôt est la 2.0.4. Pivy a un problème mineur de compilation avec SWIG 2.0.4 sur macOS (voir ci-dessous) mais semble se compiler correctement sur Fedora Core 15.

Ensuite, allez dans les sources de Pivy et tapez :


```python
python setup.py build
```

ce qui crée les fichiers sources. Notez que la compilation peut produire des milliers d\'avertissements, mais avec un peu de chance, il n\'y aura pas d\'erreurs.

C\'est probablement obsolète, mais vous pouvez rencontrer une erreur du compilateur lorsqu\'un \"const char\*\" ne peut pas être converti en un \"char\*\". Pour corriger cela, il suffit d\'écrire un \"const\" avant dans les lignes appropriées. Il y a six lignes à corriger.

Après cela, installez (en tant que root) :


```python
python setup.py install (or checkinstall python setup.py install)
```

Ça y est, pivy est installé.

#### MacOS 

Ces instructions peuvent ne pas être complètes. Quelque chose d\'approchant a fonctionné pour OS 10.7 à partir de mars 2012. J\'utilise MacPorts pour les dépôts, mais d\'autres options devraient également fonctionner.

En ce qui concerne linux, téléchargez les dernières sources :


```python
hg clone http://hg.sim.no/Pivy/default Pivy
```

Si vous n\'avez pas hg, vous pouvez l\'obtenir sur MacPorts :


```python
port install mercurial
```

Ensuite, comme ci-dessus, vous avez besoin de SWIG. Il devrait s\'agir d\'une question de :


```python
port install swig
```

J\'ai trouvé que j\'avais besoin aussi de faire :


```python
port install swig-python
```

En mars 2012, MacPorts SWIG est en version 2.0.4. Comme indiqué ci-dessus pour linux, il est préférable de télécharger une version plus ancienne. SWIG 2.0.4 semble avoir un bug qui arrête la construction de Pivy. Voir le premier message de ce [digest](https://sourceforge.net/mailarchive/message.php?msg_id=28114815).

Cela peut être corrigé en modifiant les deux sources pour ajouter des déréférences : \*arg4, \*arg5 à la place de arg4, arg5. Maintenant nous pouvons compiler Pivy :


```python
python setup.py build
sudo python setup.py install
```

#### Windows 

Si vous utilisez Visual Studio 2005 ou une version ultérieure, vous devez ouvrir une fenêtre de commande en cliquant sur \"Visual Studio 2005 Command prompt\" dans le menu Outils. Si l\'interpréteur Python ne se trouve pas encore dans le chemin d\'accès du système, procédez comme suit


```python
set PATH=path_to_python_3.x;%PATH%
```

Pour faire fonctionner pivy, vous devez obtenir les dernières sources depuis le dépôt du projet :

Informations à ajouter.

Ensuite, vous avez besoin d\'un outil appelé SWIG pour générer le code C++ pour les liaisons Python. Il est recommandé d\'utiliser la version 1.3.25 de SWIG, et non la dernière version, car pour l\'instant, pivy ne fonctionne correctement qu\'avec la version 1.3.25. Téléchargez les binaires pour la version 1.3.25 à partir de [<http://www.swig.org>](http://www.swig.org). Décompressez-les et ajoutez-les au chemin d\'accès du système à partir de la ligne de commande


```python
set PATH=path_to_swig_1.3.25;%PATH%
```

et définir le chemin approprié de COINDIR :


```python
set COINDIR=path_to_coin
```

Sous Windows, le fichier de configuration de pivy prévoit par défaut SoWin au lieu de SoQt. Je n\'ai pas trouvé de moyen évident de construire avec SoQt, j\'ai donc modifié le fichier setup.py directement. A la ligne 200, il suffit de supprimer la partie \"sowin\" : (\"gui.\_sowin\", \"sowin-config\", \"pivy.gui.\") (ne pas supprimer la parenthèse fermante).

Ensuite, allez dans les sources de Pivy et tapez :


```python
python setup.py build
```

qui crée les fichiers sources. Il se peut que vous rencontriez une erreur du compilateur, plusieurs fichiers d\'en-tête n\'ayant pu être trouvés. Dans ce cas, ajustez la variable INCLUDE


```python
set INCLUDE=%INCLUDE%;path_to_coin_include_dir
```

et si les en-têtes SoQt ne sont pas au même endroit que les en-têtes Coin également


```python
set INCLUDE=%INCLUDE%;path_to_soqt_include_dir
```

et enfin les en-têtes Qt


```python
set INCLUDE=%INCLUDE%;path_to_pyside\include\Qt
```

Si vous utilisez Express Edition of Visual Studio, il se peut que vous obteniez une exception Python keyerror. Dans ce cas, vous devez modifier quelques éléments du fichier msvccompiler.py situé dans votre installation Python.

Aller à la ligne 122 et remplacez la ligne :


```python
vsbase = r"Software\Microsoft\VisualStudio\%0.1f" % version
```

par


```python
vsbase = r"Software\Microsoft\VCExpress\%0.1f" % version
```

Réessayez ensuite. Si vous obtenez une deuxième erreur du type


```python
error: Python was built with Visual Studio 2003;...
```

vous devez également remplacer la ligne 128


```python
self.set_macro("FrameworkSDKDir", net, "sdkinstallrootv1.1")
```

par


```python
self.set_macro("FrameworkSDKDir", net, "sdkinstallrootv2.0")
```

Réessayez une nouvelle fois. Si vous obtenez à nouveau une erreur du type


```python
error: Python was built with Visual Studio version 8.0, and extensions need to be built with the same version of the compiler, but it isn't installed.
```

Vous devez alors vérifier les variables d\'environnement DISTUTILS_USE_SDK et MSSDK avec


```python
echo %DISTUTILS_USE_SDK%
echo %MSSDK%
```

S\'il n\'est pas encore arrangé, il suffit de le définir, par exemple à 1.


```python
set DISTUTILS_USE_SDK=1
set MSSDK=1
```

Il se peut que vous rencontriez une erreur du compilateur lorsqu\'un \"const char\*\" ne peut pas être converti en \"char\*\". Pour corriger cette erreur, il suffit d\'écrire un \"const\" avant les lignes appropriées. Il y a six lignes à corriger. Après cela, copiez le répertoire pivy généré à un endroit où l\'interpréteur Python de FreeCAD peut le trouver.



### Utilisation 

Pour vérifier si Pivy est correctement installé :


```python
import pivy
```

Pour avoir accès à Pivy à partir de la scénographique de FreeCAD, procédez comme ceci :


```python
from pivy import coin
App.newDocument() # Open a document and a view
view = Gui.ActiveDocument.ActiveView
FCSceneGraph = view.getSceneGraph() # returns a pivy Python object that holds a SoSeparator, the main "container" of the Coin scenegraph
FCSceneGraph.addChild(coin.SoCube()) # add a box to scene
```

Vous pouvez maintenant explorer le FCSceneGraph à l\'aide de la commande dir().



### Documentation complémentaire 

Malheureusement, la documentation sur pivy est encore presque inexistante sur le net. Mais vous pourriez trouver la documentation Coin utile, puisque pivy traduit simplement les fonctions de Coin, les noeuds et les méthodes en Python, tout en gardant le même nom et les mêmes propriétés, en gardant à l\'esprit la différence de syntaxe entre le C et Python :

-   <https://github.com/coin3d/coin/wiki/Documentation> - Coin3D API Reference
-   <http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/index.html> - The Inventor Mentor - La \"bible\" de Inventor langage de description de scène.

Vous pouvez également consulter le fichier Draft.py dans le dossier FreeCAD Mod/Draft, car il utilise beaucoup pivy.

## pyCollada

-   Page d\'accueil : <https://pycollada.github.io>
-   Licence : BSD
-   Optionnel, nécessaire pour permettre l\'importation et l\'exportation de fichiers Collada (.DAE)

pyCollada est une bibliothèque Python qui permet aux programmes de lire et d\'écrire des fichiers [Collada (\*.DAE)](https://fr.wikipedia.org/wiki/Collaborative_Design_Activity). Lorsque pyCollada est installé sur votre système, FreeCAD sera en mesure de gérer l\'importation et l\'exportation dans le format de fichier Collada.



### Installation 

#### Linux 


```python
sudo apt-get install python3-collada
```

Vous pouvez vérifier si pycollada a été correctement installé en émettant dans une console Python :


```python
import collada
```

S\'il ne renvoie rien (pas de message d\'erreur), tout va bien.



#### AppImages et Snaps Linux 

Collez ce code dans la [console Python](Python_console/fr.md) :


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

Pycollada est inclus sur Windows depuis la version 0.15 et dans les versions de développement de FreeCAD, donc aucune étape supplémentaire n\'est nécessaire.

#### MacOS 

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
$ pip install --target="/Applications/FreeCAD.app/Contents/lib/python3.x/site-packages" pycollada
```

ou après avoir téléchargé le code pycollada


```python
$ export PYTHONPATH=/Applications/FreeCAD\ 0.16.6706.app/Contents/lib/python3.x/site-packages:$PYTHONPATH
$ python setup.py install --prefix=/Applications/FreeCAD\ 0.2x.yyyy.app/Contents
```

## IfcOpenShell

-   Page d\'accueil : <http://www.ifcopenshell.org>
-   Licence : LGPL
-   Optionnel, nécessaire pour étendre les capacités d\'importation des fichiers IFC

IFCOpenShell est une bibliothèque en cours de développement qui permet d\'importer (et bientôt d\'exporter) des fichiers [IFC](http://fr.wikipedia.org/wiki/Industry_Foundation_Classes). IFC est une extension du format STEP et devient la norme dans les flux de travail [BIM](http://fr.wikipedia.org/wiki/Building_Information_Modeling). Lorsque ifcopenshell est correctement installé sur votre système, l\'[atelier BIM](BIM_Workbench/fr.md) de FreeCAD le détecte et l\'utilise pour importer des fichiers IFC, au lieu de son importateur rudimentaire intégré. Comme ifcopenshell est basé sur OpenCasCade, comme FreeCAD, la qualité de l\'importation est très élevée, produisant une géométrie solide de haute qualité.



### Installation 

#### Linux 

Les instructions d\'installation sont disponibles [ici](https://docs.ifcopenshell.org/ifcopenshell-python/installation.html).

Vous pouvez vérifier que ifcopenshell a été correctement installé en lançant une commande dans une console Python :


```python
import ifcopenshell
```

Si la commande ne retourne aucun message d\'erreur, alors tout est OK.



#### Windows et macOS 

IfcOpenShell est inclus à la fois dans la version de FreeCAD et dans les versions pour développeurs, de sorte qu\'aucune étape supplémentaire n\'est nécessaire.



### Liens

Tutoriel [Importer/Exporter IFC - compiler IfcOpenShell](Import/Export_IFC_-_compiling_IfcOpenShell/fr.md)

## LazyLoader

LazyLoader est un module Python qui permet un chargement différé, tout en continuant à importer en haut du script. C\'est utile si vous importez un autre module qui est lent et qui est utilisé plusieurs fois dans le script. L\'utilisation de LazyLoader peut améliorer les temps de démarrage d\'un atelier mais le module devra toujours être chargé lors de la première utilisation.



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

-   Source d\'origine : <https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/util/lazy_loader.py>
-   Plus d\'explications : <https://wil.yegelwel.com/lazily-importing-python-modules/>
-   Code dans le code source de FreeCAD : <https://github.com/FreeCAD/FreeCAD/tree/master/src/3rdParty/lazy_loader>
-   Discussion du forum : <https://forum.freecadweb.org/viewtopic.php?f=10&t=45298>



---
⏵ [documentation index](../README.md) > [Python Code](Category_Python%20Code.md) > [Developer Documentation](Category_Developer%20Documentation.md) > Extra python modules/fr
