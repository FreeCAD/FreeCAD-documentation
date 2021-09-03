

## Introduction

Le but de cette page est de couvrir les exemples de niveau débutant du gestionnaire de l\'interface graphique utilisateur [PySide](PySide/fr.md) (voir ensuite les pages [Exemples intermédiaires PySide](PySide_Intermediate_Examples/fr.md) et [Exemples avancés PySide](PySide_Advanced_Examples/fr.md)).

Les nouveaux arrivants à la programmation GUI peuvent trébucher sur le mot \"widget\". Sa signification en dehors de l\'informatique est généralement donnée comme

> \"un petit gadget ou dispositif mécanique, en particulier celui dont le nom est inconnu ou non spécifié\"

Pour les gestionnaires d\'interfaces graphique tel que PySide, le terme «widget» est le plus souvent utilisé pour désigner les éléments visibles de l\'interface graphique - fenêtres, boîtes de dialogue et fonctions d\'entrée / sortie. Tous les éléments visibles de PySide sont appelés widgets, et, pour ceux qui sont intéressés, ils descendent tous d\'une classe parente commune, QWidget. En plus des éléments visibles, PySide propose également des widgets pour la mise en réseau, XML, multimédia et l\'intégration de bases de données.

Un widget qui n\'est pas intégré dans un widget parent est appelé une fenêtre et généralement les fenêtres ont un cadre et une barre de titre. Les types de fenêtres les plus courants sont la \"fenêtre principale\" (de la classe QMainWindow) et les différentes sous-classes de la boîte de dialogue (de la classe QDialog). Une grande différence est que QDialog est modal (c\'est-à-dire que l\'utilisateur ne peut rien faire en dehors de la fenêtre Dialog alors qu\'il est ouvert) et que QMainWindow est non modal, ce qui permet à l\'utilisateur d\'interagir avec d\'autres fenêtres en parallèle.

Ce guide est une liste de raccourcis pour faire rapidement faire fonctionner un programme PySide sous FreeCAD, il n\'est pas destiné à enseigner Python ou PySide. Voici une liste de certains sites qui font cela : /!\\ attention /!\\ sites en anglais

-   [PySide tutorial](http://zetcode.com/gui/pysidetutorial/) at zetcode.com
-   [PySide/PyQt Tutorial](http://www.pythoncentral.io/series/python-pyside-pyqt-tutorial/) at PythonCentral.io
-   [PySide 1.0.7 Reference](http://srinikom.github.io/) at Srinikom.github.io (note this is a reference, not a tutorial)

## Déclaration d\'importation {#déclaration_dimportation}

PySide n\'est pas chargé avec Python par défaut, il doit être importé avant de l\'utiliser. La commande suivante: 
```python
from PySide import QtCore
from PySide import QtGui
``` provoque le chargement des deux parties de PySide - QtGui contient des classes pour la gestion de l\'interface graphique utilisateur tandis que QtCore contient des classes qui ne sont pas directement liées à la gestion de l\'interface graphique (par exemple les minuteurs et la géométrie). Bien qu\'il soit possible d\'importer seulement celui qui est nécessaire, généralement ils sont tous deux nécessaires et donc importés.

Les déclarations d\'importation ne sont pas répétées dans les extraits ci-dessous. On suppose que cela se fait au début dans chaque cas.

## Exemple simple {#exemple_simple}

L\'interaction la plus simple avec PySide est de présenter à l\'utilisateur un message qu\'il ne peut que accepter : 
```python
reply = QtGui.QMessageBox.information(None,"","Houston, we have a problem")
```

![](images/PySideScreenSnapshot5.jpg )

## Oui ou Non {#oui_ou_non}

L\'interaction simple suivante consiste à demander de répondre oui ou non : 
```python
reply = QtGui.QMessageBox.question(None, "", "This is your chance to answer, what do you think?",
         QtGui.QMessageBox.Yes {{!``` QtGui.QMessageBox.No, QtGui.QMessageBox.No) if reply == QtGui.QMessageBox.Yes:

        # this is where the code relevant to a 'Yes' answer goes
        pass

if reply == QtGui.QMessageBox.No:

        # this is where the code relevant to a 'No' answer goes
        pass

}}

![](images/PySideScreenSnapshot6.jpg )

## Zone de texte {#zone_de_texte}

L\'extrait de code suivant demande à l\'utilisateur un texte - notez qu\'il peut s\'agir de n\'importe quelle touche du clavier : 
```python
reply = QtGui.QInputDialog.getText(None, "Ouija Central","Enter your thoughts for the day:")
if reply[1]:
    # user clicked OK
    replyText = reply[0]
else:
    # user clicked Cancel
    replyText = reply[0] # which will be "" if they clicked Cancel
```

![](images/PySideScreenSnapshot7.jpg )

Souvenez-vous que même si l\'utilisateur ne saisit que des chiffres, \"1234\" par exemple, ce sont des chaînes de caractères et doivent être converties en représentation numérique avec l\'un des éléments suivants: 
```python
anInteger = int(userInput) # to convert to an integer from a string representation

aFloat = float(userInput) # to convert to a float from a string representation
```

## Plus de 2 boutons {#plus_de_2_boutons}

L\'exemple final du niveau débutant est de savoir comment construire une boîte de dialogue avec un nombre arbitraire de boutons. Cet exemple est trop complexe par programme pour pouvoir être invoqué à partir d\'une seule instruction Python. Par conséquent, il devrait être à la page suivante, qui est un exemple de PySide Intermédiaire. Mais d\'un autre côté, c\'est souvent tout ce qui est nécessaire sans entrer dans des définitions d\'interface graphique complexes, donc le code est placé à la fin de cette page PySide Débutant plutôt que le début de la page PySide Intermédiaire suivante. 
```python
from PySide import QtGui, QtCore

class MyButtons(QtGui.QDialog):
    """"""
    def __init__(self):
        super(MyButtons, self).__init__()
        self.initUI()
    def initUI(self):      
        option1Button = QtGui.QPushButton("Option 1")
        option1Button.clicked.connect(self.onOption1)
        option2Button = QtGui.QPushButton("Option 2")
        option2Button.clicked.connect(self.onOption2)
        option3Button = QtGui.QPushButton("Option 3")
        option3Button.clicked.connect(self.onOption3)
        option4Button = QtGui.QPushButton("Option 4")
        option4Button.clicked.connect(self.onOption4)
        option5Button = QtGui.QPushButton("Option 5")
        option5Button.clicked.connect(self.onOption5)
        #
        buttonBox = QtGui.QDialogButtonBox()
        buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
        buttonBox.addButton(option1Button, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(option2Button, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(option3Button, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(option4Button, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(option5Button, QtGui.QDialogButtonBox.ActionRole)
        #
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        # define window     xLoc,yLoc,xDim,yDim
        self.setGeometry(   250, 250, 0, 50)
        self.setWindowTitle("Pick a Button")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    def onOption1(self):
        self.retStatus = 1
        self.close()
    def onOption2(self):
        self.retStatus = 2
        self.close()
    def onOption3(self):
        self.retStatus = 3
        self.close()
    def onOption4(self):
        self.retStatus = 4
        self.close()
    def onOption5(self):
        self.retStatus = 5
        self.close()

def routine1():
    print 'routine 1'

form = MyButtons()
form.exec_()
if form.retStatus==1:
    routine1()
elif form.retStatus==2:
    routine2()
elif form.retStatus==3:
    routine3()
elif form.retStatus==4:
    routine4()
elif form.retStatus==5:
    routine5()

``` Chaque morceau de code à tester serait dans une fonction avec le nom \'routine1()\', \'routine2()\', etc. Vous pouvez utiliser autant de boutons que vous pouvez adapter à l\'écran. Suivez les modèles dans l\'exemple de code et ajoutez des boutons supplémentaires au besoin - la boîte de dialogue définira sa largeur en conséquence, jusqu\'à la largeur de l\'écran.

![](images/PySideScreenSnapshot8.jpg )

Il y a cette ligne de code : 
```python
buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
``` qui fait que les boutons sont dans une ligne horizontale. Pour les mettre dans une ligne verticale, changez la ligne de code en remplaçant Horizontal en Vertical : 
```python
buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Vertical)
```


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
