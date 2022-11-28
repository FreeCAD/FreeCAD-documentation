# TechDraw Preferences/de
{{TOCright}}

## Einführung

Die Einstellungen des [TechDraw Arbeitsbereichs](TechDraw_Workbench/de.md) befinden sich im [Einstellungseditor](Preferences_Editor/de.md), **Bearbeiten → Einstellungen → TechDraw**.

Alle Eigenschaftseinstellungen mit *kursiven* Beschriftungen sind Standardwerte für neue Zeichnungsobjekte. Sie haben keinen Einfluss auf bestehende Objekte.

## Allgemeines

<img alt="Allgemeine Einstellungen" src=images/TechDraw_PreferencesGeneral.png  style="width   *350px;">

### Zeichnung Aktualisierung 


{{Version/de|0.19}}

-   **Aktualisierung mit 3D**   * Ob die Seiten bei jeder Änderung des 3D-Modells aktualisiert werden oder nicht. Dies ist eine globale Richtlinieneinstellung.
-   **Seitenüberschreibung zulassen**   * Ob die Eigenschaft **[Aktualisiert halten](TechDraw_PageDefault/de#Eigenschaften.md)** einer Seite den globalen Parameter **Aktualisierung mit 3D** überschreiben kann oder nicht. Dies ist eine globale Richtlinieneinstellung.
-   **Seite auf dem neuesten Stand halten**   * Hält Zeichnungsseiten mit Änderungen des 3D-Modells *in Echtzeit* synchron. Dies kann die Reaktionszeit verlangsamen.
-   **Sekundäransichten automatisch verteilen**   * Verteilt automatisch Sekundäransichten für [Projektionsgruppen](TechDraw_ProjectionGroup/de.md).

### Beschriftungen

-   **Beschriftung Schrift**   * Der Name der Standardschriftart für Beschriftungen. Die Schriftart wird auch für neue [Bemaßungen](TechDraw_Preferences/de#Bemaßungen.md) verwendet, sie zu ändern hat keinen Einfluss auf bestehende Bemaßungen
-   **Beschriftung Größe**   * Standardgröße für Beschriftungen.

### Vorgaben

-   **Projektionsmethode**   * Ob eine [Ansichtengruppe](TechDraw_ProjectionGroup/de.md) entweder die europäische (first-angle) Projektion oder die amerikanische (third-angle) Projektion verwenden. Siehe [multiview projection](https   *//en.wikipedia.org/wiki/Multiview_projection#Multiviews) (engl.) (oder [Projektionsmethoden](https   *//de.wikipedia.org/wiki/Normalprojektion#Ansichten)) für eine Erklärung.
-   **Darstellung verdeckter Kanten**   * Der Stil, der für verdeckte Linien zu verwenden ist.

### Dateien

-   **Standardvorlage**   * Standarddatei [Vorlage](TechDraw_Templates/de.md) für neue Seiten.
-   **Vorlagenverzeichnis**   * Startverzeichnis für Werkzeugleistenschaltflächen **<img src="images/TechDraw_PageTemplate.svg" width=16px> [Seite unter Verwendung einer Vorlage einfügen](TechDraw_PageTemplate/de.md)**.
-   **Schraffurmusterdatei**   * Standard [SVG](SVG/de.md) oder [Bitmap](bitmap/de.md) Datei für [Schraffuren](TechDraw_Hatch/de.md).
-   **Liniegruppendatei** Alternative Datei für persönliche [Liniengruppen](TechDraw_LineGroup/de.md) Definitionen.
-   **Schweißverzeichnis**   * Standardverzeichnis für Werkzeugleisten Schaltfläche **[<img src=images/TechDraw_WeldSymbol.svg style="width   *16px"> [Schweißinformationen zur Führungslinie hinzufügen](TechDraw_WeldSymbol/de.md)**. {{Version/de|0.19}}
-   **PAT Datei**   * Standard PAT Musterfestlegungsdatei für [Geometrische Schraffuren](TechDraw_GeometricHatch/de.md).
-   **Mustername**   * Name des Standard PAT Musters.

### Raster

-   **Show Grid**   * Standardeinstellung der Rasteranzeige für neu erstellten Seiten. {{Version/de|0.20}}
-   **Grid Spacing**   * Standardabstand zwischen Rasterlinien auf neu erstellten Seiten. {{Version/de|0.20}}

## Maßstab

<img alt="Maßstabseinstellungen" src=images/TechDraw_PreferencesScale.png  style="width   *350px;">

### Maßstab 

-   **Seitenmaßstab**   * Standardmaßstab für neue Zeichnungen.
-   **Anzeige Maßstabstyp**   * Standardmaßstab für neue Ansichten.
-   **Anzeige Benutzerdefinierter Maßstab**   * Standardmaßstab für Ansichten, wenn **Anzeige Maßstabstyp** *Benutzerdefiniert* ist.

### Größenanpassungen

-   **Knotenmaßstab**   * Größe der [vertex](Glossary#V.md) Punkte. Multiplikator der Linienbreite.
-   **Zentrumsmarkierungsmaßstab**   * Größe der Mittenmarkierungen. Multiplikator der Knotengröße.
-   **Vorlage Bearbeitungsmarkierung**   * Größe des [Vorlagenfelds](TechDraw_Templates/de.md) klicken gehandhabt in mm (grüne Punkte).
-   **Schweißsymbolmaßstab**   * Größenmultiplikator [Schweißsymbole](TechDraw_WeldSymbol/de.md). {{Version/de|0.19}}

## Maßeinträge

<img alt="Einstellungen für Maßeinträge" src=images/TechDraw_PreferencesDimensions.png  style="width   *350px;">

-   **Normbasis und Ausführung von Maßeinträgen**   * Die Norm, die für Maßeinträge zu verwenden ist. Die Unterschiede zwischen den Normen sind in der Abbildung dargestellt   *

![\|500px\|Unterschiede zwischen den unterstützten Normen. ([Image source](images/https   *//forum.freecadweb.org/viewtopic.php?f=35&t=39571#p336144))](TechDraw_Dimension_standardization.png )

   *   

       *   ISO ausgerichtet (ISO Oriented) - gezeichnet gemäß Norm ISO 129-1, Text ist gedreht, um parallel zu der (Tangente an die) Maßlinie zu sein.
       *   ISO mit Hinweislinie (ISO Referencing) - gezeichnet entsprechend der Norm ISO 129-1, Text ist immer horizontal, über der kürzest möglichen Bezugslinie.
       *   ASME eingepasst (ASME Inlined) - gezeichnet gemäß Norm ASME Y14.5M, Text ist horizontal, eingefügt in einer Lücke der Maßlinie (bzw. des \"Maßbogens\" bei Winkeln).
       *   ASME mit Hinweislinie (ASME Referencing) - gezeichnet entsprechend der Norm ASME Y14.5M, Text ist horizontal, an einer Seite mittig mit einer kurzen, mit der Maßlinie verbundenen Bezugslinie versehen.

-   **Globale Dezimalstellen verwenden**   * Verwendet die Anzahl der Dezimalstellen aus dem [Voreinstellungseditor](Preferences_Editor/de#Einheiten.md).
-   **Maßeinheiten anzeigen**   * Fügt die Maßeinheit (mm, in, etc.) hinter den Maßzahlen hinzu.
-   **Dezimalstellen ändern**   * Anzahl der Dezimalstellen, wenn **Globale Dezimalstellen verwenden** nicht ausgewählt ist und unter **Maßzahlenformat** nichts angegeben wurde.
-   **Maßzahlenformat**   * Benutzerdefiniertes Format für Maßzahlen (und -Texte). Verwendet die [printf-Formatierung](https   *//de.wikipedia.org/wiki/Printf).
-   **Schrifthöhe**   * Schriftgröße für Maßzahlen und -Texte.
-   **Skalierung der Toleranzeinträge**   * Schriftgrößenanpassung für Toleranzeinträge. Ein Multiplikator der **[Schrifthöhe](TechDraw_Preferences/de#Bemaßungen.md)**.
-   **Durchmessersymbol**   * Zeichen für die Kennzeichnung von Durchmessermaßen.
-   **Pfeildarstellung**   * Art der Maßpfeile (Maßlinienbegrenzungen).
-   **Pfeillänge**   * Größe der Maßpfeile.
-   **Extension Gap Factor - ISO**   * Lücke zwischen Maßpunkt und Anfang der Maßhilfslinie für ISO-Maße. {{Version/de|1.0}}
-   **Extension Gap Factor - ASME**   * Lücke zwischen Maßpunkt und Anfang der Maßhilfslinie für ASME-Maße. {{Version/de|1.0}}

## Anmerkung

<img alt="Anmerkungseinstellungen" src=images/TechDraw_PreferencesAnnotation.png  style="width   *350px;">

-   **Normbasis für Schnittlinien**   * Norm, die zur Darstellung von Schnittlinien in [Schnittansichten](TechDraw_SectionView/de.md) zu verwenden ist.
-   **Schnittliniendarstellung**   * Linienart der Schnittlinien.
-   **Schnittflächendarstellung**   * Kennzeichnungsart für Schnittflächen. Die Optionen sind   * {{Version/de|0.19}}
    -   *Ausblenden*   * Es gibt keine sichtbare Schnittfläche.
    -   *Farbfüllung*   * Die geschnittene Fläche erhält die für **Schnittfläche** gesetzte Farbe
    -   *SVG-Schraffur*   * Die Schnittfläche wird [schraffiert](TechDraw_Hatch/de.md).
    -   *PAT-Schraffur*   * Die Oberfläche wird [geometrisch schraffiert](TechDraw_GeometricHatch/de.md).
-   **Liniengruppe**   * Eine [Liniengruppe](TechDraw_LineGroup/de.md) zum Festlegen der vorgegebenen Strichstärken.
-   **Umrissform für Detailansichten**   * Form des Detailauswahlrahmens für [Detailansichten](TechDraw_DetailView/de.md).
-   **Linienart für Detailauswahlrahmen**   * Linienart der Detailauswahlrahmen für [Detailansichten](TechDraw_DetailView/de.md). {{Version/de|0.19}}
-   **Mittelliniendarstellung**   * Linienart für [Mittellinien](TechDraw_FaceCenterLine/de.md).
-   **Form des Hinweisfeldes**   * Form des [Hinweisfeldes](TechDraw_Balloon/de.md).
-   **Ende der Linie des Hinweisfeldes**   * Standardsymbol für Hinweislinienenden.
-   **Knicklänge der Linie des Hinweisfeldes**   * Länge der Bezugslinie am Knick der Hinweislinie.
-   **Hinweisfeldes mit rechtwinkligem Dreieck**   * Wenn das **Ende der Linie des Hinweisfeldes** ein *gefülltes Dreieck* ist, kann das Dreieck nur eine vertikale oder horizontale Ausrichtung erhalten, wenn das Hinweisfeld bewegt wird.
-   **Hinweislinie automatisch horizontal**   * Erzwingt, dass das letzte Segment der[Hinweislinie](TechDraw_LeaderLine/de.md) (Bezugslinie) horizontal ist.
-   **Mittelpunktsmarkierungen darstellen**   * Bogenmittenmarkierungen in Ansichten anzeigen.
-   **Mittelpunktsmarkierungen drucken**   * Bogenmittenmarkierungen in der Druckausgabe anzeigen.

## Farben

<img alt="Farbeinstellungen" src=images/TechDraw_Preferences_Colors.PNG  style="width   *350px;">

Einstellung der Standardfarben für neue Zeichnungsblätter   *

-   **Normal**   * Normale Linienfarbe.
-   **Vorausgewählt**   * Vorausgewählte Farbe. Die Farbe, die verwendet wird, um Objekte hervorzuheben, wenn die Maus darüber bewegt wird.
-   **Ausgewählt**   * Farbe für ausgewählte Objekte.
-   **Hintergrund**   * Hintergrundfarbe um Zeichnungsblätter herum.
-   **Maßeintrag**   * Farbe der Linien und Texte für Maßeinträge.
-   **Mittellinie**   * Farbe für [Mittellinien](TechDraw_FaceCenterLine/de.md).
-   **Detailauswahl**   * Linienfarbe für die Umrissform von [Detailansichten](TechDraw_DetailView/de.md). <small>(v0.19)</small> 
-   **Transparente Flächen**   * Wenn angehakt, sind die Objektflächen transparent. Andernfalls wird die eingestellte Farbe für Flächen verwendet. {{Version/de|0.19}}
-   **Verdeckte Kante**   * Farbe der verdeckten Linie. Diese Farbe wird für alle Arten von [Verdeckten Linien](#HLR.md) verwendet.
-   **Schnittfläche**   * Farbe für Schnittflächen in [Schnittansichten](TechDraw_SectionView/de.md). Wird nur verwendet, wenn die Einstellung **Schnittflächendarstellung** auf *Farbfüllung* gesetzt ist.
-   **Schnittlinie**   * Farbe der Schnittlinie einer [Schnittansicht](TechDraw_SectionView/de.md).
-   **Schraffur**   * Farbe für [Schraffuren](TechDraw_Hatch/de.md).
-   **Geometrische Schraffur**   * Farbe für [geometrische Schraffurmuster](TechDraw_GeometricHatch/de.md).
-   **Knoten**   * Farbe der auswählbaren [Knoten](Glossary/de#V.md) in Ansichten.
-   **Hinweislinie**   * Farbe für neue [Hinweislinien](TechDraw_LeaderLine/de.md).
-   **Rasterfarbe**   * Farbe für alle Seitenraster. {{Version/de|0.20}}

## HLR

<img alt="HLR-Einstellungen" src=images/TechDraw_PreferencesHLR.png  style="width   *350px;">

HLR steht für *Entfernen verdeckter Linien* (engl.   * hidden line removal).

-   **Polygon Approximation verwenden**   * Verwendet eine Approximation, um verborgene Linien zu finden. Dies geht schnell, aber das Ergebnis ist eine Sammlung kurzer gerader Linien.
-   **Zeige harte Linien**   * Zeigt harte und Umrisskanten an (sichtbare Linien werden immer angezeigt)
-   **Glatte Linien anzeigen**   * Zeigt glatte Linien an. Eine glatte Linie ist eine Linie, die einen Wechsel zwischen tangentialen Flächen anzeigt, wie beim Übergang von einer ebenen Fläche zu einer [Verrundung](https   *//en.wikipedia.org/wiki/Fillet_(mechanics)).
-   **Nahtlinien anzeigen**   * Nahtlinien anzeigen. Eine Nahtlinie ist eine Grenzlinie zwischen Flächen.
-   **Zeige UV ISO Linien**   * Zeigt ISO Linien. ISO steht für *isoparametrisch*. [Hier ist eine Beschreibung](https   *//knowledge.autodesk.com/support/alias-products/learn-explore/caas/CloudHelp/cloudhelp/2014/ENU/Alias/files/GUID-4CCDF144-DB4F-4BEB-BA5A-E69CED27F4B9-htm.html), was isoparametrische Linien (in Wirklichkeit Kurven) sind.
-   **ISO Anzahl**\'   * Die Anzahl der ISO-Linien pro Flächenkante.

## Erweitert

<img alt="Erweiterte Einstellungen" src=images/TechDraw_PreferencesAdvanced.png  style="width   *350px;">

-   **Flächen erkennen**   * Wenn angehakt, versucht TechDraw, Flächen unter Verwendung der Liniensegmente zu erzeugen, die vom Algorithmus zur Entfernung verdeckter Linien zurückgegeben werden. Flächen müssen erkannt werden, um [Schraffierung](TechDraw_Hatching/de.md) verwenden zu können, aber bei komplexen Modellen kann es zu Leistungseinbußen kommen.
-   **Schnittkanten zeigen**   * Hebt den Rand des ausgeschnittenen Abschnitts in [Schnittansichten](TechDraw_SectionView/de.md) hervor.
-   **Fehlersuche und -bereinigung Schnittansicht**   * Gibt Zwischenergebnisse während der Verarbeitung einer Sektionsansicht aus
-   **Fehlersuche und -bereinigung Detailansicht**   * Gibt Zwischenergebnisse während der Verarbeitung einer Detailansicht aus
-   **Unübliche Kanten erlauben**   * Schließt Kanten mit unerwarteter Geometrie in die Ergebnisse ein, z.B. Nulllängen
-   **Verbinden vor Schnitterzeugung**   * Führt eine Verschmelzungsoperation an der/den Eingangsform(en) vor der Verarbeitung der Schnittansicht
-   **Zeige lose 2D-Geometrie**   * Schließt 2D-Objekte in Projektionen ein, z. B. lose Skizzen
-   **Auswahlbereich für Kanten**   * Größe des Auswahlbereichs um Kanten herum. Die Unschärfeeinheit ist ungefähr 0.1 mm, abhängig vom aktuellen Zoom.
-   **Fangbereich für Mittelpunktsmarkierungen**   * Auswahlbereich um Mittenmarkierungen herum. Die Unschärfeeinheit ist ungefähr 0.1 mm, abhängig vom aktuellen Zoom.
-   **Form der Linienenden**   * Einstellung der Form der Linienendkappe. Erläuterung der Optionen   * [pen cap styles](https   *//doc.qt.io/qt-5/qt.html#PenCapStyle-enum)
-   **Max. SVG-Schraffur-Felder**   * Die Grenze von SVG-Kacheln mit einer Größe von 64x64 Pixeln, die zum Schraffieren einer einzelnen Fläche verwendet werden. Bei großen Skalierungen könnte man einen Fehler über zu viele SVG-Kacheln erhalten, dann muss man das Kachellimit erhöhen.
-   **Max. PAT-Schraffur-Segmente**   * Die maximalen Schraffursegmente, die beim Schraffieren einer Fläche mit einem PAT-Muster verwendet werden.





{{TechDraw Tools navi

}} 

[Category   *Preferences](Category_Preferences.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Preferences/de
