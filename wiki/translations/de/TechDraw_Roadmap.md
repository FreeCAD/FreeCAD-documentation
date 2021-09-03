 <img alt="" src=images/preferences-techdraw.svg  style="width:64px;"> \_\_NOTOC\_\_

Die [TechDraw Arbeitsbereich](TechDraw_Workbench/de.md) wurde offiziell als Teil von FreeCAD in der Version 0.17 eingeführt. Sie ist relativ neu und hat noch nicht die Jahre der Entwicklung hinter sich, von denen einige andere Arbeitsbereich profitiert haben. Dennoch erfüllt TechDraw nun sein ursprüngliches Konstruktionsziel und kann nun \"grundlegende technische Zeichnungen auf der Grundlage des 3D Modells erstellen\".

Hier ist ein grober Fahrplan der Bereiche, die in Zukunft angegangen werden sollen (in keiner bestimmten Reihenfolge).

### Aktuelle Aktivität {#aktuelle_aktivität}

-   Fehlerbehebungen in Vorbereitung auf die Version 0.19
-   Anwendungsprobleme in Vorbereitung auf die Version 0.19

### Demnächst

-   Noch zu definieren

### Jüngste Änderungen {#jüngste_änderungen}

-   siehe unten

## Änderungen für v0.19 {#änderungen_für_v0.19}

Siehe auch <https://forum.freecadweb.org/viewtopic.php?f=10&t=34586&hilit=release+notes#p290433>

### Ansichtsoptionen

Die Fähigkeit, eine Ansicht aus einem 3D Fenster oder aus einer vorhandenen 2D Geometrie zu erstellen.
\'\'\'- eine experimentelle Version der Erstellung einer Ansicht aus dem 3D Fenster (Aktive Ansicht einfügen) wurde eingeführt. Sie funktioniert, muss aber noch weiterentwickelt werden.

### Normeneinhaltung

TechDraw entspricht keinem Standard vollständig. Die Fähigkeit, einen Zeichnungsstandard auszuwählen und die verschiedenen Eigenheiten zu respektieren, ist erforderlich.
\'\'\'- dank \@tpavlicek werden die Abmessungen nach einem ausgewählten Standard und Stil formatiert.

### GD&T, Kontrollrahmen, Symbole {#gdt_kontrollrahmen_symbole}

Dieser Bereich der TD ist schwach und muss aufgerüstet werden.
\'\'\'- dank an \@fjullien, \@reox und anderen wurde die Ballonfunktion verbessert, um die Basisfunktionalität in diesem Bereich zu ermöglichen.

### Zeichnungswerkzeuge

Dies schließt auch die Möglichkeit, Ansichten mit Bezugslinien, Textfeldern und Detail Hervorhebungen zu versehen, ein. Dies ist eine Voraussetzung für viele Verbesserungen, insbesondere im Bereich der Zeichnungsanmerkungen, wie z.B. Funktionskontrollrahmen und Referenzhervorhebungen für Detailansichten.
Führungslinien, eine Textformatierte Hervorhebungen, Schweißsymbole, kosmetische Knotenpunkte sowie Kanten und Mittellinien wurden hinzugefügt.
\'\'\'- einzelne Linien können nun ausgeblendet, eingefärbt oder gestylt werden.

### 2D Geometrie {#d_geometrie}

Eine Reihe von 2D Geometriefunktionen wurde vor kurzem dem Part Modul hinzugefügt. Dies muss überprüft werden, um den benutzerdefinierten 2D Geometriecode in TechDraw durch den Standardcode von Part zu ersetzen.
\'\'\'- diese 2D Funktionen werden in den neuen standardkonformen Abmessungen verwendet.

### \"nicht-Knoten\" Abmessungen {#nicht_knoten_abmessungen}

Es besteht ein Bedarf an Abmessungen, die sich nicht auf bestimmte Knoten/Kanten beziehen, sondern auf die Extrema der Abbildung - zum Beispiel Gesamtbreite/-höhe. Auch die Möglichkeit, Bemaßungen ausschließlich auf der Grundlage des 3D Modells zu erstellen, selbst wenn es keine entsprechende projizierte Geometrie gibt.
\'\'\'- Ausdehnungsabmessungen ermöglichen die Erstellung einer Abmessung, die die links/rechts oder oben/unten Ausdehnung einer Sammlung von Kanten oder Flächen abdeckt.

## Zukünftiges

### Navigationsmodelle

TechDraw unterstützt nicht die verschiedenen Navigationsmodelle, die im Rest von FreeCAD verwendet werden (CAD, Blender usw.).

### HLR gegen Flächenokklusion {#hlr_gegen_flächenokklusion}

TechDraw PartViews verwendet die OCC Algorithmen zur Entfernung verdeckter Linien, um die Form zu projizieren. HLR ist rechenintensiv, und einige (viele? die meisten?) Ansichten erfordern keine Anzeige verdeckter Linien. Eine neue Methode zur Erzeugung von Ansichten ist erforderlich. Dazu kann es erforderlich sein, das Bild direkt von der 3D Anzeige zu erhalten.

### Entwurf/Arch Koexistenz {#entwurfarch_koexistenz}

Es gibt Inkonsistenzen zwischen der Art und Weise, wie die Module Draft/Arch und TechDraw Formen darstellen. Dies schränkt die Eignung von TechDraw für Draft/Arch Anwender ein. Ein bemerkenswerter Mangel ist, dass TechDraw nicht in der Lage ist, Bemaßungen auf die Svg Bilder anzuwenden, die es von Draft/Arch erhält.

### Vorlagen

Die Erstellung einer Vorlage mit editierbaren Textfeldern erfordert erhebliches Fachwissen mit [SVG](SVG.md) und einem SVG Editor wie Inkscape. Die Vereinfachung des Erstellungsprozesses von Vorlagen wird eine Priorität im Entwicklungszyklus der Version 0.18 sein.

### Fehlerbehebungen/Funktionsforderungen

Siehe Bugtracker für aktuelle Informationen.


{{TechDraw Tools navi

}}  

[Category:User Documentation{{\#translation:}}](Category:User_Documentation.md) [Category:TechDraw{{\#translation:}}](Category:TechDraw.md)
