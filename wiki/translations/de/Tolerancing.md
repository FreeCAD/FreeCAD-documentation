# Tolerancing/de
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

![GD&T 3D Anmerkungen](images/Tolerancing_Annotated_Design_Model.png ) Geometrische Dimensionierung und Tolerierung [Form- und Lagetoleranz](https://de.wikipedia.org/wiki/Form-_und_Lagetoleranz) (GD&T) bedeutet die Festlegung von zulässigen Grenzen/Abweichungen der Abmessungen. Hier sprechen wir streng über geometrische Toleranzen: ein realer Form-, Größen-, Lage- und Orientierungsfehler in Bezug auf das entworfene Ideal.

Es gibt auch eine Unterscheidung zwischen den Begriffen \"Grenzen und Passungen\" und \"geometrische Toleranzen und Oberflächenbeschaffenheit\". 

## Normen

Es gibt 2 ANSI/ISO Normen:

-   ISO 1101 / ASME Y14.5 Angabe und Interpretation von geometrischen Abmessungen und Toleranzen (Definitionen und Symbole) [1](http://www.sharifcadcam.ir/uploaded/2e22f9ef-dfc5-47bc-a126-cc51e9686c4f.pdf)
-   ISO 16792 / ASME Y14.41 Modellbasierte Definitionen (CAD Daten) 3D Modelldarstellung und geometrische Dimensionierung und Tolerierung [2](http://gost-snip.su/download/asme_y14_412003_digital_product_definition_data_practices)

ISO 16792 ist ein Teil der \"Geometrischen Produktspezifikation\" (GPS), die dimensionale und geometrische Toleranzen, Oberflächeneigenschaften und die damit verbundenen Prüfungsgrundsätze, Messgeräte und Kalibrieranforderungen einschließlich der Unsicherheit von dimensionalen und geometrischen Messungen festlegt.

-   [GPS Inhaltsverzeichnis](https://www.iso.org/files/live/sites/isoorg/files/archive/pdf/en/gps_toc_.pdf)

Es gibt auch ISO 10303 (informell \"STEP\"), die das Dateiformat für den Austausch von Produkt- und Herstellungsinformationen festlegt, die aus modellbasierten Definitionen stammen.

## Annäherungen

Es gibt zwei Ansätze zur Angabe von Produkt- und Herstellungsinformationen (PMI).


<div class="mw-translate-fuzzy">

-   Der veraltete Ansatz (herkömmlich) zur Erstellung von 2D Zeichnungen mit GD&T Symbolen. In einigen Industrien wird diese Herangehensweise auch als [Technische Dokumentation](https://de.wikipedia.org/wiki/Technische_Dokumentation) bezeichnet. Wie dies mit FreeCADs [TechnischesZeichnen Arbeitsbereich](TechDraw_Workbench/de.md) erreicht wird, wird auf [dieser Seite](TechDraw_Geometric_dimensioning_and_tolerancing.md) beschrieben
-   Der moderne 3D Ansatz modellbasierte Definition (MBD), bei dem GD&T Daten in das Modell eingebettet werden und Zeichnungen mit GD&T Symbolen erstellt werden


</div>

  Herkömmlich                                               MBD
  --------------------------------------------------------- -------------------------------------------------
  3D Modelle mit 2D Zeichnungen, die GD&T/PMI enthalten     3D Modell mit eingebettetem GD&T/PMI
  Menschenlesbar                                            Menschen- und maschinenlesbar
  Verlässt sich auf menschliche Interpretation              Verlässt sich auf einen automatisierten Prozess
  Arbeitsintensiv                                           Automatisiert
  Mehrfache Dateien                                         Einzeldatenmodell
  Manuelle Synchronisierung zwischen CMM/CAM/CAI Software   Einzel Quelle der Wahrheit

## Vorhandene Software 

-   [Hinzufügen von geometrischer Toleranz mit Funktionskontrollrahmen in AutoCAD](https://www.youtube.com/watch?v=C4c_kJtwtxc)
-   [Arbeiten mit Zeichnungssymbolen in Fusion 360](https://www.youtube.com/watch?v=sVxuIgLgsKk)
-   [Technischer Tipp Dienstag: Verwendung des GD&T Schnellerstellungsmenüs in GOM Inspect](https://www.youtube.com/watch?v=Os1PVdb4UU8)
-   [CATIA V5 - FUNKTIONELLE TOLERANZIERUNG & ANMERKUNG](https://www.youtube.com/watch?v=WQUjodi7Izs)
-   [IntelligentesProfil GD&T Analyse Software](https://www.youtube.com/watch?v=0z7IoDiVYMY)

## Bisherige Umsetzung 

-   [TechDraw Symbole SVG Dateien](https://github.com/FreeCAD/FreeCAD/commits/master/src/Mod/TechDraw/Symbols/gd-and-t)
-   [GDT Arbeitsbereich](https://github.com/juanvanyo/FreeCAD-GDT)
-   [TechDraw Stücklistensymbol Makro](https://github.com/reox/FreeCAD_macros/blob/b6731feb10573e2d21781ce161c8ec7e894d1b73/TDCustomFormat.FCMacro)
-   [Ein Zweig, der einen neuen Typ von DocumentObject eingeführt hat: DrawViewGDTReference](https://github.com/lidiriel/FreeCAD/commits/gdt-reference2)

## Forumsbeiträge

-   [Verbesserung von TechDraw mit geometrischen Toleranzen und Oberflächenbearbeitungen](https://forum.freecadweb.org/viewtopic.php?f=35&t=41726) - Diskussion unter Entwicklern (2019)

-   [Geometrische Toleranzen](https://forum.freecadweb.org/viewtopic.php?t=15497) - Nutzerfunktionsanfrage (2016)
-   [GD&T Arbeitsbereich für FreeCAD](https://forum.freecadweb.org/viewtopic.php?f=10&t=22072) - Ein Arbeitsbereich für FreeCAD 0.16 (2016)
-   [TechDraw Stücklistensymbole](https://www.forum.freecadweb.org/viewtopic.php?f=9&t=35392) - Ein TechDraw-Makro für allgemeine Zwecke, das zum Platzieren von GD&T-Symbolen auf einer TechDraw-Seite verwendet werden kann (2019)
-   [ISO 1101: 2017 Geometrische Tolerierungsnorm](https://forum.freecadweb.org/viewtopic.php?f=35&t=35887) - Ein Verweis auf die ISO 1101:2017 PDF file (2019)
-   [Geometrische Dimensionierung & Tolerierung](https://forum.freecadweb.org/viewtopic.php?t=42426) - Entwickler, der Beiträge vorschlägt (2019)

## Tutorien und Lernmaterialien zu GD&T 

-   [Kurze Einführung (Video)](https://www.youtube.com/watch?v=P5GT9ZSRYl0)
-   [Wie präzise ist dieser Teil? Kennen Sie Ihre GD&T](https://hackaday.com/2018/10/04/how-precise-is-that-part-know-your-gdt/)
-   [GD&T für Anfänger \| Schritt für Schritt Ansatz zur Durchführung von GD&T für mechanisches Zeichnen (Video)](https://www.youtube.com/watch?v=-3tN7KvDUjQ)
-   [Straight To The Point Engineering (Video tutorials)](https://www.youtube.com/c/StraightToThePointEngineering/videos?view=0&sort=da&flow=grid)

[Category:Roadmap](Category:Roadmap.md) [Category:TechDraw](Category:TechDraw.md)

---
[documentation index](../README.md) > [Roadmap](Category:Roadmap.md) > Tolerancing/de
