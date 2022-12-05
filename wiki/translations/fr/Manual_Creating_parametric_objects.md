# Manual:Creating parametric objects/fr
{{Manual:TOC/fr}}

Dans le [chapitre précédent](Manual_Creating_and_manipulating_geometry.md), nous avons vu comment créer la géométrie Part et comment l\'afficher sur l'écran, en l\'attachant à un objet de document \"dumb\" (non paramétrique). C\'est fastidieux quand nous voulons changer la forme de cet objet. Nous devrions créer une nouvelle forme, puis l'attribuer à nouveau à notre objet.

Cependant, nous avons également vu dans tous les chapitres précédents de ce manuel comment les objets paramétriques sont puissants. Il suffit de changer une propriété, et la forme est recalculée à la volée.

En interne, les objets paramétriques ne font rien de différent de ce que nous venons de faire : ils recalculent le contenu de leur propriété Shape, à plusieurs reprises, chaque fois qu\'une autre propriété a été modifiée.

FreeCAD fournit un système très pratique pour créer de tels objets paramétriques complètement en Python. Ils consistent en une classe Python simple, qui définit toutes les propriétés dont l\'objet a besoin, et ce qui se passera quand une de ces propriétés changera. La structure de l\'objet paramétrique est aussi simple que ceci :


```python
class myParametricObject:

    def __init__(self, obj):
        obj.Proxy = self
        obj.addProperty("App::PropertyFloat", "MyLength")
        ...

    def execute(self,obj):
        print ("Recalculating the shape...")
        print ("The value of MyLength is:")
        print (obj.MyLength)
        ...
```

Toutes les classes Python ont généralement une méthode d\'initialisation (\_\_init\_\_ method). Ce qui est à l\'intérieur de cette méthode est exécuté lorsque cette classe est instanciée (ce qui signifie, en argot de programmation, qu\'un objet Python est créé à partir de cette classe. Comprenez une classe comme un \"modèle\" pour en créer des copies en direct). Ici dans notre fonction d\'initialisation (\_\_init\_\_ function), nous faisons deux choses importantes : 1- stocker notre classe elle-même dans l\'attribut \"Proxy\" de notre document objet FreeCAD, c\'est-à-dire que le document objet de FreeCAD portera ce code en lui-même, et 2- créer toutes les propriétés dont notre objet a besoin. Il existe de nombreux types de propriétés disponibles, vous pouvez obtenir la liste complète en tapant ce code :


```python
FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "dummy").supportedProperties()
```

Ensuite, la deuxième partie importante est la méthode d\'exécution. Tout code dans cette méthode sera exécuté lorsque l\'objet est marqué pour être recalculé, ce qui se produira lorsqu\'une propriété a été modifiée. C\'est tout ce qu\'il y a à faire. Dans l\'exécution, vous devez faire tout ce qui doit être fait, c\'est-à-dire calculer une nouvelle forme, et attribuer à l\'objet lui-même quelque chose comme obj.Shape = myNewShape. C\'est pourquoi la méthode d\'exécution prend un argument \"obj\" qui sera l\'objet du document FreeCAD lui-même, afin que nous puissions le manipuler dans notre code python.

Une dernière chose est importante à retenir : lorsque vous créez de tels objets paramétriques dans un document FreeCAD, lorsque vous enregistrez le fichier, le code python ci-dessus n\'est pas stocké dans le fichier. C\'est pour des raisons de sécurité, si un fichier FreeCAD contenait un code, n'importe qui pourrait distribuer des fichiers FreeCAD contenant des codes malveillants qui pourraient nuire à d\'autres personnes les utilisant sur leurs ordinateurs. Donc, si vous distribuez un fichier contenant des objets fabriqués avec ce qui précède, ce code doit également être présent sur l\'ordinateur qui ouvrira le fichier. La manière la plus simple de faire est généralement de sauvegarder le code ci-dessus dans une macro et de distribuer la macro avec votre fichier FreeCAD ou de partager votre macro sur le dépôt de macros FreeCAD ([FreeCAD macros repository](Macros_recipes.md)) où n\'importe qui peut la télécharger.

Ci-dessous, nous ferons un petit exercice, en construisant un objet paramétrique qui est une simple Face rectangulaire paramétrique. Des exemples plus complexes sont disponibles sur Exemple d\'objet paramétrique ([parametric object example](Scripted_objects.md)) et dans le code source de FreeCAD lui-même ([FreeCAD source code](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py)).

Nous allons donner à notre objet deux propriétés : Longueur et Largeur, que nous utiliserons pour construire un rectangle. Puis, puisque notre objet aura déjà une propriété de placement prédéfinie (tout objet géométrique en a une par défaut, il n\'est pas nécessaire de l\'ajouter nous-mêmes), nous décalerons notre rectangle à l\'emplacement / orientation définis dans le Placement, de sorte que l\'utilisateur pourra déplacer le rectangle n\'importe où en éditant la propriété Placement.


```python
class ParametricRectangle:

    def __init__(self,obj):
        obj.Proxy = self
        obj.addProperty("App::PropertyFloat", "Length")
        obj.addProperty("App::PropertyFloat", "Width")

    def execute(self, obj):
        # We need to import the FreeCAD module here too, because we might be running out of the Console
        # (in a macro, for example) where the FreeCAD module has not been imported automatically:
        import FreeCAD
        import Part

        # First we need to make sure the values of Length and Width are not 0
        # otherwise Part.LineSegment will complain that both points are equal:
        if (obj.Length == 0) or (obj.Width == 0):
            # If yes, exit this method without doing anything:
            return

        # We create 4 points for the 4 corners:
        v1 = FreeCAD.Vector(0, 0, 0)
        v2 = FreeCAD.Vector(obj.Length, 0, 0)
        v3 = FreeCAD.Vector(obj.Length,obj.Width, 0)
        v4 = FreeCAD.Vector(0, obj.Width, 0)

        # We create 4 edges:
        e1 = Part.LineSegment(v1, v2).toShape()
        e2 = Part.LineSegment(v2, v3).toShape()
        e3 = Part.LineSegment(v3, v4).toShape()
        e4 = Part.LineSegment(v4, v1).toShape()

        # We create a wire:
        w = Part.Wire([e1, e2, e3, e4])

        # We create a face:
        f = Part.Face(w)

        # All shapes have a Placement too. We give our shape the value of the placement
        # set by the user. This will move/rotate the face automatically.
        f.Placement = obj.Placement

        # All done, we can attribute our shape to the object!
        obj.Shape = f
```

Au lieu de coller le code ci-dessus dans la console Python, nous devrions plutôt l\'enregistrer quelque part, alors nous pourrons le réutiliser et le modifier ultérieurement. Par exemple dans une nouvelle macro (menu Outils -\> Macros → Créer). Nommez-le, par exemple, \"ParamRectangle\". Cependant, les macros FreeCAD sont enregistrées avec une extension .FCMro, que Python ne reconnaît pas lors de l\'importation. Donc, avant d'utiliser le code ci-dessus, nous devrons renommer le fichier ParamRectangle.FCMacro en ParamRectangle.py. Cela se fait simplement à partir de votre explorateur de fichiers, en naviguant vers le dossier Macros indiqué dans le menu Outils -\> Macros.

Une fois cela fait, nous pouvons maintenant l'utiliser dans la console Python :


```python
import ParamRectangle
```

En explorant le contenu de ParamRectangle, nous pouvons vérifier qu\'il contient notre Classe ParametricRectangle.

Pour créer un nouvel objet paramétrique à l\'aide de notre classe ParametricRectangle, nous utiliserons le code suivant. Observez que nous utilisons Part::FeaturePython au lieu de Part::Feature que nous avons utilisé dans les chapitres précédents (la version Python permet de définir notre propre comportement paramétrique):


```python
myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "Rectangle")
ParamRectangle.ParametricRectangle(myObj)
myObj.ViewObject.Proxy = 0 # This is mandatory unless we code the ViewProvider too.
FreeCAD.ActiveDocument.recompute()
```

Rien ne s\'affiche encore à l\'écran, car les propriétés Longueur et Largeur sont à 0, ce qui déclenchera notre condition de \"ne rien faire\" à l\'intérieur de l\'exécution. Nous devons juste changer les valeurs de Longueur et Largeur, et notre objet apparaîtra magiquement et sera recalculé à la volée.

Bien sûr, il serait fastidieux de devoir taper ces 4 lignes de code Python chaque fois que nous voulons créer un nouveau rectangle paramétrique. Une façon très simple de résoudre ceci est de placer les 4 lignes ci-dessus dans notre fichier ParamRectangle.py, à la fin, après la fin de la classe ParametricRectange (nous pouvons le faire à partir de l\'éditeur Macro).

Maintenant, lorsque nous tapons import ParamRectangle, un nouveau rectangle paramétrique sera automatiquement créé. Encore mieux, nous pouvons ajouter un bouton de barre d\'outils qui fera exactement cela :

-   Ouvrir le menu **Outils -\> Personnaliser**
-   Sous l\'onglet \"Macros\", sélectionnez notre macro ParamRectangle.py, complétez les détails au fur et à mesure que vous le souhaitez, et appuyez sur \"Ajouter\":

![](images/Exercise_python_04.jpg )

Sous l\'onglet Barres d\'outils, créez une nouvelle barre d\'outils personnalisée dans l\'atelier de votre choix (ou globalement), sélectionnez votre macro et ajoutez-la à la barre d\'outils :

![](images/Exercise_python_05.jpg )

-   Nous avons maintenant un nouveau bouton de barre d\'outils qui, lorsqu\'il sera cliqué, créera un rectangle paramétrique.

Rappelez-vous, si vous souhaitez distribuer des fichiers créés avec ce nouvel outil à d\'autres personnes, ils doivent avoir également installé la macro ParamRectangle.py sur leur ordinateur.

**Lire plus d\'informations**

-   [Le dépôt de macros FreeCAD](Macros_recipes.md)
-   [Exemple d\'objet paramétrique](Scripted_objects.md)
-   [Plus d\'exemples dans le code FreeCAD](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:Creating parametric objects/fr
