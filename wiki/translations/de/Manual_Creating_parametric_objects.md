# Manual:Creating parametric objects/de
{{Manual:TOC}}

Im [vorherigen Kapitel](Manual:Creating_and_manipulating_geometry/de.md) haben wir entdeckt, wie **Part**-Geometrie erstellt wird und wie sie auf dem Bildschirm dargestellt wird, indem sie einem \"dummen\" (nicht parametrischen) Dokumentobjekt zugeordnet wird. Dies ist zwar effektiv, wird aber umständlich, wenn man die Form ändern muss. Jede Änderung erfordert eine neue Form zu erstellen und dem Objekt zuzuordnen, und ergibt sich wiederholende und ineffektive Arbeitsabläufe.

Überall in diesem Handbuch haben wir gesehen, wie parametrischer Objekte diesem Problem begegnen, indem sie dynamische Aktualisierungen ermöglichen. wird eine einzelne Eigenschaft geändert, wird die Form automatisch neu berechnet; manuelle Aktualisierungen sind nich mehr erforderlich. Dieser Neuberechnungsprozess ermöglicht effizienteres Modellieren und führt zu Anpassbaren Konstruktionen. Intern arbeiten parametrischer Objekte ähnlich wie wir es schon zuvor gemacht haben: Sie berechnen den Inhalt ihrer Eigenschaft **Shape** neu, wann immer sich eine ihrer Eigenschaften ändert. Dieser iterative Prozess läuft ohne Unterbrechung und stellt sicher, dass das Objekt übereinstimmend mit seinen festgelegten Parametern bleibt.

FreeCAD stellt ein benutzerfreundliches System zur Erstellung parametrischer Objekte komplett in Python bereit. Diese Objekte werden unter Verwendung einer Python-Klasse erstellt, die:

-   Deklariert die notwendigen Eigenschaften für das Objekt.
-   Legt das Verhalten fest, wenn eine dieser Eigenschaften geändert wird.

Die Struktur solch eines parametrischen Objekts ist einfach:


```python
class myParametricObject:

    def __init__(self, obj):
        obj.Proxy = self
        obj.addProperty("App::PropertyFloat", "MyLength")
        ...

    def execute(self,obj):
        print ("Recalculating the shape...")
        print ("The value of MyLength is:")
        print (obj.MyLength)
        ...
```

Alle Python-Klasse besitzen üblicherweise eine Methode **\_\_init\_\_**. Diese Methode wird ausgeführt, wenn eine Klasse instanziiert wird, d.h. wenn ein Python-Objekt von dieser Klassen abgeleitet (erstellt) wird. Eine Klasse kann man sich als eine \"Vorlage\" oder Blaupause vorstellen, die zum Erstellen lebendiger Instanzen von sich selbst eingesetzt wird. Jede Instanz der Klasse wird zu einem unabhängigen Objekt mit seinen eigenen Attributen und Methoden. In unserer Methode **\_\_init\_\_** führen wir zwei wichtige Aufgaben aus:

-   Speichern Sie die Klasse selbst im Attribut **Proxy** des FreeCAD-Dokumentobjekts:

Indem wir dem Attribut **Proxy** des FreeCAD-Dokumentobjekts **self** zuweisen, verknüpfen wir die Logik unserer Python-Klasse mit dem FreeCAD-Objekt. Dies bedeutet, dass das Dokumentobjekt den Python-Klassencode in sich „trägt", sodass es sich gemäß der in der Klasse definierten Logik verhalten kann. Durch diese Verbindung weiß FreeCAD, wie es mit dem parametrischen Objekt interagieren und es neu berechnen soll.

-   Erstelle alle Eigenschaften, die das Objekt benötigt:

Mit der Methode **addProperty** definieren wir die benutzerdefinierten Eigenschaften, die das Objekt benötigt. Eigenschaften fungieren als Parameter oder Variablen für das Objekt und können im Eigenschafteneditor von FreeCAD aufgerufen, geändert und angezeigt werden. Im Beispiel fügen wir eine Gleitkomma-Eigenschaft namens **MyLength** hinzu. Diese Eigenschaft beeinflusst später die Form oder das Verhalten des Objekts.

In FreeCAD sind viele Arten von Eigenschaften verfügbar, von Gleitkommazahlen über Zeichenfolgen bis hin zu speziellen Typen für Geometrie und Materialien. Um die vollständige Liste der verfügbaren Eigenschaftstypen anzuzeigen, kannst du den folgenden Code in die Python-Konsole eingeben:


```python
FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "dummy").supportedProperties()
```

Der zweite Schlüsselbestandteil unserer Klasse ist die Methode **execute**. Diese Methode wird automatisch ausgelöst, wann immer das Objekt zum Neuberechnen gekennzeichnet wird, was passiert, sobald eine seiner Eigenschafen geändert wird. Die Methode **execute** befindet sich dort, wo alle Neuberechnungen für das Objekt und stattfinden und stellt so sicher, dass seine Form und sein Verhalten aktualisiert werden, um alle Änderungen widerzuspiegeln. Innerhalb der Methode **execute** werden alle nötigen Arbeitsabläufe zur Erstellung neuer Geometrie für ds Objekt ausgeführt. Üblicherweise ist dies mit Neuberechnung der Form auf Basis der aktuellen Werte seiner Eigenschaften verbunden und dann der Zuordnung der aktualisierten Form zum Attribut **Shape** des Objekts durch einen Ausdruck wie **obj.Shape = myNewShape**. Die Methode **execute** nimmt ein einziges Argument **obj** an, das das FreeCAD-Dokumentobjekt darstellt, dem das parametrischer Objekt zugeordnet ist. Dies ermöglicht, das Objekt direkt innerhalb der Methode zu bearbeiten, wie auf seine Eigenschaften zuzugreifen, seine Geometrie zu aktualisieren oder andere Arbeitsschritte auszuführen.

Zusammenfassend:

-   Die Methode **execute** wird aufgerufen, wenn das Objekt aktualisiert werden muss.
-   Sie ist für die Neuberechnung der Form und die Zuweisung zum Attribut **Shape** des Objekts verantwortlich.
-   Das Argument **obj** ermöglicht den Zugriff auf das FreeCAD-Dokumentobjekt, sodass du programmgesteuert Änderungen vornehmen kannst.

Mit diesem System übernimmt FreeCAD den Rest und stellt sicher, dass das Objekt im Dokument ordnungsgemäß aktualisiert und in der grafischen Benutzeroberfläche korrekt angezeigt wird.

Eine wichtige Sache, die du beachten solltest, ist, dass beim Erstellen parametrischer Objekte in einem FreeCAD-Dokument der Python-Code, der zum Definieren dieser Objekte verwendet wird, nicht in der Datei gespeichert wird. Dies ist eine absichtliche Sicherheitsmaßnahme. Wenn FreeCAD-Dateien Python-Code speichern dürften, könnte dies böswilligen Akteuren die Tür öffnen, Dateien mit schädlichen Skripten zu verteilen, die den Computer einer Person beschädigen könnten. Wenn du also eine FreeCAD-Datei mit parametrischen Objekten freigibst, die mit benutzerdefiniertem Python-Code erstellt wurden, muss der Empfänger auch Zugriff auf den Code haben, der zum Definieren dieser Objekte verwendet wurde. Ohne diesen Code weiß FreeCAD nicht, wie es die Objekte richtig neu berechnen oder mit ihnen interagieren soll.

Der einfachste Weg, dies sicherzustellen, besteht darin, den Python-Code in einer Makrodatei zu speichern. Wenn du deine FreeCAD-Datei verteilst, kannst du das Makro mit einschließen. Alternativ kannst du das Makro im [FreeCAD-Makro-Repository](Macros_recipes.md) freigeben, sodass andere es einfach herunterladen und verwenden können. Dieser Ansatz stellt sicher, dass deine benutzerdefinierten parametrischen Objekte auf anderen Systemen funktionsfähig bleiben und gleichzeitig die bewährten Sicherheitspraktiken eingehalten werden.

Im Folgenden machen wir eine kleine Übung, bei der wir ein parametrisches Objekt erstellen, das eine einfache parametrische rechteckige Fläche ist. Komplexere Beispiele findest du im [Beispiel für parametrische Objekte](Scripted_objects.md) und im [FreeCAD-Quellcode](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py) selbst.

Wir geben unserem Objekt zwei Eigenschaften: Länge und Breite, die wir verwenden, um ein Rechteck zu konstruieren. Da unser Objekt dann bereits eine vorgefertigte Platzierungseigenschaft hat (alle geometrischen Objekte haben standardmäßig eine, du musst sie nicht selbst hinzufügen), verschieben wir unser Rechteck an die in der Platzierung festgelegte Position/Rotation, sodass der Benutzer das Rechteck durch Bearbeiten der Platzierungseigenschaft überall hin verschieben kann.


```python
class ParametricRectangle:

    def __init__(self,obj):
        obj.Proxy = self
        obj.addProperty("App::PropertyFloat", "Length")
        obj.addProperty("App::PropertyFloat", "Width")

    def execute(self, obj):
        # We need to import the FreeCAD module here too, because we might be running out of the Console
        # (in a macro, for example) where the FreeCAD module has not been imported automatically:
        import FreeCAD
        import Part

        # First we need to make sure the values of Length and Width are not 0
        # otherwise Part.LineSegment will complain that both points are equal:
        if (obj.Length == 0) or (obj.Width == 0):
            # If yes, exit this method without doing anything:
            return

        # We create 4 points for the 4 corners:
        v1 = FreeCAD.Vector(0, 0, 0)
        v2 = FreeCAD.Vector(obj.Length, 0, 0)
        v3 = FreeCAD.Vector(obj.Length,obj.Width, 0)
        v4 = FreeCAD.Vector(0, obj.Width, 0)

        # We create 4 edges:
        e1 = Part.LineSegment(v1, v2).toShape()
        e2 = Part.LineSegment(v2, v3).toShape()
        e3 = Part.LineSegment(v3, v4).toShape()
        e4 = Part.LineSegment(v4, v1).toShape()

        # We create a wire:
        w = Part.Wire([e1, e2, e3, e4])

        # We create a face:
        f = Part.Face(w)

        # All shapes have a Placement too. We give our shape the value of the placement
        # set by the user. This will move/rotate the face automatically.
        f.Placement = obj.Placement

        # All done, we can attribute our shape to the object!
        obj.Shape = f
```

Anstatt den obigen Code in die Python-Konsole einzufügen, speichern wir ihn besser irgendwo, damit wir ihn später wiederverwenden und ändern können. Zum Beispiel in einem neuen Makro (Menü **Makro -\> Makros -\> Erstellen**). Nenne es zum Beispiel \"ParamRectangle\". FreeCAD-Makros werden jedoch mit der Erweiterung .FCMacro gespeichert, die Python beim Importieren nicht erkennt. Bevor wir den obigen Code verwenden, müssen wir also die Datei ParamRectangle.FCMacro in ParamRectangle.py umbenennen. Dies kannst du ganz einfach in deinem Datei-Explorer tun, indem du zum Ordner „Makros" navigierst, der im Menü „Extras -\> Makros" angegeben ist.

Sobald dies erledigt ist, können wir Folgendes in der Python-Konsole tun:


```python
import ParamRectangle
```

Indem wir den Inhalt von ParamRectangle untersuchen, können wir überprüfen, ob es unsere ParametricRectangle-Klasse enthält.

Um ein neues parametrisches Objekt mit unserer Klasse ParametricRectangle zu erstellen, verwenden wir den folgenden Code. Beachte, dass wir **Part::FeaturePython** anstelle von **Part::Feature** verwenden, das wir in den vorherigen Kapiteln verwendet haben (die Python-Version ermöglicht es, unser eigenes parametrisches Verhalten zu definieren):


```python
myObj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", "Rectangle")
ParamRectangle.ParametricRectangle(myObj)
myObj.ViewObject.Proxy = 0 # This is mandatory unless we code the ViewProvider too.
FreeCAD.ActiveDocument.recompute()
```

Hier ist eine kurze Aufschlüsselung der vorherigen Befehle:

-   **myObj = FreeCAD.ActiveDocument.addObject(\"Part::FeaturePython\", \"Rectangle\")**: Erstellt ein neues **Part::FeaturePython**-Objekt mit dem Namen **Rectangle** im aktiven FreeCAD-Dokument. Dieses Objekt ist speziell für benutzerdefiniertes parametrisches Verhalten konzipiert und ermöglicht es einer von Python definierten Logik, seine Eigenschaften und sein Verhalten zu verwalten.

-   **ParamRectangle.ParametricRectangle(myObj)**: Initialisiert das Objekt, indem es mit der Klasse **ParametricRectangle** aus dem Modul oder Skript **ParamRectangle** verknüpft wird. Dadurch wird die benutzerdefinierte, von Python definierte Logik mit dem Objekt verknüpft, sodass es als parametrisches Objekt fungieren kann.

-   **myObj.ViewObject.Proxy = 0**: Setzt das Attribut **ViewObject.Proxy** auf 0 zurück und stellt sicher, dass das Objekt die Standardansichtsbehandlung von FreeCAD verwendet. Dieser Schritt ist erforderlich, sofern du keinen benutzerdefinierten ViewProvider definierst, um die visuelle Darstellung des Objekts zu verwalten.

-   **FreeCAD.ActiveDocument.recompute()**: Berechnet das Dokument neu, um die Geometrie zu aktualisieren und Änderungen in der grafischen Benutzeroberfläche von FreeCAD widerzuspiegeln, wodurch das neue Objekt vollständig sichtbar und funktionsfähig wird.

Auf dem Bildschirm wird noch nichts angezeigt, da die Eigenschaften **Länge** und **Breite** 0 sind, was unsere \"do-nothing\"-Bedingung innerhalb der Ausführung auslöst. Wir müssen nur die Werte für Länge und Breite ändern, und unser Objekt wird wie von Zauberhand erscheinen und sofort neu berechnet.

Natürlich wäre es mühsam, diese 4 Zeilen Python-Code jedes Mal eingeben zu müssen, wenn wir ein neues parametrisches Rechteck erstellen möchten. Eine sehr einfache Möglichkeit, dies zu lösen, besteht darin, die obigen 4 Zeilen in unserer Datei **ParamRectangle.py** am Ende nach dem Ende der Klasse **ParametricRectange** einzufügen (wir können dies vom Makro-Editor aus tun).

Wenn wir nun import ParamRectangle eingeben, wird automatisch ein neues parametrisches Rechteck erstellt. Noch besser ist es, wenn wir eine Symbolleistenschaltfläche hinzufügen, die genau das tut:

-   Öffne das Menü **Tools -\> Anpassen**
-   Wähle unter der Registerkarte „Makros" unser Makro ParamRectangle.py aus, gib die gewünschten Details ein und klicke auf „Hinzufügen":

![](images/FreeCAD_python_macroRec.png )

-   Erstelle unter der Registerkarte „Symbolleisten" eine neue benutzerdefinierte Symbolleiste im Workbench deiner Wahl (oder global), wähle dein Makro aus und fügen es der Symbolleiste hinzu:

![](images/FreeCAD_python_toolbarCus.png )

-   Das war es, wir haben jetzt eine neue Symbolleistenschaltfläche, die beim Anklicken ein parametrisches Rechteck erstellt.

Denke daran: Wenn du mit diesem neuen Tool erstellte Dateien an andere Personen verteilen möchtest, muss auf deren Computern auch das Makro **ParamRectangle.py** installiert sein.

**Mehr lesen**

-   [Das FreeCAD-Makro-Repository](Macros_recipes.md)
-   [Beispiel für parametrisches Objekt](Scripted_objects.md)
-   [Weitere Beispiele im FreeCAD-Code](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/TemplatePyMod/FeaturePython.py)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:Creating parametric objects/de
