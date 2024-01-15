---
 GuiCommand:
   Name: TechDraw LeaderLine
   Name/de: TechDraw Hinweislinie
   MenuLocation: TechDraw , Linien hinzufügen , Hinweislinie zur Ansicht hinzufügen
   Workbenches: TechDraw_Workbench/de
   Version: 0.19
   SeeAlso: TechDraw_RichTextAnnotation/de, TechDraw_WeldSymbol/de, TechDraw_LineGroup/de
---

# TechDraw LeaderLine/de



## Beschreibung

Das Werkzeug **TechDraw Hinweislinie** fügt einer Ansicht eine Hinweislinie hinzu. Andere Beschriftungsobjekte (wie z.B. die [FormatierteTextAnmerkung](TechDraw_RichTextAnnotation/de.md)) können mit der Hinweislinie verbunden werden, um komplexe Beschriftungen zusammenzustellen.

![](images/TechDraw_LeaderLine_sample.png ) 
*Hinweislinie zur Ansicht View hinzugefügt*



## Anwendung, Erstellen 

1.  Eine Ansicht auswählen.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_LeaderLine.svg" width=16px> [Hinweislinie zur Ansicht hinzufügen](TechDraw_LeaderLine/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Page  → <img src="images/TechDraw_LeaderLine.svg" width=16px> Hinweislinie zur Ansicht hinzufügen** auswählen.
3.  Ein Dialog wird geöffnet.
4.  Die Schaltfläche **Punkte auswählen** drücken
5.  Den ersten Punkt auf dem Zeichnungsblatt auswählen, um den Startpunkt der Linie festzulegen.
6.  Den nächsten Punkt auf dem Zeichnungsblatt auswählen. Wird **Ctrl** gedrückt gehalten, wird auf Winkeln eingerastet, die ein Vielfaches von 22.5° sind. Wahlweise kann anstatt eines einzelnen Klicks ein Doppelklick zum Beenden der Punkteingabe verwendet werden.
7.  Wahlweise weitere Punkte auswählen.
8.  Wurde der Punkt nicht mit Doppelklick ausgewählt: Die Schaltfläche **Punkte speichern** drücken.
9.  Wahlweise **Startsymbol**, **Endsymbol**, **Farbe**, **Breite** und **Stil** der Hinweislinie anpassen. Siehe [Eigenschaften](#Eigenschaften.md) für weitere Informationen.
10. Die Schaltfläche **OK** drücken.



## Anwendung, Bearbeiten 

1.  Eine Hinweislinie in der [Baumansicht](Tree_view/de.md) doppelt anklicken.
2.  Ein Aufgaben-Bereich wird geöffnet.
3.  Zum Bearbeiten der Punkte:
    1.  Die Schaltfläche **Punkte bearbeiten** drücken.
    2.  Die Hinweislinie wird mit temporären Punkten markiert.
    3.  Einen oder mehrere Knoten auf eine neue Position ziehen.
    4.  Die Schaltfläche **Save changes** drücken.
4.  Wahlweise **Startsymbol**, **Endsymbol**, **Farbe**, **Breite** und **Stil** der Hinweislinie anpassen. Siehe [Eigenschaften](#Eigenschaften.md) für weitere Informationen.
5.  Die Schaltfläche **OK** drücken.



## Hinweise

-   Einer vorhandenen Hinweislinie können keine Punkte hinzugefügt oder von ihr entfernt werden.
-   Wurden während der Erstellung der Hinweislinie keine Punkte festgelegt, wird eine kurze Linie in der Mitte der Ansicht positioniert. Es gibt keine Möglichkeit so eine Linie zu reparieren; sie sollte gelöscht werden.
-   Standardmäßig ist die [Einstellung](TechDraw_Preferences/de#Anmerkung.md) **Hinweislinie automatisch horizontal** aktiviert. Das bedeutet, dass der letzte Abschnitt neuer Hinweislinien horizontal ausgerichtet wird. Ist nur ein Abschnitt vorhanden, ist das Ergebnis eine einzelne horizontale Linie.

-   Für vorhandene Hinweislinien kann diese automatische horizontale Ausrichtung ausgeschaltet werden, indem ihre {{PropertyData/de|Auto Horizontal}} angepasst wird.



## Eigenschaften



### Daten


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|Start Symbol|Enumeration}}: Das Symbol am Anfang der Hinweislinie. Optionen (unter Einstellungen): <img alt="" src=images/Arrowfilled.svg  style="width:20px;"> Filled Arrow (Gefüllte Pfeilspitze), <img alt="" src=images/Arrowopen.svg  style="width:20px;"> Open Arrow (Offene Pfeilspitze), <img alt="" src=images/Arrowtick.svg  style="width:20px;"> Tick (Schrägstrich), <img alt="" src=images/Arrowdot.svg  style="width:20px;"> Dot (Punkt), <img alt="" src=images/arrowopendot.svg  style="width:20px;"> Open Circle (Ring), <img alt="" src=images/arrowfork.svg  style="width:20px;"> Fork (Gabel), <img alt="" src=images/arrowpyramid.svg  style="width:20px;"> Filled Triangle (Gefülltes Dreieck), None (Kein).

-    {{PropertyData/de|End Symbol|Enumeration}}: Das Symbol am Ende der Hinweislinie. Wie vorher.

-    {{PropertyData/de|X|Distance}}: Die X-Koordinate der Hinweislinie relativ zur Ansicht.

-    {{PropertyData/de|Y|Distance}}: Die Y-Koordinate der Hinweislinie relativ zur Ansicht.


{{Properties_Title|Leader}}

-    {{PropertyData/de|Leader Parent|Link}}: Ansicht in der die Hinweislinie verankert ist.

-    {{PropertyData/de|Way Points|VectorList}}: Die Punkte der Hinweislinie.

-    {{PropertyData/de|Scalable|Bool}}: Legt fest, ob die Hinweislinie synchron zur {{PropertyData/de|Leader Parent}} skaliert wird.

-    {{PropertyData/de|Auto Horizontal|Bool}}: Legt fest, ob, der letzte Abschnitt der Hinweislinie horizontal verlaufen muss.



### Ansicht


{{TitleProperty|Basis}}

-    {{PropertyView/de|Keep Label|Bool}}: Nicht verwendet.

-    {{PropertyView/de|Stack Order|Integer}}: Angabe der Lage über oder unter anderen Zeichnungsobjekten. {{Version/de|0.21}}


{{TitleProperty|Line Format}}

-    {{PropertyView/de|Color|Color}}: Die Farbe der Hinweislinie.

-    {{PropertyView/de|Line Style|Enumeration}}: Der Stil der Hinweislinie. Optionen: NoLine (Keine), <img alt="" src=images/Continuous-line.svg  style="width:20px;"> Continuous (Volllinie), <img alt="" src=images/Dash-line.svg  style="width:20px;"> Dash (Strichlinie), <img alt="" src=images/Dot-line.svg  style="width:20px;"> Dot (Punktlinie), <img alt="" src=images/DashDot-line.svg  style="width:20px;"> DashDot (Strich-Punkt-Linie), <img alt="Length" src=images/DashDotDot-line.svg  style="width:20px;"> DashDotDot (Strich-Zweipunkt-Linie).

-    {{PropertyView/de|Line Width|Length}}: Strichstarke der Hinweislinie.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

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
