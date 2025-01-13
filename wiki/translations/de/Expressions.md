# Expressions/de
## Übersicht

Es ist möglich, Eigenschaften unter Verwendung von mathematischen Ausdrücken festzulegen. In der GUI zeigen Drehfelder oder Eingabefelder, die an Eigenschaften gebunden sind, ein blaues Symbol <img alt="" src=images/Bound-expression.svg  style="width:16px;">, wenn aktiviert. Klicken auf das Symbol oder Eingeben des Gleichheitszeichens **&#61;** öffnet den Ausdruckseditor für diese bestimmte Eigenschaft. Zeigt das Eingabefeld eine Schaltfläche **...** anstatt eines Symbols, kann der Ausdruckseditor mit einem Rechtsklick auf die Eigenschaft und Auswählen von **Expression...** im Kontextmenü geöffnet werden.

Ein FreeCAD-Ausdruck ist ein mathematischer Ausdruck, der die mathematischen Standard- [Operatoren](#Unterstützte_Operatoren.md), [Funktionen](#Unterstützte_Funktionen.md) und [vorgegebene Konstanten](#Unterstützte_Konstanten.md) verwendet, wie unten beschrieben. Zusätzlich können Ausdrücke auf Objekteigenschaften referenzieren und auch [Bedingte Ausdrücke](#Bedingte_Ausdrücke.md) verwenden. Zahlen in Ausdrücken können optionale [Einheiten](#Einheiten.md) angefügt werden.

Zahlen können entweder ein Komma `,` oder einen Dezimalpunkt `.` zur Trennung von Ganzzahlen und Nachkommastellen verwenden. Wenn ein Dezimaltrennzeichen benutzt wird, *muss* danach mindestens eine Ziffer folgen. Daher sind die Ausdrücke `1.+2.` und `1,+2,` ungültig, aber `1.0 + 2.0` und `1,0 + 2,0` sind gültig.

Operatoren und Funktionen beachten die Einheiten und erfordern gültige Kombinationen von Einheiten, falls verfügbar. Zum Beispiel ist `2mm + 4mm` ein gültiger Ausdruck, während `2mm + 4` kein gültiger Ausdruck ist. Dies gilt auch für Referenzen auf Objekteigenschaften, die Einheiten beinhalten, wie z.B. Längeneigenschaften. Daher ist `Pad001.Length + 1` ungültig, da es einer Eigenschaft mit Längeneinheit nur eine Zahl ohne Einheit hinzufügt; gültig wäre `Pad001.Length + 1mm`.

Einige Fehler im Zusammenhang mit Einheiten können unverständlich erscheinen, wenn Ausdrücke abgelehnt werden oder die Ergebnisse nicht den Einheiten der bearbeiteten Eigenschaft entsprechen. Ein paar Beispiele:


`1/2mm`

wird nicht als halber Millimeter angesehen sondern als `1/(2mm)` und ergibt: `0.5 mm^-1`.


`sqrt(2)mm`

ist ungültig, da der Funktionsaufruf keine Zahl ist. Dies muss so eingegeben werden: `sqrt(2) * 1mm`.



### Funktionsargumente

Mehrere Argumente zu einer Funktion können entweder durch ein Semikolon  gefolgt von einem Leerzeichen `,` getrennt werden. Im letzteren Fall wird das Komma nach der Eingabe in ein Semikolon umgewandelt. Wenn ein Semikolon verwendet wird, ist kein Leerzeichen am Ende des Semikolons erforderlich.

Die Argumente können Verweise auf Zellen in einer Kalkulationstabelle enthalten. Ein Zellverweis besteht aus dem großen Zeilenbuchstaben der Zelle, gefolgt von ihrer Spaltennummer, zum Beispiel `A1`. Eine Zelle kann auch durch den Alias der Zelle referenziert werden, zum Beispiel `Tabellenblatt.MeineTeilbreite`.



### Referenzierende Objekte 

Wie oben schon gezeigt, kann ein Objekt über seinen {{PropertyData/de|Namen}} referenziert werden. Es kann aber auch seine {{PropertyData/de|Benennung}} (Label) verwendet werden. Im Falle einer {{PropertyData/de|Benennung}} muss sie in doppelten `<<` und `>>` Symbolen eingeschlossen sein, wie z.B. `<<Benennung>>`.

Jede Eigenschaft eines Objekts kann referenziert werden. Um sich beispielsweise auf die Höhe eines Zylinders zu beziehen, kann `Zylinder.Height` oder `<<Benennung_des_Zylinders>>.Height` verwendet werden.

Für weitere Informationen über das Referenzieren von Objekten siehe [Auf CAD-Daten referenzieren](#Auf_CAD-Daten_referenzieren.md). 

## Unterstützte Konstanten 

Die folgenden Konstanten werden unterstützt:

  Konstante   Beschreibung
   
  **e**       [Eulersche Zahl](https://de.wikipedia.org/wiki/Eulersche_Zahl)
  **pi**      [Kreiszahl $\pi$](https://de.wikipedia.org/wiki/Kreiszahl)


{{Top}}



## Unterstützte Operatoren 

Die folgenden Operatoren werden untertstützt:

  Operator   Beschreibung
   
  **+**      [Addition](https://de.wikipedia.org/wiki/Addition)
  **-**      [Subtraktion](https://de.wikipedia.org/wiki/Subtraktion)
  **\***     [Multiplikation](https://de.wikipedia.org/wiki/Multiplikation)
  **/**      Fließkomma [Division](https://de.wikipedia.org/wiki/Division_(Mathematik))
  **%**      [Division mit Rest](https://de.wikipedia.org/wiki/Division_mit_Rest)
  **\^**     [Potenz](https://de.wikipedia.org/wiki/Potenz_(Mathematik))


{{Top}}



## Unterstützte Funktionen 



### Allgemeine mathematische Funktionen 

Die folgenden mathematischen Funktionen werden untertstützt:



#### Trigonometrische Funktionen 

[Trigonometrische Funktionen](https://de.wikipedia.org/wiki/Trigonometrische_Funktion) verwenden Grad als Standardeinheit. Für die Angabe im Bogenmaß wird ersten Wert in einem Ausdruck hinzugefügt. So ist z.B. `cos(45)` das gleiche, wie `cos(pi rad / 4)`. Ausdrücke in Grad können entweder `deg` oder `°` verwenden, z.B. `360deg - atan2(3; 4)` oder `360&deg; - atan2(3; 4)`. Ein Ausdruck, der ohne Einheiten angegeben ist und aus Kompatibilitätsgründen in Grad oder Bogenmaß umgewandelt werden muss, wird entsprechend mit `1deg`, `1°` oder `1rad` multipliziert, z.B. `(360 - X) * 1deg`; `(360 - X) * 1°`; `(0.5 + pi / 2) * 1rad`.

++++
| Funktion               | Beschreibung                                                                                                                                                           | Eingabebereich                                                |
+========================+========================================================================================================================================================================+===============================================================+
|         | [arccos](https://de.wikipedia.org/wiki/Arkusfunktion#Beziehungen_zwischen_den_Funktionen)                                                                              | -1 \<= x \<= 1                                                |
| `acos(x)`     |                                                                                                                                                                        |                                                               |
|                     |                                                                                                                                                                        |                                                               |
++++
|         | [arcsin](https://de.wikipedia.org/wiki/Arkusfunktion#Beziehungen_zwischen_den_Funktionen)                                                                              | -1 \<= x \<= 1                                                |
| `asin(x)`     |                                                                                                                                                                        |                                                               |
|                     |                                                                                                                                                                        |                                                               |
++++
|         | [arctan](https://de.wikipedia.org/wiki/Arkusfunktion#Beziehungen_zwischen_den_Funktionen), Bereich des Rückgabewertes: -90° \< Wert \< 90°                             | alle                                                          |
| `atan(x)`     |                                                                                                                                                                        |                                                               |
|                     |                                                                                                                                                                        |                                                               |
++++
|         | [arctan2](https://de.wikipedia.org/wiki/Arctan2#Implementierungen) von *y/x* unter Berücksichtigung des Quadranten, Bereich des Rückgabewertes: -180° \< Wert \<= 180° | alle, die ungültige Eingabe x = y = 0 gibt 0 zurück           |
| `atan2(y; x)` |                                                                                                                                                                        |                                                               |
|                     |                                                                                                                                                                        |                                                               |
++++
|         | [cos](https://de.wikipedia.org/wiki/Trigonometrische_Funktion#Definition)                                                                                              | alle                                                          |
| `cos(x)`      |                                                                                                                                                                        |                                                               |
|                     |                                                                                                                                                                        |                                                               |
++++
|         | [cosh](https://de.wikipedia.org/wiki/Hyperbelfunktion#Definition)                                                                                                      | alle                                                          |
| `cosh(x)`     |                                                                                                                                                                        |                                                               |
|                     |                                                                                                                                                                        |                                                               |
++++
|         | [sin](https://de.wikipedia.org/wiki/Trigonometrische_Funktion#Definition)                                                                                              | alle                                                          |
| `sin(x)`      |                                                                                                                                                                        |                                                               |
|                     |                                                                                                                                                                        |                                                               |
++++
|         | [sinh](https://de.wikipedia.org/wiki/Hyperbelfunktion#Definition)                                                                                                      | alle                                                          |
| `sinh(x)`     |                                                                                                                                                                        |                                                               |
|                     |                                                                                                                                                                        |                                                               |
++++
|         | [tan](https://de.wikipedia.org/wiki/Trigonometrische_Funktion#Definition)                                                                                              | alle, außer x = n\*90 mit n = odd integer (ungerade Ganzzahl) |
| `tan(x)`      |                                                                                                                                                                        |                                                               |
|                     |                                                                                                                                                                        |                                                               |
++++
|         | [tanh](https://de.wikipedia.org/wiki/Hyperbelfunktion#Definition)                                                                                                      | alle                                                          |
| `tanh(x)`     |                                                                                                                                                                        |                                                               |
|                     |                                                                                                                                                                        |                                                               |
++++
|         | [Pythagoreische Addition](https://de.wikipedia.org/wiki/Pythagoreische_Addition) (**Hypot**enuse), z.B. hypot(4; 3) = 5.                                               | x und y \>= 0                                                 |
| `hypot(x; y)` |                                                                                                                                                                        |                                                               |
|                     |                                                                                                                                                                        |                                                               |
++++
|         | Die gegebene Hypotenuse und eine Seite ergibt die andere Seite eines Dreiecks (Kathete), z.B. cath(5; 3) = 4.                                                          | x \>= y \>= 0                                                 |
| `cath(x; y)`  |                                                                                                                                                                        |                                                               |
|                     |                                                                                                                                                                        |                                                               |
++++



#### Exponential- und Logarithmusfunktionen 

  Funktion                                    Beschreibung                                                                                        Eingabebereich
    
  exp(x)                                      [Exponentialfunktion](https://en.wikipedia.org/wiki/Exponential_function#Definition)                alle
  log(x)                                      [Natürlicher Logarithmus](https://de.wikipedia.org/wiki/Logarithmus#Nat%C3%BCrlicher_Logarithmus)   x \> 0
  log10(x)                                    [Dekadischer Logarithmus](https://de.wikipedia.org/wiki/Dekadischer_Logarithmus)                    x \> 0
  pow(x, y)                                   [Potenz (Mathematik)](https://de.wikipedia.org/wiki/Potenz_(Mathematik))                            alle
  sqrt(x)                                     [Quadratwurzel](https://de.wikipedia.org/wiki/Quadratwurzel)                                        x \>= 0
  cbrt(x) {{Version/de|0.21}}   [Kubikwurzel](https://de.wikipedia.org/wiki/Wurzel_(Mathematik)#Quadrat-_und_Kubikwurzel)           x \>= 0



#### Rundung, Trunkierung und Modulo 

++++
| Funktion             | Beschreibung                                                                                                                                                   | Eingabebereich    |
+======================+================================================================================================================================================================+===================+
|       | [Betragsfunktion](https://de.wikipedia.org/wiki/Betragsfunktion)                                                                                               | alle              |
| `abs(x)`    |                                                                                                                                                                |                   |
|                   |                                                                                                                                                                |                   |
++++
|       | [Aufrundungsfunktion](https://de.wikipedia.org/wiki/Abrundungsfunktion_und_Aufrundungsfunktion), kleinster ganzzahliger Wert größer oder gleich x              | alle              |
| `ceil(x)`   |                                                                                                                                                                |                   |
|                   |                                                                                                                                                                |                   |
++++
|       | [Abrundungsfunktion](https://de.wikipedia.org/wiki/Abrundungsfunktion_und_Aufrundungsfunktion), größter ganzzahliger Wert kleiner oder gleich x                | alle              |
| `floor(x)`  |                                                                                                                                                                |                   |
|                   |                                                                                                                                                                |                   |
++++
|       | [Division mit Rest](https://de.wikipedia.org/wiki/Division_mit_Rest) nach einer Division *x* durch *y*, das Vorzeichen des Ergebnisses ist das des Dividenden. | alle, außer y = 0 |
| `mod(x, y)` |                                                                                                                                                                |                   |
|                   |                                                                                                                                                                |                   |
++++
|       | [Rundung](https://de.wikipedia.org/wiki/Rundung) auf die nächste Ganzzahl                                                                                      | alle              |
| `round(x)`  |                                                                                                                                                                |                   |
|                   |                                                                                                                                                                |                   |
++++
|       | [Trunkierung](https://de.wikipedia.org/wiki/Trunkierung_(Mathematik)) auf die nächste Ganzzahl in Richtung Null (Nachkommastellen entfernen).                  | alle              |
| `trunc(x)`  |                                                                                                                                                                |                   |
|                   |                                                                                                                                                                |                   |
++++


{{Top}}



### Statistische / Aggregatfunktionen 

[Aggregatfunktion](https://de.wikipedia.org/wiki/Aggregatfunktion) verwenden ein oder mehrere Argumente.
Einzelne Argumente für Aggregatfunktionen können aus Zellbereichen bestehen. Ein Zellbereich wird durch zwei Zellbezüge ausgedrückt, die durch einen Doppelpunkt {{Incode|:}} getrennt sind, zum Beispiel {{Incode|Durchschnitt(B1:B8)}} oder {{Incode|Summe(A1:A4; B1:B4)}}. Die Zellbezüge können auch Zell Aliase verwenden, zum Beispiel {{Incode|Durchschnitt(StartTemp:EndTemp)}}.

Diese Aggregatfunktionen werden unterstützt:

++++
| Funktion                         | Beschreibung                                                                                                                                                  | Eingabebereich |
+==================================+===============================================================================================================================================================+================+
|                   | [Arithmetisches Mittel](https://de.wikipedia.org/wiki/Arithmetisches_Mittel) der Werte der Argumente, dasselbe, wie sum(a; b; c; \...) / count(a; b; c; \...) | alle           |
| `average(a; b; c; ...)` |                                                                                                                                                               |                |
|                               |                                                                                                                                                               |                |
++++
|                   | [Zählen](https://de.wikipedia.org/wiki/Z%C3%A4hlen) der Argumente, üblicherweise für Zellbereiche genutzt                                                     | alle           |
| `count(a; b; c; ...)`   |                                                                                                                                                               |                |
|                               |                                                                                                                                                               |                |
++++
|                   | [Extremwert (Maximum)](https://de.wikipedia.org/wiki/Extremwert)-Werte der Argumente                                                                          | alle           |
| `max(a; b; c; ...)`     |                                                                                                                                                               |                |
|                               |                                                                                                                                                               |                |
++++
|                   | [Minimum (Minimum)](https://de.wikipedia.org/wiki/Extremwert)-Werten der Argumente                                                                            | alle           |
| `min(a; b; c; ...)`     |                                                                                                                                                               |                |
|                               |                                                                                                                                                               |                |
++++
|                   | [Varianz (Stochastik)](https://de.wikipedia.org/wiki/Varianz_(Stochastik)) der Werte der Argumente                                                            | alle           |
| `stddev(a; b; c; ...)`  |                                                                                                                                                               |                |
|                               |                                                                                                                                                               |                |
++++
|                   | [Summe](https://de.wikipedia.org/wiki/Summe) der Werte der Argumente, üblicherweise für Zellbereiche genutzt                                                  | alle           |
| `sum(a; b; c; ...)`     |                                                                                                                                                               |                |
|                               |                                                                                                                                                               |                |
++++


{{Top}}



### Zeichenkettenhandhabung



#### Zeichenkettenerkennung

Zeichenketten werden in Ausdrücken erkannt, indem sie in doppelte öffnende/schließende Winkel eingeschlossen werden (so wie Beschriftungen).

Im folgenden Beispiel wird \"TEXT\" als eine Zeichenkette erkannt: {{Incode|<<TEXT>>}}



#### Zeichenkettenverkettung

Zeichenketten können durch das \'+\'-Zeichen aneinandergehängt werden.

Das folgende Beispiel {{Incode|<<MY>>+<<TEXT>>}} wird verbunden zu \"MYTEXT\".



#### Umwandlung in Zeichenketten 

Numerische Werte können mit der Funktion `str` in Zeichenketten gewandelt werden:


`str(Box.Length.Value)`



#### Zeichenkettenformatierung

Zeichenkettenformatierung wird unterstützt durch die (alte) %-Form von Python.

Alle %-Spezifizierer wie in der (engl.) [Python documentation](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting) definiert.

Hat man bspw. einen mit den Vorgabewerten erstellten Würfel namens \'Box\' (FreeCAD-Standardbezeichnung) mit 10mm-Kantenlänge, wird der folgende Ausdruck `<<Würfellänge: %s>> % Box.Length` erweitert zu \"Würfellänge: 10.0 mm\"

Für mehr als einen %-Spezifizierer verwendet man folgende Syntax: `<<Würfellänge ist %s und Würfelbreite ist %s>> % tuple(Box.Length; Box.Width)`. Oder man verwendet die Verkettung: {{Incode|<<Würfellänge ist %s>> % Box.Length + << und Länge ist %s>> % Box.Width}}. Beide ergeben zusammen \"Würfellänge ist 10.0 mm und Breite ist 10.0 mm\".

Eine FreeCAD-Beispieldatei, die Zeichenkettenformatierung zeigt, ist unter [im Forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=58657) verfügbar (engl.) 

### Funktionen zur Objekterstellung 

Die folgenden Objekte können in Ausdrücken durch die folgenden Funktionen erstellt werden:

++++
| Art                                                            | Funktion                                                                           | Beschreibung                                                                                                                                                                                                                                                                                                                                              |
+================================================================+====================================================================================+===========================================================================================================================================================================================================================================================================================================================================================+
|                                                 |                                                                     | Beispiel: `tuple(2; 1; 2)`                                                                                                                                                                                                                                                                                                         |
| `Tuple`                                               | `tuple(a; b; ...)`                                                        |                                                                                                                                                                                                                                                                                                                                                           |
|                                                             |                                                                                 |                                                                                                                                                                                                                                                                                                                                                           |
++++
|                                                 |                                                                     | Beispiel: `list(2; 1; 2)`                                                                                                                                                                                                                                                                                                          |
| `List`                                                | `list(a; b; ...)`                                                         |                                                                                                                                                                                                                                                                                                                                                           |
|                                                             |                                                                                 |                                                                                                                                                                                                                                                                                                                                                           |
++++
| [`Vector`](Vector_API.md)       |                                                                     | Erstellt einen Vektor unter Verwendung dreier einheitenloser Werte oder dreier Werte mit einer Längeneinheit (`Length` unit values). Beispiel: `vector(2; 1; 3)`                                                                                                                                            |
|                                                                | `vector(x; y; z)`                                                         |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                                           |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                | `create(<<vector>>; x; y; z)`                                             |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                                           |
++++
| [`Matrix`](Matrix_API.md)       | matrix(                                                                          | Erstellt eine 4x4 Matrix in [row-major order](https://en.wikipedia.org/wiki/Row-_and_column-major_order): $\begin{bmatrix}                                                                                                                                                                                                                                |
|                                                                |   a~11~; a~12~; a~13~; a~14~;                                    | a_{11} & a_{12} & a_{13} & a_{14} \\                                                                                                                                                                                                                                                                                                                      |
|                                                                |   a~21~; a~22~; a~23~; a~24~;                                    | a_{21} & a_{22} & a_{23} & a_{24} \\                                                                                                                                                                                                                                                                                                                      |
|                                                                |   a~31~; a~32~; a~33~; a~34~;                                    | a_{31} & a_{32} & a_{33} & a_{34} \\                                                                                                                                                                                                                                                                                                                      |
|                                                                |   a~41~; a~42~; a~43~; a~44~                                       | a_{41} & a_{42} & a_{43} & a_{44} \\                                                                                                                                                                                                                                                                                                                      |
|                                                                | )                                                                                | \end{bmatrix}$                                                                                                                                                                                                                                                                                                                                            |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                    | Es kann auch genau ein Argument übergeben werden, wie z.B. `matrix(1)`, was eine Einheitsmatrix erstellt.                                                                                                                                                                                                                          |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                    | Beispiel: `matrix(1; 2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12; 13; 14; 15; 16)`                                                                                                                                                                                                                                                          |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                | `create(<<matrix>>; a<sub>11</sub>; a<sub>12</sub>; ...; a<sub>44</sub>)` |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                                           |
++++
|                                                 |                                                                     | Erstellt eine `Rotation` durch Angabe von `axis` (`Vector`) und `angle` (`Angle` mit oder ohne Einheiten), oder durch drei Euler-Winkel `α`, `β`, `γ`. Beispiele: |
| `Rotation`                                            | `rotation(axis; angle)`                                                   |                                                                                                                                                                                                                                                                                                                                                           |
|                                                             |                                                                                 | -                                                                                                                                                                                                                                                                                                                                          |
|                                                                |                                                                                    |     `rotation(vector(0; 1; 0); 45)`                                                                                                                                                                                                                                                                                                              |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                                          |
|                                                                |                                                                                    |     `create(<<rotation>>; 30; 30; 30)`                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                        |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                | `rotation(α; β; γ)`                                                       |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                                           |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                | `create(<<rotation>>; axis; angle)`                                       |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                                           |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                | `create(<<rotation>>; α; β; γ)`                                           |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                                           |
++++
| [`Placement`](Placement_API.md) |                                                                     | Erstellt ein `Placement` mit verschiedenen Parametern, einschließlich:                                                                                                                                                                                                                                                             |
|                                                                | `placement(base; rotation)`                                               |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                 | -                                                                                                                                                                                                                                                                                                                                          |
|                                                                |                                                                                    |     `base`                                                                                                                                                                                                                                                                                                                                       |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |     : Ausgangspunkt (`Vector`)                                                                                                                                                                                                                                                                                                     |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                                          |
|                                                                |                                                                                    |     `center`                                                                                                                                                                                                                                                                                                                                     |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |     : Mittelpunkt (`Vector`)                                                                                                                                                                                                                                                                                                       |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                                          |
|                                                                |                                                                                    |     `rotation`                                                                                                                                                                                                                                                                                                                                   |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |     : `Rotation`                                                                                                                                                                                                                                                                                                                   |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                                          |
|                                                                |                                                                                    |     `axis`                                                                                                                                                                                                                                                                                                                                       |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |     : Drehachse (`Vector`)                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                                          |
|                                                                |                                                                                    |     `angle`                                                                                                                                                                                                                                                                                                                                      |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |     : Drehwinkel (Wert ohne Einheit oder `Angle` Wert mit Einheit)                                                                                                                                                                                                                                                                 |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                                          |
|                                                                |                                                                                    |     `matrix`                                                                                                                                                                                                                                                                                                                                     |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |     : `Matrix`                                                                                                                                                                                                                                                                                                                     |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                    | Beispiele:                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                                          |
|                                                                |                                                                                    |     `placement(vector(2; 1; 3); rotation(vector(0; 0; 1); 45))`                                                                                                                                                                                                                                                                                  |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                                          |
|                                                                |                                                                                    |     `create(<<placement>>; create(<<vector>>; 2; 1; 2); create(<<rotation>>; create(<<vector>>; 0; 1; 0); 45))`                                                                                                                                                                                                                                  |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                        |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                | `placement(base; rotation; center)`                                       |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                                           |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                | `placement(base; axis; angle)`                                            |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                                           |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                | `placement(matrix)`                                                       |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                                           |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                | `create(<<placement>>; ...)`                                              |                                                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                                           |
++++


{{Top}}



### Vektorfunktionen

Funktionen: {{Version/de|1.0}}.

+++
| Function / Operator                 | Description                                                                                                                                                                               |
+=====================================+===========================================================================================================================================================================================+
|                      | Addiert zwei Vektoren.                                                                                                                                                                    |
| `v1 + v2`                  |                                                                                                                                                                                           |
|                                  |                                                                                                                                                                                           |
+++
|                      | Subtrahiert zwei Vektoren.                                                                                                                                                                |
| `v1 - v2`                  |                                                                                                                                                                                           |
|                                  |                                                                                                                                                                                           |
+++
|                      | Skaliert einen Vektor gleichförmig mit Faktor `s`.                                                                                                                 |
| `v * s`                    |                                                                                                                                                                                           |
|                                  |                                                                                                                                                                                           |
+++
|                      | Winkel zwischen zwei Vektoren in Grad.                                                                                                                                                    |
| `vangle(v1; v2)`           |                                                                                                                                                                                           |
|                                  |                                                                                                                                                                                           |
+++
|                      | Kreuzprodukt zweier Vektoren $v_1 \times v_2$.                                                                                                                                            |
| `vcross(v1; v2)`           |                                                                                                                                                                                           |
|                                  |                                                                                                                                                                                           |
+++
|                      | Skalarprodukt zweier Vektoren $v_1 \cdot v_2$.                                                                                                                                            |
| `v1 * v2`                  |                                                                                                                                                                                           |
|                                  |                                                                                                                                                                                           |
+++
|                      |                                                                                                                                                                                           |
| `vdot(v1; v2)`             |                                                                                                                                                                                           |
|                                  |                                                                                                                                                                                           |
+++
|                      | Abstand zwischen Vektor `v1` und einer Linie durch `v2` in Richtung `v3`.                                            |
| `vlinedist(v1; v2; v3)`    |                                                                                                                                                                                           |
|                                  |                                                                                                                                                                                           |
+++
|                      | Abstand zwischen Vektor `v1` und dem dichtesten Punkt auf einem Linienabschnitt (Strecke) von `v2` nach `v3`.        |
| `vlinesegdist(v1; v2; v3)` |                                                                                                                                                                                           |
|                                  |                                                                                                                                                                                           |
+++
|                      | Projiziert Vektor `v1` auf eine Linie durch `v2` in Richtung `v3`.                                                   |
| `vlineproj(v1; v2; v3)`    |                                                                                                                                                                                           |
|                                  |                                                                                                                                                                                           |
+++
|                      | Normalisiert einen Vektor zu einem Einheitsvektor.                                                                                                                                        |
| `vnormalize(v)`            |                                                                                                                                                                                           |
|                                  |                                                                                                                                                                                           |
+++
|                      | Abstand zwischen Vektor `v1` und einer Ebene, die durch einen Punkt `v2` und eine Normale `v3` festgelegt wird.      |
| `vplanedist(v1)`           |                                                                                                                                                                                           |
|                                  |                                                                                                                                                                                           |
+++
|                      | Projiziert Vektor `v1` auf eine Ebene, die durch einen Punkt `v2` und eine Normale `v3` festgelegt wird.             |
| `vplaneproj(v1)`           |                                                                                                                                                                                           |
|                                  |                                                                                                                                                                                           |
+++
|                      | Skaliert einen Vektor ungleichförmig mit den Faktoren `sx` in X-Richtung, `sy` in Y-Richtung und `sz` in Z-Richtung. |
| `vscale(v; sx; sy; sz)`    |                                                                                                                                                                                           |
|                                  |                                                                                                                                                                                           |
+++
|                      |                                                                                                                                                                                           |
| `vscalex(v; sx)`           |                                                                                                                                                                                           |
|                                  |                                                                                                                                                                                           |
+++
|                      |                                                                                                                                                                                           |
| `vscaley(v; sy)`           |                                                                                                                                                                                           |
|                                  |                                                                                                                                                                                           |
+++
|                      |                                                                                                                                                                                           |
| `vscalez(v; sz)`           |                                                                                                                                                                                           |
|                                  |                                                                                                                                                                                           |
+++


{{Top}}



### Matrixfunktionen


`Rotation`

Und `Placement` können beide durch eine `Matrix` dargestellt werden. Die folgenden Funktionen akzeptieren alle eine `Matrix`, eine `Rotation` oder ein `Placement` als ihren ersten Parameter, in der folgenden Tabelle mit `m` gekennzeichnet. Die Art der zurückgegebenen Objekte ist dieselbe, wie die des Objekts, das mit dem ersten Argument übergeben wurde, außer wenn `mtranslate` auf eine `Rotation` angewandt wird; in dem Falle wird ein `Placement` zurückgegeben.

+++
| Funktion                           | Beschreibung                                                                                                                                                                                                                                                                                                                     |
+====================================+==================================================================================================================================================================================================================================================================================================================================+
|                     | Berechnet die [Inverse Matrix](https://de.wikipedia.org/wiki/Inverse_Matrix).                                                                                                                                                                                                                                                    |
| `minvert(m)`              |                                                                                                                                                                                                                                                                                                                                  |
|                                 |                                                                                                                                                                                                                                                                                                                                  |
+++
|                     | [Rotieren](https://en.wikipedia.org/wiki/Transformation_matrix#Rotation_2) durch:                                                                                                                                                                                                                                                |
| `mrotate(m; rotation)`    |                                                                                                                                                                                                                                                                                                                                  |
|                                 | -   eine `Rotation`                                                                                                                                                                                                                                                                                       |
|                                    | -   eine Achse (`Vector`) und einen Winkel (`Angle` mit oder ohne Einheit)                                                                                                                                                                                                         |
|                                    | -   drei Euler-Winkel `α`, `β`, `γ`                                                                                                                                                                                                                         |
+++
|                     |                                                                                                                                                                                                                                                                                                                                  |
| `mrotate(m; axis; angle)` |                                                                                                                                                                                                                                                                                                                                  |
|                                 |                                                                                                                                                                                                                                                                                                                                  |
+++
|                     |                                                                                                                                                                                                                                                                                                                                  |
| `mrotate(m; α; β; γ)`     |                                                                                                                                                                                                                                                                                                                                  |
|                                 |                                                                                                                                                                                                                                                                                                                                  |
+++
|                     | [Rotieren](https://en.wikipedia.org/wiki/Transformation_matrix#Rotation_2) um die X-Achse.                                                                                                                                                                                                                                       |
| `mrotatex(m; angle)`      |                                                                                                                                                                                                                                                                                                                                  |
|                                 |                                                                                                                                                                                                                                                                                                                                  |
+++
|                     | [Rotieren](https://en.wikipedia.org/wiki/Transformation_matrix#Rotation_2) um die Y-Achse.                                                                                                                                                                                                                                       |
| `mrotatey(m; angle)`      |                                                                                                                                                                                                                                                                                                                                  |
|                                 |                                                                                                                                                                                                                                                                                                                                  |
+++
|                     | [Rotieren](https://en.wikipedia.org/wiki/Transformation_matrix#Rotation_2) um die Z-Achse.                                                                                                                                                                                                                                       |
| `mrotatez(m; angle)`      |                                                                                                                                                                                                                                                                                                                                  |
|                                 |                                                                                                                                                                                                                                                                                                                                  |
+++
|                     | [Verschieben](https://en.wikipedia.org/wiki/Translation_(geometry)#Matrix_representation) durch einen `vector` (`Vector`) oder X-, Y-, Z-Werte. wenn eine `Rotation` verschoben wird, ist das zurückgegebene Objekt ein `Placement`. |
| `mtranslate(m; vector)`   |                                                                                                                                                                                                                                                                                                                                  |
|                                 |                                                                                                                                                                                                                                                                                                                                  |
+++
|                     |                                                                                                                                                                                                                                                                                                                                  |
| `mtranslate(m; x; y; z)`  |                                                                                                                                                                                                                                                                                                                                  |
|                                 |                                                                                                                                                                                                                                                                                                                                  |
+++
|                     | [Skalieren](https://en.wikipedia.org/wiki/Scaling_(geometry)#Matrix_representation) durch einen `vector` (`Vector`) oder X-, Y-, Z-Werte.                                                                                                                                          |
| `mscale(m; vector)`       |                                                                                                                                                                                                                                                                                                                                  |
|                                 |                                                                                                                                                                                                                                                                                                                                  |
+++
|                     |                                                                                                                                                                                                                                                                                                                                  |
| `mscale(m; x; y; z)`      |                                                                                                                                                                                                                                                                                                                                  |
|                                 |                                                                                                                                                                                                                                                                                                                                  |
+++


{{Top}}



## Bedingte Ausdrücke 

Bedingte Ausdrücke haben die Form `Bedingung ? ResultatWahr : ResultatFalsch`. Die Bedingung ist definiert als ein Ausdruck, der entweder zu `0` (falsch/false) oder Nicht-Null (wahr/true) ausgewertet wird.

Man beachte, dass, um eine boolesche Eigenschaft für diese Bedingung einzusetzen, folgende Syntax verwendet werden muss: `VarSet.MyBool &#61;&#61; 1 ? 10 mm : 15 mm`.

Die folgenden [Vergleichsoperatoren](https://de.wikipedia.org/wiki/Vergleichsoperator) sind definiert:

  Einheit   Beschreibung
   
  **==**    gleich
  **!=**    ungleich
  **\>**    größer als
  **\<**    kleiner als
  **\>=**   größer oder gleich
  **\<=**   kleiner oder gleich


{{Top}}



## Einheiten

Einheiten können direkt in Ausdrücken verwendet werden. Der Analysator (parser) verbindet sie mit dem vorherigen Wert. So ist `2mm` oder `2 mm` gültig, während `mm` ungültig ist, weil es keinen vorhergehenden Wert gibt.

Alle Werte müssen eine Einheit haben. Daher müssen Werte auch in Kalkulationstabellen im allgemeinen eine Einheit haben.
In einigen Fällen funktioniert es auch ohne Einheit, z.B. wenn Sie in Zelle B1 der Kalkulationstabelle z.B. nur die Zahl `1.5` haben und sich für eine Blockhöhe darauf beziehen. Dies funktioniert nur, weil die Blockhöhe die Einheit `mm` vordefiniert und die verwendet wird, wenn keine Einheit angegeben ist. Es schlägt jedoch fehl, wenn Sie für die Blockhöhe z.B. `Sketch1.Constraints.Breite - Kalkulationstabelle.B1` verwenden, weil `Sketch1.Constraints.Breite` eine Einheit hat und `Kalkulationstabelle.B1` keine Einheit.

Einheiten mit Exponenten können direkt eingegeben werden. So wird z.B. `mm^3` als mm³ erkannt und `m^3` wird als m³ erkannt.

Wenn eine Variable mit dem Namen einer Einheit verwendet wird, muss die Variable in `<< >>` gesetzt werden. Das verhindert, dass die Variable als Einheit erkannt wird. Das Maß `Sketch.Constraints.A` würde z.B. als Einheit Ampere erkannt werden. Daher muss der Ausdruck als `Sketch.Constraints.<<A>>` geschrieben werden.

Die folgenden Einheiten werden vom Analysator für Ausdrücke erkannt:



### Stoffmenge

  Einheit   Beschreibung
   
  mmol      Milli[mol](https://de.wikipedia.org/wiki/Mol)
  mol       [Mol](https://de.wikipedia.org/wiki/Mol)



### Winkel

  Einheit   Beschreibung
   
  °         [Grad (Winkel)](https://de.wikipedia.org/wiki/Grad_(Winkel)); Alternative zur Einheit deg
  deg       [Degree](https://en.wikipedia.org/wiki/Degree_(angle)); Alternative zur Einheit °
  rad       [Radian](https://en.wikipedia.org/wiki/Radian)
  gon       [Gradian](https://en.wikipedia.org/wiki/Gon_(unit))
  M         [Winkelminute](https://de.wikipedia.org/wiki/Winkelminute); Alternative zur Einheit ′
  ′         [Winkelminute](https://de.wikipedia.org/wiki/Winkelminute); Dies ist das Symbol Prime (U+2032); Alternative zur Einheit M
  S         [Winkelsekunde](https://de.wikipedia.org/wiki/Winkelminute); **FUNKTIONIERT NICHT** (S wird für die Einheit Siemens verwendet); Alternative zur Einheit \"
  ″         [Winkelsekunde](https://de.wikipedia.org/wiki/Winkelminute); Dies ist das Symbol Doppelprime (U+2033); Alternative zur Einheit S



### Strom

  Einheit   Beschreibung
   
  mA        Milli[ampere](https://de.wikipedia.org/wiki/Ampere)
  A         [Ampere](https://de.wikipedia.org/wiki/Ampere)
  kA        Kilo[ampere](https://de.wikipedia.org/wiki/Ampere)
  MA        Mega[ampere](https://de.wikipedia.org/wiki/Ampere)



### Elektrische Kapazität 

  Einheit   Beschreibung
   
  pF        Pico[farad](https://de.wikipedia.org/wiki/Farad)
  nF        Nano[farad](https://de.wikipedia.org/wiki/Farad)
  uF        Mikro[farad](https://de.wikipedia.org/wiki/Farad); Alternative zur Einheit *µF*
  µF        Mikro[farad](https://de.wikipedia.org/wiki/Farad); Alternative zur Einheit *uF*
  mF        Milli[farad](https://de.wikipedia.org/wiki/Farad)
  F         [Farad](https://de.wikipedia.org/wiki/Farad); 1 F = 1 s\^4·A\^2/m\^2/kg



### Elektrische Ladung 

  Einheit   Beschreibung
   
  C         [Coulomb](https://de.wikipedia.org/wiki/Coulomb); 1 C = 1 A\*s



### Elektrischer Leitwert 

  Einheit   Beschreibung
   
  uS        Mikro[siemens](https://de.wikipedia.org/wiki/Siemens_(Einheit)); alternative to the unit µS
  µS        Mikro[siemens](https://de.wikipedia.org/wiki/Siemens_(Einheit)); alternative to the unit uS
  mS        Milli[siemens](https://de.wikipedia.org/wiki/Siemens_(Einheit))
  S         [Siemens](https://de.wikipedia.org/wiki/Siemens_(Einheit)); 1 S = 1 s\^3·A\^2/kg/m\^2
  kS        Kilo[Siemens](https://de.wikipedia.org/wiki/Siemens_(Einheit))
  MS        Mega[Siemens](https://de.wikipedia.org/wiki/Siemens_(Einheit))



### Elektrische Induktivität 

  Einheit   Beschreibung
   
  nH        Nano[henry (Einheit)](https://de.wikipedia.org/wiki/Henry_(Einheit))
  uH        Mikro[henry (Einheit)](https://de.wikipedia.org/wiki/Henry_(Einheit)); Alternative zur Einheit *µH*
  µH        Mikro[henry (Einheit)](https://de.wikipedia.org/wiki/Henry_(Einheit)); Alternative zur Einheit *uH*
  mH        Milli[henry (Einheit)](https://de.wikipedia.org/wiki/Henry_(Einheit))
  H         [Henry (Einheit)](https://de.wikipedia.org/wiki/Henry_(Einheit)); 1 H = 1 kg·m\^2/s\^2/A\^2



### Elektrische Spannung 

Elektrisches Spannung:

  Einheit   Beschreibung
   
  mV        Milli[volt](https://de.wikipedia.org/wiki/Volt)
  V         [Volt](https://de.wikipedia.org/wiki/Volt)
  kV        Kilo[volt](https://de.wikipedia.org/wiki/Volt)



### Elektrischer Widerstand 

Elektrischer Widerstand:

  Einheit   Beschreibung
   
  Ohm       [Ohm](https://de.wikipedia.org/wiki/Ohm); 1 Ohm = 1 kg·m\^2/s\^3/A\^2
  kOhm      Kilo[ohm](https://de.wikipedia.org/wiki/Ohm)
  MOhm      Mega[ohm](https://de.wikipedia.org/wiki/Ohm)



### Energie/Arbeit

  Einheit   Beschreibung
   
  mJ        Milli[joule](https://de.wikipedia.org/wiki/Joule)
  J         [Joule](https://de.wikipedia.org/wiki/Joule)
  kJ        Kilo[joule](https://de.wikipedia.org/wiki/Joule)
  eV        [elektron(en)volt](https://de.wikipedia.org/wiki/Elektronenvolt); 1 eV = 1.602176634e-19 J
  keV       Kilo[elektron(en)volt](https://de.wikipedia.org/wiki/Elektronenvolt)
  MeV       Mega[elektron(en)volt](https://de.wikipedia.org/wiki/Elektronenvolt)
  kWh       Kilo[wattstunde](https://de.wikipedia.org/wiki/Wattstunde); 1 kWh = 3.6e6 J
  Ws        [Wattsekunde](https://de.wikipedia.org/wiki/Joule); Alternative zur Einheit Joule
  VAs       [Voltamperesekunde](https://de.wikipedia.org/wiki/Joule); Alternative zur Einheit Joule
  CV        [Coulombvolt](https://de.wikipedia.org/wiki/Joule); Alternative zur Einheit Joule
  cal       [Kalorie](https://de.wikipedia.org/wiki/Kalorie); 1 cal = 4.184 J
  kcal      Kilo[kalorie](https://de.wikipedia.org/wiki/Kalorie)



### Kraft

  Einheit   Beschreibung
   
  mN        Milli[newton](https://de.wikipedia.org/wiki/Newton_(Einheit))
  N         [Newton](https://de.wikipedia.org/wiki/Newton_(Einheit))
  kN        Kilo[newton](https://de.wikipedia.org/wiki/Newton_(Einheit))
  MN        Mega[newton](https://de.wikipedia.org/wiki/Newton_(Einheit))
  lbf       [Pound-force](https://de.wikipedia.org/wiki/Pound-force)



### Länge

  Einheit   Beschreibung
   
  nm        Nano[meter](https://de.wikipedia.org/wiki/Meter)
  um        Mikro[meter](https://de.wikipedia.org/wiki/Meter); Alternative zur Einheit µm
  µm        Mikro[meter](https://de.wikipedia.org/wiki/Meter); Alternative zur Einheit um
  mm        Milli[meter](https://de.wikipedia.org/wiki/Meter)
  cm        Zenti[meter](https://de.wikipedia.org/wiki/Meter)
  dm        Dezi[meter](https://de.wikipedia.org/wiki/Meter)
  m         [Meter](https://de.wikipedia.org/wiki/Meter)
  km        Kilo[meter](https://de.wikipedia.org/wiki/Meter)
  mil       [Thou](https://de.wikipedia.org/wiki/Thou) (Abk. f. Thousandth of an inch); Alternative zur Einheit thou
  thou      [Thou](https://de.wikipedia.org/wiki/Thou) (Abk. f. Thousandth of an inch); Alternative zur Einheit mil
  in        [Zoll (Einheit)](https://de.wikipedia.org/wiki/Zoll_(Einheit)), in = inch, Alternative zur Einheit \"
  \"        [Inch](https://en.wikipedia.org/wiki/Inch); Alternative zur Einheit in
  ft        [Fuß (Einheit)](https://de.wikipedia.org/wiki/Fu%C3%9F_(Einheit)); Alternative zur Einheit \'
  \'        [Fuß (Einheit)](https://de.wikipedia.org/wiki/Fu%C3%9F_(Einheit)); Alternative zur Einheit ft
  yd        [Yard](https://de.wikipedia.org/wiki/Yard)
  mi        [Meile](https://de.wikipedia.org/wiki/Meile)



### Lichtstärke

  Einheit   Beschreibung
   
  cd        [Candela](https://de.wikipedia.org/wiki/Candela)



### Magnetischer Fluss 

  Einheit   Beschreibung
   
  Wb        [Weber (Einheit)](https://de.wikipedia.org/wiki/Weber_(Einheit)); 1 Wb = 1 kg\*m\^2/s\^2/A \'



### Magnetische Flussdichte 

  Einheit   Beschreibung
   
  G         [Gauß (Einheit)](https://de.wikipedia.org/wiki/Gau%C3%9F_(Einheit)); 1 G = 1 e-4 T
  T         [Tesla (Einheit)](https://de.wikipedia.org/wiki/Tesla_(Einheit)); 1 T = 1 kg/s\^2/A



### Masse

  Einheit   Beschreibung
   
  ug        Mikro[gramm](https://de.wikipedia.org/wiki/Gramm); Alternative zur Einheit µg
  µg        Mikro[gramm](https://de.wikipedia.org/wiki/Gramm); Alternative zur Einheit ug
  mg        Milli[gramm](https://de.wikipedia.org/wiki/Gramm)
  g         [Gramm](https://de.wikipedia.org/wiki/Gramm)
  kg        Kilo[gramm](https://de.wikipedia.org/wiki/Gramm)
  t         [Tonne (Einheit)](https://de.wikipedia.org/wiki/Tonne_(Einheit))
  oz        [Unze](https://de.wikipedia.org/wiki/Unze)
  lb        [Pfund](https://de.wikipedia.org/wiki/Pfund); Alternative zur Einheit lbm
  lbm       [Pfund](https://de.wikipedia.org/wiki/Pfund); Alternative zur Einheit lb
  st        [Stone (Einheit)](https://de.wikipedia.org/wiki/Stone_(Einheit))
  cwt       [Hundredweight](https://de.wikipedia.org/wiki/Hundredweight)



### Leistung

  Einheit   Beschreibung
   
  W         [Watt](https://de.wikipedia.org/wiki/Watt_(Einheit))
  kW        Kilo[watt](https://de.wikipedia.org/wiki/Watt_(Einheit))



### Druck

  Einheit   Beschreibung
   
  Pa        [Pascal (Einheit)](https://de.wikipedia.org/wiki/Pascal_(Einheit))
  kPa       Kilo-[Pascal (Einheit)](https://de.wikipedia.org/wiki/Pascal_(Einheit))
  MPa       Mega-[Pascal (Einheit)](https://de.wikipedia.org/wiki/Pascal_(Einheit))
  GPa       Giga-[Pascal (Einheit)](https://de.wikipedia.org/wiki/Pascal_(Einheit))
  uTorr     Mikro-[Torr](https://de.wikipedia.org/wiki/Torr); Alternative zu Einheit µTorr
  µTorr     Mikro-[Torr](https://de.wikipedia.org/wiki/Torr); Alternative zu Einheit uTorr
  mTorr     Milli-[Torr](https://de.wikipedia.org/wiki/Torr)
  Torr      [Torr](https://de.wikipedia.org/wiki/Torr); 1 Torr = 133.32 Pa
  psi       [Pound-force per square inch](https://de.wikipedia.org/wiki/Pound-force_per_square_inch); 1 psi = 6.895 kPa
  ksi       Kilo-[Pound-force per square inch](https://en.wikipedia.org/wiki/Pounds_per_square_inch)



### Temperatur

  Einheit   Beschreibung
   
  uK        Mikro[kelvin](https://de.wikipedia.org/wiki/Kelvin); Alternative zur Einheit *µK*
  µK        Mikro[kelvin](https://de.wikipedia.org/wiki/Kelvin); Alternative zur Einheit *uK*
  mK        Milli[kelvin](https://de.wikipedia.org/wiki/Kelvin)
  K         [Kelvin](https://de.wikipedia.org/wiki/Kelvin)



### Zeit

  Einheit    Beschreibung
   
  s          [Secunde](https://de.wikipedia.org/wiki/Sekunde)
  min        [Minute](https://de.wikipedia.org/wiki/Minute)
  h          [Stunde](https://de.wikipedia.org/wiki/Stunde)
  Hz (1/s)   [Hertz](https://de.wikipedia.org/wiki/Hertz_(Einheit))
  kHz        Kilo[hertz](https://de.wikipedia.org/wiki/Hertz_(Einheit)),
  MHz        Mega[hertz](https://de.wikipedia.org/wiki/Hertz_(Einheit))
  GHz        Giga[hertz](https://de.wikipedia.org/wiki/Hertz_(Einheit))
  THz        Tera[hertz](https://de.wikipedia.org/wiki/Hertz_(Einheit))



### Volumen

  Einheit   Beschreibung
   
  ml        Milli[liter](https://de.wikipedia.org/wiki/Liter)
  l         [Liter](https://de.wikipedia.org/wiki/Liter)
  cft       Kubik[fuß](https://de.wikipedia.org/wiki/Fuß_(Einheit))



### Spezielle nichtmetrische Einheiten 

  Einheit   Beschreibung
   
  mph       [Meilen pro Stunde](https://de.wikipedia.org/wiki/Meilen_pro_Stunde)
  sqft      [Quadratfuß](https://de.wikipedia.org/wiki/Quadratfu%C3%9F)



### Nicht unterstützte Einheiten 

Die folgenden häufig verwendeten Einheiten werden noch nicht unterstützt, für einige gibt es aber Alternativen:

  Einheit   Beschreibung                                                                                                          Alternative
    
  °C        [Grad Celsius](https://de.wikipedia.org/wiki/Grad_Celsius)                                                            \[°C\] + 273.15 K
  °F        [Grad Fahrenheit](https://de.wikipedia.org/wiki/Grad_Fahrenheit);                                                     (\[°F\] + 459.67) × ​5/9
  u         [Atomare Masseneinheit](https://de.wikipedia.org/wiki/Atomare_Masseneinheit); Alternative zur Einheit Da (Dalton) =   1.66053906660e-27 kg
  Da        [Dalton](https://de.wikipedia.org/wiki/Atomare_Masseneinheit); Alternative zur Einheit u                              1.66053906660e-27 kg
  sr        [Steradiant](https://de.wikipedia.org/wiki/Steradiant)                                                                nicht direkt
  lm        [Lumen (Einheit)](https://de.wikipedia.org/wiki/Lumen_(Einheit))                                                      nicht direkt
  lx        [Lux (Einheit)](https://de.wikipedia.org/wiki/Lux_(Einheit))                                                          nicht direkt
  px        [Pixel](https://de.wikipedia.org/wiki/Pixel)                                                                          nicht direkt


{{Top}}



## Ungültige Zeichen und Namen 

Das Ausdrucks-Feature ist sehr leistungsfähig. Um das zu ermöglichen gibt es ein paar Einschränkungen bei ein paar Zeichen. Als Abhilfe gibt es in FreeCAD die Möglichkeit anstatt der Objektnamen sog. Bezeichner (\'labels\') zu verwenden und sich auf diese zu beziehen.

In Fällen, in denen du keine Beschriftung verwenden kannst, wie z. B. der Name einer Skizzenbeschränkung, musst du dir bewusst sein, welche Zeichen nicht erlaubt sind.



### Bezeichner

Für [Bezeichner](Object_name/de#Bezeichner.md) gibt es keine ungültigen Zeichen, jedoch müssen einige Zeichen maskiert werden:

+++
| Zeichen                                                  | Beschreibung                                                                  |
+==========================================================+===============================================================================+
|                                           | Müssen durch das Voranstellen von `\` maskiert werden. |
| `'`                                             |                                                                               |
|                                                       |                                                                               |
| , `\`, `"` |                                                                               |
+++

Zum Beispiel muss der Bezeichner `Skizze\002` als `<<Skizze\002>>` referenziert werden.



### Namen

[Namen](Object_name/de#Name.md) von Objekten wie Maße, Skizzen, usw. dürfen folgende Zeichen oder Zeichenfolgen nicht enthalten. Anderenfalls ist der Namen ungültig.

  Zeichen / Zeichenfolgen                                                                                                        Beschreibung
   
  **+**, **-**, **\***, **/**, **\^**, **\_**, **\<**, **\>**, **(**, **)**, **{**, **}**, **\[**, **\]**, **.**, **,**, **=**   Zeichen die mathematische Operatoren oder mathematische Konstruktionen sind.
  **A**, **kA**, **mA**, **MA**, **J**, **K**, **\'**, **ft**, **°**, und viele andere!                                          Zeichen und Zeichenfolgen, die Einheiten sind (siehe Abschnitt [Einheiten](#Einheiten.md) ).
  **\#**, **!**, **?**, **§**, **\$**, **%**, **&**, **:**, **;**, **\\**, **\|**, **\~**, **∆**, **¿**, und viele andere!       Zeichen, die als Platzhalter verwendet werden oder die Funktionen auslösen.
  **pi**, **e**                                                                                                                  Mathematische Konstanten
  **´**, **\**, **\'**, **\"**                                                                                                  Akzente
  Leerzeichen (Space)                                                                                                            Ein Leerzeichen definiert das Ende eines Namens und kann daher nicht verwendet werden.

Beispielsweise ist folgender Name gültig: \>.Constraints.mol** (mol ist eine Einheit).

Da kürzere Namen (vor allem, wenn sie nur ein oder zwei Zeichen haben) leicht zu ungültigen Namen führen können, sollte die Verwendung längerer Namen in Betracht gezogen und/oder eine geeignete Namenskonvention festgelegt werden.



### Zell Aliasse 

Siehe [Spreadsheet Alias-Namen festlegen](Spreadsheet_SetAlias/de#Anwendung.md). 

## Referenzen auf CAD Daten 

Es ist möglich, Daten aus dem Modell selbst in einem Ausdruck zu verwenden. Um auf eine Eigenschaft zu verweisen, wird `Objekt-Name.property` oder `<<Objekt-Benennung>>.property`. Benennungen (Label) müssen in `<<` und `>>` eingeschlossen werden. Sollen Benennungen verwendet werden, müssen sie eindeutig sein.

Alle weiteren Beispiele referenzieren ein Objekt über seinen Namen, aber seine Benennung kann ebenfalls verwendet werden.

Wenn die Eigenschaft aus mehreren Feldern aufgebaut ist, kann auf die einzelnen Felder mit `object_name.property.field` zugegriffen werden.

Um auf Listenobjekte zu verweisen, wird `ObjektName.list[list_index]` verwendet. Soll beispielsweise auf eine Randbedingung in einer Skizze verwiesen werden, wird `Skizze.Constraints[16]` verwendet. Ist eine Skizze im Bearbeitungsmodus geöffnetbefindest, kann man den Namen weglassen und einfach `Constraints[16]` verwenden. Man beachte, dass der Index mit 0 beginnt, daher muss die 17. Randbedingung als `Constraints[16]` referenziert werden.

Um auf das Objekt selbst zu referenziertem wird die Pseudo-Eigenschaft `_self` verwendet: `Objekt-Name._self`.

Die folgende Tabelle zeigt einige weitere Beispiele:

++++
| CAD-Daten                                                       | Aufruf im Ausdruck                       | Ergebnis                                                                                                                                                                                 |
+=================================================================+==========================================+==========================================================================================================================================================================================+
| Länge eines [Part Würfels](Part_Box/de.md)              |                           | Länge mit Einheit (mm)                                                                                                                                                                   |
|                                                                 | `Box.Length`                    |                                                                                                                                                                                          |
|                                                                 |                                       |                                                                                                                                                                                          |
++++
| Volumen des Würfels                                             |                           | Volumen in mm³ ohne Einheit                                                                                                                                                              |
|                                                                 | `Box.Shape.Volume`              |                                                                                                                                                                                          |
|                                                                 |                                       |                                                                                                                                                                                          |
++++
| Formart des Würfels                                             |                           | Zeichenkette (String): Solid                                                                                                                                                             |
|                                                                 | `Box.Shape.ShapeType`           |                                                                                                                                                                                          |
|                                                                 |                                       |                                                                                                                                                                                          |
++++
| Bezeichnung des Würfels                                         |                           | Zeichenkette (String): Label                                                                                                                                                             |
|                                                                 | `Box.Label`                     |                                                                                                                                                                                          |
|                                                                 |                                       |                                                                                                                                                                                          |
++++
| X-Koordinate des Schwerpunktes des Würfels                      |                           | X-Koordinate in mm ohne Einheit                                                                                                                                                          |
|                                                                 | `Box.Shape.CenterOfMass.x`      |                                                                                                                                                                                          |
|                                                                 |                                       |                                                                                                                                                                                          |
++++
| X-Koordinate der Positionierung des Würfels                     |                           | X-Koordinate mit Einheit (mm)                                                                                                                                                            |
|                                                                 | `Box.Placement.Base.x`          |                                                                                                                                                                                          |
|                                                                 |                                       |                                                                                                                                                                                          |
++++
| X-Komponente der Rotationsachsen der Positionierung des Würfels |                           | X-Komponente des Einheitsvektors in mm ohne Einheit                                                                                                                                      |
|                                                                 | `Box.Placement.Rotation.Axis.x` |                                                                                                                                                                                          |
|                                                                 |                                       |                                                                                                                                                                                          |
++++
| Rotationswinkel der Positionierung des Würfels                  |                           | Rotationswinkel mit Einheit (° = Grad = deg)                                                                                                                                             |
|                                                                 | `Box.Placement.Rotation.Angle`  |                                                                                                                                                                                          |
|                                                                 |                                       |                                                                                                                                                                                          |
++++
| Das ganze Würfel-Objekt                                         |                                                                                                                                               |
|                                                                 | `Box._self`                     |                                                                                                                                                                                          |
|                                                                 |                                       |                                                                                                                                                                                          |
++++
| Wert einer Randbedingung in einer Skizze                        |                           | Zahlenwert der benannten Randbedingung `Width` (Breite) in der Skizze, wenn der Ausdruck in der Skizze selbst verwendet wird.                                     |
|                                                                 | `Constraints.Width`             |                                                                                                                                                                                          |
|                                                                 |                                       |                                                                                                                                                                                          |
++++
| Wert einer Randbedingung in einer Skizze                        |                           | Zahlenwert der benannten Randbedingung `Width` in der Skizze `MySketch`, wenn der Ausdruck außerhalb der Skizze verwendet wird.            |
|                                                                 | `MySketch.Constraints.Width`    |                                                                                                                                                                                          |
|                                                                 |                                       |                                                                                                                                                                                          |
++++
| Wert eines Alias einer Kalkulationstabelle                      |                           | Wert des Alias `Depth` (Tiefe) in der Kalkulationstabelle `Spreadsheet`                                                                    |
|                                                                 | `Spreadsheet.Depth`             |                                                                                                                                                                                          |
|                                                                 |                                       |                                                                                                                                                                                          |
++++
| Wert einer lokalen Eigenschaft eines Objekts                    |                           | Wert der {{PropertyData/de|Length}} (Länge) z.B. in einem Pad-Objekt, wenn der Ausdruck z.B. in {{PropertyData/de|Length2}} im selben Objekt verwendet wird. |
|                                                                 | `Length`                        |                                                                                                                                                                                          |
|                                                                 |                                       |                                                                                                                                                                                          |
++++



### Zyklische Abhängigkeiten 

FreeCAD prüft Abhängigkeiten aufgrund der Beziehungen zwischen Dokumentobjekten, nicht auf Basis ihrer Eigenschaften. Das heißt, dass man einem Objekt nicht Daten zur Verfügung stellen und (gleichzeitig) das Ergebnis desselben Objekts auslesen kann. Z.B. darf es, auch wenn es keine zyklischen Abhängigkeiten zwischen den Eigenschaften selbst gibt, kein Objekt geben, das seine Abmaße aus einer Tabelle erhält, und dessen (gemessenes) Volumen in derselben Tabelle ausgegeben wird. Es müssen zwei Tabellen verwendet werden, eine zum Steuern des Modells und eine für die Ausgabe (von ausgelesenen Ergebnissen).

Als Ungehunglösung kann man einen Zellenbereich der zweiten Tabelle in der ersten anzeigen (oder umgekehrt), indem eine [Zellenverbindung](Spreadsheet_Workbench#Cell_binding.md) mit der Option **Hide dependency of binding** erstellt wird.

Eine weitere Möglichkeit zyklische Abhängigkeiten zu umgehen, ist das Ausblenden der Referenz, indem die Funktion `href` oder `hiddenref` für individuelle Ausdrücke verwendet wird, z.B.: `href(Box.Length)`.

Bitte beachten, dass beide erwähnten Umgehungslösungen mit Vorsicht eingesetzt werden sollten und dass sie nicht funktionieren, wenn die Eigenschaften, die ausgegeben werden, auf Abmaßen beruhen, die aus derselben Tabelle heraus gesteuert werden. 

## Dokumentweit gültige globale Variablen 

In FreeCAD gibt es zur Zeit kein Konzept für globale Variablen. Stattdessen können beliebige Variablen mit Hilfe der [Arbeitsbereich Kalkulationstabelle](Spreadsheet_Workbench/de.md) als Zellen in einer Kalkulationstabelle definiert werden und dann mit Hilfe der Alias Eigenschaft für die Zelle (Rechtsklick auf die Zelle) einen Namen erhalten. Dann kann von jedem Ausdruck aus auf sie zugegriffen werden, wie auf jede andere Objekteigenschaft auch. 

## Dokumentenübergreifende Verweise 

Es ist (mit Begrenzungen) möglich, eine Eigenschaft eines Objekts in deinem aktuellen Dokument (\".FCstd\" Datei) durch Verwendung eines Ausdrucks zu definieren, um auf eine Eigenschaft eines Objekts in einem anderen Dokument zu verweisen (\".FCstd\" file). Zum Beispiel kann eine Zelle in einer Kalkulationstabelle oder die {{PropertyData/de|Länge}} eines Formteil Würfels usw. in einem Dokument durch einen Ausdruck definiert werden, der auf den X Platzierungswert oder eine andere Eigenschaft eines Objekts in einem anderen Dokument verweist.

Der Name des Dokuments wird verwendet, um von einem anderen Dokument aus darauf zu referenzieren. Wenn ein Dokument zum ersten Mal gespeichert wird, muss dem Dokument ein Name gegeben werden. Dies ist normalerweise ein anderer Name als die Vorgabe \"Unbenannt1\". Um zu verhindern, dass Verknüpfungen beim Speichern des Hauptdokumentes verloren gehen, wenn dieses dabei einen anderen Namen bekommt, sollte das Hauptdokument zuerst mit einer Kalkulationstabelle erstellt werden. Danach kann der Inhalt des Dokuments geändert und das Dokument gespeichert werden, aber es darf nicht umbenannt werden.

Sobald das Mutterdokument mit der Kalkulationstabelle erstellt und gespeichert (benannt) ist, können abhängige Dokumente erstellt werden. Angenommen, du nennst das Mutterdokument `master`, die Kalkulationstabelle `modelConstants` und gibst einer Zelle einen Alias-Namen `Length`, dann kannst du auf den Wert zugreifen als:


`master#modelConstants.Length`

Man beachte, dass das Hauptdokument geladen sein muss, damit die Werte des Hauptdokuments für das abhängige Dokument verfügbar sind.

Natürlich liegt es bei dir, die zugehörigen Dokumente später zu laden, wenn du etwas ändern willst. 

## Bekannte Probleme / Verbleibende Aufgaben 

-   FreeCAD hat bisher keinen eingebauten Ausdrucksmanager, der alle Ausdrücke in einem Dokument auflistet und sie erstellt, löscht, abfragt, etc. Aber es ist ein Addon verfügbar: [fcxref expression manager](https://github.com/gbroques/fcxref).
-   Offene Fehler/Tickets für die Ausdrücke (Expressions) können hier gefunden werden: [GitHub](https://github.com/FreeCAD/FreeCAD//labels/Topic%3A%20Expressions).


{{Top}}



## Skripten


```python
import FreeCAD as App

doc = App.ActiveDocument
box = doc.addObject("Part::Box", "Box")
cyl = doc.addObject("Part::Cylinder", "Cylinder")
cyl_name = cyl.Name

box.setExpression("Height", f"{cyl_name}.Height / 2")
box.setExpression("Length", f"{cyl_name}.Radius * 2")
box.setExpression("Width", "Length")

doc.recompute()

# Expressions are stored in the ExpressionEngine property:
for prop, exp in box.ExpressionEngine:
    val = getattr(box, prop)
    print(f"Property: '{prop}' -- Expression: '{exp}' -- Current value: {val}")
```


{{Top}}



---
⏵ [documentation index](../README.md) > [Spreadsheet](Category_Spreadsheet.md) > Expressions/de
