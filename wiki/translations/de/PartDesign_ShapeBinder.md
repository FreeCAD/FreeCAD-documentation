---
 GuiCommand:
   Name: PartDesign ShapeBinder
   Name/de: PartDesign FormBinder
   MenuLocation: Part Design , Formbinder erstellen
   Workbenches: PartDesign_Workbench/de
   Version: 0.17
   SeeAlso: PartDesign_SubShapeBinder/de,PartDesign Clone/de
---

# PartDesign ShapeBinder/de



## Beschreibung

Das Werkzeug **PartDesign Formbinder** erstellt einen Formbinder (ShapeBinder-Objekt), der Geometrien eines einzigen übergeordneten Objekts referenziert. Ein Formbinder wird in einem [PartDesign Körper](PartDesign_Body/de.md) (Body) verwendet, um auf Geometrie außerhalb des Körpers zuzugreifen. Externe Geometrie direkt in einem Körper zu verwenden, ist nicht erlaubt und wird zu einem \"out of scope\"-Fehler führen.

Ein Formbinder ermittelt die relative Positionierung der referenzierten Geometrie, was im Zusammenhang mit der Erstellung von [Baugruppen](Assembly/de.md) nützlich ist, wenn seine {{PropertyData/de|Trace Support}} auf {{True}} gesetzt wird. Siehe das [Beispiel](#Beispiel.md) unten, um zu verstehen, wie dies funktioniert.

Die referenzierte Geometrie kann entweder ein einzelnes Objekt sein (z.B. ein [Part-Würfel](Part_Box/de.md), ein [PartDesign-Körper](PartDesign_Body.md) oder eine [Skizze](PartDesign_NewSketch.md) oder ein [Formelement](PartDesign_Feature/de.md) innerhalb eines Körpers) oder ein oder mehrere Unterelemente (Flächen, Kanten oder Knotenpunkte), die zu demselben übergeordneten Objekt gehören. Welche Geometrie verwendet wird, hängt von der geplanten Verwendung des Formbinders ab. Für eine boolesche Operation muss ein Festkörper ausgewählt werden. Für eine Extrusion kann eine Fläche oder eine Skizze verwendet werden. Und für eine externe Geometrie in einer Skizze oder um eine Skizze zu befestigen kann jede Kombination von Unterelementen geeignet sein. Die referenzierte Geometrie kann auch zu dem Körper gehören, der den Formbinder enthält.

<img alt="" src=images/Shapebinder_flow.png  style="width:600px;"> 
*Aus zwei ausgewähleten Flächen wird ein Formbinder in einem noch leeren Körper erstellt. Die Geometrie des Formbinders kann dann als externe Geometrie in einer Skizze innerhalb dieses Körpers verwendet werden.*



## Anwendung

1.  Den [Körper aktivieren](PartDesign_Body/de#Aktiver_Status.md), in den der Formbinder eingebunden werden soll.
2.  Wahlweise ein einzelnes Objekt auswählen oder ein oder mehrere Unterelemente die zu demselben übergeordneten Objekte gehören. Unterelemente können nur in der [3D-Ansicht](3D_view/de.md) ausgewählt werden.
3.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/PartDesign_ShapeBinder.svg" width=16px> [PartDesign Formbinder](PartDesign_ShapeBinder/de.md)** drücken.
    -   Den Menüeintrag **Part Design → <img src="images/PartDesign_ShapeBinder.svg" width=16px> Formbinder erstellen** auswählen.
4.  Der Aufgabenbereich **Bezugsform-Parameter** wird geöffnet.
5.  Wahlweise ein Objekt auswählen; dies ist nicht erforderlich, wenn Unterelemente ausgwählt werden sollen:
    1.  Die Schaltfläche **Objekt** drücken.
    2.  Ein objekt in der [Baumansicht](Tree_view/de.md) oder der [3D-Ansicht](3D_view/de.md) auswählen.
    3.  Alle zuvor Ausgewählten Unterelemente werden entfernt.
    4.  Wird hier ein Körper ausgewählt, können keine Unterelemente ausgewählt werden, da sie zu einem anderen Objekt gehören, nämlich dem Formelement an der [Spitze](PartDesign_Body/de#Spitze.md) (Arbeitsposition) des Körpers.
6.  Wahlweise Unterelemente auswählen:
    1.  Die Schaltfläche **Geometrie hinzufügen** drücken.
    2.  Ein Unterelement in der [3D-Ansicht](3D_view/de.md) auswählen.
    3.  Die Schaltfläche **Geometrie hinzufügen** muss für jedes Unterelement gedrückt werden, das hinzugefügt werden soll.
    4.  Nur Unterelemente, die zu demselben übergeordneten Objekt gehören, können ausgewählt werden. Wenn erforderlich, die Schaltfläche **Objekt** drücken, um ein anderes übergeordnetes Objekt auszuwählen.
7.  Wahlweise Unterelemente entfernen:
    1.  Die Schaltfläche **Geometrie entfernen** drücken.
    2.  Ein Unterelement in der [3D-Ansicht](3D_view/de.md) auswählen.
    3.  Die Schaltfläche **Geometrie entfernen** muss für jedes Unterelement gedrückt werden, das entfernt werden soll.
8.  Die Schaltfläche **OK** drücken.



## Optionen

Die Bearbeitung eines Formbinders wird mit Doppelklick auf sein Symbol in der [Baumansicht](Tree_view/de.md) gestartet oder mit einem Rechtsklick darauf und anschließender Auswahl von **Formbinder bearbeiten** im Kontextmenü der [Baumansicht](Tree_view/de.md).



## Hinweise

-   Ein Formbinder kann aus dem Körper, in dem er eingebunden ist, herausgezogen und auf dem <img alt="" src=images/Document.svg  style="width:16px;"> Dokumentknoten in der [Baumansicht](Tree_view/de.md) abgelegt werden. So ein nicht eingebundener Formbinder kann als [Basis-Formelement](PartDesign_Body/de#Basis_Formelement.md) für einen neuen Körper verwendet werden.
-   Ein aus einer Skizze erstellter Formbinder kann eine umgekehrte \"Werkzeugausrichtung\" besitzen. Beispielsweise kann sich ein aus einer Skizze extrudierter [Block](PartDesign_Pad/de.md) in die positive Y-Richtung ausdehnen, während sich ein aus einem Formbinder extrudierter [Block](PartDesign_Pad/de.md) mit den gleichen Eigenschaften in die negative Y-Richtung ausdehnt. Durch umschalten der {{PropertyData/de|Reversed}} (oder der Checkbox) kann dies angeglichen werden.



## Vergleich PartDesign Teilformbinder und PartDesign Formbinder 

Siehe [Vergleich von PartDesign-Teilformbinder und PartDesign-Formbinder](PartDesign_SubShapeBinder/de#Vergleich_von_PartDesign_Teilformbinder_und_PartDesign_Formbinder.md).



## Eigenschaften

-    {{PropertyData/de|Trace Support}}: Der vorgegebene Wert ist false. Wenn diese Option auf true gesetzt ist, überwacht der Formbinder die relative Positionierung der Teile und Körper durch Änderung der Werte seiner verdeckten Eigenschaft {{PropertyData/de|Placement}}. Siehe das obige Beispiel, wie dies verwendet wird und funktioniert.



## Beispiel

Das Beispiel verwendet den Formbinder Funktion, um ein Loch (mit oder ohne Gewinde) durch mehr als einen Körper zu bohren. Normalerweise ist die Lochfunktion des Arbeitsbereichs Part Design auf einen einzigen Körper beschränkt. Das Beispiel verwendet zwei Würfel, die sich gegenüberliegen, aber willkürlich versetzt ausgerichtet sind. Die Löcher werden mit Skizzen erstellt, die für jedes Loch einen Kreis enthalten (Der Durchmesser wird von der Lochfunktion ignoriert). Wird die Skizze in den anderen Würfel kopiert, befindet sie sich an der gleichen Position im lokalen Koordinatensystem des Würfels. Im Bild ist dies durch den weißen Kreis auf dem hinteren Würfel dargestellt. Das ist nicht das, was wir wollen, denn das Loch an dieser Stelle würde nicht auf das Loch im vorderen Würfel ausgerichtet sein.

![](images/ShapeBinderThroughHole.png ) 
*Beispielaufbau für die Darstellung wie man Löcher durch unterschiedliche Körper erstellt. Der weiße Kreis zeigt, dass das Kopieren von Skizzen nicht ausreicht*

Und so wird das Formelement Formbinder verwendet, um das Ziel zu erreichen:

1.  Eine Szene wie im obigen Bild vorbereiten. Werden Würfel aus dem Arbeitsbereich [Part](Part_Workbench/de.md) verwendet, darf man nicht vergessen sie in einen \"Körper\" (Body-Objekt als Container) zu stecken. Jeweils einen in einen separaten Körper, andernfalls würden die [PartDesign](PartDesign_Workbench/de.md)-Funktionen nicht funktionieren. Werden sie aus Skizzen erstellt, sollte das System standardmäßig einen Körper erstellen.
2.  Im [Eigenschafteneditor](Property_editor/de.md) die Positionierung des zweiten Würfels so ändern, dass er den ersten Würfel berührt und seitlich versetzt ist.
3.  Zum Arbeitsbereich PartDesign wechseln.
4.  Eine Skizze auf der Vorderseite des ersten Würfels erstellen, darin an beliebiger Stelle einen Kreis hinzufügen und die Skizze schließen.
5.  Die Skizze im Baum auswählen und die Schaltfläche **<img src="images/PartDesign_Hole.svg" width=16px> [PartDesign-Bohrung](PartDesign_Hole/de.md)** drücken. Davor sollte man sicherstellen, dass der erste Körper der [aktive Körper](PartDesign_Body/de#Aktiver_Status.md) ist (ggf. mit Doppelklick aktivieren).
6.  Eine Bohrung in der passenden Größe auswählen. Im Bild oben ist zusätzlich eine Senkung ausgewählt. Die Funktion [Bohrung](PartDesign_Hole/de.md) schließen.

    :   Jetzt sollte das Bild wie oben aussehen. Wird der erste Würfel ausgewählt und mit der Leertaste ausgeblendet, wird ersichtlich, dass die Bohrung den zweiten Würfel nicht erreicht. Das wird sie auch dann nicht, wenn **Durch Alles** ausgewählt oder ein wirklich großer Abstand im Aufgabenbereich [Bohrung](PartDesign_Hole/de.md) eingegeben wird. Bohrung ist immer auf einen einzigen Körper beschränkt.
    :   Hier kommt nun der Formbinder ins Spiel.
7.  Zuerst den hinteren Würfel mit einem Doppelklick auswählen. Dieser ist das Ziel, zu dem der Formbinder hinzugefügt wird. Er muss vorher [aktiviert](PartDesign_Body/de#Aktiver_Status.md) worden sein (ggf. mit Doppelklick aktivieren).
8.  In der Baumansicht die Skizze auswählen, die für die Bohrung verwendet wurde. Es ist wichtig, den ersten Körper nicht zu aktivieren.
9.  Die Funktion Formbinder auswählen.

    :   Der Aufgabenbereich sollte sich öffnen. In der Zeile **Objekt** sollte der Name unserer Skizze sichtbar sein. Wurde die Funktion ausgewählt ohne vorher die Skizze auszuwählen, könnte jetzt **Objekt** angeklickt und dann die Skizze aus der Liste ausgewählt werden. Die erste Vorgehensweise (zuerst die Skizze auszuwählen) wird empfohlen, um die richtige auszuwählen, besonders wenn viele Skizzen mit automatisch generierten Namen wie Sketch001und folgende vorhanden sind. **Geometrie hinzufügen** ist hier nicht sinnvoll, da die ganze Skizze ausgewählt werden soll. **Geometrie hinzufügen** wird verwendet, wenn nur Teile (der Skizze) ausgewählt werden sollen.
10. Auf die Schaltfläche **OK** drücken, um den Aufgabenbereich zu schließen und anschließend überprüfen, ob ein neues Element zum Baum des zweiten Würfels hinzugefügt wurde.

    :   Wird die Sichtbarkeit des Formbinders umgeschaltet, wird er in der [3D-Ansicht](3D_view/de.md) gelb dargestellt. Allerdings ist er an der falschen Position, so wie der weiße Kreis im Bild oben. Dies liegt an der vorgegebenen Einstellung für den Trace-Parameter.
11. Im Eigenschafteneditor des Formbinders im Reiter Daten den Parameter **Trace Support** auf true setzen. Die Voreinstellung war false.

    :   Mit **Trace Support** auf true gesetzt wird der Formbinder nicht von lokalen Transformationen des Zielkörpers beeinflusst, z.B. unsere Verschiebung. Die Form bleibt genau dort, wo die ursprüngliche Form des vorderen Objekts gewesen ist. Versucht man, das vordere Objekt zu bewegen, sieht man, dass der Formbinder immer zur neuen Position folgt.
12. Den Formbinder in der Baumansicht auswählen und die Schaltfläche **<img src="images/PartDesign_Hole.svg" width=16px> [PartDesign-Bohrung](PartDesign_Hole/de.md)** drücken. Werden jetzt dieselben Werte wie für die Ausgangsbohrung eingegeben, erkennt man, dass im zweiten Würfel keine Bohrung erstellt wird. Dies liegt daran, dass ein Formbinder in einigen Fällen eine zur referenzierten Skizze umgekehrte \"Werkzeuausgrichtung\" aufweisen kann. Durch aktivieren der CheckBox Reverse kann die Ausrichtung angepasst werden. Zum Fertigstellen **OK** drücken.
13. Jetzt sind die Bohrungen in zwei unterschiedlichen Körpern verknüpft. Wird die Position des Kreises in der Skizze verändert, werden beide Bohrungen angepasst. Es können sogar neue Kreise zur Skizze hinzugefügt werden, um weitere verknüpfte Bohrungen zu erstellen.





{{PartDesign_Tools_ navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign ShapeBinder/de
