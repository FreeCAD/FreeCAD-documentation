# Manual:Parametric objects/de
{{Manual:TOC}}

FreeCAD verwendet eine parametrische Herangehensweise zum Modellieren, bei dem die Geometrie von Objekten von Regeln und Parametern im Hintergrund gesteuert wird, anstatt frei modelliert zu werden. Dies bedeutet, dass die Abmaße und Merkmale aller Komponenten durch Parameter festgelegt werden, die das Programm anweisen, wie die Geometrie zu erstellen ist. Zum Beispiel um einen Zylinder zu erstellen, werden Parameter wie Radius und Höhe angegeben. Mit diesen Werten erstellt FreeCAD die geometrisch genaue Form.

In FreeCAD sind parametrische Objekte im Prinzip kleine programmierbare Skripte, die ausgeführt werden, wenn ein Parameter geändert wird. Diese Parameter können sehr unterschiedlich sein, einschließlich ganzer Zahlen, Fließkommazahlen, Zahlengrößen der realen Welt in Millimetern, Metern oder Fuß, Koordinaten (dargestellt als x, y, z), Textzeichenketten und sogar Referenzen zu anderen Objekten. Solche Vielseitigkeit der Parameter ermöglicht die Erstellung komplexer Modelle durch eine Reihe verketteter Arbeitsschritte, bei denen jedes neue Objekt Merkmale des vorherigen ableitet und gleichzeitig weitere Attribute hinzufügt.

Als Beispiel stellen wir uns ein würfelförmiges Objekt vor, das durch parametrisches Modellieren erstellt wird. Wir starten mit einer grundlegenden rechteckigen 2D-Form, die Platte genannt wird, mit der Länge l und der Breite w. Diese Skizze legt die Basis unseres würfelförmigen Objekts fest. Als nächstes wird ein Arbeitsschritt zum Extrudieren festgelegt, bei dem eine Länge bestimmt wird, mit der eine Skizze zu einem 3D-Objekt ausgezogen oder aus einem 3D-Objekt herausgezogen wird. Dies ergibt eine würfelförmige Form, die auf der Form der Skizze und auf der angegebenen Extrusionslänge basiert.

![](images/FreeCAD_022_PArametricDesignPlate.png )

Auf der Oberseite der Platte skizziere einen Kreis mit einem bestimmten Durchmesser d. Anschließend verwende diesen Kreis, um aus der Originalplatte eine Tasche zu erstellen (Material zu entfernen).

![](images/FreeCAD_022_ParametricDesignPocket.png )

Wenn du dich entscheidest, die Abmessungen der Platte oder des Kreises zu ändern, wird das endgültige Objekt ebenfalls geändert. Dank der Verwendung eines parametrischen Designansatzes ist es nicht erforderlich, das Objekt von Anfang an neu zu erstellen.

1.  Die Neuberechnung erfolgt nicht immer automatisch. Schwierige Operationen, die einen großen Teil deines Dokumentes verändern können und daher einige Zeit in Anspruch nehmen, werden nicht automatisch durchgeführt. Stattdessen wird das Objekt (und alle davon abhängigen Objekte) zur Neuberechnung markiert (ein kleines blaues Symbol erscheint darauf in der Baumansicht). Du musst dann die Schaltfläche Neu berechnen (oder **Bearbeiten -> Aktualisieren**) drücken, um alle markierten Objekte neu berechnen zu lassen.
2.  Der Abhängigkeitsbaum muss immer in die gleiche Richtung fließen. Schleifen sind verboten. (Siehe [DAG](Glossary#Directed_Acyclic_Graph.md), und [DAG-Ansicht](DAG_view/de.md)) Du kannst ein Objekt A haben, das von Objekt B abhängt, das von Objekt C abhängt. Aber du kannst kein Objekt A haben, das von Objekt B abhängt, das von Objekt A abhängt. Du kannst jedoch viele Objekte haben, die vom selben Objekt abhängen, z.B. hängen die Objekte B und C beide von A ab. Menü **Werkzeuge -> Abhängigkeitsgraph...** zeigt dir ein Abhängigkeitsdiagramm wie in der obigen Abbildung. Es kann nützlich sein, um Probleme zu erkennen.

Im parametrischen Modellierungsprozess von FreeCAD bietet die Untersuchung des Abhängigkeitsbaums eines Objekts einen klaren Einblick in den sequentiellen Aufbau und die Beziehungen innerhalb eines Modells. Die Grundlage der Struktur im obigen Beispiel ist die „Plattenskizze", die als Basis für die Ausgangsform des Modells dient. Anschließend wird eine „Pad"-Operation angewendet, die dieser Grundskizze Material hinzufügt und so effektiv eine dreidimensionale Struktur aus der zweidimensionalen Basis erstellt.

Anschließend wird auf der neu geformten Oberfläche eine „Kreisskizze" entworfen. Dieser Kreis bildet die Grundlage für die nachfolgende „Taschen"-Operation. Bei der Taschenoperation wird gezielt Material aus der Struktur entfernt, im Wesentlichen wird ein Teil auf Grundlage der Kreisskizze herausgearbeitet. Dieser Prozess des Hinzufügens und anschließenden Entfernens von Material ermöglicht die nahtlose Integration komplexer Geometrien und Merkmale in das Basismodell.

Durch diese Abfolge von Vorgängen -- ausgehend von der Basisskizze, Hinzufügen von Volumen mit einem Pad und Erstellen detaillierter Merkmale mit zusätzlichen Skizzen und Taschen -- nimmt das endgültige Objekt Gestalt an. Jeder Schritt in dieser Kette hängt von seinem Vorgänger ab und veranschaulicht die vernetzte Natur des parametrischen Designs in FreeCAD.

![](images/FreeCAD_022_ParametricDesignDependGraph.png )

Nicht alle Objekte in FreeCAD sind parametrisch. Häufig enthält die Geometrie, die aus anderen Dateien importiert wird, keine Parameter und es handelt sich um einfache, nicht-parametrische Objekte. Diese können jedoch oft als Basis oder Ausgangspunkt für neu erstellte parametrische Objekte verwendet werden, was natürlich davon abhängt, was das parametrische Objekt benötigt und von der Qualität der importierten Geometrie.

Alle Objekte, ob parametrisch oder nicht, haben jedoch einige grundlegende Parameter, wie z.B. einen Namen, der im Dokument eindeutig ist und nicht bearbeitet werden kann, eine Benennung (Label), die ein benutzerdefinierter Name ist, der bearbeitet werden kann, und eine [Positionierung](placement/de.md), die die zugehörige Position im 3D-Raum enthält.

Schließlich ist es erwähnenswert, dass benutzerdefinierte parametrische Objekte einfach [in Python](Scripted_objects/de.md) programmiert werden können.

**Weiterlesen**

-   [Der Eigenschafteneditor](Property_editor/de.md)
-   [Wie man parametrische Objekte programmiert](Scripted_objects/de.md)
-   [Objekten in FreeCAD positionieren](Placement/de.md)
-   [Aktivierung des Abhängigkeitsdiagramms](Std_DependencyGraph/de.md)



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser%20Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Parametric objects/de
