# Manual:Parametric objects/de
{{Manual:TOC/de}}

FreeCAD ist für die parametrische Modellierung konzipiert. Das bedeutet, dass die Geometrie, die du erstellst, nicht frei modellierbar ist, sondern durch Regeln und Parameter erzeugt wird. Zum Beispiel kann ein Zylinder aus einem Radius und einer Höhe erzeugt werden. Mit diesen beiden Parametern hat das Programm genügend Informationen, um den Zylinder zu bauen.

Parametrische Objekte sind in FreeCAD in Wirklichkeit kleine Teile eines Programms, die immer dann laufen, wenn sich einer der Parameter geändert hat. Objekte können viele verschiedene Arten von Parametern haben: Zahlen (ganze Zahlen wie 1, 2, 3 oder Fließkommazahlen wie 3.1416), reale Größen (1mm, 2.4m, 4.5ft), (x,y,z) Koordinaten, Textstrings (\"Hallo!\") oder sogar ein anderes Objekt.

Dieser letzte Typ erlaubt es, schnell komplexe Ketten von Operationen zu erstellen, wobei jedes neue Objekt auf einem vorhergehenden Objekt basiert und diesem neue Funktionen hinzufügt.

Im folgenden Beispiel basiert ein massives, würfelförmiges Objekt (Polster) auf einer rechteckigen 2D Form (Skizze) und hat einen Extrusionsabstand. Mit diesen beiden Eigenschaften erzeugt es eine feste Form, indem es die Grundform um den angegebenen Abstand extrudiert. Du kannst dieses Objekt dann als Basis für weitere Operationen verwenden, wie z.B. das Zeichnen einer neuen 2D Form auf einer seiner Flächen (Sketch001) und dann eine Subtraktion (Tasche), bis du zu deinem endgültigen Objekt kommst.

Alle Zwischenbearbeitungen (2D Formen, Polster, Tasche, usw.) sind immer noch vorhanden, und Du kannst immer noch jeden ihrer Parameter jederzeit ändern. Die gesamte Kette wird bei Bedarf neu aufgebaut (neu berechnet).

![](images/Parametric_objects.jpg )

Zwei wesentliche Dinge sind notwendig zu wissen:

1.  Die Neuberechnung erfolgt nicht immer automatisch. Schwere Operationen, die einen großen Teil deines Dokumentes verändern können und daher einige Zeit in Anspruch nehmen, werden nicht automatisch durchgeführt. Stattdessen wird das Objekt (und alle davon abhängigen Objekte) zur Neuberechnung markiert (ein kleines blaues Symbol erscheint darauf in der Baumansicht). Du musst dann die Neu berechnen Schaltfläche (oder **Bearbeiten->Aktualisieren**) drücken, um alle markierten Objekte neu berechnen zu lassen.
2.  Der Abhängigkeitsbaum muss immer in die gleiche Richtung fließen. Schleifen sind verboten. (Siehe [DAG](Glossary#Directed_Acyclic_Graph.md), und [DAG Ansicht](DAG_view/de.md)) Du kannst ein Objekt A haben, das von Objekt B abhängt, das von Objekt C abhängt. Aber du kannst kein Objekt A haben, das von Objekt B abhängt, das von Objekt A abhängt. Du kannst jedoch viele Objekte haben, die vom selben Objekt abhängen, z.B. hängen die Objekte B und C beide von A ab. Menü **Werkzeuge-> Abhängigkeitsdiagramm** zeigt dir ein Abhängigkeitsdiagramm wie in der obigen Abbildung. Es kann nützlich sein, um Probleme zu erkennen.

Nicht alle Objekte sind in FreeCAD parametrisch. Häufig enthält die Geometrie, die Du aus anderen Dateien importierst, keine Parameter und es handelt sich um einfache, nicht-parametrische Objekte. Diese können jedoch oft als Basis oder Ausgangspunkt für neu erstellte parametrische Objekte verwendet werden, was natürlich davon abhängt, was das parametrische Objekt benötigt und von der Qualität der importierten Geometrie.

Alle Objekte, ob parametrisch oder nicht, haben jedoch einige grundlegende Parameter, wie z.B. einen Namen, der im Dokument eindeutig ist und nicht bearbeitet werden kann, eine Beschriftung, die ein benutzerdefinierter Name ist, der bearbeitet werden kann, und eine [Positionierung](placement/de.md), die ihre Position im 3D Raum hält.

Schließlich ist es erwähnenswert, dass benutzerdefinierte parametrische Objekte [einfach in Python zu programmieren](Scripted_objects/de.md) sind.

**Weiterlesen**

-   [Der Eigenschaftseditor](Property_editor/de.md)
-   [Wie man parametrische Objekte programmiert](Scripted_objects/de.md)
-   [Positionierung von Objekten in FreeCAD](Placement/de.md)
-   [Aktivierung des Abhängigkeitsdiagramms](Std_DependencyGraph/de.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Parametric objects/de
