# Manual:Using spreadsheets/de
{{Manual:TOC}}

Der Arbeitsbereich <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:16px;"> [Spreadsheet](Spreadsheet_Workbench/de.md) in FreeCAD ermöglicht Anwendern, [Kalkulationstabellen](https://de.wikipedia.org/wiki/Tabellenkalkulation) zu erstellen und zu verwalten, wie solche die mit [Excel](https://en.wikipedia.org/wiki/Microsoft_Excel) oder [Calc von LibreOffice](https://en.wikipedia.org/wiki/LibreOffice_Calc) erstellt werden, direkt in ihren Konstruktionsprojekten. Er ermöglicht die Eigabe, das Sortieren und den Umgang mit Daten in einem Tabellenformat, das dann mit verschiedenen Parametern und Modellen im Projekt verlinkt werden kann.

Einer der Hauptvorteile ist die Verwendung bei der parametrischen Modellierung. Kalkulationstabellen können mit den Abmessungen und Eigenschaften von 3D-Modellen verknüpft werden, was sie zu einem unverzichtbaren Werkzeug für dynamische Designänderungen macht. Wenn du beispielsweise einen Wert in der Tabellenkalkulation anpasst, wird die entsprechende Abmessung im Modell automatisch aktualisiert.

Neben der Verwaltung von Werten eignet sich der Arbeitsbereich hervorragend für die Datenverwaltung, da hier wichtige Informationen wie Materialeigenschaften, Abmessungen und projektweite Parameter gespeichert werden. Dies ist besonders bei komplexen Projekten nützlich, bei denen mehrere Werte referenziert oder angepasst werden müssen.

Kalkulationstabellen ermöglichen Benutzern auch die Eingabe von Formeln für Berechnungen und die Datenverwaltung. Diese Formeln können auf andere Tabellenzellen oder Parameter innerhalb des 3D-Modells verweisen, wodurch der gesamte Designprozess anpassbar und reaktionsfähig gegenüber Änderungen wird.

Er lässt sich nahtlos in andere FreeCAD-Arbeitsbereiche integrieren und ermöglicht die Interaktion zwischen Daten und Modellkomponenten. Diese Integration zentralisiert die Kontrolle über verschiedene Aspekte des Projekts und erleichtert so die Verwaltung. Die Benutzeroberfläche ist unkompliziert und ähnelt herkömmlicher Tabellenkalkulationssoftware, was sie für diejenigen, die bereits an Programme wie Excel oder LibreOffice Calc gewöhnt sind, vertraut und einfach zu verwenden macht.

In der Praxis ist der Arbeitsbereich Spreadsheet vielseitig für verschiedene Anwendungsfälle einsetzbar, darunter das Definieren projektweiter Parameter, das Verwalten von Stücklisten (BOM) und das Durchführen benutzerdefinierter Berechnungen, die Designentscheidungen beeinflussen. Er vereinfacht komplexe Projekte, indem er die Kontrolle der Parameter an einem Ort zusammenfasst.

Im folgenden Beispiel werden wir ein paar Objekte erstellen, einige ihrer Eigenschaften in eine Tabelle auslesen und die Tabelle zur direkten Steuerung der Parameter anderer Objekte einsetzen.



### Eigenschaften auslesen 

-   Wechsle zunächst zum Arbeitsbereich <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part](Part_Workbench/de.md) und erstelle einige Objekte: eine <img alt="" src=images/Part_Box.svg  style="width:16px;"> [Quader](Part_Box/de.md), einen <img alt="" src=images/Part_Cylinder.svg  style="width:16px;"> [Zylinder](Part_Cylinder/de.md) und eine <img alt="" src=images/Part_Sphere.svg  style="width:16px;"> [Kugel](Part_Sphere/de.md).
-   Bearbeite ihre Eigenschaft **Placement** (oder verwende das Werkzeug <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Draft Verschiieben](Draft_Move/de.md)), um sie etwas getrennt voneinander zu platzieren, damit wir die Auswirkungen unserer Vorgehensweise besser sehen können:

![](images/Exercise_spreadsheet_01.jpg )

-   Lassen uns nun einige Informationen zu diesen Objekten extrahieren. Wechsle zum Arbeitsbereich <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:16px;"> [Spreadsheet](Spreadsheet_Workbench/de.md)
-   Drücke die <img alt="" src=images/Spreadsheet_Create.svg  style="width:16px;"> Schaltfläche 
**Neues Arbeitsblatt**
-   Doppelklicke in der Baumansicht auf das neue Arbeitsblattobjekt. Der Arbeitsblatteditor wird geöffnet:

![](images/FreeCAD_Spreedsheet.png )

Obwohl der Tabellenkalkulationseditor von FreeCAD nicht so viele Funktionen bietet wie dedizierte Anwendungen wie Excel oder LibreOffice Calc, bietet er wichtige Werkzeuge für die meisten Designaufgaben. Benutzer können Zelleigenschaften wie Größe, Farbe und Ausrichtung anpassen und Zellen zur besseren Organisation zusammenführen oder teilen. Einfache Formeln oder Verweise auf andere Zellen werden unterstützt, was eine einfache Datenmanipulation ermöglicht. Was ihn auszeichnet, ist seine tiefe Integration in die Modellierungsumgebung von FreeCAD, wo Änderungen in der Tabelle die Modellabmessungen automatisch in Echtzeit aktualisieren können. Zwar fehlen ihm möglicherweise erweiterte Funktionen wie Pivot-Tabellen oder Diagramme, aber sein Fokus auf parametrisch gesteuertes Design macht ihn zu einem leistungsstarken Werkzeug für die Verwaltung von Designdaten direkt in FreeCAD.

In FreeCAD gibt es neben den Standardfunktionen einer Tabellenkalkulation eine besonders nützliche Funktion: die Möglichkeit, nicht nur auf andere Zellen, sondern auch auf Objekte innerhalb des Dokuments zu verweisen und Werte aus ihren Eigenschaften zu extrahieren. Du kannst beispielsweise Eigenschaften von 3D-Objekten abrufen, die auf der Registerkarte **Daten** des **Eigenschaften-Editors** sichtbar sind, wenn ein Objekt ausgewählt ist. Dies ermöglicht eine nahtlose Integration zwischen der Tabellenkalkulation und dem 3D-Modell, wodurch es einfach wird, Änderungen basierend auf den Parametern von Objekten innerhalb des Entwurfs zu verknüpfen und zu automatisieren, was einen dynamischeren und vernetzten Arbeitsablauf ermöglicht.

-   Beginnen wir damit, ein paar Texte in die Zellen A1, A2 und A3 einzugeben, damit wir uns später merken, was was ist, zum Beispiel **Würfellänge**, **Zylinderradius** und **Kugelradius**. Um Text einzugeben, schreibe einfach in das Feld „Inhalt" über der Tabelle oder doppelklicke auf eine Zelle.
-   Lass uns nun die tatsächliche Länge unseres Würfels abrufen. Gib in Zelle B1 **=Würfel.Länge** ein. Du wirst feststellen, dass die Tabelle über einen automatischen Vervollständigungsmechanismus verfügt, der eigentlich derselbe ist wie der Ausdruckseditor, den wir im vorherigen Kapitel verwendet haben.
-   Mache dasselbe für Zelle B2 (**=Zylinder.Radius**) und B3 (**=Kugel.Radius**).

![](images/FreeCAD_Spreedsheet_Autocomplete.png )

-   Obwohl diese Ergebnisse mit ihren Einheiten ausgedrückt werden, können die Werte als beliebige Zahlen bearbeitet werden. Gib beispielsweise in Zelle C1 Folgendes ein: **=B1\*2**.
-   Wir können jetzt einen dieser Werte im Eigenschafteneditor ändern und die Änderung wird sofort in der Tabelle angezeigt. Ändern wir beispielsweise die Länge unseres Würfels auf **20 mm**:

![](images/FreeCAD_Spreedsheet_Multipl.png )

Die Seite des Arbeitsbereichs <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:16px;"> [Spreadsheet](Spreadsheet_Workbench/de.md) beschreibt detailreich alle möglichen Arbeitsabläufe und Funktionen, die in Tabellen zur Verfügung stehen.



### Eigenschaften ausgeben 

Ein weiteres leistungsstarkes Feature des Arbeitsbereichs Spreadsheet in FreeCAD ist die Möglichkeit, Werte aus den Eigenschaften von 3D-Objekten nicht nur zu lesen, sondern ihnen auch Werte zuzuweisen. Dadurch können die Abmessungen und Attribute von Objekten direkt aus der Tabelle gesteuert werden. Eine der Grundregeln von FreeCAD ist jedoch, dass zirkuläre Abhängigkeiten verboten sind -- das heißt, eine Tabelle kann nicht gleichzeitig vom selben Objekt lesen und in dasselbe schreiben. Dies würde zu einer Situation führen, in der das Objekt von der Tabelle abhängt, während die Tabelle auch vom Objekt abhängt, was zu einer ungültigen Konfiguration führen würde. Um dies zu vermeiden, wird normalerweise eine zweite Tabelle erstellt, um das Schreiben von Werten zu handhaben und so eine klare Trennung zwischen den Lese- und Schreibvorgängen sicherzustellen.

-   Wir können jetzt die Registerkarte der Tabelle (unter der 3D-Ansicht) schließen. Dies ist nicht zwingend erforderlich, es ist kein Problem, mehrere Tabellenfenster geöffnet zu lassen.
-   Drücke erneut die Schaltfläche <img alt="" src=images/Spreadsheet_Create.svg  style="width:16px;"> 
**Neue Tabelle**
-   Ändere den Namen der neuen Tabelle in einen aussagekräftigeren Namen, z. B. **Eingabe** (klicke dazu mit der rechten Maustaste auf das neue Tabellenobjekt und wähle **Umbenennen**).
-   Doppelklicke auf die Eingabetabelle, um den Tabelleneditor zu öffnen.
-   Gib in Zelle A1 einen beschreibenden Text ein, z. B.: „Würfelabmessungen"
-   Schreibe in Zelle B1 **=5mm** (mit dem =-Zeichen wird sichergestellt, dass der Wert als Einheitswert und nicht als Text interpretiert wird).
-   Um diesen Wert nun außerhalb der Tabelle verwenden zu können, müssen wir der Zelle B1 einen Namen oder Alias ​​geben. Klicke mit der rechten Maustaste auf die Zelle, klicke auf **Eigenschaften** und wähle die Registerkarte **Alias**. Gib ihr einen Namen, z. B. **cubedims**:

![](images/FreeCAD_Spreedsheet_Alias.png )

-   Drücke **OK** und schließe dann die Registerkarte der Tabelle.
-   Wähle das Würfelobjekt aus.
-   Klicke im Eigenschafteneditor auf das kleine <img alt="" src=images/Bound-expression-unset.svg  style="width:16px;"> **Ausdrucks**-Symbol rechts neben dem Feld **Länge**. Dadurch wird der [Ausdruckseditor](Expressions/de.md) geöffnet, in den du **Spreadsheet001.cubedims** schreiben kannst. Wiederhole dies für **Höhe** und **Breite**:

![](images/FreeCAD_SpreedSheet_Dim.png )

Der Grund, warum wir im Ausdruck „Spreadsheet001" statt „Input" verwenden, ist, dass jedes Objekt in einem FreeCAD-Dokument einen eindeutigen internen Namen und eine benutzerfreundlichere Bezeichnung hat. Während die Bezeichnung in der Baumansicht angezeigt wird, wird der interne Name verwendet, um Objekte innerhalb des Dokuments eindeutig zu identifizieren. FreeCAD ermöglicht es dir, mehreren Objekten dieselbe Bezeichnung zuzuweisen, wenn du ihre Einstellungen anpasst, aber der interne Name bleibt eindeutig. Für alle Vorgänge, bei denen ein Objekt eindeutig identifiziert werden muss, verwendet FreeCAD den internen Namen statt der Bezeichnung, da sich die Bezeichnung auf mehr als ein Objekt beziehen könnte. Um den internen Namen eines Objekts zu finden, ist es sinnvoll, das Auswahlfenster (zugänglich über Ansicht → Fenster) geöffnet zu lassen. Dieses Fenster zeigt immer den internen Namen des ausgewählten Objekts an und stellt sicher, dass du in deinen Ausdrücken die richtige Referenz verwendest.

![](images/FreeCAD_SpreedSheet_SelectionView.png )

Durch die Verwendung von Zellaliasen im Arbeitsbereich Spreadsheet von FreeCAD ist es möglich, „Masterwerte" im Dokument zu speichern, wodurch die Verwaltung und Änderung wichtiger Parameter vereinfacht wird. Beispielsweise kann eine Kalkulationstabelle die Abmessungen eines Modells enthalten, sodass diese Werte im gesamten Entwurf referenziert werden können. Dieser Ansatz vereinfacht den Aktualisierungsprozess des Modells. Wenn neue Abmessungen erforderlich sind, kannst du einfach die Kalkulationstabelle öffnen, die Werte anpassen und das Modell wird automatisch aktualisiert, um diese Änderungen widerzuspiegeln. Diese Methode rationalisiert die Versionierung und verbessert die Effizienz, insbesondere bei der parametrischen Modellierung, bei der sich die Abmessungen häufig je nach Projektanforderungen ändern.

Beachte abschließend, dass die Randbedingungen innerhalb einer Skizze auch den Wert einer Tabellenzelle erhalten können:

Du kannst den maßlichen Randbedingungen (Horizontalen Abstand, Vertikalen Abstand oder Abstand festlegen) in einer Skizze auch Aliase zuweisen (Du kannst diese Werte dann auch außerhalb der Skizze verwenden):

![](images/FreeCAD_SpreedSheet_Rectangle.png )

**Herunterladen**

-   Die in dieser Übung erstellte Datei: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/spreadsheet.FCStd>

**Mehr lesen**

-   [Der Arbeitsbereich Tabellenkalkulation](Spreadsheet_Workbench/de.md)
-   [Ausdrücke anwenden](Expressions/de.md)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Using spreadsheets/de
