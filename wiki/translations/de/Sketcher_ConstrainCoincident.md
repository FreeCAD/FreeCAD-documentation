---
- GuiCommand   */de
   Name   *Sketcher ConstrainCoincident
   Name/de   *Skizzierer KoinzidentFestlegen
   MenuLocation   *Skizze → Skizzen-Beschränkungen → Koinzidenz erzwingen
   Workbenches   *[Sketcher](Sketcher_Workbench/de.md)
   Shortcut   ***C**
   SeeAlso   *[Sketcher Sperren](Sketcher_ConstrainLock/de.md), [Sketcher PunktAufObjektFestlegen](Sketcher_ConstrainPointOnObject/de.md)
---

# Sketcher ConstrainCoincident/de

## Beschreibung

Erstelle eine deckungsgleichen Beschränkung für das ausgewählte Element

Dieses Beschränkungswerkzeug nimmt zwei Punkte als Argument und dient dazu, die beiden Punkte *deckungsgleich* zu machen. (Das bedeutet, sie wie einen Punkt zu setzen).

In der Praxis ist dieses Beschränkungswerkzeug nützlich, wenn es z.B. zu einem Bruch in einem Profil kommt - wenn zwei Linien nahe beieinander enden und verbunden werden müssen - wird eine deckungsgleiche Zwangsbedingung ihrer Endpunkte die Lücke schließen.

## Anwendung


<div class="mw-translate-fuzzy">

Wie oben erwähnt, benötigt dieses Werkzeug zwei Argumente - beides sind Punkte.

1.  Zunächst ist es notwendig, zwei verschiedene Punkte zu markieren. (**Hinweis   *** Dies funktioniert nicht, wenn du z. B. versuchst, den Start- und Endpunkt derselben Geraden zu markieren; das Markieren des Anfangs- und Endpunkts eines Bogens erzeugt einen geschlossenen Kreis oder eine Ellipse, zwingt aber die Lage der Naht auf diesen Punkt).
2.  Das Markieren eines Zeichenelements wird erreicht, indem man die Maus über das Element bewegt und die linke Maustaste drückt.
3.  Es ist auch möglich, alle Elemente innerhalb eines Rechtecks durch Klicken und Ziehen zu markieren. Beim Ziehen von links nach rechts (mit einer beliebigen vertikalen Bewegung) werden nur die Formen markiert, die sich vollständig innerhalb des Rechtecks befinden; in der anderen Richtung werden alle Formen markiert, die sich mit dem Auswahlrechteck schneiden. Dies kann verwendet werden, um nur die Knoten auszuwählen, ohne die Kanten auszuwählen, indem man ein kleines Auswahlrechteck um einige Knoten von links nach rechts zieht, solange es keine Kanten gibt, die vollständig im Rechteck enthalten sind.
4.  Ein markiertes Element ändert seine Farbe in grün. (Diese Farbe kann in **Bearbeiten → Einstellungen → Anzeige → Farben → Auswahl** angepasst werden)
5.  Nachfolgende Elemente können durch Wiederholung der obigen Prozedur(en) markiert werden. **Hinweis   *** Es ist nicht notwendig, eine spezielle Taste wie **Strg** gedrückt zu halten, um die Auswahl mehrerer Punkte in einer Zeichnung zu erreichen.
6.  Sobald du zwei Punkte markiert hast, kannst du den Befehl mit verschiedenen Methoden aufrufen   *
    -   Drücken auf den **[<img src=images/Sketcher_ConstrainCoincident.svg style="width   *16px"> [BeschränkeDeckungsgleich](Sketcher_ConstrainCoincident/de.md)** Beschränkungsschaltfläche in der Werkzeugleiste.
    -   Verwendung des Tastaturkürzels **C**.
    -   Verwendung des **Skizze → Skizzierer Beschränkungen → Beschränkung deckungsgleich** Eintrags im oberen Menü.


**Ergebnis   ***

Der Befehl bewirkt, dass die beiden Punkte *deckungsgleich* werden und durch einen einzigen Punkt ersetzt werden.


</div>


**Hinweis   ***

Um zwei Punkte deckungsgleich zu machen, muss FreeCAD unbedingt einen oder beide der ursprünglichen Punkte verschieben.

## Alternativen zur Deckungsgleich Beschränkung 

Die beiden beschränkten Elemente einer [Deckunsgleich](Sketcher_ConstrainCoincident/de.md) Beschränkung müssen Startpunkt- oder Endpunkt Knoten oder Mittelpunkte von Bögen, Kreisen oder Ellipsen sein. Einige Kombinationen, die mit einer Deckunsgleich Beschränkung nicht möglich sind, können mit anderen Beschränkung emuliert werden   *

-   Die <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width   *24px;"> [Symmetrisch](Sketcher_ConstrainSymmetric/de.md) Beschränkung kann verwendet werden, um einen Start-, End- oder Mittelpunkt auf den Mittelpunkt einer geraden Linie zu legen.
-   Eine Mittelpunkt-zu-Mittelpunkt Platzierung von zwei Geraden kann durch das Erstellen einer neuen <img alt="" src=images/Sketcher_CreatePoint.svg  style="width   *24px;"> [Punkt](Sketcher_CreatePoint/de.md) und mit zwei <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width   *24px;"> [Symmetrisch](Sketcher_ConstrainSymmetric/de.md) Beschränkungen, so dass er auf dem Mittelpunkt der beiden Linien liegt.
-   Ein Knoten kann mit einer <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width   *24px;"> [PunktAufObjekt](Sketcher_ConstrainPointOnObject/de.md) Beschränkung so beschränkt werden, dass er entlang einer Kante liegt. Beachte, dass bei dieser Beschränkung der Punkt überall auf der vollen Ausdehnung eines Segments oder einer Kurve liegen kann (also auch vor dem Startpunkt oder über den Endpunkt hinaus).
-   Eine kollineare Platzierung zweier Geraden erhält man durch Anwendung einer <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width   *24px;"> [Tangenten](Sketcher_ConstrainTangent/de.md) Beschränkung auf sie, oder durch die Kombination einer <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width   *24px;"> [PunktAufObjekt](Sketcher_ConstrainPointOnObject/de.md) Beschränkung und einer <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width   *24px;"> [Parallel](Sketcher_ConstrainParallel/de.md) Beschränkung.
-   Zwei Kanten können identisch gemacht werden, indem zwei <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width   *24px;"> [Deckungsgleich](Sketcher_ConstrainCoincident/de.md) Beschränkungen, eine für jedes Paar von Extremstellen.
-   Zwei Kreise können identisch gemacht werden, indem man eine <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width   *24px;"> [Deckungsgleich](Sketcher_ConstrainCoincident/de.md) Beschränkung die Mittelpunkte zusammenführen und eine <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width   *24px;"> [Gleichheit](Sketcher_ConstrainEqual/de.md) Beschränkung auf ihre Kanten. Bei Bögen stellt dies sicher, dass beide Bögen Teil desselben Kreises sind, während sie unterschiedliche Start- und Endpunkte haben können.

## Skripten

Die Beschränkung kann aus [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole mit dem folgenden Befehl erstellt werden   *


```pythonSketch.addConstraint(Sketcher.Constraint('Coincident',LineFixed,PointOfLineFixed,LineMoving,PointOfLineMoving)) 
```

wo    *

-    `Skizze`ist ein Skizzenobjekt.

-    `LinieFixiert`ist die Nummer der Zeile, die sich durch die Anwendung der Beschränkung nicht bewegt.

-    `PunktderfixiertenLinie`zeigt an, welcher Knoten der Linie `fixiertenLinie`, die Beschränkung erfüllen muss.

-    `LinieBewegt`ist die Nummer der Zeile, die sich durch Anwendung der Beschränkung bewegt.

-    `PunktderbewegtenLinie`zeigt an, welcher Knoten der `bewegtenLinie`, die Beschränkung erfüllen muss.

Wie die Namen `LineFixed` und `LineMoving` andeuten, bleibt, wenn beide beschränkten Knoten sich frei in jede Richtung bewegen können, der erste (im Gui zuerst ausgewählte) fest und der andere bewegt sich. Bei vorhandenen Beschränkungen dürfen sich jedoch beide Kanten bewegen.

Die [Skizzierer Skripten](Sketcher_scripting/de.md) Seite erklärt die Werte, die für `LineFixed`, `PointOfLineFixed`, `LineMoving` und `PointOfLineMoving` verwendet werden können, und enthält weitere Beispiele, wie man Beschränkungen aus Python Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainCoincident/de
