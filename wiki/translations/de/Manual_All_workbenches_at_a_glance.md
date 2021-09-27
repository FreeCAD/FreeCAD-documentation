# Manual:All workbenches at a glance/de
{{Manual:TOC/de}}

Eine der größten Schwierigkeiten für neue Benutzer von FreeCAD, ist zu wissen, in welchem Arbeitsbereich ein bestimmtes Werkzeug zu finden ist. Die folgende Tabelle gibt einen Überblick über die wichtigsten Arbeitsbereiche und deren Werkzeuge. Eine vollständigere Liste findest du auf jeder Seite [Arbeitsbereich](Workbenches/de.md) in der FreeCAD Dokumentation.

Vier Arbeitsbereiche sind ebenfalls für die Arbeit in Paaren ausgelegt, wobei einer von ihnen vollständig in den anderen integriert ist: Arch enthält alle Entwurfswerkzeuge und PartDesign alle Skizzierer-Werkzeuge. Aus Gründen der Übersichtlichkeit sind sie jedoch unten getrennt.

### Part

Der Part Arbeitsbereich bietet grundlegende Werkzeuge für die Arbeit mit Volumenkörpern: Primitive, wie Würfel und Kugeln, und einfache geometrische Operationen und boolesche Operationen. Als Hauptankerpunkt bei [OpenCasCade](https://en.wikipedia.org/wiki/Open_Cascade_Technology) bietet der Part Arbeitsbereich die Grundlage des Geometriesystems von FreeCAD, und fast alle anderen Arbeitsbereiche erzeugen eine Teil-basierte Geometrie.

  Werkzeug                                                                                                            Beschreibung                                                                                    Werkzeug                                                                                                                     Beschreibung
  ------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------
  <img alt="" src=images/Part_Box.svg  style="width:32px;"> _                                          Zeichnet einen Kegel
  <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> _                                    Zeichnet eine Kugel
  <img alt="" src=images/Part_Torus.svg  style="width:32px;"> _            Erstellt verschiedene andere parametrische geometrische Primitive
  <img alt="" src=images/Part_Builder.svg  style="width:32px;"> _                                 Verschmilzt (Vereinigt) zwei Objekte
  <img alt="" src=images/Part_Common.svg  style="width:32px;"> _                                               Schneidet (subtrahiert) ein Objekt von einem anderen
  <img alt="" src=images/Part_JoinConnect.svg  style="width:32px;"> _                   Bettet ein Hohlobjekt in ein anderes Hohlobjekt ein
  <img alt="" src=images/Part_JoinCutout.svg  style="width:32px;"> _                           Extrudiert ebene Flächen eines Objekts
  <img alt="" src=images/Part_Fillet.svg  style="width:32px;"> _                                Erstellt einen Festkörper durch Drehung eines anderen (nicht festen) Objekts um eine Achse
  <img alt="" src=images/Part_Section.svg  style="width:32px;"> _   Erstellt mehrfache Querschnitte entlang eines Objektes
  <img alt="" src=images/Part_Chamfer.svg  style="width:32px;"> _                                  Spiegelt das ausgewählte Objekt auf einer vorgegebenen Spiegelebene
  <img alt="" src=images/Part_RuledSurface.svg  style="width:32px;"> _                                  Trägt ein oder mehrere Profile entlang eines Pfades aus
  <img alt="" src=images/Part_Loft.svg  style="width:32px;"> _                                  Erstellt eine maßstabgetreue Kopie des Originalobjekts
  <img alt="" src=images/Part_Thickness.svg  style="width:32px;"> [Dicke](Part_Thickness/de.md)                  Den Flächen einer Form eine Dicke zuweisen                                                                                                                                                                                   

### Entwurf

Der Arbeitsbereich Entwurf bietet Werkzeuge zur Durchführung grundlegender 2D CAD Entwurfsaufgaben: Linien, Kreise, usw\... und eine Reihe grundlegender praktischer Werkzeuge wie Verschieben, Drehen oder Skalieren. Sie bietet auch verschiedene Zeichenhilfen, wie Gitter und Fangen. Es ist hauptsächlich dazu gedacht, die Richtlinien für Architekturobjekte zu zeichnen, dient aber auch als FreeCADs \"Schweizer Messer\".

  Werkzeug                                                                                                                     Beschreibung                                                                  Werkzeug                                                                                                                 Beschreibung
  ---------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/Draft_Line.svg  style="width:32px;"> _                                   Zeichnet eine Linie aus mehreren Liniensegmenten (Polylinie)
  <img alt="" src=images/Draft_Circle.svg  style="width:32px;"> _                                      Zeichnet ein Bogensegment aus Mittelpunkt, Radius, Startwinkel und Endwinkel
  <img alt="" src=images/Draft_Ellipse.svg  style="width:32px;">_                        Zeichnet ein regelmäßiges Polygon aus einem Mittelpunkt und einem Radius
  <img alt="" src=images/Draft_Rectangle.svg  style="width:32px;"> _                                    Zeichnet eine mehrzeilige Textanmerkung
  <img alt="" src=images/Draft_Dimension.svg  style="width:32px;"> _                        Zeichnet einen B-Spline aus einer Reihe von Punkten
  <img alt="" src=images/Draft_Point.svg  style="width:32px;"> _   Die Formzeichenfolge fügt eine Verbundform, die einen Textzeichenfolge darstellt, an einer bestimmten Stelle im aktuellen Dokument ein
  <img alt="" src=images/Draft_Facebinder.svg  style="width:32px;"> _                 Zeichnet eine Bézierkurve aus einer Reihe von Punkten
  <img alt="" src=images/Draft_Move.svg  style="width:32px;"> _                            Dreht Objekte in einem bestimmten Winkel um einen Punkt
  <img alt="" src=images/Draft_Offset.svg  style="width:32px;"> _                            Stutzt, dehnt oder extrudiert ein Objekt
  <img alt="" src=images/Draft_Upgrade.svg  style="width:32px;"> _           Verwandelt oder trennt Objekte in ein untergeordnetes Objekt
  <img alt="" src=images/Draft_Scale.svg  style="width:32px;"> _    Erstellt ein 2D-Objekt, das eine abgeflachte Ansicht eines anderen Objekts ist.
  <img alt="" src=images/Draft_Draft2Sketch.svg  style="width:32px;"> _    Erstellt eine rechteckige Anordnung aus einem Objekt
  <img alt="" src=images/Draft_Clone.svg  style="width:32px;"> [Klon](Draft_Clone/de.md)                                     Erstellt verknüpfte Kopien von Objekten                                                                                                                                                                
  <img alt="" src=images/Draft_Mirror.svg  style="width:32px;"> [Spiegeln](Draft_Mirror/de.md)                              Spiegelt Objekte quer zu einer Linie                                                                                                                                                                   

### Skizzierer

Der Skizzierer Arbeitsbereich enthält Werkzeuge zum Erstellen und Bearbeiten komplexer 2D Objekte, genannt Skizzen. Die Geometrie innerhalb dieser Skizzen kann durch die Verwendung von Beschränkungen präzise positioniert und in Beziehung gesetzt werden. Sie sind in erster Linie als Bausteine der PartDesign Geometrie gedacht, sind aber überall in FreeCAD nützlich.

  Werkzeug                                                                                                                                                         Beschreibung                                                                                                                                                                              Werkzeug                                                                                                                                                     Beschreibung
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:32px;"> _                                                        Zeichnet einen Linienabschnitt aus zwei Punkten
  <img alt="" src=images/Sketcher_Arc.svg  style="width:32px;"> _                    Zeichnet ein Bogensegment aus zwei Endpunkten und einem weiteren Punkt auf dem Umfang
  <img alt="" src=images/Sketcher_Circle.svg  style="width:32px;"> _          Zeichnet einen Kreis aus drei Punkten auf dem Umfang
  <img alt="" src=images/Sketcher_CreateEllipse.svg  style="width:32px;"> _   Zeichnet eine Ellipse nach Hauptdurchmesser (2 Punkte) und Nebenradiuspunkt
  <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> _                            Zeichnet eine Linie, die aus mehreren Liniensegmenten besteht. Mehrere Zeichenmodi verfügbar
  <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> _                              Zeichnet ein regelmäßiges Dreieck, einbeschrieben in einen Kreis der Konstruktionsgeometrie
  <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> _                              Zeichnet ein regelmäßiges Fünfeck, einbeschrieben in einen Kreis der Konstruktionsgeometrie
  <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> _                            Zeichnet ein regelmäßiges Siebeneck, einbeschrieben in einen Kreis der Konstruktionsgeometrie
  <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width:32px;"> _                                              Zeichnet ein Oval durch Auswahl des Zentrums eines Halbkreises und eines Endpunktes des anderen Halbkreises
  <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> _                                                Stutzt eine Linie, einen Kreis oder einen Bogen in Bezug auf einen angeklickten Punkt
  <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> _       Schaltet ein Element in den/aus dem Konstruktionsmodus um. Ein Konstruktionsobjekt wird nicht in einer 3D Geometrieoperation verwendet und ist nur während der Bearbeitung der Skizze, die es enthält, sichtbar.
  <img alt="" src=images/Constraint_PointOnPoint.svg  style="width:32px;"> _        Befestigt einen Punkt auf einem anderen Objekt, z.B. einer Linie, einem Bogen oder einer Achse.
  <img alt="" src=images/Constraint_Vertical.svg  style="width:32px;"> _                       Beschränkt die ausgewählten Linien oder Polylinienelemente auf eine echte horizontale Anordnung. Es kann mehr als ein Objekt ausgewählt werden, bevor diese Beschränkung angewendet wird.
  <img alt="" src=images/Constraint_Parallel.svg  style="width:32px;"> _               Beschränkt zwei Linien, die senkrecht zueinander stehen, oder beschränkt eine Linie, die senkrecht zu einem Bogenendpunkt steht.
  <img alt="" src=images/Constraint_Tangent.svg  style="width:32px;"> _                          Beschränkt zwei gewählte Einheiten gleich zueinander. Wenn sie auf Kreise oder Bögen angewendet werden, werden ihre Radien gleich gesetzt.
  <img alt="" src=images/Constraint_Symmetric.svg  style="width:32px;"> _                                 Beschränkt das ausgewählte Element, indem vertikale und horizontale Abstände relativ zum Ursprung festgelegt werden, wodurch die Position dieses Elements gesperrt wird.
  <img alt="" src=images/Constraint_HorizontalDistance.svg  style="width:32px;"> _       Fixiert den vertikalen Abstand zwischen 2 Punkten oder Linienendpunkten. Wenn nur ein Punkt ausgewählt ist, wird der Abstand auf den Ursprung gesetzt.
  <img alt="" src=images/Constraint_Length.svg  style="width:32px;"> _                                          Definiert den Radius eines ausgewählten Bogens oder Kreises durch Beschränkung des Radius.
  <img alt="" src=images/Constraint_InternalAngle.svg  style="width:32px;"> _                   Beschränkt zwei Linien auf die Einhaltung eines Brechungsgesetzes, um das durch eine Grenzfläche gehende Licht zu simulieren
  <img alt="" src=images/Constraint_InternalAlignment.svg  style="width:32px;"> _                                     Weist eine Skizze der zuvor ausgewählten Seite eines Volumenkörpers zu
  <img alt="" src=images/Sketcher_MergeSketch.svg  style="width:32px;"> _                                   Spiegelt ausgewählte Elemente einer Skizze

### Part Design 

Der Part Design Arbeitsbereich enthält fortgeschrittene Werkzeuge zum Erstellen von Volumenteilen. Sie enthält auch alle Werkzeuge aus dem Skizzierer. Da sie nur feste Formen erzeugen kann (die Regel Nummer eins der Teilekonstruktion), ist sie die Hauptarbeitsstation, die bei der Konstruktion von Teilen, die hergestellt oder in 3D ausgedruckt werden sollen, verwendet wird, da Sie immer ein druckbares Objekt erhalten.

  Werkzeug                                                                                                                                  Beschreibung                                                                                      Werkzeug                                                                                                                                              Beschreibung
  ----------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------
  <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> _                                          Erstellt eine Tasche aus einer ausgewählten Skizze. Die Skizze muss auf die Fläche eines vorhandenen Festkörpers abgebildet werden.
  <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> _                                             Erzeugt eine Nut durch Drehen einer Skizze um eine Achse
  <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> _                                      Anfasen von Kanten eines Objekts
  <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> _                                Spiegelt Grundelementen auf einer Ebene oder einer Fläche.
  <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> _                   Erzeugt ein polares Muster von Grundelementen
  <img alt="" src=images/PartDesign_Scaled.svg  style="width:32px;"> _     Ermöglicht die Erstellung eines Musters mit einer beliebigen Kombination der anderen Transformationen
  <img alt="" src=images/PartDesign_WizardShaft.svg  style="width:32px;"> _   Ermöglicht die Erstellung verschiedener Arten von Zahnrädern

### Architektur

Der Architektur Arbeitsbereich enthält Werkzeuge für die Arbeit mit [Bauwerksdatenmodellierung](https://de.wikipedia.org/wiki/Building_Information_Modeling) (englisch: Building Information Modeling; kurz: BIM) Projekten (Bauwesen und Architektur). Sie enthält auch alle Werkzeuge des Arbeitsbereichs Entwurf. Die Hauptanwendung des Architektur Arbeitsbereich ist BIM Objekte zu erstellen oder BIM Attributen Objekten zu verleihen, die mit anderen Arbeitsbereichen gebaut wurden, um sie dann nach [Industry Foundation Classes](https://de.wikipedia.org/wiki/Industry_Foundation_Classes) zu exportieren.

  Werkzeug                                                                                                  Beschreibung                                                                    Werkzeug                                                                                                             Beschreibung
  --------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------
  <img alt="" src=images/Arch_Wall.svg  style="width:32px;"> _                Erzeugt ein Strukturelement von Grund auf oder mit einem ausgewählten Objekt als Basis
  <img alt="" src=images/Arch_Rebar.svg  style="width:32px;"> _                               Erstellt eine Etage mit ausgewählten Objekten
  <img alt="" src=images/Arch_Building.svg  style="width:32px;"> _                                Erstellt ein Gelände mit ausgewählten Objekten
  <img alt="" src=images/Arch_Window.svg  style="width:32px;"> _   Fügt dem Dokument ein Schnittebenenobjekt hinzu
  <img alt="" src=images/Arch_Axis.svg  style="width:32px;"> _                                   Erstellt ein Schrägdach aus einer ausgewählten Fläche
  <img alt="" src=images/Arch_Space.svg  style="width:32px;"> _                          Erzeugt ein Treppenobjekt im Dokument
  <img alt="" src=images/Arch_Panel.svg  style="width:32px;"> _                              Erzeugt ein Rahmenobjekt aus einem ausgewählten Layout
  <img alt="" src=images/Arch_Equipment.svg  style="width:32px;"> _          Weist ausgewählten Objekten ein Material zu
  <img alt="" src=images/Arch_Schedule.svg  style="width:32px;"> _               Ein Objekt nach einer Ebene schneiden
  <img alt="" src=images/Arch_Add.svg  style="width:32px;"> _                        Subtrahiert oder entfernt Objekte von einer Komponente
  <img alt="" src=images/Arch_Survey.svg  style="width:32px;"> [Vermessung](Arch_Survey/de.md)            Beginnt oder verlässt den Vermessungsmodus                                                                                                                                                           

### Zeichnen


**Entwicklung der [Arbeitsbereich Zeichnung](Drawing_Workbench/de.md) wurde in FreeCAD 0.16 eingestellt, und die neue [TechDraw Arbeitsbereich](TechDraw_Workbench/de.md), die diese ersetzen soll, wurde in v0.17 eingeführt. Der Arbeitsbereich Zeichnung kann in zukünftigen Versionen entfernt werden. Verwende stattdessen den TechDraw Arbeitsbereich.**

Der Arbeitsbereich Zeichnung übernimmt die Erstellung und Bearbeitung von 2D Zeichnungsblättern, die für die Anzeige von Ansichten Ihrer 3D Arbeiten in 2D verwendet werden. Diese Blätter können dann in 2D Anwendungen im SVG oder DXF Format, in eine PDF Datei oder zum Drucken exportiert werden.

  Werkzeug                                                                                                                     Beschreibung                                                                         Werkzeug                                                                                                                            Beschreibung
  ---------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------
  <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> _                                      Fügt eine Ansicht des ausgewählten Objekts in das aktive Zeichnungsblatt ein
  <img alt="" src=images/Drawing_Annotation.png  style="width:32px;"> _                                         Fügt dem aktuellen Zeichenblatt eine Clip Gruppe hinzu
  <img alt="" src=images/Drawing_Openbrowser.png  style="width:32px;"> _   Erstellt automatisch orthographische Ansichten eines Objekts auf dem aktuellen Zeichenblatt
  <img alt="" src=images/Drawing_Symbol.png  style="width:32px;"> _               Fügt eine spezielle Entwurfsansicht des ausgewählten Objekts in das aktuelle Zeichnungsblatt ein
  <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Speichern](Drawing_Save/de.md)                             Speichert das aktuelle Blatt als SVG Datei                                                                                                                                                                               

### Andere eingebaute Arbeitsbereiche 

Obwohl das oben genannte die wichtigsten Werkzeuge von FreeCAD zusammenfasst, sind viele weitere Arbeitsbereiche verfügbar, darunter:

-   Der [Polygonnetz Arbeitsbereich](Mesh_Workbench/de.md) erlaubt die Arbeit mit [Polygonnetzen](https://de.wikipedia.org/wiki/Polygonnetz). Obwohl Polygonnetze nicht der bevorzugte Typ von Geometrie sind, mit der man in FreeCAD arbeitet, wegen ihrer fehlenden Präzision und Unterstützung für Kurven, haben Polygonnetze immer noch eine Menge Anwendungsmöglichkeiten und werden von FreeCAD voll unterstützt.

Der Polygonnetz Arbeitsbereich bietet auch eine Reihe von Teil-zu-Netz und Netz-zu-Teil Werkzeugen.

-   Der [Arbeitsbereich Strahlverfolgung](Raytracing_Workbench/de.md) bietet Werkzeuge zur Anbindung an externe Renderer wie povray oder luxrender. Direkt aus FreeCAD heraus erlaubt dir dieser Arbeitsbereich, hochwertige qualitativ hochwertige Renderings von deinen Modellen zu erstellen.
-   Der [Arbeitsbereich Tabellenkalkulation](Spreadsheet_Workbench/de.md) gestattet die Erstellung und Veränderung von Tabellenkalkulationsdaten, die aus FreeCAD Modellen extrahiert werden können. Tabellenkalkulationszellen können auch in vielen Bereichen von FreeCAD referenziert werden, so dass sie als Stammdatenstrukturen verwendet werden können.
-   Der [FEM Arbeitsbereich](FEM_Workbench/de.md) beschäftigt sich mit [Finite-Elemente-Methode](https://de.wikipedia.org/wiki/Finite-Elemente-Methode) und gestattet die Durchführung von Vor- und Nach-Bearbeitung von FEM Berechnungen und die grafische Darstellung der Ergebnisse.

### Externe Arbeitsbereiche 

Es gibt auch eine Reihe anderer sehr nützlicher Arbeitsbereiche, die von Mitgliedern der FreeCAD Gemeinschaft hergestellt wurden. Obwohl sie nicht in einer Standard FreeCAD Installation enthalten sind, lassen sie sich als Plug-Ins einfach installieren. Sie sind alle im [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons) Repositorium referenziert. Zu den am weitesten entwickelten gehören:

-   Die [Zeichnung Bemessung Arbeitsbereich](https://github.com/hamish2014/FreeCAD_drawing_dimensioning) bietet viele neue Werkzeuge, mit denen du direkt auf den Zeichenblättern arbeiten und Bemaßungen, Anmerkungen und andere technische Symbole mit großer Kontrolle über deren Aussehen hinzufügen kannst. Der Zeichnungsbemaßung Arbeitsbereich wird nicht mehr gepflegt.
-   Die [Arbeitsbereich Verbindungselemente](https://github.com/shaise/FreeCAD_FastenersWB) bietet eine große Bandbreite an einbaufertigen Verbindungselementen wie Schrauben, Bolzen, Stäbe, Unterlegscheiben und Muttern. Viele Optionen und Einstellungen sind verfügbar.
-   Der [A2plus](https://github.com/kbwbe/A2plus) Arbeitsbereich bietet eine Reihe von Werkzeugen zur Montage und Arbeit mit [Baugruppen](https://en.wikipedia.org/wiki/Assembly_modelling).

**Mehr lesen**

-   [Die vollständige Liste der Arbeitsbereiche](Workbenches/de.md)
-   [Der Part Arbeitsbereich](Part_Workbench/de.md)
-   [Der Entwurf Arbeitsbereich](Draft_Workbench/de.md)
-   [Der Part Design Arbeitsbereich](PartDesign_Workbench/de.md)
-   [Der Arch Arbeitsbereich](Arch_Workbench/de.md)
-   [Der TechDraw Arbeitsbereich](TechDraw_Workbench/de.md)
-   [Der FEM Arbeitsbereich](FEM_Workbench/de.md)
-   [Die FreeCAD-Erweiterungen Repositorien](https://github.com/FreeCAD/FreeCAD-addons)

---
[documentation index](../README.md) > Manual:All workbenches at a glance/de
