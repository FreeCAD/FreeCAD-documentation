# Draft ShapeString tutorial/de
---
- TutorialInfo:/de
   Topic:Produktgestaltung
   Level:Anfänger
   Time:30 Minuten
   Author:r-frank und vocx
   FCVersion:0.17 und höher
   Files:[https://github.com/FreeCAD/Examples/blob/master/Draft_Shapestring_Tutorial_Examples/Draft_Shapestring_Tutorial_Text.FCStd?raw=true Draft_Shapestring_Text]
}}

## Einleitung

Dieses Tutorium wurde ursprünglich von Roland Frank (†2017, r-frank) geschrieben, und es wurde von vocx neu geschrieben und illustriert.

Dieses Tutorium beschreibt eine Methode zur Erstellung von 3D-Text und dessen Verwendung mit Volumenobjekten in der <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Arbeitsbereich](Part_Workbench/de.md). Wir werden diskutieren, wie man

-   umrandeten Text mit dem **![](images/)**-Werkzeug einfügen,
-   extrudieren zu einem 3D-Festkörper mit **[Part Extrudieren](File:Part_Extrude.svg   16px]] [[Part_Extrude/de.md)**,
-   positioniere es im 3D-Raum mit [Platzierung](placement/de.md), und **[Entwurf bewegen](File:Draft_Move.svg   16px]] [[Draft_Move/de.md)** (es verwendet eine Skizze als Hilfsgeometrie), und
-   graviere den Text durch Anwendung einer booleschen Operation **[Entwurf Schnitt](File:Part_Cut.svg   16px]] [[Part_Cut/de.md)**.

Um FormZeichenfolgen innerhalb der <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) zu verwenden, ist der Prozess im Wesentlichen derselbe wie beim Part Arbeitsbereich, aber die FormZeichenfolge wird innerhalb des [PartDesign Körper](PartDesign_Body/de.md) platziert, um ihn zu extrudieren. Weitere Informationen findest du am Ende dieses Tutoriums.

![](images/08_T04_Part_ShapesString_Extrude_final_cut.png ) 
*Endgültiges Modell des gravierten Textes.*

Der [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md) wird kurzzeitig zum Zeichnen einer Hilfslinie verwendet. Weitere Informationen zu den Werkzeugen dieses Arbeitsbereichs findet man in

-   [Grundlegendes Skizzierer Tutorium](Basic_Sketcher_Tutorial/de.md)
-   [Skizzierer Referenz](Sketcher_reference/de.md)

## Einrichtung

1\. Öffne FreeCAD, erstelle ein neues leeres Dokument mit {{MenuCommand/de   Datei → [<img src=images/Std_New.svg style="width:16px"> [Neu](Std_New/de.md)}}, und wechsle in den [Part Arbeitsbereich](Part_Workbench/de.md).

:   1.1. Drücke die **[Ansicht isometrisch](File:Std_ViewIsometric.svg   16px]] [[Std_ViewIsometric/de.md)** Schaltfläche oder drücke **0** auf dem Ziffernblock deiner Tastatur, um die Ansicht auf isometrisch zu ändern und die 3D Körper besser zu veranschaulichen.
:   1.2. Drücke die **[Ansicht alles einpassen](File:Std_ViewFitAll.svg   16px]] [[Std_ViewFitAll/de.md)** Schaltfläche wenn Du Objekte hinzufügst, um die [3D Ansicht](3D_view/de.md) so zu schwenken und zu zoomen, dass alle Elemente in der Ansicht zu sehen sind.
:   1.3. Halte **Strg** gedrückt, währen Du klickst, um mehrere Elemente auszuwählen. Wenn Du etwas falsch ausgewählt hast oder alles abwählen willst, klickst Du einfach auf eine leere Stelle in der [3D Ansicht](3D_view/de.md).

## Erstelle die Grundform 

2\. Füge einen Grundkörper Würfel ein, indem Du auf **![](images/)**_klickst.

:   2.1. Wähle {{incode   Würfel}} in der [Baumansicht](tree_view/de.md).
:   2.2. Ändere die Abmessungen im **Daten**reiter des [Eigenschafteneditors](property_editor/de.md).
:   2.3. Ändere **Breite** in {{incode   31 mm}}.

3\. Erstelle eine Fase.

:   3.1. Wähle die obere Kante ({{incode   Edge6}}) auf der Vorderseite des {{incode   Würfel}} in der [3D Ansicht](3D_view/de.md).
:   3.2. Drücke **![](images/)**.
:   3.3. Im **Kanten anfasen** [Aufgabenpaneel](task_panel/de.md) gehe zu **Auswahl**, wähle **Kanten wählen**. Als **Verrundungstyp** wähle {{incode   Konstante Länge}}, dann setze **Länge** auf {{incode   5 mm}}.
:   3.4. Drücke **OK**. Dies erzeugt ein {{incode   Fasen}} Objekt.
:   3.5. In der [Baumansicht](tree_view/de.md), wähle {{incode   Fase}}, im **Ansicht**s Reiter ändere den Wert **Linienbreite** auf {{incode   2.0}}.

![](images/01_T04_Part_Cube_base_long.png ) 
*Basisobjekt erzeugt aus einem Würfel und einer Fasenbearbeitung.*

## Einfügen der FormZeichenkette 

4\. Wechsle in die [Entwurf Arbeitsbereich](Draft_Workbench/de.md).

:   4.1. Stelle sicher, dass in der [Baumansicht](tree_view/de.md) nichts ausgewählt ist.
:   4.2. Lege die Arbeitsebene auf XY (oben) fest, durch klicken auf **[Wähle Ebene](File:Draft_SelectPlane.svg   16px]] [[Draft_SelectPlane/de.md)** und drücken von **[Oben (XY)](File:View-top.svg   16px]] [[Std_ViewTop/de.md)**.

5\. Füge den Text \"FreeCAD\" ein.

:   5.1. Drücke auf **[Formzeichenfolge](File:Draft_ShapeString.svg   16px]] [[Draft_ShapeString/de.md)**
:   5.2. Ändere **X** in {{incode   0 mm}}.
:   5.3. Ändere **Y** in {{incode   0 mm}}.
:   5.4. Ändere **Z** in {{incode   0 mm}}.
:   5.5. Oder drücke **Punkt zurücksetzen**.
:   5.6. Ändere **Zeichenfolge** in {{incode   FreeCAD}}; ändere **Höhe** in {{incode   5 mm}}; ändere **Nachverfolgung** in {{incode   0 mm}}.
:   5.7. Stelle sicher, dass **Schriftartdatei** auf eine gültige Schriftart zeigt, z.B. {{incode   /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf}}. Drücke die Auslassungspunkte **...**, um den Dialog des Betriebssystems zu öffnen und eine Schriftart zu finden.

    :   
        **Hinweis:**
        
        mehr Details zum Arbeiten mit Schriftarten findest du im [Draft FormZeichenfolge Hinweise](Draft_ShapeString#Notes/de.md)-Abschnitt
:   5.8. Drücke **OK**. Dies wird ein {{incode   FormZeichenfolge}} Objekt erzeugen.
:   5.9. Berechne das Dokument neu, indem du **[Aktualisieren](File:Std_Refresh.svg   16px]] [[Std_Refresh.md)** drückst.
:   5.10. Wähle in der [Baumansicht](tree_view/de.md) die Option {{incode   FormZeichenfolge}}, ändere im Reiter **Ansicht** den Wert von **Linienbreite** in {{incode   2.0}}.
:   5.11. Wähle in der [Baumansicht](tree_view/de.md) {{incode   Fase}}, in der **Ansicht** ändre im Reiter den Wert von **Visibility** in {{incode   false}} oder drücke **Space** auf der Tastatur. Dies blendet das Objekt aus, sodass Du die {{incode   Formzeichenfolge}} besser sehen kannst.
:   5.12. Um den FormZeichenfolge von oben zu sehen, ändere die Ansicht, durch drücken von **[Oben (XY)](File:View-top.svg   16px]] [[Std_ViewTop/de.md)**, oder **2** in der Tastatur.
:   5.13. Um die isometrische Ansicht wiederherzustellen, drücke **[Isoemetrische Ansicht](File:Std_ViewIsometric.svg   16px]] [[Std_ViewIsometric/de.md)**, oder **0** in der Tastatur.

![](images/02_T04_Part_ShapeString.png ) 
*Text erstellt als FormZeichenfolge, d.h. als eine Sammlung von Kanten in einer Ebene.*

## Erstellen des 3D Volumentextes 

6\. Wechsle wieder in die [Part Arbeitsbereich](Part_Workbench/de.md).

:   6.1. In der [Baumansicht](tree_view/de.md) wähle {{incode   ShapeString}} und drücke dann **[Extrudieren](File:Part_Extrude.svg   16px]] [[Part_Extrude/de.md)**.
:   6.2. Im **Extrudieren** [Aufgabenpaneel](task_panel/de.md) gehe zu **Richtung**, wähle **Entlang der Normalen**; in **Länge** setze **Entlang** auf {{incode   1 mm}}; hake auch die Option **Erzeuge Volumenkörper** an.
:   6.3. Drücke **OK**. Dies wird ein {{incode   Extrudieren}} Objekt erzeugen.
:   6.4. Wähle in der [Baumansicht](tree_view/de.md) die Option {{Incode   Extrudieren}}, ändere im Reiter **Ansicht** den Wert von **Linienbreite** in {{Incode   2.0}}.

![](images/03_T04_Part_ShapeString_Extrude.png ) 
*Text als FormZeichenfolge erstellt und durch Extrusion in einen Festkörper verwandelt.*

## Hilfsskizze zur Positionierung einfügen 

Nun zeichnen wir eine einfache Skizze, die als Hilfsgeometrie zur Positionierung der FormZeichenfolgen Extrusion verwendet wird.

7\. Wähle in der [Baumansicht](tree_view/de.md) die Option {{Incode   Extrudieren}} und drücke **Leertaste** auf der Tastatur, um sie unsichtbar zu machen.

8\. Wechsle in den [Skizzierer Arbeitsbereich](Sketcher_Workbench/de.md).

9\. Wähle in der [Baumansicht](tree_view/de.md) die Option {{Incode   Fase}} und drücke **Leertaste** auf der Tastatur, um sie sichtbar zu machen.

:   9.1. Wähle die durch die Fasenoperation ({{incode   Face3}}) erzeugte schräge Fläche aus.
:   9.2. Klicke auf **[NeueSkizze](File:Sketcher_NewSketch.svg   16px]] [[Sketcher_NewSketch/de.md)**. Wähle im Dialogfeld **Skizzenanhang** die Option {{incode   FlacheFläche}} und drücke **OK**.
:   9.3. Die Ansicht sollte sich automatisch so einstellen, dass die Kamera parallel zur gewählten Fläche ist.
:   9.4. Zeichne eine horizontale Linie in einer üblichen Position oben auf der Fläche. Die Länge ist nicht wichtig; wir sind nur an ihrer Position interessiert.
:   9.5. Beschränke den linken Endpunkt mit {{incode   2.5 mm}} auf einen Abstand von der lokalen X Achse und von der lokalen Y Achse, indem **[BeschränkeAbstandX](File:Sketcher_ConstrainDistanceX.svg   16px]] [[Sketcher_ConstrainDistanceX/de.md)** and **[BeschränkeAbstandY](File:Sketcher_ConstrainDistanceY.svg   16px]] [[Sketcher_ConstrainDistanceY/de.md)**.
:   9.6. Da die Skizze nur ein Hilfsobjekt ist, brauchen wir sie nicht vollständig zu begeschränken. Du kannst dies tun, wenn du möchtest, indem du einen festen Abstand, sagen wir, {{incode   20 mm}}, wieder mit **[BeschränkeAbstandX](File:Sketcher_ConstrainDistanceX.svg   16px]] [[Sketcher_ConstrainDistanceX/de.md)**.
:   9.7. Schließe die Skizze.

<img alt="" src=images/04_T04_Part_ShapeString_support_sketch.png  style="width:500px;"> 
*Linie mit dem Skizzierer erstellt, mit Beschränkungen.*

<img alt="" src=images/05_T04_Part_ShapeString_support_sketch_3D.png  style="width:500px;"> 
*Skizzen Linie erstellt auf der Oberseite der Volumenkörperfläche, zur Verwendung als Referenz für die Positionierung des extrudierten Textes.*

## Positionierung des Volumentextes im 3D Raum 

10\. Wähle in der [Baumansicht](tree_view/de.md) {{Incode   Extrudieren}} und drücke **Leertaste** auf der Tastatur, um sie sichtbar zu machen.

11\. Wähle in der [Baumansicht](tree_view/de.md) die Option {{Incode   Extrudieren}}, klicke im Reiter **Daten** des [Eigenschaften Editor](property_editor/de.md) auf den **Platzierung** Wert, so dass die Auslassungspunkte Schaltfläche **...** rechts erscheint.

:   11.1. Hake die Option **Inkrementelle Änderungen übernehmen** an.
:   11.2. Ändere den **Drehung** in {{incode   Rotationsachse mit Winkel}}; **Achse** in {{incode   Z}}, und **Winkel** in {{incode   90 Grad}}, dann klicke auf **Übernehmen**. Dies wendet eine Rotation um die Z Achse an und setzt das **Winkel** Feld auf Null zurück.
:   11.3. Ändere den **Drehung** in {{incode   Drehachse mit Winkel}}; **Achse** in {{incode   Y}}, und **Winkel** in {{incode   45 Grad}}, dann klicke auf **Übernehmen**. Dies wendet eine Drehung um die Y Achse an und setzt das Feld **Winkel** auf Null zurück.
:   11.4. Klicke auf **OK**, um den Dialog zu schließen.

12\. Wechsle wieder in die [Entwurf Arbeitsbereich](Draft_Workbench/de.md).

:   12.1. Wechsle zum *Drahtgitter* Zeichenstil mit **Ansicht → [16px](Std_DrawStyle/de___Zeichen_Stil]]_→_[[File:DrawStyleWireFrame.svg.md) Drahtgitter**, oder drücke **[Drahtgitter](File:DrawStyleWireFrame.svg   16px]] [[Std_DrawStyle/de.md)** Schaltfläche in der Ansichtswerkzeugleiste. Damit kannst du die Objekte hinter anderen Objekten sehen.
:   12.2. Stelle sicher, dass die Schaltfläche [Entwurf Fang](Draft_Snap/de.md) die Methode \"Am Endpunkt fangen\" aktiv ist . Dies kann über das Menü **Entwurf→ Fang → [Umschalten An/Aus](File:Draft_Snap_Lock.svg   16px]] [[Draft_Snap_Lock/de.md)**erfolgen, und dann ** → [Entwurf Endpunkt](File:Draft_Snap_Endpoint.svg   16px]] [[Draft_Snap_Endpoint/de.md)**, oder durch Drücken der **[UmschaltenFang](File:Draft_Snap_Lock.svg   16px]] [[Draft_Snap_Lock/de.md)** und **[Fang Endpunkt](File:Draft_Snap_Endpoint.svg   16px]] [[Draft_Snap_Endpoint.md)** Schaltflächen in der Fang Werkzeugleiste.

13\. Wähle in der [Baumansicht](tree_view/de.md) {{incode   Extrudieren}}.

:   13.1. Klicke auf **[Bewegen](File:Draft_Move.svg   16px]] [[Draft Move/de.md)**
:   13.2. Klicke in der [3D Ansicht](3D_view/de.md) auf den oberen linken Eckpunkt des {{incode   Extrudieren}} Objekts (1) und dann auf den äußersten linken Punkt in der mit dem Skizzierer gezeichneten Linie (2).





:   13.3. Wenn **[Fang Endpunkt](File:Draft_Snap_Endpoint.svg   16px]] [[Draft_Snap_Endpoint/de.md)** aktiv ist, sobald du den Zeiger in die Nähe eines Knotens bewegst, solltest du sehen, dass er sich genau an diesen anfügt.
:   
    **Hinweis:**Wenn du Probleme mit dem Einrasten an Knoten hast, stelle sicher, dass nur die **[Fang Endpunkt](File:Snap_Endpoint.svg   16px]] [[Draft_Snap_Endpoint/de.md)** Methode aktiviert ist. Wenn mehrere Fangmethoden gleichzeitig aktiv sind, macht es schwierig, das richtige Grundelement auszuwählen.
:   13.4. Der extrudierte Text sollte sich nun innerhalb des Körpers des {{incode   Verrundung}}s Objekts befinden.

![](images/06_T04_Part_ShapeString_move.svg ) 
*Die extrudierte FormZeichenfolge sollte auf die Position der skizzierten Linie verschoben werden, die auf der Fläche des Grundkörpers liegt.*

![](images/07_T04_Part_ShapesString_Extrude_in_place.png ) 
*Extrudierte FormZeichenfolge positioniert in der {{incode   Verrundung*.}}

## Erstellen von graviertem Text 

14\. Wechsle zurück in die [Part Arbeitsbereich](Part_Workbench/de.md).

:   14.1. Wechsle zu \"Original\" Zeichenstil {{MenuCommand/de   Ansicht → [Zeichenstil](Std_DrawStyle/de.md) → [<img src=images/DrawStyleAsIs.svg style="width:16px"> Original}}, oder drücke die **[So ist](File:DrawStyleAsIs.svg   16px]] [[Std_DrawStyle.md)** Schaltfläche in der Ansichtswerkzeugleiste. Dies zeigt alle Objekte mit der normalen Schattierung und Farbe an.
:   14.2. Wähle in der [Baumansicht](tree_view/de.md) die Option {{incode   Skizze}} und drücke **Leertaste** auf der Tastatur, um sie unsichtbar zu machen.

15\. Wähle in der [Baumansicht](tree_view/de.md) zuerst {{incode   Fase}} und dann {{Incode   Extrudieren}}.

:   15.1. Drücke dann **[Schneiden](File:Part_Cut.svg   16px]] [[Part_Cut/de.md)**. Dies wird ein {{incode   Schnitt}} Objekt erzeugen. Dies ist das endgültige Objekt.
:   
    **Hinweis:**die Reihenfolge, in der du die Objekte auswählst, ist wichtig für den Schneidevorgang. Das Basisobjekt wird zuerst ausgewählt, und das subtrahierende Objekt kommt am Ende.
:   15.2. Wähle in der [Baumansicht](tree_view/de.md) die Option {{Incode   Schnitt}}, ändere im Reiter {{MenuCommand/de   Ansicht}} den Wert von {{MenuCommand/de   Zeilenbreite}} auf {{Incode   2.0}}.

![](images/08_T04_Part_ShapesString_Extrude_final_cut.png ) 
*Endgültiges Modell eines verrundeten Würfels, mit geschnitztem Text, der aus einer ShapeString, Extrude und boolschen Schnittoperationen erzeugt wurde.*

## Gravieren von 3D Text mit dem PartDesign Arbeitsbereich 

Ein ähnlicher Ablauf wie oben beschrieben kann mit der [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) durchgeführt werden.

1.  Erstelle die **[Draft FormZeichenfolge](File:Draft_ShapeString.svg   16px]] [[Draft_ShapeString/de.md)** zuerst
2.  Erstelle einen **[PartDesign Körper](File:PartDesign_Body_Tree.svg   16px]] [[PartDesign_Body/de.md)**, aktiviere ihn und füge einen Basis-Volumenkörper hinzu, indem du Primitive hinzufügst, oder verwende eine Skizze und extrudiere sie mit **[PartDesign Polster](File:PartDesign_Pad.svg   16px]] [[PartDesign_Pad/de.md)**.
3.  Bewege das {{incode   ShapeString}}-Objekt in den aktiven Körper.
4.  Hänge das {{incode   ShapeString}}-Objekt an eine der Flächen des Volumenkörpers oder an ein **[PartDesign Bezugsebene erstellen](File:PartDesign_Plane.svg   16px]] [[PartDesign_Plane/de.md)**, unter Verwendung **[/de|Part AnhangBearbeiten](File:Part_EditAttachment.svg   16px]] [[Part_EditAttachment.md)**.
5.  Erstelle jetzt ein **[PartDesign Polster](File:PartDesign_Pad.svg   16px]] [[PartDesign_Pad/de.md)** oder eine **[PartDesign Tasche](File:PartDesign_Pocket.svg   16px]] [[PartDesign_Pocket/de.md)** aus dem {{incode   ShapeString}}, um ein entsprechendes additives bzw. subtraktives [PartDesign Formelement](PartDesign_Feature/de.md) aus dem Grundkörper zu erzeugen.

Siehe den Forumsbeitrag, [Wie man FormZeichenfolgen in PartDesign verwendet](https://forum.freecadweb.org/viewtopic.php?f=3&t=36623).

## Anmerkungen

-   Um gekrümmten Text zu erstellen, kann man das Makro <img alt="" src=images/FCCircularTextButtom.png  style="width:32px;"> [Makro FCCircularTextverwenden](Macro_FCCircularText/de.md).
-   Um Text aus einer SVG Datei zu importieren, schaue dir das Tutorium [Importieren von Text und Geometrie aus Inkscape](Import_text_and_geometry_from_Inkscape/de.md) an.


  {{PartDesign Tools navi}} {{Sketcher Tools navi}} {{Userdocnavi
---



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Part](Category_Part.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > [Draft](Draft_Workbench.md) > Draft ShapeString tutorial/de
