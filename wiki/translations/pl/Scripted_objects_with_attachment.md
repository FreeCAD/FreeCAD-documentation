# Scripted objects with attachment/pl
## Wprowadzenie

Celem tej strony jest pokazanie podstawowego przykładu zastosowania funkcji [Dołączenie](Part_EditAttachment/pl.md) środowiska Część, przy wykorzystaniu [obiektów tworzonych skryptami](Scripted_objects/pl.md) w środowisku Python.

Zobacz [pełny i kompletny minimalny przykład](#Full_and_Complete_Minimal_Example.md) poniżej.

Poniższy GIF demonstruje dołączenie naszego niestandardowego pola do walca i automatyczną aktualizację jego pozycji, gdy zmienia się pozycja walca.

![](images/Box-attached-to-cylinder-demo.gif )

**UWAGA:** Pudełko jest naszym niestandardowym obiektem skryptowym, a walec jest zwykłym obiektem FreeCAD wygenerowanym w środowisku pracy Część.



## Dołączanie obiektów tworzonych skryptami 



### Dodawanie rozszerzonego dołączania 

Najpierw musimy dodać rozszerzenie Part::AttachExtensionPython do naszego obiektu Part::FeaturePython w konstruktorze lub metodzie __init__ naszego niestandardowego obiektu tworzonego skryptem.

 {.python .numberLines}
class Box():
    """Custom Scripted Box Object"""

    def __init__(self, obj):
        self.Type = 'Box'

        obj.Proxy = self
        
        ... custom properties

        # Needed to make this object "attachable"
        obj.addExtension('Part::AttachExtensionPython')


Bez dodania tego kodu zobaczymy następujące okno dialogowe z ostrzeżeniem podczas dołączania naszego niestandardowego obiektu tworzonego skryptem do innego obiektu.

![](images/Part-attachment-warning-dialog.png )



### Aktualizacja pozycji na podstawie dołączonego obiektu 

Następnie, w metodzie \execute\ naszego niestandardowego obiektu tworzonego skryptem, musimy wywołać \positionBySupport\ na naszym obiekcie \Part::FeaturePython\.

 {.python .numberLines}
class Box:...

    def execute(self, obj):
        obj.positionBySupport()
        
        # Assign a Shape to obj
        obj.Shape = Part.makeBox(...)


Bez wywołania positionBySupport, nasz niestandardowy obiekt tworzony skryptem nie zaktualizuje swojej pozycji, gdy zmieni się pozycja dołączonego do niego obiektu.



## Pełny i kompletny minimalny przykład 

 {.python .numberLines}
import FreeCAD as App
import Part


class Box():
    """
    Simple Custom Box Object
    See Also:
        https://wiki.freecadweb.org/FeaturePython_Objects
    """

    def __init__(self, obj):
        """
        Constructor
        Arguments
        
        - obj: an existing document object or an object created with FreeCAD.Document.addObject('Part::FeaturePython', '{name}').
        """

        self.Type = 'Box'

        obj.Proxy = self
        obj.addProperty('App::PropertyLength', 'Length',
                        'Dimensions', 'Box length').Length = 10.0
        obj.addProperty('App::PropertyLength', 'Width',
                        'Dimensions', 'Box width').Width = 10.0
        obj.addProperty('App::PropertyLength', 'Height',
                        'Dimensions', 'Box height').Height = 10.0

        # Needed to make this object "attachable",
        # or able to attach parameterically to other objects
        obj.addExtension('Part::AttachExtensionPython')

    def execute(self, obj):
        """
        Called on document recompute
        """
        # Needed to update position when attached-to object changes position.
        # Reposition object based on Support, MapMode and MapPathParameter properties.
        # Returns True if attachment calculation was successful, False if object is not attached and Placement wasn't updated,
        obj.positionBySupport()

        obj.Shape = Part.makeBox(obj.Length, obj.Width, obj.Height)


def create_box(obj_name, document):
    """
    Create a Box.
    """
    obj = document.addObject('Part::FeaturePython', obj_name)
    Box(obj)
    obj.ViewObject.Proxy = 0  # Mandatory unless ViewProvider is coded
    return obj


document = App.ActiveDocument
if document is None:
    document = App.newDocument('Part Attachment Example')

box = create_box('CustomBox', document)
document.recompute()




## Bibliografia

-   [Część: Edycja dołączenia](Part_EditAttachment/pl.md)
-   [Forum FreeCAD - Parametryczne dołączanie obiektu skryptowego](https://forum.freecadweb.org/viewtopic.php?f=22&t=24794)
-   [Forum FreeCAD - Port dołączenia jako rozszerzenie](https://forum.freecadweb.org/viewtopic.php?f=10&t=18978&start=10)
-   [GitHub - freecad-part-attachment-python-example](https://github.com/gbroques/freecad-part-attachment-python-example).

 ==Przetestowano z następującą wersją FreeCAD=

Informacje o testowanej wersji FreeCAD:

    OS: Ubuntu 18.04.3 LTS
    Word size of OS: 64-bit
    Word size of FreeCAD: 64-bit
    Version: 0.18.16146 (Git) AppImage
    Build type: Release
    Branch: (HEAD detached at 0.18.4)
    Hash: 980bf9060e28555fecd9e3462f68ca74007b70f8
    Python version: 3.6.7
    Qt version: 5.6.2
    Coin version: 4.0.0a
    OCC version: 7.3.0
    Locale: English/UnitedStates (en_US)

Uwaga: Dla FreeCAD 0.19 ten samouczek wymaga drobnej aktualizacji:

-   Drugi argument metody\addExtension\ został przestarzały.
-   Szczegółowe informacje można znaleźć na forum <https://forum.freecadweb.org/viewtopic.php?f=10&t=54370>



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Scripted objects with attachment/pl
