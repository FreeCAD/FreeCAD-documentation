# Artwork Guidelines/de
## Einleitung


**Hinweis:**

für alle Symbole im Quellbaum, siehe [Grafik](Artwork/de.md).

Ein FreeCAD **Symbol** (icon) wird aus 6 Elementen zusammengesetzt, die man sich mit dem Akronym SALCHO merken kann: **S**troke, **A**lignment, **L**ighting, **C**olor, **H**ighlighting, **O**utline. (deutsch: *Strich*, *Ausrichtung*, *Beleuchtung*, *Farbe*, *Hervorhebung*, *Kontur*)

Hier ist ein konkretes, wenn auch willkürliches Beispiel:

![](images/FreeCAD_icon_example_details.svg )

  --- 
  A   Die Hervorhebungsfarbe wird für die gesamte Oberfläche benutzt, um von oben hereinfallendes Licht anzudeuten
  B   Die obligatorische dunkle Außenlinie umgibt die Symbolform, um Formkontrast zu bieten
  C   Direkt innerhalb der Außenlinie bietet der Hervorhebungsstrich (Hervorhebungsfarbe) Kontrast zu dunklen Hintergründen
  D   Diese Fläche ist hauptsächlich die Basisfarbe, aber ein leichter Verlauf von der Hervorhebung (oben links) zur Basis (unten rechts) vermittelt den Eindruck von Licht, das von links einfällt
  E   Die Hervorhebung hier ist die Basisfarbe (ein Ton darunter), um den Eindruck zu vermitteln, dass dies die am weitesten vom Licht entfernte Fläche ist
  F   Diese Fläche ist wie D, geht aber von der Basisfarbe (oben links) nach Dunkel (unten links), um den Eindruck zu vermitteln, dass dies die am weitesten vom Licht entfernte Fläche ist
  --- 

In den folgenden Abschnitten werden diese Elemente ausführlicher erläutert.

Dieses Symbol wird wie folgt angezeigt:

+++
| <img alt="" src=images/FreeCAD_icon_example.svg  style="width:64px;"> | 64 px, Originalgröße, große Schaltflächen.                                             |
+++
| <img alt="" src=images/FreeCAD_icon_example.svg  style="width:32px;"> | 32 px, mittlere Größe, normale Schaltflächen.                                          |
+++
| <img alt="" src=images/FreeCAD_icon_example.svg  style="width:16px;"> | 16 px, geringe Größe, wie sie in der [Baumansicht](Tree_view/de.md) erscheint. |
+++



## Farben


**Obligatorisch**

FreeCAD verwendet eine Palette, die der [Tango Palette](https://web.archive.org/web/20190921043652/http://tango.freedesktop.org/tango_icon_theme_guidelines) nachempfunden ist. Jede Hauptfarbe gibt es in 4 Farbtönen: Highlight, Base, Dark und Outline. Beachte, dass die Umrisslinie nicht komplett schwarz ist, sondern eine sehr dunkle Variante der Grundfarbe.

+++++
| #fce94f         | #edd400         | #c4a000         | #302b00         |
| (252, 233, 79)  | (237, 212, 0)   | (196, 160, 0)   | (48, 43, 0)     |
| Butter 1        | Butter 2        | Butter 3        | Butter 4        |
+=================+=================+=================+=================+
| #8ae234         | #73d216         | #4e9a06         | #172a04         |
| (138, 226, 52)  | (115, 210, 22)  | (78, 154, 6)    | (23, 42, 4)     |
| Chameleon 1     | Chameleon 2     | Chameleon 3     | Chameleon 4     |
+++++
| #fcaf3e         | #f57900         | #ce5c00         | #321900         |
| (252, 175, 62)  | (245, 121, 0)   | (206, 92, 0)    | (50, 25, 0)     |
| Orange 1        | Orange 2        | Orange 3        | Orange 4        |
+++++
| #729fcf         | #3465a4         | #204a87         | #0b1521         |
| (114, 159, 207) | (52, 101, 164)  | (32, 74, 135)   | (11, 21, 33)    |
| Sky Blue 1      | Sky Blue 2      | Sky Blue 3      | Sky Blue 4      |
+++++
| #ad7fa8         | #75507b         | #5c3566         | #171018         |
| (173, 127, 168) | (117, 80, 123)  | (92, 53, 102)   | (23, 16, 24)    |
| Plum 1          | Plum 2          | Plum 3          | Plum 4          |
+++++
| #e9b96e         | #c17d11         | #8f5902         | #271903         |
| (233, 185, 110) | (193, 125, 17)  | (143, 89, 2)    | (39, 25, 3)     |
| Chocolate 1     | Chocolate 2     | Chocolate 3     | Chocolate 4     |
+++++
| #ef2929         | #cc0000         | #a40000         | #280000         |
| (239, 41, 41)   | (204, 0, 0)     | (164, 0, 0)     | (40, 0, 0)      |
| Scarlet Red 1   | Scarlet Red 2   | Scarlet Red 3   | Scarlet Red 4   |
+++++
| #34e0e2         | #16d0d2         | #06989a         | #042a2a         |
| (52, 224, 226)  | (22, 208, 210)  | (6, 152, 154)   | (4, 42, 42)     |
| FreeTeal 1      | FreeTeal 2      | FreeTeal 3      | FreeTeal 4      |
+++++
| #ffffff         | #eeeeec         | #d3d7cf         | #babdb6         |
| (255, 255, 255) | (238, 238, 236) | (211, 215, 207) | (186, 189, 182) |
| Snowy White     | Aluminium 1     | Aluminium 2     | Aluminium 3     |
+++++
| #888a85         | #555753         | #2e3436         | #000000         |
| (136, 138, 133) | (85, 87, 83)    | (46, 52, 54)    | (0, 0, 0)       |
| Aluminium 4     | Aluminium 5     | Aluminium 6     | Jet Black       |
+++++



*Vollständige Palette*

Eine Auswahl einiger Hauptfarben.

      
                                                                                                                                                          Gelbtöne sollten für Werkzeuge verwendet werden, die Objekte erstellen; siehe die Arbeitsbereiche [Part](Part_Workbench/de.md) und [Draft](Draft_Workbench/de.md) für Beispiele.
  style=\"background-color:#729fcf;\|   style=\"background-color:#3465a4;\|   style=\"background-color:#204a87;\|   style=\"background-color:#0b1521;\|   Blautöne sollten für Werkzeuge verwendet werden, die Objekte verändern; siehe die Arbeitsbereiche [Part](Part_Workbench/de.md) und [Draft](Draft_Workbench/de.md) für Beispiele.
  style=\"background-color:#34e0e2\|    style=\"background-color:#16d0d2\|    style=\"background-color:#06989a\|    style=\"background-color:#042a2a\|    Türkistöne sollten für Werkzeuge im Zusammenhang mit Ansichten verwendet werden; siehe [Menü Ansicht](Std_View_Menu/de.md) für Beispiele.
  style=\"background-color:#ef2929\|    style=\"background-color:#cc0000\|    style=\"background-color:#a40000\|    style=\"background-color:#280000\|    Rottöne sollten für Werkzeuge im Zusammenhang mit (dem Festlegen von) Randbedingungen verwendet werden; siehe den Arbeitsbereich [Sketcher](Sketcher_Workbench/de.md) für Beispiele.
      

   
  style=\"width: 25%;\|Warum sollte ich mich auf diese Farben beschränken?   Die Einschränkung auf eine bestimmte Farbpalette hilft, eine heterogene Ikonographie zu vermeiden und verbessert die Lesbarkeit bei vielen Symbolen.
  Wie verwende ich die FreeCAD-Palette?                                      Die Installation [der Palette](https://gist.github.com/GAZ082/724d2092b2986e3b17b9663f34093cf5) ist so einfach wie [Kopiere dir sie in deinen Inkscape Palettenordner](https://inkscape.org/en/learn/faq/#how-install-new-extensions-palettes-document-templates-symbol-sets-icon-sets-etc).
   



## Gitter und Strichbreite 


**Obligatorisch**

FreeCAD Symbole haben eine nominale Größe von 64 Pixeln, sowohl in der Breite als auch in der Höhe. Bei der Erstellung oder Bearbeitung, vergewissere dich, dass die Dokumentgröße 64 x 64 beträgt, wobei die Einheit Pixel (px) ist. Ein innerer Rand von 2px Leerraum rund um den Dokumentbereich ist nützlich, da er Effekte wie Anti-Aliasing (Verwischung der Kanten) verhindert. Das heißt, der nutzbare Raum für das Symbol sollte als 60 x 60 betrachtet werden, und die Ränder sollten leer gelassen werden.

<img alt="" src=images/FreeCAD_icon_size.svg  style="width:128px;"> 
*Zeichne das Symbol innerhalb des blauen Bereichs und alles wird gut funktionieren.*

Es wird auch dringend empfohlen, ein visuelles Gitter zu verwenden, das alle Pixel eine Nebenrasterlinie und alle 2 Pixel eine Hauptrasterlinie aufweist. Die Striche des Symbols sollten an den Schnittpunkten des Nebenrasters ausgerichtet werden.

Striche sollten nicht \"dünner\" als 2px sein, mit abgerundeten Köpfen und Ecken in den meisten Fällen. Striche können *dicker* sein, aber sie sollten vorzugsweise ein Vielfaches von 2px sein, um die Skalierung Unschärfe zu minimieren.

<img alt="" src=images/FreeCAD_icon_stroke_2px.svg  style="width:320px;"> 
*Raster mit Strichen, die ein Vielfaches von 2px sind.*

   
  Warum dieses Gitter und Strichbreite verwenden?   Aus historischen Gründen verwendet FreeCAD ein 64x64 Symbol, das dann verkleinert wird. Das ist nicht ideal, aber es verleiht dem Ganzen Charakter. Infolgedessen hilft die Ausrichtung an einem Zweierpotenzraster mit Dicken, die Zweierpotenzen sind, Anti-Aliasing Probleme bei der Neuskalierung zu vermeiden oder zumindest abzuschwächen.
  Wie kann ich das einhalten?                       Wenn du Inkscape verwendest, gehe zu **Datei → Dokumenteigenschaften** und stelle sicher, dass die Breite, Höhe und Einheiten deiner Seite korrekt sind. Dann gehe auf den **Gitter** reiter, klicke auf **Neu**, setze die Einheiten auf `px`, `Abstand X` und `Abstand Y` auf 1 und `Hauptgitterlinie jede` auf 2.
   



## Außenlinie


**Obligatorisch**

Gestützt auf die Hauptfarbe des Symbols stelle sicher, dass es, wie bereits erwähnt, eine dunkle Umrandung von 2 px gibt. Dies funktioniert zusammen mit der Hervorhebung, um einen guten Formkontrast auf mehreren Hintergrundtönen zu gewährleisten.

<img alt="" src=images/Draft_Point.svg  style="width:" height="128px;"> <img alt="" src=images/Draft_Point_backgrounds.svg  style="width:" height="128px;"> 
*Der dunkle Rand des Symbols ist der Umriss.*

   
  Warum wird die Außenlinie gebraucht?   Die Umrisslinie ist das Skelett, an dem alles andere hängt, indem sie den Formkontrast erhöht. Die Verwendung der Umrissfarbe oder der dunklen Farbe hängt von der jeweiligen Situation ab, aber ohne diese Linie wird die Auswahl an Hintergründen, auf denen das Symbol sichtbar ist, drastisch begrenzt
  Wie kann ich dies beheben?             Füge einfach um jeden Teil des Symbols, der an die Hintergrundfarbe angrenzt, einen Strich von 2 px hinzu, d. h. die Umrisslinie ist für externe Striche. Bei Formen, die in der Mitte ein Loch haben, z. B. ein Donut, sollte der Umriss auch um das innere Loch gelegt werden. Richte die Knoten deines Pfades so weit wie möglich am Raster aus, die auf die kleineren Gitterschnittpunkte abzielen.
   



## Hervorhebung


**Dringend empfohlen**

Füge einen internen Strich von 2px unter Verwendung der Hervorhebungsfarbe hinzu, um zu helfen, dass die Außenlinie hervorspringt. Auf dunklen Hintergründen ist es diese Hervorhebung, die dem Symbol die Form gibt.

<img alt="" src=images/Draft_Move.svg  style="width:" height="128px;"> <img alt="" src=images/Draft_Move_backgrounds.svg  style="width:" height="128px;"> 
*Die helle Hervorhebung hilft bei dunklen Hintergründen.*

   
  Warum die Hervorhebung benutzen?   Die Hervorhebung arbeitet mit der Kontur zusammen, um den Kontrast der Form zu verbessern, insbesondere auf dunklen Hintergründen. Es ist nie eine schlechte Idee, aber wenn du nicht den nötigen Platz hast, z. B. wenn du eine sehr dünne Linie hast, kannst du darauf verzichten, vorausgesetzt, du hast für einen ausreichenden Kontrast zwischen der Hauptfarbe und dem Umriss gesorgt.
  Wie kann ich das einhalten?        Ziehe wie bei der Kontur einfach einen Strich von 2 px um die Innenseite der Kontur, wobei du die Knoten nach Möglichkeit am Raster fängst und auf die kleineren Rasterschnittpunkte abzielst.
   



## Beleuchtung


**Optional**

Gemäß den Tango Richtlinien solltest du beim Hinzufügen eines Beleuchtungsverlaufseffekts versuchen, es so aussehen zu lassen, als käme das Licht von links oben. Dazu fügst du die Farbe für die Lichter oben links und die Farbe für die Basis oder Dunkelheit unten rechts hinzu. Beachte, dass nur Palettenfarben verwendet werden.

<img alt="" src=images/Draft_Clone.svg  style="width:" height="128px;"> <img alt="" src=images/Draft_Clone_backgrounds.svg  style="width:" height="128px;"> 
*Subtiler Lichteffekt von links oben kommend.*

   
  style=\"width:25%;\|Warum Beleuchtung verwenden?   Beleuchtung ist nur eine weitere Möglichkeit, Symbole miteinander zu verbinden und sicherzustellen, dass es verschiedene Stufen von [\"value\"](https://en.wikipedia.org/wiki/Lightness) gibt, um ihre Lesbarkeit zu verbessern. Vorausgesetzt, der Umriss und die Hervorhebung sind vorhanden, kann dies als optional betrachtet werden.
  Wie kann ich das einhalten?                        Stelle die Füllung auf einen linearen oder radialen Farbverlauf ein. In Inkscape ist dies in den Strich- und Fülleinstellungen möglich; mit \"F2\" kann man die Knoten des Farbverlaufs verschieben, um sicherzustellen, dass sie im richtigen Winkel stehen.
   



## Empfohlenes Aufzeichnungsformat 

Alle Symbole sollten im Format [SVG](SVG/de.md) mit einer Vektorbildanwendung, wie beispielsweise [Inkscape](http://inkscape.org), erstellt werden. Dies erleichtert die Anwendung von Änderungen und die Ableitung zusätzlicher Symbole im selben Anwendungsbereich.

Wenn Symbole für die direkte Verwendung durch FreeCAD (in einer \*.qrc-Datei) übertragen werden, speichere sie als \"Reines SVG\". Dies reduziert die Größe des Symbols und spart Festplatten- und Speicherplatz.



## Abschließende Bemerkungen 

Denke daran:: **SALCHO**, Stroke, Alignment, Lighting, Colour, Highlight, Outline

Hier sind einige Tips, um Deine Arbeit zu überprüfen:



### Größe prüfen 

Inkscape verfügt über ein praktisches Werkzeug, um dein Symbol in verschiedenen Größen zu prüfen. Gehe zu **Ansicht → Symbolvorschau...** und es wird dir Voransichten deines Symbols geändert auf 16, 24, 32 und 64 Pixel anzeigen.



### Prüfung Deiner Umrißlinie 

1.  Setze dein Symbol auf ein großes Rechteck, das die gleiche Farbe hat wie die dunkelste Farbe deines Symbols.
2.  Sieht das immer noch gut aus? Prima! Gehe zum nächsten Schritt. Wenn nicht, passe die Hervorhebung an.
3.  Mache dasselbe, aber dieses Mal mit der hellsten Farbe.
4.  Sieht das immer noch gut aus? Sehr gut. Umrisse und Hervorhebungen wurden richtig eingesetzt. Andernfalls passe die Umrißlinie an.

<img alt="" src=images/Draft_Move_backgrounds_outline.svg  style="width:" height="128px;"> 
*Testen des Symbols vor der dunkelsten und der hellsten Farbe als Hintergrund*

   
  Mein Symbol ist kaum sichtbar.   Du hast einen schlechten Formkontrast. Überprüfe den Umriss und die Hervorhebung. Wahrscheinlich fehlt eines der beiden Elemente oder ist nicht richtig angewendet.
   



### Prüfung Deines Kontrastes 

1.  Exportiere dein Symbol von SVG in ein Bitmap Format, wie `.png` oder `.jpg`.
2.  Lade dein Bitmap in ein Bildprogramm und ändere es in Graustufen. In GIMP würdest du zu **Bild → Modus→ Graustufen** gehen.
3.  Inkscape erlaubt dir das SVG direkt mit **Erweiterungen → Farbe → Graustufen** in Graustufen umzuwandeln.
4.  Kannst du die internen Details noch klar erkennen? Sehr gut. Der Kontrast ist gut.

Ein Graustufenbild erlaubt dir Kontrastprobleme leichter zu erkennen, da nur eine Mischung aus Schwarz und Weiß vorhanden ist. Das Testen von Graustufenbildern ist auch für farbenblinde Benutzer von Vorteil. Wenn sie die Details in einem Graustufenbild erkennen können, dann ist der Kontrast des vollfarbigen Bildes wahrscheinlich auch gut.

<img alt="" src=images/Draft_Move_contrast_grayscale.svg  style="width:" height="128px;"> 
*Prüfung des Symbolkontrasts in Graustufen*

   
  Ich kann nicht alle Details ausmachen.   Die von Ihnen gewählten Farben haben einen schlechten Wertkontrast. Versuche, Farben zu verwenden, die in deiner 4 Ton Palette weiter voneinander entfernt sind, d. h. ein helles Grün neben einem hellen Gelb wird schwer zu erkennen sein.



---
⏵ [documentation index](../README.md) > [Artwork](Category_Artwork.md) > [Developer Documentation](Category_Developer%20Documentation.md) > Artwork Guidelines/de
