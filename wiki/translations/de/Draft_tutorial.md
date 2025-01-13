---
 TutorialInfo:e
   Topic:  Technisches Zeichnen
   Level:  Anfänger
   Time:  30 Minuten
   Author: http://freecadweb.org/wiki/index.php?title=User:Drei Drei und vocx
   FCVersion: 0.19
   Files: https://forum.freecad.org/viewtopic.php?f=36&t=43651 Entwurf Tutorium aktualisiert
---

# Draft tutorial/de







## Einleitung

Diese Anleitung wurde ursprünglich von Drei geschrieben und von vocx überarbeitet und illustriert.

Diese Anleitung soll den Leser in den grundlegenden Arbeitsablauf des Arbeitsbereichs <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/de.md) einführen.

Der Leser wird üben:

-   die Erstellung von Linien, Bögen und Polygonen
-   die Verwendung von Arbeitsebenen
-   die Erstellung von Bemaßungen, Text und Textformen
-   die Erstellung einer technischen Zeichnung

Diese Anleitung verwendet die Schreibweise {{Value|(x, y, z)}}, um die zur Definition von Punkten in einem Objekt erforderlichen Koordinaten zu bezeichnen. Die Standardeinheit ist Millimeter {{Value|mm}}.

<img alt="" src=images/00_Dr01_Draft_Tutorial_final.png  style="width:" height="400px;"> 
*Endgültige Zeichnung mit verschiedenen Draft-Objekten.*



## Einrichtung

1\. Öffne FreeCAD, erstelle ein neues leeres Dokument mit **Datei → [<img src=images/Std_New.svg style="width:16px"> [Neu](Std_New.md)**.

:   1.1. Wechsle zum [Arbeitsbereich Draft](Draft_Workbench/de.md) über die [Arbeitsbereich-Auswahl](Std_Workbench/de.md) oder das Menü **Ansicht → Arbeitsbereich → [<img src=images/Workbench_Draft.svg style="width:16px"> Draft**.
:   1.2. Stelle sicher, dass du verstehst, wie der [Eigenschafteneditor](property_editor/de.md), insbesondere die Rreiter **Daten** und **Ansichten** zum Ändern der Eigenschaften zu verwenden sind.

Wenn Eigenschaften geändert werden, musst du eventuell eine **<img src="images/Std_Refresh.svg" width=16px> [Std Aktualisierung](Std_Refresh/de.md)** vornehmen, um das Ergebnis in der [3D-Ansicht](3D_view/de.md) zu sehen.

:   1.3. Da es sich bei den Draft-Objekten um ebene Formen handelt, sind sie von oben besser zu sehen. Verwende **[<img src=images/Std_ViewTop.svg style="width:16px"> [Draufsicht](Std_ViewTop/de.md)** zum setzen der [3D-Ansicht](3D_view/de.md).
:   1.4. Obwohl es in dieser Anleitung nicht verwendet wird, ist das Draft-Raster hilfreich, um geometrische Elemente zu positionieren. Verwende **[<img src=images/Draft_SelectPlane.svg style="width:16px"> [Ebene auswählen](Draft_SelectPlane/de.md)**, um sowohl die Arbeitsebene als auch das Raster festzulegen, und dann das Raster mit **[<img src=images/Draft_ToggleGrid.svg style="width:16px"> [Raster umschalten](Draft_ToggleGrid/de.md)** anzuzeigen und auszublenden.



## Werkzeugleiste Draft-Einrasten 

2\. Die Werkzeugleiste [Draft-Einrasten](Draft_Snap/de.md) wird normalerweise aktiviert, wenn du zum Arbeitsbereich [Draft](Draft_Workbench/de.md) wechselst.

:   2.1. Um sicherzustellen, dass sie immer vorhanden ist, gehe zu den [Draft-Einstellungen](Draft_Preferences/de.md), **Bearbeiten → Einstellungen → Draft → Raster und Einrasten**.
:   2.2. Stelle sicher, dass die **Werkzeugleiste Draft-Einrasten anzeigen** aktiv ist.

Du kannst auch die Sichtbarkeit und die Eigenschaften des Draft-Rasters im gleichen Fenster ändern.



## Arbeitsebenen

Die meisten Draft-Objekte sind ebene Formen, so dass sie natürlich auf einer **Arbeitsebene** aufbauen. Eine Arbeitsebene kann eine der globalen Hauptkoordinatenebenen XY, XZ und YZ sein, oder es kann eine Ebene sein, die parallel zu diesen Ebenen mit einem positiven oder negativen Versatz verläuft, oder es kann eine Ebene sein, die durch die Fläche eines Festkörperobjekts definiert ist.

3\. Drücke **[<img src=images/Draft_SelectPlane.svg style="width:16px"> [Ebene auswählen](Draft_SelectPlane/de.md)**, oder gehe zum Menü **Dienstprogramme → [<img src=images/Draft_SelectPlane.svg style="width:16px"> [Ebene auswählen](Draft_SelectPlane/de.md)**, um die [Aufgaben-Bereich](task_panel/de.md) Arbeitsebene einrichten zu öffnen.

:   3.1. Drücke **[<img src=images/Std_ViewTop.svg style="width:16px"> Draufsicht (XY)**.

Vor dem drücken der Taste kannst du auch den Wert des Versatzes in Millimetern sowie den Rasterabstand, die Hauptlinien und den Einrastradius ändern.



## Linien und Bögen 

4\. Wir werden Bögen und Linien erstellen.

:   4.1. Drücke **[<img src=images/Draft_Arc.svg style="width:16px"> [Kreisogen](Draft_Arc/de.md)**.
:   4.2. Setze den **Mittelpunkt** auf {{Value|(0, 0, 0)}}, und drücke **Enter**.
:   4.3. Setze den **Radius** auf {{Value|30 mm}}, und drücke **Enter**.
:   4.4. Setze den **Startwinkel** auf {{Value|60.0°}}, und drücke **Enter**.
:   4.5. Setze den **Öffnungswinkel** auf {{Value|60.0°}}, und drücke **Enter**.
:   4.6. Wiederhole das gleiche Verfahren für einen zweiten Bogen mit einem Radius von {{Value|25 mm}}, die anderen Eigenschaften sind die gleichen.

5\. Wir werden nun ein geschlossenes Profil erzeugen, indem wir die Bögen mit Linien verbinden.

:   5.1. Drücke **[<img src=images/Draft_Line.svg style="width:16px"> [Linie](Draft_Line/de.md)**.
:   5.2. Stelle in der Werkzeugleiste [Draft-Einrasten](Draft_Snap/de.md) sicher, dass **[<img src=images/Draft_Snap_Lock.svg style="width:16px"> [Einrasten sperren](Draft_Snap_Lock/de.md)** aktiv ist, und außerdem nur **[<img src=images/Draft_Snap_Endpoint.svg style="width:16px"> [Einrasten auf Endpunkt](Draft_Snap_Endpoint/de.md)**. Wenn du den Zeiger auf einen Endpunkt eines Bogens bewegst, sollte das <img alt="" src=images/Draft_Snap_Endpoint.svg  style="width:24px;"> Symbol [Einrasten auf Endpunkt](Draft_Snap_Endpoint/de.md) erscheinen. Klicke diesen Punkt zum auswählen.
:   5.3. Bewege den Zeiger auf den nächstgelegenen Endpunkt des anderen Bogens, um die beiden Bögen miteinander zu verbinden.
:   5.4. Wiederhole den Vorgang für die andere Seite des Bogens, um das Profil zu schließen.

<img alt="" src=images/01_Dr01_Draft_Arc_profile.png  style="width:" height="400px;"> 
*Geschlossenes Profil, das durch zwei Bögen und zwei Linien erzeugt wird.*



## Verschmelzen oder Zusammensetzen 

Wir haben jetzt mehrere Objekte in der [Baumansicht](tree_view/de.md), die ein geschlossenes Profil bilden. Dieses Profil besteht jedoch nach wie vor aus unverbundenen Objekten; jedes von ihnen kann unabhängig von den anderen bearbeitet und verschoben werden. Es ist möglich, mit den Elementen auf diese Weise weiter zu arbeiten, aber es ist auch möglich, sie zu einem einzigen Objekt zu verschmelzen.

6a. Beachte, dass das Verschmelzen der Objekte zu einem einzigen Objekt ein Objekt erzeugt, das nicht mehr parametrisch ist, so dass ihre Eigenschaften nicht weiter geändert werden können.

:   6a.1 Wähle alle vier Objekte in der [Baumansicht](tree_view/de.md) oder mit gedrückt gehaltener **Ctrl**-Taste in der [3D-Ansicht](3D_view/de.md) .

6a.2 Wenn diese Objekte ausgewählt sind, klicke auf **[<img src=images/Draft_Upgrade.svg style="width:16px"> [Hochstufen](Draft_Upgrade/de.md)**.

:   6a.3 Dadurch werden die vier Objekte zu einer einzigen {{Value|Polylinie}} aufgewertet.

6b. Wenn du die parametrische Natur der Objekte beibehalten möchtest, kannst du stattdessen einen Verbund erstellen.

:   6b.1. Wechsle zum Arbeitsbereich <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/de.md).
:   6b.2 Wenn diese Objekte ausgewählt sind, klicke auf **[<img src=images/Part_Compound.svg style="width:16px"> [Part Erzeuge Verbund](Part_Compound/de.md)**.



## Rechtecke, Kreise und Polygone 

7\. Wir werden einen rechteckigen Rahmen zeichnen. (Wechsle zurück zum Arbeitsbereich <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Draft](Draft_Workbench/de.md).)

:   7.1. Drücke **[<img src=images/Draft_Rectangle.svg style="width:16px"> [Rechteck](Draft_Rectangle/de.md)**.
:   7.2. Gib die Werte des ersten Punktes {{Value|(-100, -60, 0)}} ein und drücke **Enter**.
:   7.3. Stelle sicher, dass die **Relativ** Option nicht angehakt ist, da wir absolute Einheiten verwenden werden. Du kannst **R** auf der Tastatur drücken, um diese Option schnell ein- und auszuschalten.
:   7.4. Gib die Werte für den zweiten Punkt {{Value|(140, 90, 0)}} ein und drücke **Enter**.

Ein Rechteck wird erstellt. Gehe in den [Eigenschafteneditor](Property_editor/de.md), um seine Eigenschaften zu ändern. Wenn das Rechteck keine Fläche erzeugen soll, setze die {{PropertyData/de|Make Face}} auf `False`. Wenn du eine Fläche erstellen möchtest, aber nur die Drähte dieses Objekts siehst, lass die {{PropertyData/de|Make Face}} auf `True`, aber setze die {{PropertyView/de|Display Mode}} auf {{Value|Wireframe}}.

8\. Wir werden einen Kreis zeichnen.

:   8.1. Drücke **[<img src=images/Draft_Circle.svg style="width:16px"> [Kreis](Draft_Circle.md)**.
:   8.2. Gib die Werte des Zentrums {{Value|(0, 0, 0)}} ein und drücke **Enter**.
:   8.3. Setze den Radius auf {{value|15 mm}} und drücke **Enter**.

9\. Wir werden ein regelmäßiges Vieleck (Polygon) zeichnen.

:   9.1. Drücke **[<img src=images/Draft_Polygon.svg style="width:16px"> [Vieleck](Draft_Polygon/de.md)**.
:   9.2. Gib die Werte des Zentrums {{Value|(0, 0, 0)}} ein, und drücke **Enter**.
:   9.3. Setze die Anzahl der Seiten auf {{Value|6}}, und drücke **Enter**.
:   9.4. Setze den Radius auf {{Value|50 mm}}, und drücke **Enter**.

Auch hier kannst du die {{PropertyData/de|Make Face}} und die {{PropertyView/de|Anzeigemodus}} im [Eingenschafteneditor](property_editor/de.md) ändern, wenn du möchtest.

Das Rechteck, der Kreis, das Vieleck und die meisten anderen Objekte, die mit dem Arbeitsbereich [Draft](Draft_Workbench/de.md) erstellt werden, haben viele gemeinsame Daten- und Ansicht-Eigenschaften, da sie von derselben Basisklasse [Part Part2DObject](Part_Part2DObject/de.md) abgeleitet sind.

<img alt="" src=images/02_Dr01_Draft_Rectangle_circle_polygon.png  style="width:" height="400px;"> 
*Rechteck, Kreis und Polygon hinzugefügt.*



## Anordnungen

Anordnungen werden verwendet, um ein Objekt mehrmals in einer orthogonalen Richtung (X, Y, Z), um eine Drehachse oder entlang eines Pfades zu vervielfältigen.

10\. Wir werden eine polare Anordnung erstellen.

:   10.1. Wähle das {{Value|Wire}}-Objekt (Polylinie), das zuvor mit dem Werkzeug **[<img src=images/Draft_Upgrade.svg style="width:16px"> [Hochstufen](Draft_Upgrade/de.md)** erstellt wurde, oder den {{Value|Verbund}} erstellt mit dem Werkzeug **[<img src=images/Part_Compound.svg style="width:16px"> [Part Erzeuge Verbund](Part_Compound/de.md)**.
:   10.2. Drücke **[<img src=images/Draft_PolarArray.svg style="width:16px"> [Polare Anordnung](Draft_PolarArray/de.md)**.
:   10.3. Stelle den Polarwinkel auf {{Value|360°}} ein.
:   10.4. Setze die Anzahl der Elemente auf {{Value|4}}.
:   10.5. Gib die Werte für den Drehmittelpunkt {{Value|(0, 0, 0)}} ein und drücke **Enter**.

Die Anordnung (Array-Objekt) stellt Kopien des Objekts um den Ursprung herum dar.

<img alt="" src=images/03_Dr01_Draft_PolarArray.png  style="width:" height="400px;"> 
*Polare Anordnung des kleinen Profils um den Ursprung zentriert.*



## Abmessungen

Lineare Maße funktionieren am besten, wenn die geeigneten Methoden zum [Draft-Einrasten](Draft_Snap/de.md) für die Auswahl der zu messenden Punkte und Kanten eingesetzt werden. Sie können jedoch auch durch Angabe absoluter Koordinaten erstellt werden.

11\. Maße für die verschiedenen Objekte erstellen.

:   11.1. Drücke **[<img src=images/Draft_Dimension.svg style="width:16px"> [Abmessung](Draft_Dimension/de.md)**.
:   11.2. Nimm den ersten Punkt. In diesem Tutorial wird der erste Punkt immer der Ursprung sein. {{Value|(0, 0, 0)}}.
:   11.3. In der Werkzeugleiste [Draft-Einrasten](Draft_Snap/de.md) stelle sicher das **[<img src=images/Draft_Snap_Lock.svg style="width:16px"> [Einrasten sperren](Draft_Snap_Lock/de.md)** aktiv ist und außerdem nur **[<img src=images/Draft_Snap_Midpoint.svg style="width:16px"> [Einrasten auf Mittelpunkt](Draft_Snap_Midpoint/de.md)**. Sowie du den Zeiger auf die Oberkante des Polygons bewegst, sollte das Symbol <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:24px;"> [Einrasten auf Mittelpunkt](Draft_Snap_Midpoint/de.md) erscheinen; klicke, um diesen Punkt auszuwählen.
:   11.4. Bewege den Cursor nach rechts, um die Position des Maßes anzugeben, und klicke dann, um die Endposition um {{Value|(100, 20, 0)}} festzulegen. Das Maß zeigt automatisch den zwischen den beiden Punkten gemessenen Längenwert an.
:   11.5. Wähle das Maß (Dimension-Objekt) in der [Baumansicht](tree_view/de.md) aus und ändere im [Eigenschafteneditor](Property_editor/de.md) die {{PropertyView/de|Fontsize}} auf {{Value|6 mm}}, setze die {{PropertyView/de|Ext Lines}} auf {{Value|45 mm}}, und die {{PropertyView/de|Show Unit}} auf `False`.

12\. Wiederhole den Vorgang für die beiden Bögen des geschlossenen Profils. Der erste Punkt des Maßes ist immer noch der Ursprung, und der zweite Punkt verwendet den <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:24px;"> [Mittelpunkt](Draft_Snap_Midpoint/de.md) des Bogens.

13\. Wiederhole den Vorgang für den Kreis in der Mitte. Der erste Punkt des Maßes ist immer noch der Ursprung. Um den zweiten Punkt auszuwählen, stelle sicher, dass **[<img src=images/Draft_Snap_Lock.svg style="width:16px"> [Einrasten sperren](Draft_Snap_Lock/de.md)** aktiv ist und außerdem nur **[<img src=images/Draft_Snap_Angle.svg style="width:16px"> [Einrastwinkel](Draft_Snap_Angle/de.md)**. Sobald du den Zeiger an den oberen Rand des Kreises bewegst, sollte das Symbol <img alt="" src=images/Draft_Snap_Angle.svg  style="width:24px;"> [Einrastwinkel](Draft_Snap_Angle/de.md) erscheinen; klicke, um diesen Punkt auszuwählen. Bewege dann den Cursor nach rechts, und klicke, um das Maß zu fixieren.

Denke daran, die {{PropertyView/de|Font Size}} und andere Eigenschaften anzupassen, damit das Maß korrekt angezeigt wird.

<img alt="" src=images/04_Dr01_Draft_Dimension.png  style="width:" height="400px;"> 
*Maße, die den vertikalen Abstand vom Ursprung bis zur Oberkante des Kreises, der Bögen und des Polygons messen.*



## Texte und Textformen 

14\. Textobjekte sind einfache planare Figuren, die in der [3D-Ansicht](3D_view/de.md) erstellt werden, denen aber keine tatsächliche \"[Form](Shape/de.md)\" zugrunde liegt. Das bedeutet, dass sie nicht in komplexen Operationen mit Formen wie Extrusionen oder boolesche Verknüpfungen verwendet werden können.

:   14.1. Die Schaltfläche **[<img src=images/Draft_Text.svg style="width:16px"> [Text](Draft_Text/de.md)** drücken.
:   14.2. Den Referenzpunkt in der [3D-Ansicht](3D_view/de.md) auswählen. In der Werkzeugleiste [Draft-Einrasten](Draft_Snap/de.md) sollte sichergestellt werden, dass **[<img src=images/Draft_Snap_Lock.svg style="width:16px"> [Einrasten sperren](Draft_Snap_Lock/de.md)** aktiv ist, und außerdem nur **[<img src=images/Draft_Snap_Midpoint.svg style="width:16px"> [Einrasten auf Mittelpunkt](Draft_Snap_Midpoint/de.md)**. Den Mauszeiger auf die Oberkante des höchsten Bogens bewegen, so dass das Symbol <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:24px;"> [Mittelpunkt](Draft_Snap_Midpoint/de.md) erscheint; klicken um diesen Punkt auszuwählen.
:   14.3. Den gewünschten **Text** eingeben und einmal **Enter** drücken, um eine neue Zeile zu beginnen; bei Bedarf weitere Textzeilen hinzufügen.
:   14.4. Ist alles eingegeben, zum Beenden zweimal **Enter** drücken.
:   14.5. Das Textobjekt in der [Baumansicht](tree_view/de.md) auswählen, und im [Eigenschafteneditor](Property_editor/de.md) {{PropertyView/de|Schriftgröße}} auf {{Value|6 mm}} und {{PropertyView/de|Ausrichtung}} auf {{Value|Center}} ändern.

15\. Textformen sind Formen aus primitiven Linienzügen, die Linien folgen, die durch eine bestimmte Schriftart vorgegeben werden. Das bedeutet, dass diesen Objekten eine echte \"[Form](Shape/de.md)\" zugrunde liegt und sie daher in komplexen Operationen wie Extrusionen und booleschen Verknüpfungen verwendet werden können.

:   15.1. Die Schaltfläche **[<img src=images/Draft_ShapeString.svg style="width:16px"> [Textform](Draft_ShapeString/de.md)** drücken.
:   15.2. Den Mauszeiger an die gewünschte Stelle in der [3D-Ansicht](3D_view/de.md) über dem regelmäßigen Vieleck bewegen und einmal klicken. Dadurch wird der Basispunkt für die Textform festgelegt. Die Koordinaten können auch manuell eingegeben werden, zum Beispiel {{Value|(-20, 65, 0)}}.
:   15.3. Die gewünschte **Zeichenkette** eingeben und die gewünschte **Höhe** auswählen.
:   15.4. Ist keine Standardschriftartdatei vorhanden: Die Schaltfläche **...** anklicken, um ein Dialogfeld zur Auswahl des Speicherorts der Schriftart im System zu öffnen.
:   15.5. Wenn eine gültige Schriftartdatei ausgewählt wurde, kann zum Fortfahren **OK** angeklickt oder **Enter**gedrückt werden.

<img alt="" src=images/05_Dr01_Draft_Text_ShapeString.png  style="width:" height="400px;"> 
*Text und Textform hinzugefügt.*

Um Buchstaben zu extrudieren und in Festkörper zu gravieren, siehe die [Draft Textform-Anleitung](Draft_ShapeString_tutorial/de.md).



## Eine technische Zeichnung erstellen 

So wie es jetzt ist, können die von uns erstellten Objekte gespeichert, in andere Formate wie [SVG](SVG/de.md) oder [DXF](DXF/de.md) exportiert oder gedruckt werden.

Jetzt kann eine technische Zeichnung erstellt werden, um diese Objekte zusammen mit weiteren Informationen wie einem Rahmen darzustellen.

Vor allen anderen Tätigkeiten sollte das Raster durch Drücken der Schaltfläche **[<img src=images/Draft_ToggleGrid.svg style="width:16px"> [Raster umschalten](Draft_ToggleGrid/de.md)** ausgeblendet werden.

16\. Zum Arbeitsbereich <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw](TechDraw_Workbench/de.md) wechseln.

:   16.1. Eine Standardseite durch Drücken von **[<img src=images/TechDraw_PageDefault.svg style="width:16px"> [TechDraw Neues Zeichnungsblatt aus der Standardvorlage erstellen](TechDraw_PageDefault/de.md)** erstellen.
:   16.2. In der [Baumansicht](tree_view/de.md) alle erstellten Objekte außer dem Zeichnungsblatt auswählen und dann die Schaltfläche **[<img src=images/TechDraw_ActiveView.svg style="width:16px"> [TechDraw Aktive (3D)-Ansicht einfügen](TechDraw_ActiveView/de.md)** drücken. Mit den Standardoptionen **OK** drücken; es kann einige Sekunden dauern, bis die Ansicht auf dem Blatt erstellt ist.
:   16.3. In der [Baumansicht](tree_view/de.md) das Zeichnungsblatt auswählen; damit wird das Blatt automatisch im Hauptfenster anzeigen. Mit ausgewähltem Blatt im [Eigenschafteneditor](Property_editor/de.md) die {{PropertyData/de|Maßstab}} auf {{Value|0.75}} setzen.
:   16.4. Das Zeichnungsblatt in der [Baumansicht](tree_view/de.md) erweitern und das Objekt Aktive Ansicht auswählen. Im [Eigenschafteneditor](Property_editor/de.md) die {{PropertyData/de|Scale Type}} auf {{Value|Page}} setzen.
:   16.5. Die schaltfläche **[<img src=images/Std_Refresh.svg style="width:16px"> [Aktualisieren](Std_Refresh/de.md)** oder **F5** drücken, um das Modell neu zu berechnen.
:   16.6. Die Rahmen der Ansichten werden durch drücken der Schaltfläche **[<img src=images/TechDraw_ToggleFrame.svg style="width:16px"> [TechDraw Ansichtsrahmen ein- oder ausschalten](TechDraw_ToggleFrame/de.md)** ausgeblendet.

Erfahre mehr über den Arbeitsbereich [TechDraw](TechDraw_Workbench/de.md) durch Lesen des [TechDraw Grundlagen Tutorium](Basic_TechDraw_Tutorial/de.md).

<img alt="" src=images/06_Dr01_Draft_TechDraw_page.png  style="width:" height="400px;"> 
*TechDraw Zeichnungsblatt mit einer Projektion der mit dem Arbeitsbereich Draft erstellten Formen.*

TechDraw funktioniert am besten mit Objekten, die eine [Part TopoForm](Part_TopoShape/de.md) besitzen. Da einige Objekte aus Draft, wie [Draft-Text](Draft_Text/de.md) und [Draft-Maß](Draft_Dimension/de.md), nicht über solche \"[Formen](Shape/de.md)\" verfügen, funktionieren einige Operationen von TechDraw nicht mit diesen Elementen.

Werkzeuge wie **[<img src=images/TechDraw_ActiveView.svg style="width:16px"> [TechDraw AktiveAnsicht](TechDraw_ActiveView/de.md)**, **[<img src=images/TechDraw_DraftView.svg style="width:16px"> [TechDraw DraftAnsicht](TechDraw_DraftView/de.md)**, und **[<img src=images/TechDraw_ArchView.svg style="width:16px"> [TechDraw ArchAnsicht](TechDraw_ArchView/de.md)** arbeiten, indem sie ein internes SVG-Bild erhalten, das von internen Draft-Funktionen erzeugt wird; daher hat TechDraw keine große Kontrolle darüber, wie diese Ansichten angezeigt werden. Die weitere Integration von Draft und TechDraw ist noch in Arbeit.



## Schlussbemerkungen

Der Arbeitsbereich [Draft](Draft_Workbench/de.md) ähnelt in vielerlei Hinsicht dem Arbeitsbereich [Sketcher](Sketcher_Workbench/de.md), da beide zur Erzeugung von 2D-Formen gedacht sind. Der Hauptunterschied besteht in der Art und Weise, wie jeder Arbeitsbereich Koordinatensysteme handhabt und wie die Objekte positioniert werden. In Draft werden die Objekte frei im globalen Koordinatensystem positioniert, wobei ihre Punkte normalerweise an einem Raster oder an anderen Objekten einrasten. Im Sketcher definiert ein \"[Sketch-Objekt](Sketch/de.md)\" ein lokales Koordinatensystem, das als Referenz für alle geometrischen Elemente innerhalb dieser Skizze dient. Darüber hinaus stützt sich die Skizze auf \"Randbedingungen\", um die endgültige Position ihrer Punkte festzulegen.

-   Der Arbeitsbereich [Draft](Draft_Workbench/de.md) ist für 2D-Zeichnungen vorgesehen, die sich zum Zeichnen auf einem Gitter eignen. Der Arbeitsbereich [BIM](BIM_Workbench/de.md) baut meist auf den im Arbeitsbereich [Draft](Draft_Workbench/de.md) definierten Werkzeugen auf.

-   Der Arbeitsbereich [Sketcher](Sketcher_Workbench/de.md) ist für 2D-Zeichnungen gedacht, die präzise Beziehungen zwischen ihren Punkten erfordern. Er stützt sich nicht auf ein Raster, sondern auf Positionierungsregeln (Randbedingungen), um zu bestimmen, wo die Punkte und Kanten platziert werden sollen. Der Arbeitsbereich [Sketcher](Sketcher_Workbench/de.md) wird meistens zusammen mit dem Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md) für die Erstellung von Festkörpern [Körper](Body/de.md) verwendet.

-   Es ist möglich, ein Draft-Objekt in eine [Skizze](Sketch/de.md) umzuwandeln und umgekehrt, indem man das Werkzeug **[<img src=images/Draft_Draft2Sketch.svg style="width:16px"> [Draft ZeichnungZuSkizze](Draft_Draft2Sketch.md)** verwendet.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft tutorial/de
