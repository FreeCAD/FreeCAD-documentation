

## Wprowadzenie

[Właściwości](Property.md) to informacje takie jak liczba lub łańcuch tekstowy, który jest dołączony do dokumentu FreeCAD, lub obiektu w dokumencie. Właściwości ogólnodostępne można przeglądać i modyfikować w [Edytorze właściwości](Property_editor.md).

Właściwości odgrywają bardzo ważną rolę w FreeCAD. Ponieważ obiekty w FreeCAD są **parametryczne**, oznacza to, że ich zachowanie jest definiowane przez ich właściwości, i jak te właściwości są wykorzystywane jako dane wejściowe dla ich metod klasowych. Zobacz również [wskaźnik właściwości:\_InList\_ oraz\_OutList](PropertyLink:_InList_and_OutList/pl.md)

## Wszystkie rodzaje właściwości 

Niestandardowe [obiekty skryptowe](scripted_objects.md) mogą używać dowolnych typów właściwości zdefiniowanych w systemie bazowym: 
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

Wewnętrzne, nazwa właściwości jest poprzedzona przez `App::Property`: 
```python
App::PropertyBool
App::PropertyFloat
App::PropertyFloatList
...
```

Pamiętajcie, że to są właściwości **typów**. Pojedynczy obiekt może mieć wiele właściwości tego samego typu, ale o różnych nazwach.

Dla przykładu:


```python
obj.addProperty("App::PropertyFloat", "Length")
obj.addProperty("App::PropertyFloat", "Width")
obj.addProperty("App::PropertyFloat", "Height")
```

Wskazuje to obiekt o trzech właściwościach typu **Float**, nazwanych odpowiednio Długość, Szerokość i Wysokość.

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics.md).

[Obiekt skryptowy](scripted_objects.md) jest tworzony najpierw, a następnie przypisywane są mu właściwości. 
```python
obj = App.ActiveDocument.addObject("Part::Feature", "CustomObject")

obj.addProperty("App::PropertyFloat", "Velocity", "Parameter", "Body speed")
obj.addProperty("App::PropertyBool", "VelocityEnabled", "Parameter", "Enable body speed")
```

Ogólnie rzecz biorąc, właściwości **Dane** są przypisywane za pomocą metody obiektu `addProperty()`. Z drugiej strony, właściwości **Widok** są zazwyczaj dostarczane automatycznie przez obiekt nadrzędny, z którego pochodzi skrypt.

Na przykład:

-   Pochodzący z `App::FeaturePython` dostarcza tylko 4 właściwości **widoku**: Tryb wyświetlania, Na górze po wybraniu, Pokaż w drzewie, i Widoczność.
-   Pochodzący z `Part::Feature` dostarcza 17 właściwości **widoku**: poprzednie cztery, plus Odchylenie kątowe, Ramka wiążąca, Odchylenie, Styl rysowania, Oświetlenie, Kolor linii, Szerokość linii, Kolor punktu, Rozmiar punktu, Wybór, Styl wyboru, Kolor kształtu i Przezroczystość.

Niemniej jednak, właściwości **widoku** można również przypisać za pomocą metody obiektu dostawcy widoku `addProperty()`. 
```python
obj.ViewObject.addProperty("App::PropertyBool", "SuperVisibility", "Base", "Make the object glow")
```

## Kod źródłowy 

W kodzie źródłowym właściwości znajdują się w różnych plikach {{FileName|src/App/Property*}}.

Są one importowane i inicjowane w `[https://github.com/FreeCAD/FreeCAD/blob/9c27f1078e5ec516fe882aac1a27f5c6c6174554/src/App/Application.cpp#L1681-L1758 src/App/Application.cpp]`. {{Code|lang=cpp|code=
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

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
