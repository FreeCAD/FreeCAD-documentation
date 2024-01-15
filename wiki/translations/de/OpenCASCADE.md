# OpenCASCADE/de
## Beschreibung

[OpenCASCADE Technologie](OpenCASCADE/de.md), kurz **OCC** oder **OCCT**, ist eine Sammlung von C++ Bibliotheken, die zusammen einen professionellen Computer-Aided-Design-Kernel (CAD-Kernel) für die Modellierung von 2D- und 3D-Objekten und den Aufbau spezialisierter Werkzeuge für die Fertigung, Simulation oder Visualisierung bilden. OpenCASCADE ist das Herzstück der geometrischen Fähigkeiten von FreeCAD.

Die geometrischen Klassen von OCCT werden in FreeCAD hauptsächlich durch das Modul [Part](Part_Workbench/de.md) umgesetzt und zur Verfügung gestellt, von dem die meisten anderen [Arbeitsbereiche](Workbenches/de.md) abhängen. Es enthält auch interne Funktionen zum Lesen und Schreiben verschiedener Dateiformate wie STEP und IGES und zum Ausführen von 2D-Projektionen, die zur Erstellung technischer Zeichnungen in [TechDraw](TechDraw_Workbench/de.md) verwendet werden können.

<img alt="" src=images/Part_Workbench_relationships.svg  style="width:600px;">



*OpenCASCADE stellt dem Arbeitsbereich [Part](Part_Workbench/de.md) die grundlegenden geometrischen Klassen und Zeichenfunktionen zur Verfügung, welche dann von allen Arbeitsbereichen in FreeCAD verwendet werden.*

OpenCASCADE ist nicht zu verwechseln mit [OpenSCAD](https://www.openscad.org/), das ein anderes Open Source Projekt zur Erstellung von 3D-Modellen ist und über den Arbeitsbereich [OpenSCAD](OpenSCAD_Workbench/de.md) zugänglich ist.

OpenCASCADE ist freie Software und unterliegt den Bedingungen der GNU Lesser General Public License (LGPL) Version 2.1 mit einer zusätzlichen Ausnahme.

## Installation

OpenCASCADE ist eine Kernkomponente von FreeCAD. Wird FreeCAD über einen der Verweise auf der Seite [Herunterladen](Download/de.md) geladen, wird es auch installiert, und es ist keine weitere Installation erforderlich.

Wenn du jedoch Anwendungen entwickeln möchtest, die OCCT verwenden, oder C++ Code zu FreeCAD beitragen möchtest, dann musst du die Entwicklungsdateien von OCCT installieren. In diesem Fall wird die Prozedur unter [Kompilieren](Compiling/de.md) für jedes der Hauptsysteme, Linux, Windows und MacOS, erklärt.



## Gemeinschaftsausgabe

Eine \"Gemeinschaftsausgabe\" von OpenCASCADE, abgekürzt OCE, wurde 2011 veröffentlicht, die auf den offiziellen OpenCASCADE Quellen (OCCT) der Version 6.5 basiert. Theoretisch sollte die Community Edition OCE in den meisten Aspekten mit der Hauptversion OCCT kompatibel sein, wobei einige zusätzliche Codes von der Gemeinschaft beigesteuert werden sollten.

Diese alternative Distribution stoppte jedoch um 2017 die aktive Entwicklung und blieb in Bezug auf Funktionen und Fehlerbehebungen hinter der Hauptversion zurück. Aus diesem Grund wird FreeCAD seit FreeCAD v0.17 ausschließlich mit OCCT kompiliert und OCE wird nicht getestet.

In einigen älteren Linux-Distributionen wird FreeCAD gegen OCE 0.18, äquivalent zu OCCT 6.9.x, kompiliert, was verschiedene Probleme verursacht, die bereits in den Hauptversionen von OCCT 7.x gelöst wurden. Wenn dies der Fall ist, versuche, OCE zu entfernen und stattdessen OCCT zu installieren. Falls dies nicht möglich ist, verwende das [AnwendungsAbbild](AppImage/de.md), um ein modernes FreeCAD mit einer aktualisierten OCCT-Version zu erhalten.



## Geschichte

Der geometrische Kernel von Cas.CADE war ursprünglich Closed-Source, wurde aber um das Jahr 2000 unter seinem heutigen Namen Open-Source. Kurz danach wurde das FreeCAD-Projekt gestartet, wobei die ältesten Dateien auf Januar 2001 datiert sind. Lies mehr unter [Geschichte](History/de.md).

OpenCASCADE Version 6.6 und früher wurde durch eine eigene öffentliche Lizenz \"OCCT public license\" reguliert, was es nicht gänzlich zu \"freier Software\" machte. Dies wurde mit der Veröffentlichung von OCCT 6.7 (2013) gelöst, als es die LGPL2-Lizenz übernahm.



## OCCT geometrische Konzepte 

In der OpenCascade-Terminologie unterscheiden wir zwischen geometrischen Grundelementen (engl.: primitives) und topologischen Formen. Ein geometrisches Grundelement kann ein Punkt, eine Linie, ein Kreis, eine Ebene usw. oder sogar einige komplexere Typen wie eine B-Spline-Kurve oder eine Oberfläche sein. Eine Form kann ein Knoten, eine Kante, ein Draht, eine Fläche, ein Solid oder eine Verbindung aus anderen Formen sein. Die geometrischen Grundelemente sind nicht dazu bestimmt, direkt in der 3D-Szene dargestellt zu werden, sondern als Baugeometrie für Formen zu dienen. So kann beispielsweise eine Kante aus einer Linie oder aus einem Teil eines Kreises konstruiert werden.

Zusammenfassend lässt sich sagen, dass Geometrie-Grundelemente \"formlose\" Bausteine sind, während [topologische Formen](Part_TopoShape/de.md) die darauf aufgebauten realen Objekte sind.

Eine vollständige Liste aller Grundelemente und Formen findet man in der [OCC-Dokumentation](https://dev.opencascade.org/resources/documentation) (Alternativ: [sourcearchive.com](https://www.opencascade.com/doc/occt-7.4.0/refman/html/)) wenn man nach **Geom\_\*** (für geometrische Grundelemente) und **TopoDS\_\*** (für Formen) sucht. Dort kann man auch mehr über die Unterschiede zwischen ihnen lesen. Bitte beachte, dass die offizielle OCC-Dokumentation nicht online verfügbar ist (Du musst ein Archiv herunterladen) und sich hauptsächlich an Programmierer und nicht an Endbenutzer richtet. Aber hoffentlich findest du hier genügend Informationen, um anzufangen. Siehe auch [Benutzerhandbuch zur Datenmodellierung](https://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__modeling_data.html).

> *Auf einer sehr hohen Stufe sagt die Topologie aus, aus welchen Teilen ein Objekt besteht und welche logischen Beziehungen zwischen ihnen bestehen. Eine Form besteht aus einem bestimmten Satz von Flächen. Eine Fläche wird durch einen bestimmten Satz von Kanten begrenzt. Zwei Flächen sind benachbart, wenn sie eine gemeinsame Kante besitzen.*

> *Die Topologie allein sagt dir nichts über die Größe, Krümmung oder 3D-Positionen jedes dieser Teile. Jedes Teil der Topologie weiß jedoch über seine zugrundeliegende Geometrie Bescheid. Eine Fläche weiß, auf welcher Oberfläche sie liegt. Eine Kante weiß, auf welcher Kurve sie liegt. Die Geometrie weiß über Krümmung und Lage im Raum Bescheid..* - [Quelle](https://www.opencascade.com/content/geometry-and-topology)


<hr />

> *So definiert die Topologie die Beziehung zwischen einfachen geometrischen Einheiten, die miteinander verbunden werden können, um komplexe Formen darzustellen.* - [Benutzerhandbuch zur Datenmodellierung](https://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__modeling_data.html)

![](images/ClassTopoDS_Shape_inherit_graph.png )

**Hinweis:** Nur 3 Arten von topologischen Objekten haben geometrische Abbilder - Knoten, Kante und Fläche ([Quelle](https://opencascade.blogspot.com/2009/02/topology-and-geometry-in-open-cascade.html)).

Die geometrischen Typen lassen sich tatsächlich in zwei große Gruppen unterteilen: Kurven und Oberflächen. Aus den Kurven (Linie, Kreis, \...) kann man direkt eine Kante bauen, aus den Oberflächen (Ebene, Zylinder,\...) kann man eine Fläche bauen. So ist beispielsweise die geometrische Grundlinie unbegrenzt, d.h. sie wird durch einen Basisvektor und einen Richtungsvektor definiert, während ihre Formdarstellung irgendetwas sein muss, das durch einen Start- und Endpunkt begrenzt ist. Und ein Quader - ein Festkörper - kann durch sechs begrenzte Ebenen erstellt werden.

Von einer Kante oder Fläche aus kannst du auch zu seinem geometrischen Grundelement-Gegenstück zurückkehren.

So können aus Formen sehr komplexe Teile gebaut oder umgekehrt alle Unterformen extrahiert werden, aus denen eine komplexere Form besteht.

<img alt="" src=images/Part_TopoShape_relationships.svg  style="width:600px;">



*Die Klasse `Part::TopoShape* ist das geometrische Objekt, das auf dem Bildschirm zu sehen ist. Im Wesentlichen verwenden alle Arbeitsbereiche intern diese [TopoFormen](Part_TopoShape/de.md) um Kanten, Flächen und Festkörper zu erstellen und anzuzeigen.`



## Verwandt

-   OpenCASCADE Technologie (OCCT) [Hauptwebsite](http://www.opencascade.com)
-   OCCT [Entwicklungsportal](https://dev.opencascade.org/)
-   OCCT [letzte Version](https://www.opencascade.com/content/latest-release)
-   OCCT [git Repositorium](https://git.dev.opencascade.org/gitweb/?p=occt.git)
-   OpenCASCADE Gemeinschaftsausgabe (OCE) [git Repositorium](https://github.com/tpaviot/oce)
-   [Open Cascade Technologie OCCT](http://en.wikipedia.org/wiki/Open_Cascade_Technology) auf Wikipedia
-   Glossar, [Open CASCADE](Glossary/de#Open_CASCADE.md)
-   Verfolgung von OCCT Fehlern im FreeCAD Bugtracker [(Beitrag)](https://forum.freecadweb.org/viewtopic.php?f=10&t=20264)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > OpenCASCADE/de
