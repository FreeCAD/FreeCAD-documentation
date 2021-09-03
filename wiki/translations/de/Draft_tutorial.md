


{{TutorialInfo/de
|Topic= Technisches Zeichnen
|Level= Anfänger
|Time= 30 Minuten
|Author=[http://freecadweb.org/wiki/index.php?title=User:Drei Drei] und vocx
|FCVersion=0.19
|Files=[https://forum.freecadweb.org/viewtopic.php?f=36&t=43651 Entwurf Tutorium aktualisiert]
}}

## Einführung

Dieses Tutorium wurde ursprünglich von Drei geschrieben, und es wurde von vocx neu geschrieben und illustriert.


<div class="mw-translate-fuzzy">

Dieses Tutorium soll den Leser in den grundlegenden Arbeitsablauf des <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Entwurf Arbeitsbereich](Draft_Module/de.md) einführen.


</div>

Der Leser wird üben:

-   Erstellung von Linien, Bögen und Polygonen
-   die Verwendung von Arbeitsebenen
-   die Erstellung von Bemaßungen, Text und Formzeichenketten
-   die Erstellung einer technischen Zeichnung

Dieses Tutorial verwendet die Schreibweise {{Value|(x, y, z)}}, um die zur Definition von Punkten in einem Objekt erforderlichen Koordinaten zu bezeichnen. Die Standardeinheit ist Millimeter {{Value|mm}}.

<img alt="" src=images/00_Dr01_Draft_Tutorial_final.png  style="width:" height="400px;"> 
*Endgültige Zeichnung mit verschiedenen Entwurfsobjekten.*

## Einrichtung


<div class="mw-translate-fuzzy">

1\. Öffne FreeCAD, erstelle ein neues leeres Dokument mit **Datei → <img src=images/Std_New.svg style="width:16px"> [Neu](Std_New.md)**.

:   1.1. Wechsle zum <img src=images/Workbench_Draft.svg style="width:Arbeitsbereich Entwurf](Draft_Module/de.md) über die [Arbeitsbereich Wähler](Std_Workbench/de.md) oder das Menü **Ansicht → Arbeitsbereich → [16px"> Entwurf**.
:   1.2. Stelle sicher, dass du verstehst, wie der [Eigenschaftseditor](property_editor/de.md), insbesondere die **Daten** und **Ansichten** Reiter zum Ändern der Eigenschaften zu verwenden sind.

Wenn Eigenschaften geändert werden, musst du eventuell eine **<img src="images/Std_Refresh.svg" width=16px> [Std Aktualisierung](Std_Refresh/de.md)**shandlung vornehmen, um das Ergebnis in der [3D Ansicht](3D_view/de.md) zu sehen.

:   1.3. Da es sich bei den Entwurfsobjekten um ebene Formen handelt, sind sie von oben besser zu sehen. Verwende **<img src=images/Std_ViewTop.svg style="width:16px"> [Ansicht oben](Std_ViewTop/de.md)** zum setzen der [3D Ansicht](3D_view/de.md).
:   1.4. Obwohl es in diesem Tutorium nicht verwendet wird, ist das Entwurfsgitter hilfreich, um geometrische Elemente zu positionieren. Verwende **<img src=images/Draft_SelectPlane.svg style="width:16px"> <img src=images/Draft_ToggleGrid.svg style="width:WähleEbene](Draft_SelectPlane/de.md)**, um sowohl die Arbeitsebene als auch das Gitter festzulegen, und dann das Gitter mit **[16px"> [Gitter umschalten](Draft_ToggleGrid/de.md)** anzuzeigen und auszublenden.


</div>

## Fang Werkzeugleiste 


<div class="mw-translate-fuzzy">

2\. Die [Entwurf Fang](Draft_Snap/de.md) Werkzeugleiste wird normalerweise aktiviert, wenn du zum [Entwurf Arbeitsbereich](Draft_Module/de.md) wechselst.

:   2.1. Um sicherzustellen, dass sie immer vorhanden ist, gehe zu [Entwurf Einstellungen](Draft_Preferences/de.md), **Bearbeiten → Einstellungen → Entwurf → Gitter und Fang Reiter**.
:   2.2. Stelle sicher, dass die **Werkzeugleiste Entwurfsfang anzeigen** aktiv ist.


</div>

Du kannst auch die Sichtbarkeit und die Eigenschaften des Entwurfsgitters im gleichen Fenster ändern.

## Arbeitsebenen

Die meisten Entwurfsobjekte sind planare Formen, so dass sie natürlich auf einer **Arbeitsebene** aufbauen. Eine Arbeitsebene kann eine der globalen Hauptkoordinatenebenen XY, XZ und YZ sein, oder es kann eine Ebene sein, die parallel zu diesen Ebenen mit einem positiven oder negativen Versatz verläuft, oder es kann eine Ebene sein, die durch die Fläche eines festen Objekts definiert ist.

3\. Drücke **<img src=images/Draft_SelectPlane.svg style="width:16px"> <img src=images/Draft_SelectPlane.svg style="width:Wähle Ebene](Draft_SelectPlane/de.md)**, oder gehe zum Menü **Hilfsmittel → [16px"> [Select plane](Draft_SelectPlane.md)**, um die Arbeitsebene [Aufgabenpaneel](task_panel/de.md) zu öffnen.

:   3.1. Drücke **<img src=images/Std_ViewTop.svg style="width:16px"> Oben (XY)**.

Vor dem drücken der Taste kannst du auch den Wert des Versatzes in Millimetern sowie den Rasterabstand, die Hauptlinien und den Fangradius ändern.

## Linien und Bögen 

4\. Wir werden Bögen und Linien erstellen.

:   4.1. Drücke **<img src=images/Draft_Arc.svg style="width:16px"> [Bogen](Draft_Arc/de.md)**.
:   4.2. Setze den **Mittelpunkt** auf {{Value|(0, 0, 0)}}, und drücke **Enter**.
:   4.3. Setze den **Radius** auf {{Value|30 mm}}, und drücke **Enter**.
:   4.4. Set the **Anfangswinkel** auf {{Value|60.0°}}, und drücke **Enter**.
:   4.5. Setze den **Öffnungswinkel** auf {{Value|60.0°}}, und drücke **Enter**.
:   4.6. Wiederhole das gleiche Verfahren für einen zweiten Bogen mit einem Radius von {{Value|25 mm}}, die anderen Eigenschaften sind die gleichen.

5\. Wir werden nun ein geschlossenes Profil erzeugen, indem wir die Bögen mit Linien verbinden.

:   5.1. Drücke **<img src=images/Draft_Line.svg style="width:16px"> [Linie](Draft_Line/de.md)**.
:   5.2. Stelle in der Werkzeugleiste <img src=images/Draft_ToggleSnap.svg style="width:Fang](Draft_Snap/de.md) sicher, dass **[16px"> <img src=images/Draft_Endpoint.svg style="width:Fang umschalten](Draft_ToggleSnap/de.md)** aktiv ist, und nur **[16px"> [Endpunkt](Draft_Endpoint/de.md)** ebenfalls. Wenn du den Zeiger auf einen Endpunkt eines Bogens bewegst, sollte das <img alt="" src=images/Draft_Endpoint.svg  style="width:24px;"> Symbol [Endpunkt](Draft_Endpoint/de.md) erscheinen. Klicke diesen Punkt zum auswählen .
:   5.3. Bewege den Zeiger auf den nächstgelegenen Endpunkt des anderen Bogens, um die beiden Bögen miteinander zu verbinden.
:   5.4. Wiederhole den Vorgang für die andere Seite des Bogens, um das Profil zu schließen.

<img alt="" src=images/01_Dr01_Draft_Arc_profile.png  style="width:" height="400px;"> 
*Geschlossenes Profil, das durch zwei Bögen und zwei Linien erzeugt wird.*

## Verschmelzen oder Zusammensetzen 

Wir haben jetzt mehrere Objekte in der [Baumansicht](tree_view/de.md), die ein geschlossenes Profil bilden. Dieses Profil besteht jedoch nach wie vor aus unverbundenen Objekten; jedes von ihnen kann unabhängig von den anderen bearbeitet und verschoben werden. Es ist möglich, mit den Elementen auf diese Weise weiter zu arbeiten, aber es ist auch möglich, sie zu einem einzigen Objekt zu verschmelzen.

6a. Beachte, dass das Verschmelzen der Objekte zu einem einzigen Objekt ein Objekt erzeugt, das nicht mehr parametrisch ist, so dass ihre Eigenschaften nicht weiter geändert werden können.

:   6a.1 Wähle alle vier Objekte in der [Baumansicht](tree_view/de.md) oder durch **Ctrl** halten und greifen in der [3D Ansicht](3D_view/de.md) .

6a.2 Wenn diese Objekte ausgewählt sind, klicke auf **<img src=images/Draft_Upgrade.svg style="width:16px"> [Aufwerten](Draft_Upgrade/de.md)**.

:   6a.3 Dadurch werden die vier Objekte zu einem einzigen {{Value|Draht}} aufgewertet.


<div class="mw-translate-fuzzy">

6b. Wenn du die parametrische Natur der Objekte beibehalten möchtest, kannst du stattdessen einen Verbund erstellen.

:   6b.1. Wechsle zum <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Arbeitsbereich Part](Part_Workbench/de.md).
:   6b.2 Wenn diese Objekte ausgewählt sind, klicke auf **<img src=images/Part_Compound.svg style="width:16px"> [Part Verbund](Part_Compound/de.md)**.


</div>

## Rechtecke, Kreise und Polygone 

7\. Wir werden einen rechteckigen Rahmen zeichnen. (Wechsle zurück zum <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Entwurf Arbeitsbereich](Draft_Workbench/de.md).)

:   7.1. Drücke **<img src=images/Draft_Rectangle.svg style="width:16px"> [Rechteck](Draft_Rectangle/de.md)**.
:   7.2. Gib die Werte des ersten Punktes {{Value|(-100, -60, 0)}} ein und drücke **Enter**.
:   7.3. Stelle sicher, dass die **Relativ** Option nicht angehakt ist, da wir absolute Einheiten verwenden werden. Du kannst **R** auf der Tastatur drücken, um diese Option schnell ein- und auszuschalten.
:   7.4. Gib die Werte für den zweiten Punkt {{Value|(140, 90, 0)}} ein und drücke **Enter**.

Ein Rechteck wird erstellt. Gehe in den [Eigenschaftseditor](Property_editor/de.md), um seine Eigenschaften zu ändern. Wenn das Rechteck keine Fläche erzeugen soll, setze **Erstelle Fläche** auf `False`. Wenn du eine Fläche erstellen möchtest, aber nur die Drähte dieses Objekts siehst, lassen **Erstelle Fläche** auf `True`, aber setze den **Anzeigemodus** auf {{Value|Wireframe}}.

8\. Wir werden einen Kreis zeichnen.

:   8.1. Drücke **<img src=images/Draft_Circle.svg style="width:16px"> [Kreis](Draft_Circle.md)**.
:   8.2. Gib die Werte des Zentrums {{Value|(0, 0, 0)}} ein und drücke **Enter**.
:   8.3. Setze den Radius auf {{value|15 mm}} und drücke **Enter**.

9\. Wir werden ein regelmäßiges Polygon zeichnen.

:   9.1. Drücke **<img src=images/Draft_Polygon.svg style="width:16px"> [Polygon](Draft_Polygon/de.md)**.
:   9.2. Gib die Werte des Zentrums {{Value|(0, 0, 0)}} ein, und drücke **Enter**.
:   9.3. Setze die Anzahl der Seiten auf {{Value|6}}, und drücke **Enter**.
:   9.4. Setze den Radius auf {{Value|50 mm}}, und drücke **Enter**.

Auch hier kannst du die Eigenschaften {**Make Face**} und {{PropertyView/de|Anzeigemodus}} im [Eingenschaftseditor](property_editor/de.md) ändern, wenn du möchtest.


<div class="mw-translate-fuzzy">

Das Rechteck, der Kreis, das Polygon und die meisten anderen Objekte, die mit der [Entwurf Arbeitsbereich](Draft_Module/De.md) erstellt werden, haben viele gemeinsame Daten- und Ansichtseigenschaften, da sie von derselben Basisklasse [Part Teil2DObjekt](Part_Part2DObject/de.md) abgeleitet sind.


</div>

<img alt="" src=images/02_Dr01_Draft_Rectangle_circle_polygon.png  style="width:" height="400px;"> 
*Rechteck, Kreis und Polygon hinzugefügt.*

## Anordnungen

Anordnungen werden verwendet, um ein Objekt mehrmals in einer orthogonalen Richtung (X, Y, Z), um eine Drehachse oder entlang eines Pfades zu vervielfältigen.

10\. Wir werden eine polare Anordnung erstellen.

:   10.1. Wähle das {{Value|Draht}} Objekt, das zuvor mit dem **<img src=images/Draft_Upgrade.svg style="width:16px"> <img src=images/Part_Compound.svg style="width:Upgrade](Draft_Upgrade.md)** Werkzeug erstellt wurde, oder den {{Value|Verbund}} erstellt mit dem **[16px"> [Part Verbund](Part_Compound/de.md)** Werkzeug.
:   10.2. Drücke **<img src=images/Draft_PolarArray.svg style="width:16px"> [PolarAnordnung](Draft_PolarArray/de.md)**.
:   10.3. Stelle den Polarwinkel auf {{Value|360°}} ein.
:   10.4. Setze die Anzahl der Elemente auf {{Value|4}}.
:   10.5. Gib die Werte für das Drehzentrum {{Value|(0, 0, 0)}} ein und drücke **Enter**.

Das Anordnungsobjekt zeigt Kopien des Objekts um den Ursprung herum an.

<img alt="" src=images/03_Dr01_Draft_PolarArray.png  style="width:" height="400px;"> 
*Polaranordnung des kleinen Profils um den Ursprung zentriert.*

## Abmessungen

Lineare Bemaßungen funktionieren am besten, wenn die geeigneten [Entwurf Fang](Draft_Snap/de.md) Methoden zur Auswahl der zu messenden Punkte und Kanten verwendet werden. Sie können jedoch auch durch Angabe absoluter Koordinaten erstellt werden.

11\. Erstelle Bemaßungen für die verschiedenen Objekte.

:   11.1. Drücke **<img src=images/Draft_Dimension.svg style="width:16px"> [Bemaßung](Draft_Dimension/de.md)**.
:   11.2. Nimm den ersten Punkt. In diesem Tutorial wird der erste Punkt immer der Ursprung sein. {{Value|(0, 0, 0)}}.
:   11.3. In der <img src=images/Draft_Snap_Lock.svg style="width:Fang Werkzeugleiste](Draft_Snap/de.md) stelle sicher das **[16px"> <img src=images/Draft_Snap_Midpoint.svg style="width:Umschalten Fang](Draft_Snap_Lock/de.md)** aktiv ist, und ebenso nur **[16px"> [Mittelpunkt](Draft_Snap_Midpoint/de.md)**. Sowie du den Zeiger auf die Oberkante des Polygons bewegst, sollte das <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:24px;"> [Mittelpunkt](Draft_Snap_Midpoint/de.md) Symbol erscheinen; klicke, um diesen Punkt auszuwählen.
:   11.4. Bewege den Cursor nach rechts, um die Position der Abmessung anzugeben, und klicke dann, um die Endposition um {{Value|(100, 20, 0)}} festzulegen. Die Bemaßung zeigt automatisch den zwischen den beiden Punkten gemessenen Längenwert an.
:   11.5. Wähle das Bemaßungsobjekt in der [Baumansicht](tree_view/de.md), und im [Eigenschaftseditor](Property_editor/de.md), wechsle **Schriftgröße** auf {{Value|6 mm}}, setze **Ext Linien** auf {{Value|45 mm}}, und **Anzeige Einheit** auf `False`.

12\. Wiederhole den Vorgang für die beiden Bögen des geschlossenen Profils. Der erste Punkt der Messung ist immer noch der Ursprung, und der zweite Punkt verwendet den <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:24px;"> [Mittelpunkt](Draft_Snap_Midpoint/de.md) des Bogens.

13\. Wiederhole den Vorgang für den Kreis in der Mitte. Der erste Punkt der Messung ist immer noch der Ursprung. Um den zweiten Punkt auszuwählen, stelle sicher, dass **<img src=images/Draft_Snap_Lock.svg style="width:16px"> <img src=images/Draft_Snap_Angle.svg style="width:Umschalten Fang](Draft_Snap_Lock/de.md)** aktiv ist, und ebenso nur **[16px"> [Winkel](Draft_Snap_Angle/de.md)**. Sobald du den Zeiger an den oberen Rand des Kreises bewegst, sollte das <img alt="" src=images/Draft_Snap_Angle.svg  style="width:24px;"> [Winkel](Draft_Snap_Angle/de.md) Symbol erscheinen; klicke, um diesen Punkt auszuwählen. Bewege dann den Cursor nach rechts, und klicke, um die Bemaßung zu fixieren.

Denke daran, die **Schriftgröße** und andere Eigenschaften anzupassen, damit die Bemaßung korrekt angezeigt wird.

<img alt="" src=images/04_Dr01_Draft_Dimension.png  style="width:" height="400px;"> 
*Bemaßungen, die den vertikalen Abstand vom Ursprung bis zur Oberkante des Kreises, der Bögen und des Polygons messen.*

## Texte und Formzeichenketten 

14\. Textobjekte sind einfache planare Figuren, die in der [3D Ansicht](3D_view/de.md) erstellt werden, aber keine tatsächliche \"[Form](Shape/de.md)\" darunter haben. Das bedeutet, dass sie nicht in komplexen Operationen mit Formen wie Extrusionen oder booleschen Operationen verwendet werden können.

:   14.1. Drücke **<img src=images/Draft_Text.svg style="width:16px"> [Text](Draft_Text/de.md)**.
:   14.2. Wähle den Referenzpunkt in der <img src=images/Draft_Snap_Lock.svg style="width:3D Ansicht](3D_view/de.md). In der [Fang Werkzeugleiste](Draft_Snap/de.md) stelle sicher das **[16px"> <img src=images/Draft_Snap_Midpoint.svg style="width:Umschalten Fang](Draft_Snap_Lock/de.md)** aktiv ist, und ebenfalls nur **[16px"> [Mittelpunkt](Draft_Snap_Midpoint/de.md)**. Bewege den Mauszeiger auf die Oberkante des höchsten Bogens, so dass das <img alt="" src=images/Draft_Snap_Midpoint.svg  style="width:24px;"> [Mittelpunkt](Draft_Snap_Midpoint/de.md) Symbol erscheint; klicke um diesen Punkt auszuwählen.
:   14.3. Gib den gewünschten **Text** ein und drücke einmal **Enter**, um eine neue Zeile zu beginnen; füge bei Bedarf weitere Textzeilen hinzu.
:   14.4. Wenn du mit der Ausgabe fertig bist, drücke zweimal **Enter**.
:   14.5. Wähle das Textobjekt in der [Baumansicht](tree_view/de.md) aus, und ändere im [Eigenschaftseditor](Property_editor/de.md) **Schriftgröße** in {{Value|6 mm}} und **Ausrichtung** in {{Value|Center}}.

15\. FormZeichenkettenobjekte sind Formen aus primitiven Drähten, die den durch eine bestimmte Schriftart angezeigten Linien folgen. Das bedeutet, dass diese Objekte eine echte \"[Form](Shape/de.md)\" darunter haben und daher in komplexen Operationen wie Extrusionen und booleschen Operationen verwendet werden können.

:   15.1. Drücke **<img src=images/Draft_ShapeString.svg style="width:16px"> [FormZeichenkette](Draft_ShapeString/de.md)**.
:   15.2. Bewege den Zeiger an die gewünschte Stelle in der [3D Ansicht](3D_view/de.md) über dem regulären Polygon, und klicke einmal. Dadurch wird der Basispunkt für die FormZeichenkette festgelegt. Die Koordinaten können auch manuell eingegeben werden, zum Beispiel {{Value|(-20, 65, 0)}}.
:   15.3. Gib die gewünschte **Zeichenkette** ein und wähle die gewünschte **Höhe**.
:   15.4. Wenn es keine Standardschriftartdatei gibt, musst du auf die Ellipsen **...** klicken, um ein Dialogfeld zur Auswahl des Speicherorts der Schriftart im System zu öffnen.
:   15.5. Wenn eine gültige Schriftartdatei angegeben wurde, kannst du fortfahren, auf **OK** zu klicken oder **Enter** zu drücken.

<img alt="" src=images/05_Dr01_Draft_Text_ShapeString.png  style="width:" height="400px;"> 
*Text  und FormZeichenkettenobjekte hinzugefügt.*

Um Buchstaben zu extrudieren und auf Volumenkörper zu gravieren, siehe das [Entwurf Formzeichenketten Tutorium](Draft_ShapeString_tutorial/de.md).

## Erstellen technischer Zeichnungen 

So wie es jetzt ist, können die von uns erstellten Objekte gespeichert, in andere Formate wie [SVG](SVG/de.md) oder [DXF](DXF/de.md) exportiert oder gedruckt werden.

Wenn du möchtest, kannst du eine technische Zeichnung erstellen, um diese Objekte zusammen mit zusätzlichen Informationen wie einem Rahmen darzustellen.

Bevor irgendetwas getan wird, blende das Entwurfsgitter durch drücken **<img src=images/Draft_ToggleGrid.svg style="width:16px"> [Umschalten Gitter](Draft_ToggleGrid/de.md)** aus.

16\. 16. Wechsle zum <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw Arbeitsbereich](TechDraw_Workbench/de.md).

:   16.1. Erstelle eine Standardseite durch Drücken von **<img src=images/TechDraw_PageDefault.svg style="width:16px"> [TechDraw StandardSeite](TechDraw_PageDefault/de.md)**.
:   16.2. Wähle in der <img src=images/TechDraw_ActiveView.svg style="width:Baumansicht](tree_view/de.md) alle erstellten Objekte mit Ausnahme der Seite aus, und drücke dann **[16px"> [TechDraw ActiveView](TechDraw_ActiveView/de.md)**. Drücke **OK** mit den Standardoptionen; es kann einige Sekunden dauern, bis die Ansicht auf der Seite erstellt ist.
:   16.3. Wahl des Seitenobjekts in der [Baumansicht](tree_view/de.md) wird die Seite automatisch im Hauptfenster anzeigen. Mit gewählter Seite gehe zum [Eigenschaftseditor](Property_editor/de.md), und wechsle den **Maßstab** auf {{Value|0.75}}.
:   16.4. Erweitere das Seitenbobjekt in der [Baumansicht](tree_view/de.md) um das AktiveAnsichtsobjekt zu wählen. Mit dieser gewählten Ansicht, gehe zum [Eigenschaftseditor](Property_editor/de.md), und wechsle den **Maßstabstyp** auf {{Value|Seite}}.
:   16.5. Berechne das Modell neu unter Verwendung von **<img src=images/Std_Refresh.svg style="width:16px"> [Aktualisieren](Std_Refresh/de.md)** oder Drücken von **F5**.
:   16.6. Blende die Rahmen der Objekte durch drücken von **<img src=images/TechDraw_ToggleFrame.svg style="width:16px"> [TechDraw UmschaltenRahmen](TechDraw_ToggleFrame/de.md)** aus.

Erfahre mehr über den [TechDraw Arbeitsbereich](TechDraw_Workbench/de.md) durch Lesen des [TechDraw Grundlagen Tutorium](Basic_TechDraw_Tutorial/de.md).

<img alt="" src=images/06_Dr01_Draft_TechDraw_page.png  style="width:" height="400px;"> 
*TechDraw Seite mit einer Projektion der mit dem Entwurf Arbeitsbereich erstellten Formen.*

TechDraw funktioniert am besten mit Objekten, die eine [Part TopoForm](Part_TopoShape/de.md). Da einige Objekte aus Entwurf, wie [Entwurf Texte](Draft_Text/de.md) und [Entwurf Bemaßungen](Draft_Dimension/de.md), nicht über solche \"[Formen](Shape/de.md)\"verfügen, funktionieren einige Operationen von TechDraw nicht mit diesen Elementen.

Werkzeuge wie **<img src=images/TechDraw_ActiveView.svg style="width:16px"> <img src=images/TechDraw_DraftView.svg style="width:TechDraw AktiveAnsicht](TechDraw_ActiveView/de.md)**, **[16px"> <img src=images/TechDraw_ArchView.svg style="width:TechDraw EntwurfAnsicht](TechDraw_DraftView/de.md)**, und **[16px"> [TechDraw ArchitekturAnsicht](TechDraw_ArchView/de.md)** arbeiten, indem sie ein internes SVG Bild erhalten, das von internen Entwurfsfunktionen erzeugt wird; daher hat TechDraw keine große Kontrolle darüber, wie diese Ansichten angezeigt werden. Die weitere Integration von Entwurf und TechDraw ist noch in Arbeit.

## Schlussbemerkungen


<div class="mw-translate-fuzzy">

Der [Entwurf Arbeitsbereich](Draft_Module/de.md) ähnelt in vielerlei Hinsicht dem [Entwurf Arbeitsbereich](Sketcher_Workbench/de.md), da beide zur Erzeugung von 2D Formen gedacht sind. Der Hauptunterschied besteht in der Art und Weise, wie jeder Arbeitsbereich Koordinatensysteme handhabt und wie die Objekte positioniert werden. Im Entwurf werden die Objekte frei im globalen Koordinatensystem positioniert, wobei ihre Punkte normalerweise an einem Gitter oder an anderen Objekten gefangen werden. Im Skizzierer definiert ein \"[Skizzenobjekt](Sketch/de.md)\" ein lokales Koordinatensystem, das als Referenz für alle geometrischen Elemente innerhalb dieser Skizze dient. Darüber hinaus stützt sich die Skizze auf \"Beschränkungen\", um die endgültige Position deiner Punkte zu definieren.


</div>


<div class="mw-translate-fuzzy">

-   Der [Entwurf Arbeitsbereich](Draft_Module/de.md) ist für 2D Zeichnungen vorgesehen, die sich zum Zeichnen auf einem Gitter eignen. Der [Architektur Arbeitsbereich](Arch_Module/de.md) baut meist auf den im [Entwurf Arbeitsbereich](Draft_Module/de.md) definierten Werkzeugen auf.


</div>

-   Der [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md) ist für 2D Zeichnungen gedacht, die präzise Beziehungen zwischen ihren Punkten erfordern. Sie stützt sich nicht auf ein Gitter, sondern auf Positionierungsregeln (Beschränkungen), um zu bestimmen, wo die Punkte und Kanten platziert werden sollen. Der [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md) wird meistens zusammen mit der [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) für die Erstellung von Volumenkörpern [Körper](Body/de.md) verwendet.

-   Es ist möglich, ein Entwurfsobjekt in eine <img src=images/Draft_Draft2Sketch.svg style="width:Skizze](Sketch/de.md) umzuwandeln und umgekehrt, indem man das **[16px"> [Entwurf EntwurfZuSkizze](Draft_Draft2Sketch.md)** Werkzeug verwendet.


{{Tutorials navi

}}  
