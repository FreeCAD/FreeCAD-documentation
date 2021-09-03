---
- GuiCommand:/de
   Name:Sketcher ConstrainPerpendicular
   Name/de:Skizzierer BeschränkeRechtwinklig
   MenuLocation:Skizze → Skizzierer Beschränkungeb → Beschränke Rechtwinklig
   Workbenches:[Skizzierer](Sketcher_Workbench/de.md)
   Shortcut:**N**
   SeeAlso:[Skizzierer Beschränke Winkel](Sketcher_ConstrainAngle/de.md)
---

## Beschreibung

Die Senkrechtbeschränkung bewirkt, dass zwei Linien senkrecht zueinander stehen (d. h. orthogonal) oder dass zwei Kurven an ihrem Schnittpunkt senkrecht zueinander stehen. Linien werden als unendlich behandelt, und Bögen werden als Vollkreise/Ellipsen behandelt. Die Beschränkung ist auch in der Lage, zwei Kurven zu verbinden und sie an der Verbindungsstelle senkrecht zu zwingen, ähnlich wie die **<img src=images/Sketcher_ConstrainTangent.svg style="width:16px">
[Tangentenbeschränkung](Sketcher_ConstrainTangent/de.md)**.

## Anwendung

Es gibt vier verschiedene Arten, wie die Beschränkung angewendet werden kann:

1.  zwischen zwei Kurven (nicht für alle Kurven verfügbar)
2.  zwischen zwei Endpunkten einer Kurve
3.  zwischen einer Kurve und einem Endpunkt einer anderen Kurve
4.  zwischen zwei Kurven an benutzerdefiniertem Punkt

Um eine rechtwinklige Beschränkung anzuwenden, sollte man die folgenden Schritte befolgen:

-   Wähle zwei oder drei Elemente in der Skizze aus.
-   Rufe die Beschränkung auf, durch anklicken des Symbols in der Werkzeugleiste, durch Auswahl des Menüelements oder durch Verwendung eines Tastaturkürzels.

### Zwischen zwei Kurven (direkte Rechtwinkligkeit) 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode1.png  style="width:600px;">

Zwei Kurven werden an ihrem Schnittpunkt (entweder real oder in der Verlängerung von Kurven) senkrecht zueinander gemacht, und der Schnittpunkt ist implizit. Dieser Modus wird angewendet, wenn zwei Kurven ausgewählt wurden.

**Zulässige Auswahl:**

-   Linie + Linie, Kreis, Bogen
-   Kreis, Bogen + Kreis, Bogen

Wenn die direkte Rechtwinkligkeit zwischen ausgewählten Kurven nicht unterstützt wird (z.B. zwischen einer Linie und einer Ellipse), wird automatisch ein Hilfspunkt zur Skizze hinzugefügt und der rechtwinklige Durchgangspunkt angewendet.

Anders als bei der Tangentialität ist es vollkommen in Ordnung, den Rechtwinkligkeitspunkt zu rekonstruieren, indem man einen Punkt erzeugt und ihn darauf beschränkt, auf beiden Kurven zu liegen (und damit den Punkt auf den Schnittpunkt beschränkt).

### Zwischen zwei Endpunkten (Punkt-zu-Punkt Rechtwinkligkeit) 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode2.png  style="width:600px;">

In diesem Modus werden die Endpunkte deckungsgleich gemacht, und die Verbindung wird rechtwinklig gemacht. Dieser Modus wird angewendet, wenn zwei Endpunkte von zwei Kurven ausgewählt wurden.

**Zulässige Auswahl:**

-   Endpunkt der Linie/des Bogens/Ellipsenbogens + Endpunkt der Linie/des Bogens/Ellipsenbogens (d.h. zwei Endpunkte von zwei beliebigen Kurven)

### Zwischen Kurve und Endpunkt (Punkt-zu-Kurve Rechtwinkligkeit) 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode3.png  style="width:600px;">

In diesem Modus wird ein Endpunkt einer Kurve beschränkt, so dass er auf der anderen Kurve liegt, und die Kurven werden senkrecht auf den Punkt gezwungen. Dieser Modus wird angewendet, wenn eine Kurve und ein Endpunkt einer anderen Kurve ausgewählt wurden.

**Zulässige Auswahl:**

-   Linie, Kreis, Kreisbogen, Ellipsenbogen + Endpunkt einer Linie / eines Kreises / eines Kreisbogens / eines Ellipsenbogens (im Allgemeinen jede Kurve + der Endpunkt irgend einer anderen Kurve)

### Zwischen zwei Kurven am Punkt (Rechtwinklig-Durch-Punkt) (v0.15) 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode4.png  style="width:600px;">

In diesem Modus werden zwei Kurven rechtwinklig gemacht, und der Punkt der Rechtwinkligkeit wird verfolgt. Dieser Modus wird angewendet, wenn zwei Kurven und ein Punkt ausgewählt wurden.

**Zulässige Auswahl:**

-   irgendeine Linie / Kurve + irgend eine Linie / Kurve + irgendein Punkt

\"Irgendein Punkt\" kann ein einzelner Punkt oder ein Punkt von irgendwas, zum Beispiel der Mittelpunkt eines Kreises oder der Endpunkt eines Bogens oder der Koordinatenursprung sein.

Damit die Beschränkung richtig funktioniert, muss der Punkt auf beiden Kurven zu liegen kommen. Somit wird bei der Ausführung der Beschränkung der Punkt automatisch auf die Kurven gelegt, wenn notwendig durch Hinzufügen von [Hilfsbeschränkungen](Sketcher_helper_constraint/de.md) und die Kurven werden tangential in dem Punkt angeordnet. Diese [Hilfsbeschränkungen](Sketcher_helper_constraint/de.md) sind einfach reguläre Beschränkungen. Sie können manuell hinzugefügt oder gelöscht werden.

Im Vergleich zur direkten Lotrechten ist diese Beschränkung langsamer, da es sich um Modalfreiheitsgrade handelt, aber sie unterstützt Ellipsen.

Die Platzierung des Punktes vor der Anwendung der Beschränkung ist für den Löser ein Hinweis darauf, wo die Rechtwinkligkeit sein sollte.

## Skripten

Die rechtwinklige Beschränkung kann aus [Makros](Macros/de.md) und aus der Python Konsole wie folgt erstellt werden: 
```python
# direct perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,icurve2))

# point-to-point perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,pointpos1,icurve2,pointpos2))

# point-to-curve perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,pointpos1,icurve2))

# perpendicular-via-point (plain constraint, helpers are not added automatically)
Sketch.addConstraint(Sketcher.Constraint('PerpendicularViaPoint',icurve1,icurve2,geoidpoint,pointpos)) 
``` wobei:

:\* `Sketch` ist ein Skizzenobjekt

:\* `icurve1`, `icurve2` sind zwei Ganzzahlen, die die Kurven identifizieren, die zueinander senkrecht liegen sollen. Diese Integer Zahlen sind Indexwerte der Skizze (der Wert, der vom Aufruf `Sketch.addGeometry`) zurückgegeben wird.

:\* `pointpos1`, `pointpos2` sollten `1` für den Startpunkt und `2` für den Endpunkt sein.

:\* `geoidpoint` und `pointpos` in PerpendicularViaPoint sind die Indizes, die den Punkt der Rechtwinkligkeit festlegen.

Die [Skizzierer Skripten](Sketcher_scripting/de.md) Seite erklärt die Werte, die für `icurve1`, `icurve2`, `pointpos1`, `pointpos2` und `geoidpoint` verwendet werden können, und enthält weitere Beispiele, wie man Beschränkungen aus Python Skripten erstellt.





{{Sketcher Tools navi

}}  
