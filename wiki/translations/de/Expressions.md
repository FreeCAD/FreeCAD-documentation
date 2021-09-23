# Expressions/de
 {{TOCright}}

## Übersicht

Es ist möglich, Eigenschaften unter Verwendung von mathematischen Ausdrücken festzulegen. In der GUI enthalten Drehfelder oder Eingabefelder, die an Eigenschaften gebunden sind, ein blaues Symbol <img alt="" src=images/Sketcher_Expressions.png  style="width:32px;">. Klicken auf das Symbol oder Eingeben des Gleichheitszeichens **&#61;** ruft den Ausdruckseditor für diese bestimmte Eigenschaft auf.

Ein FreeCAD Ausdruck ist ein mathematischer Ausdruck, der der Schreibweise für die unten beschriebenen mathematischen Standardoperatoren und -funktionen folgt. Außerdem kann der Ausdruck auf andere Eigenschaften verweisen und auch Konditionale verwenden. Zahlen in einem Ausdruck können eine optionalen Einheit angehängt bekommen.

Zahlen können entweder ein Komma `,` oder einen Dezimalpunkt `.` zur Trennung der Ganzzahlen von Nachkommastellen verwenden. Wenn diese Trennung benutzt wird, *muss* danach mindestens eine Ziffer folgen. Daher sind die Ausdrücke `1.+2.` und `1,+2,` ungültig, aber `1.0 + 2.0` und `1,0 + 2,0` sind gültig.

Operatoren und Funktionen sind einheitenbewusst und erfordern gültige Kombinationen von Einheiten, falls verfügbar. Zum Beispiel ist `2mm + 4mm` ein gültiger Ausdruck, während `2mm + 4` kein gültiger Ausdruck ist (der Grund dafür ist, dass ein Ausdruck wie `1in + 4` von Menschen höchstwahrscheinlich als `1in + 4in` interpretiert wird, aber alle Einheiten werden intern in das SI System umgewandelt, und das System ist nicht in der Lage, dies zu erraten). Diese [Einheiten](#Einheiten.md) werden derzeit erkannt.

Du kannst [vorgegebene Konstanten](#Unterstützte_Konstanten.md) und [Funktionen](#Unterstützte_Funktionen.md) verwenden.

### Funktionsargumente

Mehrere Argumente zu einer Funktion können entweder durch ein Semikolon  gefolgt von einem Leerzeichen `,` getrennt werden. Im letzteren Fall wird das Komma nach der Eingabe in ein Semikolon umgewandelt. Wenn ein Semikolon verwendet wird, ist kein Leerzeichen am Ende des Semikolons erforderlich.

Die Argumente können Verweise auf Zellen in einer Kalkulationstabelle enthalten. Ein Zellverweis besteht aus dem großen Zeilenbuchstaben der Zelle, gefolgt von ihrer Spaltennummer, zum Beispiel `A1`. Eine Zelle kann auch durch den Alias der Zelle referenziert werden, zum Beispiel `Tabellenblatt.MeineTeilbreite`.

### Referenzierende Objekte 

Du kannst auf ein Objekt über seinen {{PropertyData/de|Namen}} oder über seine {{PropertyData/de|Beschriftung}} verweisen. Im Falle einer {{PropertyData/de|Beschriftung}} muss es in doppelten {{PropertyData/de|<<}} und {{PropertyData/de|>>}} Symbolen eingeschlossen sein, wie z.B. {{PropertyData/de|<<Beschriftung>>}}.

Du kannst auf jede numerische Eigenschaft eines Objekts referenzieren. Um sich beispielsweise auf die Höhe eines Zylinders zu beziehen, kann `Zylinder.Hoehe` oder `<<Langer_Name_des_Zylinders>>.Hoehe` verwendet werden.

Um auf Listenobjekte zu verweisen, verwende `<<object_label>>.list[list_index]` oder `object_name.list[list_index]`. Wenn du beispielsweise auf eine Beschränkung in einer Skizze verweisen möchtest, verwende `<<MeineSkizze>>.Constraints[16]`. Wenn du dich in derselben Skizze befindest, kann man den Namen weglassen und einfach `Constraints[16]` verwenden.
**Hinweis:** Der Index beginnt mit 0, daher hat die Beschränkung 17 den Index 16.

Für weitere Informationen über das Referenzieren von Objekten siehe [Referenz zu CAD Daten](#Reference_to_CAD_data/de.md).

## Unterstützte Konstanten 

Die folgenden Konstanten werden unterstützt:

  Konstante   Beschreibung
  ----------- ----------------------------------------------------------------
  **e**       [Eulersche Zahl](https://de.wikipedia.org/wiki/Eulersche_Zahl)
  **pi**      [Kreiszahl $\pi$](https://de.wikipedia.org/wiki/Kreiszahl)

## Unterstützte Operatoren 

Die folgenden Operatoren werden untertstützt:

  Operator   Beschreibung
  ---------- ----------------------------------------------------------------------------
  **+**      [Addition](https://de.wikipedia.org/wiki/Addition)
  **-**      [Subtraktion](https://de.wikipedia.org/wiki/Subtraktion)
  **\***     [Multiplikation](https://de.wikipedia.org/wiki/Multiplikation)
  **/**      Fließkomma [Division](https://de.wikipedia.org/wiki/Division_(Mathematik))
  **%**      [Division mit Rest](https://de.wikipedia.org/wiki/Division_mit_Rest)
  **\^**     [Potenz](https://de.wikipedia.org/wiki/Potenz_(Mathematik))

## Unterstützte Funktionen 

### Allgemeine mathematische Funktionen 

Die nachfolgend aufgeführten mathematischen Funktionen sind verfügbar.

[Trigonometrische Funktionen](https://de.wikipedia.org/wiki/Trigonometrische_Funktion) verwenden Grad als Standardeinheit. Für die Angabe im Bogenmaß wird ersten Wert in einem Ausdruck hinzugefügt. So ist z.B. `cos(45)` das gleiche, wie `cos(pi rad / 4)`. Ausdrücke in Grad können entweder `deg` oder `°` verwenden, z.B. `360deg - atan2(3; 4)` oder `360&deg; - atan2(3; 4)`. Ein Ausdruck, der ohne Einheiten angegeben ist und aus Kompatibilitätsgründen in Grad oder Bogenmaß umgewandelt werden muss, wird mit `1&nbsp;deg`, `1&nbsp;°` oder `1&nbsp;rad` multipliziert, gegebenenfalls, z.B. `(360 - X) * 1deg`; `(360 - X) * 1°`; `(0.5 + pi / 2) * 1rad`.
Folgende Trigonometrische Funktionen werden unterstützt:

  Funktion      Beschreibung                                                                                Wertebereich
  ------------- ------------------------------------------------------------------------------------------- ------------------------------------------
  acos(x)       [arccos](https://de.wikipedia.org/wiki/Arkusfunktion#Beziehungen_zwischen_den_Funktionen)   -1 \<= x \<= 1
  asin(x)       [arcsin](https://de.wikipedia.org/wiki/Arkusfunktion#Beziehungen_zwischen_den_Funktionen)   -1 \<= x \<= 1
  atan(x)       [arctan](https://de.wikipedia.org/wiki/Arkusfunktion#Beziehungen_zwischen_den_Funktionen)   alle
  atan2(x, y)   [arctan2](https://de.wikipedia.org/wiki/Arctan2#Implementierungen) von *x/y*                alle, außer y = 0
  cos(x)        [cos](https://de.wikipedia.org/wiki/Trigonometrische_Funktion#Definition)                   alle
  cosh(x)       [cosh](https://de.wikipedia.org/wiki/Hyperbelfunktion#Definition)                           alle
  sin(x)        [sin](https://de.wikipedia.org/wiki/Trigonometrische_Funktion#Definition)                   alle
  sinh(x)       [sinh](https://de.wikipedia.org/wiki/Hyperbelfunktion#Definition)                           alle
  tan(x)        [tan](https://de.wikipedia.org/wiki/Trigonometrische_Funktion#Definition)                   alle, außer für x = n·90 mit n = integer
  tanh(x)       [tanh](https://de.wikipedia.org/wiki/Hyperbelfunktion#Definition)                           alle

Diese Exponential- oder Logarithmusfunktionen werden unterstützt:

  Funktion    Beschreibung                                                                                        Wertebereich
  ----------- --------------------------------------------------------------------------------------------------- --------------
  exp(x)      [Exponentialfunktion](https://en.wikipedia.org/wiki/Exponential_function#Definition)                alle
  log(x)      [Natürlicher Logarithmus](https://de.wikipedia.org/wiki/Logarithmus#Nat%C3%BCrlicher_Logarithmus)   x \> 0
  log10(x)    [Dekadischer Logarithmus](https://de.wikipedia.org/wiki/Dekadischer_Logarithmus)                    x \> 0
  pow(x, y)   [Potenz (Mathematik)](https://de.wikipedia.org/wiki/Potenz_(Mathematik))                            alle
  sqrt(x)     [Quadratwurzel](https://de.wikipedia.org/wiki/Quadratwurzel)                                        x \>= 0

Diese Funktionen für Rundung, Trunkierung und Modulo werden unterstützt:

  Funktion    Beschreibung                                                                                                                                               Wertebereich
  ----------- ---------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------
  abs(x)      [Betragsfunktion](https://de.wikipedia.org/wiki/Betragsfunktion)                                                                                           alle
  ceil(x)     [Abrundungsfunktion](https://de.wikipedia.org/wiki/Abrundungsfunktion_und_Aufrundungsfunktion), kleinster ganzzahliger Wert größer oder gleich x           alle
  floor(x)    [Aufrundungsfunktion](https://de.wikipedia.org/wiki/Abrundungsfunktion_und_Aufrundungsfunktion), größter ganzzahliger Wert kleiner oder gleich x           alle
  mod(x, y)   [Division mit Rest](https://de.wikipedia.org/wiki/Division_mit_Rest) nach einer Division *x* durch *y*                                                     alle, außer y = 0
  round(x)    [Rundung](https://de.wikipedia.org/wiki/Rundung) auf die nächste Ganzzahl in Richtung Null                                                                 alle
  trunc(x)    [Trunkierung](https://de.wikipedia.org/wiki/Trunkierung_(Mathematik)) auf die nächste Ganzzahl (Kürzen auf einer Reihe oder Zahl auf eine gewisse Länge)   alle

### Statistische / Aggregatfunktionen 

[Aggregatfunktion](https://de.wikipedia.org/wiki/Aggregatfunktion) verwenden ein oder mehrere Argumente.
Einzelne Argumente für Aggregatfunktionen können aus Zellbereichen bestehen. Ein Zellbereich wird durch zwei Zellbezüge ausgedrückt, die durch einen Doppelpunkt {{Incode|:}} getrennt sind, zum Beispiel {{Incode|Durchschnitt(B1:B8)}} oder {{Incode|Summe(A1:A4; B1:B4)}}. Die Zellbezüge können auch Zell Aliase verwenden, zum Beispiel {{Incode|Durchschnitt(StartTemp:EndTemp)}} {{Version/de|0.19}}.

Diese Aggregatfunktionen werden unterstützt:

  Funktion                 Beschreibung                                                                                                                                     Wertebereich
  ------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------ --------------
  average(a; b; c; \...)   [Arithmetisches Mittel](https://de.wikipedia.org/wiki/Arithmetisches_Mittel) von Werten in Zellen x bis y; sum(x:y) / count(x:y); Summe/Anzahl   alle
  count(x:y)               [Zählen](https://de.wikipedia.org/wiki/Z%C3%A4hlen) der Zellen von x bis y                                                                       alle
  max(x:y)                 [Extremwert (Maximum)](https://de.wikipedia.org/wiki/Extremwert) von Werten in Zellen x bis y                                                    alle
  min(x:y)                 [Minimum](https://de.wikipedia.org/wiki/Extremwert) von Werten in Zellen x bis y                                                                 alle
  stddev(x:y)              [Varianz (Stochastik)](https://de.wikipedia.org/wiki/Varianz_(Stochastik)) von Werten in Zellen x bis y                                          alle
  sum(x:y)                 [Summe](https://de.wikipedia.org/wiki/Summe) von Werten in Zellen x bis y                                                                        alle

### Zeichenkettenhandhabung

#### Zeichenkettenerkennung

Zeichenketten werden in Ausdrücken erkannt, indem sie in öffnende/schließende Winkel eingeschlossen werden (denn sie sind Beschriftungen).

Im folgenden Beispiel wird \"TEXT\" als eine Zeichenkette erkannt: {{Incode|<<TEXT>>}}

#### Zeichenkettenverkettung

Zeichenketten können durch das \'+\'-Zeichen aneinandergehängt werden.

Das folgende Beispiel {{Incode|<<MY>>+<<TEXT>>}} wird verbunden zu \"MYTEXT\".

#### Zeichenkettenformatierung

Zeichenkettenformatierung wird unterstützt durch die (alte) %-Form von Python.

Alle %-Spezifizierer wie in der (engl.) [Python documentation](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting) definiert.

Du hast bspw. einen (wie in der Vorgabe) Würfel namens \'Box\' (\--FreeCAD-Standardbezeichnung\--) mit 10mm-Kantenlänge und der folgende Ausdruck `<<Würfellänge: %s>> % Box.Length` wird erweitert zu \"Würfellänge: 10.0 mm\"

Eine Beschränkung ist, dass nur ein %-Spezifizierer in einer Zeichenkette ist, so dass du Zeichenketten verknüpfen musst, falls mehr als einer nötig ist. In der gleichen Situation wie oben wird der Ausdruck {{Incode|<<Würfellänge ist %s>> % Box.Length + << und Länge ist %s>> % Box.Width}} wird erweitert zu \"Würfellänge ist 10.0 mm und Breite ist 10.0 mm\".

Eine FreeCAD-Beispieldatei, die Zeichenkettenformatierung zeigt, ist unter [im Forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=58657) verfügbar (engl.)

## Bedingte Ausdrücke 

Bedingte Ausdrücke haben die Form `Bedingung ? ResultatWahr : ResultatFalsch`. Die Bedingung ist definiert als ein Ausdruck, der entweder zu `0` (falsch) oder Nicht-Null (wahr) ausgewertet wird. Beachte, dass das Einschließen des bedingten Ausdrucks in Klammern derzeit als Fehler angesehen wird. {{VersionMinus/de|0.19}}

Die folgenden [Vergleichsoperatoren](https://de.wikipedia.org/wiki/Vergleichsoperator) sind definiert:

  Einheit   Beschreibung
  --------- ---------------------
  **==**    gleich
  **!=**    ungleich
  **\>**    größer als
  **\<**    kleiner als
  **\>=**   größer oder gleich
  **\<=**   kleiner oder gleich

## Einheiten

Einheiten können direkt in Ausdrücken verwendet werden. Der Analysator (parser) verbindet sie mit dem vorherigen Wert. So ist `2mm` oder `2 mm` gültig, während `mm` ungültig ist, weil es keinen vorhergehenden Wert gibt.

Alle Werte müssen eine Einheit haben. Daher müssen Werte auch in Kalkulationstabellen im allgemeinen eine Einheit haben.
In einigen Fällen funktioniert es auch ohne Einheit, z.B. wenn Sie in Zelle B1 der Kalkulationstabelle z.B. nur die Zahl `1.5` haben und sich für eine Blockhöhe darauf beziehen. Dies funktioniert nur, weil die Blockhöhe die Einheit `mm` vordefiniert und die verwendet wird, wenn keine Einheit angegeben ist. Es schlägt jedoch fehl, wenn Sie für die Blockhöhe z.B. `Sketch1.Constraints.Breite - Kalkulationstabelle.B1` verwenden, weil `Sketch1.Constraints.Breite` eine Einheit hat und `Kalkulationstabelle.B1` keine Einheit.

Einheiten mit Exponenten können direkt eingegeben werden. So wird z.B. `mm^3` als mm³ erkannt und `m^3` wird als m³ erkannt.

Wenn eine Variable mit dem Namen einer Einheit verwendet wird, muss die Variable in `<< >>` gesetzt werden. Das verhindert, dass die Variable als Einheit erkannt wird. Das Maß `Sketch.Constraints.A` würde z.B. als Einheit Ampere erkannt werden. Daher muss der Ausdruck als `Sketch.Constraints.<<A>>` geschrieben werden.

Die folgenden Einheiten werden vom Analysator für Ausdrücke erkannt:

Chemische Menge einer Substanz:

  Einheit   Beschreibung
  --------- -----------------------------------------------
  mmol      Milli[Mol](https://de.wikipedia.org/wiki/Mol)
  mol       [Mol](https://de.wikipedia.org/wiki/Mol)

Winkel:

  Einheit   Beschreibung
  --------- -------------------------------------------------------------------------------------------------
  °         [Grad (Winkel)](https://de.wikipedia.org/wiki/Grad_(Winkel)); Alternative zur Einheit *deg*
  deg       [Degree](https://en.wikipedia.org/wiki/Degree_(angle)); Alternative zur Einheit *°*
  rad       [Radian](https://en.wikipedia.org/wiki/Radian)
  gon       [Gradian](https://en.wikipedia.org/wiki/Gon_(unit))
  S         [Winkelsekunde](https://de.wikipedia.org/wiki/Winkelminute); Alternative zur Einheit *\"*
  ″         [Winkelsekunde](https://de.wikipedia.org/wiki/Winkelminute); Alternative zur Einheit *S*
  M         [Winkelminute](https://de.wikipedia.org/wiki/Winkelminute); Alternative zur Einheit \'\' \'\'\'
  ′         [Winkelminute](https://de.wikipedia.org/wiki/Winkelminute); Alternative zur Einheit *M*

Strom:

  Einheit   Beschreibung
  --------- -----------------------------------------------------
  mA        Milli[ampere](https://de.wikipedia.org/wiki/Ampere)
  A         [Ampere](https://de.wikipedia.org/wiki/Ampere)
  kA        Kilo[ampere](https://de.wikipedia.org/wiki/Ampere)
  MA        Mega[ampere](https://de.wikipedia.org/wiki/Ampere)

Elektrische Kapazität:

  Einheit   Beschreibung
  --------- --------------------------------------------------------------------------------------------------------------------
  pF        Pico[farad](https://de.wikipedia.org/wiki/Farad), {{Version/de|0.19}}
  nF        Nano[farad](https://de.wikipedia.org/wiki/Farad), {{Version/de|0.19}}
  uF        Micro[farad](https://de.wikipedia.org/wiki/Farad); Alternative zur Einheit *µF*, {{Version/de|0.19}}
  µF        Micro[farad](https://de.wikipedia.org/wiki/Farad); Alternative zur Einheit *uF*, {{Version/de|0.19}}
  mF        Milli[farad](https://de.wikipedia.org/wiki/Farad), {{Version/de|0.19}}
  F         [Farad](https://de.wikipedia.org/wiki/Farad); 1 F = 1 s\^4·A\^2/m\^2/kg, {{Version/de|0.19}}

Elektrische Leitfähigkeit:

  Einheit   Beschreibung
  --------- -------------------------------------------------------------------------------------------------------------------------------------------
  uS        Micro[siemens (Einheit)](https://de.wikipedia.org/wiki/Siemens_(Einheit)); alternativ zur Einheit *µS*, {{Version/de|0.19}}
  µS        Micro[siemens (Einheit)](https://de.wikipedia.org/wiki/Siemens_(Einheit)); alternativ zur Einheit *uS*, {{Version/de|0.19}}
  mS        Milli[siemens (Einheit)](https://de.wikipedia.org/wiki/Siemens_(Einheit)), {{Version/de|0.19}}
  S         [Siemens (Einheit)](https://de.wikipedia.org/wiki/Siemens_(Einheit)); 1 S = 1 s\^3·A\^2/kg/m\^2, {{Version/de|0.19}}
  kS        Kilo[siemens (Einheit)](https://de.wikipedia.org/wiki/Siemens_(Einheit)), {{Version/de|0.20}}
  MS        Mega[siemens (Einheit)](https://de.wikipedia.org/wiki/Siemens_(Einheit)), {{Version/de|0.20}}

Elektrische Induktivität:

  Einheit   Beschreibung
  --------- ----------------------------------------------------------------------------------------------------------------------------------------
  nH        Nano[henry (Einheit)](https://de.wikipedia.org/wiki/Henry_(Einheit)), {{Version/de|0.19}}
  uH        Micro[henry (Einheit)](https://de.wikipedia.org/wiki/Henry_(Einheit)); Alternative zur Einheit *µH*, {{Version/de|0.19}}
  µH        Micro[henry (Einheit)](https://de.wikipedia.org/wiki/Henry_(Einheit)); Alternative zur Einheit *uH*, {{Version/de|0.19}}
  mH        Milli[henry (Einheit)](https://de.wikipedia.org/wiki/Henry_(Einheit)), {{Version/de|0.19}}
  H         [Henry (Einheit)](https://de.wikipedia.org/wiki/Henry_(Einheit)); 1 H = 1 kg·m\^2/s\^2/A\^2, {{Version/de|0.19}}

Elektrischer Widerstand:

  Einheit   Beschreibung
  --------- -------------------------------------------------------------------------------------------------------
  Ohm       [Ohm](https://de.wikipedia.org/wiki/Ohm); 1 Ohm = 1 kg·m\^2/s\^3/A\^2, <small>(v0.19)</small> 
  kOhm      Kilo[ohm](https://de.wikipedia.org/wiki/Ohm), <small>(v0.19)</small> 
  MOhm      Mega[ohm](https://de.wikipedia.org/wiki/Ohm), <small>(v0.19)</small> 

Elektrische Ladung:

  Einheit   Beschreibung
  --------- --------------------------------------------------------------------------------------------------
  C         [Coulomb](https://de.wikipedia.org/wiki/Coulomb); 1 C = 1 A·s, {{Version/de|0.19}}

Elektrisches Spannung:

  Einheit   Beschreibung
  --------- -------------------------------------------------
  mV        Milli[volt](https://de.wikipedia.org/wiki/Volt)
  V         [Volt](https://de.wikipedia.org/wiki/Volt)
  kV        Kilo[volt](https://de.wikipedia.org/wiki/Volt)

Energie / Arbeit:

  Einheit   Beschreibung
  --------- -----------------------------------------------------------------------------------------------------------------------------
  mJ        Milli[joule](https://de.wikipedia.org/wiki/Joule)
  J         [Joule](https://de.wikipedia.org/wiki/Joule)
  kJ        Kilo[joule](https://de.wikipedia.org/wiki/Joule), {{Version/de|0.19}}
  eV        [Elektronenvolt](https://de.wikipedia.org/wiki/Elektronenvolt); 1 ev = 1.602176634e-19 J, {{Version/de|0.19}}
  keV       Kilo[elektronenvolt](https://de.wikipedia.org/wiki/Elektronenvolt), {{Version/de|0.19}}
  MeV       Mega[elektronenvolt](https://de.wikipedia.org/wiki/Elektronenvolt), {{Version/de|0.19}}
  kWh       Kilo[wattstunde](https://de.wikipedia.org/wiki/Wattstunde); 1 kWh = 3.6e6 J, {{Version/de|0.19}}
  Ws        [Wattsekunde](https://de.wikipedia.org/wiki/Joule); Alternative zur Einheit *Joule*
  VAs       [Voltamperesekunde](https://de.wikipedia.org/wiki/Joule); Alternative zur Einheit *Joule*
  CV        [Coulombvolt](https://de.wikipedia.org/wiki/Joule); Alternative zur Einheit *Joule*
  cal       [Kalorie](https://de.wikipedia.org/wiki/Kalorie); 1 cal = 4.184 J, {{Version/de|0.19}}
  kcal      Kilo[kalorie](https://de.wikipedia.org/wiki/Kalorie), {{Version/de|0.19}}

Kraft:

  Einheit   Beschreibung
  --------- ---------------------------------------------------------------
  mN        Milli[newton](https://de.wikipedia.org/wiki/Newton_(Einheit))
  N         [Newton](https://de.wikipedia.org/wiki/Newton_(Einheit))
  kN        Kilo[newton](https://de.wikipedia.org/wiki/Newton_(Einheit))
  MN        Mega[newton](https://de.wikipedia.org/wiki/Newton_(Einheit))
  lbf       [Pound-force](https://de.wikipedia.org/wiki/Pound-force)

Länge:

  Einheit   Beschreibung
  --------- ------------------------------------------------------------------------------------------------------------
  mu        Nano[meter](https://de.wikipedia.org/wiki/Meter)
  um        Micro-[Meter](https://de.wikipedia.org/wiki/Meter); Alternative zur Einheit *µm*
  µm        Micro[meter](https://de.wikipedia.org/wiki/Meter); Alternative zur Einheit *mu*
  mm        Milli[meter](https://de.wikipedia.org/wiki/Meter)
  cm        Zenti[meter](https://de.wikipedia.org/wiki/Meter)
  mm        Milli[meter](https://de.wikipedia.org/wiki/Meter)
  dm        Dezi[meter](https://de.wikipedia.org/wiki/Meter)
  m         [Meter](https://de.wikipedia.org/wiki/Meter)
  km        Kilo[meter](https://de.wikipedia.org/wiki/Meter)
  mil       [Thou](https://de.wikipedia.org/wiki/Thou) (Abk. f. Thousandth of an inch); Alternative zur Einheit *thou*
  thou      [Thou](https://de.wikipedia.org/wiki/Thou) (Abk. f. Thousandth of an inch); Alternative zur Einheit *mil*
  in        [Zoll (Einheit)](https://de.wikipedia.org/wiki/Zoll_(Einheit)), in = inch
  ft        [Fuß (Einheit)](https://de.wikipedia.org/wiki/Fu%C3%9F_(Einheit)); Alternative zur Einheit \'
  \'        [Fuß (Einheit)](https://de.wikipedia.org/wiki/Fu%C3%9F_(Einheit)); Alternative zur Einheit *ft*
  yd        [Yard](https://de.wikipedia.org/wiki/Yard)
  mi        [Meile](https://de.wikipedia.org/wiki/Meile)

Lichtstärke:

  Einheit   Beschreibung
  --------- --------------------------------------------------
  cd        [Candela](https://de.wikipedia.org/wiki/Candela)

Magnetische Feldstärke (seit 1970 nicht mehr offiziell gültig):

  Einheit   Beschreibung
  --------- ------------------------------------------------------------------------------------------------------------------------------
  Oe        [Oersted (Einheit)](https://de.wikipedia.org/wiki/Oersted_(Einheit)); 1 Oe = 79.57747 A/m, {{Version/de|0.19}}

Magnetischer Fluß:

  Einheit   Beschreibung
  --------- -------------------------------------------------------------------------------------------------------------------------------
  Wb        [Weber (Einheit)](https://de.wikipedia.org/wiki/Weber_(Einheit)); 1 Wb = 1 kg\*m\^2/s\^2/A, {{Version/de|0.19}}

Magnetische Flußdichte:

  Einheit   Beschreibung
  --------- ------------------------------------------------------------------------------------------------------------------------
  G         [Gauß (Einheit)](https://de.wikipedia.org/wiki/Gau%C3%9F_(Einheit)); 1 G = 1 e-4 T, {{Version/de|0.19}}
  T         [Tesla (Einheit)](https://de.wikipedia.org/wiki/Tesla_(Einheit)); 1 T = 1 kg/s\^2/A, {{Version/de|0.19}}

Masse:

  Einheit   Beschreibung
  --------- ---------------------------------------------------------------------------------
  ug        Micro[gramm](https://de.wikipedia.org/wiki/Gramm); Alternative zur Einheit *µg*
  µg        Micro[gramm](https://de.wikipedia.org/wiki/Gramm); Alternative zur Einheit *ug*
  mg        Milli[gramm](https://de.wikipedia.org/wiki/Gramm)
  g         [Gramm](https://de.wikipedia.org/wiki/Gramm)
  kg        Kilo[gramm](https://de.wikipedia.org/wiki/Gramm)
  t         [Tonne (Einheit)](https://de.wikipedia.org/wiki/Tonne_(Einheit))
  oz        [Unze](https://de.wikipedia.org/wiki/Unze)
  lb        [Pfund](https://de.wikipedia.org/wiki/Pfund); Alternative zur Einheit *lbm*
  lbm       [Pfund](https://de.wikipedia.org/wiki/Pfund); Alternative zur Einheit *lb*
  st        [Stone (Einheit)](https://de.wikipedia.org/wiki/Stone_(Einheit))
  cwt       [Hundredweight](https://de.wikipedia.org/wiki/Hundredweight)

Energie:

  Einheit   Beschreibung
  --------- ----------------------------------------------------------------------------------------------
  W         [Watt(Einheit)](https://de.wikipedia.org/wiki/Watt_(Einheit))
  kW        Kilo-[Watt](https://de.wikipedia.org/wiki/Watt_(Einheit)), {{Version/de|0.19}}
  VA        [Voltampere](https://de.wikipedia.org/wiki/Voltampere)

Druck:

  Einheit   Beschreibung
  --------- -----------------------------------------------------------------------------------------------------------------------------
  Pa        [Pascal (Einheit)](https://de.wikipedia.org/wiki/Pascal_(Einheit))
  kPa       Kilo-[Pascal (Einheit)](https://de.wikipedia.org/wiki/Pascal_(Einheit))
  MPa       Mega-[Pascal (Einheit)](https://de.wikipedia.org/wiki/Pascal_(Einheit))
  GPa       Giga-[Pascal (Einheit)](https://de.wikipedia.org/wiki/Pascal_(Einheit))
  mbar      Milli-[Bar (Einheit)](https://de.wikipedia.org/wiki/Bar_(Einheit)), {{Version/de|0.19}}
  bar       [Bar (Einheit)](https://de.wikipedia.org/wiki/Bar_(Einheit)), {{Version/de|0.19}}
  uTorr     Micro-[Torr](https://de.wikipedia.org/wiki/Torr); Alternative zu Einheit *µTorr*
  µTorr     Micro-[Torr](https://de.wikipedia.org/wiki/Torr); Alternative zu Einheit *uTorr*
  mTorr     Milli-[Torr](https://de.wikipedia.org/wiki/Torr)
  Torr      [Torr](https://de.wikipedia.org/wiki/Torr); 1 Torr = 133.32 Pa
  psi       [Pound-force per square inch](https://de.wikipedia.org/wiki/Pound-force_per_square_inch); 1 psi = 6.895 kPa
  ksi       Kilo-[Pound-force per square inch](https://en.wikipedia.org/wiki/Pounds_per_square_inch)
  Mpsi      Mega-[Pound-force per square inch](https://en.wikipedia.org/wiki/Pounds_per_square_inch), {{Version/de|0.19}}

Temperatur:

  Einheit   Beschreibung
  --------- -----------------------------------------------------------------------------------
  uK        Micro[kelvin](https://de.wikipedia.org/wiki/Kelvin); Alternative zur Einheit *µK*
  µK        Micro[kelvin](https://de.wikipedia.org/wiki/Kelvin); Alternative zur Einheit *uK*
  mK        Milli[kelvin](https://de.wikipedia.org/wiki/Kelvin)
  K         [Kelvin](https://de.wikipedia.org/wiki/Kelvin)

Zeit:

  Einheit    Beschreibung
  ---------- ---------------------------------------------------------------------------------------------------------
  s          [Secunde](https://de.wikipedia.org/wiki/Sekunde)
  min        [Minute](https://de.wikipedia.org/wiki/Minute)
  h          [Stunde](https://de.wikipedia.org/wiki/Stunde)
  Hz (1/s)   [Hertz (Einheit)](https://de.wikipedia.org/wiki/Hertz_(Einheit)), {{Version/de|0.19}}
  kHz        Kilo[hertz (Einheit)](https://de.wikipedia.org/wiki/Hertz_(Einheit)), {{Version/de|0.19}}
  MHz        Mega[hertz (Einheit)](https://de.wikipedia.org/wiki/Hertz_(Einheit)), {{Version/de|0.19}}
  GHz        Giga[hertz (Einheit)](https://de.wikipedia.org/wiki/Hertz_(Einheit)), {{Version/de|0.19}}
  THz        Tera[hertz (Einheit)](https://de.wikipedia.org/wiki/Hertz_(Einheit)), {{Version/de|0.19}}

Volumen:

  Einheit   Beschreibung
  --------- ------------------------------------------------------------------------------------------------------------
  ml        Milli[liter](https://de.wikipedia.org/wiki/Liter), {{Version/de|0.19}}
  l         [Liter](https://de.wikipedia.org/wiki/Liter)
  cft       Kubik-[Fuß (Einheit)](https://de.wikipedia.org/wiki/Fu%C3%9F_(Einheit)), {{Version/de|0.19}}

Imperiale Spezialeinheiten:

  Einheit   Beschreibung
  --------- ---------------------------------------------------------------------------------------------------------
  mph       [Meilen pro Stunde](https://de.wikipedia.org/wiki/Meilen_pro_Stunde), {{Version/de|0.19}}
  sqft      [Quadratfuß](https://de.wikipedia.org/wiki/Quadratfu%C3%9F), {{Version/de|0.19}}

Die folgenden häufig verwendeten Einheiten werden noch nicht unterstützt:

  Einheit   Beschreibung                                                                                                              Alternative
  --------- ------------------------------------------------------------------------------------------------------------------------- --------------------------
  °C        [Grad Celsius](https://de.wikipedia.org/wiki/Grad_Celsius)                                                                \[°C\] + 273.15 K
  °F        [Grad Fahrenheit](https://de.wikipedia.org/wiki/Grad_Fahrenheit);                                                         (\[°F\] + 459.67) × ​5/9
  u         [Atomare Masseneinheit](https://de.wikipedia.org/wiki/Atomare_Masseneinheit); Alternative zur Einheit \'Da\' (Dalton) =   1.66053906660e-27 kg
  Da        [Dalton](https://de.wikipedia.org/wiki/Atomare_Masseneinheit); Alternative zur Einheit \'u\'                              1.66053906660e-27 kg
  sr        [Steradiant](https://de.wikipedia.org/wiki/Steradiant)                                                                    nicht direkt
  lm        [Lumen (Einheit)](https://de.wikipedia.org/wiki/Lumen_(Einheit))                                                          nicht direkt
  lx        [Lux (Einheit)](https://de.wikipedia.org/wiki/Lux_(Einheit))                                                              nicht direkt
  px        [Pixel](https://de.wikipedia.org/wiki/Pixel)                                                                              nicht direkt

## Ungültige Zeichen und Namen 

Das Ausdrucks-Feature ist sehr leistungsfähig. Um das zu ermöglichen gibt es ein paar Einschränkungen bei ein paar Zeichen. Als Abhilfe gibt es in FreeCAD die Möglichkeit anstatt der Objektnamen sog. Bezeichner (\'labels\') zu verwenden und sich auf diese zu beziehen.

In Fällen, in denen du keine Beschriftung verwenden kannst, wie z. B. der Name einer Skizzenbeschränkung, musst du dir bewusst sein, welche Zeichen nicht erlaubt sind.

### Bezeichner

Für [Bezeichner](Object_name/de#Bezeichner.md) gibt es keine ungültigen Zeichen, jedoch müssen einige Zeichen maskiert werden:

+----------------------------------------------------------+-------------------------------------------------------------------------------+
| Zeichen                                                  | Beschreibung                                                                  |
+==========================================================+===============================================================================+
|                                           | Müssen durch das Voranstellen von `\` maskiert werden. |
| `'`                                             |                                                                               |
|                                                       |                                                                               |
| , `\`, `"` |                                                                               |
+----------------------------------------------------------+-------------------------------------------------------------------------------+

Zum Beispiel muss der Bezeichner `Skizze\002` als `<<Skizze\002>>` referenziert werden.

### Namen

[Namen](Object_name/de#Name.md) von Objekten wie Dimensionen, Skizzen, usw. dürfen folgende Zeichen oder Zeichenfolgen nicht enthalten. Anderenfalls ist der Namen ungültig.

  Zeichen / Zeichenfolgen                                                                                                                    Beschreibung
  ------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------
  **+**, **-**, **\***, **/**, **\^**, **\_**, **\<**, **\>**, **(**, **)**, **{**, **}**, **\[**, **\]**, **.**, **,**, **=**               Zeichen die als mathematische Operatoren funktionieren.
  **A**, **kA**, **mA**, **MA**, **C**, **G**, **F**, **uF**, **µF**, **J**, **K**, \'\'\' \' \'\'\', \'\'\' ft \'\'\', **°**, und solche!   Zeichen oder Zeichenfolgen, die als [Einheiten](Expressions/de#Units.md) verwendet werden.
  **\#**, **!**, **?**, **§**, **\$**, **%**, **&**, **:**, **;**, **\\**, **\|**, **\~**, **∆**, **¿**, und solche!                         Zeichen, die als Platzhalter verwendet werden oder die Funktionen auslösen.
  **pi**, **e**                                                                                                                              Mathematische Konstanten
  **´**, **\**, \'\'\' \' \'\'\', **\"**                                                                                                    Akzente
  Leerzeichen (Space)                                                                                                                        Ein Leerzeichen definiert das Ende eines Namens und kann daher nicht Teil des Namens sein.

Beispielsweise ist folgender Name gültig: \>.Constraints.mol** (mol ist eine Einheit).

Da kürzere Namen (vor allem, wenn sie nur ein oder zwei Zeichen haben) leicht zu ungültigen Namen führen können, sollte die Verwendung längerer Namen in Betracht gezogen und/oder eine geeignete Namenskonvention festgelegt werden.

### Zell Aliase 

Für [Kalkulationstabelle SetzeAlias](Spreadsheet_SetAlias/de.md) sind nur alphanumerische Zeichen und Unterstriche erlaubt (`A` bis `Z`, `a` bis `z`, `0` bis `9` und `_`).

## Referenzen auf CAD Daten 

Es ist möglich, Daten aus dem Modell selbst in einem Ausdruck zu verwenden. Um auf eine Eigenschaft zu verweisen, verwende `object.property`. Wenn die Eigenschaft ein Verbund von Feldern ist, kann auf die einzelnen Felder mit `object.property.field` zugegriffen werden.

Die folgende Tabelle zeigt einige Beispiele:

+----------------------------------------------------------+--------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CAD-Daten                                                | Aufruf im Ausdruck                   | Ergebnis                                                                                                                                                      |
+==========================================================+======================================+===============================================================================================================================================================+
| Parametrische Länge eines Quaders im Arbeitsbereich Part |                       |                                                                                                                                                |
|                                                          | `Cube.Length`               | `Length`                                                                                                                                             |
|                                                          |                                   |                                                                                                                                                            |
|                                                          |                                      | mit der Einheit mm                                                                                                                                            |
+----------------------------------------------------------+--------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Volumen des Würfels                                      |                       |                                                                                                                                                |
|                                                          | `Cube.Shape.Volume`         | `Volume`                                                                                                                                             |
|                                                          |                                   |                                                                                                                                                            |
|                                                          |                                      | in mm³ ohne Einheiten                                                                                                                                         |
|                                                          |                                      |                                                                                                                                                               |
|                                                          |                                      | |-en  in mm³ Ausgabe ohne Einheiten                                                                                                                         |
+----------------------------------------------------------+--------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Typ der Würfelform (geometrische Figur)                  |                       | String: Solid                                                                                                                                                 |
|                                                          | `Cube.Shape.ShapeType`      |                                                                                                                                                               |
|                                                          |                                   |                                                                                                                                                               |
+----------------------------------------------------------+--------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Etikett des Würfels                                      |                       | String: Label                                                                                                                                                 |
|                                                          | `Cube.Label`                |                                                                                                                                                               |
|                                                          |                                   |                                                                                                                                                               |
+----------------------------------------------------------+--------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| X-Koordinate des Schwerpunktes des Würfels               |                       | X-Koordinate in mm ohne Einheiten                                                                                                                             |
|                                                          | `Cube.Shape.CenterOfMass.x` |                                                                                                                                                               |
|                                                          |                                   |                                                                                                                                                               |
+----------------------------------------------------------+--------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Wert der Beschränkung in einer Skizze                    |                       | numerischer Wert der benannten Beschränkung \'`Width`\' (Breite) in der Skizze, wenn der Ausdruck in der Skizze selbst verwendet wird. |
|                                                          | `Constraints.Width`         |                                                                                                                                                               |
|                                                          |                                   |                                                                                                                                                               |
+----------------------------------------------------------+--------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Wert eines Alias einer Kalkulationstabelle               |                       | Wert eines Alias \"`Depth`\" (Tiefe) in der Kalkulationstabelle \"`Spreadsheet`\"                               |
|                                                          | `Spreadsheet.Depth`         |                                                                                                                                                               |
|                                                          |                                   |                                                                                                                                                               |
+----------------------------------------------------------+--------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Wert einer lokalen Eigenschaft eines Objekts             |                       | Wert der Eigenschaft `Length` (Länge) z.B. in einem Pad-Objekt, wenn der Ausdruck z.B. in Length2 im gleichen Objekt verwendet wird.   |
|                                                          | `Length`                    |                                                                                                                                                               |
|                                                          |                                   |                                                                                                                                                               |
+----------------------------------------------------------+--------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Dokumentweit gültige globale Variablen 

In FreeCAD gibt es zur Zeit kein Konzept für globale Variablen. Stattdessen können beliebige Variablen mit Hilfe der [Arbeitsbereich Kalkulationstabelle](Spreadsheet_Workbench/de.md) als Zellen in einer Kalkulationstabelle definiert werden und dann mit Hilfe der Alias Eigenschaft für die Zelle (Rechtsklick auf die Zelle) einen Namen erhalten. Dann kann von jedem Ausdruck aus auf sie zugegriffen werden, wie auf jede andere Objekteigenschaft auch.

## Dokumentenübergreifende Verweise 

Es ist (mit Begrenzungen) möglich, eine Eigenschaft eines Objekts in deinem aktuellen Dokument (\".FCstd\" Datei) durch Verwendung eines Ausdrucks zu definieren, um auf eine Eigenschaft eines Objekts in einem anderen Dokument zu verweisen (\".FCstd\" file). Zum Beispiel kann eine Zelle in einer Kalkulationstabelle oder die {{PropertyData/de|Länge}} eines Formteil Würfels usw. in einem Dokument durch einen Ausdruck definiert werden, der auf den X Platzierungswert oder eine andere Eigenschaft eines Objekts in einem anderen Dokument verweist.

Der Name des Dokuments wird verwendet, um von einem anderen Dokument aus darauf zu referenzieren. Wenn ein Dokument zum ersten Mal gespeichert wird, muss dem Dokument ein Name gegeben werden. Dies ist normalerweise ein anderer Name als die Vorgabe \"Unbenannt1\". Um zu verhindern, dass Verknüpfungen beim Speichern des Hauptdokumentes verloren gehen, wenn dieses dabei einen anderen Namen bekommt, sollte das Hauptdokument zuerst mit einer Kalkulationstabelle erstellt werden. Danach kann der Inhalt des Dokuments geändert und das Dokument gespeichert werden, aber es darf nicht umbenannt werden.

Sobald das Mutterdokument mit der Kalkulationstabelle erstellt und gespeichert (benannt) ist, können abhängige Dokumente erstellt werden. Angenommen, du nennst das Mutterdokument `master`, die Kalkulationstabelle `modelConstants` und gibst einer Zelle einen Alias-Namen `Length`, dann kannst du auf den Wert zugreifen als:


`master#modelConstants.Length`

**Hinweis:** dass das Mutterdokument geladen sein muss, damit die Werte des Mutterdokuments für das abhängige Dokument verfügbar sind.

Leider meldet der integrierte Prüfer manchmal, dass ein gültiger Name nicht existiert. Tippe trotzdem weiter. Wenn du die vollständige Referenz eingegeben hast, wird die Schaltfläche **OK** aktiv.

Natürlich liegt es bei dir, die zugehörigen Dokumente später zu laden, wenn du etwas ändern willst.

## Bekannte Probleme / Verbleibende Aufgaben 

-   Das Abhängigkeitsdiagramm basiert auf der Beziehung zwischen Dokumentobjekten, nicht auf Eigenschaften. Das bedeutet, dass man nicht Daten einem Objekt zur Verfügung stellen kann und gleichzeitig Daten von diesem Objekt abfragt. Auch wenn es beispielsweise keine zyklischen Abhängigkeiten gibt, wenn die Eigenschaften selbst berücksichtigt werden, kann es vorkommen, dass es kein Objekt gibt, das seine Abmessungen aus einer Kalkulationstabelle erhält und dann das Volumen dieses Objekts in derselben Kalkulationstabelle anzeigt. Zur Umgehung des Problems können mehrere Tabellen angelegt werden: Eine Tabelle, die die Objektdaten zur Verfügung stellt und eine andere zur Datenauswertung.
-   Der Analysator für Ausdrücke kann mit Klammern nicht gut umgehen und ist nicht in der Lage, einige Ausdrücke korrekt zu analysieren. Zum Beispiel führt `<nowiki>=</nowiki> (A1 > A2) ? 1 : 0` zu einem Fehler, während `<nowiki>=</nowiki> A1 > A2 ? 1 : 0` akzeptiert wird. Der Ausdruck `<nowiki>=</nowiki> 5 + ((A1>A2) ? 1 : 0)` kann in keiner Form eingegeben werden.
-   Wie oben erwähnt, erkennt der eingebaute Formelprüfer einen gültigen Namen manchmal nicht. Daher einfach mit der Eingabe fortfahren. Wenn die vollständige Verknüpfung eingegeben ist, wird die Schaltfläche **OK** aktiv.
-   FreeCAD hat bisher keinen eingebauten Ausdrucksverwalter, mit dem alle Ausdrücke in einem Dokument aufgeführt und erstellt, gelöscht, abgefragt, etc. werden können. Aber es ist ein Addon verfügbar: [fcxref expression manager](https://github.com/gbroques/fcxref).
-   Offene Fehler/Tickets für die Ausdrücke (Expressions) können hier nachgeschlagen werden: [FreeCAD Bugtracker Expressions category](https://freecadweb.org/tracker/set_project.php?project_id=4;20)


{{Powerdocnavi

}} 

[Category:Spreadsheet](Category:Spreadsheet.md)
