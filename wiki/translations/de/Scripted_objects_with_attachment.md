# Scripted objects with attachment/de
## Einführung

Der Zweck dieser Seite ist es, ein minimales Beispiel zu geben, das die Funktion [Part Befestigen](Part_EditAttachment/de.md) unter Verwendung von [skriptgenerierten Objekten](Scripted_objects.md) in Python zeigt.

Siehe unten, [Full and complete minimal example](#Full_and_Complete_Minimal_Example.md).

Das folgende GIF zeigt das Befestigen unseres benutzerdefinierten Würfels an einen Zylinder, damit dieser seine Position automatisch nachführt wenn der Zylinder seine Position ändert.

![](images/Box-attached-to-cylinder-demo.gif )

**HINWEIS:** Der Würfel ist unser benutzerdefiniertes Objekt, und der Zylinder ist ein reguläres FreeCAD Objekt, das im Arbeitsbereich Part erzeugt wurde.



## Benutzerdefinierte Objekte verknüpfbar machen 



### Einfügen der Anfügen Erweiterung 

Zuerst müssen wir die Part::AttachExtensionPython Erweiterung zum Konstruktor unseres Part::FeaturePython Objektes oder in die __init__ Methode, unseres benutzerdefinierten Objektes einfügen.

 {.python .numberLines}
class Box():
    """Custom Scripted Box Object"""

    def __init__(self, obj):
        self.Type = 'Box'

        obj.Proxy = self
        
        ... custom properties

        # Needed to make this object "attachable"
        obj.addExtension('Part::AttachExtensionPython')


Ohne Anfügen dieses Code erhalten wir die folgenden Warnung, falls wir versuchen unser benutzerdefiniertes Objekt an ein anderes Objekt anzufügen.

![](images/Part-attachment-warning-dialog.png )



### Anfügen der Position basierend auf dem angefügten Objekt 

Dann müssen wir in der \execute\ Methode unseres benutzerdefinierten Objektes \positionBySupport\ unseres \Part::FeaturePython\ aufrufen.

 {.python .numberLines}
class Box:...

    def execute(self, obj):
        obj.positionBySupport()
        
        # Assign a Shape to obj
        obj.Shape = Part.makeBox(...)


Ohne den Aufruf von positionBySupport, würde unser benutzerdefiniertes Objekt seine Position nicht anfügen, falls sich die Position des Objektes an welches es angefügt ist, ändert.



## Abschließend das vollständige minimale Beispiel 

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




## Hinweise

-   [Part EditAttachment](Part_EditAttachment.md)
-   [FreeCAD Forum - Parametric attachment of scripted object](https://forum.freecadweb.org/viewtopic.php?f=22&t=24794)
-   [FreeCAD Forum - Port attachment to be an extension](https://forum.freecadweb.org/viewtopic.php?f=10&t=18978&start=10)
-   [GitHub - freecad-part-attachment-python-example](https://github.com/gbroques/freecad-part-attachment-python-example)



## Mit den folgenden Versionen von FreeCAD getestet 

Mit den folgenden Versionen von FreeCAD getestet:

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

Hinweis: Für FreeCAD 0.19 benötigt dieses Tutorial eine geringfügige Erweiterung:

-   Das zweite Argument der \addExtension\ Methode wurde überflüssig.
-   Detail siehe <https://forum.freecadweb.org/viewtopic.php?f=10&t=54370>



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Scripted objects with attachment/de
