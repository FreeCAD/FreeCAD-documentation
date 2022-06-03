# Scripted objects migration/fr
## Introduction

Les [Objets créés par script](Scripted_objects/fr.md) sont reconstruits à chaque fois qu\'un [document au format FCStd](File_Format_FCStd/fr.md) est ouvert. Pour ce faire, le document conserve une référence au module et à la classe Python qui ont été utilisés pour créer l\'objet, ainsi que ses propriétés.


{{Code|lang=xml|code=
<Document SchemaVersion="4" ProgramVersion="0.19R20959 (Git)" FileVersion="1">
    ...
    <Properties Count="15" TransientCount="3">
    ...
    </Properties>
    <Objects Count="1" Dependencies="1">
        <ObjectDeps Name="Custom" Count="0"/>
        <Object type="Part   *   *FeaturePython" name="Custom" id="2715" Touched="1" />
    </Objects>
    <ObjectData Count="1">
        <Object name="Custom">
            <Properties Count="9" TransientCount="0">
                ...
                <Property name="Proxy" type="App   *   *PropertyPythonObject" status="1">
                    <Python value="eyJUeXBlIjogIkN1c3RvbSJ9" encoded="yes" module="old_module" class="OldObject"/>
                </Property>
                ...
            </Properties>
        </Object>
    </ObjectData>
</Document>
}}

Concentrez-vous particulièrement sur cette partie    * {{Code|lang=xml|code=
                ...
                <Property name="Proxy" type="App   *   *PropertyPythonObject" status="1">
                    <Python value="eyJUeXBlIjogIkN1c3RvbSJ9" encoded="yes" module="old_module" class="OldObject"/>
                </Property>
                ...
}}

Si la valeur de module= ou class= n\'est pas trouvée sur le système installé, l\'objet ne pourra pas être chargé correctement. Cela signifie qu\'une fois qu\'un objet est créé en utilisant une classe particulière, le module ne doit plus être déplacé ou renommé, car si cela est fait, les objets précédemment enregistrés se briseront.

Toutefois, une raison valable pour déplacer ou renommer le module ou la classe est d\'améliorer la structure et la maintenabilité du code d\'origine, par exemple, lors de la restructuration d\'un atelier entier. Dans ce cas, il existe plusieurs stratégies pour faire migrer les anciens objets vers l\'utilisation d\'une nouvelle classe. Ceci est fait afin de conserver la compatibilité ascendante, lorsque la rupture pure et simple des anciens documents doit être évitée.

## Ancien et nouvel objet 

### Ancien objet 

Un ancien objet est défini dans un module qui se trouve à la racine de l\'atelier. 
```python
# old_module.py
class OldObject   *
    def __init__(self, obj)   *
        obj.addProperty("App   *   *PropertyLength", "Length")
        obj.addProperty("App   *   *PropertyArea", "Area")
        obj.Length = 15
        obj.Area = 300
        obj.Proxy = self
        self.Type = "Custom"

    def execute(self, obj)   *
        pass
```

Un objet peut être créé à l\'aide de cette classe et il peut être enregistré dans **my_document.FCstd**. Si aucun [viewprovider](viewprovider/fr.md) particulier n\'est attribué au nouvel objet, sa classe proxy est simplement définie sur une valeur différente de `None`, dans ce cas, sur `1`. 
```python
import FreeCAD as App
import old_module

doc = App.newDocument()
doc.FileName = "my_document.FCStd"

obj = doc.addObject("Part   *   *FeaturePython", "Custom")
old_module.OldObject(obj)

if App.GuiUp   *
    obj.ViewObject.Proxy = 1

doc.recompute()
doc.save()
```

Une session de [console Python](Python_console/fr.md) avec les propriétés de base omises. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.PropertiesList)
['Area', ..., ..., ..., 'Length', ..., ..., ..., ...]
>>> print(obj.Proxy)
<old_module.OldObject object at 0x7efc3c51c390>
```

### Nouvel objet 

Considérons maintenant que l\'atelier est restructuré, de sorte que les classes ne se trouvent pas seulement dans le répertoire racine, mais plutôt dans un répertoire **objects**. Les ateliers complexes qui comportent de nombreux types d\'objets différents devraient être structurés en répertoires comprenant des objets, des interfaces [viewproviders](Viewprovider/fr.md), [Commandes Gui](Command/fr.md), [Panneau des tâches](Task_panel/fr.md), etc. 
```python
# objects/new_module.py
class NewObject   *
    def __init__(self, obj)   *
        obj.addProperty("App   *   *PropertyLength", "Length")
        obj.addProperty("App   *   *PropertyArea", "GeneralArea")
        obj.addProperty("App   *   *PropertyInteger", "Divisions")
        obj.Length = 30
        obj.GeneralArea = 600
        obj.Divisions = 4
        obj.Proxy = self
        self.Type = "Custom"

    def execute(self, obj)   *
        pass
```

Cette nouvelle classe fera référence au même type d\'objet, mais le nom du module ainsi que le nom de la classe ont été renommés. De plus, les propriétés ont également changé ; une propriété a été renommée et une propriété complètement nouvelle a été ajoutée.

Si nous créons un nouvel objet avec ce nouveau module, nous aurons la session de console suivante. 
```python
>>> obj2 = App.ActiveDocument.Custom2
>>> print(obj2.PropertiesList)
['Divisions', ..., 'GeneralArea', ..., ..., 'Length', ..., ..., ..., ...]
>>> print(obj2.Proxy)
<objects.new_module.NewObject object at 0x7efc1cf68c50>
```

## Méthode 1. Migration en redirigeant la classe 

Nous allons migrer l\'ancien objet en redirigeant l\'ancienne classe. La classe originale est supprimée, et le nom de la classe est simplement redirigé pour pointer vers la nouvelle classe.


```python
# old_module.py
import objects.new_module as new_module

OldObject = new_module.NewObject
```

Tout document qui tente de charger `old_module.OldObject` sera redirigé pour charger `objects.new_module.NewObject` à la place.

Si nous ouvrons le document et inspectons les propriétés de l\'objet dans la [console Python](Python_console/fr.md), nous verrons que les anciennes propriétés sont conservées, mais que l\'objet a une nouvelle classe Proxy. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.PropertiesList)
['Area', ..., ..., ..., 'Length', ..., ..., ..., ...]
>>> print(obj.Proxy)
<objects.new_module.NewObject object at 0x7f099700b2b0>
```

Cependant, dans ce cas, nous ne voyons pas les nouvelles propriétés de la nouvelle classe. La raison en est simplement que l\'ancien objet ne possédait pas ces propriétés. Lorsque `old_module.OldObject` a été redirigé vers `objects.new_module.NewObject`, seule la classe proxy a changé, mais les informations précédentes ont été conservées.

Désormais, si le document est enregistré et rouvert, il recherchera automatiquement `objets.nouveau_module.NewObject` et ne nécessitera plus `ancien_module.OldObject`. Le fichier **old_module.py** peut être supprimé définitivement du système tant que tous les anciens objets ont été migrés vers le nouveau module. Si l\'ancien module est supprimé mais qu\'un objet n\'a pas été migré, la [Vue rapport](Report_view/fr.md) affichera un message comme celui-ci lors de l\'ouverture d\'un document contenant cet objet.


{{Code|lang=bash|code=
<class 'ModuleNotFoundError'>   * No module named 'old_module'
}}

S\'il n\'est pas possible, de manière réaliste, de migrer tous les anciens objets, par exemple parce que l\'ancien module a été utilisé dans un atelier pendant de nombreuses années, alors **old_module.py** doit être conservé aussi longtemps qu\'il est jugé nécessaire pour donner aux utilisateurs la possibilité de migrer leurs objets.

### Avantages et inconvénients 

**Avantages**

-   <img alt="" src=images/Edit_OK.svg  style="width   *24px;"> C\'est la méthode la plus simple qui nécessite juste de rediriger une ancienne classe vers une nouvelle classe.
-   <img alt="" src=images/Edit_OK.svg  style="width   *24px;"> Les anciennes propriétés sont conservées tant que la nouvelle classe ne les surcharge pas.
-   <img alt="" src=images/Edit_OK.svg  style="width   *24px;"> C\'est une bonne chose si l\'ancienne et la nouvelle classe ont les mêmes propriétés (gèrent le même type de données) mais que seul leur nom de module ou de classe est différent.

**Inconvénients**

-   <img alt="" src=images/Edit_Cancel.svg  style="width   *24px;"> La nouvelle classe conserve les anciennes propriétés de l\'objet, ce qui n\'est pas toujours souhaité.
-   <img alt="" src=images/Edit_Cancel.svg  style="width   *24px;"> Les nouvelles propriétés ou les propriétés renommées ne sont pas gérées, donc l\'objet sera chargé mais il peut ne pas montrer le comportement correct de la nouvelle classe.
-   <img alt="" src=images/Edit_Cancel.svg  style="width   *24px;"> L\'ancien module peut devoir être conservé indéfiniment pour migrer tous les anciens objets créés dans le passé.

## Méthode 2. Migration lors de la restauration du document 

Nous allons migrer l\'ancien objet en modifiant l\'ancienne classe. La majorité de la classe d\'origine est supprimée et à la place la méthode `onDocumentRestored` est implémentée. Lorsque cette méthode existe, elle s\'exécute lorsque le document tente de restaurer un objet qui utilise la classe. C\'est donc l\'occasion pour nous d\'attribuer une nouvelle classe, de manipuler les informations ou d\'imprimer des messages.

Dans ce cas, nous supposons que nous avons également défini un nouveau [viewprovider](viewprovider/fr.md) dans le module **viewp/new_view.py**. Si nous ne voulons pas migrer cette classe, nous pouvons omettre tout ce qui se trouve après la vérification `App.GuiUp`. 
```python
# old_module.py
import FreeCAD as App
import objects.new_module as new_module
import viewp.new_view as new_view
_wrn = App.Console.PrintWarning

class OldObject   *
    def onDocumentRestored(self, obj)   *
        new_module.NewObject(obj)
        _wrn("New proxy class used\n")

        if App.GuiUp   *
            new_view.ViewProviderNew(obj.ViewObject)
            _wrn("New viewprovider class used\n")
```

Un exemple plus complexe vérifie d\'abord que la classe proxy est du type que nous recherchons, et ne procède à la migration que si c\'est le bon type. 
```python
class OldObject   *
    def onDocumentRestored(self, obj)   *
        if hasattr(obj, "Proxy") and obj.Proxy.Type == "Custom"   *
            _module = str(obj.Proxy.__class__)
            _module = _module.lstrip("<class '").rstrip("'>")

            if _module == "old_module.OldObject"   *
                self._migrate(obj)

    def _migrate(self, obj)   *
        _wrn("New proxy class used\n")
        new_module.NewObject(obj)

        if App.GuiUp   *
            new_view.ViewProviderNew(obj.ViewObject)
            _wrn("New viewprovider class used\n")
```

En supposant que nous avons déjà modifié l\'ancien module de cette manière, si nous ouvrons un document avec un ancien objet, nous verrons les messages mentionnant l\'utilisation des nouvelles classes.

En inspectant l\'objet depuis la [console Python](Python_console/fr.md), nous verrons que les anciennes propriétés sont conservées, et qu\'en plus, de nouvelles propriétés ont été ajoutées avec la nouvelle classe Proxy. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.PropertiesList)
['Area', 'Divisions', ..., 'GeneralArea', ..., ..., 'Length', 'Length1', ..., ..., ..., ...]
>>> print(obj.Proxy)
<objects.new_module.NewObject object at 0x7fecb0ebd7b8>
```

Les anciennes propriétés étaient `Area` et `Length` ; les nouvelles propriétés sont `Divisions`, `GeneralArea` et `Length`. L\'objet migré conserve les deux propriétés d\'origine et acquiert trois nouvelles propriétés. Cependant, comme la nouvelle `Length` a le même nom que l\'ancienne propriété, la nouvelle propriété est renommée avec un numéro incrémental. Ce n\'est sans doute pas ce que nous voulons. Nous pouvons améliorer la situation en suivant l\'addendum 2.1 ci-dessous.

Étant donné que les classes sont censées gérer le même type d\'objet, nous aimerions une migration dans laquelle `Area` se transforme en `GeneralArea`, et `Length` est simplement affecté au nouveau `Length`, et il n\'y a pas de propriétés en double.

### Avantages et inconvénients 

**Avantages**

-   <img alt="" src=images/Edit_OK.svg  style="width   *24px;"> Cette méthode nous permet de vérifier que la classe que nous migrons est la bonne, au lieu de simplement rediriger vers une classe plus récente.
-   <img alt="" src=images/Edit_OK.svg  style="width   *24px;"> Similaire à la méthode 1, les anciennes propriétés sont conservées tant que la nouvelle classe ne les surcharge pas.
-   <img alt="" src=images/Edit_OK.svg  style="width   *24px;"> Contrairement à la méthode 1, les nouvelles propriétés sont toujours ajoutées, cependant si elles ont le même nom, elles seront renommées.
-   <img alt="" src=images/Edit_OK.svg  style="width   *24px;"> La migration n\'est pas immédiate, on peut encore manipuler les informations, ou imprimer des messages pendant que l\'objet se charge.

**Inconvénients**

-   <img alt="" src=images/Edit_Cancel.svg  style="width   *24px;"> Elle est plus verbeuse que la méthode 1 car nous devons implémenter la méthode `onDocumentRestored` pour migrer l\'objet.
-   <img alt="" src=images/Edit_Cancel.svg  style="width   *24px;"> Il ajoute toujours les nouvelles propriétés, donc il peut créer des propriétés dupliquées dans le cas où les nouvelles propriétés ont le même nom que les anciennes propriétés. Ceci doit être géré manuellement.

## Méthode 3. Migration lors de la restauration du document, manipulation manuelle des propriétés 

Il s\'agit d\'une extension de la méthode 2. Dans la méthode `onDocumentRestored`, nous devons enregistrer les valeurs des propriétés que nous voulons, puis nous pouvons supprimer ces propriétés originales. Ainsi, lorsque la nouvelle classe sera utilisée, elle attribuera les nouvelles propriétés sans risquer de collision de noms avec les anciennes propriétés.

Comme dans la méthode 2, si nous le souhaitons, nous pouvons également ajouter le morceau de code qui vérifie que la classe Proxy est la bonne. Dans cet exemple, nous supposons une fois de plus que nous utilisons un [viewprovider](Viewprovider/fr.md) personnalisé, avec au moins une propriété personnalisée. 
```python
# old_module.py
import FreeCAD as App
import objects.new_module as new_module
import viewp.new_view as new_view
_wrn = App.Console.PrintWarning

class OldObject   *
    def onDocumentRestored(self, obj)   *
        old = dict()
        old["Area"] = obj.Area
        old["Length"] = obj.Length
        obj.removeProperty("Area")
        obj.removeProperty("Length")

        new_module.NewObject(obj)

        obj.GeneralArea = 3 * old["Area"]
        obj.Length = old["Length"]
        _wrn("New proxy class used; properties migrated\n")

        if App.GuiUp   *
            vobj = obj.ViewObject
            old = dict()

            old["LineScale"] = vobj.LineScale
            vobj.removeProperty("LineScale")

            new_view.ViewProviderNew(vobj)

            vobj.LineScale = 1.05 * old["LineScale"]
            _wrn("New viewprovider class used; view properties migrated\n")
```

Nous pouvons voir que les anciennes valeurs sont stockées dans un dictionnaire auxiliaire, puis les anciennes propriétés sont supprimées, puis nous ajoutons la nouvelle classe, et enfin nous assignons les valeurs précédemment sauvegardées aux nouvelles propriétés. À ce moment, nous pouvons transformer les valeurs sauvegardées comme il se doit pour la nouvelle classe. Par exemple, le `GeneralArea` est fixé à 3 fois l\'ancien `Area`, et le nouveau `Length` reçoit simplement la valeur de l\'ancien `Length`. Comme nous savons comment l\'ancienne et la nouvelle classe sont censées se comporter, nous avons la liberté de manipuler les données pour faire migrer l\'objet comme nous le souhaitons.

Nous ne pouvons supprimer que les propriétés qui ont été ajoutées par les classes [Python](Python/fr.md) lorsque nous avons construit l\'[Objet créé par script](scripted_objects/fr.md). Les autres attributs appartiennent à l\'objet C++ de base et ne peuvent pas être supprimés. 
```python
>>> obj.removeProperty("Visibility")
False
```

En supposant que nous avons déjà modifié l\'ancien module de cette manière, si nous ouvrons un document avec un ancien objet, nous verrons les messages mentionnant l\'utilisation des nouvelles classes. En inspectant l\'objet depuis la [console Python](Python_console/fr.md), nous voyons que les anciennes propriétés ont été supprimées et que seules les nouvelles propriétés existent. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.PropertiesList)
['Divisions', ..., 'GeneralArea', ..., ..., 'Length', ..., ..., ..., ...]
>>> print(obj.Proxy)
<objects.new_module.NewObject object at 0x7efd456c9b00>
```

Comme la propriété `Divisions` n\'existait pas dans l\'ancienne classe, rien n\'a été fait avec elle. Elle a simplement été créée par la nouvelle classe `objects.new_module.NewObject`.

### Avantages et inconvénients 

**Avantages**

-   <img alt="" src=images/Edit_OK.svg  style="width   *24px;"> Similaire à la méthode 2, cette méthode nous permet de vérifier que la classe que nous migrons est la bonne.
-   <img alt="" src=images/Edit_OK.svg  style="width   *24px;"> Nous avons le contrôle total de ce qu\'il faut faire avec les anciennes propriétés. Typiquement, elles seront supprimées afin qu\'il n\'y ait pas de collision de noms avec les nouvelles propriétés ajoutées. Ainsi nous évitons les propriétés dupliquées.
-   <img alt="" src=images/Edit_OK.svg  style="width   *24px;"> En sauvegardant les anciennes valeurs, nous pouvons manipuler les informations de l\'étape de restauration comme nous le souhaitons, et affecter les valeurs correspondantes aux nouvelles propriétés.

**Inconvénients**

-   <img alt="" src=images/Edit_Cancel.svg  style="width   *24px;"> Cette méthode est très verbeuse par rapport aux précédentes, car nous devons implémenter la méthode `onDocumentRestored`, et traiter chacune des propriétés individuellement (enregistrer la valeur, supprimer la propriété, réassigner la valeur). Ceci est problématique si l\'objet que nous voulons migrer possède de nombreuses propriétés, ou si leurs valeurs doivent être transformées de manière très spéciale.

## Addendum A. Créer les propriétés uniquement si elles n\'existent pas déjà 

L\'un des inconvénients de la méthode 2 est qu\'elle essaiera toujours d\'ajouter les nouvelles propriétés. Si les anciennes propriétés ont le même nom que les nouvelles, elles seront dupliquées avec un numéro incrémental, ainsi `Length` donnera `Length1`, puis `Length2`, et ainsi de suite. Cela fait de la méthode 2 une option irréaliste dans la plupart des cas, car la nouvelle classe n\'utilisera de toute façon qu\'une seule propriété.

Pour améliorer cette méthode, la nouvelle classe peut également être modifiée pour n\'ajouter les propriétés que si elles n\'existent pas déjà sous le même nom. 
```python
# objects/new_module.py
class NewObject   *
    def __init__(self, obj)   *
        if not hasattr(obj, "Length")   *
            obj.addProperty("App   *   *PropertyLength", "Length")
            obj.Length = 30
        if not hasattr(obj, "GeneralArea")   *
            obj.addProperty("App   *   *PropertyArea", "GeneralArea")
            obj.GeneralArea = 600
        if not hasattr(obj, "Divisions")   *
            obj.addProperty("App   *   *PropertyInteger", "Divisions")
            obj.Divisions = 4

        obj.Proxy = self
        self.Type = "Custom"

    def execute(self, obj)   *
        pass
```

Dans ce cas, puisque `Length` existe déjà, elle ne sera pas ajoutée à nouveau ; `GeneralArea` et `Divisions` n\'existent pas, elles seront donc ajoutées. Et comme précédemment, `Area` sera conservé car il n\'est pas explicitement supprimé, bien qu\'il ne soit peut-être plus utilisé dans la nouvelle classe. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.PropertiesList)
['Area', 'Divisions', ..., 'GeneralArea', ..., ..., 'Length', ..., ..., ..., ...]
>>> print(obj.Proxy)
<objects.new_module.NewObject object at 0x7f036bd4c6a0>
```

La même chose peut être faite pour la classe du [viewprovider](viewprovider/fr.md).

En utilisant cette méthode 2 + A, le résultat est similaire à la méthode 1 en ce sens que l\'objet conservera toutes les propriétés précédentes, mais en plus il gagnera les nouvelles propriétés fournies par la nouvelle classe.

La méthode 3 n\'a pas besoin de cet addendum à la nouvelle classe car les anciennes propriétés sont explicitement supprimées, il n\'y aura donc aucun conflit lors de l\'installation des nouvelles propriétés. Néanmoins, c\'est toujours une bonne pratique que chaque classe ajoute ses propriétés requises seulement si celles-ci n\'existent pas déjà. Ceci est utile à la fois dans le cas de la création de nouveaux [Objets créés par script](scripted_objects/fr.md) ou de leur migration.

### Avantages et inconvénients 

**Avantages**

-   <img alt="" src=images/Edit_OK.svg  style="width   *24px;"> L\'objet conservera toutes les propriétés précédentes, mais en plus il gagnera de nouvelles propriétés sans répétition.

**Inconvénients**

-   <img alt="" src=images/Edit_Cancel.svg  style="width   *24px;"> Comme la méthode 2, elle ne traite toujours pas les propriétés renommées. Les anciennes propriétés doivent être supprimées manuellement.

## Addendum B. Migration de différentes versions de l\'ancien objet 

La méthode 3 est la plus complexe car les propriétés sont traitées individuellement. Cependant, dans cette méthode, nous disposons également d\'une flexibilité totale dans la manière de manipuler les données, ce qui constitue un avantage si nous voulons effectuer des opérations complexes.

Si, dès le début, nous créons une propriété qui contient le numéro de version de notre objet, nous pourrons utiliser ce numéro à l\'avenir pour effectuer une migration spécifique de cette version vers une autre. Nous définissons la propriété comme étant en lecture seule, de sorte que nous ne pouvons pas l\'écraser dans l\'[Éditeur de propriétés](Property_editor/fr.md), bien qu\'elle soit toujours accessible depuis la [console Python](Python_console/fr.md). 
```python
# old_module.py
class OldObject   *
    def __init__(self, obj)   *
        obj.addProperty("App   *   *PropertyLength", "Length")
        obj.addProperty("App   *   *PropertyArea", "Area")
        obj.addProperty("App   *   *PropertyString", "Version")
        obj.setEditorMode("Version", 1)
        obj.Length = 15
        obj.Area = 300
        obj.Version = "0.18"
        obj.Proxy = self
        self.Type = "Custom"

    def execute(self, obj)   *
        pass
```

Ensuite, lorsque nous voulons migrer l\'objet, nous implémentons la méthode `onDocumentRestored` et testons cette version. 
```python
# old_module.py
import FreeCAD as App
import objects.new_module as new_module
_wrn = App.Console.PrintWarning

class OldObject   *
    def onDocumentRestored(self, obj)   *
        if hasattr(obj, "Version") and obj.Version   *
            if obj.Version == "0.18"   *
                _migrate_from_018(obj)
            elif obj.Version == "0.19"   *
                _migrate_from_019(obj)

def _migrate_from_018(obj)   *
    old = dict()
    old["Area"] = obj.Area
    old["Length"] = obj.Length
    obj.removeProperty("Area")
    obj.removeProperty("Length")
    obj.removeProperty("Version")

    new_module.NewObject(obj)

    obj.GeneralArea = 3 * old["Area"]
    obj.Length = old["Length"]
    obj.Version = "0.20"
    _wrn("New proxy class used; properties migrated\n")

def _migrate_from_019(obj)   *
    ...
```

Nous ne sauvegardons pas la valeur `Version` car nous définirons un nouveau numéro `Version` lors de la migration. Comme le montre l\'exemple, nous pouvons implémenter diverses fonctions pour chaque version correspondante de l\'objet que nous avons l\'intention de migrer. Nous omettons la migration des propriétés du [viewprovider](viewprovider/fr.md) mais elle suit le même schéma.

### Avantages et inconvénients 

**Avantages**

-   <img alt="" src=images/Edit_OK.svg  style="width   *24px;"> Nous avons un contrôle total sur ce qu\'il faut faire avec les anciennes propriétés, et sur la façon d\'effectuer la migration.
-   <img alt="" src=images/Edit_OK.svg  style="width   *24px;"> Nous pouvons implémenter une méthode particulière pour migrer une version particulière de l\'ancien objet.

**Inconvénients**

-   <img alt="" src=images/Edit_Cancel.svg  style="width   *24px;"> Cette méthode est très verbeuse car nous devons avoir une idée claire de la façon de traiter chacune des propriétés de chaque \"version\" que nous voulons migrer. Si notre objet possède de nombreuses versions différentes créées au fil des ans, nous devrons peut-être préparer une longue liste de méthodes pour les faire migrer vers l\'objet le plus récent.

## Addendum B2. Utilisation des attributs internes de la classe au lieu des propriétés 

Au lieu d\'utiliser une [propriété](property/fr.md) de l\'objet pour contenir l\'information de version, nous pouvons utiliser un attribut de la classe. De cette façon, nous \"cachons\" l\'information sur la version, car les propriétés sont normalement publiques et visibles dans l\'[éditeur de propriétés](property_editor/fr.md), alors que les attributs de classe ne peuvent être manipulés qu\'à partir de la [console Python](Python_console/fr.md). Les attributs de classe peuvent être sauvegardés et restaurés comme expliqué dans [Sauvegarde des attributs des objets scripts](Scripted_objects_saving_attributes/fr.md). 
```python
# old_module.py
class OldObject   *
    def __init__(self, obj)   *
        obj.addProperty("App   *   *PropertyLength", "Length")
        obj.addProperty("App   *   *PropertyArea", "Area")
        obj.Length = 15
        obj.Area = 300
        obj.Proxy = self

        self.Type = "Custom"
        self.ver = "0.18"

    def execute(self, obj)   *
        pass
```

Cet attribut est inspecté en regardant l\'attribut `Proxy`. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.Proxy.ver)
0.18
```

Ensuite, le fichier est modifié pour migrer l\'objet. 
```python
# old_module.py
import FreeCAD as App
import objects.new_module as new_module
_wrn = App.Console.PrintWarning

class OldObject   *
    def onDocumentRestored(self, obj)   *
        if hasattr(obj.Proxy, "ver") and obj.Proxy.ver   *
            if obj.Proxy.ver == "0.18"   *
                _migrate_from_018(obj)

def _migrate_from_018(obj)   *
    old = dict()
    old["Area"] = obj.Area
    old["Length"] = obj.Length
    obj.removeProperty("Area")
    obj.removeProperty("Length")

    new_module.NewObject(obj)

    obj.GeneralArea = 3 * old["Area"]
    obj.Length = old["Length"]
    _wrn("New proxy class used; properties migrated\n")
```

Lorsque nous installons la nouvelle classe, celle-ci doit définir la nouvelle valeur de l\'attribut version, par exemple, self.ver = "0.20".

## Addendum C. Méthode 3 sans supprimer les anciennes propriétés qui portent le même nom 

Comme dans l\'addendum A, nous pouvons écrire la nouvelle classe pour créer des propriétés uniquement si elles ne sont pas déjà présentes. En utilisant la méthode 3, nous sauvegardons les valeurs des anciennes propriétés, puis nous supprimons les anciennes propriétés. Cependant, si les nouvelles propriétés sont nommées de la même manière que les anciennes, il n\'est pas nécessaire de supprimer les anciennes, nous pouvons simplement réutiliser la même propriété, car nous savons que la propriété ne sera pas dupliquée. Si nous utilisons l\'addendum B, nous avons également un moyen d\'interroger la version.


```python
# old_module.py
import FreeCAD as App
import objects.new_module as new_module
_wrn = App.Console.PrintWarning

class OldObject   *
    def onDocumentRestored(self, obj)   *
        if hasattr(obj, "Version") and obj.Version   *
            if obj.Version == "0.18"   *
                _migrate_from_018(obj)

def _migrate_from_018(obj)   *
    old = dict()
    old["Area"] = obj.Area
    obj.removeProperty("Area")

    new_module.NewObject(obj)

    obj.GeneralArea = 3 * old["Area"]
    obj.Version = "0.20"
    _wrn("New proxy class used; properties migrated\n")
```

Comme nous le voyons dans l\'exemple, l\'ancienne propriété `Area` est supprimée et migrée vers la nouvelle propriété `GeneralArea` comme d\'habitude. Nous n\'avons pas besoin de supprimer `Length` ni `Version` parce que dans la nouvelle classe ils sont toujours utilisés avec le même nom, et ils ne seront pas créés à nouveau (addendum A). Comme nous ne voulons pas modifier `Length`, cette propriété n\'est pas touchée du tout ; elle est migrée vers la nouvelle classe en silence. Par contre, nous mettons à jour `Version` avec la nouvelle valeur. Nous omettons la migration des propriétés de [viewprovider](viewprovider/fr.md) mais elle suit le même schéma.

Cela devrait fonctionner comme la méthode 3, c\'est-à-dire que les anciennes propriétés sont supprimées et que seules les nouvelles propriétés restent dans le nouvel objet. La seule différence est que nous omettons de supprimer et de recréer les propriétés qui portent le même nom. Ce processus devrait fonctionner tant que l\'ancienne [propriété](property/fr.md) et la nouvelle [propriété](property/fr.md) ont le même type (par exemple, `App   *   *PropertyLength` ou `App   *   *PropertyArea`), de sorte que l\'ancienne propriété peut transmettre sa valeur directement. Cependant, si la nouvelle propriété a un type différent de l\'ancienne, l\'ancienne propriété doit être supprimée, sinon l\'ancienne propriété écrasera complètement la nouvelle, ce qui n\'est probablement pas ce que nous voulons car la nouvelle classe s\'attendra au nouveau type et non à l\'ancien.

### Avantages et inconvénients 

**Avantages**

-   <img alt="" src=images/Edit_OK.svg  style="width   *24px;"> Comme la méthode 3, cette méthode nous permet un contrôle complet de la migration des anciennes informations.
-   <img alt="" src=images/Edit_OK.svg  style="width   *24px;"> Nous évitons d\'écrire du code qui supprime et recrée des propriétés dont le nom est identique.

**Inconvénients**

-   <img alt="" src=images/Edit_Cancel.svg  style="width   *24px;"> Comme la méthode 3, cette méthode est encore très verbeuse car nous devons manipuler les propriétés avec soin.
-   <img alt="" src=images/Edit_Cancel.svg  style="width   *24px;"> Si une nouvelle [propriété](property/fr.md) et une ancienne [propriété](property/fr.md) partagent le même nom, la nouvelle propriété sera écrasée, ce qui peut être un comportement indésirable, surtout si les deux propriétés ont des types différents. Dans ce cas, la suppression de l\'ancienne propriété et la migration manuelle de sa valeur sont toujours nécessaires.

## Résumé

Chacune des méthodes a une utilisation recommandée    *

-   Méthode 1. Le module est déplacé ou renommé mais les propriétés sont les mêmes. Redirection simple des classes car les propriétés n\'ont pas besoin d\'être modifiées du tout.
-   Méthode 2+A. Scénarios de migration simples. Affichage d\'un message lorsque l\'objet est migré d\'une classe à une autre. Les propriétés sont du même type et n\'ont pas besoin d\'être modifiées du tout.
-   Méthode 3, 3+A ou 3+B. Scénarios de migration complexes. Contrôle total des propriétés, suppression des anciennes propriétés et ajout de nouvelles propriétés. Un identifiant pour connaître la version de l\'objet est utile pour choisir la bonne fonction pour effectuer la migration (Addendum B ou B2).

Évitez de préférence les méthodes suivantes    *

-   Méthode 2. Les propriétés seront dupliquées si la nouvelle classe ne vérifie pas les propriétés existantes (Addendum A).
-   Méthode 3+C. A n\'utiliser que lorsque les anciennes propriétés et les nouvelles propriétés sont du même type. Sinon, utilisez la méthode 3 ou 3+B pour supprimer les anciennes propriétés, et traitez-les exactement comme il se doit.

## Liens

-   [Migrer et mettre à jour les anciens objets scriptés](https   *//forum.freecadweb.org/viewtopic.php?t=42948)
-   [Migrer les anciens objets scriptés](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=46218)


 

[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Scripted objects migration/fr
