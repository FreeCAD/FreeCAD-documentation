 


{{Manual:TOC/fr}}

[Python](https://fr.wikipedia.org/wiki/Python_(langage)) est un langage populaire, open source, souvent embarqué et utilisé comme langage de script dans des applications, comme c\'est le cas dans FreeCAD. Il possède également des qualités qui le rendent particulièrement attractif pour nous, utilisateurs de FreeCAD: il est facile à apprendre, surtout pour les novices en programmation et il est embarqué dans d\'autres logiciels. Cela en fait un outil essentiel à apprendre puisqu\'il pourra être utilisé dans d\'autres applications tels que [Blender](http://www.blender.org), [Inkscape](http://www.inkscape.org) ou [GRASS](http://grass.osgeo.org/).

FreeCAD fait une utilisation intensive de Python. Avec lui, vous pouvez accéder et contrôler quasiment toutes les fonctions de FreeCAD. Vous pouvez, par exemple, créer de nouveaux objets, outils et panneaux. Certains ateliers de FreeCAD et la plupart des ateliers supplémentaires sont entièrement programmés en python. FreeCAD possède une console Python améliorée disponible depuis le menu **Affichage-\>Panneaux-\>Console Python**. Elle est souvent utile pour réaliser des opérations pour lesquelles il n\'y a pas encore de boutons dans la barre d\'outils, pour vérifier des formes ou pour faire des tâches répétitives :

![](images/Exercise_python_01.jpg )

Mais la console Python a un autre rôle très important: chaque fois qu\'un bouton de la barre d\'outils est cliqué ou qu\'une autre opération est réalisée dans FreeCAD, du code Python est affiché puis exécuté dans la console. En laissant la console Python ouverte, vous pouvez littéralement voir le code Python se dérouler au fur et à mesure de votre travail, et, en un rien de temps, sans même vous en rendre compte, vous apprendrez le langage Python.

FreeCAD possède également un [système de macros](Macros/fr.md) qui vous permet d'enregistrer vos actions pour les rejouer plus tard. Ce système utilise la console Python en enregistrant simplement ce qui y est fait.

Dans ce chapitre, nous allons découvrir de façon très générale le langage Python. Si vous souhaitez en apprendre plus, la documentation wiki de FreeCAD possède une section pour utilisateurs avancés en [programmation Python](Power_users_hub/fr.md).

### Ecrire du code Python 

Il y a deux manières d\'écrire du code Python dans FreeCAD: à partir de la console Python,

-   dans la barre de menus, cliquez sur **Affichage-\> Vues-\> Console Python**,
-   ou depuis l\'éditeur de macros **Outils-\> Macros**.

Dans la console Python, vous écrivez les lignes de code Python, une par une. Elles seront exécutées lorsque vous validerez avec la touche **ENTREE** tandis que les macros peuvent contenir un script plus complexe composé de plusieurs lignes, qui est exécuté uniquement lorsque la macro est lancée à partir de la même fenêtre Macros **Exécutez la macro dans l'éditeur** (triangle vert).

Dans ce chapitre, vous pourrez utiliser les deux méthodes, mais il est fortement recommandé d\'utiliser la console Python car elle vous informe instantanément des erreurs que vous faites.

Si c\'est la première fois que vous programmez en Python, pensez à lire cette courte [introduction au langage Python](Introduction_to_Python/fr.md) avant d\'aller plus loin. Cela rendra les concepts de base de Python plus clairs.

### Manipuler des objets FreeCAD 

Commençons pas créer un nouveau document vide:

doc = FreeCAD.newDocument()

Si vous tapez ceci dans la console Python de FreeCAD, vous remarquerez que dès que vous entrez \"FreeCAD.\" (le mot FreeCAD suivi d\'un point), une fenêtre apparaît permettant rapidement de compléter le reste de votre ligne. Encore mieux, chaque entrée dans la liste des auto complétions a une bulle d'aide expliquant ce qu\'elle fait. Il est donc très facile d\'explorer la fonctionnalité disponible. Avant de choisir \"newDocument\", regardez les autres options disponibles.

![](images/Exercise_python_02.jpg )

Dès que vous appuyez sur **Entrée**, notre nouveau document est créé. C\'est équivalent à cliquer sur le bouton \"nouveau document\" dans la barre d\'outils. En Python, le point sert à indiquer quelque chose qui est contenu dans quelque chose d\'autre (newDocument est une fonction qui se trouve dans le module FreeCAD). La fenêtre qui s\'affiche vous montre donc tout ce qui est contenu dans \"FreeCAD\". Si vous souhaitiez ajouter un point après le nouveau document, au lieu des parenthèses, cela vous montrerait tout ce qui est contenu dans la nouvelle fonction newDocument. Les parenthèses sont obligatoires lorsque vous appelez une fonction Python, comme celle-ci. Nous allons mieux illustrer cela ci-dessous.

Revenons maintenant à notre document. Voyons ce que nous pouvons en tapant ce qui suit et explorons les options disponibles:

doc.

Habituellement, les noms commençant par une lettre majuscule sont des attributs: ils contiennent une valeur. Les noms commençant par une petite lettre sont des fonctions (également appelées méthodes): ils \"font quelque chose\". Les noms commençant par un trait de soulignement sont habituellement là pour le fonctionnement interne du module, il est préférable d\'ignorer ces derniers. Utilisons l\'une des méthodes pour ajouter un nouvel objet à notre document:

box = doc.addObject("Part::Box","myBox")

Notre boîte est ajoutée dans l\'arborescence mais rien ne se passe encore dans la vue 3D car quand on travaille avec Python, le document n\'est jamais recalculé automatiquement. Nous devons le faire manuellement chaque fois que nous avons besoin :

doc.recompute()

Voilà, notre boîte est apparue dans la vue 3D. De nombreux boutons de la barre d\'outils qui ajoutent des objets dans FreeCAD ont deux fonctions: ils ajoutent l\'objet et recalculent. Si vous avez activé l'option \"montrer les commandes du script dans la console Python\", essayez maintenant d\'ajouter une sphère avec le bouton approprié dans l'atelier Part et vous verrez les deux lignes du code Python exécutées l\'une après l\'autre.

Vous pouvez obtenir une liste de tous les types d\'objets possibles, comme Part :: Box:

doc.supportedTypes()

Voyons maintenant le contenu de notre boîte:

box.

Vous allez voir immédiatement quelques propriétés intéressantes telles que:

box.Height 

Cela imprime la hauteur actuelle de notre boîte. Maintenant, essayons de changer cela :

box.Height = 5 

Si vous sélectionnez votre boîte avec la souris, vous verrez cela dans le panneau des propriétés, sous l'onglet **Données**, notre propriété **Hauteur** apparaître avec la nouvelle valeur. Toutes les propriétés d\'un objet FreeCAD qui apparaissent dans les onglets **Données** et **Affichage** sont directement accessibles par Python aussi, par leur noms, comme nous l\'avons fait avec la propriété Height. Les propriétés des données sont accessibles directement depuis l'objet lui-même, par exemple :

box.Length 

Les propriétés de vue sont stockées dans un **ViewObject**. Chaque objet FreeCAd possède un ViewObject qui stocke les propriétés de visualisation de l\'objet. Lors de l\'exécution de FreeCAD sans son interface graphique (par exemple lors du lancement par un terminal avec l'option de ligne de commande -c ou l\'utilisation à partir d\'un autre script Python), le ViewObject n\'est pas disponible puisqu\'il n\'y a pas de support visuel.

Essayez l\'exemple suivant pour accéder à la couleur de trait de notre boîte:

box.ViewObject.LineColor 

### Vecteurs et emplacements 

Les vecteurs sont un concept fondamental dans n\'importe quelle application 3D. C\'est une liste de 3 nombres (x, y et z) décrivant un point ou une position dans l\'espace 3D. Beaucoup de choses peuvent être faites avec les vecteurs, telles que des ajouts, des soustractions, des projections et bien plus encore. Dans Freecad, les vecteurs fonctionnent comme ceci :

myvec = FreeCAD.Vector(2,0,0)
print(myvec)
print(myvec.x)
print(myvec.y)
othervec = FreeCAD.Vector(0,3,0)
sumvec = myvec.add(othervec)

Une autre caractéristique commune des objets FreeCAD est leur **Positionnement** (placement). Comme nous l\'avons vu dans les chapitres précédents, chaque objet a une propriété de placement qui contient la position (Base) et l\'orientation (Rotation) de l\'objet. Cs propriétés sont faciles de manipuler avec Python, par exemple pour déplacer notre objet:

print(box.Placement)
print(box.Placement.Base)
box.Placement.Base = sumvec
otherpla = FreeCAD.Placement()
otherpla.Base = FreeCAD.Vector(5,5,0)
box.Placement = otherpla

**Lire plus d\'informations**

-   [Python](https://www.python.org/)
-   [Macros](Macros/fr.md)
-   [Introduction à Python](Introduction_to_Python/fr.md)
-   [Tutoriel de scripts Python](Python_scripting_tutorial/fr.md)
-   [Portail d\'utilisation avancée](Power_users_hub/fr.md)





{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
