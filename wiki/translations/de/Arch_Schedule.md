---
 GuiCommand:
   Name: Arch Schedule
   Name/de: Arch Ablaufplan
   MenuLocation: Arch , Ablaufplan
   Workbenches: Arch_Workbench/de
   SeeAlso: Arch_Equipment/de
---

# Arch Schedule/de

## Beschreibung

Das Ablaufplan Werkzeug erlaubt dir ein [Tabellenblatt](Spreadsheet_Workbench/de.md) zu erstellen und automatisch mit Inhalten aus dem Modell zu befüllen.


**Hinweis**

: Dieses Werkzeug wurde in FreeCAD 0.17 neu geschrieben und unterscheidet sich von früheren Versionen.

Für eine allgemeinere Lösung siehe den [Auswertung Arbeitsbereich](https://github.com/furti/FreeCAD-Reporting/tree/master) in der Liste der [Externe Arbeitsbereiche](External_workbenches/de.md). Dieser Arbeitsbereich verwendet die SQL-Syntax, um Informationen aus dem Dokument zu extrahieren.

## Anwendung

1.  Öffne oder erstelle ein FreeCAD Dokument, das einige Objekte enthält.
2.  Drücke die **<img src="images/Arch_Schedule.svg" width=16px> [Ablaufplan](Arch_Schedule/de.md)** Schaltfläche.
3.  Stelle die gewünschten Optionen ein.
4.  Drücken **OK**.

## Arbeitsablauf

Zuerst musst du ein Modell haben. Hier ist zum Beispiel ein Dokument mit einigen Arch-Objekten, aber andere Objekte werden auch unterstützt.

![](images/Arch_schedule_example01.jpg )

Dann drücke die **<img src="images/Arch_Schedule.svg" width=16px> [Arch Ablaufplan](Arch_Schedule/de.md)**-Schaltfläche. Du bekommst ein Aufgaben-Paneel wie dieses. Es ist ziemlich breit, so dass du das Aufgabenfenster verbreitern musst, um komfortabler zu sein.

![](images/Arch_schedule_example02.jpg )

Dann kannst du Zeile für Zeile füllen. Jede Zeile ist eine \"Abfrage\" und wird eine Zeile im Kalkulationsblatt rendern. Drücke die **Zeile hinzufügen**-Schaltfläche, um eine Zeile hinzuzufügen und doppelklicke jede Zelle dieser Zeile, um die Werte einzutragen. Die **Zeile löschen**-Schaltfläche wird die Zeile löschen, die eine gerade ausgewählte Zelle enthält und **Löschen** wird alle Zeilen löschen. Mögliche einzutragende Werte sind:

-   **Beschreibung**: Eine Beschreibung dieser Abfrage. Die Beschreibung-Spalte wird die erste Spalte des Ergebniskalulationsblatts sein. Die Beschreibung ist verpflichtend für die Ausführung einer Abfrage. Wenn die Beschreibung-Zelle leer ist, wird die komplette Zeile übersprungen und im Kalkulationsblatt nicht ausgefüllt. Dies erlaubt es, \"Separator\"-Zeilen hinzuzufügen.
-   **Eigenschaft**: Dies ist die echte Abfrage, die auf alle von der Abfrage ausgewählten Objekte ausgeführt werden soll. Es können zwei Dinge sein: entweder das Wort `count` oder eine Objekteigenschaft:
    -   Wenn du `count` (oder `Count` oder `COUNT`, Groß-/Kleinschreibung wird ignoriert) eingibst, werden die ausgewählten Objekte einfach nur gezählt.
    -   Wenn du eine Objekteigenschaft eingibst, dann werden die Werte dieser Eigenschaft ermittelt und addiert. Objekte ohne diese Eigenschaft werden übersprungen. Verwende die Punktnotation, um Eigenschaften von Eigenschaften zu ermitteln: `PropertyOfObject.PropertyOfProperty1.PropertyOfProperty2`. Falls die Eigenschaft vor dem ersten Punkt mit einem Kleinbuchstaben beginnt, wird sie als Referenz auf das Objekt selbst angesehen und ignoriert. Bspw. ist `object.Shape.Volume` das Gleiche wie `Shape.Volume`.
-   **Einheit**: Eine optionale Einheit für das Ergebnis. Es liegt an dir, eine Einheit anzugeben, die zum Ergebnis passt. Wenn du z.B. Volumen ermittelst, solltest du eine Volumeneinheit angeben, wie `m^3`. Wenn du eine falsche Einheit wie z.B. cm, wirst du falsche Ergebnisse bekommen.
-   **Objekte**: Du kannst diese Spalte leer lassen, dann werden alle Objekte des Dokuments berücksichtigt oder eine `;`-separierte Liste von Objektnamen (nicht Label). Wenn eines der Objekte in dieser Liste eine Gruppe ist, werden auch die Kinder ausgewählt. Daher ist der einfachste Weg, diese Möglichkeit zu nutzen, die Objekte sinnvoll zu gruppieren und hier einen Gruppennamen anzugeben. Du kannst auch die **Auswahl**-Schaltfläche benutzen, um gerade im Dokument ausgewählte Objekte hinzuzufügen.
-   **Filter**: Hier kannst du eine `;`-separierte Liste von Filtern angeben. Jeder Filter hat die Form `property:value`. Du kannst nur Eigenschaften verwenden, die als Wert eine Zeichenfolge enthalten. Sowohl bei `property` (Eigenschaft) als auch bei `value` (Wert) wird Groß-/Kleinschreibung ignoriert. `value` kann entfallen, nicht aber `:`. Um mit älteren Versionen von Arch Zeitplan erstellte Pläne korrekt zu behandeln, wird die `type`-Eigenschaft in die `ifctype`-Eigenschaft konvertiert. Es ist ratsam, nicht mehr `type` in neuen Zeitplänen zu benutzen.

:   Beispiele:

    :   
        `label:floor1;ifctype:window`
        
        wird nur Objekte beibehalten, die \"floor1\" in ihrer {{PropertyData/de|Label}}- und \"window\" in {{PropertyData/de|IFC Type}}-Eigenschaft haben. Ein Fenster mit der {{PropertyData/de|Label}}-Eigenschaft \"Floor1-AA\" und dem {{PropertyData/de|IFC Type}} \"Window Standard Case\" werden eingeschlossen.

    :   
        `label:door`
        
        Wird nur Objekte mit \"door\" in ihrer {{PropertyData/de|Label}}-Eigenschaft beibehalten.

    :   
        `!label:door`
        
        Wird nur Objekte beibehalten, die nicht \"door\" in ihrer {{PropertyData/de|Label}}-Eigenschaft haben.

    :   
        `ifctype:structural`
        
        Wird nur Objekte beibehalten, die \"structural\" in ihrer {{PropertyData/de|IFC Type}}-Eigenschaft haben.

    :   
        `!ifctype:something`
        
        Wird nur Objekte beibehalten, die nicht \"structural\" in ihrer {{PropertyData/de|IFC Type}}-Eigenschaft oder nicht die {{PropertyData/de|IFC Type}}-Eigenschaft haben.

    :   
        `!ifctype:`
        
        Wird nur Objekte beibehalten, die nicht die {{PropertyData/de|IFC Type}}-Eigenschaft haben.

Der **Import** erlaubt es dir, die in einer anderen Tabellenkalkulation erstellte Liste als csv-Datei zu importieren.

So können wir eine Liste mit Abfragen erstellen:

![](images/Arch_schedule_example03.jpg )

Danach drücke **OK** und ein neues Schedule-Objekt wird zum Dokument hinzugefügt, das ein Ergebnis-Kalkulationsblatt enthält.

![](images/Arch_schedule_example04.jpg )

Durch doppelklicken des Zeitplan-Objekt kommst du zurück zum Aufgaben-Panell und kannst die Werte ändern. Durch doppelklicken des Kalkulationsblatts selbst erhälst du die Werte in drei Spalten: Beschreibung, Wert, Einheit (falls zutreffend):

![](images/Arch_schedule_example05.jpg )

Die Kalkulationstabelle kann dann ganz normal von der Arbeitsbereich Tabellenkalkulations aus nach csv exportiert werden.

## Dynamische Eigenschaften 

Es ist möglich, eigene Eigenschaften zu Objekten hinzuzufügen. Diese werden [Dynamische Eigenschaften](Property_editor/de#Maßnahmen.md) genannt. Falls sie mit der **Prefix group name**-Option ausgewählt wurden, beginnen ihre Namen tatsächlich mit dem Gruppennamen, aber dieser Präfix wird nicht im [Eigenschafteneditor](Property_editor/de.md) angezeigt. Ihre Namen haben die Form: `NameOfGroup_NameOfProperty`. Um sie in einem Zeitplan zu referenzieren muss dieser vollständige Name verwendet werden.



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Schedule/de
