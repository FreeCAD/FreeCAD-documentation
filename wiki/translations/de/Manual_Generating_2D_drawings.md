# Manual:Generating 2D drawings/de
{{Manual:TOC}}

Wenn dein Modell nicht direkt von einer Maschine gedruckt oder gefräst werden kann, weil es z. B. zu groß ist (ein Gebäude) oder einen manuellen Zusammenbau erfordert, nachdem die Teile fertig sind, muss man normalerweise einer anderen Person erklären, wie man das macht. In technischen Bereichen (Ingenieurwesen, Architektur usw.) geschieht dies meist anhand von Zeichnungen. Die Zeichnungen werden der Person ausgehändigt, die für den Zusammenbau des Endprodukts verantwortlich ist, und erklären, wie man das macht.

Typische Beispiele sind Ikea Anleitungen, [Architekturzeichnungen](https://en.wikipedia.org/wiki/Architectural_drawing) und [Blaupausen](https://en.wikipedia.org/wiki/Blueprint). Diese Zeichnungen enthalten in der Regel nicht nur die Zeichnung selbst, sondern auch viele Anmerkungen, wie Text, Maße, Zahlen und Symbole, die anderen Menschen helfen, zu verstehen, was und wie getan werden muss.

In FreeCAD ist der Arbeitsbereich, der für die Erstellung solcher Zeichnungen verantwortlich ist, der <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Arbeitsbereich](TechDraw_Workbench/de.md).

Der TechDraw Arbeitsbereich ermöglicht es dir, Blätter zu erstellen, die leer sein können oder eine vorgefertigte [Vorlage](TechDraw_Templates/de.md) verwenden, um bereits eine Reihe von Elementen auf dem Blatt zu haben, wie z.B. Rahmen und einen Titel. Auf diesen Blättern kannst du dann Ansichten der 3D Objekte, die du zuvor modelliert hast, platzieren und konfigurieren, wie diese Ansichten auf dem Blatt erscheinen sollen. Du kannst auch alle Arten von Anmerkungen auf dem Blatt platzieren, wie z. B. Bemaßungen, Texte und andere in technischen Zeichnungen häufig verwendete Symbole.

Sobald die Zeichnungsblätter vollständig sind, können sie gedruckt oder als [SVG](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics), PDF oder [DXF](https://en.wikipedia.org/wiki/AutoCAD_DXF) Dateien exportiert werden.

In der folgenden Übung werden wir sehen, wie eine einfache Zeichnung eines Stuhlmodells aus der [FreeCAD-Bibliothek](https://github.com/FreeCAD/FreeCAD-library) (Industrial Design → Chairs → IkeaLikeChair) erstellt wird. Die FreeCAD-Bibliothek kann einfach zu Deiner FreeCAD-Installation hinzugefügt werden (siehe das [FreeCAD installieren](Installing/de.md) Kapitel dieses Handbuchs), oder Du kannst einfach das Modell auf der Bibliothekswebseite oder über die direkten Verknüpfung am Ende dieses Kapitels herunterladen.

![](images/Exercise_TechDraw_01.png )

-   Wir laden die Datei IkeaLikeChair aus der Bibliothek. Wir können wählen zwischen der .[FCStd](File_Format_FCStd/de.md)-Version, die die komplette Modellierungshistorie enthält, oder die .[step](STEP/de.md)-Version, die nur ein Objekt ohne die Historie enthält. Da wir nicht weitermodellieren wollen, ist es das Beste, die .step-Version auszuwählen, da sie einfacher zu bearbeiten ist.

![](images/Parts_library.jpg )

-   Zum Arbeitsbereich <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw](TechDraw_Workbench/de.md) wechseln.
-   Die Schaltfläche <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:16px;"> [Neues Zeichnungsblatt aus einer Vorlage erstellen](TechDraw_PageTemplate/de.md) drücken
-   Die Vorlage **A4_Hochformat_ISO 7200TD** auswählen. Ein neuer Reiter öffnet sich im FreeCAD-Fenster und zeigt das neue Zeichnungsblatt.
-   In der [Baumansicht](tree_view/de.md) (oder dem Reiter Modell) das Stuhlmodell auswählen. Es wird höchstwahrscheinlich so etwas wie \"Open CASCADE STEP Übersetzer\" genannt werden.
-   Die Schaltfläche <img alt="" src=images/TechDraw_View.svg  style="width:16px;"> [Ansicht einfügen](TechDraw_View/de.md) drücken.
-   Ein Ansichtsobjekt wird auf unserem Blatt erstellt. Das Ansichtsobjekt in der Baumansicht auswählen, und der Ansicht dann die folgenden [Eigenschaften](TechDraw_View/de#Properties.md) im Datenreiter der Combo-Ansicht anpassen:

-   -   In der Kategorie Basis:
        -   X: 70 mm
        -   Y: 120 mm
        -   Drehung: 0
        -   Maßstab: 0,1
    -   In der Kategorie Projection (auf den Aufklapppfeilklicken, um die x-, y- und z-Komponenten dieser Eigenschaften einzeln zu ändern):
        -   Richtung: \[0 0 1\]
        -   XRichtung: \[0 -1 0\] (Zuerst das y-Feld ändern, dann das x-Feld)
-   Wir haben jetzt eine hübsche Draufsicht auf unseren Stuhl. Die Schaltfläche <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:16px;"> [Ansichtsrahmen ein- oder ausschalten](TechDraw_ToggleFrame/de.md), um die Ansichtsrahmen, Beschriftungen und Knoten auszuschalten.

![](images/Exercise_drawing_02.jpg )

-   Lasst uns diesen Arbeitsschritt zweimal wiederholen, um zwei weitere Ansichten zu erstellen. Wir werden ihre X- und Y-Werte eingeben, die die Position der Ansicht auf der Seite angeben, um sie getrennt von der Draufsicht anzuzeigen und ihre Richtung, um verschiedene Ansichtsausrichtungen zu erstellen. Dazu für jede neuen Ansicht die folgenden Eigenschaften eingeben:
    -   View001 (Vorderansicht): X: 70, Y: 220, Maßstab: 0.1, Drehung: 0, Richtung: (0,-1,0)
    -   View002 (Seitenansicht): X: 150, Y: 220, Maßstab: 0.1, Drehung: 0, XRichtung: (1,0,0)
-   Danach erhalten wir die folgende Seite:

![](images/Exercise_TechDraw_04.png )

-   Beachte, dass es möglicherweise einfachere Wege gibt, die gewünschten Ansichten zu bekommen. Du kannst einfach [rotieren](Manual:Navigating_in_the_3D_view/de.md) die 3D-Ansicht deines Modells drehen und sobald du die gewünschte Ansicht hast, wähle das Modell in der Baumansicht aus und drücke <img alt="" src=images/TechDraw_View.svg  style="width:16px;"> Neue Ansicht. Dadurch wird automatisch eine Ansicht mit den gewünschten Rotations- und Richtungseigenschaften eingefügt. Du kannst auch das <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:16px;"> [Projektionsgruppe](TechDraw_ProjectionGroup/de.md)-Werkzeug verwenden.

-   Wir können die Darstellung unserer Ansichten optimieren, wenn wir wollen, z.B. können wir ihre Eigenschaft **Linienbreite** (unter dem Reiter Ansicht in der Combo-Ansicht) auf 0.5 ändern.

Wir werden nun Bemaßungen und Hinweise auf unserer Zeichnung platzieren. Es gibt zwei Arten, Bemaßungen zu einem Modell hinzuzufügen: Eine ist, die Bemaßungen mit dem <img alt="" src=images/Draft_Dimension.svg  style="width:16px;"> [Abmessung](Draft_Dimension/de.md) Werkzeug des [Entwurf Arbeitsbereich](Draft_Workbench/de.md) im 3D-Modell zu platzieren und dann mit dem <img alt="" src=images/TechDraw_DraftView.svg  style="width:16px;"> [Entwurfsansicht](TechDraw_DraftView/de.md)-Werkzeug (das mit einer Bemaßung oder einer Gruppe, die Bemaßungen enthält, benutzt werden kann) eine Ansicht dieser Bemaßungen auf unsererem Blatt zu platzieren, oder wir können mit dem [Zeichnungsbemaßungs Arbeitsbereich](https://github.com/hamish2014/FreeCAD_drawing_dimensioning), der aus den [FreeCAD Erweiterungen](https://github.com/FreeCAD/FreeCAD-addons) installierbar ist, Dinge direkt auf dem Zeichenblatt tun. Wir werden hier die letztere Methode benutzen.

-   Drücke die <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:16px;"> Umschalttaste zum Einschalten der Knoten.
-   Verwende **Strg** + Linker Mausklick, um die beiden Knoten auszuwählen, zwischen denen du den Abstand messen möchtest.
-   Drücke die Schaltfläche <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Längenmaß](TechDraw_LengthDimension/de.md).

![](images/Exercise_TechDraw_05.png )

-   Den Vorgang wiederholen, bis alle Maße, die angeben werden sollen, positioniert sind. Nach Bedarf die Werkzeuge <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> [Vertikales Maß einfügen](TechDraw_VerticalDimension/de.md) und <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:16px;"> [Horizontales Maß einfügen](TechDraw_HorizontalDimension/de.md) einsetzen.
-   Wir nehmen uns einen Moment, um die [Eigenschaften](TechDraw_LengthDimension/de#Eigenschaften.md) des Dimension-Objekts in der Combo-Ansicht anzusehen.
-   Bitte beachten, dass bei dem Bemaßen einer [axonometrischen](https://en.wikipedia.org/wiki/Axonometric_projection) Ansicht (z.B. isometrische Ansicht) anstelle einer Ansicht der [Mehrfachansicht](https://en.wikipedia.org/wiki/Multiview_projection) (z.B. Vorderansicht), wie wir es hier getan haben, das Werkzeug <img alt="" src=images/TechDraw_LinkDimension.svg  style="width:16px;"> [Maß mit 3D-Geometrie verknüpfen](TechDraw_LinkDimension/de.md) eingesetzt werden muss, um die wahre Länge (anstatt der projizierten Länge) als Maß(zahl) zu erhalten.

![](images/Exercise_TechDraw_07.png )

-   We will now place the two callouts shown in the image above, using the <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> [TechDraw Balloon](TechDraw_Balloon.md) tool.

![](images/Exercise_TechDraw_06.png )

1.  Looking at the Page in the [3D view](3D_view.md) window, select the View to which the Balloon will be attached, as shown in the image above.
2.  Press the <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> Balloon button.
3.  The cursor is now displayed as a balloon icon. Click on the page to place the balloon origin at the desired position.
4.  The balloon bubble may be dragged to the desired position.
5.  Change the balloon properties by double-clicking the balloon label or the balloon object in the [tree view](Tree_view.md). This will open the Balloon Task dialog. Set the Value field to the desired text and change the Symbol drop-down menu selection to **None**
6.  Press **OK**
7.  Repeat the operation for the second callout.

-   We will now fill in the sheet title block.
    -   Make sure that the View frames, labels, and vertices are visible. If not, hit the <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:16px;"> Toggle button.
    -   Edit the text in each section of the sheet title block by clicking on the small green square on the left side of the text.

Unsere Seite kann nun ins SVG für eine weitere Verarbeitung in grafischen Anwendungen wie [Inkscape](http://www.inkscape.org) oder ins DXF exportiert werden. Wähle die Seite in der [Baumansicht](Tree_view/de.md) und wähle dann Menü **Datei → Export**. Das DXF-Format ist in fast allen vorhandenen 2D CAD Anwendungen importierbar. TechDraw-Seiten können auch direkt gedruckt oder in PDF exportiert werden.

**Herunterladen**

-   Die während dieser Übung erstellte Datei: [drawing.FCStd](https://github.com/JoshuaCall/FreeCAD-manual/blob/master/files/drawing.FCStd)
-   Das aus der Datei erstellte SVG-Blatt: [drawing.svg](https://github.com/JoshuaCall/FreeCAD-manual/blob/master/files/drawing.svg)

**Mehr lesen**

-   [Der TechDraw Arbeitsbereich](TechDraw_Workbench/de.md)
-   [Benutzerdefinierte Vorlagen erstellen](TechDraw_TemplateHowTo/de.md)
-   [Ein weiteres TechDraw Tutorium](Basic_TechDraw_Tutorial/de.md)
-   [Die FreeCAD Bibliothek](https://github.com/FreeCAD/FreeCAD-library)
-   [Inkscape](http://www.inkscape.org)

**Tutorials ansehen**

-   [Sliptonics TechDraw Wiedergabeliste](https://www.youtube.com/watch?v=7LbOmSGW9F0&list=PLEuOia-QxyFKQnmM1U9yVo7eNrK_Mcln8)
-   [Symbole und Darstellungen](https://www.youtube.com/watch?v=cggBR1Ghq7k)



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Generating 2D drawings/de
