# Python Development Environment/fr
{{TOCright}}

## Un environnement de développement simplifié pour Python au sein de FreeCAD 

_).

Il existe de nombreux outils disponibles pour le développement de programmes en Python. Les facteurs qui compliquent le développement de Python pour une utilisation avec FreeCAD sont de deux ordres : premièrement, les outils n\'ont aucun support pour les nombreuses structures de données et les points d\'accès de FreeCAD ; deuxièmement, ils ne fonctionnent pas \"dans FreeCAD\". Cela signifie que vous pouvez les utiliser pour développer du code en dehors de FreeCAD et ne pas être en mesure de tester dans l\'environnement cible, ou vous pouvez développer Python dans l\'environnement cible (c\'est-à-dire l\'environnement FreeCAD) mais ne pas avoir de support des outils de développement. Aucune de ces solutions n\'est acceptable.

## Contexte

Le développement de logiciels modernes au niveau commercial se fait généralement à l\'aide d\'un ensemble d\'outils génériquement appelés [\'IDE\' pour Environnement de développement](https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement). En général, ces outils comprennent les éléments suivants 3 :

-   éditeur du code source
-   outils d\'automatisation du build
-   débogueur

qui sont standard tandis que les suivantes sont présentes dans certains IDE mais pas dans d\'autres :

-   complétion de code intelligente
-   compilateur, interpréteur ou les deux intégrés
-   système de contrôle de version
-   construction d\'une interface utilisateur graphique (GUI)
-   navigateur de classes
-   navigateur d\'objets
-   diagramme de hiérarchie des classes

Un résumé du statut de ces outils dans FreeCAD est (\'N/D\' signifiant \'Non disponible\') :


<table style="width: 100%" border="1">


<tr>


<td>

éditeur du code source


</td>


<td>

une panoplie d\'éditeurs sont disponibles pour les plates-formes supportées par FreeCAD, discutés ci-dessous


</td>


</tr>


<tr>


<td>

outils d\'automatisation du build


</td>


<td>

N/D


</td>


</tr>


<tr>


<td>

débogueur


</td>


<td>

prévue mais pas encore disponible, il existe des solutions de contournement présentées ci-dessous.


</td>


</tr>


<tr>


<td>

complétion de code intelligente


</td>


<td>

il y en a qui sont disponibles via la console Python, mais c\'est tout ce qui est disponible.


</td>


</tr>


<tr>


<td>

compilateur, interpréteur ou les deux intégrés


</td>


<td>

le compilateur Python est intégré à la console Python mais pas aux éditeurs.


</td>


</tr>


<tr>


<td>

système de contrôle de version


</td>


<td>

N/D - il n\'existe qu\'une seule version du fichier


</td>


</tr>


<tr>


<td>

construction d\'une interface utilisateur graphique (GUI)


</td>


<td>

ce qui est disponible est basique et basé sur le copier/coller de code (voir [PySide](PySide/fr.md))


</td>


</tr>


<tr>


<td>

navigateur de classes


</td>


<td>

N/D


</td>


</tr>


<tr>


<td>

navigateur d\'objets


</td>


<td>

N/D


</td>


</tr>


<tr>


<td>

diagramme de hiérarchie des classes


</td>


<td>

N/D


</td>


</tr>


</table>

De nombreux outils existent pour supporter la fonction ci-dessus pour la programmation Python mais malheureusement ils ne s\'intègrent pas à l\'environnement de développement FreeCAD.

Une liste d\'IDE pour Python se trouve à l\'adresse [Integrated Development Environments for Python](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments).

## Éditeurs

Il y a un éditeur pour Python qui fait partie de FreeCAD, il est lancé en cliquant sur le bouton Editer de Macro -\> [Macros\...](Std_DlgMacroExecute/fr.md). Si vous souhaitez utiliser un éditeur tiers qui tire parti de votre plate-forme, il existe plusieurs éditeurs Python disponibles, pour de nombreuses plates-formes et avec différents niveaux de fonctionnalité. Un avantage de l\'utilisation d\'un éditeur externe est que la zone d\'affichage de FreeCAD peut être utilisée pour la sortie (à la fois graphique et textuelle vers la console) alors que le code source est affiché dans une autre application. Une liste d\'éditeurs Python pour diverses plateformes est disponible à l\'adresse [Python Editors](https://wiki.python.org/moin/PythonEditors).

Remarque : Pour Macintosh, l\'éditeur de texte [TextWrangler](http://www.barebones.com/products/textwrangler/) fonctionne bien. Il possède une mise en évidence du code et d\'excellentes facilités de recherche. Il existe des options pour exécuter des travaux en Python, mais bien sûr, elles ne fonctionnent pas avec l\'environnement FreeCAD.

### Répertoires du code source macro 

Il y a deux répertoires utilisés par FreeCAD, par défaut c\'est le même répertoire mais ils sont pointés par différents points d\'appel dans FreeCAD :

-   FreeCAD.ConfigGet(\"UserAppData\")
-   FreeCAD.ParamGet(\'User parameter:BaseApp/Preferences/Macro\').GetString(\'MacroPath\')

Le premier, \"UserAppData\", pointe vers un répertoire où peuvent être stockés des éléments tels que des fichiers de configuration ou d\'autres fichiers destinés à l\'utilisateur mais que celui-ci ne doit pas modifier.

Le second \"MacroPath\" pointe vers un répertoire où sont stockés les fichiers Python qui sont des fichiers macro pour FreeCAD. Pour marquer un fichier Python comme un fichier macro pour FreeCAD, l\'extension du fichier est modifiée de \".py\" à \".FCMacro\".

Par défaut, ces deux répertoires sont au même endroit, mais ce n\'est pas nécessaire. Il peut être pratique de modifier l\'emplacement des fichiers de macro (\*.FCMacro) à un autre endroit.

La modification des fichiers situés dans \"MacroPath\" est simple, l\'éditeur de texte s\'en chargera. Pour faciliter l\'utilisation des fichiers macro de FreeCAD, il est conseillé de conserver tous les fichiers macro dans le répertoire indiqué par \"MacroPath\".

Pour modifier le répertoire \"MacroPath\", utilisez Outils-\>Editer paramètres et sélectionnez ensuite Preferences/Macro/MacroPath où le texte peut être double-cliqué et édité. Il est également possible de modifier le répertoire \"MacroPath\" par le code :


```python
FreeCAD.ParamGet('User parameter:BaseApp/Preferences/Macro').SetString('MacroPath','/me/myself/and/I')
```

## Débogueur


**'''Un débogueur est prévu pour FreeCAD et ces étapes sont une solution de contournement jusqu'à ce qu'il soit disponible. Voir github.com/mumme74/FreeCAD/tree/editor_fixes'''**

Les [Débogueurs](https://en.wikipedia.org/wiki/Debugger) fournissent généralement deux principales fonctionnalités (parmi d\'autres) :

-   des points d\'arrêt dans le code source
-   l\'inspection des variables

Les **points d\'arrêt** sont des \'pièges\' placés dans le code si le chemin d\'exécution du code rencontre l\'un de ces points d\'arrêt alors l\'exécution est arrêtée ou suspendue. Notez que l\'exécution n\'est pas arrêtée car lorsqu\'un programme est arrêté, toutes les informations résidant en mémoire, comme les variables, sont perdues. Pendant que le programme est suspendu, le contenu des variables peut être inspecté et parfois modifié (ce qui dépend de la capacité du débogueur). En général, le code source ne peut pas être modifié, bien que certains environnements le permettent. Lorsqu\'il est prêt, l\'exécution du code source peut être reprise. De nombreux points d\'arrêt peuvent être placés dans le code et de nombreuses suspensions à travers les points d\'arrêt peuvent se produire. Le but du débogueur est de s\'assurer que l\'exécution avec les points d\'arrêt et les suspensions est fonctionnellement identique à l\'exécution sans points d\'arrêt.

Les **Inspections de variables** sont disponibles pendant la suspension de l\'exécution causée par un point d\'arrêt. Généralement, le contenu des variables peut être visualisé, de nombreux débogueurs prennent également en charge l\'édition du contenu avant la reprise de l\'exécution.

Bien qu\'un débogueur entièrement fonctionnel soit prévu pour FreeCAD, il n\'est pas encore disponible. Cette section détaillera quelques solutions de contournement pour l\'intérim jusqu\'à ce que le débogueur soit disponible.

### Points d\'arrêt 

L\'implémentation de points d\'arrêt implique un niveau de code de supervision qui administre l\'exécution du code en cours de développement. Un tel niveau de code pour le développement Python dans FreeCAD n\'est pas disponible actuellement. Comme succédané, le code suivant est une option. Au lieu de suspendre l\'exécution, le code arrêtera complètement l\'exécution en divisant un nombre par zéro. C\'est vraiment une option très limitée comparée à un point d\'arrêt du débogueur, et cette option n\'est utile que si elle est utilisée avec la routine montrée dans la section suivante \'Inspection des variables\'.

**Breakpoint Code** 
```python
def breakpoint(*args):
    # this routine will print an optional parameter on the console and then stop execution by diving by zero
    # e.g. breakpoint()
    # e.g. breakpoint("summation module")
    #
    if len(args)>0:
        FreeCAD.Console.PrintMessage('Breakpoint: '+str(args[0])+"\n")
    hereWeStop = 12/0
    
```

**Traceback de la console**

Lorsqu\'un programme échoue au cours de son exécution, Python génère ce que l\'on appelle un traceback qui répertorie l\'ordre d\'exécution du programme (c\'est-à-dire quel programme a appelé quel programme dans quel ordre).

Pour l\'exemple de code


```python
breakpoint('amalgamation routine')
```

nous obtenons la trace suivante :


```python
Breakpoint: amalgamation routine
Traceback (most recent call last):
  File "/Users/wylbur/Library/Preferences/FreeCAD/testStub.FCMacro", line 40, in <module>
    breakpoint()
  File "/Users/wylbur/Library/Preferences/FreeCAD/myNewMacro.FCMacro", line 28, in breakpoint
    hereWeStop = 12/0
ZeroDivisionError: integer division or modulo by zero
```

En lisant le traceback, nous pouvons déterminer que :

-   un message \'Breakpoint : amalgamation routine\' a été envoyé par le point d\'arrêt qui a la chaîne \'amalgamation routine\'.
-   L\'erreur d\'exécution s\'est produite à la ligne 28 du module \'myNewMacro\'.
-   la routine \'myNewMacro\' a été appelée à partir de la ligne 40 du module \'testStub\'.

En supposant que la chaîne passée à l\'appel du point d\'arrêt est significative, l\'emplacement du point d\'arrêt peut être facilement déterminé. Notez que dans un système complexe, la traceback peut contenir des dizaines, voire des centaines d\'entrées.

Pour devenir efficace avec ces points d\'arrêt, passez à la section suivante.

### Inspection des variables 

La deuxième fonctionnalité principale d\'un débogueur est d\'examiner et éventuellement de modifier le contenu des variables. Encore une fois, jusqu\'à ce que le débogueur FreeCAD pour Python soit prêt, nous devons dépendre de solutions de contournement.

Une caractéristique du système FreeCAD est la mise à disposition de variables globales. Ces variables sont créées par le code Python et existent dans la mémoire de FreeCAD jusqu\'à ce que l\'utilisateur quitte FreeCAD. La forme de ces variables est :


```python
FreeCAD.myVariable = 123
```

L\'instruction crée une variable Python dans la mémoire de FreeCAD qui est entièrement accessible au code Python. En fait, elle se comporte de manière identique à une variable Python normale. Pourtant, après la fin de l\'exécution du code Python, qu\'il soit exécuté en tant que macro ou par la console, il y aura une variable \'FreeCAD.myVariable\' restant en mémoire avec la valeur 123. En entrant :


```python
>>> FreeCAD.myVariable
123
```

produira le contenu de la variable sur la console. Cette valeur restera dans FreeCAD jusqu\'à ce qu\'elle soit modifiée ou que l\'utilisateur quitte FreeCAD. Cela signifie que la valeur est présente et disponible pour qu\'un programme Python ultérieur puisse la lire. A tout moment, elle peut être vérifiée depuis la console en tapant son nom. Donc un programme appelé \'Program A\':


```python
# program A
myListVariable = list()
myListVariable.append(123)
myListVariable.append('abc')
FreeCAD.myVariable = myListVariable
```

peut s\'exécuter et charger des valeurs dans la variable globale. Plus tard, un deuxième programme appelé \'Program B\' peut s\'exécuter et récupérer la valeur :


```python
myOtherVariable = FreeCAD.myVariable
# further calculations involving myOtherVariable
```

On peut supposer que \'Program B\' effectue ensuite des calculs impliquant les valeurs laissées dans FreeCAD.myVariable. A tout moment l\'utilisateur peut taper sur la console pour inspecter le contenu de la variable :


```python
>>> FreeCAD.myVariable
[123, 'abc']
>>> 
```

Un fait important à connaître avec les variables globales de FreeCAD est qu\'elles existent en mémoire et sont perdues lorsque le programme est quitté. Elles ne sont pas sauvegardées avec les documents mais existent uniquement en mémoire.

### Utilisation

Ceci nous amène à un point où nous pouvons combiner les deux étapes et les utiliser pour tracer les erreurs dans le code. C\'est un peu lourd à utiliser mais ce n\'est qu\'une option jusqu\'à ce que le débogueur de FreeCAD soit prêt.

Le plus simple est sans doute de présenter un exemple, disons que le programme suivant est en cours de débogage :


```python
def monthCounter():
    # program to calculate the number of months in the year
    signsInTheZodiac = 12
    numberOfSeasons = 3
    numberOfCompassPoints = 5
    #
    temporaryVariable1 = signsInTheZodiac + numberOfSeasons
    numberOfMonths = temporaryVariable1 - numberOfCompassPoints
    #
    FreeCAD.Console.PrintMessage(numberOfMonths)
```

L\'exécution du programme sur la console donne des résultats :


```python
>>> monthCounter()
10
```

ce qui n\'est pas ce que nous attendions ! En supposant que nous ne sommes pas en mesure de voir les erreurs, nous pouvons utiliser notre point d\'arrêt et notre examinateur de variables peu sophistiqué comme suit. Nous pouvons insérer une ligne pour copier la valeur de la variable qui nous préoccupe dans une variable globale, puis nous pouvons placer un point d\'arrêt pour stopper l\'exécution à cet endroit :


```python
def monthCounter():
    # program to calculate the number of months in the year
    signsInTheZodiac = 12
    numberOfSeasons = 3
    numberOfCompassPoints = 5
    #
    temporaryVariable1 = signsInTheZodiac + numberOfSeasons
    FreeCAD.saveMyVariable = temporaryVariable1 # <<<<<<<<<<< first inserted line
    breakpoint('is this assignment faulty?') # <<<<<<<<<<<<<< second inserted line
    numberOfMonths = temporaryVariable1 - numberOfCompassPoints
    #
    FreeCAD.Console.PrintMessage(numberOfMonths)
```

Maintenant, lorsque nous exécutons le programme, nous obtenons :


```python
>>> monthCounter()
Breakpoint: is this assignment faulty?
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "<input>", line 9, in monthCounter
  File "<input>", line 5, in breakpoint
ZeroDivisionError: integer division or modulo by zero
>>> 
```

Les choses n\'ont probablement pas l\'air très bonnes, mais ce que nous pouvons faire maintenant est d\'inspecter la valeur de la variable Python \'temporaryVariable1\' comme nous avons assigné sa valeur à la variable globale \'FreeCAD.saveMyVariable\' :


```python
>>> FreeCAD.saveMyVariable
15
>>>
```

En nous rappelant que la variable \'FreeCAD.saveMyVariable\' contient la valeur de la variable Python \'temporaryVariable1\', nous pouvons maintenant déterminer l\'erreur dans la valeur et commencer à remonter le temps pour déterminer l\'origine de l\'erreur. Lorsque nous regardons \'FreeCAD.saveMyVariable\', il est important de réaliser que la variable \'temporaryVariable1\' n\'est plus disponible - elle a été récupérée par le système Python.

Une fois que l\'erreur a été localisée dans la déclaration


```python
numberOfSeasons = 3
```

et corrigée en :


```python
numberOfSeasons = 4
```

Ensuite, nous pouvons relancer le programme, et obtenir la valeur \'11\', ce qui n\'est toujours pas correct. Nous pouvons faire plus d\'assignations aux variables globales de FreeCAD, avoir plusieurs points d\'arrêt (bien que le premier rencontré arrête l\'exécution).


```python
def monthCounter():
    # program to calculate the number of months in the year
    signsInTheZodiac = 12
    numberOfSeasons = 4
    numberOfCompassPoints = 5
    #
    temporaryVariable1 = signsInTheZodiac + numberOfSeasons
    FreeCAD.saveMyVariable1 = temporaryVariable1
    #breakpoint('first assignment')
    numberOfMonths = temporaryVariable1 - numberOfCompassPoints
    FreeCAD.saveMyVariable2 = numberOfMonths
    breakpoint('second assignment')
    #
    FreeCAD.Console.PrintMessage(numberOfMonths)
```

Nous avons maintenant deux points d\'arrêt (bien que l\'un soit commenté) et deux variables globales FreeCAD utilisées. Il n\'y a pas de limite pratique aux variables globales disponibles dans FreeCAD, il n\'y a donc pas besoin d\'économiser inutilement. Nous pouvons maintenant produire ce qui suit sur la console :


```python
>>> FreeCAD.saveMyVariable1
10
>>> FreeCAD.saveMyVariable2
11
>>> 
```

Quelques points concernant l\'utilisation des variables globales de FreeCAD :

-   Python traite ces variables de la même manière que n\'importe quelle autre variable Python.
-   ces variables peuvent contenir tout type de données Python - tout ce qu\'une variable Python normale pourrait contenir.
-   ces variables peuvent être utilisées pour \'faire ressortir\' le contenu d\'une variable Python afin que nous puissions le voir.
-   ces variables peuvent également être utilisées pour \'fournir\' des valeurs à une variable Python en définissant leur valeur depuis la console avant d\'exécuter une routine, ou en la définissant dans un programme Python précédent.
-   Ces variables peuvent être utilisées pour transmettre des données entre deux programmes qui s\'exécutent à des moments différents.
-   (pour répéter) ces variables sont seulement pour la durée de la session FreeCAD, une fois que l\'utilisateur quitte FreeCAD alors les variables sont perdues.

### Variable Watcher 

Il existe un utilitaire [Global Variable Watcher](Macro_Global_Variable_Watcher/fr.md) pour aider à surveiller les variables globales de FreeCAD. Il peut afficher le contenu d\'une variable globale soit sur demande, soit sur une base temporelle.

### Conflit d\'espace de nom 

Une chose dont il faut être conscient est qu\'il n\'y a pas de gestion des noms de variables globales par FreeCAD, il y a donc la possibilité de changer une variable depuis le système ou un autre morceau de code. Par conséquent, c\'est une bonne idée de préfixer vos variables avec quelque chose d\'unique comme le nom de la routine. Par exemple pour utiliser une variable d\'une routine appelée \'alpha1\' le nom global pourrait être \'FreeCAD.alpha1MyVariable\'.

## Structure de codage 

Lors du développement de petits morceaux de code Python dans FreeCAD, il peut être suffisant d\'utiliser la console Python. Cependant, lorsque le nombre de lignes de code augmente, il est plus logique de les stocker dans un fichier. Python peut être dans n\'importe quel fichier se terminant par l\'extension \".py\", cependant FreeCAD fournit également un mécanisme appelé Macro pour stocker de tels programmes et interagir avec eux (par ex. édition, exécution). Python dans les fichiers réguliers \'.py\' ne peut être exécuté qu\'à partir de la console Python alors que Python dans les fichiers macro \'.FCMacro\' peut être exécuté à partir de l\'interface FreeCAD pour l\'exécution des macros. Un inconvénient de l\'interface de menu de FreeCAD est qu\'elle est basée sur un menu avec une fenêtre de contrôle et peut potentiellement causer un certain encombrement sur l\'interface graphique à l\'écran.

Une approche plus simple consiste à prendre le code Python et, au lieu de le lancer à partir du menu Macro de FreeCAD, à le lancer à partir d\'une barre d\'outils. Une routine Python liée à un bouton d\'une barre d\'outils peut être exécutée en un seul clic. De plus, comme les barres d\'outils sont des fenêtres flottantes, elles n\'encombrent pas l\'affichage à l\'écran. En fait, si la fenêtre FreeCAD est inférieure à la taille physique de l\'écran, la barre d\'outils peut être laissée flottante en dehors de la fenêtre FreeCAD. Ceci est bénéfique lorsque des captures d\'écran sont nécessaires pour l\'affichage de FreeCAD. De même, la barre d\'outils peut être beaucoup plus petite que la fenêtre de contrôle des macros affichée par le menu Macro de FreeCAD.

La connexion d\'une macro à un bouton d\'une barre d\'outils est traitée dans [Comment installer des macros](How_to_install_macros/fr.md) et [Personnaliser la barre d\'outils](Customize_Toolbars/fr.md). Cela peut prendre plusieurs minutes pour connecter une macro à un bouton de la barre d\'outils, sélectionner une icône, etc. Ce n\'est pas toujours nécessaire, car il arrive que l\'on veuille simplement étoffer rapidement un morceau de code qui sera ensuite intégré dans un autre code. Dans ce cas, un test stub peut être utile. Il n\'y a pas de véritable définition de ce qu\'est un test stub, cela dépend vraiment de la personne et du domaine d\'application. Un exemple est présenté ci-dessous :


```python
#
#           TEST
#           TEST stub to clip any code onto...
#           TEST
#
################################
# routine to <description goes here>
"""
script does <long winded description goes here>
"""

# import statements
import FreeCAD
from FreeCAD import Base
import math, collections
from PySide import QtGui, QtCore

# UI Class definitions

# Class definitions

# Functions definitions

# Constant definitions

# code ***********************************************************************************

QtGui.QMessageBox.information(None,"","Test Stub")

##########################################################################################
##########################################################################################
##########################################################################################
```

Ce test stub sert également de modèle pour le code avec des emplacements définis pour les différents aspects d\'un grand programme Python. Lorsqu\'il est exécuté, le programme test stub génère simplement un message indiquant son nom et se termine. En utilisant un test stub, tout code de ligne principale écrit est placé à la toute fin du fichier avec le code pour la définition des classes, des fonctions, etc\... placé dans les sections précédentes. Le modèle peut facilement être modifié pour s\'adapter à la situation. Il est évident que pour un programme de 5 lignes, il n\'y a pas besoin d\'une telle quantité de documentation.

En gardant un bouton en permanence sur une barre d\'outils et en liant ce bouton au test stub, il y a toujours une zone pour écrire du code et l\'exécuter immédiatement. L\'exécution sera indépendante de la console Python. De même, l\'exécution peut être indépendante de l\'interface graphique de l\'écran. La sortie du programme en cours de développement apparaîtra comme il se doit à l\'écran sans aucun autre artefact de l\'environnement de programmation. La console Python peut être cachée pour augmenter la surface d\'affichage ou utilisée à d\'autres fins si nécessaire. Lorsque l\'exécution est gérée par le bouton de la barre d\'outils, la console n\'est pas nécessaire.

Lorsque le code est terminé, il peut être simplement copié/collé dans un autre fichier et le test stub est laissé vide jusqu\'à la prochaine fois qu\'il sera utilisé.

Plusieurs morceaux de code peuvent être développés à l\'aide du même test stub avec un peu de code supplémentaire pour fournir plusieurs boutons qui se trouve à [PySide: Exemples pour débutants - Plus de 2 boutons](PySide_Beginner_Examples/fr#Plus_de_2_boutons.md).

**Plus de support pour PySide**

Pour plus d\'informations sur l\'utilisation de l\'interface graphique PySide, consultez la page [PySide](PySide/fr.md).

**Plus de support pour la programmation en Python**

Pour plus d\'aide avec le codage Python, il existe une macro écrite pour aider au développement du code Python, elle se trouve à [Python Assistant Window](Macro_Python_Assistant_Window/fr.md).

## Mettre tout ça ensemble 

La gestion de l\'écran peut être un défi lors du développement d\'un code qui a une sortie graphique complexe et détaillée comme le fait FreeCAD. Le système suivant fonctionne bien :

-   FreeCAD pour la console, le rapport, l\'affichage GUI
-   barre d\'outils pour lancer le code en cours de développement
-   éditeur externe pour modifier le code
-   PAW (Python Assistant Window) pour faciliter la génération du code Python.

**Gestion de l\'écran**

Si le test stub fonctionne à partir d\'une barre d\'outils et qu\'un éditeur externe est utilisé, la disposition des fenêtres à l\'écran sera la suivante :

![](images/PythonDevelopmentEnvironment.jpg )

\"tree\" dans le diagramme fait référence aux navigateurs Combi ou Arboscence, la console Python et la Vue rapport sont combinées dans la fenêtre inférieure et peuvent être sélectionnées par des boutons. L\'utilisation sélective des outils permet d\'optimiser le flux de développement, ce qui n\'est qu\'une idée parmi d\'autres. L\'adaptation se fait sur une base personnelle.

## Liens divers 

Quelques autres liens sur les IDE pour Python qui pourraient être intéressants sont :

-   [Comparison of Python IDEs for Development](http://www.pythoncentral.io/comparison-of-python-ides-development/)
-   [Choosing the Best Python IDE](http://pedrokroger.net/choosing-best-python-ide/)
-   [Your Development Environment](http://docs.python-guide.org/en/latest/dev/env/)
-   [PyCharm Community Edition IDE](http://www.jetbrains.com/pycharm/)




_ _

---
[documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > Python Development Environment/fr
