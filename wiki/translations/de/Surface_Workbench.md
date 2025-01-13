# <img alt="Symbol des Arbeitsbereichs Surface" src=images/Workbench_Surface.svg  style="width:64px;"> Surface Workbench/de






## Einleitung

Der Arbeitsbereich <img alt="" src=images/Workbench_Surface.svg  style="width:24px;">[Suface](Surface_Workbench/de.md) enthält Werkzeuge zum Erstellen und Ändern einfacher [NURBS-Oberflächen](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline). Diese Werkzeuge haben eine ähnliche Funktionalität wie das Werkzeug **[<img src=images/Part_Builder.svg style="width:16px"> [Part Formgenerator](Part_Builder/de.md)** wenn die **Fläche aus Kanten** Option verwendet wird. Im Gegensatz zu diesem Werkzeug sind die Werkzeuge des Arbeitsbereichs Surface jedoch parametrisch und bieten zusätzliche Optionen. In dieser Hinsicht ähneln die Werkzeuge in diesem Arbeitsbereich solchen wie **[<img src=images/PartDesign_AdditiveLoft.svg style="width:16px"> [PartDesign Ausformung](PartDesign_AdditiveLoft/de.md)** und **[<img src=images/PartDesign_AdditivePipe.svg style="width:16px"> [PartDesign Rohr](PartDesign_AdditivePipe/de.md)**.

Einige der enthaltenen Funktionen sind:

-   Flächen aus Randkurven erstellen.
-   Krümmungsstetigkeit zu benachbarten Flächen festlegen.
-   Oberflächen durch zusätzliche Kurven und Knotenpunkte abstimmen.
-   Flächen verlängern.
-   Ein Netz kann als Vorlage verwendet werden, um Spline-Kurven auf seiner Oberfläche zu erstellen.

<img alt="" src=images/Surface_example.png  style="width:350px;">



## Anwendung

Der Arbeitsbereich Surface bezweckt, Flächen mit Formen zu erstellen, die mit den Standardwerkzeugen anderer Arbeitsbereiche nicht möglich sind.

<img alt="" src=images/Toy_Duck.png  style="width:350px;">



*Oberfläche, aus Skizzen erstellt, die auf Bezugsebenen angeordnet sind, mit den Werkzeugen des Arbeitsbereichs [PartDesign](PartDesign_Workbench/de.md)*

Der Arbeitsbereich Surface ist an die anderen Arbeitsbereichen von FreeCAD angepasst. Das obige Beispiel wurde im Arbeitsbereich <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/de.md) aus **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Skizzen](Sketch/de.md)** erstellt, die auf **[<img src=images/PartDesign_Plane.svg style="width:16px"> [PartDesign Bezugsebenen](PartDesign_Plane/de.md)** angelegt wurden. Die Konstruktion kann voll parametrisch sein, wenn alle Bezugsebenen und Skizzen entsprechend definiert sind. In den meisten Fällen reicht es aus eine geschlossenen Skizze zu zeichnen, um die Kontur einer Fläche festzulegen und dann verschiedene Möglichkeiten zur weiteren Formanpassung zu nutzen.

Die generierte Oberfläche kann nicht mehr innerhalb eines **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Körpers](PartDesign_Body/de.md)** abgelegt werden. Jedoch kann ein **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/de.md)** die generierte Oberfläche enthalten, zusammen mit dem zugehörigen **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Körper](PartDesign_Body/de.md)**, der die Bezugsebenen und Skizzen enthält. Das nicht-parametrische Werkzeug **[<img src=images/Part_Builder.svg style="width:16px"> [Part Formgenerator](Part_Builder/de.md)** kann dann verwendet werden, um einen [Hüllkörper](Glossary/de#Shell.md) und schließlich einen [Festkörper](Glossary/de#Solid.md) zu erstellen.



## Werkzeuge

-   <img alt="" src=images/Surface_Filling.svg  style="width:32px;"> [Füllfläche](Surface_Filling/de.md): Erstellt eine Füllfläche aus einer Reihe von Randkurven.

-   <img alt="" src=images/Surface_GeomFillSurface.svg  style="width:32px;"> [GeomFüllflächen](Surface_GeomFillSurface/de.md): Erstellt eine Füllfläche aus zwei, drei oder vier Randkurven.

-   <img alt="" src=images/Surface_Sections.svg  style="width:32px;"> [Querschnitte](Surface_Sections/de.md): Erstellt eine Oberfläche über Kanten, die die Querschnitte der Oberfläche repräsentieren.

-   <img alt="" src=images/Surface_ExtendFace.svg  style="width:32px;"> [FlächeErweitern](Surface_ExtendFace/de.md): Extrapoliert die Oberfläche an den Rändern mit ihren lokalen U- und V-Parametern.

-   <img alt="" src=images/Surface_CurveOnMesh.svg  style="width:32px;"> [KurveAufNetz](Surface_CurveOnMesh/de.md): Erstellt angenäherte Spline-Abschnitte auf einem ausgewählten [Netz](Mesh_Workbench/de.md).

-   <img alt="" src=images/Surface_BlendCurve.svg  style="width:32px;"> [Übergangskurve](Surface_BlendCurve/de.md): Erstellt eine Bezier-Kurve zwischen zwei Kanten mit der gewünschten Stetigkeit.





{{Surface Tools navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Surface](Category_Surface.md) > Surface Workbench/de
