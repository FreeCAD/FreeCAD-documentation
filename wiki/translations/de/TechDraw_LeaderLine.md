---
- GuiCommand   */de
   Name   *TechDraw LeaderLine
   Name/de   *TechDraw Hinweislinie
   MenuLocation   *TechDraw → Linien hinzufügen → Hinweislinie zur Ansicht hinzufügen
   Workbenches   *[TechDraw](TechDraw_Workbench/de.md)
   Version   *0.19
   SeeAlso   *[TechDraw Formatierte Text Anmerkung](TechDraw_RichTextAnnotation/de.md), [TechDraw Schweißsymbol](TechDraw_WeldSymbol/de.md), [TechDraw Liniengruppe](TechDraw_LineGroup/de.md)
---

# TechDraw LeaderLine/de

## Beschreibung

Das Werkzeug Hinweislinie fügt einer Ansicht eine Hinweislinie hinzu. Andere Anmerkungsobjekte (wie z.B. [Formatierte Text Anmerkungen](TechDraw_RichTextAnnotation/de.md)) können mit der Hinweislinie verbunden werden, um komplexe Anmerkungen zu bilden.

![](images/TechDraw_LeaderLine_sample.png ) 
*Hinweislinie zur Ansicht View hinzugefügt*

## Anwendung

1.  Wähle eine Ansicht.
2.  Drücke die **<img src="images/TechDraw_LeaderLine.svg" width=16px> Hinweislinie zur Ansicht hinzufügen** Schaltfläche. Es öffnet sich ein Dialog, in dem die Hinweislinie gezeichnet und der Linie Endsymbole zugewiesen werden können.
3.  Klicke auf **Punkte greifen** und klicke dann in die Seite, um den Startpunkt der Linie festzulegen.
4.  Bewege die Maus und klicke auf einen anderen Punkt, um eine Linie zu erstellen.
5.  Jetzt kannst du entweder
    1.  beende die Linienzeichnung durch Doppelklicken oder Drücken von **|Punkte speichern**.
    2.  weitere Punkte hinzufügen, um weitere Liniensegmente festzulegen.
6.  Um die Erstellung abzuschließen, drücke **OK**, um das Dialogfeld zu schließen.

**Hinweis   *** Wenn du bei der Erstellung der Führungslinie keine Punkte definiert hast, wird eine kurze Linie in der Mitte der Ansicht dargestellt.

### Bearbeitung

1.  Wähle die Hinweislinie im Dokumentbaum und doppelklicke darauf.
2.  Ein Dialogfeld wird geöffnet, in dem du das Erscheinungsbild ändern kannst.
3.  Um die Punkte zu bearbeiten, klicke auf **Punkte bearbeiten**, und die einzelnen Linienpunkte werden in der Zeichnung sichtbar.
4.  Ziehe die Punkte an die gewünschte Stelle und schließe die Änderung durch Klicken auf **Änderungen speichern** ab.

## Eigenschaften

Markiere die gewünschte Hinweislinie in der Baumansicht. Im unteren Teil der Combo-Box werden die Eigenschaften der Hinweislinie innerhalb der beiden Reiter (Daten und Ansicht) angezeigt.

-   Start Symbol   * Symbol am Anfang der Hinweislinie.
-   End Symbol   * Symbol am Ende der Hinweislinie.
-   X,Y   * Startpunkt der Hinweislinie
-   Leader Parent   * Die Ansicht, der die Hinweislinie angehängt ist.
-   Scalable   * Hinweislinie wird skaliert mit der verbundenen Ansicht.
-   Auto Horizontal   * Bei \"True\" wird das Ende der Hinweislinie als waagerechte Linie dargestellt.
-   Color   * Farbe der Hinweislinie.
-   Line Style   * Durchgehend, Strich-Punkt usw. wählbar.
-   Line Width   * Stärke der Hinweislinie.

## Programmierung


**Siehe auch   ***

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Hinweislinie kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden   *


```python
myPage = FreeCAD.ActiveDocument().Page
myBase = FreeCAD.ActiveDocument().View
leaderObj = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawLeaderLine','DrawLeaderLine')
FreeCAD.activeDocument().myPage.addView(leaderObj)
FreeCAD.activeDocument().leaderObj.LeaderParent = myBase
#first waypoint is always (0,0,0)  
#rest of waypoints are positions relative to (0,0,0)
leaderObj.WayPoints = [p0,p1,p2]
leaderObj.X = 5
leaderObj.Y = 5
```

## Hinweise

-   Du kannst deine Hinweislinie bearbeiten, indem du in der Baumansicht darauf doppelklickst. Ein Doppelklick in den Grafikbereich wird noch nicht unterstützt. Die Hinweislinie kann durch Drücken von \"Punkte bearbeiten\" im Bearbeitungsmodus bearbeitet werden. Um die Punktbearbeitung zu beenden   * drücke \"Änderungen speichern\" oder \"Änderungen verwerfen\".
-   Wenn kein Punkt als Anfangspunkt definiert wird, erscheint eine kurze Linie im Zentrum der Ansicht. Es können später keine Änderungen daran vorgenommen werden.
-   In den Eigenschaften ist **Hinweislinie Auto Horizontal** in den Grundeinstellungen aktiviert. Das bedeutet, dass das Ende der Hinweislinie horizontal dargestellt wird. Wenn nur eine Hinweislinie ohne Knick erstellt wurde, erscheint diese horizontal. Es gibt keine Möglichkeit weitere Punkte der Hinweislinie zu bearbeiten.
-   Für bestehende Hinweislinie kann **Auto Horizontal** auf \"False\" gesetzt werden.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LeaderLine/de
