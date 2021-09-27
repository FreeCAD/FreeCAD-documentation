# <img alt="Oberfläche Arbeitsbereichssymbol" src=images/Workbench_Surface.svg  style="width:64px;"> Surface Workbench/de


{{TOCright}}

## Einführung

Die <img alt="" src=images/Workbench_Surface.svg  style="width:24px;"><img src=images/Part_Builder.svg style="width:Arbeitsbereich Oberfläche](Surface_Workbench/de.md) bietet Werkzeuge zum Erstellen und Ändern einfacher _** Werkzeug wenn die **Fläche aus Kanten** Option verwendet wird. Im Gegensatz zu diesem Werkzeug sind die Werkzeuge des Arbeitsbereichs Oberfläche jedoch parametrisch und bieten zusätzliche Optionen. In dieser Hinsicht ähneln die Werkzeuge in diesem Arbeitsbereich Funktionen wie **[16px"> <img src=images/PartDesign_AdditivePipe.svg style="width:PartDesign AdditiveAusformung](PartDesign_AdditiveLoft/de.md)** und **[16px">[PartDesign AdditivesRohr](PartDesign_AdditivePipe/de.md)**.

Einige der angebotenen Funktionen sind:

-   Erzeugung von Flächen aus Begrenzungskanten.
-   Ausrichtung der Krümmung von benachbarten Flächen.
-   Beschränkung der Oberflächen auf zusätzliche Kurven und Ecken.
-   Verlängerung der Flächen.
-   Ein Netz kann als Vorlage verwendet werden, um Polynomzug Kurven auf seiner Oberfläche zu erstellen.

<img alt="" src=images/Surface_example.png  style="width:350px;">

## Verwendung

Der Arbeitsbereich Oberfläche bezweckt, Flächen mit Formen zu erstellen, was mit den Standardwerkzeugen anderer Arbeitsbereiche nicht möglich ist.

<img alt="" src=images/Toy_Duck.png  style="width:350px;">


*Fläche, die mit Skizzen erstellt wurde, platziert in Bezugsebenen mit den Werkzeugen des [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md)*

Der Oberflächen Arbeitsbereich lässt sich mit anderen Arbeitsbereichen von FreeCAD integrieren. Das obige Beispiel wurde aus **<img src=images/Sketcher_NewSketch.svg style="width:16px"><img src=images/PartDesign_Plane.svg style="width:Skizzen](Sketch/de.md)** erstellt, die auf **_ platziert wurden. Die Konstruktion kann voll parametrisch sein, wenn alle Bezugsebenen und Skizzen entsprechend definiert sind. In den meisten Fällen reicht es aus, beim Zeichnen einer geschlossenen Skizze den Rand für eine Fläche zu definieren; dann stehen Optionen für weitere Formänderungen zur Verfügung.

Die generierte Oberfläche kann nicht mehr innerhalb eines **<img src=images/PartDesign_Body.svg style="width:16px"> <img src=images/Std_Part.svg style="width:PartDesign Körper](PartDesign_Body/de.md)** platziert werden. Jedoch kann die generierte Oberfläche in einem **_** enthalten sein, der die Bezugsebenen und Skizzen enthält. Das nicht-parametrische **[16px"> [Part Builder](Part_Builder/de.md)** Werkzeug kann dann verwendet werden, um eine [Schale](Glossar#Shell/de.md) und schließlich ein [Festkörper](Glossar#Solid/de.md) zu erstellen.

## Werkzeuge

-   <img alt="" src=images/Surface_Filling.svg  style="width:32px;"> [Füllung](Surface_Filling/de.md): füllt eine Reihe von Grenzkurven mit einer Oberfläche.

-   <img alt="" src=images/Surface_GeomFillSurface.svg  style="width:32px;"> [Fülle Grenzkurven](Surface_GeomFillSurface/de.md): erzeugt eine Oberfläche aus zwei, drei oder vier Grenzkanten.

-   <img alt="" src=images/Surface_Sections.svg  style="width:32px;"> [Abschnitte](Surface_Sections/de.md): erzeugt eine Oberfläche aus Kanten, die transversale Schnitte der Oberfläche darstellen. {{Version/de|0.19}}

-   <img alt="" src=images/Surface_ExtendFace.svg  style="width:32px;"> [Fläche ausdehnen](Surface_ExtendFace/de.md): extrapoliert die Oberfläche an den Grenzen mit ihrem lokalen U Parameter und V Parameter.

-   <img alt="" src=images/Surface_CurveOnMesh.svg  style="width:32px;"> _.





{{Surface Tools navi

}} 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Surface Workbench/de
