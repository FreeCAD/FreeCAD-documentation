# Python scripting tutorial/fr
{{TOCright}}

## Introduction

[Python](https://en.wikipedia.org/wiki/Python_%28programming_language%29) est un langage de programmation qui est relativement facile à apprendre et à comprendre. Il est open-source, multi-plateforme et peut être utilisé à de nombreuses fins : des scripts shell simples aux programmes très complexes. Mais son utilisation la plus répandue se trouve dans le langage de script intégré dans d\'autres applications. C\'est ainsi qu\'il est utilisé dans FreeCAD. Depuis la [console Python](Python_console/fr.md), ou depuis des scripts personnalisés, vous pouvez contrôler FreeCAD et lui faire effectuer des opérations très complexes.

Par exemple, à partir d\'un script Python, vous pouvez :

-   Créer de nouveaux objets.
-   Modifier les objets existants.
-   Modifier la représentation 3D de ces objets.
-   Modifier l\'interface de FreeCAD.

Il existe plusieurs façons d\'utiliser Python dans FreeCAD :

-   Depuis [l\'interpréteur Python de FreeCAD](FreeCAD_Scripting_Basics/fr.md), où vous pouvez exécuter du code dans une interface du style \" ligne de commande \".
-   Depuis les [macros](macros/fr.md), qui sont un moyen pratique d\'ajouter rapidement un outil manquant à l\'interface FreeCAD.
-   A partir de scripts externes, qui peuvent être utilisés pour créer des solutions assez complexes, même des [Ateliers](Workbenches/fr.md) entiers.

Dans ce tutoriel, nous allons travailler sur quelques exemples de base pour vous aider à démarrer, mais il y a beaucoup plus de [ documentations sur les scripts Python](Power_users_hub/fr.md) disponibles sur ce wiki. Si vous êtes totalement nouveau sur Python et que vous voulez comprendre comment cela fonctionne, nous avons également une [Introduction à Python](introduction_to_Python/fr.md).

Avant de continuer avec les scripts Python, allez dans la fenêtre **Edit → Préférences → Général → Fenêtre de sortie** et cochez les deux cases :

-    **Rediriger les messages internes Python vers la vue rapport**.

-    **Rediriger les erreurs internes de Python vers la vue rapport**.

Accédez ensuite à **Affichage → Panneau** et vérifiez :

-    **Vue de rapport**coché.

## Ecrire du code Python 

Il existe deux façons d\'écrire du code Python dans FreeCAD. Dans la [Console Python](Python_console/fr.md) (sélectionnez le menu**Affichage → Panneau → Console Python**) ou dans [l\'éditeur de Macro](Std_DlgMacroExecute/fr.md) (sélectionnez **Macro → Macros …** dans le menu). Dans la console vous écrivez les commandes Python une par une, en les exécutant en appuyant sur **Entrée**, tandis que les macros peuvent contenir du code plus complexe composé de plusieurs lignes, exécuté uniquement lorsque la macro est démarrée.

![](images/Screenshot_pythoninterpreter.jpg ) *La console Python FreeCAD*

Dans ce tutoriel vous pouvez utiliser les deux méthodes. Vous pouvez copier-coller chaque ligne dans la console Python puis appuyer sur **Entrée**, ou copier-coller le code entier dans une nouvelle fenêtre Macro.

[En haut](#top.md)

## Exploration de FreeCAD 

Commençons par créer un nouveau document vierge :


```python
doc = FreeCAD.newDocument()
```

Si vous écrivez dans la console Python FreeCAD, vous remarquerez que dès que vous tapez `FreeCAD.` une fenêtre apparaît, permettant de compléter rapidement le reste de votre ligne. Encore mieux, chaque entrée de la liste de saisie semi-automatique a une info-bulle expliquant ce qu\'elle fait. Cela facilite l\'exploration des fonctionnalités disponibles. Avant de choisir `newDocument`, jetez un œil aux autres options.

![](images/Screenshot_classbrowser.jpg ) *Le mécanisme de saisie semi-automatique de la console Python FreeCAD*

Maintenant notre nouveau document sera créé. Cela revient à appuyer sur le bouton **<img src="images/Std_New.svg" width=16px> [Std New](Std_New.md)** dans la barre d\'outils. En fait, la plupart des boutons de FreeCAD ne font rien d\'autre que d\'exécuter une ou plusieurs lignes de code Python. Encore mieux, vous pouvez définir une option dans **Édition → Préférences → Général → Macro** avec **Montrer les commandes du script dans la console Python**. Cela affichera dans la console tout le code Python exécuté lorsque vous pressez les boutons. Très utile pour apprendre à reproduire des actions dans Python.

Maintenant revenons à notre document et voyons ce que nous pouvons faire avec lui :


```python
doc.
```

Explorez les options disponibles. Habituellement, les noms qui commencent par une majuscule sont des attributs, ils contiennent une valeur, tandis que les noms qui commencent par une minuscule sont des fonctions (également appelées méthodes) ; ils \"font quelque chose\". Les noms commençant par un trait de soulignement sont généralement là pour le fonctionnement interne du module et vous ne devriez pas vous en soucier. Utilisons l\'une des méthodes pour ajouter un nouvel objet à notre document :


```python
box = doc.addObject("Part::Box", "myBox")
```

Rien ne se passe. Pourquoi ? Parce que FreeCAD est conçu pour de gros projets. Un jour, il fonctionnera avec des centaines d\'objets complexes, tous dépendants les uns des autres. Faire un petit changement quelque part pourrait avoir un grand impact, vous devrez peut-être recalculer tout le document, ce qui pourrait prendre du temps. Pour cette raison, presque aucune commande ne met automatiquement à jour la scène. Vous devez le faire manuellement :


```python
doc.recompute()
```

Maintenant notre boîte est apparue. De nombreux boutons qui ajoutent des objets dans FreeCAD font en fait deux choses : ajouter l\'objet et recalculer. Si vous avez activé l\'option **Montrer les commandes du script dans la console Python** ci-dessus, essayez d\'ajouter une sphère avec le bouton GUI, vous verrez les deux lignes de code Python s\'exécuter l\'une après l\'autre.

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

Si vous sélectionnez votre boîte avec la souris, vous verrez que dans l\'[Éditeur de propriétés](Property_editor/fr.md), sous l\'onglet **Données**, notre propriété {{PropertyData/fr|Hauteur}} apparaît. Toutes les propriétés d\'un objet FreeCAD qui y apparaissent (et également sur l\'onglet **Vue**, nous développerons plus tard), sont également directement accessibles par Python, par leur nom, comme nous l\'avons fait avec notre propriété {{PropertyData/fr|Hauteur}}. Essayez de changer les autres dimensions de la boîte.

[En haut](#top.md)

## Vecteurs et placements 

[Les vecteurs](https://fr.wikipedia.org/wiki/Vecteur_euclidien) sont un concept tout à fait fondamental dans toute application 3D. Un vecteur est une liste de 3 nombres (x, y et z), décrivant un point ou une position dans l\'espace 3D. Beaucoup de choses peuvent être faites avec des vecteurs, tels que des additions, des soustractions, des projections et [beaucoup plus](https://fr.wikipedia.org/wiki/Espace_vectoriel). Dans FreeCAD, les vecteurs fonctionnent comme ceci :


```python
myvec = FreeCAD.Vector(2, 0, 0)
myvec.x
myvec.y
othervec = FreeCAD.Vector(0, 3, 0)
sumvec = myvec.add(othervec)
```

Une autre caractéristique commune des objets FreeCAD est leur [placement](Placement/fr.md). Chaque objet possède une propriété {{PropertyData/fr|Placement}}, qui contient les {{PropertyData/fr|Base}} (position) et les {{PropertyData/fr|Rotation}} (orientation) de l\'objet. Elle est facile à manipuler, par exemple pour déplacer notre objet :


```python
box.Placement
box.Placement.Base
box.Placement.Base = sumvec
 
otherpla = FreeCAD.Placement()
box.Placement = otherpla
```

Avant d\'aller plus loin, vous devez comprendre quelques concepts importants.

[En haut](#top.md)

## Application et Interface Utilisateur 

FreeCAD a été conçu pour pouvoir également être utilisé sans son interface utilisateur, en tant qu\'application en ligne de commande. Presque chaque objet dans FreeCAD se compose donc de deux parties : un `Object` (objet), sa composante \"géométrie\" et un `ViewObject` (Vue de l\'objet), sa composante \"visuelle\". Lorsque vous travaillez en mode ligne de commande, la partie géométrique est présente, mais la partie visuelle est désactivée.

Pour illustrer le concept, observons notre objet cube. Les propriétés géométriques du cube, telles que ses dimensions, sa position, etc. sont stockées dans `Object`. Alors que ses propriétés visuelles, telles que sa couleur, son épaisseur de ligne, etc. sont stockées dans `ViewObject`. Cela correspond aux onglets **Données** et **Vue** dans l\'[Éditeur de propriétés](Property_editor/fr.md). La partie ViewObject d\'un objet est accessible comme ceci :


```python
vo = box.ViewObject
```

Vous pouvez également modifier les propriétés de l\'onglet **Vue** :


```python
vo.Transparency = 80
vo.hide()
vo.show()
```

Lorsque vous démarrez FreeCAD, la console Python charge déjà deux modules de base : `FreeCAD` et `FreeCADGui` (qui sont également accessibles par leurs raccourcis `App` et `Gui`). Ils contiennent toutes sortes de fonctionnalités génériques pour travailler avec des documents et leurs objets. Pour illustrer notre concept, voyez que `FreeCAD` et `FreeCADGui` contiennent à la fois un attribut `ActiveDocument`, qui est le document actuellement ouvert. `FreeCAD.ActiveDocument` et `FreeCADGui.ActiveDocument` ne sont cependant pas le même objet. Ce sont les deux composants d\'un document FreeCAD et ils contiennent différents attributs et méthodes. Par exemple, `FreeCADGui.ActiveDocument` contient `ActiveView`, qui est la [Vue 3D](3D_view/fr.md) actuellement ouverte.

[En haut](#top.md)

## Les modules 

La véritable puissance de FreeCAD réside dans ses modules indépendants, avec leurs ateliers respectifs. L\'application de base FreeCAD est plus ou moins un conteneur vide. Sans ses modules, elle ne peut guère faire plus que créer de nouveaux documents vides. Chaque module ajoute non seulement de nouveaux ateliers à l\'interface, mais également de nouvelles commandes Python et de nouveaux types d\'objets. Par conséquent, plusieurs types d\'objets différents, voire totalement incompatibles, peuvent coexister dans le même document. Les modules les plus importants de FreeCAD que nous verrons dans ce tutoriel sont : [Part (Pièce)](Part_Workbench/fr.md), [Mesh (Maillage)](Mesh_Workbench/fr.md), [Sketcher (Esquisseur)](Sketcher_Workbench/fr.md) et [Draft (Planche à dessin)](Draft_Workbench/fr.md).

[Sketcher (Atelier Esquisse)](Sketcher_Workbench/fr.md) et [Draft (Atelier Planche à dessin)](Draft_Workbench/fr.md) utilisent tous deux l\'[Atelier Part](Part_Workbench/fr.md) pour créer et gérer leur géométrie. Tandis que [Mesh (Atelier Maillage)](Mesh_Workbench/fr.md) est totalement indépendant et gère ses propres objets. Plus d\'informations à ce sujet ci-dessous.

Vous pouvez vérifier tous les types d\'objets de base disponibles pour le document actuel comme ceci :


```python
doc.supportedTypes()
```

Les différents modules FreeCAD ne sont pas automatiquement chargés dans la console Python. C\'est pour éviter d\'avoir un démarrage très lent. Les modules sont chargés uniquement lorsque vous en avez besoin. Ainsi, par exemple, pour explorer ce qui se trouve à l\'intérieur du module Part :


```python
import Part
Part.
```

Mais nous parlerons plus en détail du module Part ci-dessous.

[En haut](#top.md)

## Mesh (Maillage) 

[Un Maillage](https://fr.wikipedia.org/wiki/Mesh_(objet)) est un type d\'objet 3D très simple, utilisé par exemple par [Sketchup](https://fr.wikipedia.org/wiki/SketchUp), [Blender](https://fr.wikipedia.org/wiki/Blender) et [3D Studio Max](https://fr.wikipedia.org/wiki/Autodesk_3ds_Max). Ils sont composés de 3 éléments : des points (également appelés sommets), des lignes (également appelées arêtes) et des faces. Dans de nombreuses applications, FreeCAD inclus, les faces peuvent n\'avoir que 3 sommets. Bien sûr, rien ne vous empêche d\'avoir une face plus grande composée de plusieurs triangles coplanaires.

Les maillages sont simples, mais comme ils sont simples, vous pouvez facilement en avoir des millions dans un seul document. Cependant, dans FreeCAD, ils sont moins utilisés et sont principalement là pour que vous puissiez importer des objets dans des formats de maillage ({{FileName|.stl}}, {{FileName|.obj}}) à partir d\'autres applications. Le module Mesh a également été largement utilisé comme module de test principal au cours du premier mois de la vie de FreeCAD.

Les objets Mesh et les objets FreeCAD sont des choses différentes. Vous pouvez voir l\'objet FreeCAD comme un conteneur pour un objet Mesh (et comme nous le verrons ci-dessous, pour les objets Part également). Donc pour ajouter un objet Mesh à FreeCAD, nous devons d\'abord créer un objet FreeCAD et un objet Mesh, puis ajouter l\'objet Mesh à l\'objet FreeCAD :


```python
import Mesh
mymesh = Mesh.createSphere()
mymesh.Facets
mymesh.Points
 
meshobj = doc.addObject("Mesh::Feature", "MyMesh")
meshobj.Mesh = mymesh
doc.recompute()
```

Il s\'agit d\'un exemple standard qui utilise la méthode `createSphere()` pour créer une sphère, mais vous pouvez également créer des maillages personnalisés à partir de zéro en définissant leurs sommets et faces.

[Plus de renseignements sur les scripts Mesh\...](Mesh_Scripting/fr.md)

[En haut](#top.md)

## Part (Atelier Pièce) 

L\'[atelier Part](Part_Workbench/fr.md) est le module le plus puissant de FreeCAD. Il vous permet de créer et de manipuler des objets [BREP](https://fr.wikipedia.org/wiki/B-Rep). BREP signifie Boundary Representation ou « Représentation par les Bords ». Un objet BREP est défini par des surfaces qui entourent et définissent un volume intérieur. Contrairement aux maillages, les objets BREP peuvent avoir une grande variété de composants, des faces planes aux surfaces NURBS très complexes.

Le module Part est basé sur la puissante bibliothèque [OpenCasCade](https://fr.wikipedia.org/wiki/Open_CASCADE_Technology), qui permet d\'effectuer un large éventail d\'opérations complexes sur ces objets, telles que les opérations booléennes, le filetage, les balayages, etc.

Le module Part fonctionne de la même manière que le module Mesh : vous créez un objet FreeCAD, un objet Part, puis ajoutez l\'objet Part à l\'objet FreeCAD :


```python
import Part
myshape = Part.makeSphere(10)
myshape.Volume
myshape.Area

shapeobj = doc.addObject("Part::Feature", "MyShape")
shapeobj.Shape = myshape
doc.recompute()
```

Le module Part (comme le module Mesh) a également un raccourci qui crée automatiquement un objet FreeCAD et lui ajoute une forme, vous pouvez donc raccourcir les trois dernières lignes avec :


```python
Part.show(myshape)
```

En explorant le contenu de myshape, vous remarquerez de nombreux sous-composants intéressants tels que `Faces`, `Edges`, `Vertexes`, `Solids` et `Shells` et un large éventail d\'opérations de géométrie telles que `cut` (soustraction), `common` (intersection) ou `fuse` (union). La page [Script pour création topologique](Topological_data_scripting/fr.md) explique tout cela en détail.

[Ici plus de renseignements sur les scripts Part](Topological_data_scripting/fr.md)

[En haut](#top.md)

## Draft (Planche à dessin) 

FreeCAD propose de nombreux autres modules tels que l\'[atelier Sketch](Sketcher_Workbench/fr.md) et l\'[atelier Draft](Draft_Workbench/fr.md) qui créent également des objets Part (Pièce). Ces modules ajoutent des paramètres supplémentaires aux objets créés, voire implémentent une toute nouvelle façon de gérer la géométrie de la pièce (Part) qu\'ils contiennent. Notre exemple de boîte ci-dessus est un exemple parfait d\'un objet paramétrique. Tout ce dont vous avez besoin pour définir la boîte est de spécifier les paramètres hauteur, largeur et longueur. Sur la base de ceux-ci, l\'objet calculera automatiquement sa forme \" de pièce \". FreeCAD vous permet de [créer de tels objets en Python](Scripted_objects/fr.md).

L\'[atelier Draft](Draft_Workbench/fr.md) ajoute des objets de type paramétrique 2D (qui sont tous des objets Part) tels que des lignes et des cercles et fournit également des fonctions génériques qui fonctionnent non seulement sur les objets Draft, mais sur tout objet Part. Pour explorer ce qui est disponible, faites simplement :


```python
import Draft
rec = Draft.makeRectangle(5, 2)
mvec = FreeCAD.Vector(4, 4, 0)
Draft.move(rec, mvec)
Draft.move(box, mvec)
```

[En haut](#top.md)

## Interface

L\'interface utilisateur de FreeCAD est faite avec [Qt](https://fr.wikipedia.org/wiki/Qt), un puissant système d\'interface graphique, chargé de dessiner et de gérer tous les contrôles, menus, barres d\'outils et boutons autour de la [Vue 3D](3D_view/fr.md). Qt fournit un module, [PySide](PySide/fr.md), qui permet à Python d\'accéder et de modifier des interfaces Qt telles que celle de FreeCAD. Essayons de jouer avec l\'interface Qt et de produire une boîte de dialogue simple :


```python
from PySide import QtGui
QtGui.QMessageBox.information(None, "Apollo program", "Houston, we have a problem")
```

Notez que la boîte de dialogue qui apparaît possède l\'icône FreeCAD dans sa barre d\'outils, ce qui signifie que Qt sait que la commande a été émise depuis l\'intérieur de l\'application FreeCAD. Il est possible de manipuler n\'importe quelle partie de l\'interface FreeCAD.

Qt est un système (de construction) d\'interface très puissant qui vous permet de faire des choses très complexes. Il possède également des outils faciles à utiliser, tel que Qt Designer, avec lequel vous pouvez concevoir graphiquement des boîtes de dialogue, puis les ajouter à l\'interface FreeCAD avec quelques lignes de code Python.

[Plus de renseignements sur PySide ici](PySide/fr.md)

[En haut](#top.md)

## Macros

Maintenant que vous avez une bonne compréhension des bases, où allons-nous conserver nos scripts Python et comment allons-nous les lancer dans FreeCAD ? Il existe un mécanisme simple pour cela, appelé [Macros](Macros/fr.md). Une macro est un script Python qui peut être ajouté à une barre d\'outils et lancé via un clic de souris. FreeCAD vous fournit un éditeur de texte simple (**Macro → Macros... → Créer**) où vous pouvez écrire ou coller des scripts. Une fois le script terminé, utilisez **Outils → Personnaliser... → Macros** pour définir un bouton qui pourra être ajouté aux barres d\'outils.

Vous êtes maintenant prêt pour des scripts FreeCAD plus approfondis. Alors rendez-vous sur le [Hub pour utilisateurs expérimentés](Power_users_hub/fr.md) !

[En haut](#top.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > Python scripting tutorial/fr
