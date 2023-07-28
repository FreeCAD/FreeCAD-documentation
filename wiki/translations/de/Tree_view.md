# Tree view/de
{{TOCright}}



## Einleitung

Die [Baumansicht](Tree_view/de.md) befindet sich auf der Registerkarte **Modell** in der [Combo-Ansicht](Combo_view/de.md), einem der wichtigsten Bereiche der [Oberfläche](Interface/de.md); sie zeigt alle benutzerdefinierten Objekte, die Teil eines FreeCAD-Dokuments sind. Die Baumansicht ist eine Darstellung der [Dokumentstruktur](document_structure/de.md) und zeigt an, welche Informationen auf die Festplatte gespeichert werden.

Diese Objekte müssen nicht unbedingt geometrische Formen sein, die in der [3D-Ansicht](3D_view/de.md) sichtbar sind, sondern können auch unterstützende Datenobjekte sein, die mit irgendeinem der [Arbeitsbereiche](workbenches/de.md) erstellt wurden.

![](images/FreeCAD_Tree_view.png )



*Die Baumansicht mit verschiedenen Elementen im Dokument.*



## Arbeiten mit der Baumansicht 

Immer wenn ein neues Objekt erstellt wird, wird es standardmäßig am Ende der Liste in der Baumansicht hinzugefügt. Die Baumansicht erlaubt die Verwaltung der Objekte, um sie übersichtlich zu halten; sie erlaubt das Erstellen von [Gruppen](Std_Group/de.md), das Verschieben von Objekten in Gruppen, das Verschieben von Gruppen in andere Gruppen, das Umbenennen von Objekten, das Kopieren von Objekten, das Löschen von Objekten und andere Operationen im Kontextmenü (Rechtsklick), die vom aktuell ausgewählten Objekt und vom aktuell aktiven Arbeitsbereich abhängen.

Viele Vorgänge erzeugen Objekte, die von einem zuvor existierenden Objekt abhängig sind. In diesem Fall zeigt die Baumansicht diese Beziehung, indem sie das ältere Objekt innerhalb des neuen Objekts aufnimmt. Das Aus- und Einklappen der Objekte in der Baumansicht zeigt die parametrische Historie dieses Objekts. Objekte, die sich (eingerückt) unter anderen befinden, sind älter, während Objekte, die sich nicht eingerückt darunter (außerhalb) befinden, neuer sind und von den älteren Objekten abgeleitet werden. Modifikationen an den älteren Objekten setzen sich über die parametrischen Operationen bis zu den neuesten fort und erzeugen ein neues Ergebnis.

<img alt="" src=images/FreeCAD_Tree_view_parametric_history_1.png  style="width:" height="304px;"> <img alt="" src=images/FreeCAD_Tree_view_parametric_history_2.png  style="width:" height="304px;">

<img alt="" src=images/FreeCAD_Tree_view_parametric_history_3.png  style="width:" height="304px;">



*Das oberste Objekt wird durch parametrische Operationen an Objekten erzeugt, die ihrerseits durch frühere Operationen erzeugt wurden. Wenn man den Baum um viele Ebenen erweitert, erhält man die ursprünglichen Elemente, die zur Erzeugung der Teilkörper verwendet wurden.*



### Bezeichnungen & Eigenschaften 

In der Spalte Bezeichnungen & Eigenschaften werden die Symbole und die Bezeichnungen (Labels) der Objekte angezeigt.

Ein Objekt in dieser Spalte auswählen und **F2** (unter Windows und Linux) oder **Enter** (unter macOS) drücken erlaubt die {{PropertyData/de|Label}} vor Ort ohne Umweg über die Aktionen des Kontextmenüs oder den [Eigenschafteneditor](Property_editor.md) zu bearbeiten.



### Beschreibung

Die Spalte Beschreibung zeigt weitere Informationen über Objekte an, wenn vorhanden.

Diese Informationen sind in der {{PropertyData/de|Label2}} des Objekts gespeichert und können vor Ort bearbeitet werden, indem das Objekt in dieser Spalte ausgewählt und **F2** (unter Windows und Linux) oder **Enter** (unter macOS) gedrückt wird oder mit Hilfe des [Eigenschafteneditors](Property_editor.md).



## Maßnahmen

Da die Baumansicht Objekte auflistet, die in der [3D-Ansicht](3D_view/de.md) sichtbar sein können, sind viele der Aktionen identisch mit denen, die in der [3D-Ansicht](3D_view/de.md) ausgeführt werden können. Die Aktionen können aus einem **Kontextmenü** heraus gestartet werden, das über einen Rechtsklick auf entweder auf den Hintergrund oder auf das Objekt erreicht werden kann.



### Start der Anwendung 

Wenn die Anwendung startet, der Standardarbeitsbereich [Start](Start_Workbench/de.md) aktiv ist, und kein Dokument erstellt wurde, besitzt das Kontextmenü der [Baumansicht](Tree_view/de.md) nur einem Eintrag:

-    **Expression Aktionen**. Wird der Mauszeiger darauf gezogen, öffnet sich ein Untermenü mit den vier Befehlen:

-   [Ausgewähltes kopieren](Std_Expressions/de.md),

-   [Aktives Dokument kopieren](Std_Expressions/de.md),

-   [Alle Dokumente kopieren](Std_Expressions/de.md),

-   [Einfügen](Std_Paste/de.md).

Diese ermöglichen das Arbeiten mit verschiedenen Dokumenten, sind aber deaktiviert, wenn kein Dokument vorhanden ist.



### Ein neues Dokument 

Sobald ein neues Dokument erstellt wurde, wird durch einen Rechtsklick auf den Hintergrund das Kontextmenü mit jetzt zwei Einträgen geöffnet:

-    **Expression Aktionen**, wie oben, aber mit diesen beiden aktivierten Einträgen:

    -   [Aktives Dokument kopieren](Std_Expressions/de.md),
    -   [Alle Dokumente kopieren](Std_Expressions/de.md).

-    **Link actions**\- ein Untermenü mit zwei Einträgen:

    -   
        **Make Link group**
        
        \- ein weiteres Untermenü, das drei Befehle enthält:

        -   [Simple group](Std_LinkMakeGroup/de.md)
        -   [Group with links](Std_LinkMakeGroup/de.md)
        -   [Group with transform links](Std_LinkMakeGroup/de.md)

    -   [VerknüpfungErstellen](Std_LinkMake/de.md)



### Auswählen des Dokuments 

Wenn man das Dokument auswählt und mit der rechten Maustaste klickt, enthält das Kontextmenü zusätzlich zu **Ausdruck-Aktionen** und **Verknüpfungen...** die folgenden Befehle:

-    **In der Baumansicht ausgeblendete Elemente anzeigen**: wenn aktiv, zeigt die Baumansicht versteckte Elemente an.

-    **Suche**: zeigt ein Eingabefeld für die Suche nach Objekten innerhalb des ausgewählten Dokuments.

-    **Dokument schließen**: schließt das ausgewählte Dokument.

-    **Neuberechnungen überspringen**: wenn aktiv, werden die Objekte des Dokuments nicht automatisch [neuberechnet](Std_Refresh/de.md).

    -   
        **Teilweise Neuberechnungen erlauben**
        
        : wenn aktiv, erlaubt das Dokument das [Neuberechnen](Std_Refresh/de.md) für nur wenige Objekte. Steht nur zur Verfügung, wenn **Neuberechnungen überspringen** aktiviert ist.

-    **Markieren zum Neuberechnen**: markiert alle Objekte des Dokuments als berührt und bereit für ein [Neuberechnen](Std_Refresh/de.md).

-    **[Gruppe erstellen](Std_Group/de.md)**: Erzeugt eine [Gruppe](Std_Group/de.md) im ausgewählten Dokument.



### Objekte auswählen 

Sobald Objekte zum Dokument hinzugefügt wurden, zeigt ein Rechtsklick auf sie zusätzliche Befehle an. Diese sind abhängig von der Anzahl der ausgewählten Objekte, der Art der Objekte und auch von dem aktiven Arbeitsbereich. In den meisten Fällen und mit den meisten Arbeitsbereichen (außer dem Arbeitsbereich [Start](Start_Workbench/de.md)) stehen folgende Befehle zur Verfügung:

-    **[Darstellung...](Std_SetAppearance/de.md)**: Öffnet einen Dialogfenster, um die visuellen Eigenschaften des gesamten Objekts zu ändern.

-    **[Zufällige Farbe](Std_RandomColor/de.md)**: Weist dem Objekt eine zufällige Farbe zu.

-    **[Ausschneiden](Std_Cut/de.md)**: Deaktiviert.

-    **[Kopieren](Std_Copy/de.md)**: Kopiert ein Objekt in den Zwischenspeicher.

-    **[Einfügen](Std_Paste/de.md)**: Setzt das kopierte Objekt in das Dokument ein; die Kopie wird am Ende der Baumansicht hinzugefügt.

-    **[Löschen](Std_Delete/de.md)**: Entfernt das Objekt aus dem Dokument.

-    **[Sichtbarkeit in der Baumansicht umschalten](#Auge-Symbol.md)**: Schaltet die Sichtbarkeit eines Objekt in der Baumansicht um.

-    **Markieren, um neu zu berechnen**: Kennzeichnet die ausgewählten Objekte als markiert und fertig zum [Neuberechnen](Std_Refresh/de.md).

-    **Objekt neu berechnen**: Berechnet die ausgewählten Objekte neu.

-    **Umbenennen**: Startet die Bearbeitung der Benennung (Label) eines Objekts, nicht des Namens, der schreibgeschützt ist. Diese Auswahl steht nur dann zur Verfügung, wenn nur ein einziges Objekt ausgewählt wurde.

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

Ein oder mehrere kleinere Überlagerungssymbole können über dem Standardsymbol eines Objekts in der Strukturansicht angezeigt werden. Die verfügbaren Überlagerungssymbole und ihre Bedeutung sind nachfolgend aufgeführt.



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



### ![](images/FreeCAD_Tree_view_hidden.png ) Auge-Symbol 

Dies zeigt an, dass das Objekt in der Baumansicht ausgeblendet ist, wenn die Kontextmenü-Option **In der Baumansicht ausgeblendete Elemente anzeigen** deaktiviert ist.


{{Interface navi

}} {{Std Base navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Tree view/de
