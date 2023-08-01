---
- GuiCommand:
   Name: TechDraw LeaderLine
   Name/de: TechDraw Hinweislinie
   MenuLocation: TechDraw - Linien hinzufügen - Hinweislinie zur Ansicht hinzufügen
   Workbenches: [TechDraw](TechDraw_Workbench/de.md)
   Version: 0.19
   SeeAlso: [TechDraw FormatierteBeschriftung](TechDraw_RichTextAnnotation/de.md), [TechDraw Schweißsymbol](TechDraw_WeldSymbol/de.md), [TechDraw Liniengruppe](TechDraw_LineGroup/de.md)
---

# TechDraw LeaderLine/de


</div>



## Beschreibung

Das Werkzeug **TechDraw Hinweislinie** fügt einer Ansicht eine Hinweislinie hinzu. Andere Beschriftungsobjekte (wie z.B. die [FormatierteTextAnmerkung](TechDraw_RichTextAnnotation/de.md)) können mit der Hinweislinie verbunden werden, um komplexe Beschriftungen zusammenzustellen.

![](images/TechDraw_LeaderLine_sample.png )


<div class="mw-translate-fuzzy">



*Hinweislinie zur Ansicht View hinzugefügt*


</div>




<div class="mw-translate-fuzzy">

## Anwendung


</div>


<div class="mw-translate-fuzzy">

1.  Eine Ansicht auswählen.
2.  Die Schaltfläche **<img src="images/TechDraw_LeaderLine.svg" width=16px> Hinweislinie zur Ansicht hinzufügen** drücken. Es öffnet sich ein Dialog, der ermöglicht, eine Hinweislinie zu zeichnen und der Linie Endsymbole zuzuweisen.
3.  Auf **Punkte auswählen** klicken und danach auf das Zeichnungsblatt, um den Startpunkt der Linie festzulegen.
4.  Die Maus bewegen und auf einen anderen Punkt klicken, um eine Linie zu erstellen.
5.  Jetzt kann man entweder
    1.  das Zeichnen der Linie durch Doppelklicken oder Drücken von **Punkte speichern** beenden.
    2.  weitere Punkte hinzufügen, um weitere Linienabschnitte festzulegen.
6.  Um die Erstellung abzuschließen, das Dialogfeld durch Drücken von **OK** schließen.


</div>

## Usage edit 


<div class="mw-translate-fuzzy">

1.  Die Hinweislinie im Dokumentbaum auswählen und doppelklicken.
2.  Ein Dialogfeld wird geöffnet, in dem die Darstellung angepasst werden kann.
3.  Um die Punkte zu bearbeiten, auf **Punkte bearbeiten** klicken, und so die einzelnen Linienpunkte in der Zeichnung sichtbar machen.
4.  Die Punkte an die gewünschte Stelle ziehen und die Änderung durch Klicken auf **Änderungen speichern** abschließen.


</div>



## Hinweise


<div class="mw-translate-fuzzy">

-   Zum Bearbeiten einer Hinweislinie wird sie in der Baumansicht mit Doppelklick aktiviert. Ein Doppelklick in den Grafikbereich wird noch nicht unterstützt. Die Abschnitte der Hinweislinie können durch Drücken von \"Punkte bearbeiten\" angepasst werden. Zum Beenden der Punktbearbeitung wird \"Änderungen speichern\" oder \"Änderungen verwerfen\" gedrückt.
-   Wird während der Erstellung der Hinweislinie kein Punkt festgelegt, wird eine kurze Linie in der Mitte der Ansicht platziert. Es können später keine weiteren Punkte hinzugefügt werden.
-   In den [Einstellungen](TechDraw_Preferences/de.md) ist die Option **Hinweislinie automatisch horizontal** standardmäßig aktiviert. Das bedeutet, dass das Ende der Hinweislinie horizontal ausgerichtet wird. Ist nur ein Abschnitt vorhanden, wird eine horizontale Linie dargestellt, egal wo für den zweiten Punkt geklickt wurde.
-   Für bestehende Hinweislinie kann die automatische horizontale Ausrichtung ausgeschaltet werden, indem die {{PropertyData/de|Auto Horizontal}} auf \"False\" gesetzt wird.


</div>



## Eigenschaften

### Data


{{Properties_Title|Base}}

-    **Start Symbol|Enumeration**: The symbol at the start of the leaderline. Options: <img alt="" src=images/Arrowfilled.svg  style="width:20px;"> Filled Arrow, <img alt="" src=images/Arrowopen.svg  style="width:20px;"> Open Arrow, <img alt="" src=images/Arrowtick.svg  style="width:20px;"> Tick, <img alt="" src=images/Arrowdot.svg  style="width:20px;"> Dot, <img alt="" src=images/arrowopendot.svg  style="width:20px;"> Open Circle, <img alt="" src=images/arrowfork.svg  style="width:20px;"> Fork, <img alt="" src=images/arrowpyramid.svg  style="width:20px;"> Filled Triangle, None.

-    **End Symbol|Enumeration**: The symbol at the end of the leaderline. Idem.

-    **X|Distance**: The X coordinate of the leaderline relative to the View.

-    **Y|Distance**: The Y coordinate of the leaderline relative to the View.


{{Properties_Title|Leader}}

-    **Leader Parent|Link**: The View the leaderline is attached to.

-    **Way Points|VectorList**: The points of the leaderline.

-    **Scalable|Bool**: Specifies if the leaderline scales with **Leader Parent**.

-    **Auto Horizontal|Bool**: Specifies if the last leaderline segment is forced to be horizontal.

### View


{{TitleProperty|Base}}

-    **Keep Label|Bool**: Not used.

-    **Stack Order|Integer**: Over or underlap relative to other drawing objects. <small>(v0.21)</small> 


{{TitleProperty|Line Format}}

-    **Color|Color**: The color of the leaderline.

-    **Line Style|Enumeration**: The style of the leaderline. Options: NoLine, <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Continuous, <img alt="" src=images/Dash-line.svg  style="width:20px;"> Dash, <img alt="" src=images/Dot-line.svg  style="width:20px;"> Dot, <img alt="" src=images/DashDot-line.svg  style="width:20px;"> DashDot, <img alt="Length" src=images/DashDotDot-line.svg  style="width:20px;"> DashDotDot.

-    **Line Width|Length**: The width of the leaderline.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Hinweislinie kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


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





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LeaderLine/de
