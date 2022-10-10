---
- GuiCommand   */de
   Name   *Sketcher ConstrainCoincident
   Name/de   *Skizzierer KoinzidentFestlegen
   MenuLocation   *Skizze → Skizzen-Beschränkungen → Koinzidenz festlegen
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

Wie oben erwähnt, benötigt dieses Werkzeug zwei Eingaben - beides sind Punkte.

1.  Zunächst ist es notwendig, zwei verschiedene Punkte zu markieren. (**Hinweis   *** Dies funktioniert nicht, wenn man z. B. versucht, den Start- und Endpunkt derselben Geraden zu markieren; das Markieren des Anfangs- und Endpunkts eines Bogens erzeugt einen geschlossenen Kreis oder eine Ellipse, legt aber die Lage der Naht auf diesen Punkt fest).
2.  Das Markieren eines Zeichenelements wird erreicht, indem man die Maus über das Element bewegt und die linke Maustaste drückt.
3.  Es ist auch möglich, alle Elemente innerhalb eines Rechtecks durch Klicken und Ziehen zu markieren. Beim Ziehen von links nach rechts (mit einer beliebigen vertikalen Bewegung) werden nur die Formen markiert, die sich vollständig innerhalb des Rechtecks befinden; in der anderen Richtung werden alle Formen markiert, die sich mit dem Auswahlrechteck schneiden. Dies kann verwendet werden, um nur die Knoten auszuwählen, ohne die Kanten auszuwählen, indem man ein kleines Auswahlrechteck um einige Knoten von links nach rechts zieht, solange es keine Kanten gibt, die vollständig im Rechteck enthalten sind.
4.  Ein markiertes Element ändert seine Farbe auf grün. (Diese Farbe kann in **Bearbeiten → Einstellungen → Anzeige → Farben → Auswahl** angepasst werden)
5.  Nachfolgende Elemente können durch Wiederholung der obigen Prozedur(en) markiert werden. **Hinweis   *** Es ist nicht notwendig, eine spezielle Taste wie **Strg** gedrückt zu halten, um die Auswahl mehrerer Punkte in einer Skizze zu erreichen.
6.  Sobald zwei Punkte markiert wurden, hat man mehrere Möglichkeiten den Befehl aufzurufen   *
    -   Die Schaltfläche **[<img src=images/Sketcher_ConstrainCoincident.svg style="width   *16px"> [Koinzidenz festlegen](Sketcher_ConstrainCoincident/de.md)** in der Werkzeugleiste drücken.
    -   Das Tastaturkürzel **C**.
    -   Den Menüeintrag **Sketch → Skizzen-Beschränkungen → [<img src=images/Sketcher_ConstrainCoincident.svg style="width   *16px"> Koinzidenz festlegen** auswählen.


**Ergebnis   ***

Der Befehl bewirkt, dass die beiden Punkte *deckungsgleich* werden und durch einen einzigen Punkt ersetzt werden.


**Hinweis   ***

Um zwei Punkte deckungsgleich zu machen, muss FreeCAD unbedingt einen oder beide der ursprünglichen Punkte verschieben.

## Alternativen zu Koinzident festlegen 

Die beiden Elemente einer Randbedingung [KoinzidentFestlegen](Sketcher_ConstrainCoincident/de.md) müssen Startpunkt- oder Endpunkt-Knoten oder Mittelpunkte von Bögen, Kreisen oder Ellipsen sein. Einige Kombinationen, die mit KoinzidentFestlegen nicht möglich sind, können mit anderen Randbedingungen emuliert werden   *

-   Die Randbedingung <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width   *24px;"> [SymmetrieFestlegen](Sketcher_ConstrainSymmetric/de.md) kann verwendet werden, um einen Start-, End- oder Mittelpunkt auf den Mittelpunkt einer geraden Linie zu legen.
-   Eine Randbdingung Mittelpunkt-auf-Mittelpunkt zweier Geraden kann emuliert werden durch das Erstellen eines neuen <img alt="" src=images/Sketcher_CreatePoint.svg  style="width   *24px;"> [Punktes](Sketcher_CreatePoint/de.md) und zweimaliger Verwendung der Randbedingung <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width   *24px;"> [SymmetrischFestlegen](Sketcher_ConstrainSymmetric/de.md), so dass er auf den Mittelpunkten beider Linien liegt.
-   Ein Knoten kann mit einer Randbedingung <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width   *24px;"> [PunktAufObjektFestlegen](Sketcher_ConstrainPointOnObject/de.md) so festgelegt werden, dass auf einer Kante liegt. Bei dieser Randbedingung kann der Punkt überall auf der vollen Ausdehnung eines Segments oder einer Kurve liegen (also auch vor dem Startpunkt oder hinter dem Endpunkt).
-   Eine kollineare (fluchtende) Platzierung zweier Geraden erhält man durch Anwendung einer Randbedingung <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width   *24px;"> [TangentialFestlegen](Sketcher_ConstrainTangent/de.md) auf sie, oder durch die Kombination der Randbedingungen <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width   *24px;"> [PunktAufObjektFestlegen](Sketcher_ConstrainPointOnObject/de.md) und <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width   *24px;"> [ParallelFestlegen](Sketcher_ConstrainParallel/de.md).
-   Zwei Kanten können deckungsgleich platziert werden, indem die Randbedingung <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width   *24px;"> [KoinzidentFestlegen](Sketcher_ConstrainCoincident/de.md) zweimal angewendet wird, auf jeweils ein Paar von Extrempunkten (Start- oder Endpunkte).
-   Zwei Kreise können deckungsgleich platziert werden, indem man mit der Randbedingung <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width   *24px;"> [KoinzidentFestlegen](Sketcher_ConstrainCoincident/de.md) die Mittelpunkte zusammenführt und die Randbedingung <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width   *24px;"> [GleichheitFestlegen](Sketcher_ConstrainEqual/de.md) auf ihre Kanten anwendet. Bei Bögen stellt dies sicher, dass beide Bögen Teil desselben Kreises sind, während sie unterschiedliche Start- und Endpunkte haben können.

## Skripten

Die Randbedingung kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit dem folgenden Befehl erstellt werden   *


```pythonSketch.addConstraint(Sketcher.Constraint('Coincident',LineFixed,PointOfLineFixed,LineMoving,PointOfLineMoving)) 
```

wobei    *

-    `Sketch`ein Skizzenobjekt ist.

-    `LineFixed`die Nummer der Linie ist, die sich durch die Anwendung der Randbedingung nicht bewegt.

-    `PointOfLineFixed`bestimmt, welcher Knoten der Linie `LineFixed` die Randbedingung erfüllen muss.

-    `LineMoving`die Nummer der Zeile ist, die sich durch Anwendung der Randbedingung bewegt.

-    `PointOfLineMoving`bestimmt, welcher Knoten der Linie `LineMoving`, die Randbedingung erfüllen muss.

Wie die Namen `LineFixed` und `LineMoving` andeuten, bleibt, wenn sich beide beteiligten Knoten frei in jede Richtung bewegen können, der erste (in der GUI zuerst ausgewählte) fest und der andere bewegt sich. Sind jedoch weitere Randbedingungen vorhanden, dürfen sich beide Kanten bewegen.

Die Seite [Sketcher Skripten](Sketcher_scripting/de.md) erklärt die Werte, die für `LineFixed`, `PointOfLineFixed`, `LineMoving` und `PointOfLineMoving` verwendet werden können, und enthält weitere Beispiele, wie man Randbedingungen mit Python-Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainCoincident/de
