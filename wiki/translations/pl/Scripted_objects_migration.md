# Scripted objects migration/pl
## Wprowadzenie

[Obiekty tworzone skryptami](Scripted_objects/pl.md) są odbudowywane przy każdym otwarciu dokumentu [FCStd](File_Format_FCStd/pl.md). W tym celu dokument przechowuje referencję do modułu i klasy Pythona, które zostały użyte do stworzenia obiektu, wraz z jego właściwościami.


{{Code|lang=xml|code=
<Document SchemaVersion="4" ProgramVersion="0.19R20959 (Git)" FileVersion="1">
    ...
    <Properties Count="15" TransientCount="3">
    ...
    </Properties>
    <Objects Count="1" Dependencies="1">
        <ObjectDeps Name="Custom" Count="0"/>
        <Object type="Part::FeaturePython" name="Custom" id="2715" Touched="1" />
    </Objects>
    <ObjectData Count="1">
        <Object name="Custom">
            <Properties Count="9" TransientCount="0">
                ...
                <Property name="Proxy" type="App::PropertyPythonObject" status="1">
                    <Python value="eyJUeXBlIjogIkN1c3RvbSJ9" encoded="yes" module="old_module" class="OldObject"/>
                </Property>
                ...
            </Properties>
        </Object>
    </ObjectData>
</Document>
}}

Szczególnie skup się na tej części: {{Code|lang=xml|code=
                ...
                <Property name="Proxy" type="App::PropertyPythonObject" status="1">
                    <Python value="eyJUeXBlIjogIkN1c3RvbSJ9" encoded="yes" module="old_module" class="OldObject"/>
                </Property>
                ...
}}

Jeśli wartość module= lub class= nie zostanie znaleziona w zainstalowanym systemie, obiekt nie zostanie poprawnie załadowany. Oznacza to, że po utworzeniu obiektu przy użyciu określonej klasy, moduł nie powinien być już przenoszony ani zmieniany, ponieważ jeśli to nastąpi, wcześniej zapisane obiekty ulegną uszkodzeniu.

Jednak ważnym powodem przeniesienia lub zmiany nazwy modułu lub klasy jest poprawa struktury i łatwości konserwacji oryginalnego kodu, na przykład podczas restrukturyzacji całego środowiska pracy. W takim przypadku istnieją różne strategie migracji starych obiektów do nowej klasy. Odbywa się to w celu zachowania kompatybilności wstecznej, gdy należy unikać jawnego zrywania funkcjonalności starych dokumentów.



## Stary i nowy obiekt 



### Stary obiekt 

Stary obiekt jest zdefiniowany w module, który znajduje się w katalogu głównym środowiska pracy. 
```python
# old_module.py
class OldObject:
    def __init__(self, obj):
        obj.addProperty("App::PropertyLength", "Length")
        obj.addProperty("App::PropertyArea", "Area")
        obj.Length = 15
        obj.Area = 300
        obj.Proxy = self
        self.Type = "Custom"

    def execute(self, obj):
        pass
```

Obiekt może zostać utworzony przy użyciu tej klasy i zapisany do pliku **my_document.FCstd**. Jeśli żaden konkretny [dostawca widoku](Viewprovider/pl.md) nie jest przypisany do nowego obiektu, jego klasa proxy jest po prostu ustawiana na wartość inną niż `None`, w tym przypadku na `1`. 
```python
import FreeCAD as App
import old_module

doc = App.newDocument()
doc.FileName = "my_document.FCStd"

obj = doc.addObject("Part::FeaturePython", "Custom")
old_module.OldObject(obj)

if App.GuiUp:
    obj.ViewObject.Proxy = 1

doc.recompute()
doc.save()
```

Sesja [konsoli Python](Python_console/pl.md) z pominiętymi podstawowymi właściwościami. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.PropertiesList)
['Area', ..., ..., ..., 'Length', ..., ..., ..., ...]
>>> print(obj.Proxy)
<old_module.OldObject object at 0x7efc3c51c390>
```



### Nowy obiekt 

Weźmy teraz pod uwagę, że środowisko pracy jest zrestrukturyzowane tak, że klasy nie znajdują się tylko w katalogu głównym, ale zamiast tego znajdują się wewnątrz katalogu **objects**. Złożone środowiska pracy, które mają wiele różnych typów obiektów, powinny być zorganizowane w katalogach zawierających obiekty, [dostawcy widoku](Viewprovider/pl.md), [polecenia Gui](Command/pl.md), interfejsy [panela zadań](Task_panel/pl.md) itd. 
```python
# objects/new_module.py
class NewObject:
    def __init__(self, obj):
        obj.addProperty("App::PropertyLength", "Length")
        obj.addProperty("App::PropertyArea", "GeneralArea")
        obj.addProperty("App::PropertyInteger", "Divisions")
        obj.Length = 30
        obj.GeneralArea = 600
        obj.Divisions = 4
        obj.Proxy = self
        self.Type = "Custom"

    def execute(self, obj):
        pass
```

Ta nowa klasa będzie odnosić się do tego samego typu obiektu, ale zarówno nazwa modułu, jak i nazwa klasy zostały zmienione. Co więcej, właściwości również uległy zmianie. Zmieniono nazwę jednej właściwości i dodano zupełnie nową właściwość.

Jeśli utworzymy nowy obiekt z tym nowym modułem, otrzymamy następującą sesję konsoli. 
```python
>>> obj2 = App.ActiveDocument.Custom2
>>> print(obj2.PropertiesList)
['Divisions', ..., 'GeneralArea', ..., ..., 'Length', ..., ..., ..., ...]
>>> print(obj2.Proxy)
<objects.new_module.NewObject object at 0x7efc1cf68c50>
```



## Metoda 1. Migracja poprzez przekierowanie klasy 

Zmigrujemy starszy obiekt poprzez przekierowanie starej klasy. Oryginalna klasa jest usuwana, a nazwa klasy jest po prostu przekierowywana, aby wskazywała na nową klasę.


```python
# old_module.py
import objects.new_module as new_module

OldObject = new_module.NewObject
```

Każdy dokument, który spróbuje załadować `old_module.OldObject` zostanie przekierowany do załadowania `objects.new_module.NewObject` zamiast niego.

Jeśli otworzymy dokument i sprawdzimy właściwości obiektu w [konsoli Python](Python_console/pl.md), zobaczymy, że starsze właściwości zostały zachowane, ale obiekt ma nową klasę Proxy. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.PropertiesList)
['Area', ..., ..., ..., 'Length', ..., ..., ..., ...]
>>> print(obj.Proxy)
<objects.new_module.NewObject object at 0x7f099700b2b0>
```

Jednak w tym przypadku nie widzimy nowych właściwości nowej klasy. Powodem jest po prostu to, że starszy obiekt nie miał tych właściwości. Kiedy `old_module.OldObject` został przekierowany do `objects.new_module.NewObject`, zmieniła się tylko klasa proxy, ale poprzednie informacje zostały zachowane.

Teraz, jeśli dokument zostanie zapisany i otwarty ponownie, będzie automatycznie szukał `objects.new_module.NewObject` i nie będzie już wymagał `old_module.OldObject`. Plik **old_module.py** może zostać trwale usunięty z systemu, o ile wszystkie starsze obiekty zostały zmigrowane do nowego modułu. Jeśli stary moduł zostanie usunięty, ale obiekt nie został zmigrowany, [widok raportu](Report_view/pl.md) wyświetli taki komunikat podczas otwierania dokumentu zawierającego taki obiekt.


{{Code|lang=bash|code=
<class 'ModuleNotFoundError'>: No module named 'old_module'
}}

Jeśli migracja wszystkich starszych obiektów nie jest realistycznie możliwa, na przykład dlatego, że stary moduł był używany w środowisku pracy przez wiele lat, **old_module.py** musi zostać zachowany tak długo, jak jest to konieczne, aby dać użytkownikom możliwość migracji ich obiektów.



### Zalety i wady 

**Zalety**

-   [24px](Plik:Edit_OK.svg.md) Jest to najprostsza metoda, która wymaga jedynie przekierowania starej klasy do nowej.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Stare właściwości są zachowywane, o ile nowa klasa ich nie nadpisuje.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Jest to dobre rozwiązanie, jeśli stara i nowa klasa mają te same właściwości *(obsługują ten sam typ danych)*, ale różnią się tylko nazwą modułu lub klasy.

**Wady**

-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Nowa klasa zachowuje stare właściwości obiektu, co nie zawsze jest pożądane.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Nowe właściwości lub zmienione właściwości nie są obsługiwane, więc obiekt zostanie załadowany, ale może nie pokazywać prawidłowego zachowania nowej klasy.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Stary moduł może być przechowywany w nieskończoność, aby zmigrować wszystkie stare obiekty utworzone w przeszłości.



## Metoda 2. Migracja podczas przywracania dokumentu 

Zmigrujemy starszy obiekt, modyfikując starą klasę. Większość oryginalnej klasy zostanie usunięta, a zamiast tego zaimplementowana zostanie metoda `onDocumentRestored`. Gdy ta metoda istnieje, zostanie uruchomiona, gdy dokument spróbuje przywrócić obiekt korzystający z tej klasy, więc jest to okazja, aby przypisać nową klasę, manipulować informacjami lub drukować komunikaty.

W tym przypadku zakładamy, że zdefiniowaliśmy również nowego [dostawcę widoku](Viewprovider/pl.md) w module **viewp/new_view.py**. Jeśli nie chcemy migrować tej klasy, możemy pominąć wszystko po sprawdzeniu `App.GuiUp`. 
```python
# old_module.py
import FreeCAD as App
import objects.new_module as new_module
import viewp.new_view as new_view
_wrn = App.Console.PrintWarning

class OldObject:
    def onDocumentRestored(self, obj):
        new_module.NewObject(obj)
        _wrn("New proxy class used\n")

        if App.GuiUp:
            new_view.ViewProviderNew(obj.ViewObject)
            _wrn("New viewprovider class used\n")
```

Bardziej złożony przykład sprawdza najpierw, czy klasa proxy jest typu, którego szukamy, i kontynuuje migrację tylko wtedy, gdy jest to właściwy typ. 
```python
class OldObject:
    def onDocumentRestored(self, obj):
        if hasattr(obj, "Proxy") and obj.Proxy.Type == "Custom":
            _module = str(obj.Proxy.__class__)
            _module = _module.lstrip("<class '").rstrip("'>")

            if _module == "old_module.OldObject":
                self._migrate(obj)

    def _migrate(self, obj):
        _wrn("New proxy class used\n")
        new_module.NewObject(obj)

        if App.GuiUp:
            new_view.ViewProviderNew(obj.ViewObject)
            _wrn("New viewprovider class used\n")
```

Zakładając, że zmieniliśmy już w ten sposób stary moduł, jeśli otworzymy dokument ze starym obiektem, zobaczymy komunikaty wspominające o użyciu nowych klas.

Sprawdzając obiekt z [konsoli Python](Python_console.md) zobaczymy, że starsze właściwości zostały zachowane, a dodatkowo nowe właściwości zostały dodane wraz z nową klasą Proxy. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.PropertiesList)
['Area', 'Divisions', ..., 'GeneralArea', ..., ..., 'Length', 'Length1', ..., ..., ..., ...]
>>> print(obj.Proxy)
<objects.new_module.NewObject object at 0x7fecb0ebd7b8>
```

Stare właściwości to `Area` i `Length`; nowe właściwości to `Divisions`, `GeneralArea` i `Length`. Migrowany obiekt zachowuje oryginalne dwie właściwości i zyskuje trzy nowe właściwości. Ponieważ jednak nowa właściwość `Length` ma taką samą nazwę jak starsza właściwość, nazwa nowej właściwości jest zmieniana na numer przyrostowy. Przypuszczalnie nie tego chcemy. Możemy poprawić sytuację, postępując zgodnie z uzupełnieniem 2.1 poniżej.

Biorąc pod uwagę, że klasy mają obsługiwać ten sam typ obiektu, chcielibyśmy migracji, w której `Area` przekształca się w `GeneralArea`, a `Length` jest po prostu przypisywany do nowego `Length` i nie ma duplikatów właściwości.

 ===Zalety i wady==

**Zalety**

-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Ta metoda pozwala nam sprawdzić, czy klasa, którą migrujemy, jest właściwą klasą, zamiast po prostu przekierowywać do nowszej klasy.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Podobnie jak w metodzie 1, stare właściwości są zachowywane, o ile nowa klasa ich nie nadpisuje.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> W przeciwieństwie do metody 1, nowe właściwości są zawsze dodawane, jednak jeśli mają tę samą nazwę, ich nazwy zostaną zmienione.
-   [24px](Plik:Edit_OK.svg.md) Migracja nie jest natychmiastowa, nadal możemy manipulować informacjami lub drukować komunikaty podczas ładowania obiektu.

**Wady**

-   [24px](Plik:Edit_Cancel.svg.md) Jest bardziej rozwlekła niż metoda 1, ponieważ musimy zaimplementować metodę `onDocumentRestored`, aby zmigrować obiekt.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Zawsze dodaje nowe właściwości, więc może tworzyć zduplikowane właściwości w przypadku, gdy nowe właściwości mają taką samą nazwę jak stare. To musi być obsługiwane ręcznie.



## Metoda 3. Migracja podczas przywracania dokumentu, ręczna obsługa właściwości 

Jest to rozszerzenie metody 2. W metodzie `onDocumentRestored` musimy zapisać wartości właściwości, które chcemy, a następnie możemy usunąć te oryginalne właściwości. Odbywa się to tak, że gdy nowa klasa jest używana, przypisuje nowe właściwości bez ryzyka kolizji nazw ze starszymi właściwościami.

Podobnie jak w metodzie 2, jeśli chcemy, możemy również dodać fragment kodu, który sprawdza, czy klasa Proxy jest właściwa. W tym przykładzie ponownie zakładamy, że używamy niestandardowego [dostawcy widoku](Viewprovider/pl.md), z co najmniej jedną niestandardową właściwością. 
```python
# old_module.py
import FreeCAD as App
import objects.new_module as new_module
import viewp.new_view as new_view
_wrn = App.Console.PrintWarning

class OldObject:
    def onDocumentRestored(self, obj):
        old = dict()
        old["Area"] = obj.Area
        old["Length"] = obj.Length
        obj.removeProperty("Area")
        obj.removeProperty("Length")

        new_module.NewObject(obj)

        obj.GeneralArea = 3 * old["Area"]
        obj.Length = old["Length"]
        _wrn("New proxy class used; properties migrated\n")

        if App.GuiUp:
            vobj = obj.ViewObject
            old = dict()

            old["LineScale"] = vobj.LineScale
            vobj.removeProperty("LineScale")

            new_view.ViewProviderNew(vobj)

            vobj.LineScale = 1.05 * old["LineScale"]
            _wrn("New viewprovider class used; view properties migrated\n")
```

Widzimy, że stare wartości są przechowywane w słowniku pomocniczym, następnie stare właściwości są usuwane, następnie dodajemy nową klasę, a na koniec przypisujemy wcześniej zapisane wartości do nowych właściwości. W tym momencie możemy przekształcić zapisane wartości zgodnie z potrzebami nowej klasy. Na przykład, `GeneralArea` jest ustawiony na 3-krotność starego `Area`, a nowy `Length` po prostu otrzymuje wartość starego `Length`. Ponieważ wiemy, jak powinny zachowywać się stare i nowe klasy, możemy swobodnie manipulować danymi, aby zmigrować obiekt tak, jak chcemy.

Możemy usunąć tylko te właściwości, które zostały dodane przez klasy [Python](Python/pl.md) podczas tworzenia [obiektów generowanych skryptami](scripted_objects/pl.md). Inne atrybuty należą do bazowego obiektu C++ i nie mogą być usunięte. 
```python
>>> obj.removeProperty("Visibility")
False
```

Zakładając, że zmieniliśmy już stary moduł w ten sposób, jeśli otworzymy dokument ze starym obiektem, zobaczymy komunikaty wspominające o użyciu nowych klas. Sprawdzając obiekt z [konsoli Python](Python_console/pl.md) widzimy, że starsze właściwości zostały usunięte i istnieją tylko nowe. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.PropertiesList)
['Divisions', ..., 'GeneralArea', ..., ..., 'Length', ..., ..., ..., ...]
>>> print(obj.Proxy)
<objects.new_module.NewObject object at 0x7efd456c9b00>
```

Ponieważ w starej klasie właściwość `Divisions` nie istniała, nic nie zostało z nią zrobione. Została ona po prostu utworzona przez nową klasę `objects.new_module.NewObject`.



### Zalety i wady 

**Zalety**

-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Podobnie jak metoda 2, ta metoda pozwala nam sprawdzić, czy klasa, którą migrujemy, jest właściwą klasą.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Mamy pełną kontrolę nad tym, co zrobić ze starymi właściwościami. Zazwyczaj zostaną one usunięte, aby nie było kolizji nazw z nowo dodanymi właściwościami. W ten sposób unikamy zduplikowanych właściwości.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Zapisując starsze wartości, możemy dowolnie manipulować informacjami w kroku przywracania i przypisać odpowiednie wartości do nowych właściwości.

**Wady**

-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Ta metoda jest bardzo rozwlekła w porównaniu do poprzednich, ponieważ musimy zaimplementować metodę `onDocumentRestored` i obsłużyć każdą z właściwości indywidualnie (zapisać wartość, usunąć właściwość, ponownie przypisać wartość). Jest to problematyczne, jeśli obiekt, który chcemy migrować, ma wiele właściwości lub ich wartości muszą być przekształcane w bardzo szczególny sposób.



## Addendum A. Creating the properties only if they do not already exist 

Jedną z wad metody 2 jest to, że zawsze będzie ona próbowała dodać nowe właściwości. Jeśli starsze właściwości mają taką samą nazwę jak nowe, zostaną zduplikowane z przyrostową liczbą, więc `Length` spowoduje `Length1`, a następnie `Length2` i tak dalej. To sprawia, że metoda 2 jest nierealistyczną opcją w większości przypadków, ponieważ nowa klasa i tak będzie używać tylko jednej właściwości.

Aby ulepszyć tę metodę, nową klasę można również zmodyfikować tak, aby dodawała właściwości tylko wtedy, gdy nie istnieją jeszcze pod tą samą nazwą. 
```python
# objects/new_module.py
class NewObject:
    def __init__(self, obj):
        if not hasattr(obj, "Length"):
            obj.addProperty("App::PropertyLength", "Length")
            obj.Length = 30
        if not hasattr(obj, "GeneralArea"):
            obj.addProperty("App::PropertyArea", "GeneralArea")
            obj.GeneralArea = 600
        if not hasattr(obj, "Divisions"):
            obj.addProperty("App::PropertyInteger", "Divisions")
            obj.Divisions = 4

        obj.Proxy = self
        self.Type = "Custom"

    def execute(self, obj):
        pass
```

W tym przypadku, ponieważ `Length` już istnieje, nie zostanie ponownie dodany; `GeneralArea` i `Divisions` nie istnieją, więc zostaną dodane. I tak jak poprzednio, `Area` zostanie zachowany, ponieważ nie został wyraźnie usunięty, chociaż prawdopodobnie nie jest już używany w nowej klasie. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.PropertiesList)
['Area', 'Divisions', ..., 'GeneralArea', ..., ..., 'Length', ..., ..., ..., ...]
>>> print(obj.Proxy)
<objects.new_module.NewObject object at 0x7f036bd4c6a0>
```

To samo można zrobić dla klasy [dostawcy widoku](Viewprovider/pl.md).

Używając tej metody 2 + A, wynik jest podobny do metody 1, ponieważ obiekt zachowa wszystkie poprzednie właściwości, ale dodatkowo zyska nowe właściwości dostarczone przez nową klasę.

Metoda 3 nie potrzebuje tego dodatku do nowej klasy, ponieważ starsze właściwości są wyraźnie usuwane, więc nie będzie żadnych konfliktów podczas instalowania nowych właściwości. Niemniej jednak, nadal dobrą praktyką jest, aby każda klasa dodawała swoje wymagane właściwości tylko wtedy, gdy jeszcze nie istnieją. Jest to pomocne zarówno w przypadku tworzenia nowych [obiektów generowanych skryptami](Scripted_objects/pl.md), jak i ich migracji.



### Zalety i wady 

**Zalety**

-   [24px](Plik:Edit_OK.svg.md) Obiekt zachowa wszystkie poprzednie właściwości, ale dodatkowo zyska nowe właściwości bez powtórzeń.

**Wady**

-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Podobnie jak metoda 2, nadal nie radzi sobie ze zmienionymi nazwami właściwości. Stare właściwości powinny zostać usunięte ręcznie.



## Dodatek B. Migracja różnych wersji starego obiektu 

Metoda 3 jest najbardziej złożoną metodą, ponieważ właściwości są obsługiwane indywidualnie. Jednak w tej metodzie mamy również pełną elastyczność w sposobie manipulowania danymi, co jest zaletą, jeśli chcemy wykonywać złożone operacje.

Jeśli od początku utworzymy właściwość, która przechowuje numer wersji naszego obiektu, możemy użyć tego numeru w przyszłości, aby wykonać określoną migrację z tej wersji do dowolnej innej. Ustawiamy właściwość jako tylko do odczytu, więc nie możemy jej nadpisać w [edytorze właściwości](Property_editor/pl.md), chociaż jest ona nadal dostępna z [konsoli Python](Python_console/pl.md). 
```python
# old_module.py
class OldObject:
    def __init__(self, obj):
        obj.addProperty("App::PropertyLength", "Length")
        obj.addProperty("App::PropertyArea", "Area")
        obj.addProperty("App::PropertyString", "Version")
        obj.setEditorMode("Version", 1)
        obj.Length = 15
        obj.Area = 300
        obj.Version = "0.18"
        obj.Proxy = self
        self.Type = "Custom"

    def execute(self, obj):
        pass
```

Następnie, gdy chcemy zmigrować obiekt, implementujemy metodę `onDocumentRestored` i testujemy tę wersję. 
```python
# old_module.py
import FreeCAD as App
import objects.new_module as new_module
_wrn = App.Console.PrintWarning

class OldObject:
    def onDocumentRestored(self, obj):
        if hasattr(obj, "Version") and obj.Version:
            if obj.Version == "0.18":
                _migrate_from_018(obj)
            elif obj.Version == "0.19":
                _migrate_from_019(obj)

def _migrate_from_018(obj):
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

def _migrate_from_019(obj):
    ...
```

Nie zapisujemy wartości `Version`, ponieważ podczas migracji ustawimy nowy numer `Version`. Jak pokazano w przykładzie, możemy zaimplementować różne funkcje dla każdej odpowiedniej wersji obiektu, który zamierzamy zmigrować. Pomijamy migrację właściwości [dostawcy widoku](Viewprovider/pl.md), ale przebiega ona według tego samego schematu.



### Zalety i wady 

**Zalety**

-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Mamy pełną kontrolę nad tym, co zrobić ze starymi właściwościami i jak przeprowadzić migrację.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Możemy zaimplementować konkretną metodę do migracji konkretnej wersji starego obiektu.

**Wady**

-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Ta metoda jest bardzo gadatliwa, ponieważ musimy mieć jasny pomysł na to, jak obsługiwać każdą z właściwości każdej \"wersji\", którą chcemy zmigrować. Jeśli nasz obiekt ma wiele różnych wersji utworzonych na przestrzeni lat, być może będziemy musieli przygotować długą listę metod, aby zmigrować je do najnowszego obiektu.



## Uzupełnienie B2. Używanie wewnętrznych atrybutów klasy zamiast właściwości 

Zamiast używać [właściwości](Property/pl.md) obiektu do przechowywania informacji o wersji, możemy użyć atrybutu klasy. W ten sposób \"ukrywamy\" informacje o wersji, ponieważ właściwości są zwykle publiczne i widoczne w [edytorze właściwości](Property_editor/pl.md), podczas gdy atrybutami klasy można manipulować tylko z [konsoli Python](Python_console/pl.md). Atrybuty klas mogą być zapisywane i przywracane, jak wyjaśniono w [Obiektchy generowanych skryptami](Scripted_objects_saving_attributes/pl.md). 
```python
# old_module.py
class OldObject:
    def __init__(self, obj):
        obj.addProperty("App::PropertyLength", "Length")
        obj.addProperty("App::PropertyArea", "Area")
        obj.Length = 15
        obj.Area = 300
        obj.Proxy = self

        self.Type = "Custom"
        self.ver = "0.18"

    def execute(self, obj):
        pass
```

Atrybut ten jest kontrolowany poprzez przeglądanie atrybutu `Proxy`. 
```python
>>> obj = App.ActiveDocument.Custom
>>> print(obj.Proxy.ver)
0.18
```

Następnie plik jest modyfikowany w celu migracji obiektu. 
```python
# old_module.py
import FreeCAD as App
import objects.new_module as new_module
_wrn = App.Console.PrintWarning

class OldObject:
    def onDocumentRestored(self, obj):
        if hasattr(obj.Proxy, "ver") and obj.Proxy.ver:
            if obj.Proxy.ver == "0.18":
                _migrate_from_018(obj)

def _migrate_from_018(obj):
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

Kiedy zainstalujemy nową klasę, ta nowa klasa powinna ustawić nową wartość atrybutu version, na przykład self.ver = "0.20".



## Uzupełnienie C. Metoda 3 bez usuwania starych właściwości o tej samej nazwie 

Podobnie jak w Uzupełnieniu A, możemy napisać nową klasę, aby tworzyła właściwości tylko wtedy, gdy jeszcze ich nie ma. Korzystając z metody 3, zapisujemy wartości starszych właściwości, a następnie usuwamy starsze właściwości. Jeśli jednak nowe właściwości nazywają się tak samo jak starsze, nie musimy usuwać starszych, możemy po prostu ponownie użyć tej samej właściwości, ponieważ wiemy, że właściwość nie zostanie zduplikowana. Jeśli korzystamy z Uzupełnienia B, mamy również sposób na zapytanie o wersję.


```python
# old_module.py
import FreeCAD as App
import objects.new_module as new_module
_wrn = App.Console.PrintWarning

class OldObject:
    def onDocumentRestored(self, obj):
        if hasattr(obj, "Version") and obj.Version:
            if obj.Version == "0.18":
                _migrate_from_018(obj)

def _migrate_from_018(obj):
    old = dict()
    old["Area"] = obj.Area
    obj.removeProperty("Area")

    new_module.NewObject(obj)

    obj.GeneralArea = 3 * old["Area"]
    obj.Version = "0.20"
    _wrn("New proxy class used; properties migrated\n")
```

Jak widzimy w przykładzie, stara właściwość `Area` jest usuwana i migrowana do nowej właściwości `GeneralArea` jak zwykle. Nie musimy usuwać `Length` ani `Version`, ponieważ w nowej klasie są one nadal używane z tą samą nazwą i nie zostaną ponownie utworzone ( uzupełnienie A). Ponieważ nie chcemy modyfikować `Length`, ta właściwość nie jest w ogóle dotykana; jest migrowana do nowej klasy po cichu. Aktualizujemy jednak `Version` do nowej wartości. Pomijamy migrację właściwości [dostawcy widoku](viewprovider/pl.md), ale przebiega ona według tego samego schematu.

Powinno to działać jak metoda 3, co oznacza, że stare właściwości są usuwane i tylko nowe właściwości pozostają w nowym obiekcie. Jedyną różnicą jest to, że pomijamy usuwanie i ponowne tworzenie właściwości, które nazywają się tak samo. Proces ten powinien działać tak długo, jak długo stara [właściwość](Property/pl.md) i nowa [właściwość](Property/pl.md) mają ten sam typ *(na przykład `App::PropertyLength` lub `App::PropertyArea`)*, więc stara właściwość może przekazać swoją wartość bezpośrednio. Jeśli jednak nowa właściwość ma inny typ niż stara właściwość, wówczas stara właściwość powinna zostać usunięta, w przeciwnym razie stara właściwość całkowicie nadpisze nową właściwość, co prawdopodobnie nie jest tym, czego chcemy, ponieważ nowa klasa będzie oczekiwać nowego typu, a nie starego.



### Zalety i wady 

**Zalety**

-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Podobnie jak metoda 3, ta metoda pozwala nam na pełną kontrolę migracji starych informacji.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Unikamy pisania kodu, który usuwa i odtwarza właściwości, które nazywają się tak samo.

**Wady**

-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Podobnie jak metoda 3, ta metoda jest nadal bardzo gadatliwa, ponieważ musimy ostrożnie obchodzić się z właściwościami.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Jeśli nowa [właściwość](Property/pl.md) i stara [właściwość](Property/pl.md) mają tę samą nazwę, nowa właściwość zostanie nadpisana, co może być niepożądanym zachowaniem, zwłaszcza jeśli obie właściwości mają różne typy. W takim przypadku konieczne jest usunięcie starej właściwości i ręczna migracja jej wartości.



## Podsumowanie

Każda z metod ma zalecane zastosowanie:

-   Metoda 1. Moduł jest przenoszony lub zmieniana jest jego nazwa, ale właściwości pozostają takie same. Proste przekierowanie klas, ponieważ właściwości nie muszą być w ogóle modyfikowane.
-   Metoda 2+A. Proste scenariusze migracji. Wyświetla komunikat, gdy obiekt jest migrowany z jednej klasy do drugiej. Właściwości są tego samego typu i nie muszą być w ogóle modyfikowane.
-   Metoda 3, 3+A lub 3+B. Złożone scenariusze migracji. Pełna kontrola nad właściwościami, usuwanie starych i dodawanie nowych właściwości. Identyfikator umożliwiający poznanie wersji obiektu jest przydatny do wybrania odpowiedniej funkcji do przeprowadzenia migracji *(dodatek B lub B2)*.

Najlepiej unikać następujących metod:

-   Metoda 2. Właściwości zostaną zduplikowane, jeśli nowa klasa nie sprawdzi istniejących właściwości *(Dodatek A)*.
-   Metoda 3+C. Używaj tylko wtedy, gdy stare i nowe właściwości są tego samego typu. W przeciwnym razie użyj metody 3 lub 3+B, aby usunąć starsze właściwości i obsłużyć je dokładnie tak, jak trzeba.



## Odnośniki internetowe 

-   [Migracja i aktualizacja starych obiektów skryptowych](https://forum.freecadweb.org/viewtopic.php?t=42948)
-   [Migracja starych obiektów skryptowych](https://forum.freecadweb.org/viewtopic.php?f=18&t=46218)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Scripted objects migration/pl
