 {{TOCright}}

## Introduction

Le but de cette page est de montrer un exemple minimal de fonctionnalité de [Part Ancrage](Part_Attachment/fr.md) utilisant des [Objets créés par script](Scripted_objects/fr.md) en Python.

Voir l\'[Exemple minimal complet](#Exemple_minimal_complet.md) ci-dessous.

Le GIF suivant montre comment attacher notre boîte personnalisée à un cylindre et mettre à jour automatiquement sa position lorsque la position du cylindre change.

![](images/Box-attached-to-cylinder-demo.gif )

 **REMARQUE:** La boîte est notre objet personnalisé crée par script et le cylindre est un objet FreeCAD standard généré à partir de l\'atelier Part.

## Rendre les objets créés par script attachables 

### Ajouter une extension attachée 

Tout d\'abord, nous devons ajouter l\'extension Part::AttachExtensionPython à notre objet Part::FeaturePython dans le constructeur, ou la méthode __init__ de notre objet créé par script personnalisé.

 {.python .numberLines}
class Box():
    """Custom Scripted Box Object"""

    def __init__(self, obj):
        self.Type = 'Box'

        obj.Proxy = self
        
        ... custom properties

        # Needed to make this object "attachable"
        obj.addExtension('Part::AttachExtensionPython', obj)


Sans ce code, nous verrions la boîte de dialogue d\'avertissement suivante lors de la connexion de notre objet personnalisé créé par script à un autre objet.

![](images/Part-attachment-warning-dialog.png )

### Mis à jour de la position en fonction de l\'objet attaché 

Ensuite, dans la méthode *execute* de notre script personnalisé, nous devons appeler le *positionBySupport* sur notre objet *Part::FeaturePython*.

 {.python .numberLines}
class Box:...

    def execute(self, obj):
        obj.positionBySupport()
        
        # Assign a Shape to obj
        obj.Shape = Part.makeBox(...)


Si positionBySupport n\'est pas appelé, notre objet personnalisé crée par script ne mettra pas à jour sa position lorsque la position de l\'objet attaché change.

## Exemple minimal complet 

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
        ---------
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
        obj.addExtension('Part::AttachExtensionPython', obj)

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


## Références

-   [Part Ancrage](Part_Attachment/fr.md)
-   [FreeCAD Forum - Parametric attachment of scripted object](https://forum.freecadweb.org/viewtopic.php?f=22&t=24794)
-   [FreeCAD Forum - Port attachment to be an extension](https://forum.freecadweb.org/viewtopic.php?f=10&t=18978&start=10)
-   [GitHub - freecad-part-attachment-python-example](https://github.com/gbroques/freecad-part-attachment-python-example)

## Testé avec la version FreeCAD 

Testé avec la version suivante de FreeCAD:

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

Remarque : pour FreeCAD 0.19, ce tutoriel nécessite une mise à jour mineure :

-   Le deuxième argument de la méthode \addExtension\ est devenu obsolète.
-   Pour plus de détails, voir <https://forum.freecadweb.org/viewtopic.php?f=10&t=54370>


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
