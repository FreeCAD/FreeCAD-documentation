# Manual:A gentle introduction/de
{{Manual:TOC}}

[Python](https://de.wikipedia.org/wiki/Python_(Programmiersprache)) ist eine weitverbreitete, quelloffene Programmiersprache, die man an ihrer Einfachheit, Vielseitigkeit und Lesbarkeit erkennt. Sie ist oft als Skriptsprache in Anwendungen eingebettet und FreeCAD ist da keine Ausnahme. Diese Integration ermöglicht Anwendern Aufgaben zu automatisieren, Arbeitsabläufe anzupassen und die Funktionalität der Software weit über die grafische Schnittstelle hinaus zu erweitern.

Python bietet einige Vorteile, die es besonders für FreeCAD-Anwender interessant macht. Es ist Anfängerfreundlich mit einer intuitiven Syntax, die das Erlernen vereinfacht, sogar für diejenigen, die noch keine Programmiererfahrung besitzen. Diese gute Zugänglichkeit ist besonders wertvoll für die FreeCAD-Gemeinschaft, wo Anwender mit unterschiedlichen Hintergründen (Bauwesen, Architektur und Konstruktion) ohne weitreichende Programmierkenntnisse zusammenkommen.

Darüber hinaus ist Python aufgrund seiner weiten Verbreitung in anderen Anwendungen wie [Blender](https://www.blender.org) für 3D-Modellierung, [Inkscape](https://www.inkscape.org) für Vektorgrafiken und [GRASS GIS](https://grass.osgeo.org) für Geodatenanalysen eine unverzichtbare Fähigkeit für alle, die ihre Skriptfähigkeiten erweitern möchten. Die Beherrschung von Python in FreeCAD verbessert nicht nur Ihre Fähigkeit, benutzerdefinierte Tools und Makros zu erstellen, sondern vermittelt auch übertragbare Fähigkeiten, die auf verschiedenen Softwareplattformen angewendet werden können.

In FreeCAD ermöglicht Python-Scripting dem Anwender:

-   Automatisieren Sie sich wiederholende Aufgaben, um Zeit zu sparen und Fehler zu reduzieren.
-   Erstellen Sie benutzerdefinierte parametrische Objekte, die sich dynamisch an Änderungen anpassen.
-   Entwickeln Sie personalisierte Makros und Tools, die auf bestimmte Arbeitsabläufe zugeschnitten sind.
-   Interagieren Sie mit der Anwendungsprogrammierschnittstelle (API) von FreeCAD, um programmgesteuert auf Geometrie, Szenen und Benutzeroberflächenelemente zuzugreifen und diese zu bearbeiten.

Durch die Nutzung von Python können FreeCAD-Benutzer das volle Potenzial der Software freisetzen und sie in ein leistungsstarkes und flexibles Werkzeug verwandeln, das auf ihre individuellen Anforderungen zugeschnitten ist.

FreeCAD enthält eine erweiterte Python-Konsole, die über **Ansicht → Bedienfelder → Python**-Konsole zugänglich ist. Mit diesem Tool können Benutzer Vorgänge über die grafische Benutzeroberfläche hinaus ausführen, z. B. auf erweiterte Funktionen zugreifen, Geometriefehler beheben und Aufgaben automatisieren. Es protokolliert auch Python-Befehle für GUI-Aktionen, wenn die Option *Skriptbefehle in Python-Konsole anzeigen* unter **Bearbeiten → Einstellungen → Python → Makro** aktiviert ist. Wenn Sie die Konsole geöffnet lassen, können Sie den Python-Code beim Arbeiten beobachten. Dies bietet eine intuitive Möglichkeit, die Sprache zu erlernen und gleichzeitig die Funktionen von FreeCAD zu erkunden. Schließlich verfügt FreeCAD auch über ein [Makrosystem](Makros.md), mit dem Sie Aktionen aufzeichnen können, um sie später erneut auszuführen. Dieses System verwendet auch die Python-Konsole, indem es einfach alles aufzeichnet, was darin getan wird.

![](images/FreeCAD_Python_Console.png )

In diesem Kapitel werden wir ganz allgemein die Sprache Python entdecken. Wer daran interessiert ist, mehr zu erfahren, findet im FreeCAD-Dokumentations-Wiki einen ausführlichen Abschnitt zum Thema [Python-Programmierung](Power_users_hub/de.md).



### Python-Code schreiben 

In FreeCAD können Sie Python-Code auf zwei Arten schreiben: über die Python-Konsole (**Ansicht → Bedienfelder → Python-Konsole**) oder mithilfe des Makro-Editors (**Makro → Makros → Erstellen**). Die Python-Konsole ermöglicht es Ihnen, Befehle einzeln einzugeben, die sofort nach Drücken der Eingabetaste ausgeführt werden, was sie perfekt für schnelle Tests oder interaktive Erkundungen macht. Der Makro-Editor hingegen wird zum Schreiben und Speichern komplexerer Skripte verwendet, die aus mehreren Codezeilen bestehen. Diese Makros können später als Ganzes aus dem Makrofenster ausgeführt werden, was eine leistungsstarke Möglichkeit bietet, sich wiederholende Aufgaben zu automatisieren und die Funktionalität von FreeCAD zu erweitern. In diesem Kapitel können Sie beide Methoden verwenden, es wird jedoch dringend empfohlen, die Python-Konsole zu verwenden, da diese Sie sofort über alle Fehler informiert, die Sie beim Eintippen machen.

Wenn du Python zum ersten Mal verwendest, solltest du diese kurze [Einführung in die Python-Programmierung](Introduction_to_Python/de.md) liest, bevor du weitermachst, wird sie die grundlegenden Konzepte von Python klarer machen.



### Handhabung von FreeCAD Objekten 

Beginnen wir, indem wir ein neues leeres Dokument erstellen:


```python
doc = FreeCAD.newDocument()
```

Sobald Sie in der FreeCAD Python-Konsole FreeCAD eingeben (das Wort „FreeCAD" gefolgt von einem Punkt), wird ein Autovervollständigungsfenster angezeigt. Diese Funktion beschleunigt nicht nur Ihren Arbeitsablauf, indem sie verfügbare Befehle vorschlägt, sondern hilft Ihnen auch, neue Funktionen und Features in FreeCAD zu entdecken. Jeder Eintrag in der Liste enthält einen Tooltip, der seinen Zweck erklärt, sodass die verfügbaren Funktionen leichter zu verstehen und zu erkunden sind. Diese Autovervollständigungsfunktion ist besonders hilfreich für Anfänger, die Python-Skripting lernen, und für fortgeschrittene Benutzer, die effizient durch die umfangreiche API von FreeCAD navigieren. Nehmen Sie sich einen Moment Zeit, um die Optionen im Autovervollständigungsfenster zu erkunden -- möglicherweise entdecken Sie Befehle, die Ihren Arbeitsablauf vereinfachen oder neue Möglichkeiten eröffnen.

![](images/FreeCAD_python_newDocument.png )

Durch Eingeben von **FreeCAD.newDocument()** wird ein neues, leeres Dokument in FreeCAD erstellt, genauso wie durch Klicken auf die Schaltfläche **Neues Dokument** in der Symbolleiste. Wenn Sie **doc = FreeCAD.newDocument()** ausführen, wird das neue Dokumentobjekt der Variable **doc** zugewiesen, sodass Sie es programmgesteuert bearbeiten können. Mit doc können Sie Objekte hinzufügen, Eigenschaften ändern oder das Dokument speichern.

In Python wird der Punkt (.) verwendet, um anzuzeigen, dass ein Element in einem anderen enthalten ist. Beispielsweise ist **newDocument** eine Funktion innerhalb des **FreeCAD-Moduls**, weshalb wir FreeCAD.newDocument schreiben. Das angezeigte Autovervollständigungsfenster zeigt alles an, was im FreeCAD-Modul verfügbar ist. Wenn Sie nach newDocument einen Punkt eingeben (ohne die Klammern hinzuzufügen), wird alles angezeigt, was zur Funktion newDocument gehört. Dies veranschaulicht, wie Python Objekte und ihre Komponenten organisiert und darauf zugreift. Es ist wichtig zu beachten, dass die Klammern beim Aufrufen einer Python-Funktion obligatorisch sind, da sie die Ausführung der Funktion signalisieren.

Kommen wir nun zurück zu unserem Dokument. Lasst uns sehen, was wir damit machen können. Wir geben Folgendes ein und durchsuchen die verfügbaren Optionen:


```python
doc.
```

In FreeCAD können Ihnen die Namenskonventionen für Python-Befehle helfen, deren Zweck zu verstehen:

-   Namen, die mit einem Großbuchstaben beginnen, sind normalerweise Attribute, die Werte oder Daten speichern, wie z. B. Eigenschaften eines Objekts.
-   Namen, die mit einem Kleinbuchstaben beginnen, sind normalerweise Funktionen (auch Methoden genannt), die Aktionen oder Operationen ausführen, wie z. B. das Erstellen oder Ändern von Objekten.
-   Namen, die mit einem Unterstrich (\_) beginnen, sind im Allgemeinen für die interne Verwendung innerhalb des Moduls vorgesehen und können normalerweise ignoriert werden.

Diese Unterscheidung hilft Ihnen, sich in der API von FreeCAD zurechtzufinden und den für Ihre Anforderungen geeigneten Befehl auszuwählen. Sie können beispielsweise eine Methode verwenden, um einem Dokument ein neues Objekt hinzuzufügen. Die Methode führt die Aktion des Erstellens und Hinzufügens des Objekts aus, während Attribute die Eigenschaften des Objekts speichern. Das Verständnis dieser Struktur erleichtert das Erkunden der verfügbaren Funktionen, insbesondere bei Verwendung der Autovervollständigungsfunktion oder beim Lesen von Tooltips. Fügen wir eine Box hinzu.


```python
box = doc.addObject("Part::Box", "myBox")
```

Der Befehl **box = doc.addObject(\"Part::Box\", \"myBox\")** fügt dem Dokument ein neues 3D-Boxobjekt hinzu. Hier ist eine einfache Erklärung:

-   **doc.addObject**: Dies weist FreeCAD an, dem Dokument ein neues Objekt hinzuzufügen.
-   **Part::Box**: Dies gibt den zu erstellenden Objekttyp an, in diesem Fall eine 3D-Box.
-   **myBox**: Dies weist dem neuen Objekt einen Namen zu, sodass es später leichter identifiziert und referenziert werden kann.

Das Ergebnis dieses Befehls ist, dass im aktiven Dokument eine Box angezeigt wird und die Variable box einen Verweis darauf speichert, sodass Sie sie später ändern oder damit interagieren können. Unsere Box wird in der Baumansicht hinzugefügt, aber in der 3D-Ansicht passiert noch nichts, da das Dokument beim Arbeiten mit Python nie automatisch neu berechnet wird. Wir müssen das bei Bedarf manuell tun:


```python
doc.recompute()
```

Jetzt ist unser Kasten in der 3D-Ansicht erschienen. Viele der Schaltflächen auf der Werkzeugleiste, mit denen in FreeCAD Objekte hinzugefügt werden können, tun eigentlich zwei Dinge: das Objekt hinzufügen und neu berechnen. Versuche nun, mit der entsprechenden Schaltfläche im Arbeitsbereich Part eine Kugel hinzuzufügen, und du wirst sehen, wie die beiden Zeilen des Python-Codes nacheinander ausgeführt werden.

![](images/FreeCAD_python_Sphere.png )

Wir können eine Liste aller möglichen Objekttypen wie Part::Box abfragen:


```python
doc.supportedTypes()
```

Lasst uns nun den Inhalt unseres Quaders erkunden:


```python
box.
```

Sofort sehen wir ein paar sehr interessante Dinge, wie zum Beispiel:


```python
box.Height
```

Dadurch wird die aktuelle Höhe unseres Quaders ausgegeben. Lasst uns nun versuchen das zu ändern:


```python
box.Height = 5
```

Wird ein Kästchen mit der Maus markiert, sehen wir, dass im Eigenschafteneditor unter dem Reiter **Daten** unsere Eigenschaft **Höhe** mit dem neuen Wert erscheint. Alle Eigenschaften eines FreeCAD-Objekts, die in den Reitern **Daten** und **Ansicht** erscheinen, sind auch mit Python direkt zugänglich, und zwar über ihre Namen, wie wir es bei der Eigenschaft Höhe getan haben. Auf die Dateneigenschaften wird z.B. direkt vom Objekt selbst aus zugegriffen:


```python
box.Length
```

In FreeCAD werden visuelle Eigenschaften von einem **ViewObject** verwaltet. Jedes FreeCAD-Objekt hat ein zugehöriges ViewObject, das Informationen darüber speichert, wie das Objekt in der grafischen Benutzeroberfläche angezeigt wird, beispielsweise Farbe, Transparenz oder Sichtbarkeit. Das ViewObject ist jedoch nur zugänglich, wenn FreeCAD mit seiner grafischen Benutzeroberfläche ausgeführt wird. Wenn FreeCAD in einem nicht grafischen Modus gestartet wird -- beispielsweise von einem Terminal mit der Befehlszeilenoption -c oder wenn es als Python-Bibliothek in einem externen Skript verwendet wird -- ist das ViewObject nicht verfügbar. Dies liegt daran, dass in diesen Modi keine visuelle Darstellung des Objekts vorhanden ist, da die grafische Benutzeroberfläche nicht geladen wird.

Wir probieren das folgende Beispiel, um auf die Linienfarbe unseres Quaders zuzugreifen:


```python
box.ViewObject.LineColor
```



### Vektoren und Platzierungen 

Vektoren sind ein grundlegendes Konzept in jeder 3D-Anwendung. Ein Vektor ist im Wesentlichen eine Liste von drei Zahlen (x, y und z), die einen Punkt, eine Position oder eine Richtung im 3D-Raum beschreiben. Vektoren sind entscheidend für die Definition von Geometrie, Transformationen und Interaktionen in der 3D-Umgebung. Sie dienen als Bausteine ​​für Operationen wie Translationen, Rotationen und Skalierungen.

In FreeCAD werden Vektoren häufig zum Erstellen und Bearbeiten von Objekten verwendet. Sie ermöglichen eine breite Palette mathematischer Operationen wie Addition, Subtraktion, Kreuzprodukte, Skalarprodukte und Projektionen. Mit diesen Operationen können Sie Entfernungen, Winkel und Richtungen berechnen oder Beziehungen zwischen Objekten im Raum definieren.

Das Verständnis von Vektoren und ihrer Funktionsweise ist für effektives Scripting und Anpassung in FreeCAD unerlässlich. Vektoren werden beispielsweise verwendet, um Objekte zu positionieren, ihre Ausrichtung zu definieren oder sogar die Pfade für komplexe Operationen wie Sweeps oder Lofts zu berechnen.

In FreeCAD werden Vektoren mithilfe der Klasse **Vector** dargestellt, die verschiedene Methoden und Eigenschaften zum Ausführen von Operationen und zum Zugriff auf ihre Komponenten bereitstellt. Die Beherrschung dieser Fähigkeiten wird Ihre Fähigkeit, programmgesteuert mit der 3D-Umgebung von FreeCAD zu interagieren, erheblich verbessern. In FreeCAD funktionieren Vektoren folgendermaßen:


```python
myvec = FreeCAD.Vector(2, 0, 0)
print(myvec)
print(myvec.x)
print(myvec.y)
othervec = FreeCAD.Vector(0, 3, 0)
sumvec = myvec.add(othervec)
```

Hier ist eine kurze Aufschlüsselung der obigen Befehle:

-   **myvec = FreeCAD.Vector(2,0,0)**: Erstellt einen Vektor myvec mit X = 2, Y = 0, Z = 0.
-   **print(myvec)**: Druckt den Vektor myvec mit seinen Komponenten (X, Y, Z).
-   **print(myvec.x)**: Druckt die X-Komponente von myvec.
-   **print(myvec.y)**: Druckt die Y-Komponente von myvec.
-   **othervec = FreeCAD.Vector(0,3,0)**: Erstellt einen zweiten Vektor othervec mit X = 0, Y = 3, Z = 0.
-   **sumvec = myvec.add(othervec)**: Addiert myvec und othervec, um einen neuen Vektor sumvec zu erstellen, der die Summe ihrer Komponenten enthält.

Ein weiteres gemeinsames Merkmal von FreeCAD-Objekten ist ihre **Platzierung**. Wie wir in früheren Kapiteln gesehen haben, hat jedes Objekt eine Platzierungseigenschaft, die die Position (Basis) und Ausrichtung (Rotation) des Objekts enthält. Diese Eigenschaften lassen sich von Python aus leicht manipulieren, beispielsweise um unser Objekt zu verschieben:


```python
print(box.Placement)
print(box.Placement.Base)
box.Placement.Base = sumvec
otherpla = FreeCAD.Placement()
otherpla.Base = FreeCAD.Vector(5, 5, 0)
box.Placement = otherpla
```

Hier ist eine kurze Aufschlüsselung der obigen Befehle:

-   **print(box.Placement)**: Druckt die Platzierung der Box, einschließlich ihrer Position, Drehung und Ausrichtung im 3D-Raum.
-   **print(box.Placement.Base)**: Druckt die Position (Basis) der Box, die ein Vektor ist, der ihre Position im 3D-Raum darstellt.
-   **box.Placement.Base = sumvec**: Setzt die Basisposition (Position) der Box auf den Vektor sumvec und verschiebt die Box effektiv an diese neue Position.
-   **otherpla = FreeCAD.Placement()**: Erstellt ein neues Platzierungsobjekt namens otherpla.
-   **otherpla.Base = FreeCAD.Vector(5,5,0)**: Setzt die Basisposition von otherpla auf einen Vektor bei den Koordinaten (5, 5, 0).
-   **box.Placement = otherpla**: Wendet otherpla auf die Box an und aktualisiert ihre Platzierung auf die neue Position und Ausrichtung, die durch otherpla definiert wird.

**Mehr lesen**

-   [Python](https://www.python.org)
-   [Makros](Macros/de.md)
-   [Einführung in Python](Introduction_to_Python/de.md)
-   [Anleitung Skripterstellung mit Python](Python_scripting_tutorial/de.md)
-   [Hauptanwenderzentrum](Power_users_hub/de.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Manual:A gentle introduction/de
