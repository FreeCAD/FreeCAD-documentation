---
- TutorialInfo:/de
   Topic:Schiff Arbeitsbereich
   Level:Anfänger
   Time:
   Author:
   FCVersion:
   Files:
---

# FreeCAD-Ship s60 tutorial/de







## Einführung

In diesem Tutorium werden wir mit einem Serie 60 Schiff der Universität von Iowa arbeiten. Das Tutorium soll zeigen, wie man mit einem symmetrischen Einrumpfschiff arbeiten kann, aber auch Mehrrumpf- oder nicht-symmetrische Schiffe können mit dem gleichen Verfahren ausgeführt werden.

Erfahre mehr über <img alt="" src=images/Workbench_Ship.svg  style="width:24px;"> [Arbeitsbereich Schiff](Ship_Workbench/de.md).



## Belastungsgeometrie

### Hintergrund

Die <img alt="" src=images/Workbench_Ship.svg  style="width:24px;"> [Arbeitsbereich Schiff](Ship_Workbench/de.md) arbeitet über **Schiffsentitäten**, die auf der bereitgestellten Geometrie erstellt werden müssen. Bei der Geometrie muss es sich um einen Festkörper (oder einen Satz von Festkörpern) handeln, wobei die folgenden Kriterien berücksichtigt werden müssen:

-   Die gesamte Rumpfgeometrie muss bereitgestellt werden (einschließlich symmetrischer Körper).
-   Die Steuerbord Geometrie muss im negativen Bereich \"y\" enthalten sein.
-   Der Nullpunkt (0,0,0) ist der *Mittschiffsabschnitt* (Mittelpunkt zwischen dem hinteren und vorderen Lot) und des *Basislinien* Schnittpunkts.

![Schematische Ansicht der Vorzeichenkriterien](images/FreeCAD-Ship-SignCriteria.jpg )


<center>

FreeCAD-Schiff Vorzeichenkriterien


</center>

### Laden der Serie 60 Geometrie 

Um neue Anwender zu unterstützen, enthält der Arbeitsbereich Schiff einen Geometrie Beispiel Lader mit den folgenden Auswahlmöglichkeiten:

-   Serie 60 von der Universität Iowa
-   Wigley Kanonisches Schiff
-   Serie 60 Katamaran
-   Wigley Katamaran

![Schiffsgeometrien Beispielladersymbol.](images/Ship_Load.svg )


<center>

 Schiffsgeometrien Beispielladersymbol


</center>

Beim Ausführen des Werkzeugs (Schiffskonstruktion/Laden einer Beispielschiffsgeometrie) wird ein Aufgabendialog angezeigt. Wähle **Series 60 der Iowa Universität** und drücke Annehmen. Das Werkzeug lädt ein neues Dokument mit der **s60_IowaUniversity** Geometrie.


**'''Warnung, bevor irgendetwas bearbeitet wird!'''
Du arbeitest jetzt mit der originalen Beispieldatei.
Um das unbearbeitete Originalbeispiel zu erhalten, '''musst du es zuerst als neue Datei speichern, bevor du irgendetwas bearbeitest.'''**

## Schiffsinstanz erstellen 

Um eine **Schiffsinstanz** zu erstellen, wähle die Geometrie s60 und führe das *\'Schiffserstellungswerkzeug* (Schiffsentwurf/Erstellen eines neuen Schiffes) aus.

![Schiffserstellungswerkzeug Symbol.](images/Ship_Logo.svg )


<center>

Schiffserstellungswerkzeug Symbol


</center>

Erstellen eines Schiffsaufgabendialogs und einige Anmerkungen werden in der [3D Ansicht](3D_view/de.md) angezeigt. Die Anmerkungen verschwinden, wenn du das Werkzeug zum Erstellen eines Schiffs schließt, mache dir also keine Sorgen.

Die meisten wesentlichen Schiffsdaten müssen eingeführt werden (der <img alt="" src=images/Workbench_Ship.svg  style="width:24px;"> Arbeitsbereich Schiffe verwendet ein progressives Dateneinführungssystem, so dass grundlegende Arbeitsschritte ausgeführt werden können, wenn nur die grundlegenden Schiffsdaten bekannt sind. Mehr Informationen werden benötigt wenn die Arbeitsschritte komplexer werden).

### Schiffsdaten

die Hauptabmessungen müssen hier eingebracht werden:

-   Länge: Länge zwischen den Loten, 25,5 m für dieses Schiff.
-   Schiffsbreite: Gesamte Schiffsbreite, 3,389 m für dieses Schiff.
-   Tiefgang: Konstruktionstiefgang, 1,0 m für dieses Schiff.

![Anmerkungen zur Vorderansicht](images/FreeCAD-Ship-S60ShipCreationFront.png )


<center>

Längen Anmerkungen.


</center>

Normalerweise hängt die Länge zwischen den Loten vom Entwurfstiefgang ab. Wenn du also nicht weisst, wie lang dein Schiff ist, kannst du den Tiefgang einstellen und die Länge anpassen, um einen Schnittpunkt zwischen Bug und Tiefgang zu erhalten.

![Anmerkungen zur Seitenansicht](images/FreeCAD-Ship-S60ShipCreationSide.png )


<center>

Balken Anmerkungen.


</center>

Dasselbe Verfahren gilt für die Breitenpassung. Beachte, dass der angeforderte Wert die gesamte Breite ist, aber die Anmerkung bezieht sich nur auf die Steuerbordhälfte des Schiffes.

Wenn du die **Annehmen** Schaltfläche drückst, wird eine neue Schiffsinstanz mit dem Namen **Schiff** im Dialogfeld *Markierungen & Attribute* erstellt. Wir benötigen die Geometrie nicht mehr, du kannst sie also ausblenden.

![Schiffsinstanz Symbol](images/FreeCAD-Ship-ShipInstance.png )


<center>

Schiffsinstanz Symbol.


</center>

Von nun an musst du **Schiff** ausgewählt haben, bevor du eines der Schiffs Arbeitsbereich Werkzeuge ausführst.

## Linienzeichnen

Der Schiffs Arbeitsbereich stellt ein Werkzeug zur Verfügung, das es einfach macht, einen Linienplan von der Schiffslinienzeichnung zu bekommen.

![Umrisszeichnungswerkzeug.](images/Ship_OutlineDraw.svg )


<center>

Umrisszeichnungswerkzeugsymbol


</center>

Das Linienzeichen ist ein Satz von Linien aus Schnitten in allen 3 Achsen, die schließlich die Rumpfgeometrie in einem Linienplan zeigen. Wir müssen die Linien für die 3 folgenden Ansichten bereitstellen:

-   Spantenriss (unter Verwendung der transversalen Schnitte)
-   Längsriss (unter Verwendung der Längsschnitte)
-   Wasserlinienriss (unter Verwendung der Wasserlinienkürzungen)

### Transversale Schnitte 

Normalerweise müssen 21 transversale äquidistante Schnitte zwischen den Senkrechten durchgeführt werden. Um dies zu tun, stellt FreeCAD ein automatisches Werkzeug zur Verfügung, wähle einfach den **Transversal** Typ der Schnitte, gehe in das **Auto erstellen** Feld und setze **21** Schnitte, dann drücke **Schnitte erstellen**.

![Umrisszeichnung Transversale Schnitte Voransicht.](images/S60OutlineTransversal.png )


<center>

Umrisszeichnung Transversale Schnitte Voransicht


</center>

Die Sektionstabelle wird gefüllt und die Sektionsvorschau **UmrissZeichnung** wird angezeigt. Normalerweise werden dazu weitere Abschnitte an Bug und Heck hinzugefügt, wo komplexere Krümmungen registriert werden:

1.  Gehe zum Ende der Tabelle und *doppelklicke* auf ein leeres Element, um es zu bearbeiten.
2.  Drücke **intro** zur Bestätigung.
3.  Füge die folgenden Abschnitte hinzu:

:   

    :   X~22~ = -12.1125 m
    :   X~23~ = 12.1125 m

Je nach Komplexität der Rumpfgeometrie kann die Vorschau der Schnitte einige Zeit in Anspruch nehmen. Um einen Abschnitt zu entfernen, fülle ihn einfach mit einem leeren Text und drücke die Eingabetaste.

### Längsschnitte

Es müssen zwei Längsschnitte hinzugefügt werden, wähle also **Längsschnitte**, gehe in das Feld **Automatisch erstellen** und stelle **2** Abschnitte ein und drücke dann **Abschnitte erstellen**. Die Sektionstabelle wird gefüllt und die Sektionsvorschau aktualisiert.

### Wasserlinien

6 Wasserlinien zwischen Grundlinie und Konstruktionsentwurf müssen hinzugefügt werden, wähle also **Wasserlinien** Art der Abschnitte, gehe zum Feld **Automatisch erstellen\'\' und stelle**5\'\'\' ein (Z = 0 m wird nicht berücksichtigt, füge es manuell hinzu, wenn du es benötigst) Abschnitte, dann drücke **Abschnitte erstellen**. Die Schnitttabelle wird gefüllt und die Schnittvorschau aktualisiert.

Weitere zusätzliche Wasserlinien müssen hinzugefügt werden:

-   Z~6~ = 1.2 m
-   Z~7~ = 1.4 m
-   Z~8~ = 1.6 m
-   Z~9~ = 1.8 m
-   Z~10~ = 2.0 m

### Plot ausführen 

Wähle den Maßstab **1:100** und drücke **Annehmen**, damit das Werkzeug die 3D Schnitte in einem neuen Objekt erzeugt.

![Resultierende Schnitte.](images/FreeCAD-Ship-S60Outline3DSections.png )


<center>

Resultierende Schnitte.


</center>

Zum Plotten dieser Schnitte kann den Arbeitsbereich [TechDraw](TechDraw_Workbench.md) verwendet werden:

![Umrisszeichnungsplot.](images/FreeCAD-Ship-S60OutlinePlot.png )


<center>

Umrisszeichnungsplot.


</center>

## Transversale Flächen Kurve 

Ein typischer hydrodynamischer Parameter des Schiffsentwurfs ist die Kurve der transversalen Flächen, die einige Indikatoren über das Verhalten des Schiffsrumpfes (Schleppwiderstand, Seeverhalten, \...) liefert. Der Schiffs Arbeitsbereich stellt ein einfaches Werkzeug zur Verfügung, um die transversale Flächenkurve auszuführen.

![Transversalflächenkurve Symbol.](images/FreeCAD-Ship-AreaCurveIco.png )


<center>

Transversalflächenkurve Symbol.


</center>

Wenn das Werkzeug ausgeführt wird, wird ein Aufgabendialog angezeigt, und es wird eine Vorschau der freien Oberfläche in der [3D Ansicht](3D_view/de.md) erstellt (Die Vorschau der freien Oberfläche wird entfernt, wenn das Werkzeug fertig ist, also mache dir keine Sorgen darüber). Im Aufgabendialog sind Eingabe- und Ausgabedaten vorhanden.

### Eingabedaten

Tiefgang und Trimm (Drehwinkel Rumpf *y Kante*, positiv, wenn der Hecktiefgang zunehmen kann) müssen angegeben werden. Je nach Beladungssituation des Schiffes können mehrere Flächenkurven durchgeführt werden, es sollten jedoch zwei typische Darstellungen durchgeführt werden:

-   Kurve der Entwurfstransversalflächen: Ohne Trimmwinkel und mit Entwurfstiefgang, in diesem Fall 1,0 m.
-   Kurve der transversalen Flächen mit maximalem Tiefgang: Ohne Trimmwinkel und mit maximal zulässigem Tiefgang, in diesem Fall 2,0 m.

### Ausgabedaten

Einige relevante Daten werden in Echtzeit angezeigt:

-   **L**\': Länge zwischen den Loten, Wert bei der Erstellung der Schiffsinstanz festgelegt.
-   **B**\': Bei der Erstellung des Schiffes ausgewählter Balken.
-   **T**\': Tatsächlicher Tiefgang mittschiffs.
-   **Trimm**\': Trimmwinkel.
-   **T~AP~**\': Nach senkrechtem Tiefgang.
-   **T~FP~**\': Senkrechter Tiefgang vorwärts.
-   **Verdrängung**\': Schiffsverdrängung (Salzwasser berücksichtigt, durch 1,025 teilen, um das verdrängte Volumen zu kennen).
-   **XCB**\'\': Auftriebsmittelpunkt X Koordinate (relativ zum Mittschiffsabschnitt).

Wenn die **Annehmen** Schaltfläche gedrückt wird, wird ein Plot ausgeführt (je nach Komplexität der Geometrie kann dies einige Zeit dauern, du kannst den Fortschritt am Terminal sehen und die Arbeit durch Drücken von **Strg**+**C** stoppen). Wenn die Aufgabe beendet ist, erzeugt FreeCAD einen Plot (siehe [Plot-Arbeitsbereich-Dokumentation](Plot_Workbench/de.md)) und eine Kalkulationstabelle (siehe [Tabellenkalkulation Arbeitsbereich Dokumentation](Spreadsheet_Workbench/de.md)).

<img alt="Konstruktionsentwurf Transversalflächenkurve. " src=images/FreeCAD-Ship-s60Areas.png  style="width:800px;">


<center>

Konstruktionsentwurf Transversalflächenkurve. 


</center>

Du kannst die Kurve der maximalen Entwurfstransversalflächen durchführen, um die Unterschiede zu sehen (z.B. stellst du fest, dass die Flächenkurve jetzt durch die Längensenkrechten geht).

## Hydrostatik

Die Hydrostatik Berechnung ist eine kritische Phase beim Schiffsentwurf, da die wichtigsten Stabilitätsparameter des Schiffskörpers bekannt sind. Die Hydrostatik ist für die Ausstellung von Schiffszertifikaten durch die Klassifikationsgesellschaften obligatorisch und liefert zusammen mit den Daten über den Beladungszustand (Gewichte und Schwerkraftposition) wesentliche Daten über die Schiffsstabilität. FreeCAD-Schiff stellt ein Werkzeug zur Verfügung, um Haupt Hydrostatikkurven zu erhalten (GZ Kurven werden in anderen Werkzeugen berücksichtigt).

![Hydrostatik Werkzeugsymbol.](images/FreeCAD-Ship-HydrostaticsIco.png‎ )


<center>

Hydrostatik Werkzeugsymbol.


</center>

Wenn das Werkzeug ausgeführt wird, wird ein Aufgabendialog angezeigt. Gewöhnlich werden Hydrostatikkurven für jeden Trimmwinkel dargestellt, in diesem Tutorium wird nur der aufrechte Trimmwinkel (0º) berücksichtigt, mit einem Intervall um jeden Entwurf der Belastungsbedingung. Da wir nicht wissen, welche Belastungszustände wir erhalten können, werden wir fast alle Möglichkeiten des Tiefgangs in Betracht ziehen (Normalerweise, um so viele Auflösungen wie möglich zu erhalten, passen Schiffbauingenieure das Intervall an machbare Entwürfe an).

Also haben wir folgende Daten festgelegt:

-   **Trimm** = 0 Grad
-   **Minimaler Tiefgang** = 0,1 m
-   **Maximaler Tiefgang** = 2,0 m
-   **Anzahl der Punkte** = 39. Viele Punkte oder wirklich komplexe Geometrien implizieren lange Rechenzeiten, in diesem Fall kann etwa 1 Minute aufgewendet werden.

Wenn die **Annehmen**-Schaltfläche gedrückt wird, werden Plots durchgeführt (siehe [Plot-ArbeitsbereichDokumentation](Plot_Workbench/de.md)) und ein Kalkulationsblatt generiert (siehe [Tabellenkalkulation Arbeitsbereich Dokumentation](Spreadsheet_Workbench/de.md)).

<img alt="Hydrostatik Kurven." src=images/FreeCAD-Ship-HydrostaticsCurves.png  style="width:800px;">


<center>

Hydrostatik Kurven.


</center>



## Weiter lernen 

Das [FreeCAD Schiff s60 Tutorium (II)](FreeCAD-Ship_s60_tutorial_(II)/de.md) ist das zweite Kapitel der Series 60 von der Iowa Universität Schiff.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Ship](Category_Ship.md) > FreeCAD-Ship s60 tutorial/de
