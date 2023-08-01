# Dialog creation/fr
{{TOCright}}

## Introduction

Dans cette page, nous allons montrer comment construire une interface graphique simple avec [Qt Designer](http://qt-project.org/doc/qt-4.8/designer-manual.html), l\'outil officiel de Qt pour concevoir des interfaces. La boîte de dialogue sera convertie en code [Python](Python/fr.md) puis elle sera utilisée dans FreeCAD. Nous supposerons que l\'utilisateur sait comment éditer et exécuter [Python](Python/fr.md) en général.

Dans cet exemple, l\'interface entière est définie en [Python](Python/fr.md). Bien que cela soit possible pour les petites interfaces, pour les interfaces plus importantes, la recommandation est de charger les fichiers **.ui** créés directement dans le programme.

<img alt="" src=images/FreeCAD_creating_interfaces.svg  style="width:600px;"> 
*Deux méthodes générales pour créer des interfaces, en incluant l'interface dans le fichier Python, ou en utilisant des fichiers `.ui*.`

## Construire une boîte de dialogue 

Dans les applications de CAO, bien concevoir une **UI** (interface utilisateur) est très important. Tout ce que l\'utilisateur fera, se fera à travers un outil de l\'interface: la lecture des boîtes de dialogue, appuyer sur les boutons, le choix entre les icônes, etc . Il est donc très important de réfléchir attentivement à la conception de votre boîte de dialogue, comment vous voulez que l\'utilisateur se comporter avec la boîte, et comment sera le flux de travail de votre action.

Il y a une deux choses à savoir lors de la conception de l\'interface:
\* Boîtes de dialogue [modales ou non-modale](http://fr.wikipedia.org/wiki/Fenêtre_modale) :

-   -   Une boîte de dialogue **modale** apparaît en face de votre écran et, arrête l\'action de la fenêtre principale, forçant l\'utilisateur à répondre à la boîte de dialogue.
    -   Une boîte de dialogue **non modale** ne vous empêche pas de travailler sur la Fenêtre principale, vous pouvez travailler sur les deux fenêtres.

Dans certains cas, le premier est préférable, dans d\'autres cas non.

-   Identifier ce qui est nécessaire et ce qui est optionnel:
    \* Assurez-vous que l\'utilisateur sait ce qu\'il doit faire. Prévoyez des étiquettes avec des descriptions appropriées, des info-bulles d\'utilisation, etc . .
-   Séparez les commandes à partir de paramètres:
    \* Cela se fait habituellement avec des boutons et des champs de saisie de texte.
    \* L\'utilisateur sait que cliquer sur un bouton va produire une action, tout en changeant une valeur dans un champ de texte, va changer un paramètre quelque part. Cependant, aujourd\'hui, les utilisateurs savent généralement bien ce qu\'est un bouton, ce qu\'est un champ de saisie, etc . . .

La boîte à outils de l\'interface **Qt** que nous utilisons, est une boîte à outils **state-of-the-art** (interface graphique avancée), et nous n\'aurons pas beaucoup d\'inquiétudes pour rendre les choses claires, car elles sont déjà très claires par elles-mêmes.

Donc, maintenant que nous avons bien défini ce que nous ferons, il est temps d\'ouvrir **Qt Designer**.
Nous allons concevoir très facilement une simple boîte de dialogue, comme ceci:

![](images/Qttestdialog.jpg )

Nous allons ensuite utiliser cette boîte de dialogue dans FreeCAD pour produire une belle surface plane rectangulaire.
Vous ne trouverez peut-être pas très utile de produire de beaux plans rectangulaires, mais il sera facile de le changer plus tard et de faire des choses plus complexes.
Lorsque vous l\'ouvrez, Qt Designer ressemble à ceci:

![](images/Qtdesigner-screenshot.jpg )

## Création de la boîte de dialogue 

Qt Designer est très simple à utiliser. Sur la barre de gauche, vous avez des éléments qui peuvent être glissés sur votre widget. Sur le côté droit, vous avez des panneaux de propriétés affichant toutes sortes de propriétés modifiables des éléments sélectionnés. Commencez donc par créer un nouveau widget.

1.  Sélectionnez \"Dialog without buttons\" car nous ne voulons pas des boutons **OK**/**Cancel** par défaut.
2.  Nous avons besoin de *Labels*. Les étiquettes sont de simples chaînes de texte qui apparaissent sur votre widget pour informer l\'utilisateur final. Si vous sélectionnez une étiquette, notez que sur le côté droit apparaîtront plusieurs propriétés que vous pouvez modifier telles que: le style de police, la hauteur, etc \... Permet donc de faire glisser 3 étiquettes distinctes sur notre widget:
    -   Une étiquette pour le titre
    -   Une autre étiquette pour écrire \"**Height**\"
    -   Une autre étiquette pour écrire \"**Width**\"
3.  Nous avons maintenant besoin de LineEdits (2 d\'entre eux en fait). Faites-en glisser deux sur le widget. **LineEdits** sont des champs de texte que l\'utilisateur final peut remplir. Nous avons donc besoin d\'un LineEdit pour la *Height* et un pour la *Width*. Ici aussi, nous pouvons éditer les propriétés. Par exemple, pourquoi ne pas définir une valeur par défaut, par exemple: 1.00 pour chacun. De cette façon, lorsque l\'utilisateur verra la boîte de dialogue, les deux valeurs seront déjà remplies. Si l\'utilisateur final est satisfait, il peut appuyer directement sur le bouton, ce qui lui fait gagner un temps précieux.
4.  Ensuite, ajoutons un **PushButton**. Il s\'agit du bouton sur lequel l\'utilisateur final devra appuyer après avoir rempli les deux champs.

**Remarque:** nous avons choisi ici des commandes très simples. Qt a beaucoup plus d\'options, par exemple on pourrait utiliser **Spinboxes** au lieu de \'\' **LineEdits** etc \... Jetez un œil à ce qui est disponible, explorez \... vous aurez sûrement d\'autres idées .

C\'est à peu près tout ce que nous devons faire dans Qt Designer.
Une dernière chose, nous allons renommer tous nos éléments avec des noms faciles, de sorte qu\'il sera plus facile de les identifier dans nos scripts:

![](images/Qtpropeditor.jpg )

## Conversion de notre boîte de dialogue en code Python avec \"pyuic\" 

Maintenant, nous allons sauver notre widget quelque part. Il sera sauvegardé dans un fichier **.Ui**, que nous allons facilement convertir en script Python avec **pyuic**.
Dans windows, le programme est livré avec **pyuic pyqt** (à vérifier), sur Linux, vous aurez probablement besoin de l\'installer séparément à partir de votre gestionnaire de paquets (sur debian-systèmes basés sur, il fait partie du paquet pyqt4-dev-tools).
Pour faire la conversion, vous aurez besoin d\'ouvrir une fenêtre de terminal (ou une fenêtre d\'invite de commandes), accédez à l\'endroit où vous avez enregistré votre fichier **ui** : 
```python
pyuic mywidget.ui > mywidget.py
``` Dans Windows pyuic.py est présent dans \"C:\\Python27\\Lib\\site-packages\\PyQt4\\uic\\pyuic.py\" Créez un fichier batch \"compQt4.bat\" pour automatiser la tâche: 
```python
@"C:\Python27\python" "C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py" -x %1.ui > %1.py
``` Dans la console Dos tapez sans extension 
```python
compQt4 myUiFile
```

Sous macOS, vous pouvez récupérer la version appropriée (celle qui est utilisée en interne dans FreeCAD 0.19) de QT et Pyside avec les commandes suivantes (pip requis). 
```python
python3 -m pip install pyqt5
python3 -m pip install pySide2
``` Cela va installer uic dans le dossier \"/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/uic\", et Designer dans \"/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/Designer.app\". Pour plus de commodité, vous pouvez créer un lien vers uic dans /usr/local/bin pour pouvoir l\'appeler simplement avec uic -g python \... au lieu de taper le chemin complet du programme, et un lien vers Designer pour le récupérer dans le dossier Applications du mac avec 
```python
sudo ln -s /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/uic /usr/local/bin
ln -s /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/Designer.app /Applications
```

Dans Linux : à venir

Depuis la version 0.13, FreeCAD migre progressivement de PyQt à [PySide](http://qt-project.org/wiki/PySide) (Choisissez votre installateur PySide suivant votre système [building PySide](http://pyside.readthedocs.org/en/latest/building/)),


```python
pyside-uic mywidget.ui -o mywidget.py
```

Dans Windows le fichier uic.py se trouve dans \"C:\\Python27\\Lib\\site-packages\\PySide\\scripts\\uic.py\" Créez un fichier batch \"compSide.bat\" 
```python
@"C:\Python27\python" "C:\Python27\Lib\site-packages\PySide\scripts\uic.py" %1.ui > %1.py
``` Dans la console Python tapez sans extension: 
```python
compSide myUiFile
``` Dans Linux: faites

Sur certains systèmes, le programme est appelé pyuic4 lieu de pyuic. Il sert uniquement de convertisseur du fichier .ui pour l\'utiliser dans un script Python. Si nous ouvrons le fichier mywidget.py, son contenu est très facile à comprendre: 
```python
from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(187, 178)
        self.title = QtGui.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(10, 10, 271, 16))
        self.title.setObjectName("title")
        self.label_width = QtGui.QLabel(Dialog)
        ...

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

   def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setText(QtGui.QApplication.translate("Dialog", "Plane-O-Matic", None, QtGui.QApplication.UnicodeUTF8))
        ...
``` Comme vous voyez, il a une structure très simple: une classe nommée **Ui_Dialog** est créé, qui stocke les éléments de l\'interface de notre widget.
Cette classe dispose de deux méthodes, une pour la mise en place du widget, et l\'autre pour traduire son contenu, qui fait partie du mécanisme général de Qt pour la traduction des éléments d\'interface. La méthode de configuration, crée simplement, un par un, les widgets tels que nous les avons définis dans Qt Designer, et définit leurs options aussi comme nous avons décidé plus tôt. Puis, toute l\'interface est traduite, et enfin, les \"slots\" se connectent (nous en reparlerons plus tard).

Nous pouvons maintenant créer un nouveau widget, et utiliser cette classe pour créer son interface. Nous pouvons déjà voir notre widget en action, en mettant notre fichier mywidget.py dans un endroit où FreeCAD la trouvera (dans le répertoire bin FreeCAD, ou dans l\'un des sous-répertoires Mod), et, dans l\'interpréteur Python de FreeCAD, faisons: 
```python
from PySide import QtGui
import mywidget
d = QtGui.QWidget()
d.ui = mywidget.Ui_Dialog()
d.ui.setupUi(d)
d.show()
``` Et notre boîte de dialogue apparaîtra! Notez que notre interpréteur Python fonctionne toujours, nous avons une boîte de dialogue non modale.
Donc, pour la fermer, nous pouvons (à part cliquer sur son icône, bien sûr) faire: 
```python
d.hide()
```

## Faire quelque chose avec notre boîte de dialogue 

Maintenant que nous pouvons afficher et masquer notre boîte de dialogue, nous avons juste besoin d\'ajouter la dernière partie, pour en faire quelque chose !
Si vous explorez un peu Qt Designer, vous découvrirez rapidement toute une section appelée \"**signaux et slots**\".
Fondamentalement, cela fonctionne comme ceci, ce sont les éléments sur vos widgets (dans la terminologie de Qt, ces éléments sont eux-mêmes des widgets) qui peuvent envoyer des signaux.
Ces signaux diffèrent selon le type de widget. Par exemple, un bouton peut envoyer un signal quand il est pressé et quand il est relâché.
Ces signaux peuvent être connectés à des créneaux, qui peuvent être des fonctionnalités spéciales d\'autres widgets (par exemple une boîte de dialogue a un bouton \"Fermer\" sur lequel vous pouvez connecter le signal à partir d\'un autre bouton \"Fermer\"), ou, peuvent être des fonctions personnalisées.
[La documentation de référence PyQt](http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/classes.html) répertorie tous les widgets Qt, ce qu\'ils peuvent faire, ce qu\'ils signalent, ce qu\'ils peuvent envoyer, etc . . .

Ce que nous allons faire ici, c\'est créer une nouvelle fonction qui permettra de créer une surface plane basée sur la hauteur et la largeur, et, relier cette fonction au bouton \"Create!\".
Donc, nous allons commencer par importer nos modules FreeCAD, en mettant la ligne suivante en haut du script, où nous importons déjà **QtCore** et **QtGui**: 
```python
import FreeCAD, Part
``` Ensuite, nous allons ajouter une nouvelle fonction à notre classe **Ui_Dialog**: 
```python
def createPlane(self):
    try:
        # first we check if valid numbers have been entered
        w = float(self.width.text())
        h = float(self.height.text())
    except ValueError:
        print("Error! Width and Height values must be valid numbers!")
    else:
        # create a face from 4 points
        p1 = FreeCAD.Vector(0,0,0)
        p2 = FreeCAD.Vector(w,0,0)
        p3 = FreeCAD.Vector(w,h,0)
        p4 = FreeCAD.Vector(0,h,0)
        pointslist = [p1,p2,p3,p4,p1]
        mywire = Part.makePolygon(pointslist)
        myface = Part.Face(mywire)
        Part.show(myface)
        self.hide()
``` Puis, nous avons besoin d\'informer Qt pour qu\'il se connecte sur le bouton de la fonction, en plaçant la ligne suivante juste avant **QtCore.QMetaObject.connectSlotsByName(Dialog)**: 
```python
QtCore.QObject.connect(self.create,QtCore.SIGNAL("pressed()"),self.createPlane)
``` Il s\'agit, comme vous le voyez, de relier le signal du bouton enfoncé de l\'objet a créer (**\"Create!\" Bouton**), à un emplacement nommé **createPlane**, dont nous venons de définir.
Ça y est ! Maintenant, la touche finale, nous pouvons ajouter une petite fonction, pour créer la boîte de dialogue, elle sera plus facile a appeler.
En dehors de la classe **Ui_Dialog class**, nous allons ajouter le code suivant: 
```python
class plane():
   def __init__(self):
       self.d = QtGui.QWidget()
       self.ui = Ui_Dialog()
       self.ui.setupUi(self.d)
       self.d.show()
``` (Rappel sur Python : la méthode **\_\_init\_\_** est une classe qui s\'exécute automatiquement chaque fois qu\'un nouvel objet est créé ! )

Puis, à partir de FreeCAD, nous avons seulement besoin de faire: 
```python
import mywidget
myDialog = mywidget.plane()
``` Voilà, c\'est tout \...
Maintenant, vous pouvez essayer toutes sortes de choses, comme par exemple l\'insertion de votre widget dans l\'interface FreeCAD (voir la page [Code snippets](Code_snippets/fr.md)), ou, faire des outils personnalisés beaucoup plus avancés, en utilisant d\'autres éléments dans votre widget.

## Le script complet 

Ceci est le script de référence complet: 
```python
# Form implementation generated from reading ui file 'mywidget.ui'
#
# Created: Mon Jun  1 19:09:10 2009
#      by: PyQt4 UI code generator 4.4.4
# Modified for PySide 16:02:2015 
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import FreeCAD, Part 

class Ui_Dialog(object):
   def setupUi(self, Dialog):
       Dialog.setObjectName("Dialog")
       Dialog.resize(187, 178)
       self.title = QtGui.QLabel(Dialog)
       self.title.setGeometry(QtCore.QRect(10, 10, 271, 16))
       self.title.setObjectName("title")
       self.label_width = QtGui.QLabel(Dialog)
       self.label_width.setGeometry(QtCore.QRect(10, 50, 57, 16))
       self.label_width.setObjectName("label_width")
       self.label_height = QtGui.QLabel(Dialog)
       self.label_height.setGeometry(QtCore.QRect(10, 90, 57, 16))
       self.label_height.setObjectName("label_height")
       self.width = QtGui.QLineEdit(Dialog)
       self.width.setGeometry(QtCore.QRect(60, 40, 111, 26))
       self.width.setObjectName("width")
       self.height = QtGui.QLineEdit(Dialog)
       self.height.setGeometry(QtCore.QRect(60, 80, 111, 26))
       self.height.setObjectName("height")
       self.create = QtGui.QPushButton(Dialog)
       self.create.setGeometry(QtCore.QRect(50, 140, 83, 26))
       self.create.setObjectName("create")

       self.retranslateUi(Dialog)
       QtCore.QObject.connect(self.create,QtCore.SIGNAL("pressed()"),self.createPlane)
       QtCore.QMetaObject.connectSlotsByName(Dialog)

   def retranslateUi(self, Dialog):
       Dialog.setWindowTitle("Dialog")
       self.title.setText("Plane-O-Matic")
       self.label_width.setText("Width")
       self.label_height.setText("Height")
       self.create.setText("Create!")
       print("tyty")
   def createPlane(self):
       try:
           # first we check if valid numbers have been entered
           w = float(self.width.text())
           h = float(self.height.text())
       except ValueError:
           print("Error! Width and Height values must be valid numbers!")
       else:
           # create a face from 4 points
           p1 = FreeCAD.Vector(0,0,0)
           p2 = FreeCAD.Vector(w,0,0)
           p3 = FreeCAD.Vector(w,h,0)
           p4 = FreeCAD.Vector(0,h,0)
           pointslist = [p1,p2,p3,p4,p1]
           mywire = Part.makePolygon(pointslist)
           myface = Part.Face(mywire)
           Part.show(myface)

class plane():
  def __init__(self):
      self.d = QtGui.QWidget()
      self.ui = Ui_Dialog()
      self.ui.setupUi(self.d)
      self.d.show()

```

## Plus d\'exemples 

-   [Création d\'une boîte de dialogues avec différents widgets](Dialog_creation_with_various_widgets.md) avec `QPushButton`, `QLineEdit`, `QCheckBox`, `QRadioButton` et bien d\'autres.
-   [Création d\'une boîte de dialogue lecture et écriture de fichiers](Dialog_creation_reading_and_writing_files/fr.md) with `QFileDialog`.
-   [Création d\'une boîte de dialogue réglage des couleurs](Dialog_creation_setting_colors/fr.md) avec `QColorDialog`.
-   [Création d\'une boîte de dialogue pour image et GIF animé](Dialog_creation_image_and_animated_GIF/fr.md) avec `QLabel` et `QMovie`.
-   [Extraits d\'utilisation de PySide](PySide_usage_snippets/fr.md).
-   [Macro Qt Example](Qt_Example/fr.md)

## Liens pertinents 

-   [Outils de création d\'interfaces](Manual:Creating_interface_tools/fr.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Dialog creation/fr
