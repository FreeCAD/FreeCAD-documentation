# Python/fr
**FreeCAD a été conçu à l'origine pour fonctionner avec Python 2.x. Cette série s'est terminée avec la version 2.7.18 du 20 avril 2020 et a été remplacée par Python 3. Le développement futur de FreeCAD se fera exclusivement avec Python 3, et la rétrocompatibilité ne sera pas supportée.**

## Description


{{TOCright}}

_.

Dans FreeCAD, le code Python peut être utilisé pour créer divers éléments par programmation, sans qu\'il soit nécessaire de cliquer sur l\'interface graphique. De plus, de nombreux outils et ateliers de FreeCAD sont programmés en Python.

Voir [Introduction à Python](Introduction_to_Python/fr.md) pour en savoir plus sur le langage de programmation Python, puis sur [Tutoriel sur les scripts Python](Python_scripting_tutorial/fr.md) et sur [principes de base des scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md) pour lancer la création de scripts dans FreeCAD.

## Lisibilité

La lisibilité du code Python est l\'un des aspects les plus importants de ce langage. L\'utilisation d\'un style clair et cohérent au sein de la communauté Python facilite les contributions de différents développeurs, car la plupart des programmeurs Python expérimentés s\'attendent à ce que le code soit formaté d\'une certaine manière et suive certaines règles. Lors de l\'écriture de code Python, il est conseillé de suivre [PEP8: Guide de style pour Python Code](https://www.python.org/dev/peps/pep-0008/) et [PEP257: Conventions Docstring](https://www.python.org/dev/peps/pep-0257/).

Ces documents présentent des explications d\'une manière plus conviviale :

-   [Comment écrire un beau code Python avec PEP 8](https://realpython.com/python-pep8/)
-   [Documenter du code Python : un guide complet](https://realpython.com/documenting-python-code/).

## Conventions

Dans cette documentation, certaines conventions relatives aux exemples Python doivent être suivies.

Ceci est une signature de fonction typique


```python
Wire = make_wire(pointslist, closed=False, placement=None, face=None, support=None)
```

-   Les arguments avec des paires clé-valeur sont facultatifs, la valeur par défaut étant indiquée dans la signature. Cela signifie que les appels suivants sont équivalents:


```python
Wire = make_wire(pointslist, False, None, None, None)
Wire = make_wire(pointslist, False, None, None)
Wire = make_wire(pointslist, False, None)
Wire = make_wire(pointslist, False)
Wire = make_wire(pointslist)
```


:   Dans cet exemple, le premier argument n\'a pas de valeur par défaut, il devrait donc toujours être inclus.

-   Lorsque les arguments sont donnés avec la clé explicite, les arguments facultatifs peuvent être donnés dans n\'importe quel ordre. Cela signifie que les appels suivants sont équivalents:


```python
Wire = make_wire(pointslist, closed=False, placement=None, face=None)
Wire = make_wire(pointslist, closed=False, face=None, placement=None)
Wire = make_wire(pointslist, placement=None, closed=False, face=None)
Wire = make_wire(pointslist, support=None, closed=False, placement=None, face=None)
```

-   Les directives de Python insistent sur la lisibilité du code; en particulier, les parenthèses doivent suivre immédiatement le nom de la fonction et un espace doit suivre une virgule.


```python
p1 = Vector(0, 0, 0)
p2 = Vector(1, 1, 0)
p3 = Vector(2, 0, 0)
Wire = make_wire([p1, p2, p3], closed=True)
```

-   Si le code doit être divisé sur plusieurs lignes, utilisez une virgule entre parenthèses ou entre crochets. la deuxième ligne doit être alignée sur la précédente.


```python
a_list = [1, 2, 3,
          2, 4, 5]

Wire = make_wire(pointslist,
                False, None,
                None, None)
```

-   Les fonctions peuvent renvoyer un objet qui peut être utilisé comme base d\'une autre fonction de dessin.


```python
Wire = make_wire(pointslist, closed=True, face=True)
Window = make_window(Wire, name="Big window")
```

## Importations

Les fonctions Python sont stockées dans des fichiers appelés modules. Avant d\'utiliser une fonction de ce module, celui-ci doit être inclus dans le document avec l\'instruction `import`.

Cela crée des fonctions préfixées, c\'est-à-dire `module.function()`. Ce système empêche les conflits de noms avec des fonctions portant le même nom mais provenant de modules différents. Par exemple, les deux fonctions `Arch.make_window()` et `myModule.make_window()` peuvent coexister sans problème.

Des exemples complets doivent inclure les importations nécessaires et les fonctions préfixées.


```python
import FreeCAD as App
import Draft

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1, 1, 0)
p3 = App.Vector(2, 0, 0)
Wire = Draft.make_wire([p1, p2, p3], closed=True)
```


```python
import FreeCAD as App
import Draft
import Arch

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1, 0, 0)
p3 = App.Vector(1, 1, 0)
p4 = App.Vector(0, 2, 0)
pointslist = [p1, p2, p3, p4]

Wire = Draft.make_wire(pointslist, closed=True, face=True)
Structure = Arch.make_structure(Wire, name="Big pillar")
```


{{Powerdocnavi

}}

_ _ _ _

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Python/fr
