# Sketcher helper constraint/de
## Überblick

<img alt="Beispiel einer Hilfsbeschränkung (Beschränkung5 - Punkt auf Kreis) für eine Tangentialbeschränkung (Beschränkung6; im Tangens über Punkt Modus). In diesem Fall wird nur eine Hilfsbeschränkung verwendet, da der Tangentenpunkt der Endpunkt des Ellipsenhauptdurchmessers ist, der von Natur aus auf der Ellipse liegt." src=images/Sketcher_helper_constraint_example1.png  style="width   *500px;">

Die Hilfsbeschränkung ist eine reguläre Skizzenbeschränkung, die als Teil einer komplexeren Beschränkung benötigt wird, aber in der Benutzeroberfläche offengelegt wird, um den Umgang mit Redundanz zu erleichtern. Für die Beschränkung [Snellius Gesetz](Sketcher_ConstrainSnellsLaw/de.md) müssen beispielsweise die beiden Linien, die Lichtstrahlen darstellen, verbunden werden ([Deckungsgleiche Beschränkung](Sketcher_ConstrainCoincident/de.md)), und die Verbindung muss auf der Benutzeroberfläche liegen ([Punkt Auf Objekt Beschränkung](Sketcher_ConstrainPointOnObject/de.md)).

Hilfsbeschränkungen werden automatisch hinzugefügt, wenn sie benötigt werden. Die Entscheidung, ob sie benötigt werden, wird derzeit durch Auswertung des Hilfs Beschränkungs Fehlers für den aktuellen Zustand der Geometrie getroffen (dies kann sich in zukünftigen Versionen ändern). Wenn der Fehler klein genug ist, wird die Beschränkung als unnötig angesehen und nicht hinzugefügt. In einigen Fällen kann diese Logik zu Fehlern führen (die Beschränkung kann versehentlich erfüllt werden, was leicht passieren kann, wenn Skizzierer Gitterfang eingeschaltet ist).

Wenn dies geschieht (eine Hilfsbeschränkung fehlt, und die erforderliche Bedingung wird andernfalls nicht erfüllt), wird die komplexe Beschränkung gebrochen. Sie wird etwas tun, aber das tatsächliche Verhalten ist undefiniert. Eine solche kaputte Beschränkung kann durch manuelles Hinzufügen der fehlenden Hilfsbeschränkung repariert werden.

Zurzeit sind Hilfsbeschränkungen erforderlich für   *

-   [Beschränkungstangente](Sketcher_ConstrainTangent/de.md) (im Tangente über Punkt Modus; zwei Punkt auf Objekt-Beschränkungen sind erforderlich).
-   [Beschränkung Rechtwinklig](Sketcher_ConstrainPerpendicular/de.md) (im Senkrecht über Punkt Modus; zwei Punkt auf Objekt Beschränkungen sind erforderlich)
-   [Beschränkung Winkel](Sketcher_ConstrainAngle/de.md) (im Winkel über Punkt Modus; zwei Punkt auf Objekt Beschränkungen sind erforderlich)
-   [Beschränkung SnelliusGesetz](Sketcher_ConstrainSnellsLaw/de.md) (Koinzidenzbeschränkung und Punkt auf Objekt Beschränkung sind erforderlich)

## Skripten

Wenn Beschränkungen, die Helfer erfordern, aus Python hinzugefügt werden, werden keine Helferbeschränkungen automatisch hinzugefügt. Man kann die automatische Entscheidungsfindung der UI Befehle in einem Skript nachbilden, indem man die folgenden Funktionen testet, die speziell für diesen Zweck hinzugefügt und in den UI Routinen verwendet werden   * 
```python
Sketch.isPointOnCurve(icurve,x,y)
``` istPunktAufKurve prüft, ob ein virtueller Punkt, der durch Skizzenkoordinaten x,y (Fließkommawerte) gegeben ist, zufällig eine virtuelle Punkt auf Objekt Beschränkung erfüllt - d.h. auf einer Kurve liegt, die durch den Kurvenindex Kurve festgelegt ist. Gibt True zurück, wenn der Punkt auf der Kurve liegt, und False, wenn er nicht auf der Kurve liegt.


```python
Sketch.calculateConstraintError(iconstr)
```

rechneBeschränkungFehler wertet eine Fehlerfunktion einer Beschränkung aus, die durch ihren Index iconstr in der Skizze angegeben ist. Wenn es nur eine Fehlerfunktion in der Beschränkung gibt, ist der Rückgabewert der vorzeichenbehaftete Rückgabewert der Fehlerfunktion. Wenn der Beschränkung mehr als eine Fehlerfunktion zugeordnet ist (d.h. die Beschränkung entfernt mehr als einen Freiheitsgrad), ist der Rückgabewert der Effektivwert aller Fehlerfunktionen (immer positiv).

## Version

Hilfsbeschränkungen wurden in v0.15.4387 eingeführt.


{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher helper constraint/de
