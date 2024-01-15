# Svg Namespace/de
**Entwicklung des Arbeitsbereichs [Drawing](Drawing_Workbench/de.md) wurde in FreeCAD v0.16 gestoppt und der neue in v0.17 eingeführte Arbeitsbereich [TechDraw](TechDraw_Workbench/de.md) zielt darauf ab, ihn zu ersetzen. Beide Arbeitsbereiche wurden von v0.17 bis v0.20 bereitgestellt, aber ab FreeCAD v0.21 ist der Arbeitsbereich Drawing nicht mehr enthalten.**


{{Message|Zurzeit verwendet der Arbeitsbereich TechDraw noch das Attribut '''freecad:EditableText''' und die zugehörige Namensraum-Angabe in den aktuellen Vorlagen.}}






## Einleitung

FreeCAD kann [SVG](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics)-Dokumente importieren und exportieren, die Code enthalten, der zu einem bestimmten **Namensraum** gehört, der eine Untermenge der XML-Befehle ist.

Wie alle XML-Dokumente enthält auch ein SVG-Dokument zwei Abschnitte:

-   Kopf (Head): eine einzelne Zeile, die angibt, welche Version der Sprache XML für die Befehle im Körper dieses Dokuments verwendet wird.
-   Körper (Body): eine Liste von Befehlen. SVG-Dokumente schließen alle Befehle in<svg>-Tags (Markierungen) ein.

:   Der öffnende Tag enthält Informationen über die (Zeichenblatt-) Größe und den verwendeten SVG-Namensraum.



## Standard-Namensraum 

Der von FreeCAD verwendete Standard-SVG-Namensraum wird mit dieser Zeile angegeben:


{{Code|lang=xml|code=
xmlns="http://www.w3.org/2000/svg" version="1.1"
}}

Die externe Verknüpfung verweist auf eine Webseite, die Informationen über den Namensraum und den zugehörigen Befehlen enthält. Attribute dieses Namensraumes werden ohne Präfix verwendet.



## Namensraum-Erweiterung 

Attribute, die dem SVG-Namensraum fehlen, können durch Namensraum-Erweiterungen hinzugefügt werden. FreeCAD verwendet so eine Erweiterung für Zeichnungsvorlagen. Vorlagen für den Arbeitsbereich Drawing verwendeten vier spezielle Attribute, die mit einem Präfix \"freecad:\" markiert werden:

-   [freecad:EditableText](#freecad_EditableText.md), Dieses wird noch immer von Vorlagen für den ArbeitsbereichTechDraw verwendet.
-   [freecad:basepoint1](#freecad_basepoint1.md)
-   [freecad:basepoint2](#freecad_basepoint2.md)
-   [freecad:dimpoint](#freecad_dimpoint.md)

Eine Namensraum-Angabe wird verwendet, um das Präfix einzuführen und auf die zugehörige Webseite, **diese Seite**, zu verweisen:


{{Code|lang=xml|code=
xmlns:freecad="http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace"
}}

Die Verknüpfung wird nicht zum Abrufen von Informationen oder Werten zur Laufzeit verwendet, sondern als ein Schlüssel zum Aktivieren der speziellen Attribute.



### Drawing-Vorlagen 

In den [SVG](http://de.wikipedia.org/wiki/Scalable_Vector_Graphics)-Dokumenten, die aus FreeCADs Arbeitsbereich [Drawing](Drawing_Workbench/de.md) exportiert wurden und als (Drawing-) Zeichnungs-[Vorlagen](Drawing_templates/de.md) (templates) eingesetzt werden, können die speziellenAttribute ([Attributes](http://www.w3schools.com/xml/xml_attributes.asp)) verwendet werden; ursprünglich für den internen Gebrauch in FreeCAD selbst, können sie zukünftig auch durch andere Anwendungen im FreeCAD-Umfeld verwendet werden. Diese Attribute nutzen alle dasNamensraum-Präfix **freecad:** (Siehe [namespace prefix](http://www.w3schools.com/xml/xml_namespaces.asp)). Die URL des Namensraumes, die in diesen SVG-Dokumenten vorgegeben ist, bezieht sich auf diese Seite.

:   Der Arbeitsbereich Drawing ist nicht länger in FreeCAD {{VersionPlus/de|0.21}} enthalten, daher sind diese Drawing-Vorlagen jetzt veraltet.



### TechDraw-Vorlagen 

Der Arbeitsbereich TechDraw verwendet auch SVG-Vorlagen, kann diese aber keine Vorlagen erstellen und exportieren. Er benötigt das Attribut [freecad:EditableText](#freecad_EditableText.md) für Eingaben in Schriftfeldern.



### Umzug nach freecad.org 

Seit das FreeCAD-Wiki, inklusive **dieser Seite**, in der Version 0.21 von **freecadweb.org** nach **freecad.org** umgezogen ist, muss die Verknüpfung entsprechend angepasst werden zu:


{{Code|lang=xml|code=
xmlns:freecad="http://www.freecad.org/wiki/index.php?title=Svg_Namespace"
}}

Aktualisierte TechDraw-Vorlagen enthalten jetzt einen Schlüssel, der die speziellen Attribute nicht aktivieren kann, wenn sie mit FreeCAD {{VersionMinus/de|0.20}} verwendet werden; als Ergebnis werden die editierbaren Texte der aktuellen Vorlagen nicht erkannt und daher als einfache Texte behandelt.

:   In solchen Fällen muss \"web\" von Hand wieder in die Namensraum-Angabe der Vorlage eingefügt werden.

Es scheint so, als könne die {{VersionPlus/de|0.21}} mit beiden verknüpften Adressen umgehen.



## Anwendung

Ein Pixel = ein Millimeter.

An irgendeiner Stelle im SVG-Code muss angegeben werden, wo sich die Inhalte der Zeichnung befinden sollen, z.B. am Ende der Datei, direkt vor dem letzten \'\'\'


</svg>

\'\'\' tag. Die folgende Zeile:

 xml



 xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
    xmlns:freecad="http://www.freecadweb.org/wiki/index.php?title=Svg_Namespace"


Um das Bedrucken der Skalen zu ermöglichen, muss die tatsächliche Wortgröße in den Attributen \'Breite\' und \'Höhe\' des SVG-Tags angegeben werden. Die Größe des Dokumentes in Benutzereinheiten (px) muss im viewBox-Attribut angegeben werden.

Das Folgende muss wie im nachfolgenden Beispiel formattiert werden:

-   xxx = Pixel-Breite
-   yyy = Pixel-Höhe

 xml
width="xxxmm"
height="yyymm"
viewBox="0 0 xxx yyy"


Zusätzliche Informationen zum Arbeitsbereich (Working space) und dem Titelblock können eingefügt werden und werden auf der Seite [Zeichnungsvorlagen](Drawing_templates/de.md) vorgegeben.



## Attribute



### [freecad:EditableText](#Code-Beispiel_für_freecad_EditableText.md)

Um **freecad:**-Attribute im SVG-Dokumenten zu nutzen, muss der FreeCAD-Namensraum als Attribut des öffnenden


<svg>

-Tags definiert werden.

Dieses beschreibt einen Text in einer Vorlage, der mit FreeCAD bearbeitet werden kann.

Beispiel:

 xml
<text freecad:EditableText="MyTitleText">
    <tspan>This is a title</tspan>
</text>




### freecad:basepoint1 (Basispunkt 1) 

Legt den ersten Basispunkt eines [Draft Maßes](Draft_Dimension/de.md) (Dimension-Objekt) fest (in einem SVG-Dokument als Gruppe dargestellt). Dieses Attribut wird verwendet, wenn das SVG-Teilstück (Fragment) in FreeCAD importiert wird, um das \'Dimension\'-Objekt neu zu erzeugen/zu ändern. Die Gruppe enthält Pfade und andere graphische Elemente, um das Maß (Dimension-Objekt) in anderen SVG-Anwendungen richtig wiederzugeben.

Beispiel:

 xml
<g freecad:basepoint1="0.5 4.34" freecad:basepoint2="2.4 5.8" dimpoint="3.2 7.76">
    <path d="...">
</g>




### freecad:basepoint2 (Basispunkt 2) 

Legt den zweiten Basispunkt des [Draft Maßes](Draft_Dimension/de.md) (Dimension-Objekt) fest (in einem SVG-Dokument als Gruppe dargestellt). Dieses Attribut wird verwendet, wenn das SVG-Teilstück (Fragment) in FreeCAD importiert wird, um das \'Dimension\'-Objekt neu zu erzeugen / zu ändern. Die Gruppe enthält Pfade und andere graphische Elemente, um das Maß (Dimension-Objekt) in anderen SVG-Anwendungen richtig wiederzugeben.

Beispiel: siehe [freecad:basepoint1](#freecad_basepoint1.md)

### freecad:dimpoint

Legt den Punkt eines [Draft Maßes](Draft_Dimension/de.md) (Dimension-Objekt) fest, durch den die Maßlinie läuft. Dieses Attribut wird verwendet, wenn das SVG-Teilstück (Fragment) in FreeCAD importiert wird, um das \'Dimension\'-Objekt neu zu erzeugen/zu ändern. Die Gruppe enthält Pfade und andere graphische Elemente, um das Maß (Dimension-Objekt) in anderen SVG-Anwendungen richtig wiederzugeben.

Beispiel: siehe [freecad:basepoint1](#freecad_basepoint1.md)



### Code-Beispiel für freecad:EditableText 

Diese Beispiel zeigt Schriftfeldeinträge auf einem Zeichnungsblatt im Format [A3_Landscape](Misc_templates#A3_Landscape_US_Text_Complet_With_Convention_US.md)



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



## Andere, verfügbare Attribute 

Siehe [Drawing Vorlagen](Drawing_templates/de.md)


{{Drawing Tools navi

}}



---
⏵ [documentation index](../README.md) > [Poweruser_Documentation](Category_Poweruser_Documentation.md) > [Developer](Category_Developer.md) > [Python_Code](Category_Python_Code.md) > [Macros](Category_Macros.md) > [Drawing](Category_Drawing.md) > Svg Namespace/de
