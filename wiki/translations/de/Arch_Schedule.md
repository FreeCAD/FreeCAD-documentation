---
 GuiCommand:
   Name: Arch Schedule
   Name: Arch Ablaufplan
   MenuLocation: Verwalten , Planung
   Workbenches: BIM_Workbench/de
   SeeAlso: 
---

# Arch Schedule/de



## Beschreibung

Das Werkzeug **ArchAblaufplan** ermöglicht ein [Tabellenblatt](Spreadsheet_Workbench/de.md) zu erstellen und automatisch mit Inhalten aus dem Modell zu befüllen.

Für eine allgemeinere Lösung siehe Arbeitsbereich [Reporting](https://github.com/furti/FreeCAD-Reporting/tree/master) in der Liste der [externen Arbeitsbereiche](External_workbenches/de.md). Dieser Arbeitsbereich verwendet die SQL-Syntax, um Informationen aus dem Dokument zu extrahieren.



## Anwendung

1.  Ein FreeCAD-Dokument öffnen oder erstellen, das einige Objekte enthält.

2.  Die Schaltfläche **<img src="images/Arch_Schedule.svg" width=16px> [Planung](Arch_Schedule/de.md)** drücken.

3.  Die gewünschten Optionen einstellen. Die Option **Tabelle verknüpfen** aktivieren, wenn der Ablaufplan eine FreeCAD-[Kalkulationstabelle](Spreadsheet_Workbench/de.md) erstellen soll. Oder alternativ den Ablaufplan nach der Erstellung in der [Baumansicht](Tree_view/de.md) mit der rechten Maustaste anklicken und **Kalkulationstabelle anhängen** im Kontextmenü auswählen.

4.  
    **OK**drücken.



## Arbeitsablauf

Zuerst muss ein Modell vorhanden sein. Hier ist zum Beispiel ein Dokument mit einigen Arch-Objekten, aber andere Objekte werden auch unterstützt.

![](images/Arch_schedule_example01.jpg )

Wird die Schaltfläche **<img src="images/Arch_Schedule.svg" width=16px> [Planung](Arch_Schedule/de.md)** gedrückt, öffnet sich dieser Dialog:

![](images/ArchSchedule.png )

Nun kann der Plan Zeile für Zeile gefüllt werden. Jede Zeile ist eine \"Abfrage\" und ergibt eine Zeile auf dem Tabellenblatt. Die Schaltfläche **<img src="images/List-add.svg" width=16px> Zeile hinzufügen** drücken, um eine Zeile hinzuzufügen; danach jede Zelle der Zeile doppelt anklicken, um die Werte einzugeben. Die Schaltfläche **<img src="images/List-remove.svg" width=16px> Zeile löschen** löscht die Zeile, die eine aktuell ausgewählte Zelle enthält und **<img src="images/Delete.svg" width=16px> Löschen** entfernt alle Zeilen. Mögliche Werte zum füllen der Spalten sind:

-   **Beschreibung**: Eine Beschreibung dieser Abfrage. Die Spalte Beschreibung wird die erste Spalte des resultierenden Tabellenblatts sein. Die Beschreibung ist verpflichtend für die Ausführung einer Abfrage. Wenn die Zelle Beschreibung leer ist, wird die komplette Zeile übersprungen und im Kalkulationsblatt nicht ausgefüllt. Dies erlaubt es, Trennzeilen hinzuzufügen.
-   **Eigenschaft**: Dies ist die echte Abfrage, die auf alle von der Abfrage ausgewählten Objekte ausgeführt werden soll. Es kann zwei Dinge enthalten: entweder das Wort `count` oder eine Objekteigenschaft:
    -   Wird `count` (oder `Count` oder `COUNT`, Groß-/Kleinschreibung wird ignoriert) eingegeben, werden die ausgewählten Objekte einfach nur gezählt.
    -   Wird eine Objekteigenschaft eingegeben, dann wird der Wert dieser Eigenschaft für jedes der ausgewählten Objekte ermittelt und aufsummiert. Objekte ohne diese Eigenschaft werden übersprungen. Im Allgemeinen ist es der Name der Eigenschaft, der im [Eigenschafteneditor](Property_editor/de.md) angezeigt wird, ohne Leerzeichen (z.B. tippt man `PerimeterLength` in der Spalte Eigenschaft ein, wenn der Eigenschafteneditor die Eigenschaft `Perimeter Length` für das Objekt anzeigt). Mit Punktnotation wird auf Eigenschaften von Eigenschaften zugegriffen: `EigenschaftDesObjekts.EigenschaftDerEigenschaft1.EigenschaftDerEigenschaft2`. Falls die Eigenschaft vor dem ersten Punkt mit einem Kleinbuchstaben beginnt, wird sie als Referenz auf das Objekt selbst angesehen und ignoriert. Bspw. ist `object.Shape.Volume` das Gleiche wie `Shape.Volume`.
-   **Einheit**: Eine optionale Einheit für das Ergebnis. Es liegt an dir, eine Einheit anzugeben, die zum Ergebnis passt. Wenn du z.B. Volumen ermittelst, solltest du eine Volumeneinheit angeben, wie `m^3` oder `m³`. Wird eine unpassende Einheit für die Eigenschaft verwendet, z.B. `cm` für ein Volumen, erhält man ein falsche Ergebnisse.
-   **Objekte**: Du kannst diese Spalte leer lassen, dann werden alle Objekte des Dokuments berücksichtigt oder eine durch `;` getrennte Liste von Objektnamen angeben. Wenn eines der Objekte in dieser Liste eine Gruppe ist, werden auch die Kinder ausgewählt. Daher ist der einfachste Weg, diese Möglichkeit zu nutzen, die Objekte sinnvoll zu gruppieren und hier einen Gruppennamen anzugeben. Du kannst auch die Schaltfläche **<img src="images/Edit-select-all.svg" width=16px> Auswahl hinzufügen** benutzen, um gerade im Dokument ausgewählte Objekte hinzuzufügen. Hier müssen die internen Namen verwendet werden. Um Objekte über ihre Benennungen (Labels) auszuwählen, wird diese Spalte leer gelassen und stattdessen die Spalte Filter verwendet.
-   **Filter**: Hier kannst du eine durch `;` getrennte Liste von Filtern angeben. Jeder Filter hat die Form `property:value`. Du kannst nur Eigenschaften verwenden, die als Wert eine Zeichenfolge enthalten. Sowohl bei `property` (Eigenschaft) als auch bei `value` (Wert) wird Groß-/Kleinschreibung ignoriert. `value` kann entfallen, nicht aber `:`. Um mit älteren Versionen von Arch Zeitplan erstellte Pläne korrekt zu behandeln, wird die `type`-Eigenschaft in die `ifctype`-Eigenschaft konvertiert. Es ist ratsam, nicht mehr `type` in neuen Zeitplänen zu benutzen.

+++
| Abfrage                                | Beschreibung                                                                                                                                                                                                                                                                                                                         |
+========================================+======================================================================================================================================================================================================================================================================================================================================+
|                         | Behält nur Objekte, die \"floor1\" in ihrer {{PropertyData/de|Label}} und \"window\" in ihrer {{PropertyData/de|IFC Type}} enthalten. Ein Fenster mit der {{PropertyData/de|Label}} \"Floor1-AA\" und der {{PropertyData/de|IFC Type}} \"Window Standard Case\" gehört dazu. |
| `label:floor1;ifctype:window` |                                                                                                                                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                                                                                                                                      |
+++
|                         | Behält nur Objekte, die \"door\" in ihrer {{PropertyData/de|Label}} enthalten                                                                                                                                                                                                                                          |
| `label:door`                  |                                                                                                                                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                                                                                                                                      |
+++
|                         | Behält nur Objekte, die \"door\" nicht in ihrer {{PropertyData/de|Label}} enthalten                                                                                                                                                                                                                                    |
| `!label:door`                 |                                                                                                                                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                                                                                                                                      |
+++
|                         | Behält nur Objekte, die \"structural\" in ihrer {{PropertyData/de|IFC Type}} enthalten                                                                                                                                                                                                                                 |
| `ifctype:structural`          |                                                                                                                                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                                                                                                                                      |
+++
|                         | Behält nur Objekte, die \"structural\" in ihrer {{PropertyData/de|IFC Type}} enthalten oder die die {{PropertyData/de|IFC Type}} nicht besitzen                                                                                                                                                          |
| `!ifctype:something`          |                                                                                                                                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                                                                                                                                      |
+++
|                         | Behält nur Objekte, die keine {{PropertyData/de|IFC Type}} besitzen                                                                                                                                                                                                                                                    |
| `!ifctype:`                   |                                                                                                                                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                                                                                                                                      |
+++

: Beispiele für Filter-Abfragen

Die Schaltfläche **<img src="images/Document-open.svg" width=16px> Importieren** ermöglicht, diese Liste in einer anderen Tabellenkalkulation zu erstellen und hier als csv-Datei zu importieren.

Der fertiggestellte Plan könnte so aussehen:

![](images/ArchScheduleExample.png )

Schließlich die Schaltfläche **OK** drücken und ein neuer Plan wird zum Dokument hinzugefügt. Wurde die zugehörige Option ausgewählt, enthält der Plan ein verknüpftes Tabellenblatt.

![](images/Arch_schedule_example04.jpg )

Um einen vorhandenen Plan zu bearbeiten, wird dieser in der Baumansicht doppelt angeklickt. Mit einem Doppelklick auf das Tabellenblatt erhält man die Ergebnisse in 3 Spalten: Beschreibung (Description), Wert (Value), Einheit (Unit)(falls zutreffend):

![](images/Arch_schedule_example05.jpg )

Das Tabellenblatt kann dann ganz normal vom Arbeitsbereich [Spreadsheet](Spreadsheet_Workbench/de.md) aus in eine csv-Datei exportiert werden.



## Dynamische Eigenschaften 

Es ist möglich, eigene Eigenschaften zu Objekten hinzuzufügen. Diese werden [Dynamische Eigenschaften](Property_editor/de#Maßnahmen.md) genannt. Falls sie mit der Option **Prefix group name** ausgewählt wurden, beginnen ihre Namen tatsächlich mit dem Gruppennamen, aber dieser Präfix wird nicht im [Eigenschafteneditor](Property_editor/de.md) angezeigt. Ihre Namen haben die Form: `NameOfGroup_NameOfProperty`. Um sie in einem Plan zu referenzieren muss dieser vollständige Name verwendet werden.





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Schedule/de
