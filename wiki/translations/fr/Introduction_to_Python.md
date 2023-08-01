# Introduction to Python/fr
## Introduction

Ceci est un petit tutoriel créé pour ceux qui veulent débuter en programmation [Python](https://fr.wikipedia.org/wiki/Python_(langage)). Python est un [langage de programmation](https://fr.wikipedia.org/wiki/Langage_de_programmation) open-source et multiplate-forme. Il a de nombreuses fonctionnalités qui le différencie des autres langages de programmation et est facilement accessible aux nouveaux utilisateurs :

-   Il a été conçu pour être lisible par les êtres humains, le faisant relativement facile à apprendre et comprendre.
-   Il est interprété, ce qui signifie que les programmes n\'ont pas besoin d\'être compilés avant qu\'ils puissent être exécutés. Le code Python peut être exécuté immédiatement même ligne par ligne si vous le désirez.
-   Il peut être intégré dans d\'autres programmes comme un langage de script. FreeCAD possède un interpréteur Python intégré. Vous pouvez écrire du code Python pour manipuler des éléments de FreeCAD. Cela est très puissant et signifie que vous pouvez construire vos propres outils.
-   Il est extensible, vous pouvez simplement installer de nouveaux modules dans votre programme Python et étendre ses fonctionnalités. Par exemple, il y a des modules qui permettent à Python de lire et d\'écrire des images, pour communiquer avec Twitter, pour planifier des tâches exécutées par votre système d\'exploitation, etc.

Ce qui suit est une introduction très basique et en aucun cas un tutoriel complet. Mais espérons le, il fournira un bon point de départ pour une exploration plus approfondie dans FreeCAD et ses mécanismes. Nous vous encourageons fortement à saisir les extraits de code ci-dessous dans un interpréteur Python.



## L'interpréteur

Habituellement, lors de l\'écriture d\'un programme informatique, vous ouvrez un éditeur de texte ou votre environnement de programmation préféré (qui est essentiellement un éditeur de texte avec quelques outils supplémentaires), vous écrivez votre programme, puis vous le compilez et l\'exécutez. Souvent une ou plusieurs erreurs ont été commises lors de la saisie, votre programme ne fonctionnera donc pas. Vous pouvez même recevoir un message d\'erreur vous indiquant ce qui n\'a pas fonctionné. Ensuite, vous revenez à votre éditeur de texte, corrigez les erreurs, exécutez à nouveau et ainsi de suite jusqu\'à ce que votre programme fonctionne comme prévu.

En Python, tout ce processus peut être effectué de manière transparente dans l\'interpréteur Python. L'interpréteur est une fenêtre Python avec une invite de commande, où vous pouvez simplement taper du code Python. Si vous avez installé Python sur votre ordinateur (téléchargez-le depuis le [site Web Python](https://www.python.org/) si vous êtes sous Windows ou Mac, installez le à partir des gestionnaires de paquets, si vous êtes sous GNU/Linux), vous aurez un interpréteur Python dans votre menu de démarrage. Mais comme déjà mentionné, FreeCAD dispose également d\'un interpréteur Python intégré : la [console Python](Python_console/fr.md).

![](images/FreeCAD_Python_console.png ) 
*La console Python FreeCAD*

Si vous ne la voyez pas, cliquez sur le menu Affichage \--\> Panneaux \--\> Console Python. La console Python peut être redimensionnée et également non \"dockée\".

L'interpréteur affiche la version Python installée, puis le symbole `>>>`, qui est l\'invite de commande. L\'écriture de code dans l\'interpréteur est très simple: une ligne correspond à une instruction. Lorsque vous appuyez sur **Entrée**, votre ligne de code est exécutée (après avoir été compilée instantanément et de manière invisible). Par exemple, écrivez ce code :


```python
print("hello")
```


`print()`

est une commande Python qui affiche manifestement quelque chose à l\'écran. Lorsque vous appuyez sur **Entrée**, l\'opération est exécutée et le message `"hello"` apparaît. Si vous faites une erreur, par exemple, écrivez :


```python
print(hello)
```

Python vous le dira immédiatement. Dans ce cas Python ne sait pas ce qu\'est `hello`. Les caractères `" "` spécifient que le contenu est un **string**, un jargon de programmation pour une chaîne de caractères. Sans cela la commande `print()` ne reconnaît pas `hello`. En appuyant sur la flèche vers le haut, vous pouvez revenir à la dernière ligne de code et la corriger.

L\'interpréteur Python dispose également d\'un système d\'aide intégré. Disons que nous ne comprenons pas ce qui s\'est mal passé avec `print(hello)` et que nous voulons des informations spécifiques sur la commande:


```python
help("print")
```

Vous obtiendrez une description longue et complète de tout ce que la commande `print()` peut faire.

Maintenant que vous comprenez l\'interpréteur Python, nous pouvons continuer avec des choses plus sérieuses. 

## Les Variables 

Très souvent dans la programmation vous avez besoin de stocker une valeur sous un nom. C\'est là que les variables entrent en jeu. Par exemple, tapez ceci :


```python
a = "hello"
print(a)
```

Vous comprenez probablement ce qui s\'est passé ici, nous avons enregistré la chaîne de caractères `"hello"` sous le nom `a`. Maintenant que `a` est connu, nous pouvons l\'utiliser n\'importe où, par exemple dans la commande `print()`. Nous pouvons utiliser n\'importe quel nom souhaité, nous avons juste besoin de suivre quelques règles simples, telles que ne pas utiliser d\'espaces ou de ponctuation et ne pas utiliser de mots-clés Python. Par exemple, nous pouvons écrire :


```python
hello = "my own version of hello"
print(hello)
```

Maintenant `hello` n\'est plus un indéfini. Les variables peuvent être modifiées à tout moment, c\'est pourquoi elles sont appelées variables, leur contenu peut varier. Par exemple :


```python
myVariable = "hello"
print(myVariable)
myVariable = "good bye"
print(myVariable)
```

Nous avons changé la valeur de `myVariable`. Nous pouvons également copier des variables :


```python
var1 = "hello"
var2 = var1
print(var2)
```

Il est conseillé de donner des noms significatifs à vos variables. Après un certain temps, vous ne vous souviendrez plus de ce que représente votre variable nommée `a`. Mais si vous l\'avez nommée, par exemple, `myWelcomeMessage` vous vous souviendrez facilement de son objectif. De plus, votre code est un pas supplémentaire vers l\'auto-documentation.

La casse est très importante, 

## Les Nombres 

Bien sûr les programmes Python peuvent traiter toutes sortes de données, pas seulement les chaînes de caractères. Une chose est importante, Python doit savoir de quel type de données il s\'agit. Nous avons vu dans notre exemple print hello que la commande `print()` a reconnu notre chaîne de caractères `"hello"`. En utilisant les caractères `" "`, nous avons spécifié que ce qui suit est une chaîne de caractères.

Nous pouvons toujours vérifier le type de données d\'une variable avec la commande `type()`:


```python
myVar = "hello"
type(myVar)
```

Il nous dira que le contenu de `myVar` est un `'str'`, qui est l\'abréviation de string (chaîne de caractères). Nous avons également d\'autres types de données de base, tels que les nombres entiers et ceux à virgule flottante:


```python
firstNumber = 10
secondNumber = 20
print(firstNumber + secondNumber)
type(firstNumber)
```

Python sait que 10 et 20 sont des nombres entiers, ils sont donc stockés en tant que `'int'` et Python peut faire avec eux tout ce qu\'il peut faire avec des entiers. Voyez les résultats suivants :


```python
firstNumber = "10"
secondNumber = "20"
print(firstNumber + secondNumber)
```

Ici nous avons forcé Python à considérer que nos deux variables ne sont pas des nombres mais des chaînes de caractères. Python peut ajouter deux morceaux de texte ensemble, bien que dans ce cas, bien sûr, ça ne fonctionnera pas en arithmétique. Mais nous parlions des nombres entiers. Il existe également des nombres à virgule flottante. La différence est que les nombres à virgule flottante peuvent avoir une partie décimale et les nombres entiers n\'en ont pas :


```python
var1 = 13
var2 = 15.65
print("var1 is of type ", type(var1))
print("var2 is of type ", type(var2))
```

Les entiers et les nombres à virgule flottante peuvent être mélangés sans problème :


```python
total = var1 + var2
print(total)
print(type(total))
```

Parce que `var2` est un flottant, Python décide automatiquement que le résultat doit également être un flottant. Mais il y a des cas où Python ne sait pas quel type utiliser. Par exemple :


```python
varA = "hello 123"
varB = 456
print(varA + varB)
```

Il en résulte une erreur, `varA` est une chaîne de caractères et `varB` est un entier et Python ne sait pas quoi faire. Cependant, nous pouvons forcer Python à convertir entre les types :


```python
varA = "hello"
varB = 123
print(varA + str(varB))
```

Maintenant que les deux variables sont des chaînes de caractères, l\'opération fonctionne. Notez que nous avons \"stratifié\" `varB` au moment de l\'affichage, mais nous n\'avons pas changé `varB` elle-même. Si nous voulions transformer `varB` de façon permanente en une chaîne de caractères, nous aurions besoin de faire ceci :


```python
varB = str(varB)
```

Nous pouvons également utiliser `int()` et `float()` pour convertir en entier et en flottant si nous voulons :


```python
varA = "123"
print(int(varA))
print(float(varA))
```

Vous devez avoir remarqué que nous avons utilisé la commande `print()` de plusieurs manières. Nous avons affiché des variables, des sommes, plusieurs choses séparées par des virgules et même le résultat d\'une autre commande Python. Peut-être avez vous aussi vu que ces deux commandes :


```python
type(varA)
print(type(varA))
```

ont le même résultat. C\'est parce que nous sommes dans l\'interpréteur et tout est automatiquement affiché. Lorsque nous écrivons des programmes plus complexes qui s\'exécutent en dehors de l\'interpréteur, ils ne s\'affichent pas automatiquement, nous devons donc utiliser la commande `print()`. Dans cet esprit arrêtons de l\'utiliser ici. Désormais, nous écrirons simplement :


```python
myVar = "hello friends"
myVar
```


{{Top}}



## Les Listes (Tableaux) 

Un autre type de données utile est le type **list**. Une liste est une collection d\'autres données. Pour définir une liste nous utilisons `[ ]` :


```python
myList = [1, 2, 3]
type(myList)
myOtherList = ["Bart", "Frank", "Bob"]
myMixedList = ["hello", 345, 34.567]
```

Comme vous pouvez le voir, une liste peut contenir tout type de données. Vous pouvez faire beaucoup de choses avec une liste. Par exemple, compter ses articles :


```python
len(myOtherList)
```

Ou récupérez un élément :


```python
myName = myOtherList[0]
myFriendsName = myOtherList[1]
```

Alors que la commande `len()` renvoie le nombre total d\'éléments dans une liste, le premier élément d\'une liste est toujours à la position `0`, donc dans notre `myOtherList` `"Bob"` sera en position `2`. Nous pouvons faire beaucoup plus avec des listes tel que le tri, la suppression ou l\'ajout d\'éléments.

Fait intéressant, une chaîne de caractères est très similaire à une liste de caractères en Python. Essayez de faire ceci :


```python
myvar = "hello"
len(myvar)
myvar[2]
```

Habituellement ce que vous pouvez faire avec des listes peut également être fait avec les chaînes de caractères. En fait, les listes et les chaînes de caractères sont des séquences.

Outre les chaînes de caractères, les entiers, les flottants et les listes, il existe davantage de types de données intégrés, tels que les dictionnaires et vous pouvez même créer vos propres types de données avec des classes. 

## L\'indentation

Une utilisation importante des listes est la possibilité de « les parcourir » et de faire quelque chose avec chaque élément. Par exemple, regardez ceci :


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for dalton in alldaltons:
    print(dalton + " Dalton")
```

Nous avons itéré (jargon de programmation) à travers notre liste avec la commande `for in` et avons fait quelque chose avec chacun des éléments. Notez la syntaxe spéciale: la commande `for` se termine par `:` indiquant que ce qui suit sera un bloc d\'une ou plusieurs commandes. Dans l\'interpréteur, immédiatement après avoir entré la ligne de commande se terminant par `:`, l\'invite de commande passera à `...`, ce qui signifie que Python sait qu\'il y a plus à venir.

Comment Python saura-t-il combien de lignes suivantes devront être exécutées à l\'intérieur de l\'opération `for in` ? Pour cela, Python s\'appuie sur l\'indentation. Les lignes suivantes doivent commencer par un espace vide, ou plusieurs espaces vides, ou une tabulation, ou plusieurs tabulations. Et tant que l\'indentation reste la même, les lignes seront considérées comme faisant partie du bloc `for in`. Si vous commencez une ligne avec 2 espaces et la suivante avec 4, il y aura une erreur. Lorsque vous avez terminé, écrivez simplement une autre ligne sans retrait, ou appuyez sur **Entrée** pour revenir du bloc `for in`.

L\'indentation facilite également la lisibilité du programme. Si vous utilisez de grandes indentations (par exemple des tabulations au lieu d\'espaces) lorsque vous écrivez un gros programme, vous aurez une vue claire de ce qui est exécuté en son sein. Nous verrons que d\'autres commandes utilisent également des blocs de code indentés.

La commande `for in` peut être utilisée pour de nombreuses choses qui doivent être effectuées plusieurs fois. Elle peut par exemple être combinée avec la commande `range()` :


```python
serie = range(1, 11)
total = 0
print("sum")
for number in serie:
    print(number)
    total = total + number
print("")
print(total)
```

Si vous avez exécuté les exemples de code dans un interpréteur par copier-coller, vous trouverez que le bloc de texte précédent générera une erreur. À la place copiez à la fin du bloc en retrait, c\'est-à-dire à la fin de la ligne `total <nowiki>=</nowiki> total + number`, puis collez-la dans l\'interpréteur. Dans l\'interpréteur appuyez sur **Entrée** jusqu\'à ce que l\'invite à trois points disparaisse et que le code s\'exécute. Copiez ensuite les deux dernières lignes suivies d\'une autre **Enter**. La réponse finale devrait apparaître.

Si vous tapez dans l\'interpréteur `help(range)`, vous verrez :


```python
range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers
```

Ici les crochets indiquent un paramètre facultatif. Cependant tous devraient être des nombres entiers. Ci-dessous nous forcerons le paramètre step à être un entier en utilisant `int()` :


```python
number = 1000
for i in range(0, 180 * number, int(0.5 * number)):
    print(float(i) / number)
```

Un autre exemple `range()` :


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
for n in range(4):
    print(alldaltons[n], " is Dalton number ", n)
```

La commande `range()` a également cette particularité étrange qu\'elle commence par `0` (si vous ne spécifiez pas le numéro de départ) et que son dernier numéro sera le numéro (n-1) du dernier numéro (n) que vous avez spécifié. Bien sûr, cela fonctionne aussi avec d\'autres commandes Python. Par exemple :


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
total = len(alldaltons)
for n in range(total):
    print(alldaltons[n])
```

Une autre utilisation intéressante des blocs d\'indentation est la commande `if`. Cette commande exécute un bloc de code uniquement si une certaine condition est remplie, par exemple :


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Joe" in alldaltons:
    print("We found that Dalton!!!")
```

Bien sûr cela affichera toujours l\'expression, mais essayez de remplacer la deuxième ligne par :


```python
if "Lucky" in alldaltons:
```

Alors rien n\'est affiché. Nous pouvons également préciser avec une instruction `else` :


```python
alldaltons = ["Joe", "William", "Jack", "Averell"]
if "Lucky" in alldaltons:
    print("We found that Dalton!!!")
else:
    print("Such Dalton doesn't exist!")
```


{{Top}}



## Les Fonctions 

Il existe très peu de [commandes Python standard](https://docs.python.org/3/reference/lexical_analysis.html#identifiers) et nous en connaissons déjà plusieurs. Mais vous pouvez créer vos propres commandes. En fait, la plupart des modules supplémentaires que vous pouvez connecter à votre installation Python le font déjà, ils ajoutent des commandes que vous pouvez utiliser. Une commande personnalisée en Python s\'appelle une fonction et se présente comme suit :


```python
def printsqm(myValue):
    print(str(myValue) + " square meters")

printsqm(45)
```

La commande `def()` définit une nouvelle fonction, vous lui donnez un nom et à l\'intérieur de la parenthèse vous définissez les arguments que la fonction utilisera. Les arguments sont des données qui seront transmises à la fonction. Par exemple, observez la commande `len()`. Si vous écrivez simplement `len()`, Python vous dira qu\'il a besoin d\'un argument. Ce qui est évident: vous voulez connaître la longueur de quelque chose. Si vous écrivez `len(maListe)` alors `maListe` est l\'argument que vous passez à la fonction `len()`. Et la fonction `len()` est définie de telle manière qu\'elle sait quoi faire avec cet argument. Nous avons fait la même chose avec notre fonction `printsqm`.

Le nom `myValue` peut être n\'importe quoi et il ne sera utilisé qu\'à l\'intérieur de la fonction. C\'est juste un nom que vous donnez à l\'argument pour que vous puissiez en faire quelque chose. En définissant des arguments, vous indiquez également à la fonction combien en attendre. Par exemple, si vous procédez ainsi :


```python
printsqm(45, 34)
```

Il y aura une erreur. Notre fonction a été programmée pour recevoir un seul argument, mais elle en a reçu deux, `45` et `34`. Essayons un autre exemple:


```python
def sum(val1, val2):
    total = val1 + val2
    return total

myTotal = sum(45, 34)
```

Ici nous avons créé une fonction qui reçoit deux arguments, les additionne et renvoie cette valeur. Renvoyer quelque chose est très utile, car nous pouvons faire quelque chose avec le résultat, comme le stocker dans la variable 

## Les Modules 

Maintenant que vous avez une bonne idée du fonctionnement de Python, vous aurez besoin de savoir encore une chose: comment travailler avec des fichiers et des modules.

Jusqu\'à présent, nous avons écrit les instructions Python ligne par ligne dans l\'interpréteur. Cette méthode n\'est évidemment pas adaptée aux programmes plus importants. Normalement le code des programmes Python est stocké dans des fichiers avec l\'extension **.py**. Ce ne sont que des fichiers de texte brut et n\'importe quel éditeur de texte (Linux gedit, emacs, vi ou même le bloc-notes Windows) peut être utilisé pour les créer et les modifier.

Il existe plusieurs façons d\'exécuter un programme Python. Sous Windows, faites simplement un clic droit sur votre fichier, ouvrez-le avec Python et exécutez-le. Mais vous pouvez également l\'exécuter à partir de l\'interpréteur Python lui-même. Pour cela, l\'interprète doit savoir où se trouve votre programme. Dans FreeCAD, le moyen le plus simple consiste à placer votre programme dans un dossier que l\'interpréteur Python de FreeCAD connaît par défaut, tel que le dossier utilisateur **Mod** de FreeCAD :

-   Sous Linux, il s\'agit généralement de **/home/<username>/.local/share/FreeCAD/Mod/** ({{VersionPlus/fr|0.20}}) ou **/home/<username>/.FreeCAD/Mod/** ({{VersionMinus/fr|0.19}}).
-   Sous Windows, il s\'agit de **%APPDATA%\FreeCAD\Mod\**, qui est généralement **C:\Utilisateurs\<nom_utilisateur>\Appdata\ Roaming\FreeCAD\Mod\**.
-   Sous macOS, il s\'agit généralement de **/Users/<username>/Library/Application Support/FreeCAD/Mod/**.

Ajoutons un sous-dossier appelé **scripts** puis écrivons un fichier comme celui-ci :


```python
def sum(a,b):
    return a + b

print("myTest.py succesfully loaded")
```

Enregistrez le fichier sous **myTest.py** dans le dossier **scripts** et dans la fenêtre de l\'interpréteur, écrivez :


```python
import myTest
```

sans l\'extension **.py**. Cela exécutera le contenu du fichier, ligne par ligne, comme si nous l\'avions écrit dans l\'interpréteur. La fonction sum (somme) sera créée et le message sera affiché. Les fichiers contenant des fonctions, comme les nôtres, sont appelés modules.

Lorsque nous écrivons une fonction `sum()` dans l\'interpréteur, nous l\'exécutons comme ceci :


```python
sum(14, 45)
```

Mais lorsque nous importons un module contenant une fonction `sum()` la syntaxe est un peu différente :


```python
myTest.sum(14, 45)
```

Autrement dit, le module est importé en tant que \"conteneur\" et toutes ses fonctions se trouvent à l\'intérieur de ce conteneur. Ceci est très utile, car nous pouvons importer de nombreux modules et garder tout bien organisé. Fondamentalement, lorsque vous voyez `something.somethingElse`, avec un point entre les deux, cela signifie que `somethingElse` est à l\'intérieur `something`.

Nous pouvons également importer notre fonction sum() directement dans l\'espace principal de l\'interpréteur :


```python
from myTest import *
sum(12, 54)
```

Presque tous les modules le font: ils définissent des fonctions, de nouveaux types de données et classes que vous pouvez utiliser dans l\'interpréteur ou dans vos propres modules Python, car rien ne vous empêche d\'importer d\'autres modules à l\'intérieur de votre module !

Comment savons-nous quels modules nous avons, quelles fonctions sont à l\'intérieur et comment les utiliser (c\'est-à-dire, de quel type d\'arguments elles ont besoin) ? Nous avons déjà vu que Python possède une fonction `help()`. Faites :


```python
help("modules")
```

nous donnera une liste de tous les modules disponibles. Nous pouvons importer n\'importe lequel d\'entre eux et parcourir leur contenu avec la commande `dir()` :


```python
import math
dir(math)
```

Nous verrons toutes les fonctions contenues dans le module `math`, ainsi que des choses étranges nommées `__doc__`, `__file__`, `__name__`. Chaque fonction d\'un module bien construit a un `__doc__` qui explique comment l\'utiliser. Par exemple, nous voyons qu\'il y a une fonction `sin()` à l\'intérieur du module mathématique. Vous voulez savoir comment l\'utiliser ? 
```python
print(math.sin.__doc__)
```

Cela peut ne pas être évident, mais de chaque côté de `doc` se trouvent deux caractères de soulignement.

Et enfin une dernière astuce : lorsque vous travaillez sur du code nouveau ou existant, il est préférable de ne pas utiliser l\'extension de fichier de macro FreeCAD, **.FCMacro**, mais plutôt d\'utiliser l\'extension standard **.py**. En effet, Python ne reconnaît pas l\'extension **.FCMacro**. Si vous utilisez **.py**, votre code peut être facilement chargé avec `import`, comme nous l\'avons déjà vu et également rechargé avec `importlib.reload()` :


```python
import importlib
importlib.reload(myTest)
```

Il existe cependant une alternative :


```python
exec(open("C:/PathToMyMacro/myMacro.FCMacro").read())
```


{{Top}}



## Démarrer avec FreeCAD 

Espérons que vous avez maintenant une bonne idée du fonctionnement de Python et que vous pouvez commencer à explorer ce que FreeCAD a à offrir. Les fonctions Python de FreeCAD sont toutes bien organisées en différents modules. Certains d\'entre eux sont déjà chargés (importés) lorsque vous démarrez FreeCAD. Essayez simplement :


```python
dir()
```


{{Top}}

## Notes

-   FreeCAD a été initialement conçu pour fonctionner avec Python 2. Puisque Python 2 a atteint la fin de sa vie en 2020, le développement futur de FreeCAD se fera exclusivement avec Python 3 et la compatibilité descendante ne sera pas prise en charge.
-   Beaucoup plus d\'informations sur Python peuvent être trouvées dans le [tutoriel Python officiel](https://docs.python.org/3/tutorial/index.html) et la [référence officielle Python](https://docs.python.org/3/reference/).


{{Top}}



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Introduction to Python/fr
