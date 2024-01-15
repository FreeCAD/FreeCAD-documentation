---
 GuiCommand:
   Name: TechDraw Balloon
   Name/de:  TechDraw Hinweisfeld
   MenuLocation: TechDraw , Anmerkungen , Hinweisfeld einfügen
   Workbenches: TechDraw_Workbench/de
   Version: 0.19
   SeeAlso: TechDraw_Annotation/de
---

# TechDraw Balloon/de



## Beschreibung

Das Werkzeug **TechDraw Hinweisfeld** kann einer Zeichnung Hinweisfelder mit zugehöriger Hinweislinie hinzufügen. (Voreingestellt ist ein kreisförmiges Hinweisfeld, das u.a. zur Kennzeichnung der Elemente einer Stückliste dienen kann)

<img alt="" src=images/Techdraw_balloon.png  style="width:600px;">



## Anwendung

1.  Eins der folgenden auswählen:
    -   Eine Ansicht (auf dem Blatt oder in der [Baumansicht](Tree_view/de.md)).
    -   Einen Knoten in einer Ansicht. {{Version/de|0.20}}
    -   Eine Kante in einer Ansicht. {{Version/de|0.20}}
    -   Einen abgeschlossenen Bereich in einer Ansicht. {{Version/de|0.20}}
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_Balloon.svg" width=16px> [Hinweisfeld einfügen](TechDraw_Balloon/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → Anmerkungen → <img src="images/TechDraw_Balloon.svg" width=16px> Hinweisfeld einfügen** auswählen.
3.  Wenn eine Ansicht oder ein Bereich ausgewählt wurde:
    1.  Der Mauszeiger wird mit dem Symbol dieses Werkzeuges angezeigt.
    2.  Einen Punkt auf dem Blatt angeklicken, um den Ursprung der Hinweisfeldes (Startpunkt der Hinweislinie) festzulegen.

Um ein Hinweisfeld zu verschieben, positioniert man den Mauszeiger über seiner Mitte, drückt und hält die linke Maustaste und zieht die Maus.

Um die Eigenschaften eines Hinweisfeldes zu ändern, wählt man es per Doppelklick auf dem Blatt oder in der [Baumansicht](Tree_view/de.md) aus. Dies Öffnet den Aufgabenbereich des Hinweisfeldes.

*Hinweis:*\' Die Position eines Hinweisfeldes ist relativ zu seiner Ursprungsansicht und verwendet den gleichen Maßstabsfaktor.



## Verwendung von Trennzeichen 

Bei Verwendung einer Rechteckform können Trennzeichen mit \"\|\" im Text hinzugefügt werden. Zum Beispiel ergibt \"AAA\|TEST\|111\":

<img alt="" src=images/balloon_separator.png  style="width:300px;">



## Eigenschaften



### Daten

-    {{PropertyData/de|Text}}: anzuzeigender Text

-    {{PropertyData/de|Source View}}: Ursprungsansicht des Hinweisfeldes.

-    {{PropertyData/de|Origin X}}: X-Lage des Ursprungs des Hinweisfeldes relativ zur Ansicht.

-    {{PropertyData/de|Origin Y}}: Y-Lage des Ursprungs des Hinweisfeldes relativ zur Ansicht.

-    {{PropertyData/de|End Type}}: Symbol am Ende der Hinweislinie

Optionen: <img alt="" src=images/Arrowfilled.svg  style="width:20px;"> Gefüllte Pfeilspitze, <img alt="" src=images/Arrowopen.svg  style="width:20px;"> Offene Pfeilspitze, <img alt="" src=images/Arrowtick.svg  style="width:20px;"> Schrägstrich, <img alt="" src=images/Arrowdot.svg  style="width:20px;"> Punkt, <img alt="" src=images/arrowopendot.svg  style="width:20px;"> Ring, <img alt="" src=images/arrowfork.svg  style="width:20px;"> Gabel, <img alt="" src=images/arrowpyramid.svg  style="width:20px;"> gefülltes Dreieck, <img alt="" src=images/Arrownone.svg  style="width:16px;"> Kein.

-    {{PropertyData/de|End Type Scale}}: Vergrößerungsfaktor für **End Type**.

-    {{PropertyData/de|Bubble Shape}}: Form des Hinweisfeldes.

Optionen: <img alt="" src=images/Circular.svg  style="width:20px;"> Kreisförmig, Kein, <img alt="" src=images/Triangle.svg  style="width:20px;"> Dreieck, <img alt="" src=images/Inspection.svg  style="width:20px;"> Prüfmaß, <img alt="" src=images/Hexagon.svg  style="width:20px;"> Sechseck, <img alt="" src=images/TechDraw_Square.svg  style="width:20px;"> Quadrat, <img alt="" src=images/Rectangle.svg  style="width:20px;"> Rechteck (, Linie).

-    {{PropertyData/de|Shape Scale}}: Vergrößerungsfaktor für **Bubble Shape** (die Form des Hinweisfeldes).

-    {{PropertyData/de|Text Wrap}}: Länge für Textumbuch; -1 heißt, daß der Text nicht umbrochen wird und dass das Ergebnis in jedem Falle eine einzige Zeile ist.

-    {{PropertyData/de|Kink Length}}: Abstand vom **Hinweisfeld** zum Knick der Hinweislinie.

-    {{PropertyData/de|X}}: Horizontale Lage des Hinweisfeldes relativ zur Ansicht.

-    {{PropertyData/de|Y}}: Vertikale Lage des Hinweisfeldes relativ zur Ansicht.



### Ansicht

-    {{PropertyView/de|Color}}: Farbe des Textes im Hinweisfeld.

-    {{PropertyView/de|Font}}: Der Name der Schriftart, die für das Hinweisfeld verwendet werden soll.

-    {{PropertyView/de|Fontsize}}: Texthöhe in mm.

-    {{PropertyView/de|Line Visible}}: Ob die Linie des Hinweisfeldes sichtbar ist.

-    {{PropertyView/de|Line Width}}: Strichstärke der Linie des Hinweisfeldes



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Ballon-Werkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen benutzt werden:


```python
bal1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewBalloon','Balloon')
rc = page.addView(bal1)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Balloon/de
