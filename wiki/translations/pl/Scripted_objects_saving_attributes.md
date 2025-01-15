# Scripted objects saving attributes/pl
## Wprowadzenie

[Obiekty tworzone skryptami](Scripted_objects/pl.md) są odbudowywane przy każdym otwarciu dokumentu [FCStd](File_Format_FCStd/pl.md). W tym celu dokument przechowuje referencję do modułu i klasy Python, które zostały użyte do stworzenia obiektu, wraz z jego właściwościami.

Atrybuty klasy użytej do utworzenia obiektu mogą być również zapisywane, czyli \"serializowane\". Może to być dalej kontrolowane przez metody klasy `dumps` i `loads`.



## Zapisywanie wszystkich atrybutów 

Domyślnie, atrybuty zapisane w klasie obiektu są atrybutami ze słownika `__dict__` klasy.


```python
# various_states.py
class VariousStates:
    def __init__(self, obj):
        obj.addProperty("App::PropertyLength", "Length")
        obj.addProperty("App::PropertyArea", "Area")
        obj.Length = 15
        obj.Area = 300
        obj.Proxy = self

        Type = dict()
        Type["Version"] = "Custom"
        Type["Release"] = "production"
        self.Type = Type
        self.Type = "Custom"
        self.ver = "0.18"
        self.color = (0, 0, 1)
        self.width = 2.5

    def execute(self, obj):
        pass
```

Obiekt może zostać utworzony przy użyciu tej klasy i zapisany do pliku **my_document.FCstd**. Jeśli żaden konkretny [dostawca widoku](Viewprovider/pl.md) nie jest przypisany do nowego obiektu, jego klasa proxy jest po prostu ustawiana na wartość inną niż `None`, w tym przypadku na `1`. 
```python
import FreeCAD as App
import various_states

doc = App.newDocument()
doc.FileName = "my_document.FCStd"

obj = doc.addObject("Part::FeaturePython", "Custom")
various_states.VariousStates(obj)

if App.GuiUp:
    obj.ViewObject.Proxy = 1

doc.recompute()
doc.save()
```

Po ponownym otwarciu pliku możemy sprawdzić słownik klasy obiektu. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.Proxy)
<various_states.VariousStates object at 0x7f0a899bde10>
>>> print(obj.Proxy.__dict__)
{'Type': {'Version': 'Custom', 'Release': 'production'}, 'ver': '0.18', 'color': [0, 0, 1], 'width': 2.5}
```

Widzimy, że wszystkie atrybuty zaczynające się od `self` w klasie zostały zapisane. Mogą one być różnych typów, w tym string, list, float i dictionary. Oryginalna krotka dla `self.color` została przekonwertowana na listę, ale poza tym wszystkie atrybuty zostały załadowane tak samo.



## Zapisywanie określonych atrybutów 

Możemy zdefiniować klasę podobną do pierwszej, która implementuje określone atrybuty do zapisania. 
```python
# various_states.py
class CustomStates:
    def __init__(self, obj):
        obj.addProperty("App::PropertyLength", "Length")
        obj.addProperty("App::PropertyArea", "Area")
        obj.Length = 15
        obj.Area = 300
        obj.Proxy = self

        Type = dict()
        Type["Version"] = "Custom"
        Type["Release"] = "production"
        self.Type = Type
        self.ver = "0.18"
        self.color = (0, 0, 1)
        self.width = 2.5

    def execute(self, obj):
        pass

    def dumps(self):
        return self.color, self.width

    def loads(self, state):
        self.color = state[0]
        self.width = state[1]
```

Wartością zwrotną `dumps` jest obiekt, który zostanie zserializowany. Może to być pojedyncza wartość lub krotka wartości. Po przywróceniu obiektu klasa wywołuje metodę `loads`, przekazując zmienną `state` z serializowaną zawartością. W tym przypadku `state` jest krotką, która jest rozpakowywana do odpowiednich zmiennych, aby zrekonstruować \"stan\", który istniał pierwotnie. 
```python
state = (self.color, self.width)
state = ((0, 0, 1), 2.5)
```

Możemy utworzyć obiekt z tą klasą i zapisać dokument, tak jak w poprzednim przykładzie. Po ponownym otwarciu pliku możemy sprawdzić słownik klasy obiektu. 
```python
>>> obj2 = App.ActiveDocument.Custom2
>>> print(obj2.Proxy)
<various_states.CustomStates object at 0x7fb399496630>
>>> print(obj2.Proxy.__dict__)
{'color': [0, 0, 1], 'width': 2.5}
```

Oryginalna krotka dla `self.color` została przekonwertowana na listę, ale poza tym informacje zostały odzyskane prawidłowo. Zamiast przywracania wszystkich atrybutów, jak w poprzednim przypadku, przywrócone zostały tylko atrybuty określone w `dumps` i `loads`.



## Użycie



### Identyfikacja typu 

Zwykle [obiekty tworzone skryptami](Scripted_objects/pl.md) powinny używać [właściwości](Property/pl.md) do przechowywania informacji, ponieważ są one automatycznie przywracane po otwarciu dokumentu.

Czasami jednak klasa przechowuje wewnętrzne informacje, które nie są przeznaczone do modyfikacji, ale które są pomocne w inspekcji.

Na przykład, większość obiektów środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md) ustawia atrybut `Type`, który może być użyty do określenia typu używanego obiektu.


```python
class DraftObject:
    def __init__(self, obj, _type):
        self.Type = _type

    def dumps(self):
        return self.Type

    def loads(self, state):
        if state:
            self.Type = state
```

Wszystkie obiekty mają właściwość `TypeId`, ale dla [obiektów tworzonych skryptami](scripted_objects.md) ta właściwość nie jest użyteczna, ponieważ zawsze odnosi się do nadrzędnej klasy C++, na przykład [`Part::Part2DObjectPython`](Part_Part2DObject/pl.md) lub [`Part::FeaturePython`](Part_Feature/pl.md). Dlatego posiadanie tego dodatkowego atrybutu `Proxy.Type` w klasie jest przydatne do traktowania każdego obiektu w określony sposób.



### Migracja obiektu 

Informacje o wersji mogą być przechowywane wewnątrz klasy w celu weryfikacji pochodzenia obiektu.


```python
class CustomObject:
    def __init__(self, obj, _type):
        self.Type = _type
        self.version = "0.18"

    def dumps(self):
        return self.Type, self.version

    def loads(self, state):
        if state:
            self.Type = state[0]
            self.version = state[1]
```

Jeśli struktura klasy ulegnie zmianie, tzn. zmienią się jej właściwości lub metody, zostanie zmieniona ich nazwa lub zostaną usunięte, możemy przetestować atrybut version w celu migracji starszego obiektu do nowego zestawu właściwości lub do nowej klasy. Można to zrobić implementując metodę `onDocumentRestored`, jak wyjaśniono na stronie [Obiekty tworzone skryptami, migracja](Scripted_objects_migration/pl.md).


```python
class CustomObject:
    def onDocumentRestored(self, obj):
        if hasattr(obj.Proxy, "version") and obj.Proxy.version:
            if obj.Proxy.version == "0.18":
                self.migrate_from_018(obj)

    def migrate_from_018(self, obj):
        ...
```



## Odnośniki internetowe 

-   [Obiekty tworzone skryptami](Scripted_objects.md)
-   [Migracja obiektów tworzonych skryptami](Scripted_objects_migration.md)
-   [Dyskusja na forum FreeCAD: Serializacja obiektów tworzonych skryptami: json czy pickle?](https://forum.freecadweb.org/viewtopic.php?f=10&t=49120)

-   [obj.Proxy.Type jest typu dict, a nie string](https://forum.freecadweb.org/viewtopic.php?f=18&t=44009), wyjaśnienie `dumps` i `loads` na forum.
-   [Moduł Pickle](https://docs.python.org/3/library/pickle.html#object.__getstate__) w dokumentacji Python.



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Scripted objects saving attributes/pl
