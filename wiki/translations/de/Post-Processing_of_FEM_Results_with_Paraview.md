---
 TutorialInfo:e
   Topic: Nachbearbeitung von FEM-Ergebnissen mit ParaView
   Level:  Aufsteiger
   Time:  120 Minuten
   Author: http://www.freecadweb.org/wiki/index.php?title=User: HarryvL
   FCVersion: 0.19
   Files: https://forum.freecadweb.org/download/file.php?id=103403 Balken und https://forum.freecadweb.org/download/file.php?id=103557 Mauer gefunden in diesem https://forum.freecadweb.org/viewtopic.php?f=18&t=37253&start=10#p367734 FC Forumsbeitrag
---

# Post-Processing of FEM Results with Paraview/de







## Einführung

Einige Forenbeiträge und Tutorien verwenden Paraview (PV) zur Überprüfung und Analyse von Ergebnissen des FreeCAD-Arbeitsbereichs <img alt="" src=images/_Workbench_FEM.svg  style="width:24px;"> [FEM](FEM_Workbench/de.md). Dieses Tutorial erklärt die Grundlagen des Datentransfers vom Arbeitsbereich FEM zu PV und zeigt einige der Optionen und Einstellungen für die Anzeige von Daten.



## Voraussetzungen

-   FreeCAD verwendet eine Version, die mit der vorgesehenen Version dieses Tutorial kompatibel ist.
-   Paraview kann direkt von [paraview.org](https://www.paraview.org/download/)geladen oder über den Paketverwalter installiert werden.
-   Dieses Tutorial basiert auf der zum Zeitpunkt der Erstellung aktuellsten Version ParaView 5.8.0 für Windows.
-   Die für dieses Tutorial verwendeten FreeCAD Dateien sind in [diesem](https://forum.freecadweb.org/viewtopic.php?f=18&t=37253&start=10#p367734) und [diesem](https://forum.freecadweb.org/viewtopic.php?f=18&t=37253&p=368315#p368315) FC Forumsbeitrag verfügbar.
-   Das original in Englisch verfasste Tutorial wurde im September 2024 in das Deutsche übersetzt. Es wurde das zu dem Zeitraum aktuelle ParaView, Version 5.13.0, getestet und bekannt gewordene Veränderungen eingearbeitet.



## Datentransfer vom Arbeitsbereich FEM 

Im Arbeitsbereich FEM wird das Objekt CCX_Results hervorgehoben. Danach wird die Menüoption **Datei > Export > FEM Ergebnis VTK (*.vtk *.vtu)** ausgewählt, um die VTK-Daten zu exportieren.



## Datenimport in Paraview 

Der Startbildschirm zeigt einen leeren Pipeline-Browser. Hier werden die importierten VTK-Datenobjekte und die angewendeten Filterobjekte (für Geometrie oder Daten) aufgelistet.

<img alt="" src=images/PVPic1.png  style="width:500px;">

Verwende den Menüpunkt **File > Open > *.vtk**, um die VTK-Datei zu öffnen, die mit dem FEM Arbeitsbereich erzeugt wurde.

<img alt="" src=images/PVPic2.png  style="width:500px;">

Auf das Augensymbol neben dem Objekt im Piplinebrowser klicken um die Sichtbarkeit des Objekts an- bzw. auszuschalten.

Drücke **Apply** auf der Registerkarte Eigenschaften. Standardmäßig wird eine Draufsicht (Blick nach unten entlang der z-Achse) der Geometrie angezeigt.

<img alt="" src=images/PVPic3.png  style="width:400px;"> \... <img alt="" src=images/PVPic0.png  style="width:550px;">

Interaktion mit der 3D-Ansicht: Mit der linken Maustaste klicken und ziehen um zu drehen, mit der mittleren Maustaste, um zu verschieben, und mit dem Scrollrad oder der rechten Maustaste zum Zoomen. Bei Mäusen mit einer oder zwei Tasten halte man beim Klicken und Ziehen die Umschalt- oder Steuerungstasten gedrückt, um zu kippen, zu verschieben und zu zoomen. Hält man beim Drehen die **X**, **Y** oder **Z** Taste gedrückt dreht man um die jeweilige Achse.

Mit der Version 5.13 kann es zur Beeintächtigung der Mausnavigation kommen, wenn z.B. das Werkzeug \"Hover Points On\" aktiv ist, dieses evtl. ausschalten

<img alt="" src=images/PVPic5.png  style="width:500px;"> 

## Speicher/Ladezustand

Paraview speichert nicht die Daten, sondern den Status (Zustand) der Aktionen, die an dem importierten VTK-Objekt durchgeführt wurden. Um die Arbeit zu speichern, verwendet man daher den Menüpunkt **File > Save State**.

**HINWEIS**: es gibt keine Warnung, wenn man Paraview beendet, um den Status zu speichern, und alle Arbeit kann beim Verlassen des Programms verloren gehen.

Um dort fortzufahren, wo in der vorherigen Sitzung aufgehört wurde, verwendet man **File > Load State**. Dies fordert den Benutzer auf, eine VTK-Datei anzugeben, was bedeutet, dass die in der letzten Sitzung durchgeführten Aktionen auch auf eine neue VTK-Datei angewendet werden können. Auf diese Weise können Daten aus verschiedenen FEM-Workbench-Analysen ohne zusätzlichen Aufwand auf die gleiche Weise dargestellt werden.

Über **Help > Paraview Guide** gelangt man hier hin, <https://docs.paraview.org/en/v5.13.0/UsersGuide/savingResults.html>, und kann sich über die vielfältigen Möglichkeiten informieren.



## Ergebnisse des Arbeitsbereichs FEM visualisieren 

Paraview verfügt über zahlreiche Optionen und Einstellungen für die Anzeige von Ergebnissen. Wir werden uns zunächst die Anzeige von Basisimportdaten auf der ursprünglichen Geometrie ansehen und danach sehen, wie man Filter anwendet, um die Geometrie zu verändern. Schließlich werden wir den Rechner und die Integrationsfilter verwenden, um neue Ergebnisse durch die Kombination von Basisimportdaten zu erhalten.



## Auf Originalgeometrie angezeigte Basisdaten 

Da der Pipeline-Browser mehrere VTK-Objekte und Filterobjekte enthalten kann, vergewissere man sich zunächst, dass das richtige VTK-Objekt im Pipeline-Browser hervorgehoben ist. Die Auswahl und die Einstellungen für die Anzeige dieses VTK-Objekts findet man nun auf der Registerkarte Properties. Mit dem Zahnradsymbol kann man alle Einstellungen sichtbar machen.

<img alt="" src=images/PVPic6.png  style="width:400px;">

Die erste Einstellung, die wir ändern können, ist die Art und Weise, wie die Daten in der Geometrie dargestellt werden. Dies geschieht über das Dropdown-Menü \"Representation\". Im Moment werden wir nur die Option Surface oder Wirefram verwenden.

<img alt="" src=images/PVPic7.png  style="width:400px;">

Bislang werden keine Ergebnisse angezeigt. Hierfür müssen wir die Option Coloring ändern. Die Standardeinstellung ist \"Solid Color\", aber das Dropdown-Menü zeigt alle Skalardaten an, die in der importierten VTK-Datei verfügbar sind.

<img alt="" src=images/PVPic8.png  style="width:400px;">

<img alt="" src=images/PVPic9.png  style="width:400px;">

Für die Zwecke dieses Tutorials wählen wir \"ReinforcementRatio_x\", aber es ist einfach, jeden Datentyp zu verwenden.

Das RenderView-Fenster zeigt nun einen Iso-Plot des ausgewählten Datentyps und eine Farblegende des Datenbereichs.

<img alt="" src=images/PVPic10.png  style="width:700px;">

Die Farblegende kann auf dem Bildschirm an eine günstigere Position gezogen werden und ändert ihre Ausrichtung, wenn sie sich einem der Fensterränder nähert. Man kann auch die Enden greifen und sie skalieren.

<img alt="" src=images/PVPic11.png  style="width:700px;">

Über die acht abgebildete Buttons gelangt man zu sehr detailierten Einstellmöglichkeiten.

<img alt="" src=images/PVPic12.png  style="width:400px;">

Es öffnet sich z.B. das folgende Fenster für die Einstellungen der Farblegende.

<img alt="" src=images/PVPic13.png  style="width:400px;">

Die Farbgebung der Isokarte kann über den Farbkarten-Editor gesteuert werden, der durch Drücken der Edit-Schaltfläche auf der Registerkarte Eigenschaften aktiviert wird:

<img alt="" src=images/PVPic12.png  style="width:300px;"> . <img alt="" src=images/PVPic15.png  style="width:300px;">

Die Einstellung für die Farbdiskretisierung ist nützlich, um die Anzahl der Iso-Werte zu begrenzen und so praktischere Bereiche für die Gestaltung zu schaffen. Die Standardanzahl der Bereiche ist 256, aber hier ist die Anzahl auf 10 festgelegt.

<img alt="" src=images/PVPic16.png  style="width:700px;"> 

## Filter auf Ergebnisse des Arbeitsbereichs FEM anwenden 

Um die Basisdaten oder die aus dem Arbeitsbereich FEM importierte Geometrie zu verändern, können Filter angewendet werden.

Hier werden nur die Filter \"Slice\" und \"Warp\" behandelt. Filter zur Erstellung zusammengesetzter Ergebnisse aus Basisdaten werden im nächsten Abschnitt behandelt.

Um den Slice-Filter anzuwenden muss das VTK-Objekt ausgewält sein, das zerlegt werden soll, dann das Slice-Symbol klicken. Alternativ ist der Slice-Filter auch im Menü Filters \> Alphabetical zu finden. Dadurch wird das Slice-Filterobjekt dem Pipeline-Browser hinzugefügt und die Position im Baum zeigt, dass es auf das VTK-Objekt angewendet wird. Durch Klick auf das Augensymbol wird es dann auch sichtbar. Die Position in der Baumstruktur ist wichtig, weil Filter auf verschiedene VTK-Objekte angewendet werden können. Das Filterobjekt kann nicht in der Baumstruktur verschoben werden.

<img alt="" src=images/PVPic17.png  style="width:700px;">

Die Lage und Ausrichtung der Schicht kann durch Ziehen der Schicht und ihres Normalenvektors mit der Maus oder über die Registerkarte Eigenschaften geändert werden. In der folgenden Abbildung wurde der Ursprung der Scheibe in der Mitte des Balkens (über der zentralen Stütze) platziert und die Normale zur Ebene zeigt in die x-Richtung.

<img alt="" src=images/PVPic18.png  style="width:400px;">

Um die Begrenzungsrahmen loszuwerden ist das Kontrollkästchen \"Show Plane\" oben im Dialogfeld \"Plane Parameter\" zu deaktivieren.

<img alt="" src=images/PVPic19.png  style="width:700px;">

Der Filter \"Warp by Vector\" (Verformen nach Vektor) kann verwendet werden, um die deformierte Geometrie anzuzeigen. Das VTK-Objekt markieren und auf das Symbol \"Warp by Vektor\" klicken. Dadurch wird der Filter zum Pipeline-Browser hinzugefügt. Alternativ ist der Filter auch im Menü Filter \> Alphabetisch zu wählen. Im Dropdown-Menü Vektoren der Registerkarte \"Properties\" die Option \"Displacement\" wählen und einen geeigneten Skalierungsfaktor einstellen. Dann die Schaltfläche **Apply** klicken.

<img alt="" src=images/PVPic20.png  style="width:400px;"> . <img alt="" src=images/PVPic21.png  style="width:700px;">

Der Höchstwert der Verschiebung beträgt 0,98 mm.

Um die verformte Geometrie über die unverformte Geometrie zu legen, sind sowohl das VTK-Objekt als auch das Verformungsfilterobjekt sichtbar zu machen \-- mit dem Augensymbol. Im folgenden Bild wurde die Darstellung für das VTK-Objekt auf Drahtgitter geändert und die Deckkraft auf 0,5 reduziert, um zu verhindern, dass es die verformte Geometrie verdeckt.

<img alt="" src=images/PVPic22.png  style="width:700px;">

**HINWEIS**: Je mehr Objekte dem Pipeline-Browser hinzugefügt werden und je mehr Anzeigefenster geöffnet sind, desto wichtiger wird es, sicherzustellen, dass das richtige Objekt im Pipeline-Browser ausgewählt ist und das richtige Fenster den Fokus hat, wenn Änderungen vorgenommen werden. Andernfalls kann viel Zeit damit verbracht werden, die daraus resultierenden Fehler zu beheben.



## Anwenden von Filtern zur Ableitung von Verbund Ergebnissen aus Basis Importdaten 

Wenn wir die Menge an Bewehrungsstahl im Balken als Ganzes oder die Menge, die durch einen bestimmten Querschnitt geht, wissen wollen, müssen wir eine Integration (Summierung über die Geometrie) der Basisdaten durchführen.

So ergibt sich beispielsweise das Gesamtvolumen über die gesamte Geometrie der in x-Richtung verlaufenden Bewehrungsstäbe im Träger aus dem Integral `INTEGRATE(ReinforcementRatio_x * dx * dy * dz)`. Die Gesamtfläche des durch eine bestimmte Geometrie verlaufenden Bewehrungsstahls ergibt sich aus `INTEGRATE(ReinforcementRatio_x * dy * dz)` über einen Schnitt (Slice).

In Paraview kann die Integration mit einem Integrationsfilter durchgeführt werden. Dieser Filter kann auf das gesamte VTK-Objekt (den Balken) oder auf einen Schnitt angewendet werden.

HINWEIS: Aufgrund einer Nichtübereinstimmung der Knotenreihenfolge zwischen FCFEM und PV führt die Integration über ein Volumen zu negativen Ergebnissen, d. h. `INTEGRATE( 1.0 * dx * dy *dz)` = - Volumen anstelle von + Volumen. Mit FC 0.22 (38261) und PV 5.13 konnte dies aber nicht mehr beobachtet werden.

Um Integrale zu berechnen, müssen wir einen Integrationsfilter anwenden, der unter dem Menüpunkt Filters \> Alphabetical zu finden ist. Markiere das VTK-Objekt und wende den Filter \"Integrate Variables\" an.

<img alt="" src=images/PVPic23.png  style="width:700px;">

Drücke die Schaltfläche **Apply** auf der Registerkarte Eigenschaften und die Ergebnisse werden in einem separaten Fenster rechts neben der Renderansicht geöffnet.

<img alt="" src=images/PVPic24.png  style="width:700px;">

Bevor wir aufräumen, um das gewünschte Ergebnis zu erhalten, d.h. `INTEGRATE(ReinforcementRatio_x * dx * dy * dz)`, sehen wir uns zunächst an, wie die Anordnung von Fenstern erfolt.

Schließe zunächst das SpreadSheetView-Fenster, das sich auf der rechten Seite geöffnet hat. Drücke dann auf das horizontale Trennsymbol im Renderview-Fenster, woraufhin sich ein neues Fenster mit einem Menü von Anzeigeoptionen öffnet. Nun das Richtige auswählen - das Objekt Integrationsfilter im Pipeline-Browser muss markiert sein.

<img alt="" src=images/PVPic25.png  style="width:700px;">

Um numerische Ergebnisse anzuzeigen, müssen wir \"SpreadSheet View\" auswählen. Dies erzeugt eine Tabelle mit allen verfügbaren Ergebnissen im VTK-Objekt, das über das Volumen integriert ist.

<img alt="" src=images/PVPic26.png  style="width:400px;">

Um `INTEGRATE(ReinforcementRatio_x * dx * dy * dz)` zu prüfen, könnten wir nach rechts durch die Tabelle blättern, aber wir können auch alle unerwünschten Ergebnisse entfernen, indem wir sie abwählen, d. h. alle Spalten abwählen und **ReinforcementRatio_x** auswählen.

<img alt="" src=images/PVPic27.png  style="width:300px;"> . <img alt="" src=images/PVPic28.png  style="width:500px;">

Jetzt bleibt nur noch ein Wert in der Tabelle der Integrationsergebnisse übrig.

<img alt="" src=images/PVPic29.png  style="width:300px;">

Das indikative Gesamtvolumen des in x-Richtung erforderlichen Stahls beträgt also 2,27e+06 mm3 (= 2270 cm3) oder 2270 cm3 \* 7,6 g/cm3 = 17262 g (= 17,3 kg). In der Praxis wird die Zahl aufgrund praktischer Überlegungen (z. B. Verankerungsanforderungen, Mindestbewehrungsanforderungen usw.) höher sein. Dennoch kann dieses Ergebnis zum Vergleich von Entwürfen herangezogen werden.

Dies war ein Beispiel für die Integration einer Variable, die direkt vom FEM Arbeitsbereich exportiert wurde. In einigen Fällen möchten wir vielleicht VTK-Variablen kombinieren, um neue Ergebnisse zu erhalten. Dies kann auf verschiedene Arten geschehen, aber hier werde ich nur die einfachste besprechen, d.h. mit dem Calculator Filter.

Wenn wir zum Beispiel den gesamten Bewehrungsbedarf in allen drei Koordinatenrichtungen wissen wollen, müssen wir die Summe aus ReinforcementRatio_x, ReinforcementRatio_y und ReinforcementRatio_z bilden.

Der Rechnerfilter ist als Symbol links in der Filterleiste oder über das Menü Filters \> Alphabetical zu finden. Der Name für die resultierende Variable kann im Feld \"Result Array Name\" eingegeben werden. Hier nennen wir das Ergebnis \"Total_Reinforcement_Ratio\". Die Formel kann in der Box unter dem Feld Ergebnisfeldname zusammengestellt werden. Die Eingabewerte können aus dem Dropdown-Menü Skalare ausgewählt und mit den angegebenen Operatoren zu einer Formel für das Ergebnis zusammengesetzt werden. Nach Drücken der Schaltfläche Anwenden steht das Ergebnis als neue Variable in allen nachfolgenden Operationen (z. B. einem Integrationsfilter) oder Ansichten (z. B. RenderView oder SpreadSheetView, siehe unten) zur Verfügung.

<img alt="" src=images/PVPic30.png  style="width:700px;">

Zum Beispiel können wir nun den Integrationsfilter auf die neue Variable Total Reinforcement Ratio anwenden

<img alt="" src=images/PVPic31.png  style="width:700px;">

Dies zeigt, wie sich der Gesamtbewehrungsbedarf im Vergleich zu den einzelnen Koordinatenrichtungen darstellt.



## Integration über einen Schnitt 

Im vorigen Abschnitt haben wir den Integrationsfilter und seine Anwendung auf das gesamte VTK-Objekt besprochen. Um die Integration über einen Schnitt (Slice) zu demonstrieren, werden wir in diesem Abschnitt den Gesamtbewehrungsbedarf und seinen Schwerpunkt für den mittleren Querschnitt des Trägers bestimmen. Das Ergebnis ist in der Abbildung unten dargestellt. Die Interaktion der verschiedenen Objekte kann im Pipeline Browser überprüft werden. Der Slice-Filter wird auf das Balken-VTK-Objekt angewendet und zwei Calculator-Filter werden auf den Slice-Filter angewendet, um die neuen Variablen \"Reinforcement_ratio_x \* y\" und \"Reinforcement_ratio_x \* z\" aus den Basisdaten zu errechnen. Um den Schwerpunkt der Bewehrung bestimmen zu können müssen diese Variablen erst noch integriert werden, dazu werden Integrationsfilter auf jeden Calculator angewendet. Eine allgemeine Einführung in den Integrationsfilter und seine Einstellungen ist im vorherigen Abschnitt zu finden.

<img alt="" src=images/PVPicSlice1.png  style="width:700px;">

Folgende Einstellungen sind auf der Registerkarte Eigenschaften für das VTK-Objekt anzuwenden:

  Properties Tab Settings          Comment
   
  Representation: Wireframe        Der Schnitt ist also sichtbar
  Coloring: ReinforcementRatio_x   Oder jede andere Farbe
  Styling \> Line Width: 2         Oder jede andere Einstellung, die ein ansprechendes Ergebnis liefert

<img alt="" src=images/PVPicSlice2.png  style="width:400px;">

Das VTK-Objekt ist zu markieren und ein Slice-Filter mit den folgenden Eigenschaften anzuwenden:

  Properties Tab Settings                        Comment
   
  Plane Parameters \> Show Plane: deselect       Die Begrenzungsrahmen entfernen
  Plane Parameters \> Origin: 4000 / 100 / 200   Lage des Mittelteils
  Plane Parameters \> Normal: 1 /0 /0            Normale der Slice-Punkte in x -Richtung
  Coloring: ReinforcementRatio_x                 Optional
  Styling \> Line Width: 2                       Oder jede andere Einstellung, die ein ansprechendes Ergebnis liefert

<img alt="" src=images/PVPicSlice3.png  style="width:400px;">

\'\'\'Einstellungen Calculator 1

Calculator 1 berechnet die neu in \"Result Array Name\" anzulegende Variable \"ReinforcementRatio_x \* y\". Im Feld für die Formel wird \"ReinforcementRatio_x \* coordsY\" eingegeben.

<img alt="" src=images/PVPicSlice4.png  style="width:400px;">

Nach dem Drücken von **Apply** steht eine neue Variable mit dem Namen \"ReinforcementRatio_x \* y\" zur Anzeige und Weiterverarbeitung zur Verfügung.

\'\'\'Einstellungen Calculator 2

Calculator 2 berechnet die neu in \"Result Array Name\" anzulegende Variable \"ReinforcementRatio_x \* z\". Im Feld für die Formel wird \"ReinforcementRatio_x \* coordsZ\" eingegeben.

<img alt="" src=images/PVPicSlice5.png  style="width:400px;">

Nach dem Drücken von **Apply** steht eine neue Variable mit dem Namen \"ReinforcementRatio_x \* z\" zur Anzeige und Weiterverarbeitung zur Verfügung.

Die soeben berechneten Werte \"ReinforcementRatio_x \* y\" und \"ReinforcementRatio_x \* z\" müssen integriert werden, um so die y- und z-Koordinate des Schwerpunkts der Bewehrung zu erhalten.

Dafür werden jeweil ein Integrationsfilter auf Calculator1 und einer auf Calculator2 angewendet. Beide werden in einem eigenen Fenster angezeigt, wobei SpreadSheetView ausgewählt ist. Wie man alle anderen Ergebnisse abwählt, wurde bereits erklärt.

<img alt="" src=images/PVPicSlice6.png  style="width:700px;">

Schließlich kann der Schwerpunkt aus den obigen Ergebnissen wie folgt berechnet werden:

CoG_y = 55744.2 / 556.277 = 100.2 mm (exact value: 100 mm)

CoG_z = 187144 / 556.277 = 336.4 mm (exact value: 5/6 \* 400 mm)



## Integration über eine Linie 

Zur Veranschaulichung der Visualisierung und Integration der Ergebnisse über eine Linie verwenden wir das 2D-Beispiel einer schweren Wand, wie es in [diesem FC Forum Beitrag](https://forum.freecadweb.org/viewtopic.php?f=18&t=33049) vorgestellt wurde. Die FreeCAD-Datei für dieses Beispiel kann unter [diesem FC Forum Beitrag](https://forum.freecadweb.org/viewtopic.php?f=18&t=37253&start=10#p367734) heruntergeladen werden. Die Herausforderung besteht darin, das Bewehrungsverhältnis über verschiedene vertikale Querschnitte zu visualisieren und die erforderliche Stahlfläche aus der Integration dieser Ergebnisse zu bestimmen.

Techniken, die in früheren Abschnitten dieses Tutorial eingeführt wurden, werden hier nicht wiederholt. Es ist auch wichtig, noch einmal darauf hinzuweisen, dass es, je mehr Objekte dem Pipeline-Browser hinzugefügt werden und je mehr Anzeigefenster geöffnet sind, immer wichtiger wird, sicherzustellen, dass das richtige Objekt im Pipeline-Browser ausgewählt ist und das richtige Fenster den Fokus hat, wenn Änderungen auf der Registerkarte Eigenschaften vorgenommen werden. Andernfalls kann viel Zeit damit verbracht werden, die Fehler zu beheben.

Beginnen wir mit dem aus FEM Workbench importierten VTK-Objekt und stellen fest, dass die PV-Steuerung bei einem zweidimensionalen Objekt etwas anders funktioniert. Mit der linken Maustaste wird die Geometrie bewegt und mit der mittleren Maustaste gedreht. Um die Geometrie in der Analyseebene (d.h. x-y) zu positionieren, ist das Symbol, das die Ansicht entlang der negativen z-Achse verschiebt zu klicken

<img alt="" src=images/PVPicLine1.png  style="width:75px;">

Für das folgende Bild wurde die Eigenschaft Coloring auf der Registerkarte Properties für das VTK-Objekt auf ReinforcementRatio_x gesetzt.

Das einzige zusätzliche Objekt, das benötigt wird, um eine Variable entlang einer geraden Linie zu visualisieren, ist ein Filter \"Plot Over Line\". Dieser kann über die Symbolleiste oder den Menüpunkt Filters \> Alphabetical aktiviert werden.

Als nächstes wollen wir die horizontalen Bewehrungsanforderungen im vertikalen Querschnitt unter der Stütze anzeigen. Um dies auf die unten gezeigte Weise zu erreichen, müssen die folgenden Einstellungen auf der Registerkarte Eigenschaften des Filters \"Plot Over Line\" geändert werden (sowohl das Fenster LineChartView als auch das Objekt Plot Over Line muss den Fokus haben)

  Properties Tab Settings                                                Comment
   
  Line Parameters \> Point 1: 4000 / 0 / 0                               Punkt an der Unterseite der Wand unter der Säule
  Line Parameters \> Point 2: 4000 / 4000 / 0                            Punkt an der Oberseite der Wand unter der Säule
  x Axis Parameters \> x Array Name: ReinforcementRatio_x                Zeigt ReinforcementRatio_x auf der horizontalen Achse an
  Series Parameters: tick "arc length" only                              Dies ist der Längenparameter entlang der Linie
  Title \> Chart Title: Mid Section                                      
  Annotation \> Show Legend: deselect                                    Für die derzeitige Wahl der vertikalen Achse bedeutungslos
  Left Axis \> Left Axis Title: Height Across Beam                       
  Left Axis Range \> Use Custom Range: deselect                          Aufheben der Auswahl, um den Datenbereich entlang der Achse zu maximieren
  Bottom Axis \> Bottom Axis Title: Reinforcement Ratio in x-Direction   
  Bottom Axis Range \> Use Custom Range: deselect                        Aufheben der Auswahl, um den Datenbereich entlang der Achse zu maximieren

<img alt="" src=images/PVPicLine2.png  style="width:700px;">

Beachte, dass der Abstand entlang der Linie (Bogenlänge) normalerweise auf der horizontalen Achse liegt und die Variable, die wir anzeigen wollen (hier ReinforcementRatio_x) auf der vertikalen Achse. Da der Wandquerschnitt in diesem Beispiel jedoch vertikal ist und wir den Bewehrungsbedarf über die Höhe der Wand sehen wollen, ist es natürlicher, die Achsen zu vertauschen. Dies geht jedoch auf Kosten einer Vielzahl von Änderungen an den Einstellungen auf der Registerkarte Eigenschaften für den Filter \"Plot Over Line\".

In den nächsten beiden Abbildungen wurde nur die Position der Linie geändert. Diese Verschiebung ändert automatisch die Einstellung \"Left Axis Range \> Use Custom Range\" auf \"select\". Dies kann dazu führen, dass das Diagramm nicht mehr richtig in das LineChartView-Fenster passt. Es ist daher notwendig, diese Option jedes Mal zu deaktivieren, wenn die Position der Linie geändert wird. Die anderen Einstellungen entsprechen der obigen Tabelle.

  Properties Tab Settings                           Comment
   
  Line Parameters \> Point 1: 6700 / 0 / 0          Punkt an der Unterseite der Wand unter der linken Seite des Ausschnitts
  Line Parameters \> Point 2: 6700 / 4000 / 0       Punkt an der Oberkante der Wand über der linken Seite des Ausschnitts
  Title \> Chart Title: Section left of Cut-out     
  Left Axis Range \> Use Custom Range: deselect     Aufheben der Auswahl, um den Datenbereich entlang der Achse zu maximieren
  Bottom Axis Range \> Use Custom Range: deselect   Aufheben der Auswahl, um den Datenbereich entlang der Achse zu maximieren

<img alt="" src=images/PVPicLine3.png  style="width:700px;">

  Properties Tab Settings                           Comment
   
  Line Parameters \> Point 1: 10950 / 0 / 0         Punkt an der Unterseite der Wand an der rechten Stütze
  Line Parameters \> Point 2: 10950 / 4000 / 0      Punkt an der Oberkante der Wand an der rechten Stütze
  Title \> Chart Title: Section at Support          
  Left Axis Range \> Use Custom Range: deselect     Aufheben der Auswahl, um den Datenbereich entlang der Achse zu maximieren
  Bottom Axis Range \> Use Custom Range: deselect   Aufheben der Auswahl, um den Datenbereich entlang der Achse zu maximieren

<img alt="" src=images/PVPicLine4.png  style="width:700px;">

Der gesamte horizontale Bewehrungsbedarf im letzten Querschnitt kann nun einfach durch Anwendung eines Integrationsfilters auf das Objekt \"Plot Over Line\" ermittelt werden. Das Objekt \"Plot Over Line\" im Pipeline Browser ist dafür zu markieren und einen Integrationsfilter über die Menüoption Filters \> Alphabetical hinzufügen.

<img alt="" src=images/PVPicLine5.png  style="width:700px;">

Hebe wie üblich in der SpreadSheetView alle Markierungen außer dem Ergebnis ReinforcementRatio_x auf und lies das Ergebnis als 23,11 mm2 / mm ab. Um die Gesamtquerschnittsfläche des Stahls zu erhalten, müssen wir noch mit der Dicke der Wand multiplizieren, die in diesem Beispiel (beeindruckende) 600 mm beträgt. Die Gesamtquerschnittsfläche des Stahls, die durch den Querschnitt in der Nähe der rechten Stütze verläuft, beträgt also 23,11 \* 600 = 13866 mm2 = 139 cm2

Um eine praktikablere Verteilung der Bewehrung zu erreichen, könnten wir das obige Diagramm in Teilen integrieren. Wenn wir zum Beispiel die erforderliche Querschnittsfläche des Stahls in den oberen 400 mm der Wand wissen wollen, sollten wir die Eigenschaften des Objekts Plot Over Line wie folgt anpassen

  Properties Tab Settings                           Comment
   
  Line Parameters \> Point 1: 10950 / 0 / 0         Punkt an der Unterseite der Wand an der rechten Stütze
  Line Parameters \> Point 2: 10950 / 4000 / 0      Punkt an der Oberkante der Wand an der rechten Stütze
  Title \> Chart Title: Section at Support          
  Left Axis Range \> Use Custom Range: deselect     Aufheben der Auswahl, um den Datenbereich entlang der Achse zu maximieren
  Bottom Axis Range \> Use Custom Range: deselect   Aufheben der Auswahl, um den Datenbereich entlang der Achse zu maximieren

Dies führt zu folgendem Ergebnis:

<img alt="" src=images/PVPicLine6.png  style="width:700px;">

Das Ergebnis für die oberen 400 mm der Wand ist somit 8,436 mm2 / mm. Für die oberen 10% der Wand werden also 8,44 / 23,11 \* 100% = 37% des Bewehrungsstahls benötigt.

Dieses Verfahren kann wiederholt werden, um die Wand in Zonen mit konstanter Bewehrung zu unterteilen.



## Darstellung der Vektorergebnisse mit dem Glyphen 3D Filter 

Bisher haben wir uns nur mit skalaren Werten, wie Bewehrungsgrad und Verschiebungsgröße, beschäftigt. Die Visualisierung von Vektorergebnissen, wie Hauptspannungsvektoren, erfolgt mit Glyphen.

Kehren wir zum VTK-Datenobjekt für den Träger mit zentralem Auflager zurück und visualisieren wir die Vektoren der maximalen und minimalen Hauptspannung.

Markiere das VTK-Datenobjekt im Pipeline-Browser und wähle den Glyphenfilter aus der Filter-Symbolleiste oder aus der Menüoption Filter \> Alphabetical. Wende dann die folgenden Einstellungen auf der Registerkarte Eigenschaften des Glyphenfilterobjekts an (siehe Tabelle und Abbildung):

  Properties Tab Settings                              Comment
   
  Glyph Source \> Glyph Type: Line                     Leider gibt es keine Option für einen doppelseitigen Pfeil
  Orientation \> Orientation: Major Principal Stress   Die Glyphe nimmt die Hauptspannungsrichtung
  Scale \> Scale Array: Major Principal Stress         Die Länge der Linie gibt die Größe der Hauptspannung an
  Scale \> Vector Scale Mode: Scale by Magnitude       
  Scale \> Scale Factor: 100                           Oder jede andere Einstellung, die ein ansprechendes Ergebnis liefert
  Masking \> Glyph Mode: All Points                    So stelle sicher, dass die Spannung in jedem Knoten angezeigt wird
  Coloring \> Solid Color                              Eine einzige Farbe gibt größte Klarheit über den \"Stressfluss\"
  Coloring \> Edit \> Green                            Oder jede andere Einstellung, die ein ansprechendes Ergebnis liefert
  Styling \> Line Width \> 2                           Oder jede andere Einstellung, die ein ansprechendes Ergebnis liefert

<img alt="" src=images/PVPic32.png  style="width:400px;">; <img alt="" src=images/PVPic33.png  style="width:400px;">

Wenn alles gut geht ist das folgende Ergebnis sehen.

<img alt="" src=images/PVPic34.png  style="width:700px;">

Markiere das VTK-Datenobjekt im Pipeline-Browser und füge dann einen weiteren Glyphenfilter mit den folgenden Einstellungen für \"Minor Principal Stress\" hinzu.

  Properties Tab Settings                              Comment
   
  Glyph Source \> Glyph Type: Line                     Leider gibt es keine Option für einen doppelseitigen Pfeil
  Orientation \> Orientation: Minor Principal Stress   Die Glyphe zeigt die Hauptspannungsrichtung
  Scale \> Scale Array: Minor Principal Stress         Die Länge der Linie gibt die Größe der Hauptspannung an
  Scale \> Vector Scale Mode: Scale by Magnitude       
  Scale \> Scale Factor: 100                           Oder jede andere Einstellung, die ein ansprechendes Ergebnis liefert
  Masking \> Glyph Mode: All Points                    So stelle sicher, dass die Spannung in jedem Knoten angezeigt wird
  Coloring \> Solid Color                              Eine einzige Farbe gibt größte Klarheit über den \"Stressfluss"
  Coloring \> Edit \> Red                              Oder jede andere Einstellung, die ein ansprechendes Ergebnis liefert
  Styling \> Line Width \> 2                           Oder jede andere Einstellung, die ein ansprechendes Ergebnis liefert

<img alt="" src=images/PVPic35.png  style="width:700px;">

Das Endergebnis zeigt die Haupt- und Nebenspannungsvektoren, die dem Balken mit ReinforcementRatio_x überlagert sind.



## Export grafischer Ergebnisse 

Um ein RenderView-Fenster zu exportieren, markiere das Fenster und verwende die Menüoption **File > Save Screenshot**


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > Post-Processing of FEM Results with Paraview/de
