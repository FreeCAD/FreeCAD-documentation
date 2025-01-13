# Manual:Creating parametric objects/fr
{{Manual:TOC}}

Dans le [chapitre précédent](Manual_Creating_and_manipulating_geometry.md), nous avons exploré la manière de créer une géométrie de **Part** et de l\'afficher à l\'écran en l\'attachant à un objet document **muet** (non paramétrique). Bien qu\'efficace, cette approche devient fastidieuse lorsqu\'il s\'agit de modifier la forme. Chaque modification nécessite la création d\'une nouvelle forme et sa réaffectation à l\'objet, ce qui entraîne des flux de travail répétitifs et inefficaces.

Tout au long de ce manuel, nous avons vu comment les objets paramétriques répondent à ce problème en permettant des mises à jour dynamiques. En modifiant une seule propriété, la forme est recalculée automatiquement, ce qui élimine le besoin de mises à jour manuelles. Ce processus de recalcul permet une modélisation plus efficace et introduit une certaine adaptabilité dans les conceptions. En interne, les objets paramétriques fonctionnent de manière similaire à ce que nous avons déjà fait : ils recalculent le contenu de leur propriété **Forme** chaque fois qu\'une de leurs propriétés change. Ce processus itératif est transparent et garantit que l\'objet reste cohérent avec ses paramètres définis.

FreeCAD propose un système convivial de création d\'objets paramétriques entièrement en Python. Ces objets sont définis à l\'aide d\'une classe Python, qui :

-   Déclare les propriétés nécessaires pour l\'objet.
-   Définit le comportement en cas de modification de l\'une de ces propriétés.

La structure d\'un tel objet paramétrique est aussi simple que cela :


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

Toutes les classes Python ont généralement une méthode **\_\_init\_\_**. Cette méthode est exécutée lorsqu\'une classe est instanciée, c\'est-à-dire lorsqu\'un objet Python est créé à partir de la classe. Vous pouvez considérer une classe comme un «modèle» ou un plan utilisé pour créer des instances vivantes d\'elle-même. Chaque instance de la classe devient un objet indépendant doté de ses propres attributs et méthodes. Dans notre méthode **\_\_init\_\_**, nous effectuons deux tâches cruciales :

-   Enregistrer la classe elle-même dans l\'attribut **Proxy** de l\'objet document FreeCAD :

En assignant **self** à l\'attribut **Proxy** de l\'objet document FreeCAD, nous lions la logique de notre classe Python à l\'objet FreeCAD. Cela signifie que l\'objet document « portera » le code de la classe Python à l\'intérieur de lui-même, lui permettant de se comporter selon la logique définie dans la classe. Cette connexion permet à FreeCAD de savoir comment interagir avec l\'objet paramétrique et le recalculer.

-   Créer toutes les propriétés dont l\'objet a besoin :

En utilisant la méthode **addProperty**, nous définissons les propriétés personnalisées requises par l\'objet. Les propriétés agissent comme des paramètres ou des variables pour l\'objet et peuvent être consultées, modifiées et affichées dans l\'éditeur de propriétés de FreeCAD. Dans l\'exemple, nous ajoutons une propriété à virgule flottante nommée **MyLength**. Cette propriété influencera ultérieurement la forme ou le comportement de l\'objet.

class myParametricObject:

  def __init__(self,obj):
    obj.Proxy = self
    obj.addProperty("App::PropertyFloat","MyLength")
    ...
       
  def execute(self,obj):
    print ("Recalculating the shape...")
    print ("The value of MyLength is:")
    print (obj.MyLength)
    ...


```python
FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "dummy").supportedProperties()
```

La deuxième partie clé de notre classe est la méthode **execute**. Cette méthode est automatiquement déclenchée chaque fois que l\'objet est marqué pour un nouveau calcul, ce qui se produit lorsque l\'une de ses propriétés est modifiée. C\'est dans la méthode **execute** que s\'effectuent tous les recalculs de l\'objet, garantissant que sa forme et son comportement sont mis à jour pour refléter tout changement. Dans la méthode **execute**, vous effectuez toutes les opérations nécessaires pour générer la nouvelle géométrie de votre objet. En règle générale, il s\'agit de recalculer la forme en fonction des valeurs en cours de ses propriétés, puis d\'affecter la forme mise à jour à l\'attribut **Shape** de l\'objet à l\'aide d\'une instruction telle que **obj.Shape = myNewShape**. La méthode **execute** prend un seul argument, **obj**, qui représente l\'objet document FreeCAD associé à votre objet paramétrique. Cela vous permet de manipuler directement l\'objet dans la méthode, par exemple en accédant à ses propriétés, en mettant à jour sa géométrie ou en effectuant d\'autres opérations.

FreeCAD.ActiveDocument.addObject(\"Part::FeaturePython\",\"dummy\").supportedProperties()

-   La méthode **execute** est appelée chaque fois que l\'objet doit être mis à jour.
-   Elle est responsable de recalculer la forme et de l\'assigner à l\'attribut **Shape** de l\'objet.
-   L\'argument **obj** donne accès à l\'objet document de FreeCAD, ce qui permet d\'effectuer des modifications par programme.

Avec ce système, FreeCAD s\'occupe du reste en s\'assurant que l\'objet est correctement mis à jour dans le document et affiché correctement dans l\'interface graphique.

Une chose essentielle à retenir est que lorsque vous créez des objets paramétriques dans un document FreeCAD, le code Python utilisé pour les définir n\'est pas sauvegardé dans le fichier. Il s\'agit d\'une mesure de sécurité intentionnelle. Si les fichiers FreeCAD étaient autorisés à stocker du code Python, des acteurs malveillants pourraient distribuer des fichiers contenant des scripts nuisibles susceptibles d\'endommager l\'ordinateur de quelqu\'un. Par conséquent, lorsque vous partagez un fichier FreeCAD contenant des objets paramétriques créés avec du code Python personnalisé, le destinataire doit également avoir accès au code utilisé pour définir ces objets. Sans ce code, FreeCAD ne saura pas comment recalculer ou interagir correctement avec les objets.

La façon la plus simple d\'y parvenir est d\'enregistrer le code Python dans un fichier macro. Lorsque vous distribuez votre fichier FreeCAD, vous pouvez inclure la macro avec celui-ci. Vous pouvez également partager la macro sur le [dépôt des macros de FreeCAD](Macros_recipes/fr.md), ce qui permet aux autres de la télécharger et de l\'utiliser facilement. Cette approche garantit que vos objets paramétriques personnalisés restent fonctionnels sur d\'autres systèmes tout en respectant les meilleures pratiques en matière de sécurité.

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

Au lieu de coller le code ci-dessus dans la console Python, nous devrions plutôt l\'enregistrer quelque part, alors nous pourrons le réutiliser et le modifier ultérieurement. Par exemple dans une nouvelle macro (menu **Macro -\> Macros → Créer**). Nommez-le, par exemple, \"ParamRectangle\". Cependant, les macros FreeCAD sont enregistrées avec une extension .FCMro, que Python ne reconnaît pas lors de l\'importation. Donc, avant d'utiliser le code ci-dessus, nous devrons renommer le fichier ParamRectangle.FCMacro en ParamRectangle.py. Cela se fait simplement à partir de votre explorateur de fichiers, en naviguant vers le dossier Macros indiqué dans le menu Outils -\> Macros.

Une fois cela fait, nous pouvons maintenant l'utiliser dans la console Python :


```python
import ParamRectangle
```

En explorant le contenu de ParamRectangle, nous pouvons vérifier qu\'il contient notre Classe ParametricRectangle.

Pour créer un nouvel objet paramétrique à l\'aide de notre classe ParametricRectangle, nous utiliserons le code suivant. Observez que nous utilisons **Part::FeaturePython** au lieu de **Part::Feature** que nous avons utilisé dans les chapitres précédents (la version Python permet de définir notre propre comportement paramétrique):


```python
myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "Rectangle")
ParamRectangle.ParametricRectangle(myObj)
myObj.ViewObject.Proxy = 0 # This is mandatory unless we code the ViewProvider too.
FreeCAD.ActiveDocument.recompute()
```

myObj = FreeCAD.ActiveDocument.addObject(\"Part::FeaturePython\",\"Rectangle\")

ParamRectangle.ParametricRectangle(myObj)
myObj.ViewObject.Proxy = 0 # this is mandatory unless we code the ViewProvider too
FreeCAD.ActiveDocument.recompute()

-   **myObj = FreeCAD.ActiveDocument.addObject(\"Part::FeaturePython\", \"Rectangle\")** : crée un nouvel objet **Part::FeaturePython** nommé **Rectangle** dans le document FreeCAD actif. Cet objet est spécifiquement conçu pour un comportement paramétrique personnalisé, permettant à la logique définie par Python de gérer ses propriétés et son comportement.

-   **ParamRectangle.ParametricRectangle(myObj)** : initialise l\'objet en l\'associant à la classe **ParametricRectangle** du module ou du script **ParamRectangle**. Cela permet de lier la logique personnalisée définie par Python à l\'objet, ce qui lui permet d\'agir comme un objet paramétrique.

-   **myObj.ViewObject.Proxy = 0** : réinitialise l\'attribut **ViewObject.Proxy** à 0, garantissant que l\'objet utilise la gestion de la vue par défaut de FreeCAD. Cette étape est nécessaire à moins que vous ne définissiez un ViewProvider personnalisé pour gérer la représentation visuelle de l\'objet.

-   **FreeCAD.ActiveDocument.recompute()** : recalcule le document pour mettre à jour la géométrie et refléter les changements dans l\'interface graphique de FreeCAD, rendant le nouvel objet entièrement visible et fonctionnel.

Rien ne s\'affiche encore à l\'écran, car les propriétés **Length** et **Width** sont à 0, ce qui déclenchera notre condition de \"ne rien faire\" à l\'intérieur de l\'exécution. Nous devons juste changer les valeurs de Longueur et Largeur, et notre objet apparaîtra magiquement et sera recalculé à la volée.

Bien sûr, il serait fastidieux de devoir taper ces 4 lignes de code Python chaque fois que nous voulons créer un nouveau rectangle paramétrique. Une façon très simple de résoudre ceci est de placer les 4 lignes ci-dessus dans notre fichier **ParamRectangle.py**, à la fin, après la fin de la classe **ParametricRectange** (nous pouvons le faire à partir de l\'éditeur Macro).

Maintenant, lorsque nous tapons import ParamRectangle, un nouveau rectangle paramétrique sera automatiquement créé. Encore mieux, nous pouvons ajouter un bouton de barre d\'outils qui fera exactement cela :

-   Ouvrir le menu **Outils -\> Personnaliser\...**
-   Sous l\'onglet \"Macros\", sélectionnez notre macro ParamRectangle.py, complétez les détails au fur et à mesure que vous le souhaitez, et appuyez sur \"Ajouter\" :

![](images/FreeCAD_python_macroRec.png )

Sous l\'onglet Barres d\'outils, créez une nouvelle barre d\'outils personnalisée dans l\'atelier de votre choix (ou globalement), sélectionnez votre macro et ajoutez-la à la barre d\'outils :

![](images/FreeCAD_python_toolbarCus.png )

-   Nous avons maintenant un nouveau bouton de barre d\'outils qui, lorsqu\'il sera cliqué, créera un rectangle paramétrique.

N\'oubliez pas que si vous souhaitez distribuer des fichiers créés avec ce nouvel outil à d\'autres personnes, celles-ci doivent également avoir la macro **ParamRectangle.py** installée sur leur ordinateur.

**Lire plus d\'informations**

-   [Le dépôt de macros FreeCAD](Macros_recipes.md)
-   [Exemple d\'objet paramétrique](Scripted_objects.md)
-   [Plus d\'exemples dans le code FreeCAD](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:Creating parametric objects/fr
