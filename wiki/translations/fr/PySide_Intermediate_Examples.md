

## Introduction


{{TOCright}}

Cette page couvre des exemples de niveau moyen du gestionnaire d\'interface graphique [PySide](PySide/fr.md) (les pages d\'accompagnement couvrent des aspects à la fois moins ou plus avancés, [Exemples PySide pour débutants](PySide_Beginner_Examples/fr.md) et [Exemples PySide pour confirmés](PySide_Advanced_Examples/fr.md)). Dans cette page, un exemple de programme est utilisé pour couvrir les différents sujets PySide. L\'intention est de présenter du code PySide fonctionnel afin que toute personne ayant besoin d\'utiliser PySide puisse copier la section correspondante, la modifier et l\'adapter à ses propres fins.

### Remarques

-   Cette page n\'est pas destinée à couvrir le langage Python ou à servir d\'instructions en Python.
-   Les noms des variables ne sont pas descriptifs mais ont été conservés dans l\'ordre pour mieux organiser les explications
-   Il existe de nombreuses conventions de dénomination pour les composants de l\'interface graphique, dont aucune n\'est «bonne» ou «mauvaise»
-   Il existe une variété de séquences différentes des déclarations pour les widgets, les signaux, les méthodes, encore une fois, aucune n\'est \"bonne\" ou \"mauvaise\"
-   Il convient de garder à l\'esprit que PySide fonctionne avec des chaînes lorsqu\'il s\'agit de la saisie de l\'utilisateur, ce qui apparaît à l\'écran sous forme de nombre est en fait une représentation textuelle d\'un nombre

## Discussion basée sur le code - Partie déclarative 

Le \"programme d\'exemple\" est en fait une grande définition de classe, la définition d\'une classe PySide GUI et a plus de 150 lignes de code (y compris les commentaires). Il n\'y a pas de but fonctionnel pour la classe ou son comportement, le seul but est de démontrer les actions possibles de l\'interface graphique et de présenter du code qui, espérons-le, peut être utilisé par d\'autres utilisateurs de FreeCAD.

La définition de classe et le petit nombre de lignes de code qui invoquent sont décrits dans l\'ordre d\'apparition dans le fichier. Cet ordre est basé sur la disposition de l\'écran qui est plutôt arbitraire et uniquement destinée à démontrer les fonctionnalités. Voici l\'écran GUI modal généré par la classe PySide:

![](images/PySideScreenSnapshot3.jpg )

La majeure partie du reste de cette section décrira le contenu de la définition de classe qui apparaît à la fin de cette section. Nous couvrirons d\'abord les éléments déclaratifs qui définissent comment les choses fonctionnent et comment l\'interface graphique est assemblée, puis nous couvrirons les sections opérationnelles (c\'est-à-dire le code qui s\'exécutera lorsque les interactions de l\'utilisateur se produiront). Cette fenêtre est basée sur la classe QDialog et est donc modale - ce qui signifie qu\'aucune activité ne peut être effectuée en dehors de la fenêtre lorsqu\'elle est ouverte.

### Déclaration d\'importation 

La déclaration d\'importation obligatoire 
```python
from PySide import QtGui, QtCore
``` Il est préférable de le placer en haut du fichier Python.

### Définition de classe 


```python
class ExampleModalGuiClass(QtGui.QDialog):
    """"""
    def __init__(self):
        super(ExampleModalGuiClass, self).__init__()
        self.initUI()
    def initUI(self):
```

Ce code est mieux copié textuellement et modifié. L\'essentiel du code est que nous sous-classons la classe QDialog de PySide. En adaptant ce code, vous voudrez changer le nom de la classe \"ExampleModalGuiClass\" - assurez-vous de le changer dans les deux endroits (par exemple les lignes 1 et 4).

### État de retour de la fenêtre 


```python
self.result = userCancelled
```

Ce n\'est pas obligatoire mais plutôt une bonne pratique de programmation, cela définit un statut de retour par défaut pour la fenêtre qui sera là indépendamment de ce que fait l\'utilisateur. Plus tard dans le code, cela peut être modifié par le code Python pour indiquer les différentes options que l\'utilisateur peut avoir sélectionnées.

### Création de fenêtres 


```python
# create our window
# define window     xLoc,yLoc,xDim,yDim
self.setGeometry(   250, 250, 400, 350)
self.setWindowTitle("Our Example Program Window")
self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
```

En vous rappelant que les dimensions de l\'écran sont mesurées à partir du coin supérieur gauche, sur la 3ème ligne, les valeurs se réfèrent à:

-   le nombre de pixels dans le coin supérieur gauche sera à droite du bord gauche de l\'écran (250)
-   le nombre de pixels dans le coin supérieur gauche sera sous le bord supérieur de l\'écran (250)
-   la largeur de l\'écran en pixels (400)
-   la hauteur de l\'écran en pixels (350)

Le titre de la fenêtre est défini et la dernière ligne signifie simplement que cette fenêtre ne sera jamais obscurcie par une autre fenêtre - si cela n\'est pas souhaité, placez simplement un caractère de commentaire Python (\'\#\') comme premier caractère de la ligne.

### Création d\'étiquettes 


```python
# create some Labels
self.label1 = QtGui.QLabel("                       ", self)
self.label1.setFont('Courier') # set to a non-proportional font
self.label1.move(20, 20)
self.label2 = QtGui.QLabel("sample string number two", self)
self.label2.move(20, 70)
self.label3 = QtGui.QLabel("                        ", self)
self.label3.setFont('Courier') # set to a non-proportional font
self.label3.move(20, 120)
self.label4 = QtGui.QLabel("can you see this?", self)
self.label4.move(20, 170)
```

Dans PySide, les étiquettes ont deux objectifs: les étiquettes statiques (comme leur nom l\'indique) et les champs de texte en lecture seule (c\'est-à-dire en affichage uniquement). Ainsi, des instructions inchangées à l\'utilisateur telles que \"Don\'t push the red button\" ainsi que des résultats de calcul dynamiques tels que \"42\" peuvent être communiquées à l\'utilisateur. La 2ème ligne déclare une étiquette et définit sa valeur initiale (qui est vide dans ce cas). La troisième ligne spécifie la police, n\'importe quelle police (sur le système) peut être spécifiée, si elle n\'est pas spécifiée, la police par défaut est utilisée. Dans ce cas, la police est spécifiée comme non proportionnelle. L\'étiquette est déplacée vers son emplacement dans la fenêtre - ses coordonnées spécifient sa position par rapport à la fenêtre (pas à l\'écran).

### Création de cases à cocher 


```python
# checkboxes
self.checkbox1 = QtGui.QCheckBox("Left side", self)
self.checkbox1.clicked.connect(self.onCheckbox1)
#self.checkbox1.toggle() # will set an initial value if executed
self.checkbox1.move(210,10)
#
self.checkbox2 = QtGui.QCheckBox("Right side", self)
self.checkbox2.clicked.connect(self.onCheckbox2)
self.checkbox2.move(210,30)
```

Les cases à cocher peuvent être désactivées et activées dans n\'importe quelle combinaison (contrairement aux boutons radio). La ligne 2 en déclare un et définit sa valeur initiale. La ligne 3 spécifie quelle méthode sera exécutée lorsque la case à cocher est cliquée (dans ce cas, la méthode \'onCheckBox1\'). Si la 4ème ligne n\'avait pas le caractère de commentaire Python (\'\#\') comme premier caractère, alors elle serait exécutée et il marquerait la case comme cochée. Enfin, la 5ème ligne place la case à cocher en position.

### Création de boutons radio 


```python
# radio buttons
self.radioButton1 = QtGui.QRadioButton("random string one",self)
self.radioButton1.clicked.connect(self.onRadioButton1)
self.radioButton1.move(210,60)
#
self.radioButton2 = QtGui.QRadioButton("owt gnirts modnar",self)
self.radioButton2.clicked.connect(self.onRadioButton2)
self.radioButton2.move(210,80)
```

La création des boutons radio est très similaire aux cases à cocher. La seule différence est vraiment le comportement des boutons radio en ce qu\'un seul d\'entre eux peut être \'activé\' à la fois.

### Création d\'un menu contextuel 


```python
# set up lists for pop-ups
self.popupItems1 = ("pizza","apples","candy","cake","potatoes")
# set up pop-up menu
self.popup1 = QtGui.QComboBox(self)
self.popup1.addItems(self.popupItems1)
self.popup1.setCurrentIndex(self.popupItems1.index("candy"))
self.popup1.activated[str].connect(self.onPopup1)
self.popup1.move(210, 115)
```

À la ligne 2, une liste est constituée de ce que seront les choix de l\'utilisateur. Une alternative consiste à créer un dictionnaire mais à n\'utiliser les touches que pour la liste des choix de menu. La ligne 4 crée le menu contextuel (appelé ComboBox vers PySide), les options utilisateur sont ajoutées à la ligne 5.

Si le Dictionnaire était utilisé, les lignes apparaîtraient comme suit : 
```python
self.popupItems1 = OrderedDict([("2","widget"),("pink","foobar"),("4","galopsis")])

self.popup1.addItems(self.popupItems1.keys())
``` Revenant à l\'exemple de code principal de cette section, la ligne 6 définit le choix par défaut, cette ligne peut être omise, la valeur du choix par défaut peut également être chargée dans l\'étiquette correspondante (encore une fois si nécessaire). Et enfin le passage en position à la ligne 8.

### Création de bouton, partie 1 


```python
# toggle visibility button
pushButton1 = QtGui.QPushButton('Toggle visibility', self)
pushButton1.clicked.connect(self.onPushButton1)
pushButton1.setAutoDefault(False)
pushButton1.move(210, 165)
```

Le bouton est créé à la ligne 2 avec son nom, le gestionnaire de son signal lorsque l\'utilisateur clique est spécifié à la ligne 3. La ligne 4 est là pour empêcher le bouton de devenir le \'bouton par défaut\' - le bouton sur lequel l\'utilisateur clique simplement si l\'utilisateur appuie sur la touche **Valider**. Et un passage à la position a terminé le segment de code.

### Création d\'une entrée de texte 


```python
# text input field
self.textInput = QtGui.QLineEdit(self)
self.textInput.setText("cats & dogs")
self.textInput.setFixedWidth(190)
self.textInput.move(20, 220)
```

Le widget QLineEdit est probablement le plus courant pour la saisie textuelle de l\'utilisateur, dans cet exemple, la section de code après celle-ci mettra en place un menu contextuel pour l\'utiliser. Cette section de code crée (ligne 2), définit une valeur initiale (ligne 3), définit une largeur pour le champ (ligne 4) et met le widget en place (ligne 5).

### Création du menu contextuel 


```python
# set contextual menu options for text editing widget
# set text field to some dogerel
popMenuAction1 = QtGui.QAction(self)
popMenuAction1.setText("load some text")
popMenuAction1.triggered.connect(self.onPopMenuAction1)
# make text uppercase
popMenuAction2 = QtGui.QAction(self)
popMenuAction2.setText("uppercase")
popMenuAction2.triggered.connect(self.onPopMenuAction2)
# menu dividers
popMenuDivider = QtGui.QAction(self)
popMenuDivider.setText('---------')
popMenuDivider.triggered.connect(self.onPopMenuDivider)
# remove all text
popMenuAction3 = QtGui.QAction(self)
popMenuAction3.setText("clear")
popMenuAction3.triggered.connect(self.onPopMenuAction3)
# define menu and add options
self.textInput.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
self.textInput.addAction(popMenuAction1)
self.textInput.addAction(popMenuAction2)
self.textInput.addAction(popMenuDivider)
self.textInput.addAction(popMenuAction3)
```

Ce code a de nombreuses répétitions car la même action est effectuée avec des valeurs différentes - cela fait partie de ce qui rend le code GUI si long (quel que soit le système). Tout d\'abord, une QAction est créée - c\'est un appariement (ou un lien) du texte que l\'utilisateur verra comme son option sélectionnable avec la méthode qui s\'exécutera s\'il sélectionne cette option. Il s\'agit essentiellement d\'un couplage d\'un choix d\'utilisateur avec un morceau de code. La ligne 3 le crée, la ligne 4 définit l\'option utilisateur (comme ils le verront) et la ligne 5 spécifie quel morceau de code Python sera exécuté.

En sautant à la ligne 19 (la ligne avec \"self.textInput.setContextMenuPolicy\"), un ActionsContextMenu est créé, qui contient tous les liens QAction séparés entre le choix de l\'utilisateur et le code à exécuter. Chaque widget ne peut avoir qu\'un seul menu contextuel (c\'est-à-dire le menu associé au clic droit) donc la ligne 19 définit ce menu. Les 4 lignes suivantes ajoutent les liens créés au début de cette section de code. L\'ordre est important ici, l\'utilisateur verra les options du menu dans l\'ordre dans lequel elles sont ajoutées. Notez que la 3ème option de menu est vraiment un peu rien, son code est nul mais il sert à séparer 2 groupes d\'options sur le menu contextuel.

### Création d\'une entrée numérique 


```python
# numeric input field
self.numericInput = QtGui.QLineEdit(self)
self.numericInput.setInputMask("999")
self.numericInput.setText("000")
self.numericInput.setFixedWidth(50)
self.numericInput.move(250, 220)
```

La création du champ pour la saisie numérique suit vraiment celle de la saisie de texte plus tôt. En fait le code est identique à l\'exception des 3ème et 4ème lignes. La troisième ligne définit le masque tel que défini par PySide, qui dans ce cas spécifie jusqu\'à 3 chiffres (qui peuvent inclure 0). Une liste complète des codes InputMask peut être trouvée sur [QLineEdit InputMask](http://doc.qt.io/qt-5/qlineedit.html#inputMask-prop)

### Création de bouton, partie 2 


```python
# cancel button
cancelButton = QtGui.QPushButton('Cancel', self)
cancelButton.clicked.connect(self.onCancel)
cancelButton.setAutoDefault(True)
cancelButton.move(150, 280)
# OK button
okButton = QtGui.QPushButton('OK', self)
okButton.clicked.connect(self.onOk)
okButton.move(260, 280)
```

Les deux boutons sont créés avec un nom (qui apparaîtra comme leur étiquette), associé à une méthode qui s\'exécutera quand ils seront cliqués et déplacés en position. La seule exception est la ligne 4 qui spécifie le bouton \'Annuler\' comme bouton par défaut - cela signifie qu\'il sera \"cliqué\" si l\'utilisateur appuie sur la touche **Valider**.

### Affichage de la fenêtre 


```python
# now make the window visible
self.show()
```

Il n\'y a qu\'une seule ligne et cela provoque l\'affichage de l\'interface graphique après l\'installation.

## Discussion basée sur le code - Partie opérative 

Nous passons maintenant à la partie opérationnelle de la définition de l\'interface graphique qui est le code qui s\'exécute en réponse aux interactions de l\'utilisateur avec l\'interface graphique. L\'ordre des groupes d\'instructions n\'est pas très pertinent - avec la mise en garde que quelque chose doit être déclaré avant de pouvoir être référencé. Certaines personnes mettent tous les gestionnaires d\'un certain type (par exemple, les gestionnaires de boutons) dans un groupe, d\'autres répertorient les gestionnaires par ordre alphabétique. Pour une application spécifique, il peut y avoir une raison liée au problème que tous les gestionnaires relatifs à un aspect spécifique soient rassemblés

Il existe un degré élevé de similitude entre les gestionnaires. La plupart ne reçoivent pas de paramètre, le fait qu\'ils s\'exécutent est vraiment le seul paramètre (ou signal) qu\'ils reçoivent. D\'autres comme \"onPopup1\" et \"mousePressEvent\" acceptent un paramètre.

Il doit y avoir une correspondance un à un entre les gestionnaires spécifiés dans la section déclarative et le gestionnaire déclaré dans cette section opérationnelle. Il peut y avoir des gestionnaires supplémentaires déclarés qui ne sont jamais appelés, mais il se peut qu\'il n\'y en ait aucun manquant.

### Gestionnaire générique 

Dans cet exemple de code, les gestionnaires génériques gèrent les événements suivants:

-   onCheckbox1
-   onCheckbox2
-   onRadioButton1
-   onRadioButton2
-   onPushButton1
-   onPopMenuAction1
-   onPopMenuAction2
-   onPopMenuDivider
-   onPopMenuAction3
-   onCancel
-   onOk

La forme générale des gestionnaires est: 
```python
def handlerName(self):
    lineOfCode1
    lineOfCode2
``` La première ligne contient le mot-clé \"def\" suivi du nom du gestionnaire. Le nom du gestionnaire doit correspondre exactement au nom de la section déclarative précédente. Le paramètre \"self\" fait partie de la syntaxe standard, tout comme la parenthèse englobante et le caractère deux-points final. Une fois la première ligne terminée, il n\'y a aucune exigence du code suivant, il est purement spécifique à l\'application.

### Gestionnaire de menu contextuel 


```python
def onPopup1(self, selectedText):
```

Le gestionnaire du menu contextuel est le même que le gestionnaire générique, à l\'exception du fait qu\'un second paramètre, le texte sélectionné par l\'utilisateur, est transmis. Rappelez-vous que tout est du texte provenant du menu Pop-Up et que même si l\'utilisateur a sélectionné le chiffre 3, il sera transmis comme la chaîne \"3\".

### Gestionnaire d\'événements de la souris 


```python
def mousePressEvent(self, event):
    # print mouse position, X & Y
    print("X = ", event.pos().x())
    print("Y = ", event.pos().y())
    #
    if event.button() == QtCore.Qt.LeftButton:
        print("left mouse button")
    if self.label1.underMouse():
        print("over the text '"+self.label1.text()+"'")
```

Le gestionnaire d\'événements de la souris est le même que le gestionnaire générique à l\'exception du fait qu\'un deuxième paramètre, l\'événement de la souris (par exemple, clic gauche, clic droit) de l\'utilisateur est transmis. Le nom du gestionnaire, \"mousePressEvent\", est réservé et s\'il est modifié, le gestionnaire ne recevra plus l\'événement des pressions de la souris.

Les coordonnées X et Y de la pression de la souris sont données par la référence \"event.pos().x()\" et \"event.pos().y()\". Les constantes \"QtCore.Qt.LeftButton\" et \"QtCore.Qt.RightButton\" sont utilisées pour déterminer quel bouton de la souris est enfoncé.

Une référence à un widget peut être faite de la forme \"self.widgetName.underMouse()\" qui retournera `True` ou `False` pour savoir si le curseur de la souris est sur le widget \"widgetName\". Bien que présenté dans le même extrait de code, le gestionnaire \"underMouse()\" n\'est pas lié au gestionnaire \"mousePressEvent\" et peut être utilisé à tout moment.

## Discussion basée sur le code - Routine principale 

La plupart du volume de code est dans la définition de la classe GUI, il n\'y a pas grand-chose dans la procédure principale. 
```python
# Constant definitions
global userCancelled, userOK
userCancelled = "Cancelled"
userOK = "OK"
``` Les lignes 2, 3 et 4 traitent de la coordination de l\'état de l\'interaction de l\'utilisateur avec l\'interface graphique - par ex. Annulé, OK ou tout autre statut défini par l\'application. Les routines de gestionnaire On Cancel et OnOk précédemment définissent également ces statuts. 
```python
form = ExampleGuiClass()
form.exec_()

if form.result==userCancelled:
    pass # steps to handle user clicking Cancel
if form.result==userOK:
    # steps to handle user clicking OK
    localVariable1 = form.label1.text()
    localVariable2 = form.label2.text()
    localVariable3 = form.label3.text()
    localVariable4 = form.label4.text()
``` Les lignes 1 et 2 montrent la méthode pour appeler l\'interface graphique. Il peut y avoir plusieurs définitions d\'interface graphique pour un programme et l\'interface graphique n\'a pas besoin d\'être invoquée en premier lieu dans le fichier Python, elle peut être appelée à tout moment. Le nom de la classe GUI est spécifié à la ligne 1 (\"ExampleGuiClass\" dans ce cas) mais le reste des 2 lignes doit être copié textuellement.

Les lignes 4 et 6 utilisent le champ de résultat pour déterminer l\'action appropriée. Les 4 dernières lignes montrent simplement la copie des données de l\'objet GUI vers des variables locales de la procédure principale en cours d\'exécution.

## Exemple de code modal complet 

Voici l\'exemple complet de code (développé sur FreeCAD v0.14): 
```python
# import statements
from PySide import QtGui, QtCore

# UI Class definitions

class ExampleModalGuiClass(QtGui.QDialog):
    """"""
    def __init__(self):
        super(ExampleModalGuiClass, self).__init__()
        self.initUI()
    def initUI(self):
        self.result = userCancelled
        # create our window
        # define window     xLoc,yLoc,xDim,yDim
        self.setGeometry(   250, 250, 400, 350)
        self.setWindowTitle("Our Example Modal Program Window")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # create some Labels
        self.label1 = QtGui.QLabel("                       ", self)
        self.label1.setFont('Courier') # set to a non-proportional font
        self.label1.move(20, 20)
        self.label2 = QtGui.QLabel("sample string number two", self)
        self.label2.move(20, 70)
        self.label3 = QtGui.QLabel("                        ", self)
        self.label3.setFont('Courier') # set to a non-proportional font
        self.label3.move(20, 120)
        self.label4 = QtGui.QLabel("can you see this?", self)
        self.label4.move(20, 170)
        # checkboxes
        self.checkbox1 = QtGui.QCheckBox("Left side", self)
        self.checkbox1.clicked.connect(self.onCheckbox1)
        #self.checkbox1.toggle() # will set an initial value if executed
        self.checkbox1.move(210,10)
        #
        self.checkbox2 = QtGui.QCheckBox("Right side", self)
        self.checkbox2.clicked.connect(self.onCheckbox2)
        self.checkbox2.move(210,30)
        # radio buttons
        self.radioButton1 = QtGui.QRadioButton("random string one",self)
        self.radioButton1.clicked.connect(self.onRadioButton1)
        self.radioButton1.move(210,60)
        #
        self.radioButton2 = QtGui.QRadioButton("owt gnirts modnar",self)
        self.radioButton2.clicked.connect(self.onRadioButton2)
        self.radioButton2.move(210,80)
        # set up lists for pop-ups
        self.popupItems1 = ("pizza","apples","candy","cake","potatoes")
        # set up pop-up menu
        self.popup1 = QtGui.QComboBox(self)
        self.popup1.addItems(self.popupItems1)
        self.popup1.setCurrentIndex(self.popupItems1.index("candy"))
        self.popup1.activated[str].connect(self.onPopup1)
        self.popup1.move(210, 115)
        # toggle visibility button
        pushButton1 = QtGui.QPushButton('Toggle visibility', self)
        pushButton1.clicked.connect(self.onPushButton1)
        pushButton1.setAutoDefault(False)
        pushButton1.move(210, 165)
        # text input field
        self.textInput = QtGui.QLineEdit(self)
        self.textInput.setText("cats & dogs")
        self.textInput.setFixedWidth(190)
        self.textInput.move(20, 220)
        # set contextual menu options for text editing widget
        # set text field to some dogerel
        popMenuAction1 = QtGui.QAction(self)
        popMenuAction1.setText("load some text")
        popMenuAction1.triggered.connect(self.onPopMenuAction1)
        # make text uppercase
        popMenuAction2 = QtGui.QAction(self)
        popMenuAction2.setText("uppercase")
        popMenuAction2.triggered.connect(self.onPopMenuAction2)
        # menu dividers
        popMenuDivider = QtGui.QAction(self)
        popMenuDivider.setText('---------')
        popMenuDivider.triggered.connect(self.onPopMenuDivider)
        # remove all text
        popMenuAction3 = QtGui.QAction(self)
        popMenuAction3.setText("clear")
        popMenuAction3.triggered.connect(self.onPopMenuAction3)
        # define menu and add options
        self.textInput.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.textInput.addAction(popMenuAction1)
        self.textInput.addAction(popMenuAction2)
        self.textInput.addAction(popMenuDivider)
        self.textInput.addAction(popMenuAction3)
        # numeric input field
        self.numericInput = QtGui.QLineEdit(self)
        self.numericInput.setInputMask("999")
        self.numericInput.setText("000")
        self.numericInput.setFixedWidth(50)
        self.numericInput.move(250, 220)
        # cancel button
        cancelButton = QtGui.QPushButton('Cancel', self)
        cancelButton.clicked.connect(self.onCancel)
        cancelButton.setAutoDefault(True)
        cancelButton.move(150, 280)
        # OK button
        okButton = QtGui.QPushButton('OK', self)
        okButton.clicked.connect(self.onOk)
        okButton.move(260, 280)
        # now make the window visible
        self.show()
        #
    def onCheckbox1(self):
        text = self.label1.text()
        if text[0]==' ':
            self.label1.setText('left'+text[4:])
        else:
            self.label1.setText('    '+text[4:])
    def onCheckbox2(self):
        text = self.label1.text()
        if text[-1]==' ':
            self.label1.setText(text[:-5]+'right')
        else:
            self.label1.setText(text[:-5]+'     ')
    def onRadioButton1(self):
        self.label2.setText(self.radioButton1.text())
    def onRadioButton2(self):
        self.label2.setText(self.radioButton2.text())
    def onPopup1(self, selectedText):
        if self.label3.text().isspace():
            self.label3.setText(selectedText)
        else:
            self.label3.setText(self.label3.text()+","+selectedText)
    def onPushButton1(self):
        if self.label4.isVisible():
            self.label4.hide()
        else:
            self.label4.show()
    def onPopMenuAction1(self):
        # load some text into field
        self.textInput.setText("Lorem ipsum dolor sit amet")
    def onPopMenuAction2(self):
        # set text in field to uppercase
        self.textInput.setText(self.textInput.text().upper())
    def onPopMenuDivider(self):
        # this option is the divider and is really there as a spacer on the menu list
        # consequently it has no functional code to execute if user selects it
        pass
    def onPopMenuAction3(self):
        # clear the text from the field
        self.textInput.setText('')
    def onCancel(self):
        self.result         = userCancelled
        self.close()
    def onOk(self):
        self.result         = userOK
        self.close()
    def mousePressEvent(self, event):
        # print mouse position, X & Y
        print("X = ", event.pos().x())
        print("Y = ", event.pos().y())
        #
        if event.button() == QtCore.Qt.LeftButton:
            print("left mouse button")
        if self.label1.underMouse():
            print("over the text '"+self.label1.text()+"'")
        if self.label2.underMouse():
            print("over the text '"+self.label2.text()+"'")
        if self.label3.underMouse():
            print("over the text '"+self.label3.text()+"'")
        if self.label4.underMouse():
            print("over the text '"+self.label4.text()+"'")
        if self.textInput.underMouse():
            print("over the text '"+self.textInput.text()+"'")
        if event.button() == QtCore.Qt.RightButton:
            print("right mouse button")
# Class definitions

# Function definitions

# Constant definitions
userCancelled = "Cancelled"
userOK = "OK"

# code ***********************************************************************************

form = ExampleModalGuiClass()
form.exec_()

if form.result==userCancelled:
    pass # steps to handle user clicking Cancel
if form.result==userOK:
    # steps to handle user clicking OK
    localVariable1 = form.label1.text()
    localVariable2 = form.label2.text()
    localVariable3 = form.label3.text()
    localVariable4 = form.label4.text()
#
#OS: Mac OS X
#Word size: 64-bit
#Version: 0.14.3703 (Git)
#Branch: releases/FreeCAD-0-14
#Hash: c6edd47334a3e6f209e493773093db2b9b4f0e40
#Python version: 2.7.5
#Qt version: 4.8.6
#Coin version: 3.1.3
#SoQt version: 1.5.0
#OCC version: 6.7.0
#
``` La meilleure façon d\'utiliser ce code est de le copier dans un éditeur ou un fichier macro FreeCAD et de jouer avec.

## Discussion basée sur le code - Exemple de code non modal 

Tous les widgets spécifiques de l\'exemple modal précédent sont transférés à utiliser dans une fenêtre non modale. La principale différence est que la fenêtre non modale n\'empêche pas l\'utilisateur d\'interagir avec d\'autres fenêtres. Fondamentalement, une fenêtre non modale est une fenêtre qui peut être ouverte et laissée ouverte aussi longtemps que nécessaire sans imposer de restrictions sur les autres fenêtres d\'application. Il existe un petit nombre de différences de code entre les deux qui seront mises en évidence, par conséquent, cet exemple de code est assez bref. Tout ce qui est identique à l\'exemple modal précédent sera omis dans l\'intérêt de garder cette vue d\'ensemble brève. Voici l\'écran GUI non modal généré par la classe PySide:

![](images/PySideScreenSnapshot4.jpg )

### Déclaration d\'importation 

La déclaration d\'importation obligatoire 
```python
from PySide import QtGui, QtCore
``` Il est préférable de le placer en haut du fichier Python.

### Définition de classe 


```python
class ExampleNonmodalGuiClass(QtGui.QMainWindow):
    """"""
    def __init__(self):
        super(ExampleNonmodalGuiClass, self).__init__()
        self.initUI()
    def initUI(self):
```

Ce code est mieux copié textuellement et modifié. L\'essentiel du code est que nous sous-classons la classe QMainWindow de PySide. En adaptant ce code, vous voudrez changer le nom de la classe \"ExampleModalGuiClass\" - assurez-vous de le changer dans les deux endroits (par exemple les lignes 1 et 4).

### Création de fenêtres 


```python
# create our window
# define window xLoc,yLoc,xDim,yDim
self.setGeometry(   250, 250, 400, 150)
self.setWindowTitle("Our Example Nonmodal Program Window")
self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
self.setMouseTracking(True)
```

Évidemment, les dimensions et le titre de nos fenêtres sont différents. Le point principal à noter est la dernière ligne qui permet à PySide de savoir qu\'il doit envoyer les événements de position de la souris au fur et à mesure qu\'ils se produisent. Notez que ces événements ne seront pas envoyés lorsque la souris sera sur un widget comme un bouton car le widget capturera les événements.

### Gestionnaire d\'événements de déplacement de la souris 


```python
def mouseMoveEvent(self,event):
    self.label6.setText("X: "+str(event.x()) + " Y: "+str(event.y()))
```

Ce gestionnaire reçoit l\'événement d\'un déplacement de la souris et en affiche la forme formatée. Testez ce qui se passe lorsqu\'il s\'agit de widgets ou en dehors de la fenêtre.

### Appeler la fenêtre 


```python
form = ExampleNonmodalGuiClass()
```

L\'appel de la fenêtre est un autre domaine de différence par rapport à l\'exemple précédent. Cette fois, une seule ligne est nécessaire pour appeler l\'interface graphique.

## Exemple de code non modal complet 


```python
from PySide import QtGui, QtCore

# UI Class definitions

class ExampleNonmodalGuiClass(QtGui.QMainWindow):
    """"""
    def __init__(self):
        super(ExampleNonmodalGuiClass, self).__init__()
        self.initUI()
    def initUI(self):
        self.result = userCancelled
        # create our window
        # define window     xLoc,yLoc,xDim,yDim
        self.setGeometry(   250, 250, 400, 150)
        self.setWindowTitle("Our Example Nonmodal Program Window")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        # create Labels
        self.label4 = QtGui.QLabel("can you see this?", self)
        self.label4.move(20, 20)
        self.label5 = QtGui.QLabel("Mouse position:", self)
        self.label5.move(20, 70)
        self.label6 = QtGui.QLabel("               ", self)
        self.label6.move(135, 70)
        # toggle visibility button
        pushButton1 = QtGui.QPushButton('Toggle visibility', self)
        pushButton1.clicked.connect(self.onPushButton1)
        pushButton1.setMinimumWidth(150)
        #pushButton1.setAutoDefault(False)
        pushButton1.move(210, 20)
        # cancel button
        cancelButton = QtGui.QPushButton('Cancel', self)
        cancelButton.clicked.connect(self.onCancel)
        cancelButton.setAutoDefault(True)
        cancelButton.move(150, 110)
        # OK button
        okButton = QtGui.QPushButton('OK', self)
        okButton.clicked.connect(self.onOk)
        okButton.move(260, 110)
        # now make the window visible
        self.show()
        #
    def onPushButton1(self):
        if self.label4.isVisible():
            self.label4.hide()
        else:
            self.label4.show()
    def onCancel(self):
        self.result         = userCancelled
        self.close()
    def onOk(self):
        self.result         = userOK
        self.close()
    def mouseMoveEvent(self,event):
        self.label6.setText("X: "+str(event.x()) + " Y: "+str(event.y()))
# Class definitions

# Function definitions

# Constant definitions
global userCancelled, userOK
userCancelled       = "Cancelled"
userOK          = "OK"

# code ***********************************************************************************

form = ExampleNonmodalGuiClass()
#
#OS: Mac OS X
#Word size: 64-bit
#Version: 0.14.3703 (Git)
#Branch: releases/FreeCAD-0-14
#Hash: c6edd47334a3e6f209e493773093db2b9b4f0e40
#Python version: 2.7.5
#Qt version: 4.8.6
#Coin version: 3.1.3
#SoQt version: 1.5.0
#OCC version: 6.7.0
```

## Divers sujets supplémentaires 

Il existe 3 concepts à l\'écran immobilier dans un environnement GUI:

-   espace physique sur l\'écran
-   cadre
-   géométrie

Dans le logiciel, tous sont mesurés en pixels. PySide a la fonction de mesurer dans des unités du monde réel, mais celles-ci ne sont pas fiables car les fabricants n\'ont pas de norme pour la taille des pixels ou le rapport hauteur/largeur.

Le cadre a la taille d\'une fenêtre, y compris ses barres latérales, la barre supérieure (éventuellement avec un menu) et la barre inférieure. La géométrie est l\'espace situé à l\'intérieur du cadre et est donc toujours inférieure ou égale au cadre. À son tour, le cadre est toujours inférieur ou égal à la taille d\'écran disponible.

### Taille d\'écran disponible 


```python
# get screen dimensions (Available Screen Size)
screenWidth     = QtGui.QDesktopWidget().screenGeometry().width()
screenHeight        = QtGui.QDesktopWidget().screenGeometry().height()
# get dimensions for available space on screen
availableWidth      = QtGui.QDesktopWidget().availableGeometry().width()
availableHeight     = QtGui.QDesktopWidget().availableGeometry().height()
```

En général, \"availableHeight\" doit être inférieur à \"screenHeight\" de la hauteur de la barre de menus. Ces 4 valeurs sont basées sur l\'environnement matériel et changeront d\'un ordinateur à l\'autre. Ils ne dépendent d\'aucune taille de fenêtre d\'application.

(Depuis Python 3.9, cet avertissement apparaît lorsque le code ci-dessus est exécuté: **DeprecationWarning: QDesktopWidget.screenGeometry(int screen) const is deprecated**. Un remplacement semble être nécessaire à partir de Python 3.10.)

### Taille et géométrie du cadre 


```python
# set up a variable to hold the Main Window to save some typing...
mainWin = FreeCAD.Gui.getMainWindow()

mainWin.showFullScreen() # no menu bars, every last pixel is given over to FreeCAD
mainWin.geometry()
mainWin.frameSize()
mainWin.frameGeometry()

mainWin.showMaximized() # show maximised within the screen, window edges and the menu bar will be displayed
mainWin.geometry()
mainWin.frameSize()
mainWin.frameGeometry()

mainWin.showNormal() # show at the last non-maximised or non-minimised size (and location)
mainWin.geometry()
mainWin.frameSize()
mainWin.frameGeometry()

mainWin.setGeometry(50, 50, 800, 800) # specifically set FreeCAD main window's size and location, this will become the new setting for 'showNormal()'

mainWin.showMinimized() # FreeCAD will disappear from view after this command...
mainWin.geometry()
mainWin.frameSize()
mainWin.frameGeometry()
```

Ces mêmes commandes peuvent être exécutées sur une fenêtre générée par l\'utilisateur, la syntaxe ne change pas.


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
