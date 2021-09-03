 Ich beginne diese Seite als Versuch, Endanwenderwünsche zu bestimmten Werkzeugen zu sammeln, die sie in FreeCAD finden möchten. Mehrere cad Benutzer haben sich bereits mit mir über cad Werkzeuge unterhalten, darüber, was sie am meisten benutzen, was sie sich in FreeCAD wünschen, worauf sie nicht verzichten können, usw\..... Obwohl FreeCAD nicht dazu gedacht ist, spezifisch ein Ersatz für jede andere berühmte CAD Software zu werden (besonders für die, die mit Auto beginnt und mit CAD endet), denke ich, dass dies eine gute Referenz werden kann, um die Erwartungen der Endbenutzer zu kennen und vielleicht die Dinge über andere in der Entwicklung zu stellen.

Wenn Du ein CAD Anwender bist und hier etwas hinzufügen möchtest, kannst Du gerne editieren, wir würden uns freuen, Deine Meinung hier zu haben.

## 2D Zeichnung {#d_zeichnung}

-   ~~**Linie**: Zeichnet eine Linie~~ - siehe [Entwurf Linie](Draft_Line/de.md).
-   **Konstruktionslinie**\': Zeichnet eine Linie in jedem beliebigen Winkel unendlich - sollte einfach sein, wenn möglich in Coin. Zu untersuchen
-   ~~**Polylinie**: Linie mit beliebig vielen Punkten, bis der Befehl beendet ist~~ - siehe [Entwurf Draht](Draft_Wire/de.md).
-   **Polygon**: abhängig von der Anzahl der Seiten
-   ~~**Rechteck**~~ - siehe [Entwurf Rechteck](Draft_Rectangle/de.md).
-   ~~**\'Bogen**\'~~ - siehe [Entwurf Bogen](Draft_Arc/de.md).
-   ~~**Kreis**\'~~ - siehe [Entwurf Kreis](Draft_Circle/de.md).
-   **Schraffur**\': In der Lage sein, einen Bereich mit einem Muster im technischen Stil (schräge Linien usw\...) auszufüllen - wird untersucht
-   **Blöcke erstellen und einfügen**: Das sind in FreeCAD zwei Dinge: ~~Elemente in einem Objekt (Verbund?)~~ gruppieren können - siehe [Entwurf Hochstufen](Draft_Upgrade/de.md). - und in der Lage sein, diese Objekte zu instanziieren (mehrere Dokumentobjekte haben die gleiche Form?)
-   **Text** - siehe [Entwurf Text](Draft_Text/de.md). Wird auf komplexere Dinge erweitert\...
-   **Anzeige Reihenfolge**: Das bedeutet, dass koplanare Objekte in der gewünschten Reihenfolge angezeigt werden. Allerdings bin ich nicht sicher, ob dies möglich ist\... Vielleicht sollten wir in einer 3D Welt die Art und Weise, wie wir 2D Objekte zeichnen, überdenken und diese \"überlappenden\" Objekte anders betrachten (= anders zeichnen). Zu diskutieren\...
-   ~~**Löschen**~~ - siehe [Std Löschen](Std_Delete/de.md).
-   ~~\'\'\'\'\'\'~~ - siehe [Entwurf Bewegen](Draft_Move/de.md).
-   ~~**Kopie mit Basispunkt**~~ - siehe [Entwurf Bewegen](Draft_Move/de.md).
-   **Mehrfachkopie**: Ein Objekt mehrmals vom selben Basispunkt aus kopieren
-   *Einfügen*\'
-   **Als Block einfügen**
-   ~~**\'Versatz**\'~~ - siehe [Entwurf Versatz](Draft_Offset/de.md).
-   ~~\'\'\'\'\'\'~~ - siehe [Entwurf Bewegen](Draft_Move/de.md).
-   ~~**Rotate**~~ - siehe [Entwurf Rotieren](Draft_Rotate/de.md).
-   **Anordnung**: interessant, könnte mit dem Kopierwerkzeug zusammengeführt werden\...
-   **Dehnen**\'
-   ~~**Stutzen**~~ - siehe [Entwurf Trimex](Draft_Trimex/de.md), könnte aber erweitert werden
-   ~~**Dehnen**~~ - siehe [Entwurf Trimex](Draft_Trimex/de.md), könnte aber verlängert werden
-   **Fase**\'
-   ~~**Verrundung (mit Winkeleingabe)**~~ - implementiert im Modul Fold

~~\'\'\'\'\'\': Explodiert Blöcke/Zeilen~~ - siehe [Entwurf Herabstufen](Draft_Downgrade/de.md).

-   ~~**Dimension**~~ - siehe [Entwurf Abmessung](Draft_Dimension/de.md).
-   **Winkelbemessung**\' - geplant im Modul Entwurf
-   **Bogenlänge** - geplant im Modul Entwurf
-   **Durchmesser** - siehe [Entwurf Abmessung](Draft_Dimension/de.md)
-   ~~**Radius**~~ - siehe [Entwurf Abmessung](Draft_Dimension/de.md)
-   **Fortsetzen Abmessung**: setzt eine laufende Dimension fort - geplant im Modul Entwurf
-   ~~**Ansichten: Oben, Unten, Rechts, Links**~~ - siehe [Std Ansicht Menü](Std_Ansicht_Menü.md).
-   ~~**\'Ansicht: Isometrische Ansichten**~~ - siehe [Std. OrthographicCamera](Std._OrthographicCamera.md).
-   ~~**Modellraum und Papierraum**~~ - siehe [Zeichnungsmodul](Drawing_Workbench/de.md). - Modellbereich = Dort, wo das Modell gezeichnet wird, Papierbereich = Registerkarten mit verschiedenen Einstellungen, die geplottet werden können. (Die Registerkarten können eingezeichnet werden und haben Ansichtsfenster, die durch geschlossene Polylinien oder Formen gebildet werden, die in den Modellbereich hineinblicken.) Sie müssen in der Lage sein, in den Modellbereich hinein- und herauszuklicken, damit Sie das Papier mit Bodern und Titelboxen einrichten können. Die Ansicht muss je nach Bedarf skaliert werden, d.h. 1:50 oder 1:100 - geplant im Zeichnungsmodul
-   **Zeichnungseinheiten**: Alle Zeichnungseinheiten sollten mm sein - dies ist ein ganz spezielles Thema, es gibt viele Dinge zu beachten. Wird weiter diskutiert. 
-   **Gewinde** - PartDesign Arbeitsbereich. Merkmal Bohrung: korrekte Funktionalität der Bohrungstiefe gemäß der Norm ISO 6410-1
-   **Gewinde** - normativ korrekte vereinfachte Darstellung des Querschnitts in Techdraw gemäß der Norm ISO 6410-1
-   **Verrundung** - PartDesign Arbeitsbereich: Beseitigung von Rundungsproblemen 

## Netz Modellierung {#netz_modellierung}

-   **Primitive**\': Würfel, Kugeln usw. - vorhanden, aber keine Schaltfläche in der Symbolleiste
-   **Teilobjekte in Netze umwandeln** - vorhanden, aber keine Schaltfläche in der Symbolleiste
-   **Netz Normale umdrehen** - vorhanden, aber keine Schaltfläche auf der Symbolleiste
-   **Löcher in Netzen entfernen** - vorhanden, aber keine Schaltfläche in der Werkzeugleiste
-   **Flächen in Netzen entfernen**\' - vorhanden, aber keine Schaltfläche in der Symbolleiste
-   **Boolesche Operationen**\': Vereinigen, Subtrahieren und Maschen schneiden - vorhanden, aber keine Schaltfläche in der Symbolleiste

## Teil Modellierung {#teil_modellierung}

-   ~~**Primitive**~~
-   **Netz Umwandlung**\' in Teilformen
-   ~~**Boolesche Operationen**~~
-   ~~**Flache Formen extrudieren**~~
-   ~~**Verrundung der Kanten von Formen**\'~~

## Parametrische Modellierung {#parametrische_modellierung}

-   **Benutzerdefinierte Eigenschaften für alle Objekte**: so können Skripte und der Export in andere Software zusätzliche Informationen enthalten
-   ~~**\'Python Objekte**~~: 100% python geskriptete Objekte - siehe [Geskriptete Objekte](Geskriptete_Objekte.md).

## Architekturmodellierung

-   Wand
-   Fenster
-   Tür
-   Balken
-   Platte
-   Dach
-   Baugruppen\*.

[Category:Hubs{{\#translation:}}](Category:Hubs.md) [Category:Roadmap{{\#translation:}}](Category:Roadmap.md) [Category:Developer{{\#translation:}}](Category:Developer.md)
