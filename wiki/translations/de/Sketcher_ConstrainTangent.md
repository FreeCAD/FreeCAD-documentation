---
- GuiCommand:
   Name: Sketcher ConstrainTangent
   Name/de: Sketcher TangentialFestlegen
   MenuLocation: Sketch - Skizzen-Beschränkungen - Tangente setzen
   Workbenches: [Sketcher](Sketcher_Workbench/de.md) 
   Shortcut: **T**
   SeeAlso: [Sketcher PunktAufObjektFestlegen](Sketcher_ConstrainPointOnObject/de.md)
---

# Sketcher ConstrainTangent/de

## Beschreibung

Die Randbedingung TangentialFestlegen legt fest, dass sich zwei Kurven berühren (sie tangential sind). Linien werden als unendlich angesehen, und Bögen werden wie Vollkreise/Ellipsen behandelt. Die Randbedingung ist auch in der Lage, zwei Kurven miteinander zu verbinden, und sie gleichzeitig an der Verbindungsstelle tangential festzulegen, wodurch die Verbindung glatt wird.

Die Randbedingung TangentialFestlegen kann auch mit zwei Linien verwendet werden, um sie kollinear (fluchtend) auszurichten.

## Anwendung

Es gibt fünf verschiedene Arten, wie die Randbedingung angewendet werden kann:

1.  zwischen zwei Kurven (nicht für alle Kurven verfügbar)
2.  zwischen zwei Endpunkten einer Kurve, wodurch eine glatte Verbindung entsteht
3.  zwischen einer Kurve und einem Endpunkt einer anderen Kurve
4.  zwischen zwei Kurven an einem benutzerdefinierten Punkt
5.  zwischen zwei Linien, um eine kollineare Bedingung zu erzeugen

Um die Randbedingung TangentialFestlegen anzuwenden, sollten die folgenden Schritte befolgt werden:

-   Zwei oder drei Elemente der Skizze auswählen.
-   Die Randbedingung aufrufen, durch klicken auf das Symbol in der Werkzeugleiste, durch Auswahl des Menüelements oder durch Verwendung eines Tastaturkürzels.

### Zwischen zwei Kurven (direkte Tangentialität) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode1.png  style="width:600px;">

Zwei Kurven werden so angeordnet, dass sie sich tangential berühren; der Berührungspunkt wird implizit bestimmt. Dieser Modus wird angewandt, wenn zwei Kurven als ganzes ausgewählt werden.

**Zulässige Auswahl:**

-   Linie + Linie, Kreis, Kreisbogen, Ellipse, Ellipsenbogen
-   Kreis, Kreisbogen + Kreis, Kreisbogen

Wenn die direkte Tangentialität zwischen den ausgewählten Kurven nicht unterstützt wird (zum Beispiel zwischen einem Kreis und einer Ellipse), wird ein Hilfspunkt automatisch eingefügt und die Tangentialität mittels Punkt wird angewandt.

Es wird nicht empfohlen den Berührungspunkt zu bestimmen, indem ein Punkt generiert wird, der so eingeschränkt wird, dass er auf beiden Kurven liegt. Dies funktioniert im Prinzip, aber die Konvergenz der Lösung wird erheblich erschwert, sprunghafter und benötigt mehr als doppelt so vieler Iterationen als normal. Wenn der Berührungspunkt benötigt wird, sollte andere Einschränkungen benutzt werden, um ihn zu bestimmen.

### Zwischen zwei Endpunkten (Punkt-zu-Punkt Tangentialität) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode2.png  style="width:600px;">

In diesem Modus werden die Endpunkte deckungsgleich gemacht und die Verbindung wird tangential gemacht (C1-glatt oder \"scharf\", je nach Platzierung der Kurven vor Anwendung der Beschränkung). Dieser Modus wird angewendet, wenn zwei Endpunkte von zwei Kurven ausgewählt wurden. Wenn du diese Art der Tangente willst, darfst du nicht die Deckungsgleichheit plus die Tangente zwischen den Kurven/Linien verwenden. Der Löser kann für diese Kombination keine stabilen Lösungen erzeugen und ersetzt die Beschränkungen entsprechend.

**Zulässige Auswahl:**

-   Endpunkt einer Linie / eines Bogens / eines Ellipsenbogens + Endpunkt einer Linie / eines Bogens / eines Ellipsenbogens (im Allgemeinen zwei Endpunkte von jedweden Kurven)

### Zwischen einer Kurve und einem Endpunkt (Punkt-zu-Kurve Tangentialität) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode3.png  style="width:600px;">

In diesen Modus wird der Endpunkt der einen Kurve auf die andere Kurve gelegt und die Kurven berühren sich tangential in diesen Punkt. Dieser Modus wird angewandt, wenn eine Kurve und der Endpunkt einer anderen Kurve ausgewählt wurden.

**Zulässige Auswahl:**

-   Linie, Kreis, Kreisbogen, Ellipsenbogen + Endpunkt einer Linie / eines Kreises / eines Kreisbogens / eines Ellipsenbogens (im Allgemeinen jede Kurve + der Endpunkt irgend einer anderen Kurve)

### Zwischen zwei Kurven an einem Punkt (Punkt-Tangentialität) (v0.15) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode4.png  style="width:600px;">

In diesen Modus werden zwei Kurven tangential an einem ausgewählten Punkt angeordnet. Dieser Modus wird angewandt, wenn zwei Kurven und ein Punkt ausgewählt werden.

**Zulässige Auswahl:**

-   irgendeine Linie / Kurve + irgend eine Linie / Kurve + irgendein Punkt

\"Irgendein Punkt\" kann ein einzelner Punkt oder ein Punkt von irgendwas, zum Beispiel der Mittelpunkt eines Kreises oder der Endpunkt eines Bogens oder der Koordinatenursprung sein.

Damit die Beschränkung korrekt funktioniert, muss der Punkt auf beiden Kurven liegen. Wenn also die Beschränkung aufgerufen wird, wird der Punkt automatisch an beide Kurven gebunden ([Hilfsbeschränkungen](Sketcher_helper_constraint/de.md) wird hinzugefügt, falls erforderlich), und die Kurven werden an den Punkt tangential gezwungen. Bei diesen [Hilfsbeschränkungen](Sketcher_helper_constraint/de.md) handelt es sich um einfache reguläre Beschränkungen. Sie können manuell hinzugefügt oder gelöscht werden.

Verglichen mit der direkten Tangentialität ist diese Beschränkung langsamer, weil mehr Freiheitsgrade involviert sind, aber wenn der Berührungspunkt benötigt wird, ist dies der empfohlene Modus, weil er eine bessere Konvergenz der Lösung aufweist verglichen mit der direkten Tangentialität + Punkt auf zwei Kurven.

Die Platzierung des Punktes vor der Anwendung der Beschränkung ist ein Hinweis für den Löser, wo die Tangentialität sein soll. Mit diesem Modus ist es möglich zwei Ellipsen so anzuordenen, dass sie sich gegenseitig in zwei Punkten berühren.

### Zwischen zwei Linien (kollinear) 

<img alt="" src=images/Sketcher_ConstraintTangent_mode5.png  style="width:600px;">

**Akzeptierte Auswahl:**

-   jede Linie/Knoten + jede Linie/Knoten

## Skripten

Die tangentiale Beschränkung kann aus [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole wie folgt erstellt werden: 
```python
# direct tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,icurve2))

# point-to-point tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,pointpos1,icurve2,pointpos2))

# point-to-curve tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,pointpos1,icurve2))

# tangent-via-point (plain constraint, helpers are not added automatically)
Sketch.addConstraint(Sketcher.Constraint('TangentViaPoint',icurve1,icurve2,geoidpoint,pointpos)) 
``` wobei:

  - `Sketch` ist ein Skizzenobjekt

  - `icurve1`, `icurve2` sind zwei Integer Zahlen, die die Kurven identifizieren, die zueinander tangential liegen sollen. Dies Integer Zahlen sind Indexwerte der Skizze (der Wert, der vom Aufruf `Sketch.addGeometry` zurückgegeben wird).

  - `pointpos1`, `pointpos2` sollten 1 für den Startpunkt und 2 für den Endpunkt sein.

  - `geoidpoint` und `pointpos` in `TangentViaPoint` sind die Indexe, die den Punkt der Tangentialität spezifizieren.

Die [Skizzierer Skripten](Sketcher_scripting/de.md) Seite erklärt die Werte, die für `incurve1`, `incurve2`, `pointpos1`, `pointpos2`, `geoidpoint` und `pointpos` verwendet werden können und enthält weitere Beispiele, wie man Beschränkungen aus Python Skripten erstellt.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainTangent/de
