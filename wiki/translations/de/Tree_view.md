# Tree view/de
{{TOCright}}



## Einführung

Die [Baumansicht](Tree_view/de.md) erscheint im **Modell** Reiter der [Kombiansicht](Combo_view/de.md), einem der wichtigsten Paneele der [Oberfläche](Interface/de.md); sie zeigt alle benutzerdefinierten Objekte, die Teil eines FreeCAD Dokuments sind. Die Baumansicht ist eine Darstellung der [Dokumentstruktur](document_structure/de.md) und zeigt an, welche Informationen auf der Festplatte gespeichert sind.

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

Da die Baumansicht Objekte auflistet, die in der [3D-Ansicht](3D_view/de.md) sichtbar sein können, sind viele der Aktionen identisch mit denen, die aus der [3D-Ansicht](3D_view/de.md) ausgeführt werden können.

Wenn die Anwendung startet, der Standardarbeitsbereich [Start](Start_Workbench/de.md) aktiv ist, und kein Dokument erstellt wurde, zeigt ein Rechtsklick auf die [Baumansicht](Tree_view/de.md) ein Untermenü mit vier Befehlen:

-    **Expression Aktionen**:

    -   [Ausgewähltes kopieren](Std_Expressions/de.md),
    -   [Aktives Dokument kopieren](Std_Expressions/de.md),
    -   [Alle Dokumente kopieren](Std_Expressions/de.md),
    -   [Einfügen](Std_Paste.md).

Diese ermöglichen das Arbeiten mit verschiedenen Dokumenten, sind aber deaktiviert, wenn kein Dokument vorhanden ist.

Sobald ein neues Dokument erstellt wurde, wird folgendes aktiv:

-    **Expression Aktionen**:

    -   [Aktives Dokument kopieren](Std_Expressions/de.md),
    -   [Alle Dokumente kopieren](Std_Expressions/de.md).

Zusätzlich sind [Verweis](Std_LinkMake/de.md) Aktionen verfügbar.

-    **Verknüpfungsvorgänge**: [Verweis herstellen](Std_LinkMake/de.md).

    -   
        **Verweisgruppe herstellen**
        
        : [Einfache Gruppe](Std_LinkMakeGroup/de.md), [Gruppe mit Verweisen](Std_LinkMakeGroup/de.md), [Gruppe mit Umwandlungsverweisen](Std_LinkMakeGroup/de.md).



### Auswählen des Dokuments 

Wenn man das aktive Dokument auswählt und mit der rechten Maustaste klickt, erscheinen zusätzlich zu **Expression actions** und **Link actions** die folgenden Befehle:

-    **Versteckte Elemente anzeigen**: wenn aktiv, zeigt die Baumansicht versteckte Elemente an.

-    **Search**: zeigt ein Eingabefeld für die Suche nach Objekten innerhalb des ausgewählten Dokuments.

-    **Close document**: schließt das ausgewählte Dokument.

-    **Skip recomputes**: wenn aktiv, werden die Objekte des Dokuments nicht automatisch [Neuberechnet](Std_Refresh/de.md).

    -   
        **Allow partial recomputes**
        
        : wenn aktiv, erlaubt das Dokument [Neuberechnen](Std_Refresh/de.md) nur für einige Objekte.

-    **Markieren zum Neuberechnen**: markiert alle Objekte des Dokuments als berührt und bereit für [Neuberechnen](Std_Refresh/de.md).

-    **[Create group](Std_Group/de.md)**: Erzeugt eine [Gruppe](Std_Group/de.md) im ausgewählten Dokument.



### Objekte auswählen 


<div class="mw-translate-fuzzy">

Sobald Objekte zum Dokument hinzugefügt wurden, zeigt ein Rechtsklick auf sie zusätzliche Befehle an. Diese sind abhängig von der Anzahl der ausgewählten Objekte, der Art der Objekte und auch von dem aktiven Arbeitsbereich. In den meisten Fällen und mit den meisten Arbeitsbereichen (außer dem Arbeitsbereich [Start](Start_Workbench/de.md)) stehen folgende Befehle zur Verfügung:

-    **[Darstellung...](Std_SetAppearance/de.md)**: Öffnet einen Dialogfenster, um die visuellen Eigenschaften des gesamten Objekts zu ändern.

-    **[Zufällige Farbe](Std_RandomColor/de.md)**: Weist dem Objekt eine zufällige Farbe zu.

-    **[Ausschneiden](Std_Cut/de.md)**: Deaktiviert.

-    **[Kopieren](Std_Copy/de.md)**: Kopiert ein Objekt in den Zwischenspeicher.

-    **[Einfügen](Std_Paste/de.md)**: Setzt das kopierte Objekt in das Dokument ein; die Kopie wird am Ende der Baumansicht hinzugefügt.

-    **[Löschen](Std_Delete/de.md)**: Entfernt das Objekt aus dem Dokument.

-    **Element ausblenden**: Wenn aktiviert, wird das ausgewählte Objekt ausgeblendet.

-    **Abhängige Objekte zur Auswahl hinzufügen**: Fügt alle abhängigen Objekte zur Auswahl hinzu. So können alle Abhängigkeiten angezeigt und z.B. alle abhängigen Objekte auf einmal gelöscht werden. Diese Auswahl steht nur zur Verfügung, wenn eines der ausgewählten Objekte Verknüpfungen besitzt {{Version/de|0.20}}

-    **Markieren, um neu zu berechnen**: Kennzeichnet die ausgewählten Objekte als markiert und fertig zum [Neuberechnen](Std_Refresh/de.md).

-    **Objekt neu berechnen**: Berechnet die ausgewählten Objekte neu.

-    **Umbenennen**: Startet die Bearbeitung des Labels eines Objekts, nicht des Namens, der schreibgeschützt ist. Diese Auswahl steht nur dann zur Verfügung, wenn nur ein einziges Objekt ausgewählt wurde.


</div>

Ein Beispiel für eine Erweiterung des Kontextmenüs zeigt ein Rechtsklick auf ein [Part Würfel](Part_Box/de.md)-Objekt; bei aktiviertem Arbeitsbereich [Part](Part_Workbench/de.md) stehen folgende zusätzliche Befehle zur Verfügung:

-    **[Würfel bearbeiten](Std_Edit/de.md)**: Aktiviert den Bearbeitungsmodus des Würfels.

-    **[Transformieren](Std_TransformManip/de.md)**: Startet das Transformations-Widget, um das Objekt zu verschieben oder zu drehen.

-    **[Anhang-Editor](Part_EditAttachment/de.md)**: Öffnet ein Dialogfenster, um das Objekt einem oder mehreren anderen Objekten als Anhang zuzuordnen.

-    **[Farbe festlegen](Part_FaceColors/de.md)**: Legt die Farbe der ausgewählten Flächen eines Objekts fest.

-    **[Ein/Ausblenden](Std_ToggleVisibility/de.md)**: Schaltet die Sichtbarkeit eines Objekts in der [3D-Ansicht](3D_view/de.md) ein/aus.

-    **[Auswahl einblenden](Std_ShowSelection/de.md)**: Macht die ausgewählten Objekte sichtbar.

-    **[Auswahl ausblenden](Std_HideSelection/de.md)**: Macht die ausgewählten Objekte unsichtbar.

-    **[Selektierbarkeit an/aus](Std_ToggleSelectability/de.md)**: Schaltet die Auswählbarkeit de Objekts in der [3D-Ansicht](3D_view/de.md) ein/aus.

-    **[Alle Instanzen auswählen](Std_TreeSelectAllInstances/de.md)**: Wählt alle Instanzen dieses Objekts in der Baumansicht aus.

-    **[An Python-Konsole senden](Std_SendToPythonConsole/de.md)**: Erstellt eine Variable in der [Python-Konsole](Python_console/de.md), die auf dieses Objekt verweist.



### Tastaturbefehle

Folgende Tastaturbefehle stehen zur Verfügung, wenn der Fokus auf der Baumansicht liegt:

-    **Ctrl**\+**F**: Öffnet ein Suchfeld am unteren Rand der Baumansicht, das ermöglicht Objekte durch Angabe ihres Namens oder ihres Labels zu suchen und zu erreichen.

-   Aktionen zum Aus- und Einklappen mit Kombinationen aus **Alt**+**Pfeil**-Tasten: {{Version/de|0.20}}
    -   
        **Alt**
        
        \+**Left**: Klappt ausgewählte Elemente ein.

    -   
        **Alt**
        
        \+**Right**: Klappt ausgewählte Elemente aus.

    -   
        **Alt**
        
        \+**Up**: Klappt ausgewählte Elemente aus mit eingeklappten Unterelementen in der nächsten Ebene (Tiefer verknüpfte Unterelemente bleiben unverändert).

    -   
        **Alt**
        
        \+**Down**: Klappt ausgewählte Elemente aus mit ebenfalls ausgeklappten Unterelementen in der nächsten Ebene (Tiefer verknüpfte Unterelemente bleiben unverändert).



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

Dies wird nur für [Skizzen](Sketch/de.md) verwendet und zeigt an, dass die Skizze nicht vollständig bestimmt ist. Innerhalb des [Sketchers](Sketcher_Workbench/de.md) wird die Anzahl der verbleibenden Freiheitsgrade in den Meldungen des Lösers angezeigt.



### ![](images/FreeCAD_Tree_view_error.png ) Weißes Ausrufezeichen auf rotem Hintergrund 

Dies zeigt an, dass das Objekt einen Fehler hat, der behoben werden muss. Nach der Neuberechnung des gesamten Dokuments wird eine QuickInfo angezeigt, die den Fehler beschreibt, wenn Sie mit der Maus über das Objekt in der Baumansicht fahren. Hinweis: Alle anderen Objekte, die von einem Objekt in einem solchen Fehlerzustand abhängen, werden nicht korrekt neu berechnet, so dass sie möglicherweise noch einen alten Zustand aufweisen.

### ![](images/FreeCAD_Tree_view_hidden.png ) Eye symbol 

This indicates that the object will be hidden in the Tree view because its **Hide item** context menu option is checked. Check and then uncheck the **Show hidden items** context menu option of the document, or reopen the document, to update the Tree view.


{{Interface navi

}} {{Std Base navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Tree view/de
