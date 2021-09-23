# Property/it
## Introduzione

Una [proprietà](Property/it.md) è una parte di informazione sotto forma di numero o di stringa di testo che viene allegata a un documento di FreeCAD oppure a un oggetto di un documento. Le proprietà pubbliche possono essere visualizzate e, se consentito, modificate nell\'[editore delle proprietà](Property_editor/it.md).


<div class="mw-translate-fuzzy">

In FreeCAD le proprietà svolgono un ruolo molto importante. Dato che gli oggetti in FreeCAD sono \"parametrici\", ciò significa che il loro comportamento è definito dalle loro proprietà e dal modo in cui queste proprietà vengono utilizzate come input per i loro metodi delle classi.


</div>

## Tutti i tipi di proprietà 

In FreeCAD gli oggetti [script personalizzati](scripted_objects/it.md) possono utilizzare uno qualsiasi dei tipi di proprietà definiti nel sistema di base: 
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

Internamente, il nome della proprietà ha il prefisso `App::Property`: 
```python
App::PropertyBool
App::PropertyFloat
App::PropertyFloatList
...
```

Ricordare che queste sono della proprietà **types**. Un singolo oggetto può avere molte proprietà dello stesso tipo, ma con nomi diversi.

Per esempio:


```python
obj.addProperty("App::PropertyFloat", "Length")
obj.addProperty("App::PropertyFloat", "Width")
obj.addProperty("App::PropertyFloat", "Height")
```

Ciò indica un oggetto con tre proprietà di tipo \"Float\", denominate rispettivamente \"Length\", \"Width\", e \"Height\".

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Prima viene creato un [oggetto script](scripted_objects/it.md), quindi gli vengono assegnate le proprietà. 
```python
obj = App.ActiveDocument.addObject("Part::Feature", "CustomObject")

obj.addProperty("App::PropertyFloat", "Velocity", "Parameter", "Body speed")
obj.addProperty("App::PropertyBool", "VelocityEnabled", "Parameter", "Enable body speed")
```

In generale, le proprietà **Data** sono assegnate usando il metodo `addProperty()` dell\'oggetto. D\'altra parte, le proprietà **View** sono normalmente fornite automaticamente dall\'oggetto genitore da cui deriva l\'oggetto script.

Per esempio:

-   Derivato da `App::FeaturePython` fornisce solo 4 proprietà **View**: \"Display Mode\", \"On Top When Selected\", \"Show In Tree\", e \"Visibility\".
-   Derivato da `Part::Feature` fornisce 17 proprietà **View**: le quattro precedenti più \"Angular Deflection\", \"Bounding Box\", \"Deviation\", \"Draw Style\", \"Lighting\", \"Line Color\", \"Line Width\", \"Point Color\", \"Point Size\", \"Selectable\", \"Selection Style\", \"Shape Color\", e \"Transparency\".

Tuttavia, le proprietà **View** possono anche essere assegnate usando il metodo `addProperty()` dell\'oggetto fornitore della vista. 
```python
obj.ViewObject.addProperty("App::PropertyBool", "SuperVisibility", "Base", "Make the object glow")
```

## Source code 

In the source code, properties are located in various {{FileName|src/App/Property*}} files.

They are imported and initialized in `[https://github.com/FreeCAD/FreeCAD/blob/9c27f1078e5ec516fe882aac1a27f5c6c6174554/src/App/Application.cpp#L1681-L1758 src/App/Application.cpp]`. {{Code|lang=cpp|code=
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

---
[documentation index](../README.md) > [Developer Documentation](Category:Developer Documentation.md) > Property/it
