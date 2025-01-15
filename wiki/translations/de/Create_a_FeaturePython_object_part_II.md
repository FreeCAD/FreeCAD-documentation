# Create a FeaturePython object part II/de
## Einführung

Auf der Seite [Erstellen eines FeaturePython-Objekts Teil I](Create_a_FeaturePython_object_part_I/de.md) haben wir uns auf die internen Aspekte einer Python-Klasse konzentriert, die um ein FeaturePython-Objekt herum aufgebaut ist, insbesondere um ein `App::FeaturePython`-Objekt. Wir haben das Objekt erstellt, einige Eigenschaften definiert und einen Ereignisrückruf auf Dokumentebene hinzugefügt, der es unserem Objekt ermöglicht, auf eine Dokumentneuberechnung mit der Methode `execute()` zu reagieren. Unser Objekt ist jedoch noch immer nicht in der [3D-Ansicht](3D_view/de.md) vorhanden. Beheben wir das, indem wir eine Box hinzufügen.



## Hinzufügen eines Kastens 

Füge zunächst oben in der Datei **box.py** unterhalb des vorhandenen Imports Folgendes hinzu:


```python
import Part
```

Lösche dann in `execute()` die Anweisung `print()` und füge an ihrer Stelle die folgende Zeile hinzu:


```python
Part.show(Part.makeBox(obj.Length, obj.Width, obj.Height))
```

![ right](images/App_featurepython_box.png )

Diese Befehle führen Python-Methoden aus, die standardmäßig mit FreeCAD mitgeliefert werden:

-   Die Methode `Part.makeBox()` erzeugt eine Kastenform.
-   Der umschließende Aufruf von `Part.show()` fügt die Form dem Dokument hinzu und macht sie sichtbar.

Lösche alle vorhandenen Objekte, lade das Box-Modul neu und erstelle mit `box.create()` ein neues Box-Objekt. Beachte, dass sofort eine Box auf dem Bildschirm erscheint. Das liegt daran, dass wir das Dokument am Ende von `box.create()` zu einer Neuberechnung zwingen, was wiederum die Methode `execute()` unserer Klasse `box` auslöst.

Auf den ersten Blick sieht das Ergebnis vielleicht gut aus, aber es gibt einige Probleme. Das offensichtlichste ist, dass die Box durch ein völlig anderes Objekt als unser FeaturePython-Objekt dargestellt wird. `Part.show()` erstellt einfach ein separates Box-Objekt und fügt es dem Dokument hinzu. Schlimmer noch: Wenn du die Abmessungen des FeaturePython-Objekts änderst, wird eine andere Box-Form erstellt und die alte bleibt an Ort und Stelle. Und wenn du die [Berichtsansicht](Report_view.md) geöffnet hast, ist dir möglicherweise ein Fehler mit der Meldung „Rekursiver Aufruf von Neuberechnung für Dokument Unbenannt" aufgefallen. Dies hat mit der Verwendung der `Part.show()`-Methode innerhalb eines FeaturePython-Objekts zu tun. 

[Anfang](#top.md)



## Festlegen des Codes 

Um diese Probleme zu lösen, müssen wir eine Reihe von Änderungen vornehmen. Bisher haben wir ein `App::FeaturePython`-Objekt verwendet, das eigentlich nicht für eine visuelle Darstellung in der 3D-Ansicht vorgesehen ist. Stattdessen müssen wir ein `Part::FeaturePython`-Objekt verwenden. Ändere in `create()` die folgende Zeile:


```python
obj = App.ActiveDocument.addObject('App::FeaturePython', obj_name)
```

in:


```python
obj = App.ActiveDocument.addObject('Part::FeaturePython', obj_name)
```

Um das separate Box-Objekt loszuwerden, müssen wir das Ergebnis der Methode `makeBox()` der Eigenschaft `Shape` unseres Objekts `Part::FeaturePython` zuweisen. Änderne diese Zeile in `execute()`:


```python
Part.show(Part.makeBox(obj.Length, obj.Width, obj.Height))
```

in:


```python
obj.Shape = Part.makeBox(obj.Length, obj.Width, obj.Height)
```

![](images/Part_featurepython_no_vp.png )

Speichere deine Änderungen, wechsle zurück zu FreeCAD, lösche alle vorhandenen Objekte, lade das Boxmodul neu und erstelle ein neues Boxobjekt. Das neue Ergebnis ist etwas enttäuschend. Es gibt kein zusätzliches Objekt mehr in der Baumansicht und das Symbol in der Baumansicht hat sich geändert, aber unsere Box in der 3D-Ansicht ist auch verschwunden (weshalb das Symbol grau ist). Was ist passiert? Obwohl wir unsere Boxform ordnungsgemäß erstellt und einem `Part::FeaturePython`-Objekt zugewiesen haben, müssen wir einen [ViewProvider](Viewprovider.md) zuweisen, damit sie tatsächlich in der 3D-Ansicht angezeigt wird. 

[Anfang](#top.md)



## Einen ViewProvider schreiben 

Ein Viewprovider ist die Komponente eines Objekts, die eine visuelle Darstellung in der 3D-Ansicht ermöglicht. FreeCAD verwendet eine Anwendungsstruktur, die die Daten (das „Modell") von ihrer visuellen Darstellung (der „Ansicht") trennt. Wenn du schon einmal mit FreeCAD in Python gearbeitet hast, bist du dir dessen wahrscheinlich bereits durch die Verwendung der beiden Python-Kernmodule `FreeCAD` und `FreeCADGui` (oft als `App` bzw. `Gui` bezeichnet) bewusst.

Unser FeaturePython-Objekt erfordert auch diese Elemente. Bisher haben wir uns ausschließlich auf den „Modell"-Teil des Codes konzentriert, jetzt ist es an der Zeit, den „Ansicht"-Teil zu schreiben. Glücklicherweise sind die meisten ViewProvider einfach und erfordern wenig Schreibaufwand, zumindest für den Anfang. Hier ist ein Beispiel-ViewProvider, der von [1](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py) übernommen und leicht modifiziert wurde:


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

Im obigen Code definieren wir ein XMP-Symbol für dieses Objekt. Die Symbolgestaltung geht über den Rahmen dieses Tutorials hinaus, aber die grundlegende Gestaltung kann mit Open-Source-Tools wie [GIMP](https://www.gimp.org), [Krita](https://krita.org/en/) und [Inkscape](https://inkscape.org/) verwaltet werden. Die Methode `getIcon()` ist optional. FreeCAD verwendet ein Standardsymbol, wenn diese Methode nicht bereitgestellt wird.

Fügen Sie den ViewProvider-Code am Ende von **box.py** hinzu und fügen Sie in der Methode `create()` die folgende Zeile über der Anweisung `recompute()` ein:


```python
ViewProviderBox(obj.ViewObject)
```

Dies instanziiert die benutzerdefinierte ViewProvider-Klasse und übergibt ihr das integrierte ViewObject von FeaturePython. Wenn die ViewProvider-Klasse initialisiert wird, speichert sie einen Verweis auf sich selbst im Attribut `ViewObject.Proxy` von FeaturePython. Auf diese Weise kann FreeCAD, wenn es unsere Box visuell darstellen muss, die ViewProvider-Klasse finden, um dies zu tun.

Speichere nun die Änderungen und kehre zu FreeCAD zurück. Importiere oder lade das Box-Modul neu und rufe `box.create()` auf. Du solltest jetzt zwei Dinge sehen:

-   Das Symbol für das Box-Objekt hat sich geändert.
-   Und, was noch wichtiger ist, es gibt eine Box in der 3D-Ansicht. Wenn du sie nicht sehen kannst, drücke die Schaltfläche **<img src="images/Std_ViewFitAll.svg" width=16px> [Std ViewFitAll](Std_ViewFitAll.md)**. Du kannst sogar die Abmessungen der Box ändern, indem du die Werte im [Eigenschafteneditor](Property_editor/de.md) änderst. Probiere es aus!

[Anfang](#top.md)



## Ereignisfallen

Wir haben bereits das Event Trapping besprochen. Fast jede Methode einer FeaturePython-Klasse dient als Callback, auf den das FeaturePython-Objekt zugreifen kann (das über das `Proxy`-Attribut Zugriff auf unsere Klasseninstanz erhält).

Unten finden Sie eine Liste der Rückrufe, die im grundlegenden FeaturePython-Objekt implementiert werden können:

++++
|                             | Wird während der Neuberechnung von Dokumenten aufgerufen                                             | Rufe `recompute()` nicht von dieser Methode aus auf (oder von einer Methode, die von `execute()` aufgerufen wird), da dies eine verschachtelte Neuberechnung verursacht.                                                                                                                                                                                                                 |
| `execute(self, obj)`              |                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                         |                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                        |
++++
|                             | Wird aufgerufen, bevor ein Eigenschaftswert geändert wird                                            |                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `onBeforeChange(self, obj, prop)` |                                                                                                      | `prop`                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                         |                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                            |                                                                                                      | ist der Name der zu ändernden Eigenschaft, nicht das Eigenschaftsobjekt selbst. Eigenschaftsänderungen können nicht abgebrochen werden. Vorherige/nächste Eigenschaftswerte stehen nicht gleichzeitig zum Vergleich zur Verfügung.                                                                                                                                                                                                     |
++++
|                             | Wird aufgerufen, nachdem eine Eigenschaft geändert wurde                                             |                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `onChanged(self, obj, prop)`      |                                                                                                      | `prop`                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                         |                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                            |                                                                                                      | ist der Name der zu ändernden Eigenschaft, nicht das Eigenschaftsobjekt selbst.                                                                                                                                                                                                                                                                                                                                                        |
++++
|                             | Wird aufgerufen, nachdem ein Dokument wiederhergestellt oder ein FeaturePython-Objekt kopiert wurde. | Gelegentlich können Verweise auf das FeaturePython-Objekt aus der Klasse oder die Klasse aus dem FeaturePython-Objekt beschädigt sein, da die Klassenmethode `__init__()` nicht aufgerufen wird, wenn das Objekt rekonstruiert wird. Das Hinzufügen von `self.Object <nowiki>=</nowiki> obj` oder `obj.Proxy <nowiki>=</nowiki> self` löst diese Probleme häufig. |
| {{Incode|onDocumentRestored(self, obj)}}   |                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                         |                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                        |
++++

: FeaturePython-Basisrückrufe

Eine vollständige Referenz der verfügbaren FeaturePython-Methoden findest du unter [FeaturePython-Methoden](FeaturePython_methods/de.md).

Darüber hinaus gibt es in der ViewProvider-Klasse zwei Callbacks, die sich gelegentlich als nützlich erweisen können:

++++
|                         | Wird aufgerufen, nachdem eine Dateneigenschaft (Modelleigenschaft) geändert wurde |                                                                                                                                                                                          |
| `updateData(self, obj, prop)` |                                                                                   | `obj`                                                                                                                                                                                          |
|                                     |                                                                                   |                                                                                                                                                                                                      |
|                                        |                                                                                   | ist ein Verweis auf die FeaturePython-Klasseninstanz, nicht auf die ViewProvider-Instanz. `prop` ist der Name der zu ändernden Eigenschaft, nicht das Eigenschaftsobjekt selbst. |
++++
|                         | Wird aufgerufen, nachdem eine Ansichtseigenschaft geändert wurde                  |                                                                                                                                                                                          |
| `onChanged(self, vobj, prop)` |                                                                                   | `vobj`                                                                                                                                                                                         |
|                                     |                                                                                   |                                                                                                                                                                                                      |
|                                        |                                                                                   | ist ein Verweis auf die ViewProvider-Instanz. `prop` ist der Name der Ansichtseigenschaft, die geändert wurde.                                                                   |
++++

: Grundlegende ViewProvider-Rückrufe

Es kommt nicht selten vor, dass die Python-Rückrufe nicht wie vorgesehen ausgelöst werden. Anfänger auf diesem Gebiet können sicher sein, dass das FeaturePython-Rückrufsystem nicht fehleranfällig oder defekt ist. Wenn Rückrufe nicht ausgeführt werden, liegt dies immer daran, dass eine Referenz im zugrunde liegenden Code verloren gegangen oder nicht definiert ist. Wenn Rückrufe jedoch scheinbar ohne Erklärung abgebrochen werden, kann das Bereitstellen von Objekt-/Proxy-Referenzen im `onDocumentRestored()`-Rückruf (wie in der ersten Tabelle oben angegeben) diese Probleme lindern. Bis Sie mit dem Rückrufsystem vertraut sind, kann es sinnvoll sein, in jeden Rückruf Druckanweisungen einzufügen, um während der Entwicklung Nachrichten auf der Konsole auszugeben.

[Anfang](#top.md)



## Vollständiger Code 


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

[Anfang](#top.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Create a FeaturePython object part II/de
