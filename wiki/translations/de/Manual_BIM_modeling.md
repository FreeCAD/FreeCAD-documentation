# Manual:BIM modeling/de
{{Manual:TOC/de}}

BIM steht für [Bauwerksdatenmodellierung](https://de.wikipedia.org/wiki/Building_Information_Modeling). Die exakte Definition, was damit gemeint ist, variiert, aber vereinfacht gesagt handelt es sich darum, wie Gebäude und andere große Strukturen wie Brücken, Tunnel, etc. heutzutage modelliert werden. BIM-Modelle basieren normalerweise auf 3D-Modellen und enthalten auch eine Reihe von zusätzlichen Informationsschichten, wie Materialinformationen, Beziehungen zu anderen Objekten oder Modellen oder speziellen Anweisungen für Gebäude oder Wartung. Diese zusätzlichen Informationen erlauben alle Arten von erweiterten Analysen des Modells, wie struktureller Widerstand (structural resistance), Kosten und geschätzte Bauzeit oder Berechnungen des Energieverbrauchs.

Der [Architektur Arbeitsbereich](Arch_Workbench/de.md) von FreeCAD enthält eine Reihe von Werkzeugen und Einrichtungen für die BIM Modellierung. Obwohl es einem anderen Zweck dient, arbeitet es in enger Integration mit dem Rest von FreeCAD: Alles, was mit einem anderen Arbeitsbereich erstellt wurde, kann zu einem Architektur Objekt oder Grundlage für ein Architektur Objekt werden.

Wie im [PartDesign-Arbeitsbereich](PartDesign_Workbench/de.md) sind mit dem Arch-Arbeitsbereich erstellte Objekte für die reale Welt gedacht. Daher müssen sie **solide** (solid) sein. Die Arch-Werkzeuge achten normalerweise automatisch darauf und bieten auch Hilfswerkzeuge zur Prüfung der Gültigkeit von Objekten.

Der Architektur Arbeitsbereich schließt auch alle Werkzeuge des [Entwurf Arbeitsbereichs](Draft_Workbench/de.md) ein und verwendet sein Gitter und Fangsystem. Vor dem Anfangen, ist es immer eine gute Idee, die Einstellungsseiten von Entwurf und Architektur zu durchstöbern und die Standardeinstellungen nach Ihren Wünschen festzulegen.

In diesem Kapitel werden wir sehen, wie dieses kleine Gebäude modelliert wird:

![](images/Exercise_arch_01.jpg )

und einen Plan und eine Schnittansicht davon erstellen:

![](images/Exercise_arch_02.jpg )

-   Erstelle ein neues Dokument und wechsle zum [Architektur Arbeitsbereich](Arch_Workbench/de.md).
-   Öffne das Menü **Bearbeiten → Einstellungen → Entwurf → Gitter und Fang** und setze:
    -   **Hauptlinien alle** `10`.
    -   **Gitterabstand** `1000mm`, um ein auf einem Meter basierendes Raster zu haben, das für die Größe unseres Gebäudes geeignet ist.
    -   **Rastergröße** `100 Zeilen`.
-   Stelle in der **Fang Symbolleiste** sicher, dass das <img alt="" src=images/Draft_Snap_Grid.svg  style="width:16px;"> [Gitterfang](Draft_Snap_Grid/de.md) aktiviert ist, damit wir das Gitter so weit wie möglich nutzen können.
-   Wenn du Achsen nicht siehst, klicke auf die <img alt="" src=images/Draft_Snap_Grid.svg  style="width:16px;"> [Einschalten des Entwurfsgitters](Draft_Snap_Grid/de.md).
-   Stelle die [Arbeitsebene](Draft_SelectPlane/de.md) auf **XY** Ebene
-   Zoome heraus und schwenke, so dass du den Bereich von (0,0) bis (4,3) sehen kannst. Siehe das [Mausnavigation](Mouse_navigation/de.md) für Anweisungen.
-   Zeichne vier Linien mit dem <img alt="" src=images/Draft_Line.svg  style="width:16px;"> [Entwurf Linie](Draft_Line/de.md) Werkzeug. Du kannst die Koordinaten manuell eingeben oder die Punkte einfach mit der Maus auf dem Gitter anwählen:
    -   Von Punkt (0,0) bis Punkt (0,3)
    -   Von Punkt (0,3) bis Punkt (4,3) \*\* Von Punkt (0,3) bis Punkt (4,3)
    -   Vom Punkt (4,3) zum Punkt (4,0)
    -   Vom Punkt (4,0) zum Punkt (0,0)

HINWEIS: Aufgrund eines Fehlers in Version 0.18 müssen Sie sicherstellen, dass Sie die Linien in dieser Reihenfolge und in dieser Richtung ausführen.

![](images/Exercise_arch_03.jpg )

Beachte, dass wir immer in der gleichen Richtung gezeichnet haben (im Uhrzeigersinn). Dies ist nicht notwendig, stellt aber sicher, dass die Wände anschließend alle die gleichen rechts/links-Eigenschaften haben. Du könntest auch denken, dass wir einfach ein Rechteck hätten zeichnen können (was stimmt). Die vier Linien illustrieren aber besser, wie ein Objekt zu einem anderen hinzugefügt werden kann.

-   Wenn du die Linien erstellt hast, überprüfe deren Start- und Endpunkte und passe sie gegebenenfalls an, damit sie genau stimmen.

![](images/Manual-BIM_Modeling_-_Adjusting_Lines.png )

-   Wähle die erste Linie, drücke dann den <img alt="" src=images/Arch_Wall.svg  style="width:16px;"> [Wand](Arch_Wall/de.md) Schaltfläche.
-   Wiederhole dies für die anderen 3 Linien, bis Du vier Wände hast.
-   Wähle die vier Wände und setze die **Höhe** Eigenschaft auf **3,00 m** und die **Ausrichtung** Eigenschaft auf **links**. Falls Du die Linien nicht in der gleichen Reihenfolge wie oben gezeichnet hast, sind bei einigen Wänden möglicherweise die rechts/links Richtungen vertauscht, so dass hier **rechts** eingestellt werden muss. Du hast nun vier sich kreuzende Wände innerhalb der Grundlinien:

![](images/Exercise_arch_04.jpg )

Jetzt müssen wir diese Wände miteinander verbinden, so dass sie sich sauber schneiden. Das ist nicht notwendig, wenn Deine Wände so gezeichnet sind, dass sie bereits sauber verbunden sind, aber hier müssen wir es tun, da sie sich überschneiden. Im Arch Arbeitsbereich passiert das, indem eine Wand zum \"Host\" wird und die anderen als \"Additionen\" hinzugefügt werden. Jedes Arch Objekt kann eine beliebige Anzahl von \"Additionen\" haben (Objekte, deren Geometrie zur Host Geometrie hinzugefügt wird), und \"Subtraktionen\" (Objekte, deren Geometrie subtrahiert wird). Die \"Additionen\" und \"Subtractions\" eines Objekts können jederzeit durch Doppelklick auf das Objekt in der Baumansicht verändert werden.

-   Wähle die vier Wände mit gedrückter **Strg** Taste, die letzte wird dann zum Host
-   Drücke den <img alt="" src=images/Arch_Add.svg  style="width:16px;"> [Hinzufügen](Arch_Add/de.md) Taste. Die vier Wände sind nun zu einer geworden:

![](images/Exercise_arch_05.jpg )

Die einzelnen Wände sind nach wie vor zugänglich, wenn die Wand in der Baumansicht expandiert wird.

-   Lass uns nun eine Tür platzieren. In FreeCAD werden Türen als ein Sonderfall von Fenstern betrachtet, daher wird dies mit dem [Fenster](Arch_Window/de.md) Werkzeug durchgeführt.
-   Beginne mit der Auswahl der Wand. Dies ist nicht notwendig, sollte aber eine gute Angewohnheit werden. Wenn ein Objekt ausgewählt ist, wenn das Fenster Werkzeug gestartet wird, erzwingst du, dass das Fenster in dieses Objekt eingefügt wird, auch wenn du auf ein anderes Objekt fängst.
-   Setze die [Arbeitsebene](Draft_SelectPlane/de.md) auf **auto**, so dass wir nicht auf die Grundebene beschränkt sind.
-   Drücke die <img alt="" src=images/Arch_Window.svg  style="width:16px;"> [Fenster](Arch_Window/de.md) Taste.
-   Wähle im Fenster Erstellungspaneel die \"Simple door\" Vorgabe und setze **Width** auf 0,9 m und **Height** auf 2,1 m
-   Stelle sicher, dass die <img alt="" src=images/Draft_Snap_Near.svg  style="width:16px;"> [Nächste Fang](Draft_Snap_Near/de.md) eingeschaltet ist, damit wir auf Flächen fangen können
-   Platziere dein Fenster ungefähr in der Mitte der Stirnseite der Wand:

![](images/Exercise_arch_06.jpg )

-   Nach dem Klicken ist unser Fenster auf der richtigen Fläche platziert, aber nicht exakt da, wo wir es wollen:

![](images/Exercise_arch_07.jpg )

-   Durch Aufklappen des Wand- und des Fensterobjekts in der Baumansicht können wir nun die genaue Position festlegen. Dazu ist die **Placement**-Eigenschaft der Grundlinie unserer Tür zu ändern. Setze die Position auf **x = 2m, y = 0, z = 0**. Unsere Tür ist nun genau an der richtigen Stelle:

![](images/Exercise_arch_08.jpg )

-   Wiederhole die Operation, um ein Fenster zu platzieren: Wähle die Wand, drücke das [Fenster](Arch_Window/de.md)-Werkzeug, wähle die **Open 2-pane**-Vorgabe und platziere ein 1m x 1m-Fenster auf der gleichen Fläche wie die Tür. Setze die **Placement**-Eigenschaft der Grundlinie des Fensters auf **x = 0.6m, y = 0, z = 1.1m**, so dass die Oberkante des Fensters mit der der Tür übereinstimmt.

![](images/Exercise_arch_09.jpg )

Fenster basieren immer auf Skizzen. Es ist einfach, maßgeschneiderte Fenster zu erstellen, indem zuerst eine Skizze auf einer Fläche erzeugt wird, die dann zu einem Fenster wird, wenn man den Fenster-Button drückt. Dann können nach Doppelklick auf das Fenster in der Baumansicht die Fenster-Erstellungsparameter, also welche Polygonzüge der Skizze und wie sehr diese zu extrudieren sind, verändert werden. Nun werden wir eine Decke erstellen:

-   Setze mit [Ebene markieren](Draft_SelectPlane/de.md) die Arbeitsebene auf **XY**
-   Erstelle ein <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Rechteck](Draft_Rectangle/de.md) mit einer **Länge** von 5 m, einer **Höhe** von **4 m** und einer Position von **x = -0.5m, y:-0.5m, z:0**.
-   Wähle das Rechteck
-   Klicke das <img alt="" src=images/Arch_Structure.svg  style="width:16px;"> [Struktur](Arch_Structure/de.md) Werkzeug, um aus dem Rechteck eine Decke zu erzeugen
-   Setze die **Höhe** Eigenschaft der Decke auf 0,2 m und die **normal** Richtung auf (0,0,-1), weil wir sie nach unten extrudieren wollen. Wir hätten sie auch vorher 20 cm nach unten verschieben können, aber es immer gute Praxis, das extrudierte Objekt am gleichen Platz wie das Basisprofil zu belassen.
-   Setze die **Role** Eigenschaft der Decke auf **slab**. Das ist für FreeCAD nicht nötig, aber für den IFC Export ist das wichtig, weil es dafür sorgt, dass das Objekt mit dem richtigen IFC Typ exportiert wird.

![](images/Exercise_arch_10.jpg )

-   Jetzt benutzen wir eine der strukturellen Vorgaben, um einen Stahlträger zu erstellen. Klicken den <img alt="" src=images/Arch_Structure.svg  style="width:16px;"> [Struktur](Arch_Structure/de.md) Schaltfläche, wähle die **HEB 180**-Vorgabe und setze **Höhe** auf **4 m**. Platziere ihn irgendwo:

![](images/Exercise_arch_11.jpg )

-   Passe das **Placement** an, indem **Angle** auf 90° in der (1,0,0)-Achse und **Position** auf x:90mm, y:3.5m, z:3.09m geändert werden. Dies wird den Träger exakt auf einer der Seitenwände positionieren:

![](images/Exercise_arch_12.jpg )

-   Wir müssen diesen Träger nun ein paar Mal duplizieren. Wir können das einen nach dem anderen mit dem <img alt="" src=images/Draft_Clone.png  style="width:16px;"> [Klonen](Draft_Clone/de.md) Werkzeug machen, aber es gibt einen besseren Weg, alle Kopien mit Hilfe einer Anordung auf einmal zu machen:
-   Wähle den Träger
-   Drücke die <img alt="" src=images/Draft_OrthoArray.svg  style="width:16px;"> [rechtwinklige Anordnung](Draft_OrthoArray/de.md)-Schaltfläche
-   Setze die **Number of elements**-Eigenschaft für die X-Richtung der Anordung auf 6 und belasse die Werte für Y- und Z-Richtung auf 1 und **OK**.
-   Erweitere die **interval X**-Eigenschaft der Anordnung und drücke das <img alt="" src=images/Bound-expression-unset.png  style="width:16px;"> **Expression**-Symbol rechts neben dem X-Feld. Das öffnet den [Formeleditor](Expressions/de.md):

![](images/Exercise_arch_13.jpg )

-   Schreibe **(4m-180mm)/5** in das Ausdrucksfeld und drücke **OK**. Dies wird den x-Wert auf 0,764 setzen (4 m ist die Gesamtlänge unserer vorderen Wand, 180 mm ist die Breite des Trägers, der deshalb HEB180 heißt, und wir wollen ein Fünftel des Platzes als Zwischenraum zwischen den Balken haben):

![](images/Exercise_arch_14.jpg )

-   Wir können nun problemlos eine einfache Decke auf diesen Trägern erstellen, indem wir ein Rechteck direkt auf der oberen Fläche der Träger zeichnen. Wähle die obere Fläche eines der Träger.
-   Drücke den <img alt="" src=images/Draft_SelectPlane.svg  style="width:16px;"> [Ebene markieren](Draft_SelectPlane/de.md) Schaltfläche. Die Arbeitsebene wird nun auf diese Fläche gesetzt.
-   Erstelle ein <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Rechteck](Draft_Rectangle/de.md) durch Fangen von zwei gegenüberliegenden Punkten der äußeren Träger:

![](images/Exercise_arch_15.jpg )

-   Wähle das Rechteck
-   Klicke die <img alt="" src=images/Arch_Structure.svg  style="width:16px;"> [Struktur](Arch_Structure/de.md) Schaltfläche und erstelle eine Decke mit einer Höhe von **0,2 m**.

Das war\'s, unser Modell ist jetzt fertig. Wir sollten es nun gliedern, um es richtig nach IFC exportieren zu können. Das IFC-Format erfordert, dass sich alle Objekte eines Gebäudes in einem Gebäude-Objekt befinden, optional in einem Geschoss. Es erfordert auch, dass alle Gebäude auf einem Grundstück platziert werden, aber der IFC-Export-Prozess von FreeCAD wird, falls erforderlich, automatisch ein Standardgrundstück erstellen, so dass wir uns hier darum nicht kümmern müssen.

-   Wähle die beiden Decken, die Wand und die Anordung der Träger
-   Drücke die <img alt="" src=images/Arch_Floor.svg  style="width:16px;"> [Geschoss](Arch_Floor/de.md) Schaltfläche
-   Wähle das gerade angelegte Geschoss
-   Drücke die <img alt="" src=images/Arch_Building.svg  style="width:16px;"> [Gebäude](Arch_Building/de.md) Schaltfläche

Unser Modell ist nun bereit für den Export:

![](images/Exercise_arch_16.jpg )

Das [IFC-Format](https://de.wikipedia.org/wiki/Industry_Foundation_Classes) ist einer der wertvollsten Vorzüge in einer freien BIM-Welt, denn es erlaubt den Datenaustausch zwischen jeder Anwendung und jedem Akteur in der Welt des Baugewerbes in einer offenen Weise (das Format ist offen, frei und wird von einem unabhängigen Konsortium gepflegt). Der Export Deines Modells im IFC-Format gewährleistet, dass jeder es ansehen und untersuchen kann, unabhängig von der verwendeten Anwendung.

In FreeCAD erfolgt der IFC-Im- und Export durch Anbindung an einen anderen Software-Teil namens [IfcOpenShell](http://ifcopenshell.org/). Für den Export nach IFC muss außerdem das [IfcOpenShell-python](http://ifcopenshell.org/python.html)-Paket auf Deinem System installiert sein. Stelle sicher, dass dieses Paket die gleiche Python-Version wie FreeCAD verwendet. Die von FreeCAD benutzte Python-Version kann über **Ansicht -\> Paneele -\> Python-Konsole** ermittelt werden. Wenn das getan ist, können wir nun unser Modell exportieren:

-   Wähle das oberste zu exportierende Objekt, das Gebäude-Objekt.
-   Wähle aus dem Menü **Datei -\> Export -\> IFC** und speichere Deine Datei.
-   Die resultierende IFC-Datei kann nun mit einer Vielzahl von Anwendungen und Betrachtern (das folgende Bild zeigt die geöffnete Datei im [IfcPlusPlus](http://www.ifcquery.com/)-Betrachter). Die Überprüfung der exportierten Datei in solch einer Betrachtungsanwendung ist wichtig, um sicherzustellen, dass die enthaltenen Daten korrekt sind, bevor die Datei an andere Personen weitergegeben wird. FreeCAD kann ebenfalls verwendet werden, um die IFC-Datei zu öffnen.

![](images/Exercise_arch_17.jpg )

Wir werden nun ein paar Bemaßungen platzieren. Wir werden anders als im [vorigen Kapitel](Manual:Generating_2D_drawings/de.md) die Bemaßungen nicht direkt auf das Zeichenblatt zeichnen, sondern hier eine andere Methode nutzen und [Bemaßungen](Draft_Dimension/de.md) direkt im 3D-Modell platzieren. Diese Bemaßungen werden dann automatisch auf dem Zeichenblatt platziert. Wir werden zuerst zwei Gruppen für unsere Bemaßungen erstellen, eine für die Bemaßungen, die im Lageplan erscheinen, und eine weitere für die in der Draufsicht.

-   Rechtsklicke das **house** Dokument in der Baumansicht und erstelle zwei neue Gruppen: **Plan dimensions** und **Elevation dimensions**.
-   Setze mit [Arbeitsebene](Draft_SelectPlane/de.md) auf die **XY** Ebene.
-   Stelle sicher, dass die <img alt="" src=images/Draft_Snap_WorkingPlane.svg  style="width:16px;"> [einschränken](Draft_Snap_WorkingPlane/de.md) Fangposition eingeschaltet ist, damit alles, was du zeichnest, auf der Arbeitsebene bleibt.
-   Zeichne eine Reihe von <img alt="" src=images/Draft_Snap_Dimensions.svg  style="width:16px;"> [Bemaßungen](Draft_Snap_Dimensions/de.md), beispielsweise wie auf dem folgenden Bild. Drücken von **Shift** und **Strg** während des Fangs der Bemaßungspunkte gibt dir zusätzliche Wahlmöglichkeiten.

![](images/Exercise_arch_18.jpg )

-   Wähle all Deine Bemaßungen und ziehe sie in die **Plan dimensions**-Gruppe in der Baumansicht.
-   Setze mit [Ebene markieren](Draft_SelectPlane/de.md) die Arbeitsebene auf **XY**, also die Draufsicht.
-   Wiederhole die Operation, zeichne eine Reihe von Bemaßungen und verschiebe sie in die **Elevation dimensions**-Gruppe.

![](images/Exercise_arch_19.jpg )

Wir werden nun einen Satz von Ansichten unseres Modells vorbereiten, die auf einem Zeichenblatt platziert werden. Wir können das mit den Werkzeugen des Drawing-Arbeitsbereichs tun, wie wir das im vorigen Kapitel gesehen haben, aber der Arch-Arbeitsbereich bietet auch ein fortgeschrittenes All-in-one-Werkzeug, um Lagepläne, Schnitt- und Draufsichten zu erstellen, genannt [Schnittebenen](Arch_SectionPlane/de.md). Wir werden nun zwei dieser Schnittebenen hinzufügen, um einen Lageplan und eine Draufsicht zu erzeugen.

-   Wähle das Gebäude-Objekt in der Baumansicht
-   Drücke den <img alt="" src=images/Arch_SectionPlane.svg  style="width:16px;"> [Schnittebene](Arch_SectionPlane/de.md)-Button.
-   Setze die **Height**-Eigenschaft auf 5 m, die **Display Length** auf 6 m, so dass wir unser Haus erfassen (das ist nicht nötig, aber es sieht besser aus, weil es auf natürliche Weise zeigt, wofür es benutzt wird) und die **Placement**-Position auf x:2m, y:1.5m, z:1.5m.
-   Prüfe die von der Schnittebene vorgeschlagene Objektliste durch Doppelklick in der [Baumansicht](tree_view/de.md). Schnittebenen rendern nur angegebene Objekte des Modells, nicht alle. Die ausgewählten Objekte können hier geändert werden.

![](images/Exercise_arch_20.jpg )

-   Wiederhole die Operation, um eine weitere Schnittebene zu erzeugen, mit den gleichen Werten für Height und Display length, aber unterschiedlicher **Placement**-Position: x:2m, y:-2m, z:1.5m, angle: 90°, axis: x:1, y:0, z:0. Sorge dafür, dass diese Schnittebene ebenfalls das Gebäude-Objekt berücksichtigt.

![](images/Exercise_arch_21.jpg )


**Die Entwicklung des [Zeichnung Arbeitsbereich](Drawing_Workbench/de.md)es wurde in FreeCAD 0.16 beendet, als Ersatz wurde in Version 0.17 der [TechDraw Arbeitsbereich](TechDraw_Workbench/de.md) eingeführt. Der Drawing Arbeitsbereich könnte in zukünftigen FreeCAD Versionen entfallen. Benutze statt dessen den TechDraw Arbeitsbereich.**

-   Jetzt haben wir alles notwendige und wir können unsere Zeichnungsseite erstellen. Beginne mit dem Wechsel zum [Arbeitsbereich Zeichnung](Drawing_Workbench/de.md) und erzeuge eine neue Standard<img alt="" src=images/Drawing_Landscape_A3.png  style="width:16px;"> [DIN A3 Seite](Drawing_Landscape_A3/de.md) (oder wähle eine andere Vorlage, wenn du möchtest).
-   Wähle die erste Abschnittsebene, die für den Lageplan benutzt wird
-   Drücke die <img alt="" src=images/Drawing_DraftView.png  style="width:16px;"> [DraftView](Drawing_DraftView.md) Taste. Dieses Werkzeug bietet eine Reihe von zusätzlichen Möglichkeiten gegenüber dem Standard [Entwurf Ansicht](Drawing_View/de.md) Werkzeug und unterstützt die Abschnittsebenen des Architektur Arbeitsbereichs.
-   Gib der neuen Ansicht folgende Eigenschaften:
    -   X: 50
    -   Y: 140
    -   Scale: 0.03
    -   Line width: 0.15
    -   Show Cut True
    -   Show Fill: True
-   Wähle die andere Schnittebene und erstelle eine neue Entwurf Ansicht mit den folgenden Eigenschaften:
    -   X: 250
    -   Y: 150
    -   Scale: 0.03
    -   Rendering: Solid

![](images/Exercise_arch_22.jpg )

Wir werden nun zwei weitere Draft-Ansichten erzeugen, für jede Gruppe von Bemaßungen eine.

-   Wähle die Plan dimensions-Gruppe
-   Drücke den <img alt="" src=images/Drawing_DraftView.png  style="width:16px;"> [Entwurfsansicht](Drawing_View/de.md)-Button.
-   Gib der neuen Ansicht folgende Eigenschaften:
    -   X: 50
    -   Y: 140
    -   Scale: 0.03
    -   Line width: 0.15
    -   Font size: 10mm
-   Wiederhole die Operation für die andere Gruppe mit den folgenden Eigenschaften:
    -   X: 250
    -   Y: 150
    -   Scale: 0.03
    -   Line width: 0.15
    -   Font size: 10mm
    -   Direction: 0,-1,0
    -   Rotation: 90°

Unsere Seite ist nun fertig und wir können sie im SVG- oder DXF-Format ausgeben oder sie drucken. Das SVG-Format erlaubt Dir, die Datei in Illustrationsanwendungen wie [Inkscape](http://www.inkscape.org) zu öffnen, mit denen Du technische Zeichnungen schnell aufwerten und sie in schönere Präsentationszeichnungen verwandeln kannst. Es bietet viel mehr Möglichkeiten als das DXF-Format.

## Herunterladen

-   Die in dieser Übung erstellte Datei <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.FCStd>
-   Die aus der obigen Datei exportierte IFC Datei: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.ifc>
-   Die aus der obigen Datei exportierte SVG Datei: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.svg>

## Verwandtes

-   [BIM Arbeitsbereich](BIM_Workbench/de.md)
-   [Der Arch Arbeitsbereich](Arch_Workbench/de.md)
-   [Die Entwurf Arbeitsebene](Draft_SelectPlane/de.md)
-   [Die Entwurf Fang Einstellungen](Draft_Snap/de.md)
-   [Das Ausdrücke System](Expressions/de.md)
-   [Das IFC Format](https://de.wikipedia.org/wiki/Industry_Foundation_Classes)
-   [IfcOpenShell](http://ifcopenshell.org)
-   [IfcPlusPlus](http://www.ifcquery.com)
-   [Inkscape](http://www.inkscape.org)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [BIM](Category_BIM.md) > [Arch](Category_Arch.md) > Manual:BIM modeling/de
