# Tree view/de
{{TOCright}}

## Einführung

Die [Baumansicht](Tree_view/de.md) erscheint im {{MenuCommand/de|Modell}} Reiter der [Kombiansicht](Combo_view/de.md), einem der wichtigsten Paneele der [Oberfläche](Interface/de.md); sie zeigt alle benutzerdefinierten Objekte, die Teil eines FreeCAD Dokuments sind. Die Baumansicht ist eine Darstellung der [Dokumentstruktur](document_structure/de.md) und zeigt an, welche Informationen auf der Festplatte gespeichert sind.

Diese Objekte müssen nicht unbedingt geometrische Formen sein, die in der [3D Ansicht](3D_view/de.md) sichtbar sind, sondern können auch unterstützende Datenobjekte sein, die mit einer der [Arbeitsbereiche](workbenches/de.md) erstellt wurden.

![](images/FreeCAD_Tree_view.png )


*Die Baumansicht mit verschiedenen Elementen im Dokument.*

## Arbeiten mit der Baumansicht 

Immer wenn ein neues Objekt erstellt wird, wird es standardmäßig am Ende der Liste in der Baumansicht hinzugefügt. Die Baumansicht erlaubt die Verwaltung der Objekte, um sie übersichtlich zu halten; sie erlaubt das Erstellen von [Gruppen](Std_Group/de.md), das Verschieben von Objekten innerhalb von Gruppen, das Verschieben von Gruppen innerhalb anderer Gruppen, das Umbenennen von Objekten, das Kopieren von Objekten, das Löschen von Objekten und andere Operationen im Kontextmenü (Rechtsklick), die vom aktuell ausgewählten Objekt und des aktuell aktiven Arbeitsbereichs abhängen.

Viele Vorgänge erzeugen Objekte, die von einem zuvor existierenden Objekt abhängig sind. In diesem Fall zeigt die Baumansicht diese Beziehung, indem sie das ältere Objekt innerhalb des neuen Objekts aufnimmt. Das Auf- und Zuklappen der Objekte in der Baumansicht zeigt die parametrische Historie dieses Objekts. Objekte, die tiefer in anderen sind, sind älter, während Objekte, die sich außerhalb befinden, neuer sind und von den älteren Objekten abgeleitet werden. Durch die Modifikation der inneren Objekte breiten sich die parametrischen Operationen bis nach oben aus und erzeugen ein neues Ergebnis.

<img alt="" src=images/FreeCAD_Tree_view_parametric_history_1.png  style="width:" height="304px;"> <img alt="" src=images/FreeCAD_Tree_view_parametric_history_2.png  style="width:" height="304px;">

<img alt="" src=images/FreeCAD_Tree_view_parametric_history_3.png  style="width:" height="304px;">


*Das oberste Objekt wird durch parametrische Operationen an Objekten erzeugt, die ihrerseits durch frühere Operationen erzeugt wurden. Wenn man den Baum um viele Ebenen erweitert, erhält man die ursprünglichen Elemente, die zur Erzeugung der Teilkörper verwendet wurden.*

## Maßnahmen


**Hinweis:**

Ausdrücke und Verknüpfungsvorgänge wurden in Version 0.19 hinzugefügt.

Da die Baumansicht Objekte auflistet, die in der [3D Ansicht](3D_view/de.md) sichtbar sein können, sind viele der Aktionen identisch mit denen, die aus der [3D Ansicht](3D_view/de.md) ausgeführt werden können.

Beim Start der Anwendung ist die Standardeinstellung [Start Arbeitsbereich](Start_Workbench/de.md) aktiv, und kein Dokument wurde erstellt, wenn Du mit der rechten Maustaste auf die Schaltfläche [Baumansicht](Tree_view/de.md) klickst, wird nur ein Befehl angezeigt:

-    **Expression Aktionen**: [Ausgewähltes kopieren](Std_Expressions.md), [Aktives Dokument kopieren](Std_Expressions.md), [Alle Dokumente kopieren](Std_Expressions.md), Einfügen. Diese ermöglichen das Arbeiten mit verschiedenen Dokumenten, sind aber deaktiviert, wenn kein Dokument vorhanden ist.

Sobald ein neues Dokument erstellt wurde, wird folgendes aktiv:

-    **Expression actions**: [Aktives Dokument kopieren](Std_Expressions/de.md), [Alle Dokumente kopieren](Std_Expressions/de.md).

Zusätzlich sind [Verweis](Std_LinkMake/de.md) Aktionen verfügbar.

-    **Verknüpfungsvorgänge**: [Verweis herstellen](Std_LinkMake/de.md).

    -   
        **Verweisgruppe herstellen**
        
        : [Einfache Gruppe](Std_LinkMakeGroup/de.md), [Gruppe mit Verweisen](Std_LinkMakeGroup/de.md), [Gruppe mit Umwandlungsverweisen](Std_LinkMakeGroup/de.md).

### Auswählen des Dokuments 

Wenn du das aktive Dokument auswählst und mit der rechten Maustaste klickst, musst du zusätzlich zum {{MenuCommand/de|Expression actions}} und {{MenuCommand/de|Link actions}}, werden die folgenden Befehle angezeigt:

-    {{MenuCommand/de|Versteckte Elemente anzeigen}}: wenn aktiv, zeigt die Baumansicht versteckte Elemente an.

-    {{MenuCommand/de|Search}}: zeigt ein Eingabefeld für die Suche nach Objekten innerhalb des ausgewählten Dokuments.

-    {{MenuCommand/de|Close document}}: schließt das ausgewählte Dokument, indem es die Anwendung aufruft. `closeDocument()` Methode.

-    {{MenuCommand/de|Skip recomputes}}: wenn aktiv, werden die Objekte des Dokuments nicht automatisch [Neuberechnen](recompute/de.md).

    -   
        {{MenuCommand/de|Allow partial recomputes}}
        
        : wenn aktiv, erlaubt das Dokument [Neuberechnen](recompute/de.md) nur für einige Objekte.

-    {{MenuCommand/de|Markieren zum Neuberechnen}}: markiert alle Objekte des Dokuments als berührt und bereit für [Neuberechnen](recompute/de.md).

-    {{MenuCommand/de|[Create group](Std_Group/de.md)}}: Erzeugt eine [Gruppe](Std_Group/de.md) im ausgewählten Dokument, indem du die Dokumenten `addObject()` Methode.

### Objekte auswählen 

Sobald Objekte zum Dokument hinzugefügt wurden, zeigt ein Rechtsklick auf einen leeren Teil der Baumansicht zusätzlich zu den vorherigen Aktionen weitere Befehle an, die vom Objekttyp und dem aktiven Arbeitsbereich abhängen.

Zum Beispiel mit angewähltem [Arbeitsbereich Entwurf](Draft_Workbench/de.md), wähle zuerst ein Objekt und klicke dann mit der rechten Maustaste auf eine leere Stelle in der Baumansicht:

-    {{MenuCommand/de|[Toggle visibility](Std_ToggleVisibility/de.md)}}: macht das Objekt in der [3D Ansicht](3D_view/de.md) sichtbar oder unsichtbar.

-    {{MenuCommand/de|[Show selection](Std_ShowSelection/de.md)}}: macht die ausgewählten Objekte sichtbar.

-    {{MenuCommand/de|[Hide selection](Std_HideSelection/de.md)}}: macht die ausgewählten Objekte unsichtbar.

-    {{MenuCommand/de|[Toggle selectability](Std_ToggleSelectability/de.md)}}: macht das Objekt in der[3D Ansicht](3D_view/de.md) nicht mehr auswählbar; verwende diesen Befehl erneut, um die Wirkung aufzuheben. Es setzt das Attribut `Selectable` des Objekts auf `True` oder `False`. Ändere die Eigenschaft, indem Du {{PropertyView/de|Selectable}} im [Property Editor](Property_Editor/de.md) umschaltest.

-    {{MenuCommand/de|[Select all instances](Std_TreeSelectAllInstances/de.md)}}: wählt alle Instanzen dieses Objekts in der Baumansicht aus.

-    {{MenuCommand/de|[Appearance](Std_SetAppearance/de.md)}}: startet den Dialog zum Ändern der Farbe und Größe von Linien und Knoten sowie der Farbe von Flächen.

-    {{MenuCommand/de|[Zufällige Farbe](Std_RandomColor/de.md)}}: Weist dem Objekt eine Zufallsfarbe zu. Es setzt das Attribut `ShapeColor` des Objekts auf ein Tupel `(r,g,b)` mit drei zufälligen Gleitkommazahlen zwischen 0 und 1 und ändert die Eigenschaft, indem es {{PropertyView/de|Form Farbe}} im [Eigenschaftseditor](Property_Editor/de.md) ändert.

-    {{MenuCommand/de|[Schnitt](Std_Cut/de.md)}}: deaktiviert, wenn der Rechtsklick nicht auf das Objekt erfolgt.

-    {{MenuCommand/de|[Kopie](Std_Copy/de.md)}}: kopiert ein Objekt in den Speicher.

-    **[Einfügen](Std_Paste/de.md)**: fügt das kopierte Objekt in das Dokument ein; die Kopie wird am Ende der Baumansicht hinzugefügt.

-    {{MenuCommand/de|[Löschen](Std_Delete/de.md)}}: entfernt das Objekt aus dem Dokument und aus der Baumansicht, indem die Methode `Objekt entfernen()` des Dokuments aufgerufen wird.

-    {{MenuCommand/de|Hilfsmittel}}: Zusätzliche inhaltliche Befehle, die von der [Arbeitsbereich Entwurf](Draft_Workbench/de.md) zur Verfügung gestellt werden.

Wenn ein Objekt ausgewählt wird, z.B. eine [ Entwurfslinie](Draft_Line/de.md), und ein Rechtsklick auf das gleiche Objekt ausgeführt wird, können zusätzliche Befehle verfügbar sein:

-    **Transformation**: startet das Transformations Widget, um das Objekt zu verschieben oder zu drehen.

-    **Set colors**: setzt die Farben des Objekts.

-    **Draht Abflachen**: **(Draft)** Spezifischer Befehl für eine [Entwurfslinie](Draft_Line/de.md).

-    **Eintrag ausblenden**: Wenn aktiv, wird das ausgewählte Objekt als ausgeblendet gesetzt.

-    {{MenuCommand/de|Markieren zum Neuberechnen}}: markiert das ausgewählte Objekt als berührt und bereit für [Neuberechnung](Std_Refresh/de.md).

-    **Neuberechnung**: Berechnet das ausgewählte Objekt neu.

-    **Umbenennen**:beginnt mit der Bearbeitung des Namens des ausgewählten Objekts. Dies ermöglicht es, das Attribut `Label` zu ändern, nicht aber das Attribut `Name`, da letzteres schreibgeschützt ist.

## Überlagerungssymbole

Ein oder mehrere kleinere Überlagerungssymbole können über dem Standardsymbol eines Objekts in der Strukturansicht angezeigt werden. Die verfügbaren Überlagerungssymbole und ihre Bedeutung sind unten aufgeführt. {{Version/de|0.19}}

### ![](images/FreeCAD_Tree_view_recompute.png ) Weißes Häkchen auf blauem Hintergrund 

Dies zeigt an, dass das Objekt [neuberechnet](Std_Refresh/de.md) werden muss, aufgrund von Änderungen am Modell oder weil der Benutzer das Objekt im Kontextmenü der Baumansicht zur Neuberechnung markiert hat. In den meisten Fällen werden Neuberechnungen automatisch ausgelöst, aber manchmal werden sie aus Leistungsgründen verzögert.

### ![](images/FreeCAD_Tree_view_tip.png ) Weißer Pfeil auf grünem Hintergrund 

Dies bezeichnet die sogenannte [Spitze](PartDesign_Body/de#Spitze.md) eines Körpers. Er ist in der Regel das letzte Merkmal in einem [PartDesign Körper](PartDesign_Body/de.md) und repräsentiert den gesamten Körper nach außen, z. B. wenn der Körper exportiert oder in [Part booleschen](Part_Boolean/de.md) Operationen verwendet wird. Die Spitze kann vom Benutzer geändert werden.

### ![](images/FreeCAD_Tree_view_unattached.png ) Lila Kettenglied auf weißem Hintergrund 

Dies wird typischerweise für [Skizzen](Sketch/de.md), geometrische Primitive, wie Kasten, Zylinder usw. und [Bezugsgeometrie](Datum/de.md) angezeigt. Es zeigt an, dass das Objekt an nichts angehängt ist. Es hat keinen Anfügeversatz und bezieht seine Position und Ausrichtung ausschließlich von seiner Eigenschaft [Platzierung](Placement/de.md).

Es gibt ein [Grundlegendes Anfügungs Tutorium](Basic_Attachment_Tutorial/de.md), das erklärt, wie man mit solchen Objekten umgeht.

### ![](images/FreeCAD_Tree_view_notfullyconstrained.png ) Gelbes X 

Dies wird nur für [Skizzen](Sketch/de.md) verwendet und zeigt an, dass die Skizze nicht vollständig beschränkt ist. Innerhalb des [Skizzierer](Sketcher_Workbench/de.md) wird die Anzahl der verbleibenden Freiheitsgrade in den Löser Meldungen angezeigt.

### ![](images/FreeCAD_Tree_view_error.png ) Weißes Ausrufezeichen auf rotem Hintergrund 

Dies zeigt an, dass das Objekt einen Fehler hat, der behoben werden muss. Nach der Neuberechnung des gesamten Dokuments wird eine Werkzeugspitze angezeigt, der den Fehler beschreibt, wenn Sie mit der Maus über das Objekt in der Strukturansicht fahren. Hinweis: Alle anderen Objekte, die von einem Objekt in einem solchen Fehlerzustand abhängen, werden nicht korrekt neu berechnet, so dass sie möglicherweise noch einen alten Zustand aufweisen.


{{Interface navi

}} {{Std Base navi}}

---
[documentation index](../README.md) > Tree view/de
