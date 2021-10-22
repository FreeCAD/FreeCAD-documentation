---
- GuiCommand:/de
   Name:TechDraw Balloon   Name/de:Ballon
   MenuLocation:TechDraw → Anmerkungen → Ballon-Anmerkung einfügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.19
   SeeAlso:[TechDraw Anmerkung](TechDraw_Annotation/de.md)
---

# TechDraw Balloon/de

## Beschreibung

Das Werkzeug Stücklistensymbol kann Stücklistensymbole mit Führungslinie einer Zeichnung hinzufügen.

<img alt="" src=images/Techdraw_balloon.png  style="width:600px;">

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle die Ansicht, an die das Stücklistensymbol angefügt werden soll.
2.  Drücke die **<img src="images/TechDraw_Balloon.svg" width=16px> [Stücklistensymbol](TechDraw_Balloon/de.md)** Taste.
3.  Der Mauszeiger wird nun als Blasensymbol angezeigt. Klicke auf die Seite, um den Blasenursprung an die gewünschte Position zu setzen.
4.  Das Stücklistensymbol kann an die gewünschte Position gezogen werden. Verwende **Strg**+Ziehen, um die Blase und den Pfeil zu bewegen.
5.  Um die Eigenschaften der Blase zu ändern, doppelklicke entweder in der Zeichnung darauf oder doppelklicke im Modellbaum auf das Blasenobjekt. Dadurch wird der Stücklistensymboldialog geöffnet.


</div>

To move the bubble of a Balloon, press and hold the left mouse button on its center and drag the mouse.

To change the properties of a Balloon double-click it on the page or in the [Tree view](Tree_view.md). This will open the Balloon task panel.


<div class="mw-translate-fuzzy">

*Hinweis:*\' Die Position des Ballons ist relativ zur Ansicht und verwendet den gleichen Maßstabsfaktor wie die Ansicht.


</div>

## Verwendung von Trennzeichen 

Bei Verwendung einer Rechteckform können Trennzeichen mit \"\|\" im Text hinzugefügt werden. Zum Beispiel \"AAA\|TEST\|111\" ergibt:

<img alt="" src=images/balloon_separator.png  style="width:300px;">

## Eigenschaften

### Daten

-    **Text**: angezeigter Text

-    **Source View**: Gewählte Ansicht in der Zeichnung

-    **Origin X**: Blasenursprung in X-Richtung relativ zur Ansicht.

-    **Origin Y**: Blasenursprung in Y-Richtung relativ zur Ansicht.

-    **End Type**: Symbol am Ende der Führungslinie

Optionen: <img alt="" src=images/Arrowfilled.svg  style="width:20px;"> Pfeil, gefüllt <img alt="" src=images/Arrowopen.svg  style="width:20px;"> Pfeil, offen <img alt="" src=images/Arrowtick.svg  style="width:20px;"> Strich, <img alt="" src=images/Arrowdot.svg  style="width:20px;"> Punkt, <img alt="" src=images/arrowopendot.svg  style="width:20px;"> Kreis, offen, <img alt="" src=images/arrowfork.svg  style="width:20px;"> Haken, <img alt="" src=images/arrowpyramid.svg  style="width:20px;"> Dreieck, gefüllt, <img alt="" src=images/Arrownone.svg  style="width:20px;"> Ohne

-    **Shape**: Aussehen des Stücklistensymbols.

Optionen: <img alt="" src=images/Circular.svg  style="width:20px;"> Kreis, Ohne, <img alt="" src=images/Triangular.svg  style="width:20px;"> Dreieck, <img alt="" src=images/Inspection.svg  style="width:20px;"> Oval, <img alt="" src=images/Hexagon.svg  style="width:20px;"> Hexagon, <img alt="" src=images/Square-Shape.svg  style="width:20px;"> Quadrat, <img alt="" src=images/Rectangular.svg  style="width:20px;"> Rechteck

-    **Shape Scale**: Vergrößerungsfaktor für das **Stücklistensymbol** in beide Richtungen.

-    **Text Wrap**: Länge des Stücklistensymbols; -1 meint, daß die Größe der Einhüllung zum Text passt. +1 usw. vergrößern das Stücklistensymbol in X Richtung

-    **Kink Length**: Länge der horizontalen Linie vom **Stücklistensymbol** zur Führungslinie.

-    **X**: Verschiebung des Stücklistensymbols in X Richtung.

-    **Y**: Verschiebung des Stücklistensymbols in Y Richtung.

### Ansicht

-    **Farbe**: Farbe des Stücklistensymboltextes.

-    **Schriftart**: Der Name der Schriftart, die für die Stücklistensymbolblase verwendet werden soll.

-    **Schriftgröße**: Größe des Textes in mm.

-    **Linie Sichtbar**: Ob die Ballonlinie sichtbar ist.

-    **Linienbreite**: Strichstärke des Stücklistensymbols

## Skripten


**Siehe auch:**

[TechDraw Anwendungsschnittstelle](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Ballon-Werkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen benutzt werden:


```python
bal1 = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewBalloon','Balloon')
rc = page.addView(bal1)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Balloon/de
