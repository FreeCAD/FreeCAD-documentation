# Python scripting tutorial/de
{{TOCright}}

## Einführung

[Python](http://en.wikipedia.org/wiki/Python_%28programming_language%29) ist eine Programmiersprache, sehr einfach zu bedienen und sehr schnell zu erlernen. Sie ist quelloffen, plattformübergreifend und kann für eine Vielzahl von Aufgaben allein verwendet werden, von der Programmierung einfacher Shell Skripte bis hin zu sehr komplexen Programmen. Aber eine der am weitesten verbreiteten Anwendungen ist die Skriptsprache, da sie leicht in andere Anwendungen integriert werden kann. Genau so wird es in FreeCAD verwendet. Von der [Python Konsole](Python_console/de.md) oder von deinen benutzerdefinierten Skripten aus kannst du FreeCAD steuern und es sehr komplexe Aktionen ausführen lassen.

Zum Beispiel aus einem Python Skript, kannst Du:

-   neue Objekte erstellen
-   bestehende Objekte ändern
-   die 3D Darstellung dieser Objekte ändern
-   die FreeCAD Oberfläche verändern

Es gibt mehrere Möglichkeiten, Python in FreeCAD zu verwenden:

-   Aus dem [FreeCAD Python Interpreter](FreeCAD_Scripting_Basics/de.md), wo du einfache Befehle wie in einer \"Kommandozeile\" ähnlichen Oberfläche ausgeben kannst.
-   Aus [Makros](Macros/de.md), die eine bequeme Möglichkeit darstellen, ein fehlendes Werkzeug schnell zur FreeCAD Oberfläche hinzuzufügen.
-   Aus externen Skripten, mit denen man viel komplexere Dinge programmieren kann, wie z.B. ganze [Arbeitsbereiche](Workbenches/de.md).

In diesem Tutorial werden wir an ein paar einfachen Beispielen arbeiten, um dir den Einstieg zu erleichtern, aber es gibt auch viel mehr [Dokumentation über Python Skripten](Power_users_hub/de.md) auf diesem Wiki. Wenn du völlig neu in Python bist und verstehen willst, wie es funktioniert, haben wir auch eine grundlegende [Einführung in Python](introduction_to_Python/de.md).

Bevor Du mit dem Python Skripting fortfährst, gehe zum {{MenuCommand/de|Bearbeiten → Einstellungen → Allgemein → Ausgabefenster}} und hake 2 Kästchen an:

-    **Interne Python Ausgabe auf Berichtsansicht umleiten**.

-    **Interne Python Fehler auf Berichtsansicht umleiten**.

Dann gehe zu **Ansicht → Paneele** und hake an:

-    **Berichtsansicht**
    

## Python Code schreiben 

Es gibt zwei einfache Wege, Python Code in FreeCAD zu schreiben: Über die Python Konsole (verfügbar im Menü Ansicht → Paneele → Python Konsole) oder über den Makro Editor (Werkzeuge → Makros). In der Konsole schreibst Du nacheinander Python Befehle, die ausgeführt werden, wenn Du die Eingabetaste drückst, während die Makros ein komplexeres Skript aus mehreren Zeilen enthalten können, das erst bei der Ausführung des Makros ausgeführt wird.

![](images/Screenshot_pythoninterpreter.jpg ) 
*Die FreeCAD Python Konsole*

In diesem Tutorium kannst Du beide Methoden verwenden. Du kannst Kopieren/Einfügen von einzelnen Zeilen in die Python Konsole und drücken der **Eingabetaste** oder Kopieren/Einfügen des gesamten Codes in ein neues Makro Fenster. {{Top}}

## Erkunden von FreeCAD 

Wir beginnen damit, ein neues leeres Dokument zu erstellen:


```python
doc = FreeCAD.newDocument()
```

Wenn du dies in der FreeCAD Python Konsole eingibst, wirst du feststellen, dass sobald du `FreeCAD.` eingibst, ein Fenster erscheint, in dem du den Rest deiner Zeile schnell automatisch vervollständigen kannst. Besser noch, jeder Eintrag in der Autovervollständigungsliste hat einen Werkzeugtip, der erklärt, was er tut. Dies macht es einfacher, die verfügbare Funktionalität zu erkunden. Bevor du `newDocument` wählst, wirf einen Blick auf die anderen Optionen.

![](images/Screenshot_classbrowser.jpg ) 
*Autovervollständigungsmechanismus der FreeCAD Pythonkonsole*

Nun wird unser neues Dokument erstellt. Dies ist ähnlich wie das Drücken der **<img src="images/Std_New.svg" width=16px> [Std Neu](Std_New/de.md)** Schaltfläche in der Werkzeugleiste. Tatsächlich tun die meisten Schaltflächen in FreeCAD nichts anderes, als eine oder mehrere Zeilen Python Code auszuführen. Noch besser, du kannst eine Option in **Bearbeiten → Einstellungen → Allgemein → Makro** auf **Zeige Skriptbefehle in der Python konsole** setzen. Dadurch wird in der Konsole der gesamte Python Code ausgegeben, der ausgeführt wird, wenn fu Tasten drückst. Sehr nützlich, um zu lernen, wie man Aktionen in Python reproduziert.

Lass uns nun zu unserem Dokument zurückkehren und sehen, was wir mit ihm machen können:


```python
doc.
```

Erkunde die verfügbaren Optionen. Normalerweise sind Namen, die mit einem Großbuchstaben beginnen, Attribute, sie enthalten einen Wert, während Namen, die mit einem Kleinbuchstaben beginnen, Funktionen (auch Methoden genannt) sind, sie \"tun etwas\". Namen, die mit einem Unterstrich beginnen, sind normalerweise für die interne Arbeit des Moduls da, und du solltest dich nicht um sie kümmern. Lasse uns eine der Methoden verwenden, um ein neues Objekt zu unserem Dokument hinzuzufügen:


```python
box = doc.addObject("Part::Box", "myBox")
```

Es geschieht nichts. Warum nicht? Weil FreeCAD für das große Ganze gemacht ist. Eines Tages wird es mit Hunderten von komplexen Objekten arbeiten, die alle voneinander abhängen. Wenn du irgendwo eine kleine Änderung vornimmst, kann das große Auswirkungen haben, und du musst vielleicht das ganze Dokument neu berechnen, was sehr lange dauern kann. Aus diesem Grund aktualisiert fast kein Befehl die Szene automatisch. Du musst es manuell durchführen:


```python
doc.recompute()
```

Nun erschien unser Würfel. Viele der Schaltflächen, mit denen in FreeCAD Objekte hinzugefügt werden können, tun eigentlich zwei Dinge: das Objekt hinzufügen und neu berechnen. Wenn du die obige Option **Skriptbefehle in der Python Konsole anzeigen** eingeschaltet hast, versuche, mit der GUI Schaltfläche eine Kugel hinzuzufügen. Du wirst sehen, wie die beiden Zeilen des Python Codes nacheinander ausgeführt werden.

Lass uns nun den Inhalt unseres Würfels erkunden:


```python
box.
```

Du wirst sofort einige sehr interessante Dinge sehen, wie zum Beispiel:


```python
box.Height
```

Dadurch wird die aktuelle Höhe unseres Würfels ausgegeben. Lass uns nun versuchen das zu ändern:


```python
box.Height = 5
```

Wenn du dein Feld mit der Maus auswählst, siehst du, dass im [Eigenschaftseditor](Property_editor/de.md) auf dem **Daten** Reiter unsere Eigenschaft **Höhe** erscheint. Alle Eigenschaften eines FreeCAD Objekts, die dort (und auch auf dem **Ansicht** Reiter erscheinen, dazu später mehr), sind auch von Python direkt zugänglich, und zwar über ihren Namen, wie wir es mit der **Höhe** Eigenschaft getan haben. Versuche, die anderen Dimensionen des Würfels zu ändern. {{Top}}

## Vektoren und Platzierungen 

[Vektoren](https://de.wikipedia.org/wiki/vektor) sind ein fester Bestandteil jeder 3D-Anwendung. Ein Vektor ist dabei eine Liste von Zahlen (x,y,z), die einen Ort im dreidimensionalen Raum beschreiben. Mit Vektoren sind verschiedene mathematische Operationen möglich, wie z.B. Addition, Subtraktion, Projektion (Skalarprodukt) und [vieles mehr](https://de.wikipedia.org/wiki/Vektorraum). In FreeCAD funktionieren Vektoren wie folgt:


```python
myvec = FreeCAD.Vector(2, 0, 0)
myvec.x
myvec.y
othervec = FreeCAD.Vector(0, 3, 0)
sumvec = myvec.add(othervec)
```

Ein weiteres gemeinsames Merkmal von FreeCAD Objekten ist ihre [Placement](Placement/de.md). Jedes Objekt hat eine **Platzierung**s Eigenschaft, die die **Base** enthält. (Position) und **Rotation** (Orientierung) des Objekts. Es ist leicht zu bearbeiten, zum Beispiel um unser Objekt zu bewegen:


```python
box.Placement
box.Placement.Base
box.Placement.Base = sumvec
 
otherpla = FreeCAD.Placement()
box.Placement = otherpla
```

Nun musst du einige wichtige Konzepte verstehen, bevor wir weiter kommen. {{Top}}

## App und GUI 

FreeCAD wurde von Anfang an als Kommandozeilen-Anwendung konzipiert, d.h. ohne notwendige Benutzeroberfläche. Als Folge davon ist fast alles zwischen einer \"geometrischen\" Komponente und einer \"visuellen\" Komponente aufgeteilt. Wenn man im Kommandozeilenmodus arbeitet, dann ist der geometrische Teil vorhanden, aber der visuelle Teil deaktiviert. Fast jedes Objekt in FreeCAD besteht deshalb aus zwei Teilen, einem *Object* und einem *ViewObject* (Objektansicht).

Um das Konzept zu veranschaulichen, schauen wir uns unser Würfel Objekt an. Die geometrischen Eigenschaften des Würfels wie Abmessungen, Position usw. sind im `Objekt` gespeichert. Während seine visuellen Eigenschaften wie Farbe, Linienstärke usw. im `AnsichtObjekt` gespeichert sind, werden seine visuellen Eigenschaften wie Farbe, Linienstärke usw. im `AnsichtObjekt` gespeichert. Dies entspricht den **Daten** und **Ansicht** Reitern im [Eigenschaftseditor](Property_editor/de.md). Auf das Ansicht Objekt eines Objekts wird wie folgt zugegriffen:


```python
vo = box.ViewObject
```

Jetzt kannst du auch die Eigenschaften auf dem **Ansicht** Reiter ändern:


```python
vo.Transparency = 80
vo.hide()
vo.show()
```

Wenn du FreeCAD startest, lädt die Python Konsole bereits zwei Basismodule: `FreeCAD` und `FreeCADGui` (die auch über ihre Kürzel `App` und `Gui` erreicht werden können). Sie enthalten alle Arten von generischer Funktionalität für die Arbeit mit Dokumenten und ihren Objekten. Um unser Konzept zu veranschaulichen, siehe, dass sowohl `FreeCAD` als auch `FreeCADGui` ein `ActiveDocument` Attribut enthalten, das das aktuell geöffnete Dokument ist. `FreeCAD.ActiveDocument` und `FreeCADGui.ActiveDocument` sind jedoch nicht dasselbe Objekt. Sie sind die beiden Komponenten eines FreeCAD Dokuments, und sie enthalten unterschiedliche Attribute und Methoden. So enthält z.B. `FreeCADGui.ActiveDocument` `ActiveView`, welches die aktuell geöffnete [3D Ansicht](3D_view/de.md) ist. {{Top}}

## Module

Die wahre Stärke von FreeCAD liegt in seinen treuen Modulen mit ihren jeweiligen Arbeitsbereichen. Die FreeCAD Basisanwendung ist mehr oder weniger ein leerer Behälter. Ohne seine Module kann es kaum mehr tun, als neue, leere Dokumente zu erstellen. Jedes Modul fügt der Oberfläche nicht nur neue Arbeitsbereiche hinzu, sondern auch neue Python Befehle und neue Objekttypen. So können mehrere verschiedene, sogar völlig inkompatible Objekttypen in einem Dokument koexistieren. Die wichtigsten Module in FreeCAD, die wir uns in diesem Tutorium ansehen werden, sind: [Part](Part_Workbench/de.md), [Netz](Mesh_Workbench/de.md), [Skizzierer](Sketcher_Workbench/de.md) und [Entwurf](Draft_Workbench/de.md).

[Skizzierer](Sketcher_Workbench/de.md) und [Entwurf](Draft_Workbench/de.md) verwenden beide das [Part](Part_Workbench/de.md) Modul, um ihre Geometrie zu erzeugen und handzuhaben. Während [Netz](Mesh_Workbench/de.md) völlig unabhängig ist und seine eigenen Objekte handhabt. Mehr dazu weiter unten.

Du kannst alle verfügbaren Basisobjekttypen für das aktuelle Dokument folgendermaßen prüfen:


```python
doc.supportedTypes()
```

Die verschiedenen FreeCAD Module werden nicht automatisch in die Python Konsole geladen. Damit soll ein sehr langsamer Start vermieden werden. Die Module werden nur geladen, wenn du sie benötigst. So kannst du z.B. untersuchen, was sich innerhalb des Part Moduls befindet:


```python
import Part
Part.
```

Aber wir werden weiter unten mehr über das Part Modul sprechen. {{Top}}

## Modul Mesh 

[Polygonnetze](https://de.wikipedia.org/wiki/Polygonnetz) (engl.: Meshes) sind eine sehr einfache Art von 3D Objekten, die z.B. von [Sketchup](https://en.wikipedia.org/wiki/SketchUp), [Blender](https://en.wikipedia.org/wiki/Blender_(software)) und [3D Studio Max](https://en.wikipedia.org/wiki/Autodesk_3ds_Max) verwendet werden. Sie werden aus 3 Elementen gebildet: Punkte (auch Knoten genannt), Linien (auch Kanten genannt) und Flächen. In vielen Anwendungen, einschließlich FreeCAD, können Flächen nur 3 Knoten haben. Natürlich hindert Dich nichts daran, eine größere ebene Fläche aus mehreren nebeneinander liegenden Dreiecken zu haben.

Polygonnetze sind einfach, aber weil sie einfach sind, kannst Du leicht Millionen von ihnen in einem einzigen Dokument haben. Allerdings sind sie in FreeCAD weniger nützlich und meist vorhanden, so dass Du Objekte in Netzformaten (**.stl**, **.obj**) aus anderen Anwendungen importieren kannst. Das Netzmodul wurde auch im ersten Monat des FreeCAD Lebens ausgiebig als Haupttestmodul verwendet.

Netzobjekte und FreeCAD Objekte sind unterschiedliche Dinge. Du kannst das FreeCAD Objekt als einen Behälter für ein Netzobjekt betrachten (und wie wir unten sehen werden, auch für Part Objekte). Um also ein Netz Objekt zu FreeCAD hinzuzufügen, müssen wir zuerst ein FreeCAD Objekt und ein Mesh Objekt erstellen und dann das Netz Objekt zum FreeCAD Objekt hinzufügen:


```python
import Mesh
mymesh = Mesh.createSphere()
mymesh.Facets
mymesh.Points
 
meshobj = doc.addObject("Mesh::Feature", "MyMesh")
meshobj.Mesh = mymesh
doc.recompute()
```

Dies ist ein Standardbeispiel, das die `createSphere()` Methode verwendet, um eine Kugel zu erstellen, aber Du kannst auch benutzerdefinierte Netze von Grund auf neu erstellen, indem Du ihre Knoten und Flächen definierst.

[Lies mehr über Netz Skripten\...](Mesh_Scripting/de.md) {{Top}}

## Modul Part 

Das [Part](Part_Workbench/de.md) Modul ist das leistungsfähigste Modul im gesamten FreeCAD. Es erlaubt Dir [BREP](http://en.wikipedia.org/wiki/Boundary_representation) Objekte zu erstellen und zu verändern. Diese Art von Objekten kann, im Gegensatz zu Netzen, eine Vielzahl von Komponenten haben. BREP steht für Begrenzungsflächenmodell (engl.: Boundary Representation), was bedeutet, dass BREP Objekte durch ihre Oberflächen definiert werden; diese Oberflächen umschließen und definieren ein Innenvolumen. Eine Oberfläche kann eine Vielzahl von Dingen sein, wie z.B. ebene Flächen oder sehr komplexe NURBS Oberflächen.

Das Part Modul basiert auf der leistungsstarken [OpenCasCade](https://en.wikipedia.org/wiki/Open_CASCADE_Technology) Bibliothek, die es ermöglicht, eine Vielzahl von komplexen Operationen auf diesen Objekten einfach durchzuführen, wie z.B. boolesche Operationen, Verrundungung, Ausformungen, usw.

Das Part-Modul arbeitet auf dieselbe Weise wie das Netz Modul: Man erzeugt ein FreeCAD Objekt, ein Part Objekt, danach fügt man das Part Objekt zum FreeCAD Objekt hinzu:


```python
import Part
myshape = Part.makeSphere(10)
myshape.Volume
myshape.Area

shapeobj = doc.addObject("Part::Feature", "MyShape")
shapeobj.Shape = myshape
doc.recompute()
```

Das Part Modul (wie das Netz Modul) hat auch ein Tastaturkürzel, das automatisch ein FreeCAD Objekt erstellt und eine Form hinzufügt, so dass du die letzten drei Zeilen verkürzen kannst auf:


```python
Part.show(myshape)
```

Beim erforschen der Inhalt von myshape, wirst Du viele interessante Unterkomponenten wie `Flächen`, `Kanten`, `Knoten`, `Festkörper` und `Schalen`, und eine weite Bandbreite von Geometrieoperationen wie `Schnitt` (Subtraktion), `Gemeinsam` (Schnittpunkt) oder `Verschmelzung` (Vereinigung) bemerken. Die [Topologisches Daten Skripten](Topological_data_scripting/de.md) Seite erklärt all das im Detail.

[Lies mehr über Part Skripten\...](Topological_data_scripting/de.md) {{Top}}

## Modul Draft 

FreeCAD bietet noch viele weitere Module, wie [Skizzierer](Sketcher_Workbench/de.md) und [Entwurf](Draft_Workbench/de.md), die ebenfalls Teilobjekte erzeugen. Diese Module fügen zusätzliche Parameter zu den erzeugten Objekten hinzu oder implementieren sogar eine völlig neue Art und Weise, die Teilegeometrie in ihnen zu handhaben. Unser obiges Box Beispiel ist ein perfektes Beispiel für ein parametrisches Objekt. Alles was Du zur Definition der Box benötigst, ist die Angabe der Parameter Höhe, Breite und Länge. Basierend auf diesen Parametern berechnet das Objekt automatisch seine Teileform. FreeCAD erlaubt es Dir [Erzeuge solche Objekte in Python](Scripted_objects/de.md).

Das [Entwurf](Draft_Workbench/de.md) Modul fügt parametrische 2D Objekttypen (die alle Part Objekte sind) wie Linien und Kreise hinzu und bietet auch einige grundlegende Funktionen, die nicht nur auf Entwurfsobjekte, sondern auf jedes Part Objekt wirken. Um zu erkunden, was verfügbar ist, mache einfach:


```python
import Draft
rec = Draft.makeRectangle(5, 2)
mvec = FreeCAD.Vector(4, 4, 0)
Draft.move(rec, mvec)
Draft.move(box, mvec)
```


{{Top}}

## Benutzeroberfläche

Die Benutzeroberfläche von FreeCAD ist mit [Qt](http://en.wikipedia.org/wiki/Qt_%28framework%29), einer leistungsstarken grafischen Schnittstellensystem, erstellt worden, das für das Zeichnen und die Handhabung aller Bedienelemente, Menüs, Werkzeugleisten und Schaltflächen rund um die 3D Ansicht verantwortlich ist. Qt stellt ein Modul, PySide, zur Verfügung, welches Python erlaubt, auf die Qt Schnittstellen wie FreeCAD zuzugreifen und zu verändern. Lass uns versuchen, mit der Qt Schnittstelle zu tüfteln und einen einfachen Dialog zu erzeugen:


```python
from PySide import QtGui
QtGui.QMessageBox.information(None, "Apollo program", "Houston, we have a problem")
```

Beachte, dass der erscheinende Dialog das FreeCAD Symbol in seiner Werkzeugleiste hat, was bedeutet, dass Qt weiß, dass der Auftrag aus der FreeCAD Anwendung heraus erteilt wurde. Es ist möglich, jeden Teil der FreeCAD Oberfläche zu verändern.

Qt ist ein sehr mächtiges Schnittstellensystem, das es dir erlaubt, sehr komplexe Dinge zu tun. Es hat auch einige einfach zu benutzende Werkzeuge wie den Qt Designer, mit dem du Dialoge grafisch entwerfen kannst und sie dann mit ein paar Zeilen Python Code zur FreeCAD Oberfläche hinzufügen kannst.

[Erfahre hier mehr über PySide\...](PySide/de.md) {{Top}}

## Makros

Nun, da Du ein gutes Verständnis der Grundlagen hast, wo werden wir unsere Python Skripte aufbewahren und wie werden wir sie einfach von FreeCAD aus starten? Dafür gibt es einen einfachen Mechanismus, genannt [Makros](Macros/de.md). Ein Makro ist einfach ein Python Skript, das zu einer Werkzeugleiste hinzugefügt und per Mausklick gestartet werden kann. FreeCAD bietet dir einen einfachen Texteditor (**Makro → Makros → Erstellen**), in dem du Skripte schreiben oder einfügen kannst. Sobald das Skript fertig ist, verwende **Werkzeuge → Anpassung → Makros**, um eine Schaltfläche dafür zu definieren, die zu den Werkzeugleisten hinzugefügt werden kann.

Jetzt bist Du bereit für eine vertieftere FreeCAD Skripterstellung. Gehe weiter zum [Verteiler für Erfahrene Anwender](Power_users_hub/de.md)! {{Top}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Python scripting tutorial/de
