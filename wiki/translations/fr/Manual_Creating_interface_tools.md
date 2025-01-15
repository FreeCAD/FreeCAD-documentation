# Manual:Creating interface tools/fr
{{Manual:TOC}}

Dans les deux derniers chapitres, nous avons vu comment créer la géométrie Part ([Création et manipulation de la géométrie](Manual:Creating_and_manipulating_geometry/fr.md)) et créer des objets paramétriques ([Création d\'objets paramétriques](Manual:Creating_parametric_objects/fr.md)). Une dernière pièce manque pour avoir un contrôle total sur FreeCAD: créer des outils qui interagiront avec l\'utilisateur.

Dans de nombreuses situations, il n\'est pas très convivial de construire un objet avec des valeurs nulles, comme nous avons fait avec le rectangle dans le chapitre précédent, puis de demander à l\'utilisateur de remplir la hauteur et la largeur dans le panneau Propriétés. Cela fonctionne pour un très petit nombre d\'objets, mais devient très fastidieux si vous avez beaucoup de rectangles à réaliser. Une meilleure façon serait d\'être capable de donner déjà la hauteur et la largeur lors de la création du rectangle.

Python offre un outil de base permettant à l\'utilisateur de saisir du texte à l\'écran :

text = raw_input("Height of the rectangle?")
print("The entered height is ",text)

Cependant, cela nécessite une console Python en cours d\'exécution et, lors de l\'exécution de notre code à partir d\'une macro, nous ne sommes pas toujours sûrs que la console Python sera activée sur la machine de l\'utilisateur.

L\'[interface utilisateur graphique](https://fr.wikipedia.org/wiki/Interface_graphiquel), ou GUI en anglais, qui comprend les menus, les barres d\'outils, la vue 3D et d\'autres composants visuels de FreeCAD - est conçue pour rendre le logiciel intuitif et accessible. Elle sert de pont entre l\'utilisateur et les fonctionnalités sous-jacentes de FreeCAD, permettant aux utilisateurs occasionnels comme aux experts d\'interagir efficacement avec le programme.

L\'interface graphique de reeCAD est construite à l\'aide de [Qt](https://fr.wikipedia.org/wiki/Qt), une boîte à outils d\'interface graphique puissante et libre qui offre un large éventail de fonctionnalités. Qt offre des éléments essentiels à la conception d\'une interface, tels que des boîtes de dialogue, des boutons, des étiquettes, des champs de saisie de texte et des menus déroulants, collectivement connus sous le nom de « widgets ». Ces widgets constituent la base de l\'expérience utilisateur de FreeCAD.

L\'un des principaux avantages de Qt est sa compatibilité multiplateforme, qui permet à FreeCAD de fonctionner de manière transparente sur différents systèmes d\'exploitation tels que Windows, macOS et Linux. En outre, la flexibilité de Qt permet aux développeurs d\'étendre ou de personnaliser facilement l\'interface de FreeCAD, soit en créant de nouvelles barres d\'outils et de nouveaux menus, soit en construisant des modules entièrement nouveaux qui s\'intègrent au logiciel. Cette adaptabilité garantit que FreeCAD reste à la fois convivial et hautement extensible.

Pour les utilisateurs intéressés par l\'écriture de scripts ou le développement de nouveaux outils, l\'API Python de FreeCAD permet également d\'accéder à de nombreuses fonctionnalités de Qt. Cela signifie que vous pouvez non seulement automatiser des tâches, mais aussi créer des widgets ou des boîtes de dialogue personnalisés qui s\'intègrent directement dans l\'environnement FreeCAD.

Les outils Qt sont très faciles à utiliser à partir de Python, grâce à un module Python appelé [PySide](https://fr.wikipedia.org/wiki/PySide). PySide est la liaison Python officielle pour la bibliothèque Qt, qui permet de créer des widgets et d\'interagir avec eux de manière programmatique. Il permet aux développeurs de concevoir des interfaces, de gérer les entrées de l\'utilisateur (comme la lecture de texte dans des boîtes de saisie) et de définir des actions basées sur les interactions de l\'utilisateur, comme la réponse à la pression d\'un bouton. En utilisant PySide, vous pouvez créer des boîtes de dialogue, des menus et des barres d\'outils personnalisés directement dans FreeCAD, en étendant ses fonctionnalités d\'une manière qui s\'intègre harmonieusement à l\'interface existante.

PySide facilite la connexion des actions de l\'utilisateur à des fonctions spécifiques de votre code. Par exemple, vous pouvez configurer un bouton de sorte que lorsqu\'il est pressé, il déclenche un script pour exécuter une commande ou modifier un objet dans la vue 3D. Cette capacité interactive ouvre des possibilités infinies de personnalisation des flux de travail et d\'automatisation des tâches répétitives.

Qt fournit également un autre outil intéressant appelé [Qt Designer](http://doc.qt.io/qt-4.8/designer-manual.html), aujourd\'hui incorporé à l\'intérieur d'une plus grande application appelée [Qt Creator](https://fr.wikipedia.org/wiki/Qt_Creator). Il permet de concevoir des boîtes de dialogue et des panneaux d\'interface graphiquement au lieu d\'avoir à les coder manuellement. Dans ce chapitre, nous utiliserons Qt Creator pour dessiner un widget de panneau que nous utiliserons dans le **panneau des tâches** de FreeCAD. Vous devrez télécharger et installer Qt Creator à partir de sa page officielle ([official page](https://www.qt.io/ide/)) si vous êtes sur Windows ou Mac. Sur Linux, il est généralement disponible auprès de votre application de gestionnaire de logiciels.

Dans l\'exercice suivant, nous allons d\'abord créer un panneau avec Qt Creator qui demande les valeurs de longueur, de largeur et de hauteur, alors nous allons créer une classe Python autour de lui, qui lira les valeurs entrées par l\'utilisateur à partir du panneau, et créer une boîte avec les dimensions données. Cette classe Python sera ensuite utilisée par FreeCAD pour afficher et contrôler le panneau des tâches :

![](images/Exercise_python_07.jpg )

Commençons par créer le widget. Démarrez Qt Creator, puis menu **Fichier → Nouveau fichier ou projet → Qt → Formulaire Qt Designer → Boîte de dialogue sans boutons**. Cliquez sur **Suivant**, donnez lui un nom de fichier pour l'enregistrer, cliquez sur **Suivant**, laissez tous les champs de projet à leur valeur par défaut (\"\") et **Créer**. Le système de tâches de FreeCAD ajoutera automatiquement les boutons OK/Annuler, c\'est pourquoi nous avons choisi ici une boîte de dialogue sans boutons.

![](images/Exercise_python_06.jpg )

-   Trouvez le **Label** (étiquette) dans la liste du panneau de gauche (dans la section affichage des widgets) et faites-le glisser sur le canevas de notre widget. Double-cliquez sur l\'étiquette juste placée et modifiez son texte en **Longueur**.
-   Cliquez avec le bouton droit de la souris sur la toile du widget, puis choisissez **Lay out → Lay out in a Grid**. Cela mettra notre widget dans une grille avec actuellement une seule cellule, occupée par notre première étiquette. Nous pouvons maintenant ajouter les éléments suivants à gauche, à droite, en haut ou en bas de notre première étiquette, et la grille s'étendra automatiquement.
-   Ajoutez deux autres étiquettes en dessous de la première et modifiez leur texte en **Largeur** et **Hauteur** :

![](images/Exercise_python_08.jpg )

-   Maintenant, placez 3 widgets **Double Spin Box** (dans la section entrée des widgets) à côté de nos étiquettes Longueur, Largeur et Hauteur. Pour chacun d\'entre eux, dans le panneau inférieur droit qui affiche tous les paramètres disponibles pour le Widget sélectionné, localisez **Suffix** et définissez leur suffixe en **mm**. FreeCAD a un widget plus avancé qui peut gérer différentes unités mais cela n\'est pas disponible dans Qt Creator par défaut (néanmoins il peut être ([compilé](Compile_on_Linux/fr#Plugin_Qt_designer.md))), alors, pour l\'instant, nous utiliserons une Double Spin Box standard et nous ajouterons le suffixe \"mm\" pour nous assurer que l\'utilisateur sait dans quelle unité ils fonctionnent :

![](images/Exercise_python_09.jpg )

-   Maintenant, notre widget est terminé, il suffit de nous assurer d\'une dernière chose. Étant donné que FreeCAD devra accéder à ce widget et lire les valeurs Longueur, Largeur et Hauteur, nous devons donner les noms appropriés à ces widgets, afin que nous puissions les récupérer facilement dans FreeCAD. Cliquez sur chacune des boîtes Double Spin, et dans la fenêtre supérieure droite, double-cliquez sur leur nom d\'objet, et modifiez-les par quelque chose de facile à retenir, par exemple : BoxLength, BoxWidth et BoxHeight :

![](images/Exercise_python_10.jpg )

-   Enregistrez le fichier, vous pouvez maintenant fermer Qt Creator, le reste se fera dans Python.
-   Ouvrez FreeCAD et créez une nouvelle macro dans le menu **Macro → Macros → Créer**
-   Collez le code suivant. Assurez-vous de modifier le chemin du fichier pour correspondre à l\'endroit où vous avez enregistré le fichier .ui créé dans QtCreator :


```python
import FreeCAD,FreeCADGui,Part
 
# CHANGE THE LINE BELOW
path_to_ui = "C:\Users\yorik\Documents\dialog.ui"
 
class BoxTaskPanel:
   def __init__(self):
       # this will create a Qt widget from our ui file
       self.form = FreeCADGui.PySideUic.loadUi(path_to_ui)
 
   def accept(self):
       length = self.form.BoxLength.value()
       width = self.form.BoxWidth.value()
       height = self.form.BoxHeight.value()
       if (length == 0) or (width == 0) or (height == 0):
           print("Error! None of the values can be 0!")
           # we bail out without doing anything
           return
       box = Part.makeBox(length,width,height)
       Part.show(box)
       FreeCADGui.Control.closeDialog()
        
panel = BoxTaskPanel()
FreeCADGui.Control.showDialog(panel)
```

Dans le code ci-dessus, nous avons utilisé une fonction commode **PySideUic.loadUi** à partir du module **FreeCADGui**. Cette fonction charge un fichier .ui, crée un widget Qt à partir de celui-ci et écrit les noms, afin que nous puissions accéder facilement au sous-espace par leurs noms (ex: self.form.BoxLength).

La fonction \"accept\" est également une commodité offerte par Qt. Lorsqu\'il existe un bouton \"OK\" dans une boîte de dialogue (ce qui est le cas par défaut lors de l\'utilisation du panneau des Tâches FreeCAD), toute fonction appelée \"accept\" sera automatiquement exécutée lorsque vous appuyez sur le bouton \"OK\". De même, vous pouvez également ajouter une fonction de \"reject\" qui s\'exécute lorsque vous appuyez sur le bouton \"Annuler\". Dans notre cas, nous avons supprimé cette fonction, alors appuyer sur \"Annuler\" provoquera le comportement par défaut (ne rien faire et fermer la boîte de dialogue).

Si nous implémentons une des fonctions d\'acceptation ou de rejet, leur comportement par défaut (ne rien faire et fermer) ne se produira plus. Nous devons donc fermer le panneau de tâches nous-mêmes. Cela se fait avec :


```python
FreeCADGui.Control.closeDialog() 
```

Une fois que nous avons notre BoxTaskPanel qui a 1- un widget appelé \"self.form\" et 2- si nécessaire, les fonctions Accepter et Rejeter, nous pouvons ouvrir le panneau de tâches avec lui, ce qui est fait avec ces deux dernières lignes :


```python
panel = BoxTaskPanel()
 FreeCADGui.Control.showDialog(panel)
```

Notez que le widget créé par **PySideUic.loadUi** n\'est pas spécifique à FreeCAD, c\'est un widget Qt standard qui peut être utilisé avec d\'autres outils Qt. Par exemple, nous aurions pu afficher une boîte de dialogue distincte. Essayez ceci dans la console Python de FreeCAD (en utilisant le chemin correct pour votre fichier .ui bien sûr) :


```python
from PySide import QtGui
 w = FreeCADGui.PySideUic.loadUi("C:\Users\yorik\Documents\dialog.ui")
 w.show()
```

Bien sûr, nous n\'avons ajouté aucun bouton \"OK\" ou \"Annuler\" à notre fenêtre de dialogue, car il a été fait pour être utilisé à partir du panneau de tâches FreeCAD, qui fournit déjà de tels boutons. Il n\'y a donc aucun moyen de fermer la fenêtre de dialogue (autrement que de presser son bouton Fermer la fenêtre). Mais la fonction show () crée une fenêtre de dialogue non modale, ce qui signifie qu\'elle ne bloque pas le reste de l\'interface. Ainsi, alors que notre fenêtre de dialogue est toujours ouverte, nous pouvons lire les valeurs des champs :


```python
w.BoxHeight.value() 
```

Ceci est très utile pour les tests.

Enfin, n\'oubliez pas qu\'il existe beaucoup plus de documentation sur l\'utilisation des widgets Qt dans le Wiki FreeCAD, dans la section [Python Scripting](Power_users_hub.md), qui contient un didacticiel de création de dialogue ([dialog creation tutorial](Dialog_creation.md)), un tutoriel spécial en 3 parties de PySide ([PySide tutorial](PySide.md)) qui couvre le sujet en profondeur.

## Liens pertinents 

-   [Qt Creator Documentation](https://fr.wikipedia.org/wiki/Qt_Creator)
-   [Installing Qt Creator](https://www.qt.io/qt-features-libraries-apis-tools-and-ide/)
-   [Documentation pour utilisateurs avancés](Power_users_hub/fr.md)
-   [Création de dialogue](Dialog_creation/fr.md)
-   [PySide](PySide/fr.md)
-   [Documentation PySide](http://srinikom.github.io/pyside-docs/index.html)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Manual:Creating interface tools/fr
