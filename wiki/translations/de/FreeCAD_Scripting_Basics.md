# FreeCAD Scripting Basics/de
{{TOCright}}

## Python skripten in FreeCAD 

FreeCAD wurde von Grund auf neu entwickelt, um vollständig von Python Skripten gesteuert zu werden. Nahezu alle Teile von FreeCAD, wie z.B. die Oberfläche, die Szeneninhalte und sogar die Darstellung dieser Inhalte in den 3D Ansichten, sind über den eingebauten Python Interpreter oder über eigene Skripte zugänglich. Damit ist FreeCAD wahrscheinlich eine der am weitesten anpassbaren Engineering Anwendungen, die heute verfügbar sind.

Wenn du nicht mit Python vertraut bist, empfehlen wir dir, nach Tutorien im Internet zu suchen, um so einen kurzen Blick auf seine Struktur zu bekommen. Python ist eine sehr einfache Sprache zu lernen, vor allem, weil es innerhalb eines Interpreters ausgeführt werden kann, wobei von einfachen Befehlen bis zu vollständigen Programmen alles dynamisch ausgeführt werden kann. Wenn du das Fenster mit der Aufschrift \"Python Konsole\", wie unten dargestellt nicht siehst, kannst du es unter **Ansicht → Paneele → Python Konsole** aktivieren.

### Der Interpreter 

Über den Interpreter, können Sie auf alle Ihre systeminstallierten Python-Module zugreifen, sowie die eingebaute FreeCAD Module und alle zusätzlichen Module, die Sie später installiert haben. Der folgende Screenshot zeigt den Python-Interpreter:

![Der FreeCAD Python Interpreter](images/screenshot_pythoninterpreter.jpg )

Vom Interpreter aus kannst du Python Code ausführen und durch die verfügbaren Klassen und Funktionen blättern. FreeCAD bietet einen sehr handlichen Klassenbrowser zur Erkundung der FreeCAD Welt: Wenn du den Namen einer bekannten Klasse gefolgt von einem Punkt eingibst (d.h. wenn du etwas von dieser Klasse hinzufügen möchtest), öffnet sich ein Klassenbrowser Fenster, in dem du zwischen den verfügbaren Unterklassen und Methoden navigieren kannst. Wenn du etwas auswählst, wird ein zugehöriger Hilfetext (falls vorhanden) angezeigt:

![The FreeCAD class browser](images/screenshot_classbrowser.jpg )

Beginne also hier mit der Eingabe von `App.` oder `Gui.` und schau was passiert. Eine andere, allgemeinere Python Methode, um den Inhalt von Modulen und Klassen zu untersuchen, ist die Verwendung des `print(dir())` Befehls. Wenn du beispielsweise `print(dir())` eingibst, werden alle derzeit in FreeCAD geladenen Module aufgelistet. `print(dir(App))` zeigt dir alles innerhalb des App Moduls usw.

Eine weitere nützliche Funktion des Interpreters ist die Möglichkeit, zurück zu gehen in der Befehlshistorie und eine Zeile des Codes wiederzubekommen, den du bereits früher getippt hast. Um durch die Befehlshistorie zu navigieren, benutze einfach **Pfeil oben** or **Pfeil unten**.

Mit Rechtsklick im Interpreter Fenster hast du auch einige andere Optionen, wie z. B. Kopie der gesamten Historie (nützlich, wenn du mit Dingen experimentieren möchtest, bevor du ein vollständiges Skript davon erstellst), oder füge einen Dateinamen mit vollständigem Pfad ein. {{Top}}

### Python Hilfe 

Im FreeCAD **Hilfe** findest Du einen mit **Automatische Python Moduldokumentation** beschrifteten Eintrag, der ein Browserfenster öffnet, das eine vollständige, in Echtzeit generierte Dokumentation aller dem FreeCAD Interpreter zur Verfügung stehenden Python Module enthält, einschließlich Python- und FreeCAD Einbaumodule, systeminstallierte Module und FreeCAD Zusatzmodule. Die dort verfügbare Dokumentation hängt davon ab, wie viel Aufwand jeder Modulentwickler in die Dokumentation seines Codes gesteckt hat, aber normalerweise haben Python Module den Ruf, ziemlich gut dokumentiert zu sein. Dein FreeCAD Fenster muss geöffnet bleiben, damit dieses Dokumentationssystem funktioniert. Der Eintrag **Python Skripten Dokumentation** gibt dir einen schnelle Verknüpfung zum [Vielnutzer Verteiler](Power_users_hub/de.md) Wiki Bereich. {{Top}}

## Eingebaute Module 

Da FreeCAD für den Betrieb ohne grafische Benutzeroberfläche (GUI) konzipiert ist, ist fast die gesamte Funktionalität in zwei Gruppen unterteilt: Kernfunktionalität, genannt `App`, und GUI Funktionalität, genannt `Gui`. Diese beiden Module heißen daher App und Gui. Auf diese beiden Module kann auch von Skripten ausserhalb des Interpreters unter den Namen `FreeCAD` bzw. `FreeCADGui` zugegriffen werden.

-   Im `App` findest Du alles, was mit der Anwendung selbst zu tun hat, wie Methoden zum Öffnen oder Schließen von Dateien, und mit den Dokumenten, wie das Setzen des aktiven Dokuments oder das Auflisten seines Inhalts.

-   Im `Gui` Modul, wirst du Werkzeuge für den Zugriff und die Verwaltung von GUI Elementen finden, wie die Arbeitsbereiche und ihre Werkzeugleisten, und, noch interessanter, die grafische Darstellung aller FreeCAD Inhalte.

Eine Auflistung des Inhalts dieser Module ist nicht sehr nützlich, da sie mit der Entwicklung von FreeCAD recht schnell wachsen. Aber die beiden zur Verfügung gestellten Browsing Werkzeuge (der Klassenbrowser und die Python Hilfe) sollte dir jederzeit eine vollständige und aktuelle Dokumentation liefern. {{Top}}

### Die App und GUI Objekte 

Wie gesagt, in FreeCAD, wird alles zwischen Kern und Darstellung getrennt. Dazu gehören auch die 3D-Objekte. Sie können auf die Definition von Eigenschaften von Objekten (so genannte Features in FreeCAD) über das App Modul zugreifen, und die Art ändern, wie sie auf dem Schirm über das Gui Modul dargestellt werden. Zum Beispiel hat ein Würfel Eigenschaften, um ihn zu definieren, wie Breite, Länge, Höhe, die in einem App-Objekt gespeichert sind, und Darstellung-Eigenschaften, wie Flächen-Farbe, Zeichnen-Modus, die in einem entsprechenden GUI-Objekt gespeichert sind.

Diese Handlungsweise ermöglicht eine sehr breite Palette von Anwendungen, wie mit Algorithmen nur aem Teil der Definition von Features zu arbeiten, ohne die Notwendigkeit, sich um den visuellen Teil kümmern zu müssen, oder sogar den Inhalt des Dokumentes zu nichtgraphischen Anwendung, wie Listen, Spreadsheets, oder Element-Analysen umzuleiten.

Für jedes `App` Objekt in deinem Dokument gibt es ein entsprechendes `Gui` Objekt. Tatsächlich hat das Dokument selbst sowohl ein `App` als auch ein `Gui` Objekt. Dies gilt natürlich nur, wenn du FreeCAD mit seiner vollständigen Benutzeroberfläche ausführst. In der Befehlszeilenversion gibt es keine GUI, so dass nur `App` Objekte verfügbar sind. Beachte, dass der `Gui` Teil von Objekten jedes Mal neu erzeugt wird, wenn ein `App` Objekt als \"neu zu berechnen\" markiert wird (z. B. wenn sich einer seiner Parameter ändert), so dass alle direkt am `Gui` Objekt vorgenommenen Änderungen verloren gehen können.

Um auf den `App` Teil von etwas zuzugreifen, gib ein:


```python
myObject = App.ActiveDocument.getObject("ObjectName")
```

wobei `"ObjectName"` der Name deines Objektes ist. Du kannst auch eingeben:


```python
myObject = App.ActiveDocument.ObjectName
```

Um auf den `Gui` Teil desselben Objekts zuzugreifen, gib ein:


```python
myViewObject = Gui.ActiveDocument.getObject("ObjectName")
```

wobei `"ObjectName"` der Name deines Objektes ist. Du kannst auch eingeben:


```python
myViewObject = App.ActiveDocument.ObjectName.ViewObject
```

Wenn du dich im Befehlszeilenmodus befindest und keine GUI hast, wird in der letzten Zeile `None` zurückgegeben. {{Top}}

### Die Dokument Objekte 

In FreeCAD befindet sich deine gesamte Arbeit in Dokumenten. Ein Dokument enthält deine Geometrie und kann in einer Datei gespeichert werden. Mehrere Dokumente können gleichzeitig geöffnet werden. Das Dokument hat, wie die darin enthaltene Geometrie `App` und `Gui` Objekte. Das `App` Objekt die verschiedenen Ansichten deines Dokuments enthält. Du kannst mehrere Fenster öffnen, von denen jedes deine Arbeit mit einem anderen Zoomfaktor oder aus einer anderen Richtung betrachtet. Diese Ansichten sind alle Teil deines `Gui` Dokument Objekts.

Um auf den `App` Teil des aktuell geöffneten (aktiven) Dokuments zuzugreifen, gib ein:


```python
myDocument = App.ActiveDocument
```

Um ein neues Dokument zu erstellen, gib ein:


```python
myDocument = App.newDocument("Document Name")
```

Um auf den `Gui` Teil des aktuell geöffneten (aktiven) Dokuments zuzugreifen, gib ein:


```python
myGuiDocument = Gui.ActiveDocument
```

Um auf die aktuelle Ansicht zuzugreifen, gib ein:


```python
myView = Gui.ActiveDocument.ActiveView
```


{{Top}}

## Das Verwenden zusätzlicher Module 

Die `FreeCAD` und `FreeCADGui` Module sind ausschließlich Verantwortlich für das Erstellen und Verwalten von Objekten in einem FreeCAD Dokument. Sie tun eigentlich nichts mehr, wie zum Beispiel Geometrie erstellen oder verändern. Das liegt daran, dass diese Geometrie aus mehreren Typen bestehen kann und daher zusätzliche Module erfordert, die jeweils für die Verwaltung eines bestimmten Geometrietyps zuständig ist. Beispielsweise ist der [Part-Arbeitsbereich](Part_Workbench/de.md) unter Verwendung des OpenCascade Kernels in der Lage, Geometrie vom Typ [BRep](http://en.wikipedia.org/wiki/Boundary_representation) zu erstellen und zu verändern. Wohingegen der [Netz-Arbeitsbereich](Mesh_Workbench/de.md) in der Lage ist, Netzobjekte zu erstellen und zu modifizieren. Auf diese Weise ist FreeCAD in der Lage, eine Vielzahl von Objekttypen zu handhaben, die alle im selben Dokument koexistieren können, und neue Typen können in Zukunft leicht hinzugefügt werden. {{Top}}

### Erzeugen von Objekten 

Jedes Modul hat seine eigene Art, mit Geometrie umzugehen, aber eine Sache, die sie normalerweise alle tun können, ist, Objekte im Dokument zu erstellen. Das FreeCAD Dokument kennt aber auch die verfügbaren Objekttypen, die von den Modulen bereitgestellt werden:


```python
FreeCAD.ActiveDocument.supportedTypes()
```

listet alle möglichen Objekte auf, die du erstellen kannst. Lass uns zum Beispiel ein Netz (gehandhabt vom Modul `Mesh`) und ein Teil (gehandhabt vom Modul `Part`) erstellen:


```python
myMesh = FreeCAD.ActiveDocument.addObject("Mesh::Feature", "myMeshName")
myPart = FreeCAD.ActiveDocument.addObject("Part::Feature", "myPartName")
```

Das erste Argument ist der Objekttyp, das zweite der Name des Objekts. Unsere beiden Objekte sehen fast gleich aus: Sie enthalten noch keine Geometrie, und die meisten ihrer Eigenschaften sind die gleichen, wenn du sie mit `dir(myMesh)` und `dir(myPart)` inspizierst. Mit einer Ausnahme `myMesh` hat eine `Mesh` Eigenschaft und `myPart` hat eine `Shape` Eigenschaft. Dort werden die Netz und Teildaten gespeichert werden. Lass uns zum Beispiel einen `Part` Würfel erstellen und speichern ihn in unserem `myPart` Objekt:


```python
import Part
cube = Part.makeBox(2, 2, 2)
myPart.Shape = cube
```

Du könntest versuchen, den Würfel innerhalb der `Mesh` Eigenschaft des `myMesh` Objekts zu speichern, aber es wird ein Fehler zurückgegeben. Das liegt daran, dass jede Eigenschaft dazu gemacht ist, nur einen bestimmten Typ zu speichern. In einer `Mesh` Eigenschaft kannst du nur Dinge speichern, die mit dem `Mesh` Modul erstellt wurden. Beachte, dass die meisten Module auch eine Verknüpfung zum Hinzufügen ihrer Geometrie zum Dokument haben:


```python
import Part
cube = Part.makeBox(2, 2, 2)
Part.show(cube)
```


{{Top}}

### Ändern von Objekten 

Das Ändern eines Objekts erfolgt auf die gleiche Weise:


```python
import Part
cube = Part.makeBox(2, 2, 2)
myPart.Shape = cube
```

Nun wollen wir die Form durch eine größere verändern:


```python
biggercube = Part.makeBox(5, 5, 5)
myPart.Shape = biggercube
```


{{Top}}

### Abfragen von Objekten 

Du kannst dir jederzeit den Typ eines solchen Objekts ansehen:


```python
myObj = FreeCAD.ActiveDocument.getObject("myObjectName")
print(myObj.TypeId)
```

oder prüfe, ob ein Objekt von einem der Basisobjekte (Part Formelement, Netz Formelement usw.) abgeleitet ist:


```python
print(myObj.isDerivedFrom("Part::Feature"))
```

Jetzt kannst du wirklich anfangen, mit FreeCAD zu spielen! Eine vollständige Liste der verfügbaren Module und ihrer Werkzeuge findest du im [<img src="images/Property.png" style="width:16px"> API](:Category_API.md) Abschnitt. {{Top}}





{{Powerdocnavi

}}

[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Python Code](Category_Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > FreeCAD Scripting Basics/de
