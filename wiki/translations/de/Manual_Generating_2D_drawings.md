# Manual:Generating 2D drawings/de
{{Manual:TOC/de}}

Wenn dein Modell nicht direkt von einer Maschine gedruckt oder gefräst werden kann, z. B. ist es zu groß (ein Gebäude) oder es erfordert manuellen zusammenbau, nachdem die Teile fertig sind, musst du normalerweise einer anderen Person erklären, wie man das macht. In technischen Bereichen (Ingenieurwesen, Architektur usw.) geschieht dies meist anhand von Zeichnungen. Die Zeichnungen werden der Person ausgehändigt, die für den Zusammenbau des Endprodukts verantwortlich ist, und erklären, wie man das macht.

Typische Beispiele sind Ikea Anleitungen, [Architekturzeichnungen](https://en.wikipedia.org/wiki/Architectural_drawing) und [Blaupausen](https://en.wikipedia.org/wiki/Blueprint). Diese Zeichnungen enthalten in der Regel nicht nur die Zeichnung selbst, sondern auch viele Anmerkungen, wie Text, Maße, Zahlen und Symbole, die anderen Menschen helfen, zu verstehen, was und wie getan werden muss.

In FreeCAD ist der Arbeitsbereich, der für die Erstellung solcher Zeichnungen verantwortlich ist, der <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Arbeitsbereich](TechDraw_Workbench/de.md).

Der TechDraw Arbeitsbereich ermöglicht es dir, Blätter zu erstellen, die leer sein können oder eine vorgefertigte [Vorlage](TechDraw_Templates/de.md) verwenden, um bereits eine Reihe von Elementen auf dem Blatt zu haben, wie z.B. Rahmen und einen Titel. Auf diesen Blättern kannst du dann Ansichten der 3D Objekte, die du zuvor modelliert hast, platzieren und konfigurieren, wie diese Ansichten auf dem Blatt erscheinen sollen. Du kannst auch alle Arten von Anmerkungen auf dem Blatt platzieren, wie z. B. Bemaßungen, Texte und andere in technischen Zeichnungen häufig verwendete Symbole.

Sobald die Zeichnungsblätter vollständig sind, können sie gedruckt oder als [SVG](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics), PDF oder [DXF](https://en.wikipedia.org/wiki/AutoCAD_DXF) Dateien exportiert werden.

In der folgenden Übung werden wir sehen, wie eine einfache Zeichnung eines Stuhlmodells aus der [FreeCAD Bibliothek](https://github.com/FreeCAD/FreeCAD-library) (Möbel → Stühle → IkeaÄhnlicherStuhl) erstellt wird. Die FreeCAD Bibliothek kann einfach zu Deiner FreeCAD Installation hinzugefügt werden (siehe das [FreeCAD installieren](Installing/de.md) Kapitel dieses Handbuchs), oder Du kannst einfach das Modell auf der Bibliothekswebseite oder über die direkten Verknüpfung am Ende dieses Kapitels herunterladen.

![](images/Exercise_TechDraw_01.svg )

-   Lade die IkeaÄhnlicherStuhl Datei aus der Bibliothek. Du kannst wählen zwischen der .[FCStd](File_Format_FCStd/de.md) Version, die die komplette Modellierungshistorie enthält, oder die .[step](STEP/de.md) Version, die nur ein Objekt ohne die Historie enthält. Da wir nicht weiter modellieren wollen, ist es das Beste, die .step Version zu wählen, da sie einfacher zu bearbeiten ist.

![](images/Parts_library.jpg )

-   Wechsle zum <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Arbeitsbereich](TechDraw_Workbench/de.md)
-   Drücke die <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:16px;"> [SeitenVorlage](TechDraw_PageTemplate/de.md) Schaltfläche
-   Wähle die **A4\_Hochformat\_ISO 7200TD** Vorlage. Ein neuer Reiter öffnet sich im Deinem FreeCAD Fenster und zeigt die neue Seite.
-   Wähle in der [Baumansicht](tree_view/de.md) (oder dem Modell Reiter) das Stuhlmodell. Es wird höchstwahrscheinlich so etwas wie \"Open CASCADE STEP Übersetzer\" genannt werden.
-   Drücke die <img alt="" src=images/TechDraw_View.svg  style="width:16px;"> [Ansicht](TechDraw_View/de.md)-Schaltfläche.
-   Ein Ansichtsobjekt wird auf unserer Seite erstellt. Wähle das Ansichtsobjekt in der Baumansicht aus, und gib der Ansicht dann die folgenden [Eigenschaften](TechDraw_View/de#Properties.md) im Datenreiter der Combo-Ansicht:
    -   Unter der Basiskategorie:
        -   X: 70 mm
        -   Y: 120 mm
        -   Drehung: 0
        -   Maßstab: 0.1
    -   Unter der Projektionskategorie (klicke auf den Aufklapppfeil, um die x-, y- und z-Komponenten dieser Eigenschaften einzeln zu ändern):
        -   Richtung: \[0 0 1\]
        -   XRichtung: \[0 -1 0\] (Ändere zuerst das y-Feld, dann das x-Feld)
-   Wir haben jetzt eine hübsche Draufsicht auf unseren Stuhl. Drücke die <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:16px;"> [UmschaltenRahmen](TechDraw_ToggleFrame/de.md)-Schaltfläche, um die Ansichtsrahmen, Beschriftungen und Knoten auszuschalten.

![](images/Exercise_drawing_02.jpg )

-   Lass uns diese Operation zweimal wiederholen, um zwei weitere Ansichten zu erstellen. Wir werden die X und Y Werte setzen, die die Position der Ansicht auf der Seite angibt, um sie getrennt von der Draufsicht anzuzeigen, und ihre Richtung, um verschiedene Ansichtsausrichtungen zu erstellen. Gib jeder neuen Ansicht die folgenden Eigenschaften:
    -   View001 (Frontansicht): X: 70, Y: 220, Maßstab: 0.1, Drehung: 0, Richtung: (0,-1,0)
    -   View002 (Seitenansicht): X: 150, Y: 220, Maßstab: 0.1, Drehung: 0, XRichtung: (1,0,0)
-   Danach erhalten wir die folgende Seite:

![](images/Exercise_TechDraw_04.png )

-   Beachte, dass es möglicherweise einfachere Wege gibt, die gewünschten Ansichten zu bekommen. Du kannst einfach [rotieren](Manual:Navigating_in_the_3D_view/de.md) die 3D-Ansicht deines Modells drehen und sobald du die gewünschte Ansicht hast, wähle das Modell in der Baumansicht aus und drücke <img alt="" src=images/TechDraw_View.svg  style="width:16px;"> Neue Ansicht. Dadurch wird automatisch eine Ansicht mit den gewünschten Rotations- und Richtungseigenschaften eingefügt. Du kannst auch das <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:16px;"> [Projektionsgruppe](TechDraw_ProjectionGroup/de.md)-Werkzeug verwenden.

-   Wir können den Aspekt unserer Ansichten optimieren, wenn wir wollen, z.B. können wir ihre **Linienbreite** Eigenschaft (unter dem Ansichtsreiter in der Combo Ansicht) auf 0.5 ändern.

Wir werden nun Bemaßungen und Hinweise auf unserer Zeichnung platzieren. Es gibt zwei Arten, Bemaßungen zu einem Modell hinzuzufügen: Eine ist, die Bemaßungen mit dem <img alt="" src=images/Draft_Dimension.svg  style="width:16px;"> [Abmessung](Draft_Dimension/de.md) Werkzeug des [Entwurf Arbeitsbereich](Draft_Workbench/de.md) im 3D-Modell zu platzieren und dann mit dem <img alt="" src=images/TechDraw_DraftView.svg  style="width:16px;"> [Entwurfsansicht](TechDraw_DraftView/de.md)-Werkzeug (das mit einer Bemaßung oder einer Gruppe, die Bemaßungen enthält, benutzt werden kann) eine Ansicht dieser Bemaßungen auf unsererem Blatt zu platzieren, oder wir können mit dem [Zeichnungsbemaßungs Arbeitsbereich](https://github.com/hamish2014/FreeCAD_drawing_dimensioning), der aus den [FreeCAD Erweiterungen](https://github.com/FreeCAD/FreeCAD-addons) installierbar ist, Dinge direkt auf dem Zeichenblatt tun. Wir werden hier die letztere Methode benutzen.

-   Drücke die <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:16px;"> Umschalttaste zum Einschalten der Knoten.
-   Verwende **Strg** + Linker Mausklick, um die beiden Knoten auszuwählen, zwischen denen du den Abstand messen möchtest.
-   Drücke die Schaltfläche <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Längenmaß](TechDraw_LengthDimension/de.md).

![](images/Exercise_TechDraw_05.png )


<div class="mw-translate-fuzzy">

-   Wiederhole den Vorgang, bis alle Abmessungen, die du angeben möchtest, platziert sind. Verwende die <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> [Vertike Abmessung](TechDraw_VerticalDimension/de.md) und <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:16px;"> [Horizontale Abmessung](TechDraw_HorizontalDimension/de.md) Werkzeuge nach Bedarf.
-   Nimm dir eine Minute Zeit, um dir die [Eigenschaften](TechDraw_LengthDimension/de#Properties.md) des Bemaßungsobjekts in der Combo-Ansicht anzusehen.
-   Bitte beachte, dass bei der Bemaßung einer [axonometrischen](https://en.wikipedia.org/wiki/Axonometric_projection) Ansicht (z.B. isometrische Ansicht) anstelle einer [Mehrfachansicht](https://en.wikipedia.org/wiki/Multiview_projection) Ansicht (z.B. Vorderansicht), wie wir es hier getan haben, du das <img alt="" src=images/TechDraw_LinkDimension.svg  style="width:16px;"> [Dimension Link](TechDraw_LinkDimension.md) Werkzeug verwenden musst, um eine genaue Bemaßung zu erhalten.


</div>

![](images/Exercise_TechDraw_07.png )

-   Wir werden nun die beiden in der obigen Abbildung gezeigten Aufrufe unter Verwendung des <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> [Stücklistensymbol](TechDraw_Balloon/de.md) Werkzeugs platzieren.

![](images/Exercise_TechDraw_06.png )

1.  Beim Betrachten der Seite im [Baumansicht](3D_view/de.md) Fenster, wähle die Ansicht, an die das Stücklistensymbol angehängt wird, wie in der Abbildung oben gezeigt.
2.  Drücke die <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> Stücklistensymbol Schaltfläche.
3.  Der Mauszeiger wird jetzt als Stücklistensymbol angezeigt. Klicke auf die Seite, um den Stücklistensymbolursprung an der gewünschten Position zu platzieren.
4.  Die Stücklistensymbolblase kann an die gewünschte Position gezogen werden.
5.  Ändere die Stücklistensymboleigenschaften durch Doppelklicken auf die Stücklistensymbolbeschriftung oder das Stücklistensymbolobjekt in der [Baumansicht](Tree_view/de.md). Dadurch wird der Stücklistensymbol Aufgabendialog geöffnet. Setze das Wert Feld auf den gewünschten Text und ändere die Symbol Ausklappmenüauswahl auf **Kein**.
6.  Drücke **OK**
7.  Wiederhole den Vorgang für den zweite Aufruf.

-   Wir werden nun das Blatttitelfeld ausfüllen.
    -   Stelle sicher, dass die Ansichtsrahmen, Beschriftungen und Knoten sichtbar sind. Wenn dies nicht der Fall ist, drücke die <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:16px;">-Umschalttaste.
    -   Bearbeite den Text in jedem Abschnitt des Blatttitelblocks, indem du auf das kleine grüne Quadrat auf der linken Seite des Textes klickst.

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
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Generating 2D drawings/de
