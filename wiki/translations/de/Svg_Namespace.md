# Svg Namespace/de
**Entwicklung des Arbeitsbereichs [Drawing](Drawing_Workbench/de.md) wurde in FreeCAD v0.16 gestoppt und der neue in v0.17 eingeführte Arbeitsbereich [TechDraw](TechDraw_Workbench/de.md) zielt darauf ab, ihn zu ersetzen. Beide Arbeitsbereiche wurden von v0.17 bis v0.20 bereitgestellt, aber ab FreeCAD v0.21 ist der Arbeitsbereich Drawing nicht mehr enthalten.**


{{Message|Zurzeit verwendet der Arbeitsbereich TechDraw noch das Attribut '''freecad:EditableText''' und die zugehörige Namensraum-Angabe in den aktuellen Vorlagen.}}






## Einleitung

FreeCAD kann [SVG](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics)-Dokumente importieren und exportieren, die Code enthalten, der zu einem bestimmten **Namensraum** gehört, der eine Untermenge der XML-Befehle ist.

Wie alle XML-Dokumente enthält auch ein SVG-Dokument zwei Abschnitte:

-   [Kopf](#Kopf.md) (Head): eine einzelne Zeile, die angibt, welche Version der Sprache XML für die Befehle im Körper dieses Dokuments verwendet wird.
-   [Körper](#Körper.md) (Body): eine Liste von Befehlen. SVG-Dokumente schließen alle Befehle in {{Incode|<svg>}}-Tags (Markierungen) ein.

:   Der öffnende Tag enthält Informationen über die (Zeichenblatt-) Größe und den verwendeten SVG-Namensraum.



## Standard-Namensraum 

Der von FreeCAD verwendete Standard-SVG-Namensraum wird mit dieser Zeile angegeben:


{{Code|lang=xml|code=
xmlns="http://www.w3.org/2000/svg" version="1.1"
}}

Die externe Verknüpfung verweist auf eine Webseite, die Informationen über den Namensraum und den zugehörigen Befehlen enthält. Attribute dieses Namensraumes werden ohne Präfix verwendet.



## Namensraum-Erweiterung 

Attribute die im SVG-Namensraum (namespace) fehlen, können als Namensraum-Erweiterungen hinzugefügt werden. FreeCAD verwendet solche Erweiterungen für Zeichnungsvorlagen. Die dazugehörige Namensraum-Angabe, die verwendet wird, um das Präfix {{Value|freecad:}} einzuführen, verweist auf **diese Seite**:


{{Code|lang=xml|code=
xmlns:freecad="http://www.freecad.org/wiki/index.php?title=Svg_Namespace"
}}

Die Verknüpfung wird nicht zum Abrufen von Informationen oder Werten zur Laufzeit verwendet, sondern als ein Schlüssel zum Aktivieren der speziellen Attribute.



### TechDraw-Vorlagen und Zeichnungselemente 

Der Arbeitsbereich TechDraw verwendet SVG-Vorlagen zum Erstellen von Zeichnungen. Er kann keine Vorlagen erstellen und exportieren, benötigt aber extern erstellte Vorlagen mit manuell eingefügten Attributen:

-   [freecad:EditableText](#freecad_EditableText.md) ermöglicht bearbeitbare Einträge in Schriftfeldern.
-   [freecad:autofill](#freecad_autofill.md) ({{Version/de|1.0}}) zum obigen hinzugefügt, markiert den Text für die automatische Eingabe während der Vorlagenerstellung.

Zeichnungselemente (symbols) sind eine weitere Art der SVG-Dateien, die in Zeichnungen verwendet werden können, z.B. als stempelartige Beschriftungen. Sie müssen ebenfalls extern erstellt werden und können auch die oben genannten Attribute verwenden.



### Umzug nach freecad.org 

Vor dem Umzug des FreeCAD-Wikis, inklusive **dieser Seite**, von **freecadweb.org** nach **freecad.org** in der Version 0.21 hieß die Verknüpfung zu dieser Seite :

**xmlns:freecad=\"http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace\"**

Aktualisierte TechDraw-Vorlagen enthalten jetzt einen Schlüssel, der die speziellen Attribute nicht aktivieren kann, wenn sie mit FreeCAD {{VersionMinus/de|0.20}} verwendet werden; als Ergebnis werden die editierbaren Texte der aktuellen Vorlagen nicht erkannt und daher als einfache Texte behandelt.

:   In solchen Fällen muss \"web\" von Hand wieder in die Namensraum-Angabe der Vorlage eingefügt werden.

Es scheint so, als könne die {{VersionPlus/de|0.21}} mit beiden verknüpften Adressen umgehen.



## Anwendung


<div class="mw-collapsible mw-collapsed toccolours">



### Kurze Zusammenfassung der SVG-Datei 


<div class="mw-collapsible-content">

TechDraw-Vorlagen sind SVG-Dateien, die eingesetzt werden, um die Grundstruktur einer technische Zeichnungen in FreeCAD bereitzustellen, während Symbole grafische Beschriftungselemente hinzufügen.

Das SVG-Format ist eine Untermenge des XML-Formats. Deshalb besteht eine SVG-Datei, wie jede XML-Datei, aus zwei Teilen:

-   Einem **Kopf** (Head), der Angaben zum verwendeten Format macht.
-   Einem **Körper** (Body), der die Informationen enthält, was dargestellt wird und wo es platziert wird.



#### Kopf

Der Kopf besteht aus nur einer Zeile zur Angabe der Version der XML-Sprache, die verwendet werden soll, um die im Körper befindlichen Anweisungen zu verarbeiten.


{{Code|lang=xml|code=
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
}}



#### Körper

Der Körper einer SVG-Datei beginnt mit einem öffnenden {{Incode|<svg>}}-Tag, das Informationen zu Namensräumen enthält sowie zur Größe der Vorlage und wo sie platziert wird. Am Ende befindet sich ein schließender {{Incode|</svg>}}-Tag. Alle Anweisungen zum Erstellen und Bearbeiten von Geometrie- und Textelementen werden zwischen den beiden Tags eingefügt.


{{Code|lang=xml|code=
<svg
  xmlns="http://www.w3.org/2000/svg" version="1.1"
  width="420mm"
  height="297mm"
  viewBox="0 0 420 297">
</svg>
}}

Die Tags können Attribute enthalten, die die Elemente zwischen den öffnenden und schließenden Tags steuern:

:   **xmlns=**\"<http://www.w3.org/2000/svg>\": Externe Verknüpfung zu dem XML-Namensraum, der die normalen XML-Anweisungen beschreibt.
:   **version=**\"1.1\": Die Anweisungen, der XML-Version 1.1 werden verwendet.
:   **width=**\"420mm\": Länge (Breite) des Zeichnungsblattes.
:   **height=**\"297mm\": Höhe des Zeichnungsblattes.
:   **viewBox=**\"0 0 420 297\": Position der linken oberen Ecke (0;0) und der rechten unteren Ecke (420;297) im SVG-Konstruktionsraum (in SVG-Einheiten).

Die Kombination von {{Incode|width}}, {{Incode|height}} und {{Incode|viewBox}} legt **1 SVG-Einheit = 1 mm** für das gesamte Dokument fest, um maßstabsgetreues Drucken zu ermöglichen, d.h. alle Abmessungen in SVG-Einheiten werden als Millimeter angesehen und die Angabe einer Maßeinheit kann ab diesem Punkt entfallen. (Die Beispielwerte legen die Fläche eines A3-Blattes im Querformat fest)


</div>


</div>



### Die FreeCAD-Namensraum-Erweiterung aktivieren 

Zum Aktivieren der [Namensraum-Erweiterung](#Namensraum-Erweiterung.md) muss der Namensraum-Deklaration zu den Attributen des öffnenden {{Incode|<svg>}}-Tags hinzugefügt werden. Dies ergibt eine Grundstruktur für eine Vorlagendatei, ein leeres A3-Blatt im Querformat, das für {{Incode|freecad:}}-[Attribute](#Attribute.md) vorbereitet ist:


{{Code|lang=xml|code=
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
  xmlns="http://www.w3.org/2000/svg" version="1.1"
  xmlns:freecad="http://www.freecad.org/wiki/index.php?title=Svg_Namespace"
  width="420mm"
  height="297mm"
  viewBox="0 0 420 297">
</svg>
}}



## Attribute

Mit [ aktiviertem FreeCAD-Namensraum](#Die_FreeCAD-Namensraum-Erweiterung_aktivieren.md) können jetzt folgende {{Incode|freecad:}}-Attribute in den öffnenden {{Incode|<text>}}-Tags im SVG-Dokument eingesetzt werden:

### freecad:editable

Das Attribut freecad:editable wird eingesetzt, um bearbeitbare Texte in SVG-Dateien zu kennzeichnen. Der Wert dieses Attributs kann geändert werden:

-   mit dem Dialog \"Bearbeitbaren Texteintrag ändern\".
-   durch Bearbeiten der in der Eigenschaft Editable Texts der Symbole enthaltenen Liste.

Vorgabetexte müssen mit tspan-Tags eingerahmt werden, andernfalls wird der in den Vorlagen/Symbolen angezeigte Text nicht mit geänderten variablen Inhalten synchronisiert.

Beispiel:

 xml
<text freecad:editable="MyTitleText">
    <tspan>This is a title</tspan>
</text>


### freecad:autofill


{{Version/de|1.0}}

: Kennzeichnet einen bearbeitbaren Text in einer Vorlage für automatisches Ausfüllen, wenn eine Vorlage eingefügt wird. (Dies wird einem vorhandenen Attribut freecad:editable hinzugefügt)

Beispiel:

 xml
<text freecad:editable="MyTitleText"; freecad:autofill="AutofillElement" >
    <tspan>This is a title</tspan>
</text>


Die folgenden \"AutofillElements\" sind bisher implementiertyet:

1.  freecad:autofill=\"author\" fügt den Wert von BaseApp/Preferences/Document/prefAuthor ein.
2.  freecad:autofill=\"date\" fügt das aktuelle Datum mit currentDateTime() ein.
3.  freecad:autofill=\"organization\" fügt den Wert von BaseApp/Preferences/Document/prefCompany ein.
4.  freecad:autofill=\"scale\" fügt die Eigenschaft page scale ein.
5.  freecad:autofill=\"sheet\" Fügt Seitennummer/Anzahl der Seiten ein.
6.  freecad:autofill=\"title\" fügt den Wert der Eigenschaft Label des aktuellen Dokuments ein.


<div class="mw-collapsible mw-collapsed toccolours">



### Kurze Zusammenfassung zum Umgang mit Text 


<div class="mw-collapsible-content">

Die obigen Beispiele sind nicht komplett, da ihr Fokus nur auf den {{Incode|freecad:}}-Attributen liegt, aber Text braucht mehr Angaben, um an der gewünschten Stelle in einem bestimmten Stil und wahlweise gedreht dargestellt zu werden.

Attribute können weggelassen werden; dadurch werden Standardwerte verwendet. Dies verbessert die Lesbarkeit und ergibt eine ziemlich kurze und einfach zu wartende Datei.

Jede Text-Zeichenfolge wird zwischen {{Incode|<text>}}- und {{Incode|</text>}}-Tags eingebettet. Ein bearbeitbarer Text muss außerdem zwischen {{Incode|<tspan>}}- und {{Incode|</tspan>}}-Tags eingebettet werden, andernfalls wird er sich nicht bearbeitetn lassen.

Texte werden normalerweise bei {{Value|0;0}} eingefügt. Um den Text an der gewünschten Stelle zu positionieren, werden die Koordinaten des Ankerpunktes {{Incode|x}} und {{Incode|y}} in den {{Incode|<text>}}-Tag eingefügt. Nicht vergessen, dass die Y-Richtung in SVG-Dateien nach unten verläuft.

Es wird empfohlen, Texte, die mehrere gemeinsame Eigenschaften besitzen, zu gruppieren (d.h. Text zwischen {{Incode|<g>}} und {{Incode|</g>}}-Tags einzubetten). Auf diese Weise können gemeinsame Attribute im Gruppen-Tag {{Incode|<g>}} festgelegt werden, während individuelle Attribute im {{Incode|<text>}}-Tag festgelegt werden. Eingebettete Text-Attribute überschreiben umgebende Gruppen-Attributte.

Beispiel:


{{Code|lang=xml|code=
<g id="text-non-editable"
  font-family="osifont"
  font-size="10"
  text-anchor="start">
    <text x="10" y="20">A simple text</text>
    <text x="10" y="40" font-color:"blue">another simple text</text>
</g>
}}

In diesem Beispiel werden beide gruppierte Texte in der Schriftart osifont mit 10 mm Schrifthöhe dargestellt und mit ihren Ankerpunkten am ersten Zeichen. Der erste wird schwarz eingefärbt (Standardfarbe), der zweite blau.


{{Code|lang=xml|code=
<g id="text-editable"
  style="font-family:osifont; font-size:15; text-anchor:start; fill:blue">
    <text freecad:editable="Text1" x="50" y="40">  <tspan>Editable text in blue</tspan>. </text>
    <text freecad:editable="Text2" x="50" y="60" fill="red" text-anchor="middle">
        <tspan>Centered editable text in red</tspan>
    </text>
    <text freecad:editable="Text3" x="50" y="80" transform="rotate(90,50,80)>
        <tspan>Rotated editable text in blue</tspan>
    </text>
</g>
}}

In Diesem Beispiel werden alle drei gruppierten bearbeitbaren Texte in der Schriftart osifont mit 15 mm Schrifthöhe blau dargestellt und mit ihren Ankerpunkten am ersten Zeichen. Text2 hat die abweichende Farbe Rot und den Ankerpunkt in der Mitte, Text3 ist um 90° im Uhrzeigersinn gedreht, wobei sich Drehpunkt und Ankerpunkt an derselben Stelle befinden.

die Beispiele verwenden zwei unterschiedliche Arten die Eigenschaften der Schrift festzulegen; separate Attribute im ersten und in einem einzigen Style-Attribut kombiniert im zweiten Beispiel.

Es wird empfohlen das ID-Attribut im Gruppen-Tag dafür einzusetzen, die Art der Elemente zu beschreiben, die gruppiert werden.

Transform-Attribute funktionieren mit allen Texten, aber bearbeitbare Texte verlieren die Verbindung zu Bearbeitungsmarken (standardmäßig blaue Unterstriche), da diese der Bewegung des Textes nicht folgen. Daher können einfache Texte mit Schriftfeld-Geometrie gruppiert werden und mit einer einzigen Verschiebung bewegt werden, aber bearbeitbare Texte müssen einzeln positioniert werden. Drehungen mit deckungsgleichen Anker- und Drehpunkten können, im Gegensatz zu anderen Transformationen, sicher in {{Incode|<text>}}-Tags eigesetzt werden, da Text und Bearbeitungsmarke sich dann nicht auseinanderbewegen.


</div>


</div>



### Code-Beispiel für freecad:editable 



#### 1 : Feldüberschrift, nicht änderbar (Title without textedit) 

<img alt="" src=images/Svg_Namespace_01.png  style="width:300px;">

 xml
  <g
     id="g3587">
    <text
       sodipodi:linespacing="119.00001%"
       id="text3482"
       y="229.10912"
       x="220.8476"
       style="font-size:1.97555566px;font-style:normal;font-weight:normal;line-height:119.00000572%;letter-spacing:0.01975556px;word-spacing:0.00846667px;writing-mode:lr-tb;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans;-inkscape-font-specification:Sans"
       xml:space="preserve"><tspan
         y="229.10912"
         x="220.8476"
         id="tspan3484"
         sodipodi:role="line">AUTHOR NAME :</tspan></text>




#### 2 : Feldeintrag, bearbeitbar (Title with textedit) 

<img alt="" src=images/Svg_Namespace_02.png  style="width:300px;">

 xml
  <g
     style="fill:none;stroke:#000000;stroke-width:0.13;stroke-linecap:butt;stroke-linejoin:miter"
     id="g578-7"
     transform="translate(0,4)">
    <text
       xml:space="preserve"
       style="font-size:4px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:sans;-inkscape-font-specification:sans"
       x="220.9935"
       y="228.95425"
       id="text3331"
       sodipodi:linespacing="125%"
       freecad:editable="AuthorName"><tspan
         sodipodi:role="line"
         id="tspan3333"
         x="220.9935"
         y="228.95425">AUTHOR NAME</tspan></text>
    <text
    ...
    ...
    ...
    ... </text>
  
  </g>




#### Erklärungen

 xml
  <g


Beginn der Gruppierung

 xml
     style="fill:none;stroke:#000000;stroke-width:0.13;stroke-linecap:butt;stroke-linejoin:miter"
     id="g578-7"
     transform="translate(0,4)">


Zur Gruppierung gehörige Daten

 xml
    <text


Beginn des Textblockes

 xml
       xml:space="preserve"
       style="font-size:4px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:sans;-inkscape-font-specification:sans"


Alle Informationen über den Text, der angezeigt wird (Textattribute)

 xml
       x="220.9935"
       y="228.95425"
       id="text3331"
       sodipodi:linespacing="125%"


Koordinaten des Textes (wo dieser angezeigt wird) und eine Benennung (ID)

 xml
       freecad:editable="AuthorName"><tspan


Hier ist **AuthorName** die Variable, die durch **freecad:editable** verwaltet wird und die bearbeitbare Zeichenkette (string) speichert, die angezeigt wird.

 xml
         sodipodi:role="line"
         id="tspan3333"
         x="220.9935"
         y="228.95425">AUTHOR NAME</tspan></text>


Koordinaten und Benennung (ID) des Textes, der als Vorgabe angezeigt wird. **** schließt den text-Block.

 xml
    <text
    ...
    ...
    ...
    ... </text>
  </g>


Weitere text-Blöcke und das End-Tag **** der Gruppierung der text-Blöcke.

Es ist möglich, dass nach dem Bearbeiten der Inkscape-SVG-Datei die Datei nicht mehr funktioniert. Möglicherweise sind Informationen verlorengegangen.

Dann muss geprüft werden, ob der bearbeitbare Text geändert wurde.

Beispiel:

-   **editable** = \"AuthorName\"
-   wird ersetzt durch **freecad:editable** = \"AuthorName\"


{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [Poweruser_Documentation](Category_Poweruser_Documentation.md) > [Developer](Category_Developer.md) > [Python_Code](Category_Python_Code.md) > [Macros](Category_Macros.md) > [TechDraw](Category_TechDraw.md) > Svg Namespace/de
