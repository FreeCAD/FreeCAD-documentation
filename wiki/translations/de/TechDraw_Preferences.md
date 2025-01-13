# TechDraw Preferences/de
## Einführung

Die Einstellungen für den Arbeitsbereich <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw](TechDraw_Workbench/de.md) findet man im [Voreinstellungseditor](Preferences_Editor/de.md). Den Menüeintrag **Bearbeiten → Einstellungen...** auswählen und dann **<img src="images/Workbench_TechDraw.svg" width=16px> TechDraw**. Diese Gruppe steht nur dann zur Verfügung, wenn der Arbeitsbereich TechDraw in der aktuellen FreeCAD-Sitzung geladen wurde.

Es gibt sieben Seiten: [Allgemein](#General/de.md), [Skalieren](#Scale/de.md), [Maßeinträge](#Dimensions/de.md), [Beschriftung](#Annotation/de.md), [Farben](#Colors/de.md), [Ausblenden verdeckter Kanten (HLR)](#HLR/de.md) und [Erweitert](#Advanced/de.md).

Alle Einstellungen mit *kursiven* Beschriftungen sind Standardwerte für neue Zeichnungsobjekte. Sie haben keinen Einfluss auf bestehende Objekte.

Diese Seite wurde für Version 1.0 aktualisiert.



## Allgemeines

<img alt="Allgemeine Einstellungen" src=images/Preferences_TechDraw_Page_General.png  style="width:350px;">



### Zeichnung Aktualisierung 

-   **Aktualisierung mit 3D (globale Richtlinie)**: Ob die Seiten bei jeder Änderung des 3D-Modells aktualisiert werden oder nicht.
-   **Seitenüberschreibung zulassen (globale Richtlinie)**: Ob die Eigenschaft **[Aktualisiert halten](TechDraw_PageDefault/de#Eigenschaften.md)** einer Seite den globalen Parameter **Aktualisierung mit 3D** überschreiben kann oder nicht.
-   **Seite auf dem neuesten Stand halten**: Hält Zeichnungsblätter mit Änderungen des 3D-Modells *in Echtzeit* synchron. Dies kann die Reaktionszeit verlangsamen.
-   **Sekundäransichten automatisch verteilen**: Verteilt automatisch Sekundäransichten für [Projektionsgruppen](TechDraw_ProjectionGroup/de.md).



### Beschriftungen

-   **Anmerkungsschriftart**: Der Name der Schriftart für Beschriftungen. Die Schriftart wird auch für neue [Maßeinträge](#Maßeinträge.md) verwendet; sie zu ändern hat keinen Einfluss auf bestehende Maße
-   **Anmerkungsschrifthöhe**: Standardhöhe für Beschriftungen.



### Vorgaben

-   **Projektionsmethode**: Ob eine [Ansichtengruppe](TechDraw_ProjectionGroup/de.md) entweder die europäische (first-angle) Projektion oder die amerikanische (third-angle) Projektion verwenden. Siehe [multiview projection](https://en.wikipedia.org/wiki/Multiview_projection#Multiviews) (engl.) (oder [Projektionsmethoden](https://de.wikipedia.org/wiki/Normalprojektion#Ansichten)) für eine Erklärung.
-   **Schnittlinienkonvention**: Norm nach der die Pfeile und Symbole platziert werden ({{Version/de|1.0}}). Optionen sind:
    -   *ANSI*
    -   *ISO*



### Dateien

-   **Standardvorlage**: Standard-[Vorlagendatei](TechDraw_Templates/de.md) für neue Seiten.
-   **Vorlagenverzeichnis**: Startverzeichnis für Symbolleistenschaltfläche **<img src="images/TechDraw_PageTemplate.svg" width=16px> [Seite unter Verwendung einer Vorlage einfügen](TechDraw_PageTemplate/de.md)**.
-   **Schraffurmusterdatei**: Standard-[SVG](SVG/de.md)- oder [Bitmap](bitmap/de.md)-Datei für [Schraffuren](TechDraw_Hatch/de.md).
-   **Liniegruppendatei** Alternative Datei für persönliche [Liniengruppen](TechDraw_LineGroup/de.md)-Definitionen.
-   **Schweißverzeichnis**: Standardverzeichnis für Symbolleistenschaltfläche **[<img src=images/TechDraw_WeldSymbol.svg style="width:16px"> [Schweißinformationen zur Hinweislinie hinzufügen](TechDraw_WeldSymbol/de.md)**.
-   **PAT Datei**: Standarddatei zum Festlegen von PAT-Mustern für [geometrische Schraffuren](TechDraw_GeometricHatch/de.md).
-   **Mustername**: Name des Standard-PAT-Musters.
-   **Symbolverzeichnis**: Alternatives Verzeichnis für die Suche nach SVG-Symbol-Dateien.



### Raster

-   **Raster anzeigen**: Standardeinstellung der Rasteranzeige für neu erstellten Seiten.
-   **Rasterabstand**: Standardabstand zwischen Rasterlinien auf neu erstellten Seiten.



### Auswahl

-   **Mehrfachauswahl-Modus aktivieren**: Wenn aktiviert, führt das Klicken ohne **Strg** nicht zum Löschen der bisherigen Auswahl. {{Version/de|1.0}}

### View Defaults 

-   **3D-Kamerarichtung verwenden**: Wenn akktiviert, wird die Richtung der 3D-Kamera (oder die Normale einer ausgewählten Fläche) als Ansichtsrichtung verwendet. Wenn nicht aktiviert, werden Ansichten als Vorderansichten erstellt. {{Version/de|1.0}}
-   **Benennung immer anzeigen**: Wenn aktiviert, werden die Benennungen von Ansichten auch dann angezeigt, wenn die Rahmen unterdrückt werden. {{Version/de|1.0}}



### Einrasten

-   **Snap View Alignment**: If checked, Views will be snapped into alignment when dragged. <small>(v1.0)</small> 
-   **View Snapping Factor**: Tolerance for snapping of Views - if a View is within this fraction of View size of perfect alignment, it will snap into alignment. <small>(v1.0)</small> 



## Maßstab

<img alt="Maßstabseinstellungen" src=images/Preferences_TechDraw_Page_Scale.png  style="width:350px;">



### Maßstab 

-   **Seitenmaßstab**: Standardmaßstab für neue Zeichnungen.
-   **Anzeige Maßstabstyp**: Standardmaßstab für neue Ansichten.
-   **Anzeige Benutzerdefinierter Maßstab**: Standardmaßstab für Ansichten, wenn **Anzeige Maßstabstyp** *Benutzerdefiniert* ist.



### Größenanpassungen

-   **Knotenmaßstab**: Größe der [vertex](Glossary#V.md) Punkte. Multiplikator der Linienbreite.
-   **Zentrumsmarkierungsmaßstab**: Größe der Mittenmarkierungen. Multiplikator der Knotengröße.
-   **Vorlage Bearbeitungsmarkierung**: Größe des [Vorlagenfelds](TechDraw_Templates/de.md) klicken gehandhabt in mm (grüne Punkte).
-   **Schweißsymbolmaßstab**: Größenmultiplikator [Schweißsymbole](TechDraw_WeldSymbol/de.md).



## Maßeinträge

<img alt="Einstellungen für Maßeinträge" src=images/Preferences_TechDraw_Page_Dimensions.png  style="width:350px;">



### Maßeinträge 

-   **Normbasis und Ausführung von Maßeinträgen**: Die Norm, die für Maßeinträge zu verwenden ist. Die Unterschiede zwischen den Normen sind in der Abbildung dargestellt:

![\|500px\|Unterschiede zwischen den unterstützten Normen. ([Image source](images/https://forum.freecadweb.org/viewtopic.php?f=35&t=39571#p336144))](TechDraw_Dimension_standardization.png )

:   

    :   ISO ausgerichtet (ISO Oriented) - gezeichnet gemäß Norm ISO 129-1, Text ist gedreht, um parallel zu der (Tangente an die) Maßlinie zu sein.
    :   ISO mit Hinweislinie (ISO Referencing) - gezeichnet entsprechend der Norm ISO 129-1, Text ist immer horizontal, über der kürzest möglichen Bezugslinie.
    :   ASME eingepasst (ASME Inlined) - gezeichnet gemäß Norm ASME Y14.5M, Text ist horizontal, eingefügt in einer Lücke der Maßlinie (bzw. des \"Maßbogens\" bei Winkeln).
    :   ASME mit Hinweislinie (ASME Referencing) - gezeichnet entsprechend der Norm ASME Y14.5M, Text ist horizontal, an einer Seite mittig mit einer kurzen, mit der Maßlinie verbundenen Bezugslinie versehen.

-   **Globale Dezimalstellen verwenden**: Verwendet die Anzahl der Dezimalstellen aus dem [Voreinstellungseditor](Preferences_Editor/de#Einheiten.md).
-   **Maßeinheiten anzeigen**: Fügt die Maßeinheit (mm, in, etc.) hinter den Maßzahlen hinzu.
-   **Dezimalstellen ändern**: Anzahl der Dezimalstellen, wenn **Globale Dezimalstellen verwenden** nicht ausgewählt ist und unter **Maßzahlenformat** nichts angegeben wurde.
-   **Maßzahlenformat**: Benutzerdefiniertes Format für Maßzahlen (und -Texte). Verwendet die [printf-Formatierung](https://de.wikipedia.org/wiki/Printf).
-   **Schrifthöhe**: Schriftgröße für Maßzahlen und -Texte.
-   **Skalierung der Toleranzeinträge**: Schrifthöhenanpassung für Toleranzeinträge. Ein Multiplikator der **Schrifthöhe**.
-   **Durchmessersymbol**: Zeichen für die Kennzeichnung von Durchmessermaßen.
-   **Pfeildarstellung**: Art der Maßpfeile (Maßlinienbegrenzungen).
-   **Pfeillänge**: Größe der Maßpfeile.
-   **Extension Gap Factor - ISO**: Lücke zwischen Maßpunkt und Anfang der Maßhilfslinie für ISO-Maße. {{Version/de|0.21}}
-   **Extension Gap Factor - ASME**: Lücke zwischen Maßpunkt und Anfang der Maßhilfslinie für ASME-Maße. {{Version/de|0.21}}
-   **Line Spacing - ISO**: Abstand zwischen der Maßlinie und dem Maßtext für ISO-Maße. {{Version/de|0.21}}



### Werkzeuge

-   **Dimensioning tools**: Select the type of dimensioning tools for the toolbar. Whichever you choose, all tools are always available in the menu and through shortcuts. The options are: <small>(v1.0)</small> 
    -   *Single tool*: A [single tool](TechDraw_Dimension.md) for all dimensioning in the toolbar: Distance, Distance X / Y, Angle, Radius. Others in dropdown.
    -   *Separated tools*: Individual tools for each dimensioning tool.
    -   *Both*: You will have both the \'Single tool\' and the separated tools.
-   **Dimension tool diameter/radius mode**: While using the [Dimension](TechDraw_Dimension.md) tool you may choose how to handle circles and arcs: <small>(v1.0)</small> 
    -   *Auto*: The tool will apply radius to arcs and diameter to circles.
    -   *Diameter*: The tool will apply diameter to all.
    -   *Radius*: The tool will apply radius to all.



## Anmerkung

<img alt="Einstellungen für Beschriftungen" src=images/Preferences_TechDraw_Page_Annotation.png  style="width:350px;">



### Beschriftung

-   **Schnittflächendarstellung**: Kennzeichnungsart für Schnittflächen. Die Optionen sind:
    -   *Ausblenden*: Es gibt keine sichtbare Schnittfläche.
    -   *Farbfüllung*: Die geschnittene Fläche erhält die für **Schnittfläche** gesetzte Farbe
    -   *SVG-Schraffur*: Die Schnittfläche wird [schraffiert](TechDraw_Hatch/de.md).
    -   *PAT-Schraffur*: Die Oberfläche wird [geometrisch schraffiert](TechDraw_GeometricHatch/de.md).
-   **Schnittlinien in der Ausgangsansicht anzeugen**: Wenn aktiviert, wird die Beschriftung des Schnittes in der Ausgangsansicht dargestellt. Wenn nicht aktiviert, werden keine Schnittlinie, Pfeile oder Symbole in der Ausgangsansicht angezeigt. {{Version/de|1.0}}
-   **Schnittlinie in die Beschriftung des Schnittes einbeziehen**: Wenn aktiviert, wird die Schnittlinie in der Ausgangsansicht eingezeichnet. Wenn nicht aktiviert, werden nur die Verlaufsänderungen, Pfeile und Symbole angezeigt. {{Version/de|1.0}}
-   **Linienmarkierungen für komplexe Schnittlinien**: Zeigt Markierungen an den Richtungswechseln von Schnitlinien [komplexer Schnitte](TechDraw_ComplexSection/de.md) an. {{Version/de|0.21}}
-   **Umrissform für Detailansichten**: Form des Detailauswahlrahmens für [Detailansichten](TechDraw_DetailView/de.md). Optionen sind:
    -   *Kreis*
    -   *Quadrat*
-   **Umriss der Detailansicht anzeigen**: Diese Checkbox legt fest, ob die Umrisslinie einer Detailansicht dargestellt wird oder nicht. {{Version/de|1.0}}
-   **Detailquelle Hervorhebung anzeigen**: Diese Checkbox legt fest, ob die Linie für die Detailauswahl in der Basisansicht dargestellt wird oder nicht. {{Version/de|1.0}}
-   **Form des Hinweisfeldes**: Form des [Hinweisfeldes](TechDraw_Balloon/de.md).
-   **Ende der Linie des Hinweisfeldes**: Standardsymbol für Hinweislinienenden, siehe [Eigenschaften des Hinweisfeldes](TechDraw_Balloon/de#Eigenschaften.md).
-   **Knicklänge der Linie des Hinweisfeldes**: Länge der Bezugslinie am Knick der Hinweislinie.
-   **Hinweisfeldes mit rechtwinkligem Dreieck**: Wenn das **Ende der Linie des Hinweisfeldes** ein *gefülltes Dreieck* ist, kann das Dreieck nur eine vertikale oder horizontale Ausrichtung erhalten, wenn das Hinweisfeld bewegt wird.
-   **Hinweislinie automatisch horizontal**: Legt fest, dass das letzte Segment der [Hinweislinie](TechDraw_LeaderLine/de.md) (Bezugslinie) horizontal ist.
-   **Art der unterbrochenen Ansicht**: Die standardmäßige Unterbrechung, die [Unterbrochene Ansichten](TechDraw_BrokenView/de.md) kennzeichnet: {{Version/de|1.0}}
    -   *Keine Bruchlinien*
    -   *Zickzack-Linien*
    -   *Einfache Linien*
-   **Mittelpunktsmarkierungen darstellen**: Bogenmittenmarkierungen in Ansichten anzeigen.
-   **Mittelpunktsmarkierungen drucken**: Bogenmittenmarkierungen in der Druckausgabe anzeigen.
-   **Liniengruppe**: Eine [Liniengruppe](TechDraw_LineGroup/de.md) zum Festlegen der vorgegebenen Strichstärken.
-   **Linienart für Detailauswahlrahmen**: Linienart der Detailauswahlrahmen für [Detailansichten](TechDraw_DetailView/de.md).
-   **Mittelliniendarstellung**: Linienart für [Mittellinien](TechDraw_FaceCenterLine/de.md).



### Linien

-   **Liniennorm**: Norm nach der Schnittlinien einer [Schnittansicht](TechDraw_SectionView/de.md) erstellt werden.
-   **Liniengruppe**: Eine [Liniengruppe](TechDraw_LineGroup/de.md) wird zum Einstellen der vorgegebenen Linienbreitenverwendet.
-   **Darstellung verdeckter Kanten**: Linienart für verdeckte Kanten. {{Version/de|1.0}}
-   **Schnittliniendarstellung**: Linienart für Schnittlinien.
-   **Linienart für Detailauswahlrahmen**: Linienart für die Umrissform der [Detailansichten](TechDraw_DetailView/de.md).
-   **Mittelliniendarstellung**: Standard-Linienart für [Mittellinien](TechDraw_FaceCenterLine/de.md).
-   **Linienart für Bruchkanten**: Standard-Linienart zum Kennzeichnen von [unterbrochenen Ansichten](TechDraw_BrokenView/de.md). {{Version/de|1.0}}
-   **Form der Linienenden**: Der Standardwert (Rund) sollte in den meisten Fällen die richtige Wahl sein. Flach oder Quadrat sind nützlich, wenn eine Zeichnung als 1:1 Schablone (? cutting guide) verwendet werden soll.



## Farben

<img alt="Farbeinstellungen" src=images/Preferences_TechDraw_Page_Colors.png  style="width:350px;">

Einstellung der Standardfarben für neue Zeichnungsblätter:

-   **Normal**: Normale Linienfarbe.
-   **Vorausgewählt**: Vorausgewählte Farbe. Die Farbe, die verwendet wird, um Objekte hervorzuheben, wenn die Maus darüber bewegt wird.
-   **Ausgewählt**: Farbe für ausgewählte Objekte.
-   **Hintergrund**: Hintergrundfarbe um Zeichnungsblätter herum.
-   **Maßeintrag**: Farbe der Linien und Texte für Maßeinträge.
-   **Mittellinie**: Farbe für [Mittellinien](TechDraw_FaceCenterLine/de.md).
-   **Detailauswahl**: Linienfarbe für die Umrissform von [Detailansichten](TechDraw_DetailView/de.md).
-   **Rasterfarbe**: Farbe für alle Seitenraster.
-   **Vorlagenunterstrich**: Farbe für den Unterstrich, der in einer Vorlage die editierbaren Texte kennzeichnet.{{Version/de|1.0}}
-   **Verdeckte Kante**: Farbe der verdeckten Linie. Diese Farbe wird für alle Arten von [Verdeckten Linien](#HLR.md) verwendet.
-   **Schnittfläche**: Farbe für Schnittflächen in [Schnittansichten](TechDraw_SectionView/de.md). Wird nur verwendet, wenn die Einstellung **Schnittflächendarstellung** auf *Farbfüllung* gesetzt ist.
-   **Schnittlinie**: Farbe der Schnittlinie einer [Schnittansicht](TechDraw_SectionView/de.md).
-   **Schraffur**: Farbe für [Schraffuren](TechDraw_Hatch/de.md).
-   **Geometrische Schraffur**: Farbe für [geometrische Schraffurmuster](TechDraw_GeometricHatch/de.md).
-   **Knoten**: Farbe der auswählbaren [Knoten](Glossary/de#V.md) in Ansichten.
-   **Hinweislinie**: Farbe für neue [Hinweislinien](TechDraw_LeaderLine/de.md).
-   **Transparente Flächen**: Wenn angehakt, sind die Objektflächen transparent. Andernfalls wird die eingestellte Farbe für Flächen verwendet.
-   **Hell auf dunkel**: Wenn aktiviert, erhalten Texte und Linien eine helle Farbe. Wird verwendet, wenn die \"Blattfarbe\" dunkel ist. Transparente oder hell eingefärbte Flächen werden für diese Option empfohlen. {{Version/de|0.21}}
-   **Einfarbig**: Wenn aktiviert, wird die eingestellte Farbe für alle Texte und Linien verwendet. {{Version/de|0.21}}
-   **Blattfarbe**: Die Hintergrundfarbe des Zeichenblattes. {{Version/de|0.21}}

## HLR

<img alt="HLR-Einstellungen" src=images/Preferences_TechDraw_Page_HLR.png  style="width:350px;">

HLR steht für *Entfernen verdeckter Linien* (engl.: hidden line removal).

-   **Polygon Approximation verwenden**: Verwendet eine Approximation, um verborgene Linien zu finden. Dies geht schnell, aber das Ergebnis ist eine Sammlung kurzer gerader Linien.
-   **Zeige harte Linien**: Zeigt harte und Umrisskanten an (sichtbare Linien werden immer angezeigt)
-   **Glatte Linien anzeigen**: Zeigt glatte Linien an. Eine glatte Linie ist eine Linie, die einen Wechsel zwischen tangentialen Flächen anzeigt, wie beim Übergang von einer ebenen Fläche zu einer [Verrundung](https://en.wikipedia.org/wiki/Fillet_(mechanics)).
-   **Nahtlinien anzeigen**: Nahtlinien anzeigen. Eine Nahtlinie ist eine Grenzlinie zwischen Flächen.
-   **Zeige UV ISO Linien**: Zeigt ISO Linien. ISO steht für *isoparametrisch*. [Hier ist eine Beschreibung](https://knowledge.autodesk.com/support/alias-products/learn-explore/caas/CloudHelp/cloudhelp/2014/ENU/Alias/files/GUID-4CCDF144-DB4F-4BEB-BA5A-E69CED27F4B9-htm.html), was isoparametrische Linien (in Wirklichkeit Kurven) sind.
-   **ISO Anzahl**\': Die Anzahl der ISO-Linien pro Flächenkante.



## Erweitert

<img alt="Erweiterte Einstellungen" src=images/Preferences_TechDraw_Page_Advanced.png  style="width:350px;">

-   **Flächen erkennen**: Wenn angehakt, versucht TechDraw, Flächen unter Verwendung der Liniensegmente zu erzeugen, die vom Algorithmus zum Entfernen verdeckter Linien zurückgegeben werden. Flächen müssen erkannt werden, um [Schraffieren](TechDraw_Hatching/de.md) verwenden zu können, aber bei komplexen Modellen kann es zu Leistungseinbußen kommen.
-   **Fortschritt berichten**: Gibt Fortschrittsmeldungen aus, während die darzustellende Geometrie berechnet wird. {{Version/de|0.21}}
-   *\'Neuen Flächenfinder-Algorithmus verwenden*: Wenn aktiviert, wird der neue Flächenfinder-Algorithmus verwendet, anstatt des originalen. {{Version/de|0.21}}
-   **Automatische Korrektur der Maßreferenzen**: Wenn aktiviert, wird versucht Maßreferenzen zu aktualisieren, wenn sich das Modell ändert. {{Version/de|0.21}}
-   **Schnittkanten zeigen**: Hebt den Rand des ausgeschnittenen Abschnitts in [Schnittansichten](TechDraw_SectionView/de.md) hervor.
-   **Verbinden vor Schnitterzeugung**: Führt eine Vereinigungsoperation an der bzw. den Eingangsform(en) durch, bevor die Schnittansicht berechnet wird.
-   **Durch klicken den Arbeitsbereich wechseln**: Wenn aktiviert, wird, sobald ein Doppelklick auf ein Zeichnungsblatt (Page-Objekt) erfolgt, zu TechDraw gewechselt und das Blatt wird angezeigt. {{Version/de|1.1}}
-   **Unübliche Kanten erlauben**: Schließt Kanten mit unerwarteter Geometrie in die Ergebnisse ein, z.B. Nulllängen.
-   **Formen validieren**: Wenn aktiviert, werden Eingabeformen auf Fehler überprüft, bevor sie verwendet werden, und ungültige Formen werden ausgelassen. Es kann langsamer sein, sollte aber Abstürze verhindern. {{Version/de|1.1}}
-   **Fehlersuche und -bereinigung Schnittansicht**: Gibt Zwischenergebnisse während der Verarbeitung einer Schnittansicht aus.
-   **Debug Bad Shape**: Wenn aktiviert, werden Formen, die bei der Überprüfung durchgefallen sind, für eine spätere Analyse als brep-Daten gespeichert. {{Version/de|1.1}}
-   **Fehlersuche und -bereinigung Detailansicht**: Gibt Zwischenergebnisse während der Verarbeitung einer Detailansicht aus.
-   **Schruppdurchgänge für überlappende Kanten**: Die Anzahl der Versuche zum Entfernen von überlappenden Kanten, die vom Hidden-Line-Removal-Algorithmus zurückgegeben werden. Ein Wert von 0 bedeutet kein Schruppen. Werte über 2 sind im Allgemeinen nicht sinnvoll. Jeder Versuch trägt zur benötigten Zeit für die Erstellung der Zeichnung bei. {{Version/de|0.21}}
-   **Auswahlbereich für Kanten**: Größe des Auswahlbereichs um Kanten herum. Die Unschärfeeinheit ist ungefähr 0.1 mm, abhängig vom aktuellen Zoom. Der Standardwert ist 10. Werte von 20 bis 30 erleichtern die Auswahl von Kanten deutlich. Große Werte führen zu Überlappungen mit anderen Zeichnungselementen.
-   **Fangbereich für Mittelpunktsmarkierungen**: Auswahlbereich um Mittenmarkierungen herum. Die Unschärfeeinheit ist ungefähr 0.1 mm, abhängig vom aktuellen Zoom.
-   **Max. SVG-Schraffur-Felder**: Die maximale Anzahl (Limit) von SVG-Kacheln mit einer Größe von 64x64 Pixeln, die zum Schraffieren einer einzelnen Fläche verwendet werden. Bei großen Maßstäben könnte man einen Fehler wegen zu vieler SVG-Kacheln erhalten, dann muss man das Kachellimit erhöhen.
-   **Max. PAT-Schraffur-Segmente**: Die maximale Anzahl von Schraffursegmenten, die beim Schraffieren einer Fläche mit einem PAT-Muster verwendet werden.
-   **Balloon Drag**: Die Modifikatortaste für Balloon-Drag kann angepasst werden, um Konflikte mit dem Betriebssystem oder der Tastenzuordnungen der Navigationsart zu verhindern. {{Version/de|1.0}}





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [Preferences](Category_Preferences.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Preferences/de
