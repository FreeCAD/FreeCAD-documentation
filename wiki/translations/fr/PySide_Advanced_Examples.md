


{{TOCright}}

## Introduction

Le but de cette page est de couvrir des exemples de niveau avancé du gestionnaire GUI [PySide](PySide/fr.md) (il y a des pages d\'accompagnement [PySide: Exemples pour débutant](PySide_Beginner_Examples/fr.md) et [PySide: Exemples pour niveau intermédiaire](PySide_Intermediate_Examples/fr.md)).

En utilisant le module PySide depuis FreeCAD, vous avez un contrôle total sur son interface. Vous pouvez par exemple:

-   Ajouter vos propres panneaux, widgets et barres d\'outils
-   Ajouter ou masquer des éléments aux panneaux existants
-   Changer, rediriger ou ajouter des connexions entre tous ces éléments

## Créer une référence pour la fenêtre principale {#créer_une_référence_pour_la_fenêtre_principale}

Si vous souhaitez travailler sur l\'interface FreeCAD, la toute première chose à faire est de créer une référence à la fenêtre principale de FreeCAD:


```python
import sys
from PySide import QtGui ,QtCore 
app = QtGui.qApp
mw = FreeCADGui.getMainWindow()
```

## Parcourir les Enfants de la fenêtre principale {#parcourir_les_enfants_de_la_fenêtre_principale}

Ensuite, vous pouvez par exemple parcourir tous les widgets de l\'interface:


```python
for child in mw.children():
   print('widget name = ', child.objectName(), ', widget type = ', child)
```

Les widgets d\'une interface Qt sont généralement imbriqués dans des \"conteneurs\" widgets, de sorte que les enfants de notre fenêtre principale peuvent contenir d\'autres enfants. Selon le type de widget, vous pouvez faire énormément de choses. Vérifiez la documentation de l\'API pour voir ce qui est possible.

## Ajouter un nouveau widget manuellement {#ajouter_un_nouveau_widget_manuellement}

L\'ajout d\'un nouveau widget, par exemple un qdockWidget (qui peut être placé dans l\'un des panneaux latéraux de FreeCAD) est facile:


```python
myWidget = QtGui.QDockWidget()
mw.addDockWidget(QtCore.Qt.RightDockWidgetArea,myWidget)
```

Vous pouvez ensuite ajouter ce que vous voulez directement sur votre widget:


```python
myWidget.setObjectName("my Nice New Widget")
myWidget.resize(QtCore.QSize(300,100)) # sets size of the widget
label = QtGui.QLabel("Hello World", myWidget) # creates a label
label.setGeometry(QtCore.QRect(2,50,200,24))  # sets its size
label.setObjectName("myLabel") # sets its name, so it can be found by name
```

## Ajouter un nouveau widget en créant un objet d\'interface utilisateur {#ajouter_un_nouveau_widget_en_créant_un_objet_dinterface_utilisateur}

Mais une méthode préférée est de créer un objet d\'interface utilisateur qui effectuera toute la configuration de votre widget à la fois. Le gros avantage est qu\'un tel objet UI peut être [créé graphiquement](Dialog_creation/fr.md) avec le programme Qt Designer. Un objet typique généré par Qt Designer est comme ceci:


```python
class myWidget_Ui(object):
  def setupUi(self, myWidget):
    myWidget.setObjectName("my Nice New Widget")
    myWidget.resize(QtCore.QSize(300,100).expandedTo(myWidget.minimumSizeHint())) # sets size of the widget

    self.label = QtGui.QLabel(myWidget) # creates a label
    self.label.setGeometry(QtCore.QRect(50,50,200,24)) # sets its size
    self.label.setObjectName("label") # sets its name, so it can be found by name

  def retranslateUi(self, draftToolbar): # built-in QT function that manages translations of widgets
    myWidget.setWindowTitle(QtGui.QApplication.translate("myWidget", "My Widget", None, QtGui.QApplication.UnicodeUTF8))
    self.label.setText(QtGui.QApplication.translate("myWidget", "Welcome to my new widget!", None, QtGui.QApplication.UnicodeUTF8))
```

Pour l\'utiliser, il suffit de l\'appliquer à votre widget fraîchement créé comme ceci:


```python
app = QtGui.qApp
FCmw = app.activeWindow()
myNewFreeCADWidget = QtGui.QDockWidget() # create a new dckwidget
myNewFreeCADWidget.ui = myWidget_Ui() # load the Ui script
myNewFreeCADWidget.ui.setupUi(myNewFreeCADWidget) # setup the ui
FCmw.addDockWidget(QtCore.Qt.RightDockWidgetArea,myNewFreeCADWidget) # add the widget to the main window
```

## Chargement de l\'interface utilisateur à partir d\'un fichier .ui Qt Designer {#chargement_de_linterface_utilisateur_à_partir_dun_fichier_.ui_qt_designer}

La clé pour charger un fichier d\'interface utilisateur avec succès est d\'utiliser le chemin d\'accès complet au fichier. Par exemple, le [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) le fait comme ceci:


```python
self.dialog = FreeCADGui.PySideUic.loadUi(os.path.join(os.path.dirname(__file__), "AddonManager.ui"))
```


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
