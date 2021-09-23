# Property/fr


## Introduction

Une [propriété](Property/fr.md) est une information, telle qu\'un nombre ou une chaîne de texte, attachée à un document FreeCAD ou à un objet d\'un document. Les propriétés peuvent être visualisées et modifiées avec l\'[éditeur de propriétés](Property_editor/fr.md).

Les propriétés jouent un rôle très important dans FreeCAD. Comme les objets dans FreeCAD sont \"paramétriques\", cela signifie que leur comportement est défini par leurs propriétés et par la manière dont ces propriétés sont utilisées comme entrée pour leurs méthodes de classe. Voir aussi [PropertyLink:\_InList\_and\_OutList](PropertyLink:_InList_and_OutList/fr.md)

## Tous les types de propriétés 

Les [Objets créés par script](scripted_objects/fr.md) personnalisés dans FreeCAD peuvent avoir des propriétés des types suivants : 
```python
Bool
Float
FloatList
FloatConstraint
Angle
Distance
ExpressionEngine
Integer
IntegerConstraint
Percent
Enumeration
IntegerList
String
StringList
Length
Link
LinkList
LinkSubList
Matrix
Vector
VectorList
VectorDistance
Placement
PlacementLink
PythonObject
Color
ColorList
Material
Path
File
FileIncluded
PartShape
FilletContour
Circle
```

En interne, le nom de la propriété est préfixé par `App::Property`: 
```python
App::PropertyBool
App::PropertyFloat
App::PropertyFloatList
...
```

Rappelez-vous qu\'il s\'agit de propriétés **types**. Un même objet peut avoir plusieurs propriétés du même type, mais avec des noms différents.

par exemple:


```python
obj.addProperty("App::PropertyFloat", "Length")
obj.addProperty("App::PropertyFloat", "Width")
obj.addProperty("App::PropertyFloat", "Height")
```

Cela indique un objet avec trois propriétés de type \"Float\", nommées respectivement \"Length\", \"Width\" et \"Height\".

## Scrip


**See also:**

[FreeCAD scrip de base](FreeCAD_Scripting_Basics/fr.md)

Un [objet scripté](scripted_objects/fr.md) est créé en premier, puis les propriétés lui sont attribuées. 
```python
obj = App.ActiveDocument.addObject("Part::Feature", "CustomObject")

obj.addProperty("App::PropertyFloat", "Velocity", "Parameter", "Body speed")
obj.addProperty("App::PropertyBool", "VelocityEnabled", "Parameter", "Enable body speed")
```

En général, les propriétés **Data** sont affectées à l\'aide de la méthode `addProperty()` de l\'objet. D\'autre part, les propriétés **View** sont normalement fournies automatiquement par l\'objet parent à partir duquel l\'objet scripté est dérivé.

Par exemple:

-   Dériver de `App::FeaturePython` fournit uniquement 4 propriétés **View**: \"Display Mode\", \"On Top When Selected\", \"Show In Tree\" et \"Visibility\".
-   Dériver de `Part::Feature` fournit 17 propriétés **View**: les quatre précédentes, plus \"Angular Deflection\", \"Zone de sélection\", \"Deviation\", \"Draw Style\", \"Lighting\", \"Line Color\", \"Line Width\", \"Point Color\", \"Point Size\", \"Selectable\", \"Selection Style\", \"Shape Color\", et \"Transparency\".

Néanmoins, les propriétés **View** peuvent également être affectées à l\'aide de la méthode `addProperty()` de l\'objet fournisseur de vue. 
```python
obj.ViewObject.addProperty("App::PropertyBool", "SuperVisibility", "Base", "Make the object glow")
```

## Code source 

Dans le code source, les propriétés se trouvent dans divers fichiers {{FileName|src/App/Property*}} .

Ils sont importés et initialisés dans `[https://github.com/FreeCAD/FreeCAD/blob/9c27f1078e5ec516fe882aac1a27f5c6c6174554/src/App/Application.cpp#L1681-L1758 src/App/Application.cpp]`. {{Code|lang=cpp|code=
#include "Property.h"
#include "PropertyContainer.h"
#include "PropertyUnits.h"
#include "PropertyFile.h"
#include "PropertyLinks.h"
#include "PropertyPythonObject.h"
#include "PropertyExpressionEngine.h"
}}


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
