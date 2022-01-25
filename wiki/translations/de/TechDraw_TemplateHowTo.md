---
- TutorialInfo:/de
   Topic:Entwerfen
   Level:Zwischenstufe
   Time:60 Minuten
   Author:[http://freecadweb.org/wiki/index.php?title=User:wandererfan wandererfan]
   FCVersion:0.17
---

# TechDraw TemplateHowTo/de





## Einführung

Dieses Tutorium zeigt dir die Erstellung einer [SVG](SVG/de.md) Datei, die als Hintergrund [Vorlage](TechDraw_Templates/de.md) für die [TechDraw Arbeitsbereich](TechDraw_Workbench/de.md)-Seiten verwendet werden kann.

Dieses Tutorial setzt voraus, dass du mäßig vertraut bist mit [Inkscape](https://de.wikipedia.org/wiki/Inkscape) und [SVG](SVG/de.md) sowie in FreeCAD und dem [TechDraw](TechDraw_Workbench/de.md)-Arbeitsbereich.

Wir erstellen eine einfache Vorlage für US Briefgrößenpapier in Querformat Ausrichtung.

Eine Kopie des Ergebnisses dieses Tutoriums ist verfügbar in 
```python
$INSTALL_DIR/Mod/TechDraw/Templates/HowToExample.svg
```

Wobei `$INSTALL_DIR` das Verzeichnis ist, wo FreeCAD installiert wurde, z.B. 
```python
/usr/share/freecad/Mod/TechDraw/Templates/HowToExample.svg
```

## Basisdokument erzeugen 

1\. Öffne ein neues Dokument in Inkscape

2\. In den Dokumenteneigenschaften

-   Wähle die Seitengröße \"US Letter\" oder \"A4\" und die Ausrichtung \"Querformat\".
-   Setze die Standardeinheiten auf \"mm\" und die Seitengröße auf Breite \"279,4\" und Höhe \"215,9\". Für DIN-A4 würdest du \"210\" und \"297\" verwenden.

<img alt="" src=images/InkDocProp.png  style="width:800px;"> 
*align=center|Inkscape: Dokument mit Seitengröße und Ausrichtung* 

3\. Verwende den XML Editor, um dem `<svg>` Element eine \"freecad\" Namensraumklausel hinzuzufügen.

-   xmlns:freecad="[http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace](http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace)"

Beachte, dass deine editierbaren Texte *nicht* funktionieren, wenn du \"<https://>\...\" verwendest, auch wenn das Wiki heutzutage über https erreicht wird. Da SVG ein von Menschen lesbares Format ist, könntest du die obige Zeile auch mit einem Texteditor in die Datei eingeben. <img alt="" src=images/InkXMLNameSpace.png  style="width:800px;"> 
*align=center|Inkscape: XML Editor, der die "freecad" Namensraumklausel zum Element <svg> hinzufügt* 

## Erstelle eine Vorlagenzeichnung 

4\. Zeichne Umrisse, Zonennummern, Mittellinien und andere Geometrie.

5\. Zeichne die Kästen und Linien für das Schriftfeld.

6\. Füge deinen statischen Text hinzu und positioniere ihn.

7\. Füge den zu bearbeitenden Text hinzu und positioniere ihn.

8\. Du hast nun dein fertiges Kunstwerk, das in etwa so aussehen sollte: <img alt="" src=images/InkFinishedArt.png  style="width:800px;"> 
*align=center|Inkscape: Vorläufiges Vorlagenlayout* 

## Erstelle änderbare Felder 

9\. Verwende den XML Editor, um mit `freecad:editable` jedes Textelement `text` auch als änderbar zu kennzeichnen

-   vergib einen sinnvollen Namen für jedes änderbaren Text

<img alt="" src=images/InkXMLeditableTag.png  style="width:800px;"> 
*align=center|Inkscape: XML Editor beim Hinzufügen der "freecad:editable" Eigenschaft zum gewünschten <text> Element* 

## Größe der SVG anpassen 

10\. Verwende den XML Editor, um das `viewBox` Attribut so anzupassen, dass es deiner Seitengröße in Millimetern entspricht.

-   Es sind vier Werte im Format `"0 0 Breite Höhe"`

<img alt="" src=images/InkXMLviewBox.png  style="width:800px;"> 
*align=center|Inkscape: XML Editor beim Anpassen des Anzeigefeldes zur Übereinstimmung mit der Seitengröße in Millimetern* 

11\. Deine Vorlage wird nun viel größer als gewünscht erscheinen. <img alt="" src=images/InkMuchTooBig.png  style="width:800px;"> 
*align=center|Inkscape: Vorläufiges Vorlagenlayout überschreitet die Seitengröße* 

12\. Wir müssen ihn verkleinern.

-    **Bearbeiten → Alles in allen Schichten auswählen**oder Kästchen auswählen und alles auswählen.

-   Passe die **W:** und **H:** Spinboxen an die Größe Ihres Kunstwerks in Millimetern an.

-   Stelle sie auf die Seitengröße abzüglich der anwendbaren Ränder ein, z. B. **W: 250** und **H: 200**.

13\. Verwende \"Ausrichten und Verteilen\" oder die **X:** und **Y:** Spinboxen, um das Kunstwerk bei Bedarf innerhalb der Grenzen der Seite zu positionieren.

14\. Die Vorlage sollte nun so wie das Beispiel oben aussehen.

## Entferne Transformationen aus dem SVG 

15\. Stelle sicher, dass alle editierbaren Textelemente nicht gruppiert sind mit **Shift**+**Strg**+**g**.

16\. Wähle alles auf Deiner Seite **Bearbeiten → Alles auswählen**, und dann **Bearbeiten → Kopieren** (**Ctrl**+**c**).

17\. Lösche dann die aktuelle Schicht mit **Ebene → aktuelle schicht löschen**

:   Hinweis: Wenn du die Ebene bereits gelöscht hast (in deinem Lagen Paneel ist keine Lage aufgeführt), ist dieser Schritt nicht erforderlich. In diesem Fall solltest du alle (**Ctrl**+**a**), die Auswahl ausschneiden (**Ctrl**+**x**) und mit dem Befehl im nächsten Schritt einfügen.

18\. Füge dann ein **Bearbeiten → Einfügen an Ort und Stelle**.

:   **Hinweis:** Dieser Befehl verhindert, dass die Textpositionen in Transformations Tags gespeichert werden.  Es ist wichtig, dass du nicht den normalen Einfügebefehl verwendest!

19\. Deine Vorlagen sollte nun korrekt aussehen und keine ungewünschten Transformationen enthalten.

20\. Speichere Deine Vorlage. Wenn Du Inkscape benutzt, speichere sie vorzugsweise als **Plain SVG**, da FreeCAD nur mit Elementen der SVG-1.1-Spezifikation umgehen kann. **Plain SVG** entfernt alle inkscape-spezifischen XML-Anweisungen.

21\. Probiere sie in FreeCAD und dem [TechDraw-Arbeitsbereich](TechDraw_Workbench/de.md) mit [Seite mittels Vorlage einfügen](TechDraw_PageTemplate/de.md) aus. ![](images/FCTemplateHow.png ) 
*align=center|FreeCAD: fertige Vorlage mit änderbarem Textfeld während der Änderung* 

## Anmerkungen

Verwende keine Lagen in Inkscape, bevor Du nicht Vorlagen ohne sie beherrscht. Lagen und Gruppen können unerwünschte Transformationen in der [SVG](SVG/de.md)-Datei verursachen.

Stelle als letzten Schritt vor der Verwendung deiner neuen Vorlage sicher, daß alle Umwandlungsklauseln aus dem Svg Code entfernt werden. Umwandlungsklauseln **werden Probleme verursachen**.

Siehe eine Stackoverflow Debatte auf [Entfernen von Transformationsklauseln in SVG Dateien](https://stackoverflow.com/questions/13329125/removing-transforms-in-svg-files).

Wenn du die grünen Kästchen für deine bearbeitbaren Texte nicht siehst, ist möglicherweise etwas mit deinem Dokumentenmaßstab nicht in Ordnung. Öffne dein Datei erneut in Inkscape und bestätige, dass die Werte des AnsichtsKasten und die Größen übereinstimmen.

If texts appear offset in FreeCAD, you may need to remove the {{Incode|xml:space<nowiki>=</nowiki>"preserve"}} attributes in the SVG file. See: <https://www.forum.freecadweb.org/viewtopic.php?t=50897>.


 {{TechDraw Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw TemplateHowTo/de
