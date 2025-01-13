# Manual:A gentle introduction/fr
{{Manual:TOC}}

[Python](https://fr.wikipedia.org/wiki/Python_(langage)) est un langage de programmation open-source largement utilisé, reconnu pour sa simplicité, sa polyvalence et sa lisibilité. Il est souvent intégré dans les applications en tant que langage de script, et FreeCAD ne fait pas exception. Cette intégration permet aux utilisateurs d\'automatiser des tâches, de personnaliser des flux de travail et d\'étendre les fonctionnalités du logiciel bien au-delà de son interface graphique.

Python offre plusieurs avantages qui le rendent particulièrement adapté aux utilisateurs de FreeCAD. Il est convivial pour les débutants, avec une syntaxe claire et intuitive qui le rend facile à apprendre, même pour les personnes n\'ayant aucune expérience préalable de la programmation. Cette accessibilité est particulièrement précieuse dans la communauté FreeCAD, où de nombreux utilisateurs viennent d\'horizons divers, tels que l\'ingénierie, l\'architecture et le design, et n\'ont pas de connaissances approfondies en matière de codage.

De plus, l\'adoption généralisée de Python dans d\'autres applications, telles que [Blender](https://www.blender.org) pour la modélisation 3D, [Inkscape](https://www.inkscape.org) pour les graphiques vectoriels, et [GRASS GIS](https://grass.osgeo.org/) pour l\'analyse géospatiale, en fait une compétence essentielle pour tous ceux qui cherchent à étendre leurs capacités de script. La maîtrise de Python dans FreeCAD améliore non seulement votre capacité à créer des outils et des macros personnalisés, mais fournit également des compétences transférables qui peuvent être appliquées à diverses plates-formes logicielles.

Dans FreeCAD, les scripts Python vous permettent de :

-   Automatiser les tâches répétitives pour gagner du temps et réduire les erreurs.
-   Créer des objets paramétriques personnalisés qui s\'adaptent dynamiquement aux changements.
-   Développer des macros et des outils personnalisés adaptés à des flux de travail spécifiques.
-   Interagir avec l\'interface de programmation d\'applications (API) de FreeCAD pour accéder à la géométrie, aux scènes et aux éléments de l\'interface utilisateur et les manipuler par programme.

En utilisant Python, les utilisateurs de FreeCAD peuvent exploiter tout le potentiel du logiciel, le transformant en un outil puissant et flexible adapté à leurs besoins uniques.

FreeCAD comprend une console Python avancée, accessible via **Affichage → Panneaux → Console Python**. Cet outil permet aux utilisateurs d\'effectuer des opérations au-delà de l\'interface graphique, telles que l\'accès aux fonctionnalités avancées, le dépannage de la géométrie et l\'automatisation des tâches. Il enregistre également les commandes Python pour les actions de l\'interface graphique si l\'option *Afficher les commandes des scripts dans la console Python* est activée sous **Édition → Préférences → Python → Macro**). En gardant la console ouverte, vous pouvez regarder le code Python se dérouler au fur et à mesure que vous travaillez, ce qui constitue un moyen intuitif d\'apprendre le langage tout en explorant les capacités de FreeCAD. Enfin, FreeCAD dispose également d\'un [système de macros](Macros/fr.md), qui vous permet d\'enregistrer des actions pour les rejouer plus tard. Ce système utilise également la console Python, en enregistrant simplement tout ce qui y est fait.

![](images/FreeCAD_Python_Console.png )

Dans ce chapitre, nous allons découvrir de façon très générale le langage Python. Si vous souhaitez en apprendre plus, la documentation wiki de FreeCAD possède une section pour utilisateurs avancés en [programmation Python](Power_users_hub/fr.md).



### Ecrire du code Python 

Dans FreeCAD, vous pouvez écrire du code Python de deux manières principales : à travers la console Python (**Affichage → Panneaux → Console Python**) ou en utilisant l\'éditeur de macros (**Macro → Macros → Créer**). La console Python vous permet de saisir des commandes une par une, qui sont exécutées immédiatement après avoir appuyé sur la touche Retour, ce qui la rend idéale pour les tests rapides ou l\'exploration interactive. L\'éditeur de macros, quant à lui, est utilisé pour écrire et enregistrer des scripts plus complexes composés de plusieurs lignes de code. Ces macros peuvent être exécutées dans leur ensemble plus tard à partir de la fenêtre Macros, ce qui constitue un moyen puissant d\'automatiser les tâches répétitives et d\'étendre les fonctionnalités de FreeCAD. Dans ce chapitre, vous pourrez utiliser les deux méthodes, mais il est fortement recommandé d\'utiliser la console Python, car elle vous informera immédiatement de toutes les erreurs que vous faites en tapant.

Si c\'est la première fois que vous programmez en Python, pensez à lire cette courte [introduction au langage Python](Introduction_to_Python/fr.md) avant d\'aller plus loin. Cela rendra les concepts de base de Python plus clairs.



### Manipuler des objets FreeCAD 

Commençons pas créer un nouveau document vide:


```python
doc = FreeCAD.newDocument()
```

Dans la console FreeCAD Python, dès que vous tapez FreeCAD. (le mot « FreeCAD » suivi d\'un point), une fenêtre d\'autocomplétion apparaît. Cette fonction n\'accélère pas seulement votre flux de travail en suggérant des commandes disponibles, mais vous aide également à découvrir de nouvelles fonctions et caractéristiques dans FreeCAD. Chaque entrée de la liste est accompagnée d\'une infobulle expliquant sa fonction, ce qui facilite la compréhension et l\'exploration des fonctionnalités disponibles. Cette fonction d\'autocomplétion est particulièrement utile pour les débutants qui apprennent les scripts Python et pour les utilisateurs avancés qui naviguent efficacement dans la vaste API de FreeCAD. Prenez le temps d\'explorer les options de la fenêtre d\'autocomplétion, vous découvrirez peut-être des commandes qui simplifieront votre flux de travail ou ouvriront de nouvelles possibilités.

![](images/FreeCAD_python_newDocument.png )

Taper **FreeCAD.newDocument()** crée un nouveau document vide dans FreeCAD, tout comme cliquer sur le bouton **Nouveau document** dans la barre d\'outils. Lorsque vous exécutez **doc = FreeCAD.newDocument()**, le nouvel objet document est assigné à la variable **doc**\', ce qui vous permet de le manipuler par programme. En utilisant doc, vous pouvez ajouter des objets, modifier des propriétés ou enregistrer le document.

En Python, le point (.) est utilisé pour indiquer qu\'un élément est contenu dans un autre. Par exemple, **newDocument** est une fonction du **module FreeCAD**, c\'est pourquoi nous écrivons FreeCAD.newDocument. La fenêtre d\'autocomplétion qui apparaît montre tout ce qui est disponible dans le module FreeCAD. Si vous tapez un point après newDocument (sans ajouter les parenthèses), cela affichera tout ce qui appartient à la fonction newDocument. Ceci illustre la façon dont Python organise et accède aux objets et à leurs composants. Il est important de noter que les parenthèses sont obligatoires lors de l\'appel d\'une fonction Python, car elles signalent l\'exécution de la fonction.

Revenons maintenant à notre document. Voyons ce que nous pouvons en tapant ce qui suit et explorons les options disponibles:


```python
doc.
```

Dans FreeCAD, les conventions d\'appellation des commandes Python peuvent vous aider à comprendre leur objectif :

-   Les noms commençant par une lettre majuscule sont généralement des attributs, qui stockent des valeurs ou des données, telles que les propriétés d\'un objet.
-   Les noms commençant par une lettre minuscule sont généralement des fonctions (également appelées méthodes), qui effectuent des actions ou des opérations, telles que la création ou la modification d\'objets.
-   Les noms commençant par un trait de soulignement (\_) sont généralement destinés à un usage interne au module et peuvent être ignorés.

Cette distinction vous aide à naviguer dans l\'API de FreeCAD et à sélectionner la commande appropriée à vos besoins. Par exemple, vous pouvez utiliser une méthode pour ajouter un nouvel objet à un document. La méthode exécute l\'action de création et d\'ajout de l\'objet, tandis que les attributs stockent les propriétés de l\'objet. La compréhension de cette structure facilite l\'exploration des fonctionnalités disponibles, en particulier lors de l\'utilisation de la fonction d\'autocomplétion ou de la lecture d\'infobulles. Ajoutons une boîte.


```python
box = doc.addObject("Part::Box", "myBox")
```

La commande **box = doc.addObject(\"Part::Box\", \"myBox\")** ajoute un nouvel objet box 3D au document. Voici une explication simple :

-   **doc.addObject** : indique à FreeCAD d\'ajouter un nouvel objet au document.
-   **Part::Box** : spécifie le type d\'objet à créer, dans ce cas, une boîte 3D.
-   **myBox** : cette commande attribue un nom au nouvel objet, ce qui permet de l\'identifier et de le référencer plus facilement par la suite.

Le résultat de cette commande est qu\'une boîte apparaît dans le document actif et que la variable boîte stocke une référence à cette boîte afin que vous puissiez la modifier ou interagir avec elle ultérieurement. Notre boîte est ajoutée dans l\'arborescence, mais rien ne se passe encore dans la vue 3D, car lorsqu\'on travaille à partir de Python, le document n\'est jamais recalculé automatiquement. Nous devons le faire manuellement, chaque fois que cela est nécessaire :


```python
doc.recompute()
```

Notre boîte est maintenant apparue dans la vue 3D. De nombreux boutons de la barre d\'outils qui ajoutent des objets dans FreeCAD font en fait deux choses : ajouter l\'objet et recalculer. Essayez maintenant d\'ajouter une sphère avec le bouton approprié dans l\'atelier Part, et vous verrez les deux lignes de code Python s\'exécuter l\'une après l\'autre.

![](images/FreeCAD_python_Sphere.png )

Vous pouvez obtenir une liste de tous les types d\'objets possibles, comme Part :: Box:


```python
doc.supportedTypes()
```

Explorons maintenant le contenu de notre boîte :


```python
box.
```

Vous verrez immédiatement un certain nombre de choses très intéressantes telles que :


```python
box.Height
```

Cela affichera la hauteur actuelle de notre boîte. Maintenant, essayons de changer cela :


```python
box.Height = 5
```

Si vous sélectionnez votre boîte avec la souris, vous verrez cela dans le panneau des propriétés, sous l'onglet **Données**, notre propriété **Hauteur** apparaître avec la nouvelle valeur. Toutes les propriétés d\'un objet FreeCAD qui apparaissent dans les onglets **Données** et **Affichage** sont directement accessibles par Python aussi, par leur noms, comme nous l\'avons fait avec la propriété Height. Les propriétés des données sont accessibles directement depuis l'objet lui-même, par exemple :


```python
box.Length
```

Dans FreeCAD, les propriétés visuelles sont gérées par **ViewObject**. Chaque objet FreeCAD a un ViewObject associé, qui stocke des informations sur la façon dont l\'objet est affiché dans l\'interface graphique, comme la couleur, la transparence ou la visibilité. Cependant, le ViewObject n\'est accessible que lorsque FreeCAD fonctionne avec son interface graphique. Si FreeCAD est lancé dans un mode non graphique, comme à partir d\'un terminal avec l\'option de ligne de commande -c ou lorsqu\'il est utilisé comme bibliothèque Python dans un script externe, le ViewObject n\'est pas disponible. Ceci est dû au fait qu\'il n\'y a pas de représentation visuelle de l\'objet dans ces modes, puisque l\'interface graphique n\'est pas chargée.

Essayez l\'exemple suivant pour accéder à la couleur de trait de notre boîte :


```python
box.ViewObject.LineColor
```



### Vecteurs et emplacements 

Les vecteurs sont un concept fondamental dans toute application 3D. Un vecteur est essentiellement une liste de trois nombres (x, y et z) qui décrivent un point, une position ou une direction dans l\'espace 3D. Les vecteurs sont essentiels pour définir la géométrie, les transformations et les interactions dans l\'environnement 3D. Ils servent d\'éléments de base pour des opérations telles que les translations, les rotations et les mises à l\'échelle.

Dans FreeCAD, les vecteurs sont largement utilisés pour créer et manipuler des objets. Ils permettent un large éventail d\'opérations mathématiques, telles que l\'addition, la soustraction, les produits en croix, les produits en points et les projections. Ces opérations vous permettent de calculer des distances, des angles et des directions ou de définir des relations entre des objets dans l\'espace.

Il est essentiel de comprendre les vecteurs et leur fonctionnement pour pouvoir créer des scripts et des personnalisations efficaces dans FreeCAD. Par exemple, les vecteurs sont utilisés pour positionner des objets, définir leur orientation, ou même calculer les trajectoires pour des opérations complexes telles que les balayages ou les lissages.

Dans FreeCAD, les vecteurs sont représentés à l\'aide de la classe **Vector**, qui fournit diverses méthodes et propriétés pour effectuer des opérations et accéder à leurs composants. La maîtrise de ces capacités améliorera considérablement votre capacité à interagir avec l\'environnement 3D de FreeCAD par le biais de programmes. Dans FreeCAD, les vecteurs fonctionnent comme suit :


```python
myvec = FreeCAD.Vector(2, 0, 0)
print(myvec)
print(myvec.x)
print(myvec.y)
othervec = FreeCAD.Vector(0, 3, 0)
sumvec = myvec.add(othervec)
```

Voici une brève description des commandes ci-dessus :

-   **myvec = FreeCAD.Vector(2,0,0)** : crée un vecteur myvec avec X = 2, Y = 0, Z = 0.
-   **print(myvec)** : affiche le vecteur myvec avec ses composantes (X, Y, Z).
-   **print(myvec.x)** : affiche la composante X de myvec.
-   **print(myvec.y)** : affiche la composante Y de myvec.
-   **othervec = FreeCAD.Vector(0,3,0)** : crée un second vecteur othervec avec X = 0, Y = 3, Z = 0.
-   **sumvec = myvec.add(othervec)** : additionne myvec et othervec pour créer un nouveau vecteur sumvec contenant la somme de leurs composantes.

Une autre caractéristique commune des objets FreeCAD est leur **Positionnement** (placement). Comme nous l\'avons vu dans les chapitres précédents, chaque objet a une propriété de placement qui contient la position (Base) et l\'orientation (Rotation) de l\'objet. Cs propriétés sont faciles de manipuler avec Python, par exemple pour déplacer notre objet :


```python
print(box.Placement)
print(box.Placement.Base)
box.Placement.Base = sumvec
otherpla = FreeCAD.Placement()
otherpla.Base = FreeCAD.Vector(5, 5, 0)
box.Placement = otherpla
```

Voici une brève description des commandes ci-dessus :

-   **print(box.Placement)** : affiche le placement de la boîte, ce qui inclut sa position, sa rotation et son orientation dans l\'espace 3D.
-   **print(box.Placement.Base)** : affiche la position (Base) de la boîte, qui est un vecteur représentant son emplacement dans l\'espace 3D.
-   **box.Placement.Base = sumvec** : définit la position de base (emplacement) de la boîte au vecteur sumvec, déplaçant ainsi la boîte vers cette nouvelle position.
-   **otherpla = FreeCAD.Placement()** : crée un nouvel objet de placement nommé otherpla.
-   **otherpla.Base = FreeCAD.Vector(5,5,0)** : définit la position de base de otherpla à un vecteur aux coordonnées (5, 5, 0).
-   **box.Placement = otherpla** : applique otherpla à la boîte, en mettant à jour son placement à la nouvelle position et à l\'orientation définies par otherpla.

**Lire plus d\'informations**

-   [Python](https://www.python.org/)
-   [Macros](Macros/fr.md)
-   [Introduction à Python](Introduction_to_Python/fr.md)
-   [Tutoriel de scripts Python](Python_scripting_tutorial/fr.md)
-   [Portail d\'utilisation avancée](Power_users_hub/fr.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:A gentle introduction/fr
