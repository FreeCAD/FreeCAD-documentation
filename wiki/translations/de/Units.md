# Units/de
Einige Artikel zu Einheiten:

-   [Metrologie](https://de.wikipedia.org/wiki/Metrologie) (Meßwesen)
-   [SI System](https://de.wikipedia.org/wiki/Internationales_Einheitensystem)
-   [Angloamerikanisches Maßsystem (Imperiale Einheiten)](https://de.wikipedia.org/wiki/Angloamerikanisches_Ma%C3%9Fsystem)
-   [Abgeleitete SI Einheiten](https://de.wikipedia.org/wiki/Internationales_Einheitensystem#Abgeleitete_SI-Einheiten_mit_besonderem_Namen)
-   [Grad(Winkel)](https://de.wikipedia.org/wiki/Grad_(Winkel))
-   [In OCC implementierte Einheiten](https://github.com/3drepo/occt/blob/master/src/UnitsAPI/Units.dat)

## Beispiele


```python
# -- some examples of the FreeCAD unit translation system --
# make a shortcut for the examples
pq = FreeCAD.Units.parseQuantity

# 10 meters in internal numbers
pq('10 m')

# doing math
pq('3/8 in')

# combined stuff
pq('100 km/h')

# transfer to other units
pq('100 km/h')/tu('m/s')

# derived units (Ohm)
pq('m^2*kg*s^-3*A^-2')

# or
pq('(m^2*kg)/(A^2*s^3)')

# angles 
pq('2*pi rad') # full circle

# as gon
pq('2*pi rad') / tu('gon')

# more imperial
tu('1ft (3+7/16)in')

# or 
pq('1\' (3+7/16)"') # the ' we have to escape because of python

# trigonometry
pq('sin(pi)')

# Using translated units as parameters, this command will create a 50.8mm x 20mm x 10mm box
b = Part.makeBox(pq('2in'), pq('2m')/100, 10)
```

## Unterstützte Einheiten 

Eine vollständige Liste aller unterstützten Einheiten kann [hier gefunden](Expressions/de#Einheiten.md) werden.

## Ziele und Grundsätze: Vorschlag für eine Erweiterung des Einheitenverwaltungssystems 

Eine Erweiterung des Einheitenverwaltungssystems wird in den folgenden Abschnitten vorgeschlagen und das Konzept eines *Einheitensystems* entwickelt, das während einer laufenden FreeCAD-Instanz aktiviert wird. Das Interesse an der Definition eines neues Konzepts ist es, einfacher mit einer größtmöglichen Anzahl von **physischen** Einheiten arbeiten zu können (selbst mit benutzerdefinierten), ohne die Komplexität der Einheitenverwaltung für den Benutzer oder die FreeCAD-Entwickler zu erhöhen.

Kurzgesagt werden Ereignisse von Einheitenskalierung präzise lokalisiert und in einer generischen Weise ausgeführt.

Die Erreichung solch einer Flexibilität ist insbesondere dann erforderlich, wenn man mit Materialeigenschaften hantiert, die sehr unterschiedlich sein können, und sie manuell schwierig zu verarbeiten sind.

Die vorgeschlagene Argumentation erlaubt die Behandlung von Einheiten wie in [Guide for the Use of the International System of Units (SI)](http://physics.nist.gov/cuu/pdf/sp811.pdf) und [The International System of Units (SI)](http://physics.nist.gov/Pubs/SP330/sp330.pdf) beschrieben, beide vom NIST.

In diesem Vorschlag wird im Abschnitt [Ideenfindung](Units/de#Brainstorming.md) zunächst daran erinnert, welche möglichen Kontexte für eine Einheitenverwaltung erforderlich sind.

Im [Organisieren](Units/de#Organizing.md) Abschnitt stellen wir das Datenmodell vor, das zur Erreichung der Einheitenverwaltung beibehalten wurde, basierend auf 3 Objekten, der *Einheit*, dem *Einheitenwörterbuch* und dem *Einheitensystem*. Schließlich wird auch eine kurze API eines 4. Objekts namens *Einheitenverwalter* vorgestellt.

## Ergebnis

Dank dieser Erweiterung soll die Skalierung von Einheiten, die zwischen verschiedenen geschäftlichen Aufgaben auftreten können, erleichtert werden. Beispielsweise können technische Zeichnungen im Standard Einheitensystem erstellt werden, während die FE Modellierung in einem dafür besser geeigneten Einheitensystem verwaltet werden kann.

Der Datenaustausch zwischen diesen beiden Arten von Aktivitäten wird mit dieser Erweiterung einfacher.

## Ideenfindung

In diesem Abschnitt werden die Anwendungszusammenhänge eines solchen Einheitenverwaltungssystems hervorgehoben. Anhand dieser Zusammenhänge können wir dann seine technischen Spezifikationen festlegen.

Im Wesentlichen werden 2 Zusammenhänge als Beispiel angeführt.

### Zusammenhang 1: Öffnen einer Datendatei 

Dieser Fall ist wahrscheinlich der häufigste Fall. Du erhältst eine Datei, die zum Beispiel ein geometrisches Modell enthält oder ein Material mit ziemlich vielen Eigenschaften beschreibt. Das geometrische Modell wird in Metern oder die Materialeigenschaften nach dem internationalen Einheitensystem ausgedrückt.

Wie schade\...

Du bist ein Experte für FE Modellierung und arbeitest normalerweise mit Millimeter für Länge, MegaPascal für Spannung, Tonne für Masse\...

In diesem Zusammenhang ist das Einheitenmanagement erforderlich, um Daten von einem in der Eingabedatei definierten Anfangseinheitensystem auf ein benutzerdefiniertes Zieleinheitensystem zu skalieren.

### Zusammenhang 2: Umschalten des Einheitensystems während der Laufzeit 

In diesem Fall kannst du gleichzeitig derjenige sein, der eine Zeichnung ausführt, und derjenige, der die FE Modellierung verwaltet. Ähnlich wie im vorigen Fall sind die Einheitensysteme für diese beiden Aufgaben nicht identisch, und du musst das anfängliche Einheitensystem während der Laufzeit auf dein Lieblingssystem umstellen.

## Organisieren

### Logik der Einheitenskalierung 

Im Abschnitt [Ideenfindung](Units/de#Ideenfindung.md) wurden 2 Zusammenhänge bei der Verwendung der Einheitenskalierung vorgestellt. Aus diesen beiden Zusammenhänge sollen einige Punkte hervorgehoben werden.

#### Einheitenkohärenz in der gesamten laufenden FreeCAD Instanz 

Das vorgeschlagene System basiert auf einer primären Annahme: Der Benutzer arbeitet in einem kohärenten Einheitensystem. Das bedeutet zum Beispiel, dass, wenn der Benutzer die Länge in Millimetern ausdrückt, die Bereiche notwendigerweise in Form von quadrierten Millimetern und nicht in quadrierten Metern ausgedrückt werden. Dies ist **Hypothese eins**.

#### Einheitensystem

Aufgrund der *Hypothese 1* ist es möglich und relevant, ein Einheitensystem zu definieren. Ein Einheitensystem gilt für:

-   eine laufende FreeCAD Instanz, in der du gerade arbeitest
-   oder es kann auch global für den Inhalt einer Eingabedatei gelten

Gemäß [Guide for the Use of the International System of Units (SI)](http://physics.nist.gov/cuu/pdf/sp811.pdf) vom NIST sind es 7 physikalische Basiseinheiten. Wir haben uns dafür entschieden, ein Einheitensystem in Form dieser 7 Basiseinheiten auszudrücken.

When working within an instance of FreeCAD, the user has thus to define first the unit system according to which she/he is working before she/he decides to switch to another unit system, or before importing data from an input file.

Dieses Einheitensystem gilt so lange, bis der Anwender beschließt, es zu ändern. Wenn sie/er dies tut, werden alle Daten mit Abmessungen skaliert.

Bei der *Hypothese eins* wird davon ausgegangen, dass alle Daten, die der Anwender manuell in FreeCAD eingibt, mit dem gewählten Einheitensystem kohärent sind.

Der Nutzen, mit einem *Einheitensystem* zu arbeiten, das auf der Ebene einer FreeCAD Laufinstanz oder auf Datendateiebene definiert ist (anstelle von *Einheiten*, die auf der Datenebene definiert sind), besteht darin, dass die Einheitenverwaltung erheblich vereinfacht wird

Hier sind einige Beispiele für Einheitensysteme.

-   Meter, Kilogramm, Sekunde, Ampere, Kelvin, Mol, Candela
-   Millimeter, Tonne, Millisekunde, Ampere, Kelvin, Mol, Candela
-   Millimeter, Kilogramm, Millisekunde, Ampere, Kelvin, Mol, Candela
-   \...

#### Basis- und abgeleitete Einheiten 

Abgeleitete Einheiten werden durch Kombination von Basiseinheiten gebildet. Zum Beispiel kombiniert eine Beschleunigung (m/s) gleichzeitig Länge und Zeit. Ein interessantes Bild, das die Beziehungen zwischen Basis- und abgeleiteten Einheiten darstellt, ist [hier](http://physics.nist.gov/cuu/pdf/SIDiagramColorAnnot.pdf) auch vom NIST zu sehen.

Dank der Definition des *Einheitensystems* ist es dem Anwender möglich, mit jeder Art von abgeleiteten Einheiten zu arbeiten, ohne dass die FreeCADbEntwickler diese im Voraus vorsehen müssen.

#### Base and derived unit symbols 

According to [The International System of Units (SI)](http://physics.nist.gov/Pubs/SP330/sp330.pdf), the symbols to specify a units are officially approved. Two consequences can be highlighted from this.

-   it is not easy for a computer program to work with unit symbols because some are greek letters for instance. Hence they can be a bit difficult to process by a program
-   while some units and their symbols can be used widely, they may be not approved officially, like for instance *tonne* unit (see p32 of [The International System of Units (SI)](http://physics.nist.gov/Pubs/SP330/sp330.pdf))

To overcome these limitations and remain flexible, the proposed system favors the use of unit magnitudes instead of unit symbols, which remain nonetheless available for an ergonomy reason.

### Datenmodell

Es werden die drei Kernobjekte des Einheitenmanagementsystems vorgestellt, nämlich die *Einheiten*, das *Einheitenbeschreibungsverzeichnis* und das *Einheitensystem*.

#### Unit

As a foreword, it is important to highlight that a *unit* object in itself only indicates a **dimension** like length, mass, time\... It doesn\'t specify a **magnitude** like meter, millimeter, kilometer\... This last information is specified through the unit system.

##### Dimension

Compulsory string indicating the *dimension* of the unit. The *dimension* of the 7 base units are indicated below (from [Guide for the Use of the International System of Units (SI)](http://physics.nist.gov/cuu/pdf/sp811.pdf)).

-   LENGTH
-   MASS
-   TIME
-   ELECTRIC CURRENT
-   THERMODYNAMIC TEMPERATURE
-   AMOUNT OF SUBSTANCE
-   LUMINOUS INTENSITY

*Dimension* attribute allows identifying the unit. Two units cannot share the same *dimension*.

##### Signatur

Compulsory integer array of size 7 (number of base units) that defines what the unit is. The signature of the 7 base units are:

-   LENGTH: \[1,0,0,0,0,0,0\]
-   MASS: \[0,1,0,0,0,0,0\]
-   TIME: \[0,0,1,0,0,0,0\]
-   ELECTRIC CURRENT: \[0,0,0,1,0,0,0\]
-   THERMODYNAMIC TEMPERATURE: \[0,0,0,0,1,0,0\]
-   AMOUNT OF SUBSTANCE: \[0,0,0,0,0,1,0\]
-   LUMINOUS INTENSITY: \[0,0,0,0,0,0,1\]

From these 7 units, we are then able to express all derived units defined in [Guide for the Use of the International System of Units (SI)](http://physics.nist.gov/cuu/pdf/sp811.pdf) and create new ones as needed such as for instance:

-   MASS DENSITY: \[-3,1,0,0,0,0,0\]
-   AREA: \[0,2,0,0,0,0,0\]

*Signature* is the attribute thanks to which unit scaling can be achieved in a generic way.

##### Symbols

Array of \[real, string\] (meaning \[*magnitude*, *symbol*\]) that lists all *symbols* known by FreeCAD. Thanks to this array, the unit scaling API becomes more ergonomic because *symbols* and related *magnitudes* are linked.

This array can be extended as required.

For instance, the list of *symbols* of the LENGTH unit, and their related *magnitudes* is:

[1e+12,"Tm"],[1e+09,"Gm"],[1e+06,"Mm"],
[1e+03,"km"],[1e+02,"hm"],[1e+01,"dam"],
[1e+00,"m"],[1e-01,"dm"],[1e-02,"cm"],
[1e-03,"mm"],[1e-06,"µm"],[1e-09,"nm"],
[1e-12,"pm"],[1e-15,"fm"]

Standard *symbols* can be found on [NIST website](http://physics.nist.gov/cuu/Units/units.html) and p23 to 26 and p32 (*metric ton* or *tonne*) of [The International System of Units (SI)](http://physics.nist.gov/Pubs/SP330/sp330.pdf).

#### Unit dictionary 

All the units available in FreeCAD, and new ones created by the user, should be stored in *unit dictionary*, which is an XML file (FreeCAD configuration file), so as to be retrieved when needed, i.e. when achieving unit scaling.

##### Units

Array of units, contained in the *unit dictionary*.

#### Unit system 

A *unit system* is the object that allows the user defining the current unit *magnitude* of each base units with which she/he is working. For instance, knowing that the user is working with millimeter, tonne, and second, thanks to the use of a unit system, FreeCAD can know that energy is expressed in terms of milliJoule, force in terms of Newton, and stress in terms of MegaPascal. Hence a unit system is only defined by a *name* (for instance *Standard unit system*) and a *magnitude table* specifying for each of the 7 base units, what is its corresponding *magnitude*.

##### Name

String allowing to the user identifying what is the unit system.

##### Magnitudes

By specifying the magnitude of the 7 base units, a unit system is defined.

For instance \[1e-03, 1e+03, 1, 1, 1, 1, 1\], meaning millimeter, tonne, second, ampere, Kelvin, mole, candela

#### Unit management API 

Only the logic of some methods is presented, in order to highlight some features. These methods could belong to an object called *Unit manager*.

##### Checking the unit dictionary 

###### isValid

The unit dictionary can be an XML file (FreeCAD configuration file). It contains a list of defined units. Such a dictionary is required for the proposed unit management system to work.

It must fulfills some conditions that should be checked before activating the unit management system. These conditions are:

-   check that all base units are defined
-   check that a *dimension* is not defined twice through the units
-   check that a *symbol* is not defined twice in all the existing symbols
-   check that the *signatures* of all units have all the same size
-   chacke that a *standard symbol* (for which *magnitude* is 1) is defined for all units

###### isCompatibleWithThisSignature

A unit dictionary defines a set of units and their known magnitudes. When managing a unit, it is relevant to check that its signature is compatible with the set of units registered in the unit dictionary, so as to process it. This check includes:

-   check that the input *signature* length is of the same size than the unit dictionary unit *signatures*

##### Scaling units 

###### scaleUnitFromSymbolToSymbol

Knowing a value, an initial unit by its symbol, the target unit by its symbol, scale the value.

###### scaleUnitFromSymbolToUnitSystem

Knowing a value, an initial unit by its symbol, the target unit system, scale the value.

###### scaleUnitFromUnitSystemToSymbol

Knowing a value, an initial unit system, the target unit by its symbol, scale the value.

#### Motivations for such a management: example of application 

Let\'s assume that we are going to setup a finite element model. To build our model, we need the mesh, material properties, and to define numerical parameters. Considering that they can be tens of material properties to manage, expressed with different units, sometimes not always very common, it is interesting for the user to only have to specify a global unit system, without caring much.

FreeCAD würde dann einfach die Arbeit erledigen.

As FreeCAD developpers and FreeCAD users do not necessarily know all units that can be defined in the material property files, it is interesting to rely on a generic system.

Let\'s assume that in such a file we have a fair number of exotic material properties expressed with exotic units, and that we want to work in a specific unit system.

It is easy with the proposed extension to scale any of these properties by knowing their signatures, magnitudes, and the target unit system.

For each of the properties, the scaling is obtained by multiplying the initial property value with the factor $\frac{initialMagnitude}{targetMagnitude}$.

The *targetMagnitude* is then simply obtained with the operation $\prod_{bu} targetMagnitude_{bu}^{signature_{bu}}$, *bu* standing for *base unit*.

So wird es sehr einfach, mit wenigen Zeilen Python eine beliebige Anzahl von Objekten mit beliebigen Einheiten zu verwalten.

## Siehe auch 


<div class="mw-translate-fuzzy">

-   Implementieren der Klassen Quantity und Unit (größtenteils fertig)
-   Implementieren von InputField als Benutzer Frontend (in Arbeit)
-   UnitsCalculator als Testumgebung (in Arbeit)
-   [MengeDokumentation](Quantity/de.md)
-   [Std UnitsCalculator](Std_UnitsCalculator/de.md) Dokumentation
-   Aktualisierung des Werkstoff Frameworks, um nur noch mit Quantities zu arbeiten
-   Testfälle


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > Units/de
