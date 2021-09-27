# HiDPI support/de
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

![Device pixel ratio. 100% = 1, 200% = 2, 150% = 1.5](images/HiDpiDevicePixelRatio.png )


<div class="mw-translate-fuzzy">

Dies ist ein [Projekt](project/de.md), das sich der Unterstützung hochauflösender Anzeigen in FreeCAD widmet.


</div>


<div class="mw-translate-fuzzy">

Die HiDPI Unterstützung bezieht sich auf das Problem der Darstellung von Rastergrafiken (Schriftarten, Cursor, Bilder) und UI Elementen (Schaltflächen, Menüs, Handgriffe) auf hochauflösenden Bildschirmen.


</div>


<div class="mw-translate-fuzzy">

Das Problem besteht darin, dass die physische Größe eines Bildschirms gleich bleibt, während seine Auflösung zunimmt.


</div>

To solve the issue, Apple introduced \"HiDPI\", that is scaling all the UI elements according to the font size. Font sizes are specified in points, while their pixel value is calculated using DPI and device pixel ratio which is a scale factor specified by a user in OS settings. At the same time, raster images are rendered at their true pixel size, so individual pixels are less noticeable. It means that raster images are provided at higher resolution to make up for their size on a screen. Vector graphics (UI elements) are rendered accordingly, at higher resolution.

## Gesamtkonzept

### Teil eins 

Ziel: Sicherstellen, dass wir das Beste aus der Qt Unterstützung herausholen.


<div class="mw-translate-fuzzy">

-   In Bearbeitung. Migriere die Benutzerbasis auf Qt \> 5.6 und setze die AA\_EnableHighDpiScaling auf true.
-   Skaliere alle Cursor und Symbole (multipliziert mit devicePixelRatio) <https://github.com/FreeCAD/FreeCAD/pull/3712>


</div>

### Teil zwei 

Ziel: Sicherstellen, dass die Systemschriftart korrekt festgelegt ist.

-   Bündele geeignete QPA Thema Zusatzmodule auf allen wichtigen Plattformen (AppImage usw.)
-   Finde Wege, um festzustellen, ob die Schriftart des Systems geändert wurde
-   Entferne die Werkzeugleiste/Symbolgröße Einstellung und stelle die Werkzeugleiste relativ zur Systemschriftart ein
-   Füge eine experimentelle \"Skalierungsfaktor\" Einstellung hinzu, der vom Pixelverhältnis des Geräts und/oder der Schriftgröße des Systems abhängt.
-   Skaliere die Werkzeugleiste/Symbolgröße entsprechend der neuen experimentellen Einstellung neu
-   Sammle Anwender Rückmeldungen, ob wir die anpassbare Werkzeugleisten Symbolgröße benötigen

### Teil drei 

Ziel: Alle UI Widgets relativ zur Schriftgröße skalieren

-   Hole dir an allen geeigneten Stellen Systemschriftarten Metriken, um die Größe eines Widgets zu bestimmen.
-   An Stellen, an denen auf die reale Größe Bezug genommen wird, nimm die Schriftgröße als relatives Maß an (72 Punkte = 96 virtuelle Pixel = 1 Zoll).
-   Wähle ein Referenzgerät, relativ zu dem die Benutzeroberfläche nach oben und unten skaliert werden könnte.
-   2D Koordinaten und Größen sollten geräteunabhängige Pixel annehmen.
-   Stelle sicher, dass qreal Versionen von APIs verwendet werden.
-   Schalte AA\_EnableHighDpiScaling aus.

### Teil vier 

Ziel: Unterstützung der Neuskalierung beim Verschieben des Fensters von einem Bildschirm zum anderen

-   Erkennen, dass sich das Pixelverhältnis des Geräts geändert hat
-   Benachrichtigung aller Widgets abhängig vom Pixelverhältnis des Geräts oder der Schriftgröße

## Hintergrund

### Bildschirmauflösungen

<img alt="" src=images/Vector_Video_Standards8.svg  style="width:800px;">

### Geräte Pixelverhältnis 

Es ist ein bekanntes Konzept für Web und Android Entwickler. Aber nicht so sehr für Desktop Entwickler.

Im Grunde ist es das Verhältnis zwischen physikalischen Pixeln und geräteunabhängigen Pixeln.

Eins nach dem anderen. UI Positionierung und Größe (x, y, Breite, Höhe) sind historisch in Pixeln definiert.

Da jedoch immer mehr verschiedene Bildschirmauflösungen in vielen verschiedenen physikalischen Größen verfügbar sind, ist dies zu einem Problem geworden, dessen sich Software Entwickler bewusst sein müssen.

Mit der Entwicklung von FreeCAD wurde 2002 begonnen, lange bevor ein solches Problem überhaupt absehbar war.

Ok, warum nicht einfach den DPI erhöhen, fragst du. Nun, das Problem ist, dass du immer noch von der hochauflösenden Anzeige profitieren willst.

Alle Rastergrafiken müssen mehr Pixel enthalten, während Vektorgrafiken (Schriften und Symbole) die gleiche physikalische Größe haben sollten, wie sie auf dem Bildschirm sichtbar sind.

Wenn du nur den DPI änderst, würdest du alles nach oben und unten skalieren. Tatsächlich müssen aber alle Pixelgrößen gleich bleiben, während die Ressourcen (Bilder) in einer höheren Auflösung angezeigt werden müssen.

So wurde das Konzept der \"geräteunabhängigen Pixel\" eingeführt. Die Idee war, dass sich die Entwickler keine Gedanken über die physische Größe eines Displays machen und UIs in virtuellen Pixeln entwerfen konnten.

Die Realität sieht jedoch so aus, dass Rastergrafiken verpixelt, verschwommen oder verfremdet werden, wenn sie in nicht nativer Auflösung angezeigt werden. Daher müssen Entwickler jetzt mehrere Versionen von Rasterbildern für jedes Geräte-Pixelverhältnis bereitstellen. Normalerweise handelt es sich dabei um ganze Zahlen: 1, 2, 3, 4. Es kann aber auch ein Bruchteil sein (125%, 150%, 175% = 1,25, 1,5, 1,75), d.h. es ist immer noch eine gewisse Skalierung erforderlich, aber nicht so offensichtlich.

-   <https://stackoverflow.com/questions/8785643/what-exactly-is-device-pixel-ratio>
-   <https://stackoverflow.com/questions/13911786/what-is-device-pixel-ratio-for>

## Ausgabetesten/Vorführung

### OS X 

1.  \"Anzeige\" öffnen
2.  Wähle \"Skaliert\".
3.  Wähle \"Größerer Text\" - dies erhöht das Pixelverhältnis des Geräts

Video: <https://www.youtube.com/watch?v=4U3eh_fMo4o>

### X Window 

Nützliche Befehle:

    ~$ xrdb -query
    *customization: -color
    Xft.dpi:    192
    Xft.antialias:  1
    Xft.hinting:    1
    Xft.hintstyle:  hintslight
    Xft.rgba:   rgb
    Xcursor.size:   128
    Xcursor.theme:  DMZ-White

    ~$ xdpyinfo | grep -B 2 resolution
    screen #0:
      dimensions:    3840x2160 pixels (1016x572 millimeters)
      resolution:    96x96 dots per inch

### Ubuntu (GNOME Shell) 

1.  \"Anzeigen\" öffnen (Einstellungen \> Geräte \> Anzeigen)
2.  Wähle die höchste verfügbare Auflösung
3.  Wähle Skalierung höher als 100%

## Probleme und Lösungen 

-   Rasterbilder (Mauszeiger, Symbole)
-   Schriften (definiert in Pixeln statt in Punkten)
-   Mauszeiger-Brennpunkt
-   Zoom/Drehen des Ursprungs
-   Fangabstand
-   Auswahlabstand (der heiße Bereich um auswählbare Objekte)

### Schriftgröße

Schriften sind in der Regel vektoriell. Sie benötigen also keine Version mit höherer Auflösung, um skaliert werden zu können (in Pixel). Wir können jedoch nicht einfach jede Schriftgröße vergrößern und Feierabend machen. Die Menschen sind an Schriftgrößen gewöhnt, die im Verhältnis zu ihrem Aussehen auf Papier stehen. Und auf Papier ist bekannt, dass eine 72pt-Schrift einen Zoll benötigt, und auf Bildschirmen früherer Zeiten entsprach ein Zoll 96 Pixeln bei einer Zoomstufe von 1:1.

Wenn die Bildschirmauflösungen höher werden, könnten also mehr Textzeilen gleicher Größe auf die Displays passen. Da also die physische Größe der Anzeige gleich bleibt und unsere Augen beim Erkennen kleinerer Details nicht besser werden, nehmen wir natürlich die gleiche Schriftgröße bei höheren Auflösungen als kleiner wahr.

Um dieses Problem zu beheben, implementierte das Betriebssystem die so genannte DPI Skalierung (oder DPI Schrifteinstellungen in früheren Zeiten) oder High-DPI Skalierung der neuesten 4K Bildschirme. Die Benutzer konnten die DPI ändern und von viel mehr Platz in Bezug auf die Pixel profitieren, während gleichzeitig eine bequem lesbare Schriftgröße beibehalten wurde.

### Benutzerdefinierte Mauszeiger Größe 

Die Mauszeigergröße ist etwas schwierig. Qt empfiehlt die Verwendung einer hartkodierten Bildgröße von 32x32. Ab 5.x bietet es keine Funktionalität zur Integration mit dem Betriebssystem und zur Abfrage der Größe des Mauszeigers. Das ist schade, da es bedeutet, dass du nicht von Zugänglichkeitseinstellungen profitieren kannst, bei denen die Mauszeigergröße auf einen beliebig großen Wert eingestellt werden kann.

Bis Qt eine bessere Anleitung für die Cursorgröße liefert, lasst uns also ein Bild mit einem 32 \* Gerätepixelverhältnis verwenden.

In Betriebssystemen, zum Beispiel in GNOME, scheint die Größe des Mauszeigers in Form von virtuellen Pixeln festgelegt zu sein. Das heißt, sie respektiert das Pixelverhältnis des Geräts (gleiche scheinbare Größe beibehalten). Sie erhöht sich jedoch, wenn du die Bildschirmauflösung änderst (d.h. in Pixeln gleich bleibt, aber die scheinbare Größe erhöht sich).

Hier ist zum Beispiel eine Standardeinstellung für virtuelle Pixel in GNOME:

    ~$ gsettings get org.gnome.desktop.interface cursor-size
    64

Unter Berücksichtigung des Skalierungsfaktors bedeutet dies die physikalische Pixelgröße von 128.

Qt bietet nicht die Funktionalität, um diesen Wert abzurufen. Also müssen wir ihn entweder hart codieren oder eine Benutzereinstellung bereitstellen, um das zu ändern.

## Forumsbeiträge


<div class="mw-translate-fuzzy">

-   [Verbessere die Unterstützung von Bildschirmen mit hohem DPI](https://forum.freecadweb.org/viewtopic.php?t=34916) - allgemeine Qt Unterstützung
-   [Neuigkeiten: Qt 5.14 bringt deutlich bessere HiDPI Unterstützung](https://forum.freecadweb.org/viewtopic.php?t=39325) - allgemeine Qt Unterstützung
-   [Benutzerdefinierte Mauszeiger und hohe dpi (Windows- und MacOS Tester erforderlich)](https://forum.freecadweb.org/viewtopic.php?&t=48719) - Raster Mauszeiger Bildproblem
-   [HiDPI Unterstützung in der Skizzierer Ansicht](https://forum.freecadweb.org/viewtopic.php?t=34853) - Auswahldistanzproblem
-   [Hohe DPI Verbesserungen](https://forum.freecadweb.org/viewtopic.php?t=10512) - PR \"Hohe DPI Korrekturen\" <https://github.com/FreeCAD/FreeCAD/pull/54>, schlechte Qualität, 2015
-   [Hohe dpi](https://forum.freecadweb.org/viewtopic.php?t=12123) - experimenteller Aufbau mit \"Hohe DPI Verbesserungen\" PR
-   [GUI Schriftgröße](https://forum.freecadweb.org/viewtopic.php?t=41656) - Schriftgrößenproblem und die QT\_SCALE\_FACTOR Umgehung
-   [FEHLER? abgeschnittene Symbole](https://forum.freecadweb.org/viewtopic.php?t=28838) - Probleme mit HiDPI auf mehreren Bildschirmen
-   [FreeCAD 0.17 auf MacOS Aktualisierung (Qt 5 ist jetzt verfügbar)](https://forum.freecadweb.org/viewtopic.php?t=20977) - Probleme mit HiDPI auf OS X nach Höherstufung auf Qt5
-   [Ticket \#3537 - Entwurf Bearbeitungsmodus funktioniert nicht unter MacOS X (HiDPi Problem)](https://forum.freecadweb.org/viewtopic.php?f=3&t=29743) - OS X + HiDPI, Qt5
-   [Menü auf externem MAC Bildschirm verzerrt](https://forum.freecadweb.org/viewtopic.php?t=39975) - OS X + HiDPI, externer Bildschirm
-   [macOS Qt5 Plan und Status](https://forum.freecadweb.org/viewtopic.php?t=19724&start=60) - OS X hat die Unterstützung für Qt4 und HiDPI Probleme eingestellt
-   <https://www.google.com/search?q=freecad+hidpi+site:forum.freecadweb.org>


</div>

## Relevante Änderungen 

-    {{commit|a14b99e77}}
    

-    {{commit|2f2d50535}}
    

-    {{commit|bb6e4e6ad}}
    

-    {{commit|23ecb8eac}}
    

-    {{commit|ca7770b80}}
    

-    {{commit|51fcdd2c0}}
    

-    {{commit|805ccd8deb}}
    

-    {{commit|347156403}}
    

-    {{commit|094dda5900d}}
    

-    {{commit|925cffc1535}}
    

-    {{commit|7dfeb801a}}
    

## Fehlerverfolgungsprobleme

-   Tickets markiert mit [HiDPI](https://tracker.freecadweb.org/search.php?tag_string=HiDPI)

## Externe Referenzen 

-   <https://doc.qt.io/qt-5/highdpi.html>
-   <https://doc.qt.io/qt-5/scalability.html>
-   <https://docs.microsoft.com/en-us/windows/win32/hidpi/high-dpi-desktop-application-development-on-windows>
-   <https://docs.microsoft.com/en-us/windows/win32/w8cookbook/high-dpi-for-desktop-apps-in-windows-8-1?redirectedfrom=MSDN>



_

---
[documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > HiDPI support/de
