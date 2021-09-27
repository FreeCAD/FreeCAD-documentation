# Development roadmap/de
**Wichtig: Viele dieser Planungen sind nicht aktuell oder vielleicht eingestellt. Diese Seite und die Seiten, auf die sie verweist, enthalten sehr wahrscheinlich veraltete Informationen. Eine 'weiche' Planung ist unter [http://www.freecadweb.org/tracker/roadmap_page.php bugtracker] (engl.) zu finden, aber bisher gibt es keine 'harte' Planung. Viele Anstrengungen verlaufen simultan.**

FreeCAD - obwohl in vielen Anwendungen verwendbar - steht am Anfang eines langen Weges in den CAD Mainstream. Es bleibt noch viel zu tun, um einen Zustand zu erreichen, in dem wir mit kommerzieller Software konkurrieren können.

Dieser Abschnitt gibt einen Überblick darüber, was geplant ist und gibt Dir die Möglichkeit, Dich zu beteiligen oder Deine Meinung zu äußern. Da wir Freiwillige bei FreeCAD sind, haben wir nur eine begrenzte Zeit. Wenn du also an einem der Themen interessiert und hilfsbereit bist, lass es uns einfach wissen! Wir verwenden den Stil _.

-   Das [Organization chart](Organization_chart.md) zeigt, wer was im FreeCAD Universum macht.
-   Du kannst Probleme, an denen derzeit gearbeitet wird, über den Bugtracker verfolgen: <http://www.freecadweb.org/tracker/roadmap_page.php>

## Projekte

  Projekt                                                                                        Beschreibung                                                                                                                                                       Kategorie                                                            Status
  ---------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------- ------------
  **[STEP Projekt](STEP_project/de.md)**                                                 über die Verbesserung und Weiterentwicklung der STEP Unterstützung in FreeCAD                                                                                      Modellierung, Dateiformate                                           Aktuell
  **[Benennungsprojekt](Naming_project/de.md)**                                          es geht um die Implementierung eines robusten Form Referenzierungsrahmens.                                                                                         Modellierung                                                         Aktuell
  **[FreeCAD Entwicklungsmodellprojekt](FreeCAD_development_model_project/de.md)**       FreeCAD in ein leistungsfähigeres Entwicklungsmodell überführen                                                                                                    Entwicklungsprozess                                                  Aktuell
  **[Skizziererprojekt](Sketcher_project/de.md)**                                        ist die laufende Implementierung des Beschränkung/Parameter Skizzierers                                                                                            Modellierung, 2D Beschränkungen                                      Aktuell
  **[PartDesign Projekt](PartDesign_project/de.md)**                                     ist das Bemühen in Richtung einer funktionierenden Teilekonstruktion in FreeCAD                                                                                    Modellierung                                                         Aktuell
  **[Zusammenbauprojekt](Assembly_project/de.md)**                                       erstellt ein Baugruppenmodul, das die Produkterstellung, Teillisten und einige Kinematiken handhabt.                                                               Modellierung, 3D Beschränkungen                                      \| Aktuell
  **[Architekturprojekt](Arch_Concept/de.md)**                                           wird die Grundlagen einer modernen, parametrischen Architekturmodellierungsumgebung schaffen.                                                                      Modellierung, BIM                                                    Aktuell
  **[Einheiten Projekt](Units_project/de.md)**                                           endlich FreeCAD dazu bringen, verschiedene Einheiten und Einheitensysteme zu erkennen.                                                                             Modellierung, Fertigungsdokumentation, Bemaßung und Referenzierung   \| Aktuell
  **[Ressourcen Rahmenprojekt](Resource_framework_project/de.md)**                       Adressierung der Nutzer Zusammenarbeit, [PDM](http://en.wikipedia.org/wiki/Product_Data_Management) Katalog/Standardteilmaterial                                   Cloud, Datenbanken, BOM                                              Aktuell
  **[Qualitätsprojekt](Quality_project/de.md)**                                          zielt darauf ab, unfertige Formelemente auszublenden und die Dokumentation zu verbessern.                                                                          Entwicklungsprozess                                                  Aktuell
  **[Strahlverfolgungsprojekt](Raytracing_project/de.md)**                               eine neue generische Schnittstelle für externe Renderer zur Visualisierung anbieten                                                                                3D Visualisierung                                                    Aktuell
  **[UTF Projekt](UTF_Project/de.md)**\'\'                                               zielt darauf ab, FreeCADs Coin3D Schnittstelle zu aktualisieren, um UTF Zeichenketten für eine bessere mehrsprachige Erfahrung mit Nicht ASCII Zeichen zu nutzen   Internationalisierung                                                Aktuell
  **[FEM Projekt](FEM_project/de.md)**                                                   stellt ein [FEM](http://en.wikipedia.org/wiki/Finite_element_method) Modul in FreeCAD zur Verfügung.                                                               Modellierung, Analyse                                                \| Aktuell
  **[Materialdatenmodell](Material_data_model/de.md)**                                   Versuch, ein Materialdatenmodell in FreeCAD zu beschreiben                                                                                                         \| Modellierung                                                      \| Aktuell
  **[Python 3](Python_3/de.md)**                                                         Portierung von FreeCAD nach Python 3.                                                                                                                              Entwicklungswerkzeuge                                                Aktuell
  **[HiDPI Unterstützung](HiDPI_support/de.md)**                                         Unterstützung der Skalierbarkeit auf 4K Displays.                                                                                                                  GUI                                                                  Aktuell
  **[Tolerierung](Tolerancing/de.md)**                                                   Die Unterstützung von Modellierungstoleranzen unter Verwendung internationaler Normen (ISO 1101 / ASME Y14.5, ISO 16792 / ASME Y14.41)                             Modellierung, Fertigungsdokumentation, Bemaßung und Referenzierung   Aktuell
  **[Landvermessungsarbeitsbereich Blaupause](Land_Survey_Workbench_Blueprint/de.md)**                                                                                                                                                                                                                                           Zukunft
  **[Roboterprojekt](Robot_project/de.md)**                                              Ein Robotersimulationsarbeitsbereich                                                                                                                               Modellierung, 3D Beschränkungen                                      Fertig
  **[Bildgestaltungsprojekt](Artwork_project/de.md)**                                    Ein Projekt zur Aktualisierung von Logo und Symbolen                                                                                                               GUI                                                                  Aktuell
                                                                                                                                                                                                                                                                                                                                         

## Veröffentlichungsplan

Wie in den meisten [FLOSS](http://en.wikipedia.org/wiki/FLOSS) Projekten ist ein Veröffentlichungsplan sehr grob. Es wird keine festen Termine geben und **\'\"Es ist erledigt, wenn es erledigt ist!\"**\'\'.

-   Die [Release process](Release_process.md) Seite versammelt Ideen für einen effizienteren Freigabe Arbeitsablauf.




_

---
[documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > Development roadmap/de
