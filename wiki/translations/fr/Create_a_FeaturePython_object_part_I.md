# Create a FeaturePython object part I/fr
{{TOCright}}

## Introduction

Les objets FeaturePython (également appelés [Objets créés par script](Scripted_objects/fr.md)) offrent aux utilisateurs la possibilité d\'étendre FreeCAD avec des objets qui s\'intègrent de manière transparente dans le framework FreeCAD.

Cela favorise:

-   Le prototypage rapide de nouveaux objets et outils avec des classes personnalisées de Python.
-   Sauvegarde et restauration des données (également appelées sérialisation) via des objets `App::Property` sans intégrer de script dans le fichier de document FreeCAD.
-   Une liberté créative pour adapter FreeCAD à n\'importe quelle tâche.

Sur cette page, nous allons construire un exemple de travail d\'une classe personnalisée FeaturePython, en identifiant tous les composants principaux et en comprenant comment tout fonctionne au fur et à mesure.

### Comment ça marche? 

FreeCAD est livré avec un certain nombre de types d\'objets par défaut pour gérer différents types de géométrie. Certains d\'entre eux ont des alternatives \"FeaturePython\" qui permettent une personnalisation avec une classe Python définie par l\'utilisateur.

Cette classe Python personnalisée prend une référence à l\'un de ces objets et le modifie. Par exemple, la classe Python peut ajouter des propriétés à l\'objet ou le lier à d\'autres objets. De plus, la classe Python peut implémenter certaines méthodes pour permettre à l\'objet de répondre aux événements du document, ce qui permet de piéger les modifications de propriété de l\'objet et de recalculer le document.

Lorsque vous travaillez avec des classes personnalisées et des objets FeaturePython, il est important de savoir que la classe personnalisée et son état ne sont pas enregistrés dans le document car cela nécessiterait l\'incorporation d\'un script dans un fichier de document FreeCAD, ce qui poserait un risque de sécurité important. Seul l\'objet FeaturePython lui-même est enregistré (sérialisé). Mais comme le chemin du module de script est stocké dans le document, un utilisateur n\'a qu\'à installer le code de classe Python personnalisé en tant que module importable, suivant la même structure de dossier, pour retrouver la fonctionnalité perdue.

[En haut](#top.md)

## Mise en place 

Les classes d\'objets FeaturePython doivent agir comme des modules importables dans FreeCAD. Cela signifie que vous devez les placer dans un chemin qui existe dans votre environnement Python (ou l\'ajouter spécifiquement). Pour les besoins de ce tutoriel, nous allons utiliser le dossier Macro utilisateur FreeCAD, mais si vous avez une autre idée en tête, n\'hésitez pas à l\'utiliser à la place!

Si vous ne savez pas où se trouve le dossier Macro de FreeCAD, tapez `FreeCAD.getUserMacroDir(True)` dans la [console Python](Python_console/fr.md) de FreeCAD :

-   Sous Linux, il s\'agit généralement de {{FileName|/home/<username>/.FreeCAD/Macro/}}.
-   Sous Windows, c\'est {{FileName|%APPDATA%\FreeCAD\Macro\}}, ce qui est généralement {{FileName|C:\Users\<username>\Appdata\Roaming\FreeCAD\Macro\}}.
-   Sous Mac OSX, il s\'agit généralement de {{FileName|/Users/<username>/Library/Preferences/FreeCAD/Macro/}}.

Maintenant, nous devons créer des fichiers.

-   Dans le dossier {{FileName|Macro}}, créez un nouveau dossier appelé {{FileName|fpo}}.
-   Dans le dossier {{FileName|fpo}}, créez un fichier vide : {{FileName|__init__.py}}.
-   Dans le dossier {{FileName|fpo}}, créez un nouveau dossier appelé {{FileName|box}}.
-   Dans le dossier {{FileName|box}}, créez deux fichiers : {{FileName|__init__.py}} et {{FileName|box.py}} (laissez les deux cases vides pour l\'instant).

La structure de votre dossier devrait ressembler à ceci:

Macro/
    |--> fpo/
        |--> __init__.py
        |--> box/
            |--> __init__.py
            |--> box.py

Le dossier {{FileName|fpo}} est l\'endroit pour jouer avec les nouveaux objets FeaturePython et le dossier {{FileName|box}} est le module dans lequel nous allons travailler. {{FileName|__init__.py}} indique à Python qu\'il y a un module importable dans le dossier et {{FileName|box.py}} sera le fichier de classe pour notre nouvel objet FeaturePython.

Une fois nos chemins et fichiers de module créés, nous assurons que FreeCAD est correctement configuré:

-   Démarrez FreeCAD (si vous ne l\'avez pas déjà fait).
-   Activez la [Vue rapport](Report_view/fr.md) (**Affichage → Panneaux → Vue rapport**).
-   Activez la [console Python](Python_console/fr.md) (**Affichage → Panneaux → Console Python**) voir [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics/fr.md).

Enfin, naviguez jusqu\'au dossier {{FileName|Macro/fpo/box}} et ouvrez {{FileName|box.py}} dans votre éditeur de code préféré. Nous ne modifierons que ce fichier.

[En haut](#top.md)

## Un objet FeaturePython 

Commençons par écrire notre classe et son constructeur:


```python
class box():

    def __init__(self, obj):
        """
        Default constructor
        """

        self.Type = 'box'

        obj.Proxy = self
```

**La méthode `__init__()` se décompose comme suit:**

+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
|                                | Les paramètres font référence à la classe Python elle-même et à l\'objet FeaturePython auquel elle est attachée. |
| `def __init__(self, obj):`           |                                                                                                                  |
|                                            |                                                                                                                  |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
|                                | Définition de chaîne du type Python personnalisé.                                                                |
| `self.Type <nowiki>=</nowiki> 'box'` |                                                                                                                  |
|                                            |                                                                                                                  |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+
|                                | Stocke une référence à l\'instance Python dans l\'objet FeaturePython.                                           |
| `obj.Proxy <nowiki>=</nowiki> self`  |                                                                                                                  |
|                                            |                                                                                                                  |
+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------+

Ajoutez le code suivant en haut du fichier :


```python
import FreeCAD as App

def create(obj_name):
    """
    Object creation method
    """

    obj = App.ActiveDocument.addObject('App::FeaturePython', obj_name)

    box(obj)

    return obj
```

**La méthode `create()` se décompose comme suit:**

+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | Importation standard pour la plupart des scripts Python, l\'alias d\'application n\'est pas requis.                                                                                                                                                |
| `import FreeCAD as App`                     |                                                                                                                                                                                                                                                    |
|                                                   |                                                                                                                                                                                                                                                    |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | Crée un nouvel objet FreeCAD FeaturePython avec le nom transmis à la méthode. S\'il n\'y a pas de conflit de nom, ce sera le libellé et le nom de l\'objet créé. Sinon, un nom et une étiquette uniques seront créés en fonction de \'obj\_name\'. |
| `obj <nowiki>=</nowiki> ... addObject(...)` |                                                                                                                                                                                                                                                    |
|                                                   |                                                                                                                                                                                                                                                    |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | Crée notre instance de classe personnalisée.                                                                                                                                                                                                       |
| `box(obj)`                                  |                                                                                                                                                                                                                                                    |
|                                                   |                                                                                                                                                                                                                                                    |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                       | Renvoie l\'objet FeaturePython.                                                                                                                                                                                                                    |
| `return obj`                                |                                                                                                                                                                                                                                                    |
|                                                   |                                                                                                                                                                                                                                                    |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

La méthode `create()` n\'est pas requise mais elle fournit un bon moyen d\'encapsuler le code de création d\'objet.

[En haut](#top.md)

### Test du code 

Nous pouvons maintenant tester notre nouvel objet. Enregistrez votre code et revenez à FreeCAD. Assurez-vous que vous avez ouvert un nouveau document, vous pouvez le faire en appuyant sur **Ctrl**+**N** ou en sélectionnant **Fichier → Nouveau**.

Dans la console Python, tapez ce qui suit:


```python
from fpo.box import box
```

Maintenant, nous devons créer notre objet:


```python
mybox = box.create('my_box')
```

![](images/Fpo_treeview.png ) Vous devriez voir apparaître un nouvel objet dans la [Vue en arborescence](Tree_view/fr.md) étiqueté \"my\_box\".

Notez que l\'icône est grise. FreeCAD nous dit que l\'objet ne peut rien afficher dans la [Vue 3D](3D_view/fr.md). Cliquez sur l\'objet et regardez ses propriétés dans l\'[Éditeur de propriétés](Property_editor/fr.md). Il n\'y a pas grand-chose là-bas, juste le nom de l\'objet.

Notez également qu\'il y a une petite coche bleue à côté de l\'objet FeaturePython dans l\'arborescence. En effet, lorsqu\'un objet est créé ou modifié, il est \"touché\" et doit être recalculé. Appuyez sur le bouton **<img src="images/Std_Refresh.svg" width=16px> [Std Rafraîchir](Std_Refresh/fr.md)** pour y parvenir. Nous ajouterons du code pour automatiser cela plus tard. 


Jetons un oeil aux attributs de notre objet: 
```python
dir(mybox)
```

Cela retournera:


```python
['Content', 'Document', 'ExpressionEngine', 'FullName', 'ID', 'InList',
...
'setPropertyStatus', 'supportedProperties', 'touch']
```

Il y a beaucoup d\'attributs car nous accédons à l\'objet FeaturePyton natif de FreeCAD créé à la première ligne de notre méthode `create()`. La propriété `Proxy` que nous avons ajoutée dans notre méthode `__init__()` est là aussi.

Inspectons-la avec la méthode `dir()`:


```python
dir(mybox.Proxy)
```

Cela retournera:


```python
['Type', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
...
'__str__', '__subclasshook__', '__weakref__']
```

Nous pouvons voir notre propriété `Type`. Vérifions:


```python
mybox.Proxy.Type
```

Cela retournera:


```python
'box'
```

Il s\'agit bien de la valeur assignée, nous savons donc que nous accédons à la classe personnalisée via l\'objet FeaturePython.

Voyons maintenant si nous pouvons rendre notre classe un peu plus intéressante, et peut-être aussi plus utile.

[En haut](#top.md)

### Ajout de propriétés 

Les propriétés sont l\'élément vital d\'une classe FeaturePython. Heureusement, FreeCAD supporte [un certain nombre de types de propriétés](FeaturePython_Custom_Properties/fr.md) pour les classes FeaturePython. Ces propriétés sont attachées directement à l\'objet FeaturePython et sont entièrement sérialisées lors de l\'enregistrement du fichier. Pour éviter d\'avoir à sérialiser les données vous-même, il est conseillé de n\'utiliser que ces types de propriétés.

L\'ajout de propriétés se fait à l\'aide de la méthode `add_property()`. La syntaxe de cette méthode est la suivante :

add_property(type, name, section, description)

Vous pouvez consulter la liste des propriétés prises en charge en tapant :


```python
mybox.supportedProperties()
```

Essayons d\'ajouter une propriété à notre classe de boîte. Passez à votre éditeur de code, passez à la méthode `__init__()`, et à la fin de la méthode, ajoutez:


```python
obj.addProperty('App::PropertyString', 'Description', 'Base', 'Box description').Description = ""
```

Notez que nous utilisons la référence à l\'objet FeaturePython (sérialisable) `obj`, et non l\'instance de classe Python (non sérialisable) `self`.

Une fois que vous avez terminé, enregistrez les modifications et revenez à FreeCAD. Avant de pouvoir observer les modifications apportées à notre code, nous devons recharger le module. Cela peut être accompli en redémarrant FreeCAD, mais redémarrer FreeCAD à chaque fois que nous éditons le code serait gênant. Pour faciliter les choses, tapez ce qui suit dans la console Python:


```python
from importlib import reload
reload(box)
```

Avec le module rechargé, voyons ce que nous obtenons lorsque nous créons un objet :


```python
box.create('box_property_test')
```

Vous devriez voir le nouvel objet boîte apparaître dans l\'arborescence:

-   Sélectionnez-le et regardez l\'éditeur de propriétés. Là, vous devriez voir la propriété *Description*.
-   Passez la souris sur le nom de la propriété à gauche et l\'info-bulle devrait apparaître avec la description que vous avez fournie.
-   Sélectionnez le champ et tapez ce que vous voulez. Vous remarquerez que les commandes de mise à jour Python sont exécutées et affichées dans la console lorsque vous tapez des lettres et que les propriétés changent.

[En haut](#top.md)

Ajoutons quelques propriétés supplémentaires. Retournez à votre code source et ajoutez les propriétés suivantes à la méthode `__init__()`:


```python
obj.addProperty('App::PropertyLength', 'Length', 'Dimensions', 'Box length').Length = 10.0
obj.addProperty('App::PropertyLength', 'Width', 'Dimensions', 'Box width').Width = '10 mm'
obj.addProperty('App::PropertyLength', 'Height', 'Dimensions', 'Box height').Height = '1 cm'
```

Et ajoutons aussi un code pour recalculer le document automatiquement. Ajoutez la ligne suivante au-dessus de l\'instruction `return()` de la méthode `create()`:


```python
App.ActiveDocument.recompute()
```

**Faites attention à l\'endroit où vous recalculez un objet FeaturePython. Le recalcul doit être effectué par une méthode externe à sa classe.**

![ right](images/fpo_box_properties.png )

Maintenant, testez vos modifications comme suit:

-   Enregistrez vos modifications et rechargez votre module.
-   Supprimez tous les objets dans l\'arborescence.
-   Créez un nouvel objet boîte à partir de la console Python en appelant `box.create('myBox')`.

Une fois que la boîte est créée et que vous avez vérifié pour vous assurer qu\'elle a été recalculée, sélectionnez l\'objet et regardez ses propriétés. Vous devez noter deux choses:

-   Un nouveau groupe de propriétés: *Dimensions*.
-   Trois nouvelles propriétés: *Height*, *Length* et *Width*.

Notez également que les propriétés ont des unités. Plus précisément, elles ont repris les unités linéaires définies dans les préférences de l\'utilisateur (**Edition → Préférences... → Général → Unités**). 


Vous avez sans doute remarqué que trois valeurs différentes ont été saisies pour les dimensions : une valeur en virgule flottante (`10.0`) et deux chaînes de caractères différentes (`'10 mm'` et `'1 cm'`). Le type `App::PropertyLength` suppose que les valeurs en virgule flottante sont en millimètres, les valeurs des chaînes sont analysées en fonction des unités spécifiées et, dans l\'interface graphique, toutes les valeurs sont converties dans les unités spécifiées dans les préférences de l\'utilisateur (`mm` dans l\'image). Ce comportement intégré rend le type `App::PropertyLength` idéal pour les dimensions.

[En haut](#top.md)

### Piège à événements 

Le dernier élément requis pour un objet FeaturePython de base est le recouvrement d\'événements. Un objet FeaturePython peut réagir aux événements avec des fonctions de rappel. Dans notre cas, nous voulons que l\'objet réagisse chaque fois qu\'il est recalculé. En d\'autres termes, nous voulons intercepter les recalculs. Pour ce faire, nous devons ajouter une fonction avec un nom spécifique, `execute()`, à la classe d\'objets. Il existe plusieurs autres événements qui peuvent être piégés, à la fois dans l\'objet FeaturePython lui-même et dans le [ViewProvider](Viewprovider/fr.md), que nous aborderons dans la [Création d\'une boîte FeaturePython, partie II](Create_a_FeaturePython_object_part_II/fr.md).

Pour une référence complète des méthodes disponibles à implémenter sur les classes FeautrePython, voir [Méthodes FeaturePython](FeaturePython_methods/fr.md).

Ajoutez ce qui suit après la fonction `__init__()`:


```python
def execute(self, obj):
    """
    Called on document recompute
    """

    print('Recomputing {0:s} ({1:s})'.format(obj.Name, self.Type))
```

Testez le code en suivant à nouveau ces étapes:

-   Enregistrez et rechargez le module.
-   Supprimer tous les objets.
-   Créez un nouvel objet boîte.

Vous devriez voir la sortie imprimée dans la console Python, grâce à l\'appel `recompute()` que nous avons ajouté à la méthode `create()`. Bien sûr, la méthode `execute()` ne fait rien ici, sauf nous dire qu\'elle a été appelée, mais elle est la clé de la magie des objets FeaturePython.

Voilà, vous savez maintenant comment construire un objet FeaturePython basique et fonctionnel !

[En haut](#top.md)

### Le code terminé 


```python
import FreeCAD as App

def create(obj_name):
    """
    Object creation method
    """

    obj = App.ActiveDocument.addObject('App::FeaturePython', obj_name)

    box(obj)

    App.ActiveDocument.recompute()

    return obj

class box():

    def __init__(self, obj):
        """
        Default constructor
        """

        self.Type = 'box'

        obj.Proxy = self

        obj.addProperty('App::PropertyString', 'Description', 'Base', 'Box description').Description = ""
        obj.addProperty('App::PropertyLength', 'Length', 'Dimensions', 'Box length').Length = 10.0
        obj.addProperty('App::PropertyLength', 'Width', 'Dimensions', 'Box width').Width = '10 mm'
        obj.addProperty('App::PropertyLength', 'Height', 'Dimensions', 'Box height').Height = '1 cm'

    def execute(self, obj):
        """
        Called on document recompute
        """

        print('Recomputing {0:s} ({1:s})'.format(obj.Name, self.Type))
```

[En haut](#top.md)





{{Powerdocnavi

}} 

_ _

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Create a FeaturePython object part I/fr
