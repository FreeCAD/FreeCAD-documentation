# Svg Namespace/de
**Entwicklung des [Zeichnung Arbeitsbereich](Drawing_Workbench/de.md) wurde in FreeCAD v0.16 gestoppt und der neue in v0.17 eingeführte [TechDraw Arbeitsbereich](TechDraw_Workbench/de.md) zielt darauf, ihn zu ersetzen. Beide Arbeitsbereiche werden in v0.17 bereitgestellt, aber der Zeichnung Arbeitsbereich könnte in zukünftigen Ausgaben entfernt werden.**


{{TOCright}}

In den [SVG](http://de.wikipedia.org/wiki/Scalable_Vector_Graphics)-Dokumenten, die aus FreeCAD\'s [Zeichnungsmodul](Drawing_Workbench/de.md) exportiert wurden und als Seite [Vorlagen (templates)](Drawing_templates/de.md) verwendet werden, können verschiedene anwenderspezifische [Attribute](http://www.w3schools.com/xml/xml_attributes.asp) verwendet werden. Ursprünglich für den internen Gebrauch in FreeCAD, können sie auch durch andere FreeCAD-Applikationen in der Zukunft verwendet werden. All diese Attribute nutzen das **freecad:** [Namensraum](http://www.w3schools.com/xml/xml_namespaces.asp)-Präfix. Die URL des Namensraumes, die in diesen SVG-Dokumenten vorgegeben ist, bezieht sich auf diese Seite.

## Anwendung

1 pixel = 1 mm

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

### [freecad:EditierbarerText](#Example_of_code_freecad_EditableText.md)

Um **freecad:** Attribute im SVG-Dokumenten zu nutzen, muss der FreeCAD Namensraum als Attribut des Eröffnungstags


<svg>

definiert werden.

Dies beschreibt einen Text, der in FreeCAD geändert werden kann.

Beispiel:

 xml
<text freecad:EditableText="MyTitleText">
    <tspan>This is a title</tspan>
</text>


### freecad:basepoint1 (Basispunkt 1) 

Definiert den ersten Basispunkt eines [Entwurf Abmessung](Draft_Dimension/de.md)-Objektes, als Gruppe in einem SVG-Dokument dargestellt. Dieses Attribut wird verwendet, wenn das SVG-Teilstück (Fragment) in FreeCAD importiert wird, um das Objekt \'Dimension\' neu zu erzeugen/zu ändern. Die Gruppe enthält Pfade und andere graphische Punkte, um das Objekt Dimensionen in anderen SVG-Anwendungen richtig wiederzugeben.

Beispiel:

 xml
<g freecad:basepoint1="0.5 4.34" freecad:basepoint2="2.4 5.8" dimpoint="3.2 7.76">
    <path d="...">
</g>


### freecad:basepoint2 (Basispunkt 2) 

Definiert den zweiten Basispunkt des [Entwurf Abmessung](Draft_Dimension/de.md) Objektes, als Gruppe in einem SVG-Dokument dargestellt. Dieses Attribut wird verwendet, wenn das SVG-Teilstück (Fragment) in FreeCAD importiert wird, um das Objekt \'Dimension\' neu zu erzeugen / zu ändern. Die Gruppe enthält Pfade und andere graphische Punkte, um das Objekt Dimensionen in anderen SVG-Anwendungen richtig wiederzugeben.

Beispiel: siehe [freecad:basepoint1](#freecad_basepoint1.md)

### freecad:dimpoint

Definiert den Punkt eines [Entwurf Abmessung](Draft_Dimension/de.md) Objektes, durch den die Bemaßungslinie läuft. Dieses Attribut wird verwendet, wenn das SVG-Teilstück (Fragment) in FreeCAD importiert wird, um das Objekt \'Dimension\' neu zu erzeugen/zu ändern. Die Gruppe enthält Pfade und andere graphische Punkte, um das Objekt Dimensionen in anderen SVG-Anwendungen richtig wiederzugeben.

Beispiel: siehe [freecad:basepoint1](#freecad_basepoint1.md)

### Beispiel eines freecad-Codes:EditierbarerText 

Diese Beispiel wurde von einer Kartusche auf ein Blatt übertragen [A3_Landscape](Misc_templates#A3_Landscape_US_Text_Complet_With_Convention_US.md)

#### 1 : Titel ohne Textbearbeitung (textedit) 

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


#### 1 : Titel mit Textbearbeitung (textedit) 

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


Beginn der Rahmensumbebung (framework)

 xml
     style="fill:none;stroke:#000000;stroke-width:0.13;stroke-linecap:butt;stroke-linejoin:miter"
     id="g578-7"
     transform="translate(0,4)">


Datum (data) in der Rahmensumgebung (framework)

 xml
    <text


Beginn des Textblockes

 xml
       xml:space="preserve"
       style="font-size:4px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:sans;-inkscape-font-specification:sans"


Alle Informationen über den Text, der angezeigt wird

 xml
       x="220.9935"
       y="228.95425"
       id="text3331"
       sodipodi:linespacing="125%"


Koordiniert und identifiziert den Text, wo dieser angezeigt wird

 xml
       freecad:editable="AuthorName"><tspan


Hier ist **AuthorName** die Variable, die durch **freecad:editable** gemanaged wird und den zu ändernden Text (string) speichert, der angezeigt wird.

 xml
         sodipodi:role="line"
         id="tspan3333"
         x="220.9935"
         y="228.95425">AUTHOR NAME</tspan></text>


Koordiniert und identifiziert den vorgegebenen Text, der angezeigt wird. **** ist das Ende des Blockes \'Text\'.

 xml
    <text
    ...
    ...
    ...
    ... </text>
  </g>


Andere Textblöcke und das Ende **** der Rahmensumgebung \'Gruppe Textblöcke\'.

Es ist möglich, dass nach dem Bearbeiten der \'Inkscape SVG-Datei\' die Datei nicht mehr funktioniert. Möglicherweise sind Informationen verloren gegangen.

Prüfen, ob der bearbeitete Text geändert wurde

Beispiel:

-   **editable** = \"AuthorName\"
-   replace by **freecad:editable** = \"AuthorName\"

## Andere, verfügbare Attribute 

Siehe [Zeichnungsvorlagen](Drawing_templates/de.md)


{{Drawing Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Poweruser_Documentation](Category_Poweruser_Documentation.md) > [Developer](Category_Developer.md) > [Python_Code](Category_Python_Code.md) > [Macros](Category_Macros.md) > [Drawing](Category_Drawing.md) > Svg Namespace/de
