# FeaturePython Custom Properties/fr
## Introduction

Voir aussi : [Documentation API générée automatiquement (documentation C++)](https://freecad.github.io/SourceDoc/dd/dc2/namespaceApp.html).

Les propriétés sont les véritables blocs de construction des objets FeaturePython. Grâce à elles, l\'utilisateur pourra interagir et modifier votre objet. Après avoir créé un nouvel objet FeaturePython dans votre document :


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "Box")
```

Vous pouvez obtenir une liste des propriétés disponibles en émettant :


```python
obj.supportedProperties()
```



##  Créer un objet FeaturePython et lui ajouter une propriété 

Ce code créera un objet avec le nom interne `InternalObjectName` (automatiquement renommé en `InternalObjectName001` et ainsi de suite, si un objet nommé `InternalObjectName` existe déjà) et lui affectera l\'étiquette personnalisée `User-friendly label`. Cette étiquette sera affichée dans la [Vue en arborescence](Tree_view/fr.md). Les [Expressions](Expressions/fr.md) peuvent faire référence à cet objet par son étiquette en utilisant `<<User-friendly label>>`.


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
```

Pour ajouter une propriété à cet objet, utilisez la forme longue de `addProperty` comme indiqué ci-dessous. FreeCAD divisera automatiquement `ThePropertyName` et l\'affichera avec des espaces (`The Property Name`) dans l\'[Onglet Données de la vue Propriété](Property_editor/fr#Vue_et_Propri.C3.A9t.C3.A9s_des_donn.C3.A9es.md).


```python
obj.addProperty("App::PropertyBool", "ThePropertyName", "Subsection", "Description for tooltip")
```


`App::PropertyBool`

est le type de la propriété. Les différents types sont décrits plus en détail ci-dessous.

Vous pouvez également utiliser la forme courte qui omet les deux derniers arguments. La sous-section a par défaut la valeur `Base` et l\'infobulle n\'est pas affichée avec ce formulaire.


```python
obj.addProperty("App::PropertyBool", "ThePropertyName")
```

Pour obtenir ou définir la propriété, utilisez `obj.ThePropertyName` :


```python
# set
obj.ThePropertyName = True
# get
thePropertyValue = obj.ThePropertyName
```

Si le type de la propriété est [App::PropertyEnumeration](#App:_PropertyEnumeration.md), le setter a un comportement spécial : la définition d\'une liste de chaînes définit les cas autorisés par l\'énumération, la définition d\'une chaîne sélectionne l\'un de ces cas. Pour définir la liste des cas possibles et définir le cas actuel, utilisez :


```python
# allowed cases
obj.ThePropertyName = ["aaa", "bbb", "ccc"]
# set
obj.ThePropertyName = "bbb"
```


{{Version/fr|1.0}}

: l\'argument {{Incode|enum_vals}} de la fonction {{Incode|addProperty}} peut également être utilisé pour définir les cas d\'énumération.


{{Version/fr|1.0}}

: la signature complète de la fonction est :


```python
obj.addProperty(type: string, name: string, group="", doc="", attr=0, read_only=False, hidden=False, enum_vals=[])
```

-    {{Incode|type}}: type de propriété.

-    {{Incode|name}}: nom de la propriété.

-    {{Incode|group}}: sous-section de la propriété.

-    {{Incode|doc}}: infobulle.

-    {{Incode|attr}}: attribut, voir [Objets créés par script](Scripted_objects/fr#Attributs_des_propriétés.md).

-    {{Incode|read_only}}: voir idem.

-    {{Incode|hidden}}: voir idem.

-    {{Incode|enum_vals}}: valeurs d\'énumération (liste de chaînes), uniquement pertinentes si le type est [App::PropertyEnumeration](#App:_PropertyEnumeration.md).

## App::PropertyAcceleration

Une propriété {{TODO}}acceleration. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyAcceleration", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyAmountOfSubstance

## App::PropertyAngle

Une propriété d\'angle. Elle peut contenir une valeur `angle`. Vous pouvez utiliser la variable \"Value\" pour obtenir une variable flottante. Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyAngle", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = 180
obj.ThePropertyName # returns 180.0 deg
obj.ThePropertyName.Value # returns 180.0
```

## App::PropertyArea

Une propriété {{TODO}}area. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyArea", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyBool

Une propriété booléenne. Elle peut contenir `True` et `False`. Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyBool", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = True
obj.ThePropertyName = False
obj.ThePropertyName # returns False
```

## App::PropertyBoolList

Une propriété contenant une liste de booléens. Elle peut contenir une liste Python de booléens, par exemple `[True, False, True]`. Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyBoolList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = [True, False, True]
obj.ThePropertyName    # returns [True, False, True]
obj.ThePropertyName[1] # returns False
```

## App::PropertyColor

Une propriété de couleur. Elle peut contenir un tuple de quatre valeurs `float`. Chaque élément peut prendre des valeurs comprises entre 0.0 et 1.0. Vous pouvez définir les valeurs rouge, verte et bleue. Vous pouvez également définir la transparence des étapes. Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyColor", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = (0.0, 1.0, 0.5, 0.8) # (Red, Green, Blue, Transparency)
obj.ThePropertyName # returns (0.0, 1.0, 0.5, 0.8)
```

## App::PropertyColorList

Une propriété {{TODO}}colorList. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyColorList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyCurrentDensity


{{Version/fr|0.21}}

## App::PropertyDensity

## App::PropertyDirection

Identique à [App::PropertyVectorDistance](#App:_PropertyVectorDistance.md).

## App::PropertyDissipationRate


{{Version/fr|0.21}}

## App::PropertyDistance

Une propriété de distance. Elle peut contenir une valeur `distance` positive, négative ou nulle. Utilisez le paramètre \"Value\" de la propriété pour obtenir la valeur sous forme de nombre flottant. La valeur est toujours en mm, mais dans l\'[éditeur de propriétés](Property_editor/fr.md), elle est présentée avec les unités des préférences. Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).

[App::PropertyLength](#App:_PropertyLength.md) est une propriété similaire qui ne peut pas contenir de valeur négative.


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyDistance", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = 500
obj.ThePropertyName # returns "500.0 mm"
obj.ThePropertyName.Value # returns 500.0
```

## App::PropertyDynamicViscosity


{{Version/fr|0.21}}

## App::PropertyElectricalCapacitance


{{Version/fr|0.21}}

## App::PropertyElectricalConductance


{{Version/fr|0.21}}

## App::PropertyElectricalConductivity


{{Version/fr|0.21}}

## App::PropertyElectricalInductance


{{Version/fr|0.21}}

## App::PropertyElectricalResistance


{{Version/fr|0.21}}

## App::PropertyElectricCharge


{{Version/fr|0.21}}

## App::PropertyElectricCurrent


{{Version/fr|0.21}}

## App::PropertyElectricPotential

## App::PropertyEnumeration

Une propriété de type énumération. Les éléments autorisés sont définis en donnant à la propriété la valeur d\'une liste. Ensuite, elle peut contenir des éléments de la liste donnée. La liste des éléments autorisés peut être modifiée en donnant à nouveau à la propriété la valeur d\'une liste. Pour plus de détails, voir la section sur [Création d\'un objet FeaturePython et ajout d\'une propriété à celui-ci](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyEnumeration", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = ["Foo", "Bar", "Baz"]  # set allowed items
obj.ThePropertyName = "Foo"                  # choose single item
obj.ThePropertyName = ["Foo", "Bar", "Quux"] # change allowed items
obj.ThePropertyName = "Quux"                 # choose single item
obj.ThePropertyName # returns "Quux"
```


{{Version/fr|1.0}}

: l\'argument {{Incode|enum_vals}} de la fonction {{Incode|addProperty}} peut également être utilisé pour définir les cas d\'énumération. Voir [au-dessus](#Créer_un_objet_FeaturePython_et_lui_ajouter_une_propriété.md).


{{Version/fr|0.20}}

: il est possible de regrouper des énumérations affichées dans l\'interface graphique à l\'aide d\'une interface de sous-menu. Pour grouper, utilisez le caractère `<nowiki>|</nowiki>` comme séparateur, par exemple :


```python
obj.ThePropertyName = [
    "Group 1 <nowiki>|</nowiki> Item A", 
    "Group 1 <nowiki>|</nowiki> Item B", 
    "Group 2 <nowiki>|</nowiki> Another item", 
    "Group 2 <nowiki>|</nowiki> Last item"
] # set allowed items
obj.ThePropertyName = "Group 1 <nowiki>|</nowiki> Item A" # choose single item
```

L\'interface graphique affichera ceci comme une structure de menu :

-   Groupe 1
    -   Elément A
    -   Elément B
-   Groupe 2
    -   Autre élément
    -   Dernier élément

## App::PropertyExpressionEngine

Une propriété {{TODO}}expressionEngine. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyExpressionEngine", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyFile

Une propriété de nom de fichier. Elle peut contenir une chaîne de caractères indiquant le chemin d\'accès à un nom de fichier {{TODO}} :(autorise-t-elle les chemins relatifs ou absolus ou les deux ?). Pour plus de détails, voir la section sur [Création d\'un objet FeaturePython et ajout d\'une propriété à celui-ci](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyFile", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyFileIncluded

Une propriété de nom de fichier qui inclut également le fichier lui-même dans le document. Le fichier n\'est pas chargé en mémoire, il est copié de l\'archive du document dans le répertoire transitoire du document. Là, il est accessible en lecture. Vous pouvez obtenir le chemin d\'accès transitoire par {{Incode|getDocTransientPath()}}. Comme valeur, la propriété accepte une chaîne contenant le chemin d\'accès au fichier d\'origine. La propriété renvoie le chemin du fichier temporaire dans le répertoire transitoire. Pour plus de détails, voir cet [exemple de l\'atelier Arch](https://github.com/FreeCAD/FreeCAD/blob/adfdbf7cd76fe78c7f818623e019454337ed1bcd/src/Mod/Arch/ArchBuildingPart.py#L595-L597).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyFileIncluded", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = "D:/file.txt"
obj.ThePropertyName # returns the path to the temporary file
```

## App::PropertyFloat

Une propriété de flottant. Elle peut contenir une valeur `float`. Pour plus de détails, voir la section sur [Création d\'un objet FeaturePython et ajout d\'une propriété à celui-ci](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyFloat", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = 15.7
obj.ThePropertyName # returns 15.7
```

## App::PropertyFloatConstraint

Une propriété de contrainte flottante. Elle peut contenir une valeur `float`. En utilisant cette propriété, vous pouvez définir les valeurs de début et de fin. Vous pouvez également définir un intervalle de pas. Pour plus de détails, voir la section sur [Création d\'un objet FeaturePython et ajout d\'une propriété à celui-ci](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyFloatConstraint", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = (50.0, 0.0, 100.0, 1.0) # (Default, Start, Finish, Step)
obj.ThePropertyName # returns 50.0
```

## App::PropertyFloatList

Une propriété de liste de valeurs flottantes. Elle peut contenir une liste de valeurs `float`. Pour plus de détails, voir la section sur [Création d\'un objet FeaturePython et ajout d\'une propriété à celui-ci](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyFloatList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = [12.7, 5.8, 28.6, 17.22] # It can also be an empty list.
obj.ThePropertyName # returns [12.7, 5.8, 28.6, 17.22]
```

## App::PropertyFont

Une propriété {{TODO}}font. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyFont", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyForce

Une propriété {{TODO}}force. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyForce", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyFrequency

Une propriété {{TODO}}frequency. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyFrequency", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyHeatFlux


{{Version/fr|0.21}}

## App::PropertyInteger

Une propriété entière. Elle peut contenir une valeur entière comprise entre -2147483646 et 2147483647 inclus. Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Créer_un_objet_FeaturePython_et_lui_ajouter_une_propriété.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyInteger", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = 25
obj.ThePropertyName # returns 25
```

## App::PropertyIntegerConstraint

Une propriété de contrainte entière. Avec cette propriété, vous pouvez définir une valeur par défaut, une valeur minimale, une valeur maximale et une taille de pas. Toutes les valeurs doivent être des entiers et peuvent être comprises entre -2147483646 et 2147483647 inclus. Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Créer_un_objet_FeaturePython_et_lui_ajouter_une_propriété.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyIntegerConstraint", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = (50, 0, 100, 1) # (Default, Minimum, Maximum, Step size)
obj.ThePropertyName # returns 50
```

## App::PropertyIntegerList

Une propriété de liste d\'entiers. Elle peut contenir une liste de valeurs `integer`. Pour plus de détails, voir la section sur [Création d\'un objet FeaturePython et ajout d\'une propriété à celui-ci](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyIntegerList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = [12, 5, 28, 17] # It can also be an empty list.
obj.ThePropertyName # returns [12, 5, 28, 17]
```

## App::PropertyIntegerSet

Une propriété {{TODO}}integerSet. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyIntegerSet", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyInverseArea


{{Version/fr|0.21}}

## App::PropertyInverseLength


{{Version/fr|0.21}}

## App::PropertyInverseVolume


{{Version/fr|0.21}}

## App::PropertyKinematicViscosity


{{Version/fr|0.21}}

## App::PropertyLength

Une propriété de longueur. Elle peut contenir une valeur `length` positive ou nulle. Utilisez le paramètre \"Value\" de la propriété pour obtenir la valeur sous forme de nombre flottant. La valeur est toujours en mm mais dans l\'[éditeur de propriétés](Property_editor/fr.md), elle est présentée avec les unités des préférences. Pour plus de détails, voir la section [Création d\'un objet FeaturePython et ajout d\'une propriété à celui-ci](#Creating.md).

[App::PropertyDistance](#App:_PropertyDistance.md) est une propriété similaire qui peut aussi contenir une valeur négative.


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLength", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = 500
obj.ThePropertyName # returns "500.0 mm"
obj.ThePropertyName.Value # returns 500.0
```

## App::PropertyLink

Une propriété de lien. Elle peut contenir un lien vers un objet. Lorsque vous appelez cette propriété, elle renvoie l\'objet lié. Pour plus de détails, voir la section sur [Création d\'un objet FeaturePython et ajout d\'une propriété à celui-ci](#Creating.md).


```python
link_obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "LinkObjectName")
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLink", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = link_obj
obj.ThePropertyName # returns link_obj
```

## App::PropertyLinkChild

Une propriété {{TODO}}linkChild. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkChild", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkGlobal

Une propriété {{TODO}}linkGlobal. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkGlobal", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkHidden

Une propriété {{TODO}}linkHidden. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkHidden", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkList

Une propriété de liste de liens. Elle peut contenir une liste d\'objets liés. Pour plus de détails, voir la section sur [Création d\'un objet FeaturePython et ajout d\'une propriété à celui-ci](#Creating.md).


```python
link_obj0 = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "LinkObjectName0")
link_obj1 = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "LinkObjectName1")
link_obj2 = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "LinkObjectName2")

obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = [link_obj0, link_obj1, link_obj2]
obj.ThePropertyName # returns [link_obj0, link_obj1, link_obj2]
```

## App::PropertyLinkListChild

Une propriété {{TODO}}linkListChild. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkListChild", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkListGlobal

Une propriété {{TODO}}linkListGlobal. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkListGlobal", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkListHidden

Une propriété {{TODO}}linkListHidden. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkListHidden", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkSub

Un LinkSub est une liste de deux éléments : le premier est une référence à un [objet de document](App_DocumentObject/fr.md), le second une chaîne de caractères ou une liste de chaînes de caractères indiquant le(s) nom(s) interne(s) du (des) sous-élément(s). Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
doc = FreeCAD.ActiveDocument
box = doc.addObject("Part::Box", "Box")

obj = doc.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkSub", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = [box, ["Vertex1", "Vertex2"]]

doc.recompute()
```

## App::PropertyLinkSubChild

Une propriété {{TODO}}linkSubChild. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkSubChild", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkSubGlobal

Une propriété {{TODO}}linkSubGlobal. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkSubGlobal", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkSubHidden

Une propriété {{TODO}}linkSubHidden. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkSubHidden", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkSubList

Une LinkSubList est une liste de tuples. Chaque tuple contient deux éléments : le premier est une référence à un [objet de document](App_DocumentObject/fr.md), le second une chaîne de caractères ou une liste de chaînes de caractères indiquant le(s) nom(s) interne(s) du (des) sous-élément(s). Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
doc = FreeCAD.ActiveDocument
box = doc.addObject("Part::Box", "Box")
cyl = doc.addObject("Part::Cylinder", "Cylinder")

obj = doc.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkSubList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = [(box, ["Vertex1", "Vertex2"]), (cyl, "Edge1")]

doc.recompute()
```

## App::PropertyLinkSubListChild

Une propriété {{TODO}}linkSubListChild. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkSubListChild", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkSubListGlobal

Une propriété {{TODO}}linkSubListGlobal. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkSubListGlobal", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLinkSubListHidden

Une propriété {{TODO}}linkSubListHidden. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyLinkSubListHidden", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyLuminousIntensity


{{Version/fr|0.21}}

## App::PropertyMagneticFieldStrength


{{Version/fr|0.21}}

## App::PropertyMagneticFlux


{{Version/fr|0.21}}

## App::PropertyMagneticFluxDensity


{{Version/fr|0.21}}

## App::PropertyMagnetization


{{Version/fr|0.21}}

## App::PropertyMap

Une propriété {{TODO}}map. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyMap", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyMass


{{Version/fr|0.21}}

## App::PropertyMaterial

Une propriété de matériau. Elle peut contenir un objet matériau de FreeCAD. Pour plus de détails, voir la section sur [Création d\'un objet FeaturePython et ajout d\'une propriété à celui-ci](#Creating.md).


```python
import FreeCAD
material=FreeCAD.Material()

obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyMaterial", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = material
obj.ThePropertyName # returns material
```

## App::PropertyMaterialList

Une propriété de liste de matériaux. Elle peut contenir une liste de matériaux. Pour plus de détails, voir la section sur [Création d\'un objet FeaturePython et ajout d\'une propriété à celui-ci](#Creating.md).


```python
import FreeCAD
material0 = FreeCAD.Material()
material1 = FreeCAD.Material()
material2 = FreeCAD.Material()

obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython","InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyMaterialList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = [material0, material1, material2] # It can also be an empty list.
obj.ThePropertyName # returns [material0, material1, material2]
```

## App::PropertyMatrix

Une propriété {{TODO}}matrix. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyMatrix", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyPath

Une propriété de chemin. Elle peut contenir une chaîne de caractères représentant un chemin d\'accès à un dossier {{TODO}} :(autorise-t-elle également les chemins d\'accès aux fichiers ? autorise-t-elle les chemins relatifs ou absolus, ou les deux ?) Pour plus de détails, voir la section sur [Création d\'un objet FeaturePython et ajout d\'une propriété à celui-ci](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyPath", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyPercent

Une propriété {{TODO}}percent. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyPercent", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyPersistentObject

Une propriété {{TODO}}persistentObject. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyPersistentObject", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyPlacement

Une propriété de placement. Elle peut contenir un objet `placement`. Pour plus de détails, voir la section sur [Création d\'un objet FeaturePython et ajout d\'une propriété à celui-ci](#Creating.md).


```python
import FreeCAD
placement = FreeCAD.Placement()
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython","InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyPlacement", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = placement
obj.ThePropertyName # returns placement
```

## App::PropertyPlacementLink

Une propriété {{TODO}}placementLink. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyPlacementLink", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyPlacementList

Une propriété de liste de placement. Elle peut contenir une liste de `placements`. Pour plus de détails, voir la section sur [Création d\'un objet FeaturePython et ajout d\'une propriété à celui-ci](#Creating.md).


```python
import FreeCAD
placement0 = FreeCAD.Placement()
placement1 = FreeCAD.Placement()
placement2 = FreeCAD.Placement()

obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython","InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyPlacementList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = [placement0, placement1, placement2]
obj.ThePropertyName # returns [placement0, placement1, placement2]
```

## App::PropertyPosition

Identique à [App::PropertyVectorDistance](#App:_PropertyVectorDistance.md).

## App::PropertyPower


{{Version/fr|0.21}}

## App::PropertyPrecision

Une propriété {{TODO}}precision. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyPrecision", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyPressure

Une propriété {{TODO}}pressure. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyPressure", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyPythonObject

Une propriété {{TODO}}pythonObject. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyPythonObject", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyQuantity

Une propriété {{TODO}}quantity. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyQuantity", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyQuantityConstraint

Une propriété {{TODO}}quantityConstraint. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyQuantityConstraint", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyRotation

## App::PropertyShearModulus


{{Version/fr|0.21}}

## App::PropertySpecificEnergy


{{Version/fr|0.21}}

## App::PropertySpecificHeat


{{Version/fr|0.21}}

## App::PropertySpeed

Une propriété {{TODO}}speed. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertySpeed", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyStiffness

## App::PropertyStress


{{Version/fr|0.21}}

## App::PropertyString

Une propriété {{TODO}}string. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyString", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyStringList

Une propriété {{TODO}}stringList. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyStringList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyTemperature


{{Version/fr|0.21}}

## App::PropertyThermalConductivity


{{Version/fr|0.21}}

## App::PropertyThermalExpansionCoefficient


{{Version/fr|0.21}}

## App::PropertyThermalTransferCoefficient


{{Version/fr|0.21}}

## App::PropertyTime


{{Version/fr|0.21}}

## App::PropertyUltimateTensileStrength


{{Version/fr|0.21}}

## App::PropertyUUID

Une propriété {{TODO}}uUID. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyUUID", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyVacuumPermittivity

Une propriété {{TODO}}vacuumPermittivity. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyVacuumPermittivity", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyVector

Une propriété vectorielle. Elle peut contenir un objet `vector` de FreeCAD. La valeur peut être définie en fournissant un vecteur ou un tuple. Pour plus de détails, voir la section [Création d\'un objet FeaturePython et ajout d\'une propriété à celui-ci](#Creating.md).


```python
import FreeCAD
vector = FreeCAD.Vector(0, -2, 5)

obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyVector", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = vector
obj.ThePropertyName # returns Vector(0, -2, 5)
obj.ThePropertyName = (1, 2, 3)
obj.ThePropertyName # returns Vector(1, 2, 3)
obj.ThePropertyName.x # returns 1.0
obj.ThePropertyName.y # returns 2.0
obj.ThePropertyName.z # returns 3.0
obj.ThePropertyName.z = 6
obj.ThePropertyName # returns Vector(1, 2, 6)
obj.ThePropertyName.Length # returns 6.4031242374328485
obj.ThePropertyName.Length = 2 * obj.ThePropertyName.Length
obj.ThePropertyName # Vector (2.0, 4.0, 12.0)
```

## App::PropertyVectorDistance

Une propriété vectorielle qui est presque identique à [App::PropertyVector](#App:_PropertyVector.md). La seule différence est que dans l\'[éditeur de propriétés](Property_editor/fr.md), les paramètres \"x\", \"y\" et \"z\" de cette propriété sont présentés avec des unités des préférences. Mais en interne, toutes les valeurs sont sans unité et donc en mm.


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyVectorDistance", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = (1, 2, 3)
obj.ThePropertyName # returns Vector(1, 2, 3)
obj.ThePropertyName.x # returns 1
```

## App::PropertyVectorList

Une propriété de liste de vecteurs. Elle peut contenir une liste de `vectors`. La valeur peut être définie en fournissant une liste de vecteurs et/ou de tuples. Pour plus de détails, voir la section [Création d\'un objet FeaturePython et ajout d\'une propriété à celui-ci](#Creating.md).


```python
import FreeCAD
v0 = FreeCAD.Vector(0, 10, 0)
v1 = FreeCAD.Vector(0, 10, 0)
v2 = FreeCAD.Vector(30, -10, 0)
v3 = FreeCAD.Vector(0, -10, 0)

obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython","InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyVectorList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = [v0, v1, v2, v3]
obj.ThePropertyName # returns [Vector(0, 10, 0), Vector(0, 10, 0), Vector(30, -10, 0), Vector(0, -10, 0)]
obj.ThePropertyName = [v0, (1, 2, 3), v2, (4, 5, 6)]
obj.ThePropertyName # returns [Vector (0, 10, 0), Vector (1, 2, 3), Vector (30, -10, 0), Vector (4, 5, 6)]
```


{{Version/fr|0.21}}

## App::PropertyVelocity


{{Version/fr|0.21}}

## App::PropertyVolume

Une propriété {{TODO}}volume. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyVolume", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyVolumeFlowRate


{{Version/fr|0.21}}

## App::PropertyVolumetricThermalExpansionCoefficient


{{Version/fr|0.21}}

## App::PropertyWork


{{Version/fr|0.21}}

## App::PropertyXLink

Une propriété {{TODO}}xLink. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyXLink", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyXLinkList

Une propriété {{TODO}}xLinkList. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyXLinkList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyXLinkSub

Une propriété {{TODO}}xLinkSub. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyXLinkSub", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyXLinkSubList

Une propriété {{TODO}}xLinkSubList. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("App::PropertyXLinkSubList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## App::PropertyYieldStrength


{{Version/fr|0.21}}

## App::PropertyYoungsModulus


{{Version/fr|0.21}}

## Mesh::PropertyCurvatureList

Une propriété {{TODO}}curvatureList. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Mesh::PropertyCurvatureList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Mesh::PropertyMeshKernel

Une propriété de noyau de maillage. Elle peut contenir un objet `mesh`. Pour plus de détails, voir la section sur [Création d\'un objet FeaturePython et ajout d\'une propriété à celui-ci](#Creating.md).


```python
import Mesh
mesh = Mesh.Mesh()

obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Mesh::PropertyMeshKernel", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = mesh
obj.ThePropertyName # returns mesh
```

## Mesh::PropertyNormalList

Une propriété {{TODO}}normalList. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Mesh::PropertyNormalList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Part::PropertyFilletEdges

Une propriété {{TODO}}filletEdges. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Part::PropertyFilletEdges", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Part::PropertyGeometryList

Une propriété {{TODO}}geometryList. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Part::PropertyGeometryList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Part::PropertyPartShape

Une propriété de forme de pièce. Elle peut contenir un objet `shape`. Pour plus de détails, voir la section sur [Création d\'un objet FeaturePython et ajout d\'une propriété à celui-ci](#Creating.md).


```python
import Part
part = Part.Shape()

obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Part::PropertyPartShape", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = part
obj.ThePropertyName # returns part
```

## Part::PropertyShapeHistory

Une propriété {{TODO}}shapeHistory. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Part::PropertyShapeHistory", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Path::PropertyPath

Une propriété {{TODO}}path. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Path::PropertyPath", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Path::PropertyTool

Une propriété {{TODO}}tool. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Path::PropertyTool", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Path::PropertyTooltable

Une propriété {{TODO}}tooltable. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Path::PropertyTooltable", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Sketcher::PropertyConstraintList

Une propriété {{TODO}}constraintList. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Sketcher::PropertyConstraintList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Spreadsheet::PropertyColumnWidths

Une propriété {{TODO}}columnWidths. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Spreadsheet::PropertyColumnWidths", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Spreadsheet::PropertyRowHeights

Une propriété {{TODO}}rowHeights. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Spreadsheet::PropertyRowHeights", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Spreadsheet::PropertySheet

Une propriété {{TODO}}sheet. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section sur [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Spreadsheet::PropertySheet", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## Spreadsheet::PropertySpreadsheetQuantity

Une propriété {{TODO}}spreadsheetQuantity. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("Spreadsheet::PropertySpreadsheetQuantity", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## TechDraw::PropertyCenterLineList

Une propriété {{TODO}}centerLineList. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("TechDraw::PropertyCenterLineList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## TechDraw::PropertyCosmeticEdgeList

Une propriété {{TODO}}cosmeticEdgeList. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("TechDraw::PropertyCosmeticEdgeList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## TechDraw::PropertyCosmeticVertexList

Une propriété {{TODO}}cosmeticVertexList. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("TechDraw::PropertyCosmeticVertexList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}

## TechDraw::PropertyGeomFormatList

Une propriété {{TODO}}geomFormatList. Elle peut contenir des {{TODO}} \"types et/ou valeurs autorisés\". Pour plus de détails, voir la section [Créer un objet FeaturePython et lui ajouter une propriété](#Creating.md).


```python
obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "InternalObjectName")
obj.Label = "User-friendly label"
obj.addProperty("TechDraw::PropertyGeomFormatList", "ThePropertyName", "Subsection", "Description for tooltip")
obj.ThePropertyName = {{TODO```"example value for setter"
obj.ThePropertyName # returns {{TODO}}"example value for getter"
}}



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Developer Documentation](Category_Developer Documentation.md) > FeaturePython Custom Properties/fr
