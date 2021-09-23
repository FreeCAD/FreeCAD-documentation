# Draft ShapeString tutorial/de
 {{TutorialInfo/de
|Topic=Produktgestaltung
|Level=Anfänger
|Time=30 Minuten
|Author=r-frank und vocx
|FCVersion=0.17 und höher
|Files=[https://github.com/FreeCAD/Examples/blob/master/Draft_Shapestring_Tutorial_Examples/Draft_Shapestring_Tutorial_Text.FCStd?raw=true Draft_Shapestring_Text]
}}

## Einleitung

Dieses Tutorium wurde ursprünglich von Roland Frank (†2017, r-frank) geschrieben, und es wurde von vocx neu geschrieben und illustriert.

Dieses Tutorium beschreibt eine Methode zur Erstellung von 3D-Text und dessen Verwendung mit Volumenobjekten in der <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Arbeitsbereich](Part_Workbench/de.md). Wir werden diskutieren, wie man

-   umrandeten Text mit dem **<img src="images/Draft_ShapeString.svg" width=16px> [Entwurf FormZeichenfolge](Draft_ShapeString/de.md)**-Werkzeug einfügen,
-   extrudieren zu einem 3D-Festkörper mit **<img src=images/Part_Extrude.svg style="width:16px"> [Part Extrudieren](Part_Extrude/de.md)**,
-   positioniere es im 3D-Raum mit <img src=images/Draft_Move.svg style="width:Platzierung](placement/de.md), und **[16px"> [Entwurf bewegen](Draft_Move/de.md)** (es verwendet eine Skizze als Hilfsgeometrie), und
-   graviere den Text durch Anwendung einer booleschen Operation **<img src=images/Part_Cut.svg style="width:16px"> [Entwurf Schnitt](Part_Cut/de.md)**.

Um FormZeichenfolgen innerhalb der <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) zu verwenden, ist der Prozess im Wesentlichen derselbe wie beim Part Arbeitsbereich, aber die FormZeichenfolge wird innerhalb des [PartDesign Körper](PartDesign_Body/de.md) platziert, um ihn zu extrudieren. Weitere Informationen findest du am Ende dieses Tutoriums.

![](images/08_T04_Part_ShapesString_Extrude_final_cut.png ) *Endgültiges Modell des gravierten Textes.*

Der [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md) wird kurzzeitig zum Zeichnen einer Hilfslinie verwendet. Weitere Informationen zu den Werkzeugen dieses Arbeitsbereichs findet man in

-   [Grundlegendes Skizzierer Tutorium](Basic_Sketcher_Tutorial/de.md)
-   [Skizzierer Referenz](Sketcher_reference/de.md)

## Einrichtung

1\. Öffne FreeCAD, erstelle ein neues leeres Dokument mit {{MenuCommand/de|Datei → <img src=images/Std_New.svg style="width:16px"> [Neu](Std_New/de.md)}}, und wechsle in den [Part Arbeitsbereich](Part_Workbench/de.md).

:   1.1. Drücke die **<img src=images/Std_ViewIsometric.svg style="width:16px"> [Ansicht isometrisch](Std_ViewIsometric/de.md)** Schaltfläche oder drücke **0** auf dem Ziffernblock deiner Tastatur, um die Ansicht auf isometrisch zu ändern und die 3D Körper besser zu veranschaulichen.
:   1.2. Drücke die **<img src=images/Std_ViewFitAll.svg style="width:16px"> [Ansicht alles einpassen](Std_ViewFitAll/de.md)** Schaltfläche wenn Du Objekte hinzufügst, um die [3D Ansicht](3D_View/de.md) so zu schwenken und zu zoomen, dass alle Elemente in der Ansicht zu sehen sind.
:   1.3. Halte **Strg** gedrückt, währen Du klickst, um mehrere Elemente auszuwählen. Wenn Du etwas falsch ausgewählt hast oder alles abwählen willst, klickst Du einfach auf eine leere Stelle in der [3D Ansicht](3D_view/de.md).

## Erstelle die Grundform 

2\. Füge einen Grundkörper Würfel ein, indem Du auf **<img src="images/Part_Box.svg" width=16px> [Quader](Part_Box/de.md)** klickst.

:   2.1. Wähle `Würfel` in der [Baumansicht](tree_view/de.md).
:   2.2. Ändere die Abmessungen im **Daten**reiter des [Eigenschafteneditors](property_editor/de.md).
:   2.3. Ändere **Breite** in `31 mm`.

3\. Erstelle eine Fase.

:   3.1. Wähle die obere Kante (`Edge6`) auf der Vorderseite des `Würfel` in der [3D Ansicht](3D_view/de.md).
:   3.2. Drücke **<img src="images/Part_Chamfer.svg" width=16px> [Fase](Part_Chamfer/de.md)**.
:   3.3. Im **Kanten anfasen** [Aufgabenpaneel](task_panel/de.md) gehe zu **Auswahl**, wähle **Kanten wählen**. Als **Verrundungstyp** wähle `Konstante Länge`, dann setze **Länge** auf `5 mm`.
:   3.4. Drücke **OK**. Dies erzeugt ein `Fasen` Objekt.
:   3.5. In der [Baumansicht](tree_view/de.md), wähle `Fase`, im **Ansicht**s Reiter ändere den Wert **Linienbreite** auf `2.0`.

![](images/01_T04_Part_Cube_base_long.png ) *Basisobjekt erzeugt aus einem Würfel und einer Fasenbearbeitung.*

## Einfügen der FormZeichenkette 

4\. Wechsle in die [Entwurf Arbeitsbereich](Draft_Workbench/de.md).

:   4.1. Stelle sicher, dass in der [Baumansicht](tree_view/de.md) nichts ausgewählt ist.
:   4.2. Lege die Arbeitsebene auf XY (oben) fest, durch klicken auf **<img src=images/Draft_SelectPlane.svg style="width:16px"> <img src=images/View-top.svg style="width:Wähle Ebene](Draft_SelectPlane/de.md)** und drücken von **[16px"> [Oben (XY)](Std_ViewTop/de.md)**.

5\. Füge den Text \"FreeCAD\" ein.

:   5.1. Drücke auf **<img src=images/Draft_ShapeString.svg style="width:16px"> [Formzeichenfolge](Draft_ShapeString/de.md)**
:   5.2. Ändere **X** in `0 mm`.
:   5.3. Ändere **Y** in `0 mm`.
:   5.4. Ändere **Z** in `0 mm`.
:   5.5. Oder drücke **Punkt zurücksetzen**.
:   5.6. Ändere **Zeichenfolge** in `FreeCAD`; ändere **Höhe** in `5 mm`; ändere **Nachverfolgung** in `0 mm`.
:   5.7. Stelle sicher, dass **Schriftartdatei** auf eine gültige Schriftart zeigt, z.B. `/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf`. Drücke die Auslassungspunkte **...**, um den Dialog des Betriebssystems zu öffnen und eine Schriftart zu finden.

    :   
        **Hinweis:**
        
        mehr Details zum Arbeiten mit Schriftarten findest du im [Draft FormZeichenfolge Hinweise](Draft_ShapeString#Notes/de.md)-Abschnitt
:   5.8. Drücke **OK**. Dies wird ein `FormZeichenfolge` Objekt erzeugen.
:   5.9. Berechne das Dokument neu, indem du **<img src=images/Std_Refresh.svg style="width:16px"> [Aktualisieren](Std_Refresh.md)** drückst.
:   5.10. Wähle in der [Baumansicht](tree_view/de.md) die Option `FormZeichenfolge`, ändere im Reiter **Ansicht** den Wert von **Linienbreite** in `2.0`.
:   5.11. Wähle in der [Baumansicht](tree_view/de.md) `Fase`, in der **Ansicht** ändre im Reiter den Wert von **Visibility** in `false` oder drücke **Space** auf der Tastatur. Dies blendet das Objekt aus, sodass Du die `Formzeichenfolge` besser sehen kannst.
:   5.12. Um den FormZeichenfolge von oben zu sehen, ändere die Ansicht, durch drücken von **<img src=images/View-top.svg style="width:16px"> [Oben (XY)](Std_ViewTop/de.md)**, oder **2** in der Tastatur.
:   5.13. Um die isometrische Ansicht wiederherzustellen, drücke **<img src=images/Std_ViewIsometric.svg style="width:16px"> [Isoemetrische Ansicht](Std_ViewIsometric/de.md)**, oder **0** in der Tastatur.

![](images/02_T04_Part_ShapeString.png ) *Text erstellt als FormZeichenfolge, d.h. als eine Sammlung von Kanten in einer Ebene.*

## Erstellen des 3D Volumentextes 

6\. Wechsle wieder in die [Part Arbeitsbereich](Part_Workbench/de.md).

:   6.1. In der <img src=images/Part_Extrude.svg style="width:Baumansicht](tree_view/de.md) wähle `ShapeString` und drücke dann **[16px"> [Extrudieren](Part_Extrude/de.md)**.
:   6.2. Im **Extrudieren** [Aufgabenpaneel](task_panel/de.md) gehe zu **Richtung**, wähle **Entlang der Normalen**; in **Länge** setze **Entlang** auf `1 mm`; hake auch die Option **Erzeuge Volumenkörper** an.
:   6.3. Drücke **OK**. Dies wird ein `Extrudieren` Objekt erzeugen.
:   6.4. Wähle in der [Baumansicht](tree_view/de.md) die Option {{Incode|Extrudieren}}, ändere im Reiter **Ansicht** den Wert von **Linienbreite** in {{Incode|2.0}}.

![](images/03_T04_Part_ShapeString_Extrude.png ) *Text als FormZeichenfolge erstellt und durch Extrusion in einen Festkörper verwandelt.*

## Hilfsskizze zur Positionierung einfügen 

Nun zeichnen wir eine einfache Skizze, die als Hilfsgeometrie zur Positionierung der FormZeichenfolgen Extrusion verwendet wird.

7\. Wähle in der [Baumansicht](tree_view/de.md) die Option {{Incode|Extrudieren}} und drücke **Leertaste** auf der Tastatur, um sie unsichtbar zu machen.

8\. Wechsle in den [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md).

9\. Wähle in der [Baumansicht](tree_view/de.md) die Option {{Incode|Fase}} und drücke **Leertaste** auf der Tastatur, um sie sichtbar zu machen.

:   9.1. Wähle die durch die Fasenoperation (`Face3`) erzeugte schräge Fläche aus.
:   9.2. Klicke auf **<img src=images/Sketcher_NewSketch.svg style="width:16px"> [NeueSkizze](Sketcher_NewSketch/de.md)**. Wähle im Dialogfeld **Skizzenanhang** die Option `FlacheFläche` und drücke **OK**.
:   9.3. Die Ansicht sollte sich automatisch so einstellen, dass die Kamera parallel zur gewählten Fläche ist.
:   9.4. Zeichne eine horizontale Linie in einer üblichen Position oben auf der Fläche. Die Länge ist nicht wichtig; wir sind nur an ihrer Position interessiert.
:   9.5. Beschränke den linken Endpunkt mit `2.5 mm` auf einen Abstand von der lokalen X Achse und von der lokalen Y Achse, indem **<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> <img src=images/Sketcher_ConstrainDistanceY.svg style="width:BeschränkeAbstandX](Sketcher_ConstrainDistanceX/de.md)** and **[16px"> [BeschränkeAbstandY](Sketcher_ConstrainDistanceY/de.md)**.
:   9.6. Da die Skizze nur ein Hilfsobjekt ist, brauchen wir sie nicht vollständig zu begeschränken. Du kannst dies tun, wenn du möchtest, indem du einen festen Abstand, sagen wir, `20 mm`, wieder mit **<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [BeschränkeAbstandX](Sketcher_ConstrainDistanceX/de.md)**.
:   9.7. Schließe die Skizze.

<img alt="" src=images/04_T04_Part_ShapeString_support_sketch.png  style="width:500px;"> 
*Linie mit dem Skizzierer erstellt, mit Beschränkungen.*

<img alt="" src=images/05_T04_Part_ShapeString_support_sketch_3D.png  style="width:500px;"> 
*Skizzen Linie erstellt auf der Oberseite der Volumenkörperfläche, zur Verwendung als Referenz für die Positionierung des extrudierten Textes.*

## Positionierung des Volumentextes im 3D Raum 

10\. Wähle in der [Baumansicht](tree_view/de.md) {{Incode|Extrudieren}} und drücke **Leertaste** auf der Tastatur, um sie sichtbar zu machen.

11\. Wähle in der [Baumansicht](tree_view/de.md) die Option {{Incode|Extrudieren}}, klicke im Reiter **Daten** des [Eigenschaften Editor](property_editor/de.md) auf den **Platzierung** Wert, so dass die Auslassungspunkte Schaltfläche **...** rechts erscheint.

:   11.1. Hake die Option **Inkrementelle Änderungen übernehmen** an.
:   11.2. Ändere den **Drehung** in `Rotationsachse mit Winkel`; **Achse** in `Z`, und **Winkel** in `90 Grad`, dann klicke auf **Übernehmen**. Dies wendet eine Rotation um die Z Achse an und setzt das **Winkel** Feld auf Null zurück.
:   11.3. Ändere den **Drehung** in `Drehachse mit Winkel`; **Achse** in `Y`, und **Winkel** in `45 Grad`, dann klicke auf **Übernehmen**. Dies wendet eine Drehung um die Y Achse an und setzt das Feld **Winkel** auf Null zurück.
:   11.4. Klicke auf **OK**, um den Dialog zu schließen.

12\. Wechsle wieder in die [Entwurf Arbeitsbereich](Draft_Workbench/de.md).

:   12.1. Wechsle zum *Drahtgitter* Zeichenstil mit **Ansicht → <img src=images/DrawStyleWireFrame.svg style="width:Zeichen Stil](Std_DrawStyle/de.md) → [16px"> Drahtgitter**, oder drücke **<img src=images/DrawStyleWireFrame.svg style="width:16px"> [Drahtgitter](Std_DrawStyle/de.md)** Schaltfläche in der Ansichtswerkzeugleiste. Damit kannst du die Objekte hinter anderen Objekten sehen.
:   12.2. Stelle sicher, dass die Schaltfläche <img src=images/Draft_ToggleSnap.svg style="width:Entwurf Fang](Draft_Snap/de.md) die Methode \"Am Endpunkt fangen\" aktiv ist . Dies kann über das Menü **Entwurf→ Fang → [16px"> <img src=images/Snap_Endpoint.svg style="width:Umschalten An/Aus](Draft_ToggleSnap/de.md)**erfolgen, und dann ** → [16px"> <img src=images/Draft_ToggleSnap.svg style="width:Entwurf Endpunkt](Draft_Endpoint/de.md)**, oder durch Drücken der **[16px"> <img src=images/Snap_Endpoint.svg style="width:UmschaltenFang](Draft_ToggleSnap/de.md)** und **[16px"> [Fang Endpunkt](Draft_Endpoint.md)** Schaltflächen in der Fang Werkzeugleiste.

13\. Wähle in der [Baumansicht](tree_view/de.md) `Extrudieren`.

:   13.1. Klicke auf **<img src=images/Draft_Move.svg style="width:16px"> [Bewegen](Draft_Move/de.md)**
:   13.2. Klicke in der [3D Ansicht](3D_view/de.md) auf den oberen linken Eckpunkt des `Extrudieren` Objekts (1) und dann auf den äußersten linken Punkt in der mit dem Skizzierer gezeichneten Linie (2).





:   13.3. Wenn **<img src=images/Draft_Snap_Endpoint.svg style="width:16px"> [Fang Endpunkt](Draft_Snap_Endpoint/de.md)** aktiv ist, sobald du den Zeiger in die Nähe eines Knotens bewegst, solltest du sehen, dass er sich genau an diesen anfügt.
:   
    **Hinweis:**Wenn du Probleme mit dem Einrasten an Knoten hast, stelle sicher, dass nur die **<img src=images/Snap_Endpoint.svg style="width:16px"> [Fang Endpunkt](Draft_Snap_Endpoint/de.md)** Methode aktiviert ist. Wenn mehrere Fangmethoden gleichzeitig aktiv sind, macht es schwierig, das richtige Grundelement auszuwählen.
:   13.4. Der extrudierte Text sollte sich nun innerhalb des Körpers des `Verrundung`s Objekts befinden.

![](images/06_T04_Part_ShapeString_move.svg ) *Die extrudierte FormZeichenfolge sollte auf die Position der skizzierten Linie verschoben werden, die auf der Fläche des Grundkörpers liegt.*

![](images/07_T04_Part_ShapesString_Extrude_in_place.png ) *Extrudierte FormZeichenfolge positioniert in der `Verrundung*.`

## Erstellen von graviertem Text 

14\. Wechsle zurück in die [Part Arbeitsbereich](Part_Workbench/de.md).

:   14.1. Wechsle zu \"Original\" Zeichenstil {{MenuCommand/de|Ansicht → <img src=images/DrawStyleAsIs.svg style="width:Zeichenstil](Std_DrawStyle/de.md) → [16px"> Original}}, oder drücke die **<img src=images/DrawStyleAsIs.svg style="width:16px"> [So ist](Std_DrawStyle.md)** Schaltfläche in der Ansichtswerkzeugleiste. Dies zeigt alle Objekte mit der normalen Schattierung und Farbe an.
:   14.2. Wähle in der [Baumansicht](tree_view/de.md) die Option `Skizze` und drücke **Leertaste** auf der Tastatur, um sie unsichtbar zu machen.

15\. Wähle in der [Baumansicht](tree_view/de.md) zuerst `Fase` und dann {{Incode|Extrudieren}}.

:   15.1. Drücke dann **<img src=images/Part_Cut.svg style="width:16px"> [Schneiden](Part_Cut/de.md)**. Dies wird ein `Schnitt` Objekt erzeugen. Dies ist das endgültige Objekt.
:   
    **Hinweis:**die Reihenfolge, in der du die Objekte auswählst, ist wichtig für den Schneidevorgang. Das Basisobjekt wird zuerst ausgewählt, und das subtrahierende Objekt kommt am Ende.
:   15.2. Wähle in der [Baumansicht](tree_view/de.md) die Option {{Incode|Schnitt}}, ändere im Reiter {{MenuCommand/de|Ansicht}} den Wert von {{MenuCommand/de|Zeilenbreite}} auf {{Incode|2.0}}.

![](images/08_T04_Part_ShapesString_Extrude_final_cut.png ) *Endgültiges Modell eines verrundeten Würfels, mit geschnitztem Text, der aus einer ShapeString, Extrude und boolschen Schnittoperationen erzeugt wurde.*

## Gravieren von 3D Text mit dem PartDesign Arbeitsbereich 

Ein ähnlicher Ablauf wie oben beschrieben kann mit der [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) durchgeführt werden.


<div class="mw-translate-fuzzy">

1.  Erstelle die **<img src=images/Draft_ShapeString.svg style="width:16px"> [Entwurf FormZeichenfolge](Draft_ShapeString/de.md)** zuerst
2.  Erstelle einen **<img src=images/PartDesign_Body_Tree.svg style="width:16px"> <img src=images/PartDesign_Pad.svg style="width:PartDesign Körper](PartDesign_Body/de.md)**, aktiviere ihn und füge einen Basis-Volumenkörper hinzu, indem du Primitive hinzufügst, oder verwende eine Skizze und extrudiere sie mit **[16px"> [PartDesign Polster](PartDesign_Pad/de.md)**.
3.  Bewege das `FormZeichenfolge` Objekt in den aktiven Körper.
4.  Hänge das `FormZeichenfolge` Objekt an eine der Flächen des Volumenkörpers oder an ein **<img src=images/PartDesign_Plane.svg style="width:16px"> <img src=images/Part_Attachment.svg style="width:PartDesign Ebene](PartDesign_Plane/de.md)**, unter Verwendung **[16px"> [/de|Part Bindung](Part_Attachment.md)**.
5.  Erstelle jetzt ein **<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Polster](PartDesign_Pad/de.md)** oder ein **[16px](Datei:PartDesign_Pocket.svg.md) [PartDesign Tasche](PartDesign_Pocket/de.md)** aus der `Formzeichenfolge`, um eine additive bzw. subtraktive [Grundelement](PartDesign_Feature/de.md) des Grundkörpers zu erzeugen.


</div>

Siehe den Forumsbeitrag, [Wie man FormZeichenfolgen in PartDesign verwendet](https://forum.freecadweb.org/viewtopic.php?f=3&t=36623).

## Anmerkungen

-   Um gekrümmten Text zu erstellen, kannst Du das Makro <img alt="" src=images/FCCircularTextButtom.png  style="width:32px;"> verwenden. [Kreisförmiger Text](Macro_Circular_Text/de.md).
-   Um Text aus einer SVG Datei zu importieren, schaue dir das Tutorium [Importieren von Text und Geometrie von Inkscape](Import_text_and_geometry_from_Inkscape/de.md) an.


{{Tutorials navi

}}  {{PartDesign Tools navi}} {{Sketcher Tools navi}} 
