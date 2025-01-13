# Create a FeaturePython object part I/de
## Einführung

FeaturePython-Objekte (auch als [Skriptgenerierte Objekte](Scripted_objects/de.md) bezeichnet) bieten die Möglichkeit, FreeCAD mit Objekten zu erweitern, die sich nahtlos in die FreeCAD-Struktur integrieren.

Das ermutigt:

-   Schnelle Prototypenerstellung von neuen Objekten und Werkzeugen mit benutzerdefinierten Python-Klassen.
-   Speichern und Wiederherstellen von Daten (auch als Serialisierung bekannt) durch `App::Property`-Objekte, ohne dass ein Skript in die FreeCAD-Dokumentdatei eingebettet wird.
-   Kreative Freiheit, FreeCAD für jede Aufgabe anzupassen.

Auf dieser Seite werden wir ein funktionierendes Beispiel für eine benutzerdefinierte FeaturePython-Klasse konstruieren, wobei wir alle wichtigen Komponenten identifizieren und ein Verständnis dafür gewinnen, wie alles funktioniert, während wir vorankommen.



## Wie funktioniert es? 

FreeCAD wird mit einer Reihe von standard Objekttypen zur Verwaltung verschiedener Arten von Geometrie ausgeliefert. Einige von ihnen haben \"FeaturePython\"-Alternativen, die eine Anpassung mit einer benutzerdefinierten Python-Klasse ermöglichen.

Diese benutzerdefinierte Python-Klasse nimmt einen Verweis auf eines dieser Objekte und modifiziert es. Zum Beispiel kann die Python-Klasse dem Objekt Eigenschaften hinzufügen oder es mit anderen Objekten verknüpfen. Außerdem kann die Python-Klasse bestimmte Methoden implementieren, um das Objekt in die Lage zu versetzen, auf Dokumentereignisse zu reagieren, wodurch es möglich wird, Änderungen von Objekteigenschaften und Neuberechnungen von Dokumenten abzufangen.

Bei der Arbeit mit benutzerdefinierten Klassen und FeaturePython-Objekten ist es wichtig zu wissen, dass die benutzerdefinierte Klasse und ihr Zustand nicht im Dokument gespeichert werden, da dies die Einbettung eines Skripts in eine FreeCAD-Dokumentdatei erfordern würde, was ein erhebliches Sicherheitsrisiko darstellen würde. Nur das FeaturePython-Objekt selbst wird gespeichert (serialisiert). Da aber der Pfad des Skriptmoduls im Dokument gespeichert ist, muss ein Benutzer nur den Code der benutzerdefinierten Python-Klasse als importierbares Modul installieren und dabei der gleichen Ordnerstruktur folgen, um die verlorene Funktionalität wiederzuerlangen.

[Anfang](#top.md)



## Einrichten der Dinge 

FeaturePython-Objektklassen müssen in FreeCAD als importierbare Module fungieren. Das bedeutet, dass du sie in einem Pfad platzieren musst, der in deiner Python Umgebung existiert (oder füge ihn speziell hinzu). Für die Zwecke dieses Tutoriums werden wir den FreeCAD-Benutzerordner Macro verwenden. Aber wenn du eine andere Idee im Kopf hast, kannst du diese stattdessen verwenden.

Wenn du nicht weißt, wo sich der FreeCAD Macro-Ordner befindet, gib `FreeCAD.getUserMacroDir(True)` in die [Python-Konsole](Python_console.md) von FreeCAD ein:

-   Unter Linux ist es normalerweise **/home/<username>/.local/share/FreeCAD/Macro/** (<small>(v0.20)</small> ) oder **/home/<username>/.FreeCAD/Macro/** ({{VersionMinus|0.19}}).
-   Unter Windows ist es **%APPDATA%\FreeCAD\Macro\**, was normalerweise **C:\Users\<username>\Appdata\Roaming\FreeCAD\Macro\** ist.
-   Unter macOS ist es normalerweise **/Users/<username>/Library/Application Support/FreeCAD/Macro/**.

Jetzt müssen wir einige Ordner und Dateien erstellen:

-   Erstelle im Ordner **Macro** einen neuen Ordner namens **fpo**.
-   Erstelle im Ordner **fpo** eine leere Datei: **__init__.py**.
-   Erstelle im Ordner **fpo** einen neuen Ordner namens **box**.
-   Erstelle im Ordner **box** zwei Dateien: **__init__.py** und **box.py** (lasse beide vorerst leer).

Deine Ordnerstruktur sollte folgendermaßen aussehen:

Macro/
    |--> fpo/
        |--> __init__.py
        |--> box/
            |--> __init__.py
            |--> box.py

Der Ordner **fpo** eignet sich gut zum Spielen mit neuen FeaturePython-Objekten und der Ordner **box** ist das Modul, in dem wir arbeiten werden. **__init__.py** teilt Python mit, dass sich im Ordner ein importierbares Modul befindet und **box.py** wird die Klassendatei für unser neues FeaturePython-Objekt sein.

Nachdem wir unsere Modulpfade und Dateien erstellt haben, stellen wir sicher, dass FreeCAD richtig eingerichtet ist:

-   Starte FreeCAD (falls du dies noch nicht getan hast).
-   Aktiviere die [Berichtsansicht](Report_view.md) (**Ansicht → Bedienfelder → Berichtsansicht**).
-   Aktiviere die [Python-Konsole](Python_console.md) (**Ansicht → Bedienfelder → Python-Konsole**), siehe [Grundlagen der FreeCAD-Skripterstellung](FreeCAD_Scripting_Basics.md).

Navigiere abschließend zum Ordner **Macro/fpo/box** und öffne **box.py** in deinem bevorzugten Code-Editor. Wir werden nur diese Datei bearbeiten.

[Anfang](#top.md)



## Ein FeaturePython-Objekt 

Beginnen wir mit dem Schreiben unserer Klasse und ihres Konstruktors:


```python
class box():

    def __init__(self, obj):
        """
        Default constructor
        """

        self.Type = 'box'

        obj.Proxy = self
```

**Die Aufschlüsselung der `__init__()`-Methode:**

\'{\|class=\"wikitable\" cellpadding=\"5px\" width=\"100%\" \|style=\"width:25%\" \| `def __init__(self, obj):` \|style=\"width:75%\" \| Parameter beziehen sich auf die Python-Klasse selbst und das FeaturePython-Objekt, an das sie angehängt ist. \|- \| `self.Type <nowiki>=</nowiki> 'box'` \| String-Definition des benutzerdefinierten Python-Typs. \|- \| `obj.Proxy <nowiki>=</nowiki> self` \| Speichert einen Verweis auf die Python-Instanz im FeaturePython-Objekt. \|}

Füge oben in der Datei den folgenden Code hinzu:


```python
import FreeCAD as App

def create(obj_name):
    """
    Object creation method
    """

    obj = App.ActiveDocument.addObject('App::FeaturePython', obj_name)

    box(obj)

    return obj
```

A**Die Aufschlüsselung der `create()`-Methode:**

+++
|                                       | Standardimport für die meisten Python-Skripte, der App-Alias ​​ist nicht erforderlich.                                                                                                                                                                                                                    |
| `import FreeCAD as App`                     |                                                                                                                                                                                                                                                                                                         |
|                                                   |                                                                                                                                                                                                                                                                                                         |
+++
|                                       | Erstellt ein neues FreeCAD FeaturePython-Objekt mit dem an die Methode übergebenen Namen. Wenn es keine Namenskollision gibt, sind dies die Bezeichnung und der Name des erstellten Objekts. Andernfalls werden ein eindeutiger Name und eine eindeutige Bezeichnung basierend auf „obj_name" erstellt. |
| `obj <nowiki>=</nowiki> ... addObject(...)` |                                                                                                                                                                                                                                                                                                         |
|                                                   |                                                                                                                                                                                                                                                                                                         |
+++
|                                       | Erstellt unsere benutzerdefinierte Klasseninstanz.                                                                                                                                                                                                                                                      |
| `box(obj)`                                  |                                                                                                                                                                                                                                                                                                         |
|                                                   |                                                                                                                                                                                                                                                                                                         |
+++
|                                       | Gibt das FeaturePython-Objekt zurück.                                                                                                                                                                                                                                                                   |
| `return obj`                                |                                                                                                                                                                                                                                                                                                         |
|                                                   |                                                                                                                                                                                                                                                                                                         |
+++

Die Methode `create()` ist nicht erforderlich, bietet aber eine gute Möglichkeit, den Code zur Objekterstellung zu kapseln.

[Anfang](#top.md)



### Testen des Codes 

Jetzt können wir unser neues Objekt testen. Speichere deinen Code und kehre zu FreeCAD zurück. Stelle sicher, dass du ein neues Dokument geöffnet hast. Du kannst dies tun, indem du **Ctrl**+**N** drückst oder **File → New** auswählst.

Gib in der Python-Konsole Folgendes ein:


```python
from fpo.box import box
```

Jetzt müssen wir unser Objekt erstellen:


```python
mybox = box.create('my_box')
```

![ right](images/Fpo_treeview.png ) Du solltest ein neues Objekt in der [Baumansicht](Tree_view.md) mit der Bezeichnung „my_box" erscheinen sehen.

Beachte, dass das Symbol grau ist. FreeCAD teilt uns mit, dass das Objekt in der [3D-Ansicht](3D_view.md) nichts anzeigen kann. Klicke auf das Objekt und sieh dir seine Eigenschaften im [Eigenschafteneditor](Property_editor.md) an. Dort steht nicht viel, nur der Name des Objekts.

Beachte auch, dass sich in der Strukturansicht neben dem FeaturePython-Objekt ein kleines blaues Häkchen befindet. Das liegt daran, dass ein Objekt beim Erstellen oder Ändern „berührt" wird und neu berechnet werden muss. Dies wird durch Drücken der Schaltfläche **<img src="images/Std_Refresh.svg" width=16px> [Std Refresh](Std_Refresh.md)** erreicht. Wir werden später etwas Code hinzufügen, um dies zu automatisieren.





Schauen wir uns die Attribute unseres Objekts an: 
```python
dir(mybox)
```

Das Ergebnis ist:


```python
['Content', 'Document', 'ExpressionEngine', 'FullName', 'ID', 'InList',
...
'setPropertyStatus', 'supportedProperties', 'touch']
```

Es gibt viele Attribute, weil wir auf das native FreeCAD FeaturePyton-Objekt zugreifen, das in der ersten Zeile unserer `create()`-Methode erstellt wurde. Die `Proxy`-Eigenschaft, die wir in unserer `__init__()`-Methode hinzugefügt haben, ist ebenfalls vorhanden.

Lass es uns mit der Methode `dir()` untersuchen:


```python
dir(mybox.Proxy)
```

Das Ergebnis ist:


```python
['Type', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
...
'__str__', '__subclasshook__', '__weakref__']
```

Wir können unsere `Type`-Eigenschaft sehen. Schauen wir sie uns an:


```python
mybox.Proxy.Type
```

Das Ergebnis ist:


```python
'box'
```

Dies ist tatsächlich der zugewiesene Wert, sodass wir wissen, dass wir über das FeaturePython-Objekt auf die benutzerdefinierte Klasse zugreifen.

Nun wollen wir sehen, ob wir unseren Unterricht etwas interessanter und vielleicht auch nützlicher gestalten können.

[oben](#oben.md)



### Hinzufügen von Eigenschaften 

Eigenschaften sind das Lebenselixier einer FeaturePython-Klasse. Glücklicherweise unterstützt FreeCAD [eine Reihe von Eigenschaftstypen](FeaturePython_Custom_Properties.md) für FeaturePython-Klassen. Diese Eigenschaften werden direkt an das FeaturePython-Objekt angehängt und beim Speichern der Datei vollständig serialisiert. Um zu vermeiden, dass Sie Daten selbst serialisieren müssen, ist es ratsam, nur diese Eigenschaftstypen zu verwenden.

Das Hinzufügen von Eigenschaften erfolgt mit der Methode `add_property()`. Die Syntax für die Methode lautet:

add_property(type, name, section, description)

Du kannst die Liste der unterstützten Eigenschaften anzeigen, indem du Folgendes eingibst:


```python
mybox.supportedProperties()
```

Versuchen wir, unserer Box-Klasse eine Eigenschaft hinzuzufügen. Wechsle zu deinem Code-Editor, gehe zur Methode `__init__()` und füge am Ende der Methode Folgendes hinzu:


```python
obj.addProperty('App::PropertyString', 'Description', 'Base', 'Box description').Description = ""
```

Beachte, dass wir den Verweis auf das (serialisierbare) FeaturePython-Objekt `obj` und nicht auf die (nicht serialisierbare) Python-Klasseninstanz `self` verwenden.

Wenn du fertig bist, speichere die Änderungen und wechsle zurück zu FreeCAD. Bevor wir die an unserem Code vorgenommenen Änderungen beobachten können, müssen wir das Modul neu laden. Dies kann durch einen Neustart von FreeCAD erreicht werden, aber ein Neustart von FreeCAD jedes Mal, wenn wir den Code bearbeiten, wäre unpraktisch. Um die Dinge einfacher zu machen, gib Folgendes in die Python-Konsole ein:


```python
from importlib import reload
reload(box)
```

Nachdem wir das Modul neu geladen haben, sehen wir uns an, was wir erhalten, wenn wir ein Objekt erstellen:


```python
box.create('box_property_test')
```

Du solltes das neue Boxobjekt in der Strukturansicht sehen:

-   Wähle es aus und sehe dir den Eigenschafteneditor an. Dort solltest du die Eigenschaft „Beschreibung" sehen.
-   Bewege den Mauszeiger über den Eigenschaftennamen auf der linken Seite und der Tooltip sollte mit der von dir angegebenen Beschreibung erscheinen.
-   Wähle das Feld aus und gib ein, was du möchtest. Du wirst feststellen, dass Python-Aktualisierungsbefehle ausgeführt und in der Konsole angezeigt werden, während du Buchstaben eingibst und sich die Eigenschaft ändert.

[Anfang](#top.md)

Lass uns noch einige weitere Eigenschaften hinzufügen. Kehre zu deinem Quellcode zurück und füge der Methode `__init__()` die folgenden Eigenschaften hinzu:


```python
obj.addProperty('App::PropertyLength', 'Length', 'Dimensions', 'Box length').Length = 10.0
obj.addProperty('App::PropertyLength', 'Width', 'Dimensions', 'Box width').Width = '10 mm'
obj.addProperty('App::PropertyLength', 'Height', 'Dimensions', 'Box height').Height = '1 cm'
```

Und fügen wir auch etwas Code hinzu, um das Dokument automatisch neu zu berechnen. Füge die folgende Zeile über der `return()`-Anweisung in der `create()`-Methode hinzu:


```python
App.ActiveDocument.recompute()
```

**Sei vorsichtig, wenn du ein FeaturePython-Objekt neu berechnest. Die Neuberechnung sollte von einer Methode außerhalb seiner Klasse durchgeführt werden.**

![ right](images/fpo_box_properties.png )

Teste nun deine Änderungen wie folgt:

-   Speichere deine Änderungen und lade dein Modul neu.
-   Lösche alle Objekte in der Strukturansicht.
-   Erstelle ein neues Box-Objekt aus der Python-Konsole, indem du `box.create('myBox')` aufrufst.

Sobald die Box erstellt ist und du überprüft hast, ob sie neu berechnet wurde, wähle das Objekt aus und sehe dir seine Eigenschaften an. Dabei solltest du zwei Dinge beachten:

-   Eine neue Eigenschaftengruppe: „Abmessungen".
-   Drei neue Eigenschaften: „Höhe", „Länge" und „Breite".

Beachte auch, dass die Eigenschaften Einheiten haben. Genauer gesagt haben sie die linearen Einheiten übernommen, die in den Benutzereinstellungen festgelegt sind (**Bearbeiten → Einstellungen... → Allgemein → Einheiten**). 


Sicherlich ist dir aufgefallen, dass für die Abmessungen drei verschiedene Werte eingegeben wurden: ein Gleitkommawert (`10.0`) und zwei verschiedene Zeichenfolgen (`'10 mm'` und `'1 cm'`). Der Typ `App::PropertyLength` geht davon aus, dass Gleitkommawerte in Millimetern vorliegen, Zeichenfolgenwerte werden gemäß den angegebenen Einheiten analysiert und in der GUI werden alle Werte in die in den Benutzereinstellungen angegebenen Einheiten konvertiert (`mm` im Bild). Aufgrund dieses integrierten Verhaltens ist der Typ `App::PropertyLength` ideal für Abmessungen.

[Anfang](#top.md)



### Ereignisse abfangen 

Das letzte für ein grundlegendes FeaturePython-Objekt erforderliche Element ist das Abfangen von Ereignisen. Ein FeaturePython-Objekt kann mit Rückruffunktionen auf Ereignisse reagieren. In unserem Fall möchten wir, dass das Objekt reagiert, wenn es neu berechnet wird. Mit anderen Worten, wir möchten Neuberechnungen abfangen. Um dies zu erreichen, müssen wir der Objektklasse eine Funktion mit einem bestimmten Namen, `execute()`, hinzufügen. Es gibt mehrere andere Ereignisse, die abgefangen werden können, sowohl im FeaturePython-Objekt selbst als auch im [ViewProvider](Viewprovider.md), die wir in [Erstellen eines FeaturePython-Objekts, Teil II](Create_a_FeaturePython_object_part_II.md) behandeln werden.

Eine vollständige Referenz der für die Implementierung in FeautrePython-Klassen verfügbaren Methoden findest du unter [FeaturePython-Methoden](FeaturePython_methods.md).

Füge nach der Funktion `__init__()` Folgendes hinzu:


```python
def execute(self, obj):
    """
    Called on document recompute
    """

    print('Recomputing {0:s} ({1:s})'.format(obj.Name, self.Type))
```

Teste den Code, indem du diese Schritte erneut ausführst:

-   Speichern und Modul neu laden.
-   Alle Objekte löschen.
-   Neues Box-Objekt erstellen.

Du solltest die gedruckte Ausgabe in der Python-Konsole sehen, dank des Aufrufs `recompute()`, den wir der Methode `create()` hinzugefügt haben. Natürlich tut die Methode `execute()` hier nichts, außer uns mitzuteilen, dass sie aufgerufen wurde, aber sie ist der Schlüssel zur Magie der FeaturePython-Objekte.

Das war es, du weißt jetzt, wie du ein einfaches, funktionales FeaturePython-Objekt erstellst!

[Anfang](#top.md)



### Vollständiger Code 


```python
import FreeCAD as App

def create(obj_name):
    """
    Object creation method
    """

    obj = App.ActiveDocument.addObject('App::FeaturePython', obj_name)

    box(obj)

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

        print('Recomputing {0:s} ({1:s})'.format(obj.Name, self.Type))
```

[Anfang](#top.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Create a FeaturePython object part I/de
