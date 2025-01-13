# Create a FeaturePython object part II/pl
## Wprowadzenie

Na stronie [Tworzenie obiektów FeaturePython - część I](Create_a_FeaturePython_object_part_I/pl.md) skupiliśmy się na wewnętrznych aspektach klasy Python zbudowanej wokół obiektu FeaturePython, a konkretnie obiektu `App::FeaturePython`. Stworzyliśmy obiekt, zdefiniowaliśmy niektóre właściwości i dodaliśmy wywołanie zwrotne zdarzenia na poziomie dokumentu, które pozwala naszemu obiektowi odpowiedzieć na ponowne obliczenie dokumentu za pomocą metody `execute()`. Ale nasz obiekt wciąż nie jest obecny w [widoku 3D](3D_view/pl.md). Naprawmy to, dodając ramkę.



## Dodawanie prostopadłościanu 

Najpierw na górze pliku **box.py**, poniżej istniejącego importu, dodaj:


```python
import Part
```

Następnie w `execute()` usuń instrukcję `print()` i dodaj następującą linię w jej miejsce:


```python
Part.show(Part.makeBox(obj.Length, obj.Width, obj.Height))
```

![ right](images/App_featurepython_box.png )

Polecenia te wykonują metody Python, które są domyślnie dostarczane z FreeCAD:

-   Metoda `Part.makeBox()` generuje kształt prostopadłościanu.
-   Obejmujące wywołanie `Part.show()` dodaje kształt do dokumentu i czyni go widocznym.

Usuń wszystkie istniejące obiekty, przeładuj moduł box i utwórz nowy obiekt box za pomocą `box.create()`. Zauważ, że na ekranie natychmiast pojawia się prostopadłościan. Dzieje się tak, ponieważ wymuszamy ponowne obliczenie dokumentu na końcu `box.create()`, co z kolei uruchamia metodę `execute()` naszej klasy `box`.

Na pierwszy rzut oka wynik może wyglądać dobrze, ale są pewne problemy. Najbardziej oczywistym z nich jest to, że prostopadłościan jest reprezentowany przez zupełnie inny obiekt niż nasz obiekt FeaturePython. `Part.show()` po prostu tworzy osobny obiekt prostopadłościanu i dodaje go do dokumentu. Co gorsza, jeśli zmienisz wymiary obiektu FeaturePython, zostanie utworzony inny kształt prostopadłościanu, a stary pozostanie na swoim miejscu. A jeśli masz otwarty panel [Widoku raportu](Report_view.md), być może zauważyłeś błąd \"Recursive calling of recompute for document Unnamed\". Ma to związek z użyciem metody `Part.show()` wewnątrz obiektu FeaturePython. 

[na początek strony](#top.md)



## Naprawa kodu 

Aby rozwiązać te problemy, musimy wprowadzić kilka zmian. Do tej pory używaliśmy obiektu `App::FeaturePython`, który w rzeczywistości nie jest przeznaczony do wizualnej reprezentacji w widoku 3D. Zamiast tego musimy użyć obiektu `Part::FeaturePython`. W `create()` zmień następującą linię:


```python
obj = App.ActiveDocument.addObject('App::FeaturePython', obj_name)
```

na:


```python
obj = App.ActiveDocument.addObject('Part::FeaturePython', obj_name)
```

Aby pozbyć się oddzielnego obiektu pudełka, musimy przypisać wynik metody `makeBox()` do właściwości `Shape` naszego obiektu `Part::FeaturePython`. Zmień tę linię w `execute()`:


```python
Part.show(Part.makeBox(obj.Length, obj.Width, obj.Height))
```

na:


```python
obj.Shape = Part.makeBox(obj.Length, obj.Width, obj.Height)
```

![](images/Part_featurepython_no_vp.png )

Zapisz zmiany, przełącz się z powrotem do FreeCAD, usuń wszystkie istniejące obiekty, przeładuj moduł prostopadłoscianu i utwórz nowy obiekt prostopadłoscianu. Nowy wynik jest nieco rozczarowujący. Nie ma już dodatkowego obiektu w widoku drzewa, a ikona w widoku drzewa zmieniła się, ale nasz prostopadłościan w widoku 3D również zniknął (dlatego ikona jest szara). Co się stało? Chociaż poprawnie utworzyliśmy nasz kształt prostopadłoscianu i przypisaliśmy go do obiektu `Part::FeaturePython`, aby faktycznie pojawił się w widoku 3D, musimy przypisać [ViewProvider](Viewprovider.md). .

[na początek strony](#top.md)



## Piszemy ViewProvider 

Dostawca widoku jest składnikiem obiektu, który pozwala mu na wizualną reprezentację w widoku 3D. FreeCAD wykorzystuje strukturę aplikacji, która została zaprojektowana w celu oddzielenia danych (\"modelu\") od ich wizualnej reprezentacji (\"widoku\"). Jeśli spędziłeś trochę czasu pracując z FreeCAD w Python, prawdopodobnie jesteś już tego świadomy dzięki wykorzystaniu dwóch podstawowych modułów Python: `FreeCAD` i `FreeCADGui`. *(często aliasowanych odpowiednio jako `App` i `Gui`)*

Nasz obiekt FeaturePython również wymaga tych elementów. Do tej pory skupialiśmy się wyłącznie na części \"modelowej\" kodu, teraz nadszedł czas na napisanie części \"widokowej\". Na szczęście większość ViewProviderów jest prosta i nie wymaga wiele wysiłku do napisania, przynajmniej na początek. Oto przykładowy ViewProvider zapożyczony i nieco zmodyfikowany z [1](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py):


```python
class ViewProviderBox:

    def __init__(self, obj):
        """
        Set this object to the proxy object of the actual view provider
        """

        obj.Proxy = self

    def attach(self, obj):
        """
        Setup the scene sub-graph of the view provider, this method is mandatory
        """
        return

    def updateData(self, fp, prop):
        """
        If a property of the handled feature has changed we have the chance to handle this here
        """
        return

    def getDisplayModes(self,obj):
        """
        Return a list of display modes.
        """
        return []

    def getDefaultDisplayMode(self):
        """
        Return the name of the default display mode. It must be defined in getDisplayModes.
        """
        return "Shaded"

    def setDisplayMode(self,mode):
        """
        Map the display mode defined in attach with those defined in getDisplayModes.
        Since they have the same names nothing needs to be done.
        This method is optional.
        """
        return mode

    def onChanged(self, vp, prop):
        """
        Print the name of the property that has changed
        """

        App.Console.PrintMessage("Change property: " + str(prop) + "\n")

    def getIcon(self):
        """
        Return the icon in XMP format which will appear in the tree view. This method is optional and if not defined a default icon is shown.
        """

        return """
            /* XPM */
            static const char * ViewProviderBox_xpm[] = {
            "16 16 6 1",
            "    c None",
            ".   c #141010",
            "+   c #615BD2",
            "@   c #C39D55",
            "#   c #000000",
            "$   c #57C355",
            "        ........",
            "   ......++..+..",
            "   .@@@@.++..++.",
            "   .@@@@.++..++.",
            "   .@@  .++++++.",
            "  ..@@  .++..++.",
            "###@@@@ .++..++.",
            "##$.@@$#.++++++.",
            "#$#$.$$$........",
            "#$$#######      ",
            "#$$#$$$$$#      ",
            "#$$#$$$$$#      ",
            "#$$#$$$$$#      ",
            " #$#$$$$$#      ",
            "  ##$$$$$#      ",
            "   #######      "};
            """

    def dumps(self):
        """
        Called during document saving.
        """
        return None

    def loads(self,state):
        """
        Called during document restore.
        """
        return None
```

W powyższym kodzie definiujemy ikonę XMP dla tego obiektu. Projektowanie ikon wykracza poza zakres tego poradnika, ale podstawowym projektowaniem można zarządzać za pomocą narzędzi open source, takich jak [GIMP](https://www.gimp.org), [Krita](https://krita.org/en/) i [Inkscape](https://inkscape.org/). Metoda `getIcon()` jest opcjonalna, FreeCAD użyje domyślnej ikony, jeśli ta metoda nie zostanie podana.

Dodaj kod ViewProvider na końcu **box.py** i w metodzie `create()` wstaw następującą linię nad instrukcją `recompute()`:


```python
ViewProviderBox(obj.ViewObject)
```

Powoduje to instancję niestandardowej klasy ViewProvider i przekazuje do niej wbudowany obiekt ViewObject FeaturePython. Podczas inicjalizacji klasa ViewProvider zapisuje odniesienie do siebie w atrybucie FeaturePython `ViewObject.Proxy`. W ten sposób, gdy FreeCAD musi wizualnie wyrenderować nasz prostopadłościan, może znaleźć klasę ViewProvider, aby to zrobić.

Teraz zapisz zmiany i wróć do FreeCAD. Zaimportuj lub przeładuj moduł prostopadłościanu i wywołaj `box.create()`. Powinieneś teraz zobaczyć dwie rzeczy:

-   Ikona obiektu prostopadłościanu uległa zmianie.
-   I, co ważniejsze, w widoku 3D pojawia się prostopadłościan. Jeśli go nie widzisz, naciśnij przycisk **<img src="images/Std_ViewFitAll.svg" width=16px> [Std: Przybliż i dopasuj wszystko](Std_ViewFitAll/pl.md)**. Możesz nawet zmienić wymiary prostopadłościanu, zmieniając wartości w [Edytorze właściwości](Property_editor/pl.md). Spróbuj!

[na początek strony](#top.md)



## Zdarzenia związane z łapaniem 

Omówiliśmy już pułapkowanie zdarzeń. Prawie każda metoda klasy FeaturePython służy jako wywołanie zwrotne dostępne dla obiektu FeaturePython *(który uzyskuje dostęp do instancji naszej klasy poprzez atrybut `Proxy`)*.

Poniżej znajduje się lista wywołań zwrotnych, które mogą być zaimplementowane w podstawowym obiekcie FeaturePython:

++++
|                             | Wywoływany podczas ponownego obliczania dokumentu                           | Nie wywołuj `recompute()` z tej metody (lub jakiejkolwiek metody wywołanej z `execute()`), ponieważ spowoduje to zagnieżdżone ponowne obliczenie.                                                                                                                                                                                            |
| `execute(self, obj)`              |                                                                             |                                                                                                                                                                                                                                                                                                                                                                                            |
|                                         |                                                                             |                                                                                                                                                                                                                                                                                                                                                                                            |
++++
|                             | Wywoływana przed zmianą wartości właściwości                                |                                                                                                                                                                                                                                                                                                                                                                             |
| `onBeforeChange(self, obj, prop)` |                                                                             | `prop`                                                                                                                                                                                                                                                                                                                                                                            |
|                                         |                                                                             |                                                                                                                                                                                                                                                                                                                                                                                         |
|                                            |                                                                             | to nazwa właściwości, która ma zostać zmieniona, a nie sam obiekt właściwości. Zmian właściwości nie można anulować. Poprzednie / następne wartości właściwości nie są jednocześnie dostępne do porównania.                                                                                                                                                                                |
++++
|                             | Wywoływana po zmianie właściwości                                           |                                                                                                                                                                                                                                                                                                                                                                             |
| `onChanged(self, obj, prop)`      |                                                                             | `prop`                                                                                                                                                                                                                                                                                                                                                                            |
|                                         |                                                                             |                                                                                                                                                                                                                                                                                                                                                                                         |
|                                            |                                                                             | to nazwa właściwości, która ma zostać zmieniona, a nie sam obiekt właściwości.                                                                                                                                                                                                                                                                                                             |
++++
|                             | Wywoływana po przywróceniu dokumentu lub skopiowaniu obiektu FeaturePython. | Czasami odniesienia do obiektu FeaturePython z klasy lub klasy z obiektu FeaturePython mogą być uszkodzone, ponieważ metoda klasy `__init__()` nie jest wywoływana podczas rekonstrukcji obiektu. Dodanie `self.Object <nowiki>=</nowiki> obj` lub `obj.Proxy <nowiki>=</nowiki> self` często rozwiązuje te problemy. |
| {{Incode|onDocumentRestored(self, obj)}}   |                                                                             |                                                                                                                                                                                                                                                                                                                                                                                            |
|                                         |                                                                             |                                                                                                                                                                                                                                                                                                                                                                                            |
++++

: Podstawowe wywołania zwrotne FeaturePython

Aby uzyskać pełną listę dostępnych metod FeaturePython, zobacz stronę [metody FeaturePython](FeaturePython_methods/pl.md).

Ponadto w klasie ViewProvider znajdują się dwa wywołania zwrotne, które mogą czasami okazać się przydatne:

++++
|                         | Wywoływana po zmianie właściwości danych *(modelu)* |                                                                                                                                                                               |
| `updateData(self, obj, prop)` |                                                     | `obj`                                                                                                                                                                               |
|                                     |                                                     |                                                                                                                                                                                           |
|                                        |                                                     | jest odwołaniem do instancji klasy FeaturePython, a nie instancji ViewProvider. `prop` to nazwa właściwości, która ma zostać zmieniona, a nie sam obiekt właściwości. |
++++
|                         | Wywoływane po zmianie właściwości widoku            |                                                                                                                                                                               |
| `onChanged(self, vobj, prop)` |                                                     | `vobj`                                                                                                                                                                              |
|                                     |                                                     |                                                                                                                                                                                           |
|                                        |                                                     | jest odwołaniem do instancji ViewProvider. `prop` jest nazwą właściwości widoku, która została zmieniona.                                                             |
++++

: Podstawowe wywołania zwrotne ViewProvider

Nierzadko można spotkać się z sytuacją, w której wywołania zwrotne Python nie są uruchamiane tak, jak powinny. Początkujący w tej dziedzinie mogą być pewni, że system wywołań zwrotnych FeaturePython nie jest kruchy ani uszkodzony. Niezmiennie, gdy wywołania zwrotne nie są uruchamiane, jest to spowodowane utratą lub niezdefiniowaniem odniesienia w kodzie bazowym. Jeśli jednak wydaje się, że wywołania zwrotne nie działają bez wyjaśnienia, dostarczenie odwołań do obiektów/proxy w wywołaniu zwrotnym `onDocumentRestored()` *(jak wspomniano w pierwszej tabeli powyżej)* może złagodzić te problemy. Dopóki nie poczujesz się komfortowo z systemem wywołań zwrotnych, przydatne może być dodanie instrukcji drukowania w każdym wywołaniu zwrotnym, aby drukować komunikaty na konsoli podczas programowania.

[na początek strony](#top.md)



## Kompletny kod 


```python
import FreeCAD as App
import Part

def create(obj_name):
    """
    Object creation method
    """

    obj = App.ActiveDocument.addObject('Part::FeaturePython', obj_name)

    box(obj)

    ViewProviderBox(obj.ViewObject)

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

        obj.Shape = Part.makeBox(obj.Length, obj.Width, obj.Height)

class ViewProviderBox:

    def __init__(self, obj):
        """
        Set this object to the proxy object of the actual view provider
        """

        obj.Proxy = self

    def attach(self, obj):
        """
        Setup the scene sub-graph of the view provider, this method is mandatory
        """
        return

    def updateData(self, fp, prop):
        """
        If a property of the handled feature has changed we have the chance to handle this here
        """
        return

    def getDisplayModes(self,obj):
        """
        Return a list of display modes.
        """
        return []

    def getDefaultDisplayMode(self):
        """
        Return the name of the default display mode. It must be defined in getDisplayModes.
        """
        return "Shaded"

    def setDisplayMode(self,mode):
        """
        Map the display mode defined in attach with those defined in getDisplayModes.
        Since they have the same names nothing needs to be done.
        This method is optional.
        """
        return mode

    def onChanged(self, vp, prop):
        """
        Print the name of the property that has changed
        """

        App.Console.PrintMessage("Change property: " + str(prop) + "\n")

    def getIcon(self):
        """
        Return the icon in XMP format which will appear in the tree view. This method is optional and if not defined a default icon is shown.
        """

        return """
            /* XPM */
            static const char * ViewProviderBox_xpm[] = {
            "16 16 6 1",
            "    c None",
            ".   c #141010",
            "+   c #615BD2",
            "@   c #C39D55",
            "#   c #000000",
            "$   c #57C355",
            "        ........",
            "   ......++..+..",
            "   .@@@@.++..++.",
            "   .@@@@.++..++.",
            "   .@@  .++++++.",
            "  ..@@  .++..++.",
            "###@@@@ .++..++.",
            "##$.@@$#.++++++.",
            "#$#$.$$$........",
            "#$$#######      ",
            "#$$#$$$$$#      ",
            "#$$#$$$$$#      ",
            "#$$#$$$$$#      ",
            " #$#$$$$$#      ",
            "  ##$$$$$#      ",
            "   #######      "};
            """

    def dumps(self):
        """
        Called during document saving.
        """
        return None

    def loads(self,state):
        """
        Called during document restore.
        """
        return None
```

[na początek strony](#top.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Create a FeaturePython object part II/pl
