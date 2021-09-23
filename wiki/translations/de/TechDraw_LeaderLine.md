---
- GuiCommand:/de
   Name:TechDraw LeaderLine
   Name/de:TechDraw Führungslinie
   MenuLocation:TechDraw → Linien hinzufügen → Führungslinie zur Ansicht hinzufügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.19
   SeeAlso:[TechDraw Formatierte Text Anmerkung](TechDraw_RichTextAnnotation/de.md), [TechDraw Schweißsymbol](TechDraw_WeldSymbol/de.md), [TechDraw Liniengruppe](TechDraw_LineGroup/de.md)
---

# TechDraw LeaderLine/de

## Beschreibung

Das FührungsLinien Werkzeug fügt einer Ansicht eine Führungslinie hinzu. Andere Anmerkungsobjekte (wie z.B. [Formatierte Text Anmerkungen](TechDraw_RichTextAnnotation/de.md)) können mit der Führungslinie verbunden werden, um komplexe Anmerkungen zu bilden.

![](images/TechDraw_LeaderLine_sample.png ) *Führungslinie zur Ansicht View hinzugefügt*

## Anwendung

1.  Wähle eine Ansicht.
2.  Drücke die **<img src="images/TechDraw_LeaderLine.svg" width=16px> Führungslinie zur Ansicht hinzufügen** Schaltfläche. Es öffnet sich ein Dialog, in dem die Führungslinie gezeichnet und der Linie Endsymbole zugewiesen werden können.
3.  Klicke auf **Punkte greifen** und klicke dann in die Seite, um den Startpunkt der Linie festzulegen.
4.  Bewege die Maus und klicke auf einen anderen Punkt, um eine Linie zu erstellen.
5.  Jetzt kannst du entweder
    1.  beende die Linienzeichnung durch Doppelklicken oder Drücken von **|Punkte speichern**.
    2.  weitere Punkte hinzufügen, um weitere Liniensegmente festzulegen.
6.  Um die Erstellung abzuschließen, drücke **OK**, um das Dialogfeld zu schließen.

**Hinweis:** Wenn du bei der Erstellung der Führungslinie keine Punkte definiert hast, wird eine kurze Linie in der Mitte der Ansicht dargestellt.

### Bearbeitung

1.  Wähle die Führungslinie im Dokumentbaum und doppelklicke darauf.
2.  Ein Dialogfeld wird geöffnet, in dem du das Erscheinungsbild ändern kannst.
3.  Um die Punkte zu bearbeiten, klicke auf **Punkte bearbeiten**, und die einzelnen Linienpunkte werden in der Zeichnung sichtbar.
4.  Ziehe die Punkte an die gewünschte Stelle und schließe die Änderung durch Klicken auf **Änderungen speichern** ab.

## Eigenschaften

Markiere die gewünschte Führungslinie in der Baumansicht. Im unteren Teil der Combo-Box werden die Eigenschaften der Führungslinie innerhalb der beiden Reiter (Daten und Ansicht) angezeigt.

-   Start Symbol: Symbol am Anfang der Führungslinie.
-   End Symbol: Symbol am Ende der Führungslinie.
-   X,Y: Startpunkt der Führungslinie
-   Leader Parent: Die Ansicht, der die Führung angehängt ist.
-   Scalable: Führungslinie wird skaliert mit der verbundenen Ansicht.
-   Auto Horizontal: Bei \"True\" wird das Ende der Führungslinie als waagerechte Linie dargestellt.
-   Color: Farbe der Führungslinie.
-   Line Style: Durchgehend, Strich-Punkt usw. wählbar.
-   Line Width: Stärke der Führungslinie.

## Programmierung


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das FührungsLininen Werkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md) Konsole aus mit den folgenden Funktionen verwendet werden:


```python
myPage = FreeCAD.ActiveDocument().Page
myBase = FreeCAD.ActiveDocument().View
leaderObj = FreeCAD.ActiveDocument.addObject('TechDraw::DrawLeaderLine','DrawLeaderLine')
FreeCAD.activeDocument().myPage.addView(leaderObj)
FreeCAD.activeDocument().leaderObj.LeaderParent = myBase
#first waypoint is always (0,0,0)  
#rest of waypoints are positions relative to (0,0,0)
leaderObj.WayPoints = [p0,p1,p2]
leaderObj.X = 5
leaderObj.Y = 5
```

## Notes


<div class="mw-translate-fuzzy">

## Hinweise

-   Du kannst deine FührungsLinie bearbeiten, indem du in der Baumansicht darauf doppelklickst. Ein Doppelklick in den Grafikbereich wird noch nicht unterstützt. Die FührungsLinie kann durch Drücken von \"Punkte bearbeiten\" im Bearbeitungsmodus bearbeitet werden. Um die Punktbearbeitung zu beenden: drücke \"Änderungen speichern\" oder \"Änderungen verwerfen\".
-   Wenn kein Punkt als Anfangspunkt definiert wird, erscheint eine kurze Linie im Zentrum der Ansicht. Es können später keine Änderungen daran vorgenommen werden.
-   In den Eigenschaften ist **Führungslinie Auto Horizontal** in den Grundeinstellungen aktiviert. Das bedeutet, dass das Ende der Führungslinie horizontal dargestellt wird. Wenn nur eine Führungslinie ohne Knick erstellt wurde, erscheint diese horizontal. Es gibt keine Möglichkeit weitere Punkte der Führungslinie zu bearbeiten.
-   Für bestehende Führungslinien kann **Auto Horizontal** auf \"False\" gesetzt werden.


</div>





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LeaderLine/de
